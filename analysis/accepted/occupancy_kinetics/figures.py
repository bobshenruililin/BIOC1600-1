#!/usr/bin/env python3
"""SVG figures for occupancy inversion and diffusion-limited clocks. All curves labeled BOUND/SIMULATION."""

from __future__ import annotations

import math
import xml.etree.ElementTree as ET
from pathlib import Path

from model import (
    C_CLEFT_M,
    C_TONIC_M,
    CONSTRUCTS,
    KON_DIFFUSION_M_S,
    occupancy,
    toff_diffusion_bound,
)

ROOT = Path(__file__).resolve().parent


def _line(x1, y1, x2, y2, stroke="#333", width="1"):
    return ET.Element(
        "line",
        attrib={"x1": str(x1), "y1": str(y1), "x2": str(x2), "y2": str(y2), "stroke": stroke, "stroke-width": width},
    )


def occupancy_svg() -> str:
    width, height = 720, 420
    svg = ET.Element("svg", attrib={"xmlns": "http://www.w3.org/2000/svg", "width": str(width), "height": str(height)})
    ET.SubElement(svg, "rect", attrib={"x": "0", "y": "0", "width": str(width), "height": str(height), "fill": "#fff"})
    title = ET.SubElement(svg, "text", attrib={"x": "20", "y": "24", "font-size": "14", "font-family": "sans-serif"})
    title.text = "1:1 occupancy vs [Glu] — SIMULATION using published Kd/EC50 as occupancy parameters"
    # log x from 1e-12 to 1e-2
    plot_x, plot_y, plot_w, plot_h = 70, 50, 500, 300

    def xmap(c):
        lg = (math.log10(c) - (-12)) / ( -2 - (-12))
        return plot_x + lg * plot_w

    def ymap(th):
        return plot_y + plot_h * (1 - th)

    ET.SubElement(svg, "rect", attrib={"x": str(plot_x), "y": str(plot_y), "width": str(plot_w), "height": str(plot_h), "fill": "#fafafa", "stroke": "#000"})
    colors = {"1d04_Kd_12uM": "#1f77b4", "Hu_apparent_1.8nM": "#d62728", "Xiao_SPR_293nM": "#2ca02c"}
    cs = [10 ** x for x in [i / 20 for i in range(-12 * 20, -2 * 20 + 1)]]
    for name, kd in CONSTRUCTS.items():
        pts = " ".join(f"{xmap(c):.2f},{ymap(occupancy(c, kd)):.2f}" for c in cs if c > 0)
        ET.SubElement(svg, "polyline", attrib={"points": pts, "fill": "none", "stroke": colors[name], "stroke-width": "2"})
    # tonic and cleft
    svg.append(_line(xmap(C_TONIC_M), plot_y, xmap(C_TONIC_M), plot_y + plot_h, "#666", "1"))
    svg.append(_line(xmap(C_CLEFT_M), plot_y, xmap(C_CLEFT_M), plot_y + plot_h, "#666", "1"))
    t1 = ET.SubElement(svg, "text", attrib={"x": str(xmap(C_TONIC_M) + 4), "y": str(plot_y + 14), "font-size": "10", "font-family": "sans-serif"})
    t1.text = "25 nM tonic"
    t2 = ET.SubElement(svg, "text", attrib={"x": str(xmap(C_CLEFT_M) - 80), "y": str(plot_y + 14), "font-size": "10", "font-family": "sans-serif"})
    t2.text = "1.1 mM cleft"
    # legend
    y = 70
    for name, kd in CONSTRUCTS.items():
        ET.SubElement(svg, "rect", attrib={"x": "590", "y": str(y), "width": "14", "height": "8", "fill": colors[name]})
        lab = ET.SubElement(svg, "text", attrib={"x": "608", "y": str(y + 9), "font-size": "10", "font-family": "sans-serif"})
        th_t = occupancy(C_TONIC_M, kd)
        lab.text = f"{name} θ(25 nM)={th_t:.3f}"
        y += 18
    note = ET.SubElement(svg, "text", attrib={"x": "20", "y": "400", "font-size": "10", "font-family": "sans-serif", "fill": "#444"})
    note.text = "LOD values are not plotted here. 1.8 nM is Hu electrochemical apparent Kd (EC50), not a proven molecular Kd. 10–90% span is 81-fold for each curve."
    return ET.tostring(svg, encoding="unicode")


