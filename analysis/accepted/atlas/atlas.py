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
    ("Hu Glu-apt 50% serum", "sensor_LOD"): ("E006", "51.5 pM 50% serum"),
    ("Hu Glu-apt surface", "measurement_time"): ("E008", "15 min"),
    ("Xiao SPR oligo", "Kd_molecular"): ("E024", "293 nM"),
    ("Xiao CNT FET", "sensor_LOD"): ("E025", "10 fM"),
    ("Xiao CNT FET", "response_time"): ("E027", "200 s"),
    ("cleft inference", "biological_concentration_range"): ("E032", "1.1 mM"),
    ("cleft inference", "response_time"): ("E033", "1.2 ms"),
    ("slice ambient", "biological_concentration_range"): ("E034", "25 nM"),
    ("Hu retina probe thesis", "measurement_time"): ("E042", "10 min"),
    ("Hu retina probe thesis", "sensor_LOD"): ("E043", "0.3 pM"),
}

ROWS = [
    "1d04 isolate",
    "glu1 E-AB",
    "Hu Glu-apt surface",
    "Hu Glu-apt 50% serum",
    "Xiao SPR oligo",
    "Xiao CNT FET",
    "cleft inference",
    "slice ambient",
    "Hu retina probe thesis",
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
    matrix = (row.get("matrix") or "").strip()
    if not value:
        return ""
    core = f"{value} {units}".strip()
    fallback_norm = fallback.replace("µ", "u")
    core_norm = core.replace("µ", "u")
    if fallback and core_norm in fallback_norm:
        return fallback
    if "serum" in matrix.lower() and "serum" not in core.lower():
        return f"{core} 50% serum"
    if "PBS" in matrix and "PBS" not in core:
        return f"{core} PBS"
    return core


def build_grid(ledger: dict[str, dict[str, str]]) -> dict[tuple[str, str], str]:
    grid: dict[tuple[str, str], str] = {}
    for (construct, qtype), (eid, fallback) in SELECTED.items():
        grid[(construct, qtype)] = cell_text(eid, fallback, ledger)
    return grid


def svg(grid: dict[tuple[str, str], str]) -> str:
    col_w = 118
    row_h = 36
    left = 170
    top = 72
    width = left + col_w * len(COLS) + 16
    height = top + row_h * len(ROWS) + 64 + 36
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
    for x, label, fill in (
        (12, "MEASURED", "#b7e4c7"),
        (132, "MODELED", "#90e0ef"),
        (252, "UNKNOWN", "#d3d3d3"),
        (372, "PROPOSED", "#ffd166"),
    ):
        ET.SubElement(
            svg_el,
            "rect",
            attrib={"x": str(x), "y": "6", "width": "110", "height": "22", "fill": fill, "stroke": "#111", "stroke-width": "1"},
        )
        st = ET.SubElement(
            svg_el,
            "text",
            attrib={"x": str(x + 55), "y": "22", "font-size": "11", "font-family": "sans-serif", "font-weight": "bold", "text-anchor": "middle"},
        )
        st.text = label
    title = ET.SubElement(svg_el, "text", attrib={"x": "12", "y": "48", "font-size": "14", "font-family": "sans-serif"})
    title.text = "Glutamate story atlas — selected subset; glutamate kon/koff stay empty"
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
    foot.text = "Glutamate kon/koff stay empty (none found). Other grey dashes may be curated omissions, not genuine empties. Not-glutamate IPA/ITC rates omitted on purpose."
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
        "Figure: Construct-by-quantity atlas from a selected subset of `core_evidence.csv`. "
        "Green cells copy those selected ledger numbers. Grey em-dashes are not all genuine empties: "
        "some are curated omissions (quantities present in the ledger but not selected for this grid). "
        "Glutamate kon/koff cells stay empty (none found). "
        "This is not a heatmap of affinity. "
        "Hu 32 pM is PBS (E005); 51.5 pM is 50% serum (E006); 0.3 pM is PaC PBS (E043), not Ames. "
        "Cleft 1.2 ms is a kinetic inference stored under response_time, not a sensor specification.\n",
        encoding="utf-8",
    )
    print(out / "atlas.svg")


if __name__ == "__main__":
    main()
