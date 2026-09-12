#!/usr/bin/env python3
"""Three-layer interrogation/sampling-timescale SVG. COMPUTATIONAL ILLUSTRATION.

Quantity types on-figure: inferred literature waveform, measured interrogation,
measured sampling. IPA and GlutOx are not drawn. No glutamate kon/koff.
No electrode nM from averaging. The word Nyquist is forbidden in outputs.
"""

from __future__ import annotations

import csv
import math
import xml.etree.ElementTree as ET
from pathlib import Path

from ledger import LedgerClocks, load_clocks
from model import (
    axis_occupancy_fraction,
    clock_ratio,
    inferred_clements_waveform_m,
    shape_reporting_excluded,
    timescale_mismatch,
)

ROOT = Path(__file__).resolve().parent

COLOR_INFERRED = "#0d5c4d"
COLOR_INTERROG = "#c45c26"
COLOR_SAMPLE = "#5b4b8a"
COLOR_INK = "#222222"
COLOR_MUTED = "#555555"
COLOR_LAYER = "#f4f4f4"
FONT = "sans-serif"

FORBIDDEN = (
    "too slow",
    "nyquist",
    "94 nM",
    "94 nm",
    "mean-equivalent",
    "mean equivalent",
    "the aptamer is",
)


def _line(x1, y1, x2, y2, stroke="#333", width="1"):
    return ET.Element(
        "line",
        attrib={
            "x1": f"{x1:.2f}",
            "y1": f"{y1:.2f}",
            "x2": f"{x2:.2f}",
            "y2": f"{y2:.2f}",
            "stroke": stroke,
            "stroke-width": width,
        },
    )


def _text(x, y, content, size="12", fill=COLOR_INK, weight="normal", anchor="start"):
    el = ET.Element(
        "text",
        attrib={
            "x": f"{x:.2f}",
            "y": f"{y:.2f}",
            "font-size": size,
            "font-family": FONT,
            "fill": fill,
            "font-weight": weight,
            "text-anchor": anchor,
        },
    )
    el.text = content
    return el


def _rect(x, y, w, h, fill="#fff", stroke="none", sw="1", opacity="1"):
    return ET.Element(
        "rect",
        attrib={
            "x": f"{x:.2f}",
            "y": f"{y:.2f}",
            "width": f"{w:.2f}",
            "height": f"{h:.2f}",
            "fill": fill,
            "stroke": stroke,
            "stroke-width": sw,
            "opacity": opacity,
        },
    )


def _pulse_points(clocks: LedgerClocks, x0, y0, w, h, t_max_s: float, n: int = 240):
    y_max_m = clocks.peak_m * 1.12

    def xmap(t):
        return x0 + (t / t_max_s) * w

    def ymap(c):
        return y0 + h * (1.0 - c / y_max_m)

    pts = []
    for i in range(n + 1):
        t = t_max_s * i / n
        pts.append(f"{xmap(t):.2f},{ymap(inferred_clements_waveform_m(t, clocks)):.2f}")
    return " ".join(pts), xmap, ymap


def _plot_frame(svg, x, y, w, h):
    svg.append(_rect(x, y, w, h, fill="#fafafa", stroke="#000", sw="1"))


def _log_x(t_s: float, t_min: float, t_max: float, x0: float, w: float) -> float:
    return x0 + (math.log10(t_s) - math.log10(t_min)) / (math.log10(t_max) - math.log10(t_min)) * w