def clocks_svg() -> str:
    width, height = 720, 320
    svg = ET.Element("svg", attrib={"xmlns": "http://www.w3.org/2000/svg", "width": str(width), "height": str(height)})
    ET.SubElement(svg, "rect", attrib={"x": "0", "y": "0", "width": str(width), "height": str(height), "fill": "#fff"})
    title = ET.SubElement(svg, "text", attrib={"x": "20", "y": "24", "font-size": "14", "font-family": "sans-serif"})
    title.text = "Time clocks — BOUND vs MEASURED vs INFERENCE (log10 seconds)"
    items = [
        ("cleft τ 1.2 ms (inference)", 1.2e-3, "#000"),
        ("1d04 t_off BOUND @ kon=1e8", toff_diffusion_bound(CONSTRUCTS["1d04_Kd_12uM"]), "#1f77b4"),
        ("Xiao t_off BOUND @ kon=1e8", toff_diffusion_bound(CONSTRUCTS["Xiao_SPR_293nM"]), "#2ca02c"),
        ("Hu t_off BOUND @ kon=1e8", toff_diffusion_bound(CONSTRUCTS["Hu_apparent_1.8nM"]), "#d62728"),
        ("GlutOx 500 ms (enzyme, measured)", 0.5, "#9467bd"),
        ("Xiao FET stabilize 200 s (measured)", 200.0, "#8c564b"),
        ("Hu Glu ACV wait 15 min (measured)", 900.0, "#e377c2"),
    ]
    plot_x, plot_y, plot_w, plot_h = 200, 50, 480, 220
    tmin, tmax = 1e-4, 2e3

    def xmap(t):
        lg = (math.log10(t) - math.log10(tmin)) / (math.log10(tmax) - math.log10(tmin))
        return plot_x + lg * plot_w

    ET.SubElement(svg, "rect", attrib={"x": str(plot_x), "y": str(plot_y), "width": str(plot_w), "height": str(plot_h), "fill": "#fafafa", "stroke": "#000"})
    for i, (lab, t, color) in enumerate(items):
        y = plot_y + 18 + i * 28
        svg.append(_line(xmap(t), y - 6, xmap(t), y + 6, color, "3"))
        tx = ET.SubElement(svg, "text", attrib={"x": "16", "y": str(y + 4), "font-size": "11", "font-family": "sans-serif", "fill": color})
        tx.text = lab
    foot = ET.SubElement(svg, "text", attrib={"x": "20", "y": "300", "font-size": "10", "font-family": "sans-serif", "fill": "#444"})
    foot.text = f"BOUND uses kon={KON_DIFFUSION_M_S:.0e} M^-1 s^-1 × Kd. Not a glutamate kon. Tobramycin IPA 2 ms interrogation is omitted so it cannot be misread as Glu koff."
    return ET.tostring(svg, encoding="unicode")


def main() -> None:
    out = ROOT / "figures"
    out.mkdir(exist_ok=True)
    (out / "occupancy.svg").write_text(occupancy_svg(), encoding="utf-8")
    (out / "clocks.svg").write_text(clocks_svg(), encoding="utf-8")
    (out / "CAPTION.md").write_text(
        "Figure occupancy: Langmuir θ([Glu]) using three published numbers as occupancy Kd/EC50. "
        "SIMULATION/illustration. Vertical lines mark Herman 25 nM and Clements 1.1 mM. "
        "Hu 1.8 nM is an electrochemical apparent Kd. LOD is not occupancy.\n\n"
        "Figure clocks: log time. Cleft τ is inference. t_off values are diffusion-limited BOUNDS, "
        "not measured glutamate koff. Hu 15 min and Xiao 200 s are measured protocol times. "
        "GlutOx 500 ms is an enzyme comparator, not an aptamer.\n",
        encoding="utf-8",
    )
    print(out / "occupancy.svg")
    print(out / "clocks.svg")


if __name__ == "__main__":
    main()
