#!/usr/bin/env python3
"""MODELED Langmuir–Freundlich span vs n. Not a fitted n. Not a flagship."""

from __future__ import annotations

import csv
import math
import xml.etree.ElementTree as ET
from pathlib import Path

from model import (
    C_HERMAN_SLICE_M,
    HERMAN_CLEMENTS_RATIO,
    KD_HU_AUED_MEA_APPARENT_M,
    lf_occupancy,
    lf_span_ratio,
    n_for_herman_clements_span,
)

ROOT = Path(__file__).resolve().parent
N_GRID = (0.30, 0.40, 0.411, 0.50, 0.70, 1.00, 1.50, 2.00)


def _text(svg, x, y, s, size="12", anchor="start", weight="normal"):
    t = ET.SubElement(
        svg,
        "text",
        attrib={
            "x": str(x),
            "y": str(y),
            "font-size": size,
            "font-family": "sans-serif",
            "font-weight": weight,
            "text-anchor": anchor,
            "fill": "#111",
        },
    )
    t.text = s
    return t


def span_vs_n_svg() -> str:
    width, height = 760, 460
    svg = ET.Element("svg", attrib={"xmlns": "http://www.w3.org/2000/svg", "width": str(width), "height": str(height)})
    ET.SubElement(svg, "rect", attrib={"x": "0", "y": "0", "width": str(width), "height": str(height), "fill": "#fff"})
    _text(svg, 20, 22, "MODELED: Langmuir–Freundlich 10–90% span = 81^(1/n)", size="14", weight="bold")
    _text(svg, 20, 40, "Hu n is unpublished. Herman/Clements 44000-fold is a labeled literature-example ratio, not a device spec.", size="11")

    plot_x, plot_y, plot_w, plot_h = 70, 60, 520, 300
    ET.SubElement(
        svg,
        "rect",
        attrib={"x": str(plot_x), "y": str(plot_y), "width": str(plot_w), "height": str(plot_h), "fill": "#fafafa", "stroke": "#000"},
    )
    n_min, n_max = 0.28, 2.15
    span_min, span_max = math.log10(6), math.log10(2e5)

    def xmap(n):
        return plot_x + (n - n_min) / (n_max - n_min) * plot_w

    def ymap(span):
        lg = (math.log10(span) - span_min) / (span_max - span_min)
        return plot_y + plot_h * (1 - lg)

    ns = [n_min + i * (n_max - n_min) / 80 for i in range(81)]
    pts = " ".join(f"{xmap(n):.2f},{ymap(lf_span_ratio(n)):.2f}" for n in ns)
    ET.SubElement(svg, "polyline", attrib={"points": pts, "fill": "none", "stroke": "#1d4ed8", "stroke-width": "2.5"})

    y81 = ymap(81)
    y44 = ymap(HERMAN_CLEMENTS_RATIO)
    ET.SubElement(svg, "line", attrib={"x1": str(plot_x), "y1": str(y81), "x2": str(plot_x + plot_w), "y2": str(y81), "stroke": "#111", "stroke-dasharray": "6 4"})
    ET.SubElement(svg, "line", attrib={"x1": str(plot_x), "y1": str(y44), "x2": str(plot_x + plot_w), "y2": str(y44), "stroke": "#b45309", "stroke-dasharray": "6 4"})
    n_star = n_for_herman_clements_span()
    ET.SubElement(
        svg,
        "circle",
        attrib={"cx": str(xmap(n_star)), "cy": str(y44), "r": "5", "fill": "#b45309", "stroke": "#111"},
    )
    _text(svg, plot_x + plot_w + 8, y81 + 4, "81-fold (n=1)", size="11")
    _text(svg, plot_x + plot_w + 8, y44 + 4, "44000-fold example", size="11")
    _text(svg, xmap(n_star) - 10, y44 - 12, f"n*≈{n_star:.3f}", size="11", anchor="end")

    for tick in (0.5, 1.0, 1.5, 2.0):
        x = xmap(tick)
        ET.SubElement(svg, "line", attrib={"x1": str(x), "y1": str(plot_y + plot_h), "x2": str(x), "y2": str(plot_y + plot_h + 6), "stroke": "#111"})
        _text(svg, x, plot_y + plot_h + 20, str(tick), size="11", anchor="middle")
    for span in (10, 81, 1000, 44000, 1e5):
        y = ymap(span)
        ET.SubElement(svg, "line", attrib={"x1": str(plot_x - 6), "y1": str(y), "x2": str(plot_x), "y2": str(y), "stroke": "#111"})
        _text(svg, plot_x - 10, y + 4, f"{span:g}", size="10", anchor="end")

    _text(svg, plot_x + plot_w / 2, height - 28, "heterogeneity exponent n (UNKNOWN for Hu)", size="12", anchor="middle")
    _text(svg, 16, plot_y + plot_h / 2, "10–90% span", size="12", anchor="middle")
    # rotate-ish label via extra text at left
    stamp = ET.SubElement(
        svg,
        "rect",
        attrib={"x": "20", "y": str(height - 52), "width": "200", "height": "28", "fill": "#fef3c7", "stroke": "#111", "stroke-width": "2"},
    )
    _ = stamp
    _text(svg, 120, height - 33, "MODELED — n unmeasured", size="12", anchor="middle", weight="bold")
    return ET.tostring(svg, encoding="unicode")


