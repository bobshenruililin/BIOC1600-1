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
    langmuir_span_10_90,
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


def _stamp(svg, x, y, w, h, label, fill):
    ET.SubElement(
        svg,
        "rect",
        attrib={
            "x": str(x),
            "y": str(y),
            "width": str(w),
            "height": str(h),
            "fill": fill,
            "stroke": "#111",
            "stroke-width": "2",
        },
    )
    lab = ET.SubElement(
        svg,
        "text",
        attrib={
            "x": str(x + w / 2),
            "y": str(y + h / 2 + 5),
            "font-size": "16",
            "font-family": "sans-serif",
            "font-weight": "bold",
            "text-anchor": "middle",
            "fill": "#111",
        },
    )
    lab.text = label


def occupancy_svg() -> str:
    width, height = 720, 420
    svg = ET.Element("svg", attrib={"xmlns": "http://www.w3.org/2000/svg", "width": str(width), "height": str(height)})
    ET.SubElement(svg, "rect", attrib={"x": "0", "y": "0", "width": str(width), "height": str(height), "fill": "#fff"})
    title = ET.SubElement(svg, "text", attrib={"x": "20", "y": "24", "font-size": "14", "font-family": "sans-serif"})
    title.text = "DEMOTED 1:1 overlay SIMULATION — advertised Kd/EC50, not tissue occupancy, not PaC Kd"
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
    t1 = ET.SubElement(svg, "text", attrib={"x": str(xmap(C_TONIC_M) + 4), "y": str(plot_y + 14), "font-size": "9", "font-family": "sans-serif"})
    t1.text = "25 nM Herman (hippocampal slice literature)"
    t2 = ET.SubElement(svg, "text", attrib={"x": str(xmap(C_CLEFT_M) - 150), "y": str(plot_y + 14), "font-size": "9", "font-family": "sans-serif"})
    t2.text = "1.1 mM Clements (cultured hippocampal inference)"
    _stamp(svg, 560, 48, 150, 28, "MODELED", "#90e0ef")
    y = 88
    legend_names = {
        "1d04_Kd_12uM": "1d04 12 µM (abstract Kd)",
        "Hu_apparent_1.8nM": "AuED-MEA LF 1.8 nM (not PaC)",
        "Xiao_SPR_293nM": "Xiao SPR 293 nM",
    }
    for name, kd in CONSTRUCTS.items():
        ET.SubElement(svg, "rect", attrib={"x": "590", "y": str(y), "width": "14", "height": "8", "fill": colors[name]})
        lab = ET.SubElement(svg, "text", attrib={"x": "608", "y": str(y + 9), "font-size": "9", "font-family": "sans-serif"})
        lab.text = legend_names[name]
        y += 16
    unk = ET.SubElement(svg, "text", attrib={"x": "590", "y": str(y + 18), "font-size": "10", "font-family": "sans-serif", "font-weight": "bold"})
    unk.text = "PaC θ UNKNOWN"
    note = ET.SubElement(svg, "text", attrib={"x": "20", "y": "400", "font-size": "10", "font-family": "sans-serif", "fill": "#444"})
    note.text = "Overlay math only. Not tissue occupancy. 1.8 nM is AuED-MEA Langmuir–Freundlich apparent Kd in PBS, not 1:1 molecular Kd of the retina probe."
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