def caption_text(clocks: LedgerClocks) -> str:
    r_scan = clock_ratio(clocks.interrogation_s, clocks.tau_s)
    r_samp = clock_ratio(clocks.sampling_s, clocks.tau_s)
    return (
        "Figure sampling-clock (Mission 2 candidate; not accepted flagship): "
        "three layers on one architecture versus an inferred literature waveform. "
        "COMPUTATIONAL ILLUSTRATION, not a recording. "
        "Frame: interrogation/sampling-timescale mismatch. "
        "Not a sampling-theorem reconstruction claim.\n\n"
        "Layer 1 MEASURED. Hu 2025 RWTH thesis (S066) in vitro mouse retina, "
        "Glu-apt on PaC probe, large bottom electrode at the GCL. One ACV scan "
        "(0 to 0.7 V, 0.05 V^-1) yields one data point every 14 s (E045 / C034). "
        "Subsequent recordings at ~1 min intervals (E046 / C031). Authors: "
        "electrochemical glutamate averaged over much longer windows (on the order "
        "of one minute per data point); captures sustained basal glutamate rather "
        "than fast synaptic transients (C031 / C033). Protocol time is not koff.\n\n"
        "Layer 2 INFERRED. Clements 1992 PubMed abstract (S049; VoR closed): "
        "glutamate peaked at 1.1 mM and decayed with a time constant of 1.2 ms "
        "at cultured hippocampal synapses (E032 / E033 / C011). Kinetic inference, "
        "not a chemical assay. Transferable to a retinal GCL electrode: unknown. "
        "Herman 25 nM (E034 / C012) is a different hippocampal-slice ambient "
        "estimate and is not spliced into the plotted waveform. Amplitude is not "
        "required for T/τ.\n\n"
        "Layer 3 MODELED. Clock ratios 14 s / 1.2 ms = "
        f"{r_scan:,.0f} and 60 s / 1.2 ms = {r_samp:,.0f} are dimensionless T/τ, "
        "not koff. Each architecture clock independently satisfies T ≫ τ. One ACV "
        "scan is one scalar, so a 1.2 ms event occupies a sub-pixel fraction of "
        "the 14 s interrogation axis and waveform identity is not a degree of "
        "freedom. Instantaneous occupancy is a hypothetical measurement-operator "
        "assumption; glutamate kon/koff remain empty (C007). Spatial dilution is "
        "unmeasured and is not modeled. No rectangular-window mean is plotted.\n\n"
        "UNKNOWN: PaC occupancy / apparent Kd in Ames or tissue; glutamate "
        "kon/koff; [Glu] at the GCL-positioned electrode; whether a 1.2 ms "
        "hippocampal-cleft waveform is the named biological spec for this retina "
        "experiment.\n\n"
        "PROPOSED: interrogate the same oligo on a known millisecond [Glu](t) "
        "pulse with a sub-millisecond to few-millisecond electrical query, or "
        "lock the biological spec as basal/graded retinal glutamate rather than "
        "a 1.2 ms hippocampal cleft waveform. A koff measured on 14 s ACV cannot "
        "reopen shape reporting on this cadence.\n\n"
        "Off-figure protocol times, not interrogation and not koff: journal 15 min "
        "Glu wait (C006/E008); thesis ~10 min plateau after 10 nM (C028/E042). "
        "Other-class footnote, not plotted: IPA 2 ms is tobramycin interrogation "
        "(C009); GlutOx 500–800 ms is an enzyme comparator (C022).\n"
    )


