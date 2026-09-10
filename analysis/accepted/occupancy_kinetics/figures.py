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
    KON_ITC_HIGH_M_S,
    KON_ITC_LOW_M_S,
    KON_TOBRAMYCIN_IPA_M_S,
    occupancy,
    tau_eq,
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


def sensitivity_svg() -> str:
    """t_off vs kon. Empirical SM-aptamer kon band is NOT glutamate."""
    width, height = 720, 420
    svg = ET.Element("svg", attrib={"xmlns": "http://www.w3.org/2000/svg", "width": str(width), "height": str(height)})
    ET.SubElement(svg, "rect", attrib={"x": "0", "y": "0", "width": str(width), "height": str(height), "fill": "#fff"})
    title = ET.SubElement(svg, "text", attrib={"x": "20", "y": "24", "font-size": "14", "font-family": "sans-serif"})
    title.text = "t_off = 1/(kon Kd) vs kon — SIMULATION/BOUND; empirical band is NOT glutamate"
    plot_x, plot_y, plot_w, plot_h = 70, 48, 500, 300
    kmin, kmax = 10.0, 1e9
    tmin, tmax = 1e-4, 1e4

    def xmap(k):
        lg = (math.log10(k) - math.log10(kmin)) / (math.log10(kmax) - math.log10(kmin))
        return plot_x + lg * plot_w

    def ymap(t):
        lg = (math.log10(t) - math.log10(tmin)) / (math.log10(tmax) - math.log10(tmin))
        return plot_y + plot_h * (1 - lg)

    ET.SubElement(svg, "rect", attrib={"x": str(plot_x), "y": str(plot_y), "width": str(plot_w), "height": str(plot_h), "fill": "#fafafa", "stroke": "#000"})
    # empirical band C010
    ET.SubElement(
        svg,
        "rect",
        attrib={
            "x": str(xmap(KON_ITC_LOW_M_S)),
            "y": str(plot_y),
            "width": str(xmap(KON_ITC_HIGH_M_S) - xmap(KON_ITC_LOW_M_S)),
            "height": str(plot_h),
            "fill": "#ffe6cc",
            "opacity": "0.9",
        },
    )
    colors = {"1d04_Kd_12uM": "#1f77b4", "Hu_apparent_1.8nM": "#d62728", "Xiao_SPR_293nM": "#2ca02c"}
    kons = [10 ** (i / 10) for i in range(10, 91)]
    for name, kd in CONSTRUCTS.items():
        pts = " ".join(f"{xmap(k):.2f},{ymap(toff_diffusion_bound(kd, k)):.2f}" for k in kons)
        ET.SubElement(svg, "polyline", attrib={"points": pts, "fill": "none", "stroke": colors[name], "stroke-width": "2"})
    svg.append(_line(xmap(KON_DIFFUSION_M_S), plot_y, xmap(KON_DIFFUSION_M_S), plot_y + plot_h, "#444", "1"))
    svg.append(_line(xmap(KON_TOBRAMYCIN_IPA_M_S), plot_y, xmap(KON_TOBRAMYCIN_IPA_M_S), plot_y + plot_h, "#9467bd", "1"))
    svg.append(_line(plot_x, ymap(1.2e-3), plot_x + plot_w, ymap(1.2e-3), "#000", "1"))
    lab1 = ET.SubElement(svg, "text", attrib={"x": str(xmap(KON_ITC_LOW_M_S) + 4), "y": str(plot_y + 14), "font-size": "9", "font-family": "sans-serif"})
    lab1.text = "C010 ITC kon envelope (NOT Glu)"
    lab2 = ET.SubElement(svg, "text", attrib={"x": str(xmap(KON_TOBRAMYCIN_IPA_M_S) + 4), "y": str(plot_y + 28), "font-size": "9", "font-family": "sans-serif", "fill": "#9467bd"})
    lab2.text = "C008 tobramycin IPA"
    lab3 = ET.SubElement(svg, "text", attrib={"x": str(xmap(KON_DIFFUSION_M_S) - 110), "y": str(plot_y + 42), "font-size": "9", "font-family": "sans-serif"})
    lab3.text = "1e8 diffusion ceiling"
    lab4 = ET.SubElement(svg, "text", attrib={"x": str(plot_x + 6), "y": str(ymap(1.2e-3) - 4), "font-size": "9", "font-family": "sans-serif"})
    lab4.text = "1.2 ms cleft tau (inference)"
    y = 70
    for name, kd in CONSTRUCTS.items():
        ET.SubElement(svg, "rect", attrib={"x": "590", "y": str(y), "width": "14", "height": "8", "fill": colors[name]})
        lab = ET.SubElement(svg, "text", attrib={"x": "608", "y": str(y + 9), "font-size": "10", "font-family": "sans-serif"})
        lab.text = name
        y += 16
    note = ET.SubElement(svg, "text", attrib={"x": "20", "y": "400", "font-size": "10", "font-family": "sans-serif", "fill": "#444"})
    t_1d04_emp = toff_diffusion_bound(CONSTRUCTS["1d04_Kd_12uM"], KON_ITC_HIGH_M_S)
    t_rise = tau_eq(C_CLEFT_M, CONSTRUCTS["1d04_Kd_12uM"], KON_ITC_HIGH_M_S)
    note.text = (
        f"At C010 high-end kon={KON_ITC_HIGH_M_S:.0e} (NOT Glu): 1d04 t_off={t_1d04_emp:.2f} s, "
        f"tau_eq(1.1 mM)={t_rise*1e3:.1f} ms. Rising-edge FoM != falling-edge t_off."
    )
    return ET.tostring(svg, encoding="unicode")


