#!/usr/bin/env python3
"""Construct × quantity-type atlas. Empty cells stay empty."""

from __future__ import annotations

import argparse
import csv
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def find_repo(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "research/evidence/core_evidence.csv").is_file():
            return candidate
    raise FileNotFoundError("core_evidence.csv not found above " + str(start))


REPO = find_repo(ROOT)
DEFAULT_CSV = REPO / "research/evidence/core_evidence.csv"

# Smallest set that determines the story. Ledger evidence_ids only.
SELECTED = {
    ("1d04 isolate", "Kd_molecular"): ("E001", "12 µM"),
    ("glu1 E-AB", "sensor_LOD"): ("E002", "0.0013 pM"),
    ("Hu Glu-apt surface", "EC50"): ("E004", "1.8 nM"),
    ("Hu Glu-apt surface", "sensor_LOD"): ("E005", "32 pM PBS"),
    ("Hu Glu-apt surface", "measurement_time"): ("E008", "15 min"),
    ("Xiao SPR oligo", "Kd_molecular"): ("E024", "293 nM"),
    ("Xiao CNT FET", "sensor_LOD"): ("E025", "10 fM"),
    ("Xiao CNT FET", "response_time"): ("E027", "200 s"),
    ("cleft inference", "biological_concentration_range"): ("E032", "1.1 mM"),
    ("cleft inference", "response_time"): ("E033", "1.2 ms"),
    ("slice ambient", "biological_concentration_range"): ("E034", "25 nM"),
}

ROWS = [
    "1d04 isolate",
    "glu1 E-AB",
    "Hu Glu-apt surface",
    "Xiao SPR oligo",
    "Xiao CNT FET",
    "cleft inference",
    "slice ambient",
]

COLS = [
    "Kd_molecular",
    "EC50",
    "sensor_LOD",
    "kon",
    "koff",
    "measurement_time",
    "response_time",
    "biological_concentration_range",
]


def load_ledger(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["evidence_id"]: row for row in csv.DictReader(handle)}


def cell_text(eid: str, fallback: str, ledger: dict[str, dict[str, str]]) -> str:
    row = ledger.get(eid)
    if not row:
        return fallback
    value = (row.get("numerical_result") or "").strip()
    units = (row.get("units") or "").strip()
    if not value:
        return ""
    return f"{value} {units}".strip()


def build_grid(ledger: dict[str, dict[str, str]]) -> dict[tuple[str, str], str]:
    grid: dict[tuple[str, str], str] = {}
    for (construct, qtype), (eid, fallback) in SELECTED.items():
        grid[(construct, qtype)] = cell_text(eid, fallback, ledger)
    return grid


def svg(grid: dict[tuple[str, str], str]) -> str:
    col_w = 118
    row_h = 36
    left = 170
    top = 48
    width = left + col_w * len(COLS) + 16
    height = top + row_h * len(ROWS) + 64
    svg_el = ET.Element(
        "svg",
        attrib={
            "xmlns": "http://www.w3.org/2000/svg",
            "width": str(width),
            "height": str(height),
            "viewBox": f"0 0 {width} {height}",
        },
    )
    ET.SubElement(svg_el, "rect", attrib={"x": "0", "y": "0", "width": str(width), "height": str(height), "fill": "#fff"})
    title = ET.SubElement(svg_el, "text", attrib={"x": "12", "y": "22", "font-size": "14", "font-family": "sans-serif"})
    title.text = "Glutamate story atlas — empty cells are empty (not unknown-filled)"
    for j, col in enumerate(COLS):
        t = ET.SubElement(
            svg_el,
            "text",
            attrib={
                "x": str(left + j * col_w + 4),
                "y": str(top - 8),
                "font-size": "9",
                "font-family": "sans-serif",
            },
        )
        t.text = col
    for i, row in enumerate(ROWS):
        y = top + i * row_h
        lab = ET.SubElement(svg_el, "text", attrib={"x": "8", "y": str(y + 22), "font-size": "11", "font-family": "sans-serif"})
        lab.text = row
        for j, col in enumerate(COLS):
            x = left + j * col_w
            val = grid.get((row, col), "")
            fill = "#d9ead3" if val else "#f3f3f3"
            ET.SubElement(
                svg_el,
                "rect",
                attrib={
                    "x": str(x),
                    "y": str(y),
                    "width": str(col_w - 4),
                    "height": str(row_h - 4),
                    "fill": fill,
                    "stroke": "#333",
                    "stroke-width": "0.6",
                },
            )
            if val:
                tx = ET.SubElement(
                    svg_el,
                    "text",
                    attrib={
                        "x": str(x + 6),
                        "y": str(y + 22),
                        "font-size": "10",
                        "font-family": "sans-serif",
                    },
                )
                tx.text = val
            else:
                tx = ET.SubElement(
                    svg_el,
                    "text",
                    attrib={
                        "x": str(x + 6),
                        "y": str(y + 22),
                        "font-size": "10",
                        "font-family": "sans-serif",
                        "fill": "#888",
                    },
                )
                tx.text = "—"
    foot = ET.SubElement(
        svg_el,
        "text",
        attrib={"x": "12", "y": str(height - 18), "font-size": "10", "font-family": "sans-serif", "fill": "#444"},
    )
    foot.text = "kon/koff on glutamate aptamer rows are empty because none were found. Not-glutamate IPA/ITC rates are omitted on purpose."
    return ET.tostring(svg_el, encoding="unicode")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()
    ledger = load_ledger(args.csv)
    grid = build_grid(ledger)
    out = ROOT / "figures"
    out.mkdir(exist_ok=True)
    (out / "atlas.svg").write_text(svg(grid), encoding="utf-8")
    (out / "CAPTION.md").write_text(
        "Figure: Construct-by-quantity atlas from `core_evidence.csv`. "
        "Green cells copy ledger numbers; grey em-dashes are empty. "
        "This is not a heatmap of affinity. kon/koff are empty for glutamate constructs. "
        "Cleft 1.2 ms is a kinetic inference stored under response_time, not a sensor specification.\n",
        encoding="utf-8",
    )
    print(out / "atlas.svg")


if __name__ == "__main__":
    main()