def sampling_clock_svg(clocks: LedgerClocks) -> str:
    width, height = 980, 860
    svg = ET.Element(
        "svg",
        attrib={
            "xmlns": "http://www.w3.org/2000/svg",
            "width": str(width),
            "height": str(height),
            "viewBox": f"0 0 {width} {height}",
        },
    )
    title = ET.SubElement(svg, "title")
    title.text = (
        "Interrogation and sampling clocks versus a 1.2 ms inferred literature "
        "waveform (computational illustration; candidate, not flagship)"
    )
    desc = ET.SubElement(svg, "desc")
    desc.text = (
        "Three layers: MEASURED Hu ACV clocks, INFERRED Clements tau, MODELED "
        "T over tau ratios. Waveform identity is lost on a 14 s interrogation "
        "axis. Not koff. Not a concentration at the electrode."
    )
    svg.append(_rect(0, 0, width, height, fill="#fff"))

    svg.append(
        _text(
            20,
            24,
            "Can this ACV cadence report the shape of a 1.2 ms literature waveform?",
            size="16",
            weight="bold",
        )
    )
    svg.append(
        _text(
            20,
            44,
            "Mission 2 candidate — interrogation/sampling-timescale mismatch. COMPUTATIONAL ILLUSTRATION. Not flagship. Not glutamate koff. C007 empty.",
            size="11",
            fill=COLOR_MUTED,
        )
    )

    r_scan = clock_ratio(clocks.interrogation_s, clocks.tau_s)
    r_samp = clock_ratio(clocks.sampling_s, clocks.tau_s)

    # --- Layer 1 MEASURED ---
    svg.append(_rect(16, 56, 948, 168, fill=COLOR_LAYER, stroke="#ccc", sw="1"))
    svg.append(_text(28, 78, "Layer 1  MEASURED  — Hu PaC retina ACV clocks (S066 §6.3)", size="13", weight="bold"))
    cards = [
        (
            COLOR_INTERROG,
            "interrogation",
            "14 s / scan",
            "E045 / C034",
            "one ACV sweep → one scalar",
        ),
        (
            COLOR_SAMPLE,
            "sampling",
            "~1 min / point",
            "E046 / C031",
            "cadence after insertion",
        ),
    ]
    for i, (color, kind, value, ids, note) in enumerate(cards):
        x = 28 + i * 470
        svg.append(_rect(x, 90, 450, 86, fill="#fff", stroke=color, sw="2"))
        svg.append(_rect(x, 90, 8, 86, fill=color, stroke="none"))
        svg.append(_text(x + 18, 112, kind, size="11", fill=color, weight="bold"))
        svg.append(_text(x + 18, 136, f"{value}   {ids}", size="14", weight="bold"))
        svg.append(_text(x + 18, 160, note, size="11", fill=COLOR_MUTED))
    svg.append(
        _text(
            28,
            208,
            "Authors: basal / sustained glutamate, not synaptic transients (C031). Protocol time ≠ koff. In vitro retina, not in vivo.",
            size="11",
            fill=COLOR_MUTED,
        )
    )

    # --- Layer 2 INFERRED ---
    svg.append(_rect(16, 234, 948, 248, fill="#fff", stroke="#ccc", sw="1"))
    svg.append(
        _text(
            28,
            256,
            "Layer 2  INFERRED  — Clements 1992 cultured hippocampal synapses (S049 abstract; VoR closed)",
            size="13",
            weight="bold",
        )
    )

    px, py, pw, ph = 70.0, 270.0, 430.0, 168.0
    t_max_a = 8e-3
    pts, xmap, ymap = _pulse_points(clocks, px, py, pw, ph, t_max_a)
    _plot_frame(svg, px, py, pw, ph)
    ET.SubElement(
        svg,
        "polyline",
        attrib={"points": pts, "fill": "none", "stroke": COLOR_INFERRED, "stroke-width": "2.4"},
    )
    tau_x = xmap(clocks.tau_s)
    svg.append(_line(tau_x, py, tau_x, py + ph, COLOR_INFERRED, "1"))
    svg.append(_text(tau_x + 4, py + 14, "τ = 1.2 ms", size="10", fill=COLOR_INFERRED))
    svg.append(
        _text(
            px + 8,
            py + 18,
            "peak 1.1 mM (E032)  inferred decay, not a PaC recording",
            size="10",
            fill=COLOR_INFERRED,
        )
    )
    svg.append(
        _text(
            px + 8,
            py + ph - 8,
            "Herman 25 nM (E034) is not spliced onto this axis",
            size="9",
            fill=COLOR_MUTED,
        )
    )
    for t_ms, label in [(0, "0"), (1.2, "1.2"), (2, "2"), (4, "4"), (6, "6"), (8, "8")]:
        x = xmap(t_ms * 1e-3)
        svg.append(_line(x, py + ph, x, py + ph + 5, "#333", "1"))
        svg.append(_text(x, py + ph + 18, label, size="10", anchor="middle"))
    svg.append(
        _text(px + pw / 2, py + ph + 34, "time (ms) — inferred biological τ axis", size="11", anchor="middle")
    )
    for c_mM in (0.0, 0.5, 1.0, 1.1):
        c = c_mM * 1e-3
        y = ymap(c)
        svg.append(_line(px - 5, y, px, y, "#333", "1"))
        svg.append(_text(px - 8, y + 4, f"{c_mM:g}", size="10", anchor="end"))
    ylab = _text(22, py + ph / 2, "inferred [Glu] (mM)", size="11", anchor="middle")
    ylab.set("transform", f"rotate(-90 22 {py + ph / 2:.1f})")
    svg.append(ylab)

    svg.append(_rect(530, 270, 412, 168, fill="#fff", stroke=COLOR_INFERRED, sw="2"))
    svg.append(_rect(530, 270, 8, 168, fill=COLOR_INFERRED, stroke="none"))
    svg.append(_text(552, 292, "biological τ", size="11", fill=COLOR_INFERRED, weight="bold"))
    svg.append(_text(552, 316, "1.2 ms   E033 / C011", size="14", weight="bold"))
    svg.append(_text(552, 338, "quantity type: inferred free-Glu lifetime", size="11", fill=COLOR_MUTED))
    svg.append(_text(552, 360, "not a sensor t90; stored as response_time in ledger", size="11", fill=COLOR_MUTED))
    svg.append(_text(552, 382, "transferable to retina GCL electrode: UNKNOWN", size="11", fill=COLOR_MUTED))
    svg.append(_text(552, 404, "kinetic inference, not a chemical assay", size="11", fill=COLOR_MUTED))
    svg.append(
        _text(
            552,
            424,
            "If this τ is the named spec, Layer 3 follows. If it is not, Layer 3 does not grade Hu’s experiment.",
            size="10",
            fill=COLOR_MUTED,
        )
    )

    # --- Layer 3 MODELED ---
    svg.append(_rect(16, 492, 948, 328, fill="#fff", stroke="#ccc", sw="1"))
    svg.append(
        _text(
            28,
            514,
            "Layer 3  MODELED  — T/τ clock ratios under hypothetical instantaneous occupancy",
            size="13",
            weight="bold",
        )
    )

    # log clocks
    lx, ly, lw, lh = 70.0, 528.0, 880.0, 70.0
    svg.append(_rect(lx, ly, lw, lh, fill="#fafafa", stroke="#000", sw="1"))
    t_min, t_max = 1e-4, 1e3
    ticks = [
        (1e-3, "1 ms"),
        (clocks.tau_s, "1.2 ms"),
        (1.0, "1 s"),
        (clocks.interrogation_s, "14 s"),
        (clocks.sampling_s, "60 s"),
        (1e3, "10³ s"),
    ]
    for t_s, lab in ticks:
        x = _log_x(t_s, t_min, t_max, lx, lw)
        svg.append(_line(x, ly + lh, x, ly + lh + 6, "#333", "1"))
        svg.append(_text(x, ly + lh + 20, lab, size="10", anchor="middle"))
    svg.append(_text(lx + lw / 2, ly + lh + 36, "log10 time (s) — clocks, not a shared kinetic axis", size="11", anchor="middle"))

    tau_x = _log_x(clocks.tau_s, t_min, t_max, lx, lw)
    int_x = _log_x(clocks.interrogation_s, t_min, t_max, lx, lw)
    samp_x = _log_x(clocks.sampling_s, t_min, t_max, lx, lw)
    svg.append(_line(tau_x, ly + 8, tau_x, ly + lh - 8, COLOR_INFERRED, "3"))
    svg.append(_line(int_x, ly + 8, int_x, ly + lh - 8, COLOR_INTERROG, "3"))
    svg.append(_line(samp_x, ly + 8, samp_x, ly + lh - 8, COLOR_SAMPLE, "3"))
    svg.append(_text(tau_x + 4, ly + 22, "INFERRED τ", size="10", fill=COLOR_INFERRED))
    svg.append(_text(int_x - 4, ly + 22, "MEASURED scan", size="10", fill=COLOR_INTERROG, anchor="end"))
    svg.append(_text(samp_x + 4, ly + 38, "MEASURED sampling", size="10", fill=COLOR_SAMPLE))

    svg.append(
        _text(
            28,
            650,
            f"14 s / 1.2 ms = {r_scan:,.0f} × τ     60 s / 1.2 ms = {r_samp:,.0f} × τ     each clock independently T ≫ τ",
            size="13",
            weight="bold",
        )
    )

    # 14 s axis needle
    bx, by, bw, bh = 70.0, 668.0, 720.0, 90.0
    t_max_b = clocks.interrogation_s
    _plot_frame(svg, bx, by, bw, bh)
    svg.append(_rect(bx, by, bw, bh, fill=COLOR_INTERROG, stroke="none", opacity="0.12"))
    svg.append(
        _text(
            bx + 10,
            by + 16,
            "one 14 s interrogation window (E045) → one scalar; shape is not a degree of freedom",
            size="10",
            fill=COLOR_INTERROG,
        )
    )
    svg.append(_line(bx + 1, by + bh, bx + 1, by + 8, COLOR_INFERRED, "2"))
    svg.append(
        _text(
            bx + 8,
            by + 36,
            "inferred 1.2 ms waveform — narrower than one pixel on this 14 s axis",
            size="10",
            fill=COLOR_INFERRED,
        )
    )
    svg.append(
        _text(
            bx + 8,
            by + 52,
            "Not [Glu] at the GCL-positioned PaC electrode. Spatial dilution unmeasured. No mean nM is plotted.",
            size="10",
            fill=COLOR_MUTED,
        )
    )
    for t_s, lab in [(0.0, "0"), (7.0, "7"), (14.0, "14")]:
        x = bx + (t_s / t_max_b) * bw
        svg.append(_line(x, by + bh, x, by + bh + 5, "#333", "1"))
        svg.append(_text(x, by + bh + 18, lab, size="10", anchor="middle"))
    svg.append(
        _text(
            bx + bw / 2,
            by + bh + 32,
            "time (s) — one interrogation window",
            size="11",
            anchor="middle",
        )
    )

    ix, iy, iw, ih = 810.0, 668.0, 132.0, 90.0
    svg.append(_rect(ix - 4, iy - 16, iw + 8, ih + 28, fill="#fff", stroke="#888", sw="1"))
    svg.append(_text(ix, iy - 4, "inset 0–8 ms", size="9", fill=COLOR_MUTED))
    ipts, _, _ = _pulse_points(clocks, ix, iy, iw, ih, t_max_a, n=120)
    svg.append(_rect(ix, iy, iw, ih, fill="#fafafa", stroke="#000", sw="1"))
    ET.SubElement(
        svg,
        "polyline",
        attrib={"points": ipts, "fill": "none", "stroke": COLOR_INFERRED, "stroke-width": "1.8"},
    )

    svg.append(
        _text(
            20,
            822,
            "UNKNOWN: PaC occupancy; glutamate kon/koff; [Glu] at GCL.  PROPOSED: fast interrogation of the same oligo on a known millisecond pulse, or lock the spec as basal/graded retina glutamate.",
            size="10",
            fill=COLOR_MUTED,
        )
    )
    svg.append(
        _text(
            20,
            842,
            "If Layer 3 is correct: on this ACV architecture, missing koff is not what excludes 1.2 ms shape reporting. If Layer 2 is the wrong spec, this figure does not grade Hu’s basal retina experiment.",
            size="10",
            fill=COLOR_MUTED,
        )
    )

    xml = ET.tostring(svg, encoding="unicode")
    low = xml.lower()
    for needle in FORBIDDEN:
        if needle.lower() in low:
            raise RuntimeError(f"forbidden caption fragment leaked into SVG: {needle}")
    if "ipa" in low or "glutox" in low:
        raise RuntimeError("IPA/GlutOx must stay off-figure")
    frac = axis_occupancy_fraction(clocks.tau_s, t_max_b)
    if frac >= 0.01:
        raise RuntimeError("1.2 ms event unexpectedly occupies a visible fraction of the 14 s axis")
    if not timescale_mismatch(clocks.interrogation_s, clocks.tau_s):
        raise RuntimeError("interrogation unexpectedly not longer than tau")
    if not timescale_mismatch(clocks.sampling_s, clocks.tau_s):
        raise RuntimeError("sampling unexpectedly not longer than tau")
    if not shape_reporting_excluded(clocks.interrogation_s, clocks.sampling_s, clocks.tau_s):
        raise RuntimeError("ledger clocks unexpectedly pass the coarse T>tau test")
    return xml