def write_table(path) -> None:
    import csv

    rows = []
    for name, kd in CONSTRUCTS.items():
        for label, kon in [
            ("diffusion_ceiling_1e8", KON_DIFFUSION_M_S),
            ("C010_ITC_high_2e5_NOT_Glu", KON_ITC_HIGH_M_S),
            ("C008_tobramycin_IPA_3.5e4_NOT_Glu", KON_TOBRAMYCIN_IPA_M_S),
            ("C010_ITC_low_96_NOT_Glu", KON_ITC_LOW_M_S),
        ]:
            rows.append(
                {
                    "construct": name,
                    "occupancy_parameter_M": f"{kd:.3e}",
                    "kon_assumption": label,
                    "kon_M_s": f"{kon:.3e}",
                    "theta_25nM": f"{occupancy(C_TONIC_M, kd):.4f}",
                    "theta_1.1mM": f"{occupancy(C_CLEFT_M, kd):.4f}",
                    "t_off_s": f"{toff_diffusion_bound(kd, kon):.4e}",
                    "tau_eq_cleft_s": f"{tau_eq(C_CLEFT_M, kd, kon):.4e}",
                    "label": "SIMULATION/BOUND",
                }
            )
    path.parent.mkdir(exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    out = ROOT / "figures"
    out.mkdir(exist_ok=True)
    (out / "occupancy.svg").write_text(occupancy_svg(), encoding="utf-8")
    (out / "clocks.svg").write_text(clocks_svg(), encoding="utf-8")
    (out / "sensitivity.svg").write_text(sensitivity_svg(), encoding="utf-8")
    write_table(ROOT / "tables" / "occupancy_table.csv")
    (out / "CAPTION.md").write_text(
        "Figure occupancy: Langmuir θ([Glu]) using three published numbers as occupancy Kd/EC50. "
        "SIMULATION/illustration. Vertical lines mark Herman 25 nM and Clements 1.1 mM. "
        "Hu 1.8 nM is an electrochemical apparent Kd (Langmuir–Freundlich), not a 1:1 molecular Kd. "
        "LOD is not occupancy.\n\n"
        "Figure clocks: log time. Cleft τ is inference. t_off values are diffusion-limited BOUNDS, "
        "not measured glutamate koff. Hu 15 min and Xiao 200 s are measured protocol times. "
        "GlutOx 500 ms is an enzyme comparator, not an aptamer.\n\n"
        "Figure sensitivity: t_off vs assumed kon. Orange band is Ding ITC kon endpoints (C010) "
        "and the purple line is tobramycin IPA kon (C008). Those rates are NOT glutamate. "
        "If they applied, even 12 µM t_off is seconds, not 0.8 ms. Rising-edge tau_eq at 1.1 mM "
        "can still be milliseconds because tau_eq = 1/(kon c + koff). BOUND/SIMULATION.\n",
        encoding="utf-8",
    )
    print(out / "occupancy.svg")
    print(out / "clocks.svg")
    print(out / "sensitivity.svg")


if __name__ == "__main__":
    main()