def write_table() -> None:
    path = ROOT / "tables" / "lf_n_span.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    n_star = n_for_herman_clements_span()
    rows = []
    for n in N_GRID:
        span = lf_span_ratio(n)
        th = lf_occupancy(C_HERMAN_SLICE_M, KD_HU_AUED_MEA_APPARENT_M, n)
        rows.append(
            {
                "n": f"{n:.3f}",
                "span_10_90": f"{span:.6g}",
                "span_vs_44000_example": "wider" if span >= HERMAN_CLEMENTS_RATIO - 1e-6 else "narrower",
                "overlay_theta_25nM_if_1p8nM_c50": f"{th:.4f}",
                "quantity_class": "MODELED",
            }
        )
    rows.append(
        {
            "n": f"{n_star:.6f}",
            "span_10_90": f"{HERMAN_CLEMENTS_RATIO:.6g}",
            "span_vs_44000_example": "equal (critical n*)",
            "overlay_theta_25nM_if_1p8nM_c50": f"{lf_occupancy(C_HERMAN_SLICE_M, KD_HU_AUED_MEA_APPARENT_M, n_star):.4f}",
            "quantity_class": "MODELED",
        }
    )
    with path.open("w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["n", "span_10_90", "span_vs_44000_example", "overlay_theta_25nM_if_1p8nM_c50", "quantity_class"],
        )
        w.writeheader()
        w.writerows(rows)


def write_caption() -> None:
    n_star = n_for_herman_clements_span()
    text = f"""# Caption — lf_n_span.svg

MODELED. For a Langmuir–Freundlich isotherm with unpublished heterogeneity exponent n, the concentration ratio between 10% and 90% occupancy is exactly 81^(1/n), independent of Kd. At n = 1 this is the canonical 81-fold 1:1 identity. The orange dashed line is the 44000-fold ratio of two named hippocampal literature examples (Herman ~25 nM in acute slice; Clements ~1.1 mM inferred at cultured synapses). Those poles are not a retinal range and not a device specification. They would sit inside a 10–90% window only if n ≤ {n_star:.3f}. Hu's n is UNKNOWN. The overlay column in the companion table is a 1.8 nM AuED-MEA apparent c50 treated as if it were occupancy c50 at 25 nM — not PaC-probe tissue occupancy.

Do not read this figure as restoring the withdrawn 81-versus-44000 flagship. It shows why that comparison is n-sensitive.
"""
    (ROOT / "figures" / "CAPTION.md").write_text(text, encoding="utf-8")


def main() -> None:
    fig_dir = ROOT / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    (fig_dir / "lf_n_span.svg").write_text(span_vs_n_svg(), encoding="utf-8")
    write_caption()
    write_table()
    print("wrote figures/lf_n_span.svg, figures/CAPTION.md, tables/lf_n_span.csv")


if __name__ == "__main__":
    main()