def write_clock_table(path: Path, clocks: LedgerClocks) -> None:
    rows = [
        {
            "layer": "2_inferred",
            "quantity_class": "biological_tau",
            "stamp": "INFERRED",
            "ledger_id": clocks.tau_id,
            "value_s": f"{clocks.tau_s:.6g}",
            "vs_tau": "1",
            "on_figure": "yes",
            "notes": "Clements literature waveform timescale; E033; not a sensor t90",
        },
        {
            "layer": "2_inferred",
            "quantity_class": "cleft_peak",
            "stamp": "INFERRED",
            "ledger_id": clocks.peak_id,
            "value_s": "",
            "vs_tau": "",
            "on_figure": "yes",
            "notes": "1.1 mM peak used only to draw the inferred decay; not required for T/tau",
        },
        {
            "layer": "2_not_spliced",
            "quantity_class": "slice_ambient",
            "stamp": "MEASURED_elsewhere",
            "ledger_id": clocks.basal_id,
            "value_s": "",
            "vs_tau": "",
            "on_figure": "no",
            "notes": "Herman 25 nM not spliced into plotted waveform; not load-bearing for T/tau",
        },
        {
            "layer": "1_measured",
            "quantity_class": "interrogation",
            "stamp": "MEASURED",
            "ledger_id": clocks.interrogation_id,
            "value_s": f"{clocks.interrogation_s:.6g}",
            "vs_tau": f"{clock_ratio(clocks.interrogation_s, clocks.tau_s):.6g}",
            "on_figure": "yes",
            "notes": "ACV scan clock; ratio is T/tau not koff",
        },
        {
            "layer": "1_measured",
            "quantity_class": "sampling",
            "stamp": "MEASURED",
            "ledger_id": clocks.sampling_id,
            "value_s": f"{clocks.sampling_s:.6g}",
            "vs_tau": f"{clock_ratio(clocks.sampling_s, clocks.tau_s):.6g}",
            "on_figure": "yes",
            "notes": "retina sampling interval after insertion",
        },
        {
            "layer": "off_figure",
            "quantity_class": "incubation",
            "stamp": "MEASURED",
            "ledger_id": clocks.incubation_id,
            "value_s": f"{clocks.incubation_s:.6g}",
            "vs_tau": f"{clock_ratio(clocks.incubation_s, clocks.tau_s):.6g}",
            "on_figure": "no",
            "notes": "journal 15 min Glu wait C006/E008; off-figure protocol time",
        },
        {
            "layer": "off_figure",
            "quantity_class": "plateau",
            "stamp": "MEASURED",
            "ledger_id": clocks.plateau_id,
            "value_s": f"{clocks.plateau_s:.6g}",
            "vs_tau": f"{clock_ratio(clocks.plateau_s, clocks.tau_s):.6g}",
            "on_figure": "no",
            "notes": "thesis 10 min 10 nM plateau C028/E042; off-figure protocol time",
        },
        {
            "layer": "3_modeled",
            "quantity_class": "clock_ratio_scan",
            "stamp": "MODELED",
            "ledger_id": "derived_E045_over_E033",
            "value_s": "",
            "vs_tau": f"{clock_ratio(clocks.interrogation_s, clocks.tau_s):.6g}",
            "on_figure": "yes",
            "notes": "dimensionless T/tau; computational illustration",
        },
        {
            "layer": "3_modeled",
            "quantity_class": "clock_ratio_sample",
            "stamp": "MODELED",
            "ledger_id": "derived_E046_over_E033",
            "value_s": "",
            "vs_tau": f"{clock_ratio(clocks.sampling_s, clocks.tau_s):.6g}",
            "on_figure": "yes",
            "notes": "dimensionless T/tau; computational illustration",
        },
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _assert_clean_text(text: str) -> None:
    low = text.lower()
    for needle in FORBIDDEN:
        if needle.lower() in low:
            raise RuntimeError(f"forbidden fragment in caption/table: {needle}")


def main() -> None:
    clocks = load_clocks()
    out = ROOT / "figures"
    out.mkdir(exist_ok=True)
    svg = sampling_clock_svg(clocks)
    caption = caption_text(clocks)
    _assert_clean_text(svg)
    _assert_clean_text(caption)
    (out / "sampling_clock.svg").write_text(svg, encoding="utf-8")
    (out / "CAPTION.md").write_text(caption, encoding="utf-8")
    write_clock_table(ROOT / "tables" / "clocks.csv", clocks)
    table = (ROOT / "tables" / "clocks.csv").read_text(encoding="utf-8")
    _assert_clean_text(table)
    print(out / "sampling_clock.svg")
    print(out / "CAPTION.md")


if __name__ == "__main__":
    main()