def span_identity_svg() -> str:
    """Flagship: 81-fold 1:1 identity vs hippocampal literature examples. No PaC occupancy number."""
    width, height = 900, 500
    svg = ET.Element("svg", attrib={"xmlns": "http://www.w3.org/2000/svg", "width": str(width), "height": str(height)})
    ET.SubElement(svg, "rect", attrib={"x": "0", "y": "0", "width": str(width), "height": str(height), "fill": "#fff"})
    title = ET.SubElement(svg, "text", attrib={"x": "20", "y": "28", "font-size": "18", "font-family": "sans-serif", "font-weight": "bold"})
    title.text = "1:1 Langmuir 10–90% span is 81-fold — a design principle, not a retinal occupancy measurement"
    _stamp(svg, 20, 44, 150, 32, "MEASURED", "#b7e4c7")
    _stamp(svg, 180, 44, 150, 32, "MODELED", "#90e0ef")
    _stamp(svg, 340, 44, 150, 32, "UNKNOWN", "#d3d3d3")
    _stamp(svg, 500, 44, 150, 32, "PROPOSED", "#ffd166")
    plot_x, plot_y, plot_w, plot_h = 70, 130, 680, 220

    def xmap(c):
        lg = (math.log10(c) - (-11)) / (-2 - (-11))
        return plot_x + lg * plot_w

    ET.SubElement(
        svg,
        "rect",
        attrib={"x": str(plot_x), "y": str(plot_y), "width": str(plot_w), "height": str(plot_h), "fill": "#f7f7f7", "stroke": "#111"},
    )
    # Sliding 81-fold ruler placed at a generic 1 µM Kd so it cannot be read as Hu 1.8 nM occupancy.
    kd_generic = 1.0e-6
    c10, c90, _ = langmuir_span_10_90(kd_generic)
    band_x = xmap(c10)
    band_w = xmap(c90) - xmap(c10)
    ET.SubElement(
        svg,
        "rect",
        attrib={
            "x": str(band_x),
            "y": str(plot_y + 40),
            "width": str(band_w),
            "height": "80",
            "fill": "#90e0ef",
            "stroke": "#0077b6",
            "stroke-width": "3",
            "opacity": "0.85",
        },
    )
    band_lab = ET.SubElement(
        svg,
        "text",
        attrib={
            "x": str(band_x + band_w / 2),
            "y": str(plot_y + 85),
            "font-size": "16",
            "font-family": "sans-serif",
            "font-weight": "bold",
            "text-anchor": "middle",
        },
    )
    band_lab.text = "81-fold 10–90%  MODELED"
    band_sub = ET.SubElement(
        svg,
        "text",
        attrib={
            "x": str(band_x + band_w / 2),
            "y": str(plot_y + 105),
            "font-size": "11",
            "font-family": "sans-serif",
            "text-anchor": "middle",
        },
    )
    band_sub.text = "slides with any 1:1 Kd; not this device's fitted window"
    svg.append(_line(xmap(C_TONIC_M), plot_y, xmap(C_TONIC_M), plot_y + plot_h, "#1b4332", "3"))
    svg.append(_line(xmap(C_CLEFT_M), plot_y, xmap(C_CLEFT_M), plot_y + plot_h, "#9b2226", "3"))
    h1 = ET.SubElement(svg, "text", attrib={"x": str(xmap(C_TONIC_M) - 8), "y": str(plot_y - 8), "font-size": "12", "font-family": "sans-serif", "font-weight": "bold", "fill": "#1b4332"})
    h1.text = "25 nM"
    h1b = ET.SubElement(svg, "text", attrib={"x": str(xmap(C_TONIC_M) - 8), "y": str(plot_y + plot_h + 18), "font-size": "11", "font-family": "sans-serif", "fill": "#1b4332"})
    h1b.text = "Herman ambient  MEASURED"
    h1c = ET.SubElement(svg, "text", attrib={"x": str(xmap(C_TONIC_M) - 8), "y": str(plot_y + plot_h + 34), "font-size": "11", "font-family": "sans-serif", "fill": "#1b4332"})
    h1c.text = "acute hippocampal slice — not retina"
    c1 = ET.SubElement(svg, "text", attrib={"x": str(xmap(C_CLEFT_M) - 70), "y": str(plot_y - 8), "font-size": "12", "font-family": "sans-serif", "font-weight": "bold", "fill": "#9b2226"})
    c1.text = "1.1 mM"
    c1b = ET.SubElement(svg, "text", attrib={"x": str(xmap(C_CLEFT_M) - 120), "y": str(plot_y + plot_h + 18), "font-size": "11", "font-family": "sans-serif", "fill": "#9b2226"})
    c1b.text = "Clements peak  INFERENCE"
    c1c = ET.SubElement(svg, "text", attrib={"x": str(xmap(C_CLEFT_M) - 120), "y": str(plot_y + plot_h + 34), "font-size": "11", "font-family": "sans-serif", "fill": "#9b2226"})
    c1c.text = "cultured hippocampal synapses — different prep"
    span_x1, span_x2 = xmap(C_TONIC_M), xmap(C_CLEFT_M)
    svg.append(_line(span_x1, plot_y + 175, span_x2, plot_y + 175, "#111", "2"))
    span_lab = ET.SubElement(
        svg,
        "text",
        attrib={"x": str((span_x1 + span_x2) / 2), "y": str(plot_y + 168), "font-size": "14", "font-family": "sans-serif", "font-weight": "bold", "text-anchor": "middle"},
    )
    span_lab.text = "~44,000-fold  MODELED arithmetic on two literature examples"
    ET.SubElement(
        svg,
        "rect",
        attrib={"x": "770", "y": "130", "width": "120", "height": "120", "fill": "#d3d3d3", "stroke": "#111", "stroke-width": "3"},
    )
    u1 = ET.SubElement(svg, "text", attrib={"x": "830", "y": "175", "font-size": "14", "font-family": "sans-serif", "font-weight": "bold", "text-anchor": "middle"})
    u1.text = "UNKNOWN"
    u2 = ET.SubElement(svg, "text", attrib={"x": "830", "y": "198", "font-size": "12", "font-family": "sans-serif", "text-anchor": "middle"})
    u2.text = "PaC probe θ"
    u3 = ET.SubElement(svg, "text", attrib={"x": "830", "y": "216", "font-size": "12", "font-family": "sans-serif", "text-anchor": "middle"})
    u3.text = "in Ames/tissue"
    u4 = ET.SubElement(svg, "text", attrib={"x": "830", "y": "234", "font-size": "11", "font-family": "sans-serif", "text-anchor": "middle"})
    u4.text = "unmeasured"
    foot = ET.SubElement(svg, "text", attrib={"x": "20", "y": "430", "font-size": "13", "font-family": "sans-serif"})
    foot.text = "Hu 1.8 nM Langmuir–Freundlich apparent Kd is an AuED-MEA PBS number. It is not drawn here as tissue occupancy or as the retinal probe’s molecular Kd."
    foot2 = ET.SubElement(svg, "text", attrib={"x": "20", "y": "450", "font-size": "13", "font-family": "sans-serif"})
    foot2.text = "PROPOSED: paired solution/surface isotherm of the Fc-thiol 39-mer; report n. Different hippocampal contexts are not a retinal spec."
    foot3 = ET.SubElement(svg, "text", attrib={"x": "20", "y": "480", "font-size": "12", "font-family": "sans-serif", "fill": "#444"})
    foot3.text = "Axis: log10 [Glu] from 10 pM to 10 mM. 81-fold ruler shown at a generic 1 µM Kd so it cannot be mistaken for the 1.8 nM overlay."
    return ET.tostring(svg, encoding="unicode")


def two_regime_clocks_svg() -> str:
    width, height = 900, 420
    svg = ET.Element("svg", attrib={"xmlns": "http://www.w3.org/2000/svg", "width": str(width), "height": str(height)})
    ET.SubElement(svg, "rect", attrib={"x": "0", "y": "0", "width": str(width), "height": str(height), "fill": "#fff"})
    title = ET.SubElement(svg, "text", attrib={"x": "20", "y": "28", "font-size": "18", "font-family": "sans-serif", "font-weight": "bold"})
    title.text = "Two clocks: basal/slow MEASURED on the retina probe; rapid transients UNKNOWN"
    _stamp(svg, 20, 44, 150, 32, "MEASURED", "#b7e4c7")
    _stamp(svg, 180, 44, 150, 32, "MODELED", "#90e0ef")
    _stamp(svg, 340, 44, 150, 32, "UNKNOWN", "#d3d3d3")
    _stamp(svg, 500, 44, 150, 32, "PROPOSED", "#ffd166")
    ET.SubElement(svg, "rect", attrib={"x": "20", "y": "100", "width": "420", "height": "230", "fill": "#d8f3dc", "stroke": "#111", "stroke-width": "3"})
    ET.SubElement(svg, "rect", attrib={"x": "460", "y": "100", "width": "420", "height": "230", "fill": "#e9ecef", "stroke": "#111", "stroke-width": "3"})
    lhead = ET.SubElement(svg, "text", attrib={"x": "230", "y": "128", "font-size": "16", "font-family": "sans-serif", "font-weight": "bold", "text-anchor": "middle"})
    lhead.text = "SLOW / BASAL  —  MEASURED"
    rhead = ET.SubElement(svg, "text", attrib={"x": "670", "y": "128", "font-size": "16", "font-family": "sans-serif", "font-weight": "bold", "text-anchor": "middle"})
    rhead.text = "RAPID TRANSIENT  —  UNKNOWN"
    left_lines = [
        "S066 in vitro mouse retina (not in vivo)",
        "ACV scan ~14 s; sampling ~1 min/point",
        "10 nM step plateaus ~10 min",
        "Authors: basal, not synaptic transients",
        "Probes 1–2 light-correlated ACV",
        "GCL/IPL electrode vs photoreceptor narrative: UNKNOWN pool",
    ]
    right_lines = [
        "Clements 1.2 ms: cultured hippocampal INFERENCE",
        "Different preparation from Herman slices",
        "Glutamate aptamer koff: UNKNOWN",
        "Missing koff does not prove slow kinetics",
        "τ_eq at millimolar c: untested (MODELED if assumed)",
        "Not a failed hippocampal-cleft sensor",
    ]
    y = 158
    for line in left_lines:
        t = ET.SubElement(svg, "text", attrib={"x": "36", "y": str(y), "font-size": "13", "font-family": "sans-serif"})
        t.text = line
        y += 26
    y = 158
    for line in right_lines:
        t = ET.SubElement(svg, "text", attrib={"x": "476", "y": str(y), "font-size": "13", "font-family": "sans-serif"})
        t.text = line
        y += 26
    ET.SubElement(svg, "rect", attrib={"x": "20", "y": "350", "width": "860", "height": "50", "fill": "#ffd166", "stroke": "#111", "stroke-width": "2"})
    p = ET.SubElement(svg, "text", attrib={"x": "450", "y": "380", "font-size": "15", "font-family": "sans-serif", "font-weight": "bold", "text-anchor": "middle"})
    p.text = "PROPOSED: IPA/SPR kon/koff on the 39-mer — does not exist in this ledger"
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
    (out / "span_identity.svg").write_text(span_identity_svg(), encoding="utf-8")
    (out / "two_regime_clocks.svg").write_text(two_regime_clocks_svg(), encoding="utf-8")
    (out / "occupancy.svg").write_text(occupancy_svg(), encoding="utf-8")
    (out / "clocks.svg").write_text(clocks_svg(), encoding="utf-8")
    (out / "sensitivity.svg").write_text(sensitivity_svg(), encoding="utf-8")
    write_table(ROOT / "tables" / "occupancy_table.csv")
    (out / "CAPTION.md").write_text(
        "Figure span_identity (FLAGSHIP): 1:1 Langmuir 10–90% occupancy is exactly 81-fold, "
        "independent of Kd. MODELED design principle. Herman ~25 nM is MEASURED ambient glutamate "
        "in acute hippocampal slice. Clements ~1.1 mM is an INFERENCE at cultured hippocampal "
        "synapses — a different preparation. Those two literature examples span ~44,000-fold "
        "(MODELED arithmetic). They are not a retinal concentration range. PaC-probe occupancy "
        "in Ames/tissue is UNKNOWN. Hu 1.8 nM is not drawn as tissue occupancy.\n\n"
        "Figure two_regime_clocks: left column S066 basal/slow clocks MEASURED in vitro mouse "
        "retina; right column rapid transients UNKNOWN. Missing koff does not prove slow kinetics. "
        "PROPOSED: 39-mer kon/koff.\n\n"
        "Figure occupancy (DEMOTED): Langmuir θ([Glu]) using three published numbers as if they "
        "were 1:1 occupancy Kd/EC50. MODELED overlay. Not tissue occupancy. Not the PaC probe’s Kd. "
        "Vertical lines mark Herman 25 nM and Clements 1.1 mM as hippocampal literature examples. "
        "Hu 1.8 nM is an AuED-MEA Langmuir–Freundlich apparent Kd in PBS. LOD is not occupancy.\n\n"
        "Figure clocks (supporting omnibus): log time. Cleft τ is inference. t_off values are "
        "diffusion-limited BOUNDS, not measured glutamate koff. Hu 15 min and Xiao 200 s are "
        "measured protocol times. GlutOx 500 ms is an enzyme comparator, not an aptamer.\n\n"
        "Figure sensitivity: t_off vs assumed kon. Orange band is Ding ITC kon endpoints (C010) "
        "and the purple line is tobramycin IPA kon (C008). Those rates are NOT glutamate. "
        "If they applied, even 12 µM t_off is seconds, not 0.8 ms. Rising-edge tau_eq at 1.1 mM "
        "can still be milliseconds because tau_eq = 1/(kon c + koff). BOUND/SIMULATION.\n",
        encoding="utf-8",
    )
    print(out / "span_identity.svg")
    print(out / "two_regime_clocks.svg")
    print(out / "occupancy.svg")
    print(out / "clocks.svg")
    print(out / "sensitivity.svg")


if __name__ == "__main__":
    main()
