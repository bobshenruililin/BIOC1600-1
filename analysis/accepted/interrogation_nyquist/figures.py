#!/usr/bin/env python3
"""Two-panel interrogation Nyquist SVG. COMPUTATIONAL ILLUSTRATION.

Quantity types on-figure: literature stimulus / biological τ, interrogation,
sampling. IPA and GlutOx are not drawn. No glutamate kon/koff. No electrode nM from averaging.
"""

from __future__ import annotations

import csv
import xml.etree.ElementTree as ET
from pathlib import Path

from ledger import LedgerClocks, load_clocks
from model import (
    axis_occupancy_fraction,
    clock_ratio,
    literature_stimulus_m,
    nyquist_interval_s,
    shape_reconstructable,
)

ROOT = Path(__file__).resolve().parent

COLOR_STIM = "#0d5c4d"
COLOR_INTERROG = "#c45c26"
COLOR_SAMPLE = "#5b4b8a"
COLOR_INK = "#222222"
COLOR_MUTED = "#555555"
FONT = "sans-serif"

FORBIDDEN = (
    "too slow",
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
        pts.append(f"{xmap(t):.2f},{ymap(literature_stimulus_m(t, clocks)):.2f}")
    return " ".join(pts), xmap, ymap, y_max_m


def _plot_frame(svg, x, y, w, h):
    svg.append(_rect(x, y, w, h, fill="#fafafa", stroke="#000", sw="1"))


def caption_text(clocks: LedgerClocks) -> str:
    r_scan = clock_ratio(clocks.interrogation_s, clocks.tau_s)
    r_samp = clock_ratio(clocks.sampling_s, clocks.tau_s)
    nyq_ms = nyquist_interval_s(clocks.tau_s) * 1e3
    return (
        "Figure nyquist (A4): two clocks on one architecture versus a literature "
        "stimulus. COMPUTATIONAL ILLUSTRATION, not a recording.\n\n"
        "Panel A. Left: Clements-like pulse constructed as Herman 25 nM (E034/C012) "
        "plus inferred peak 1.1 mM decaying with τ = 1.2 ms (E032/E033/C011). This "
        "is a literature stimulus, not a measurement on the parylene-C probe. "
        "Clements is a kinetic inference at cultured hippocampal synapses (abstract; "
        "transferable unknown). Right: three quantity types kept separate — "
        "biological τ (1.2 ms), interrogation (14 s ACV scan, E045), sampling "
        f"(~1 min/point, E046). Clock ratios 14 s / 1.2 ms = {r_scan:,.0f} and "
        f"60 s / 1.2 ms = {r_samp:,.0f} are dimensionless T/τ, not koff.\n\n"
        "Panel B. The same literature stimulus on a 14 s interrogation axis. The "
        "1.2 ms event occupies a sub-pixel fraction of one ACV window, so waveform "
        "identity is lost. A rectangular averaging window is drawn; its numerical "
        "mean is not plotted and is not a concentration at the GCL-positioned "
        "electrode. Spatial dilution is unmeasured and is not modeled.\n\n"
        f"Nyquist sketch: τ/2 = {nyq_ms:.1f} ms (COMPUTATIONAL ILLUSTRATION; an "
        "exponential is not band-limited). Ledger interrogation 14 s and sampling "
        "60 s both sit far above that inequality. Even if occupancy tracked the "
        "literature stimulus instantly, this ACV cadence cannot report the shape. "
        "Hu thesis authors already state the retina ACV reports basal glutamate, "
        "not synaptic transients (C031). Protocol time ≠ koff; glutamate kon/koff "
        "cells remain empty (C007).\n\n"
        "Off-figure protocol times, not interrogation and not koff: journal 15 min "
        "Glu wait (C006/E008); thesis ~10 min plateau after 10 nM (C028/E042). "
        "Other-class footnote, not plotted: IPA 2 ms is tobramycin interrogation "
        "(C009); GlutOx 500–800 ms is an enzyme comparator (C022).\n"
    )


def nyquist_svg(clocks: LedgerClocks) -> str:
    width, height = 960, 720
    svg = ET.Element(
        "svg",
        attrib={
            "xmlns": "http://www.w3.org/1999/svg",
            "width": str(width),
            "height": str(height),
            "viewBox": f"0 0 {width} {height}",
        },
    )
    title = ET.SubElement(svg, "title")
    title.text = (
        "Interrogation and sampling versus a 1.2 ms literature stimulus "
        "(computational illustration)"
    )
    desc = ET.SubElement(svg, "desc")
    desc.text = (
        "Panel A shows a Clements-like millisecond pulse beside 14 s interrogation "
        "and 60 s sampling cards. Panel B shows the pulse on a 14 s axis where "
        "waveform identity is lost. Not a koff. Not a concentration at the electrode."
    )
    svg.append(_rect(0, 0, width, height, fill="#fff"))

    svg.append(
        _text(
            20,
            24,
            "A4. Can this ACV cadence report the shape of a 1.2 ms literature stimulus?",
            size="15",
            weight="bold",
        )
    )
    svg.append(
        _text(
            20,
            42,
            "COMPUTATIONAL ILLUSTRATION — literature stimulus vs interrogation vs sampling. Not glutamate koff. C007 remains empty.",
            size="11",
            fill=COLOR_MUTED,
        )
    )

    # --- Panel A ---
    svg.append(_rect(16, 54, 928, 318, fill="#fff", stroke="#ddd", sw="1"))
    svg.append(_text(28, 74, "A. Literature stimulus on a millisecond axis", size="13", weight="bold"))

    px, py, pw, ph = 70.0, 96.0, 430.0, 230.0
    t_max_a = 8e-3
    pts, xmap, ymap, y_max_m = _pulse_points(clocks, px, py, pw, ph, t_max_a)
    _plot_frame(svg, px, py, pw, ph)
    ET.SubElement(
        svg,
        "polyline",
        attrib={"points": pts, "fill": "none", "stroke": COLOR_STIM, "stroke-width": "2.4"},
    )
    tau_x = xmap(clocks.tau_s)
    svg.append(_line(tau_x, py, tau_x, py + ph, COLOR_STIM, "1"))
    svg.append(_text(tau_x + 4, py + 14, "τ = 1.2 ms", size="10", fill=COLOR_STIM))
    peak_mM = clocks.peak_m * 1e3
    svg.append(
        _text(
            px + 8,
            py + 18,
            f"peak {peak_mM:g} mM (E032)  literature stimulus",
            size="10",
            fill=COLOR_STIM,
        )
    )
    svg.append(_text(px + 8, py + ph - 8, "basal 25 nM (E034) is ~0 on this linear mM axis", size="9", fill=COLOR_MUTED))

    for t_ms, label in [(0, "0"), (1.2, "1.2"), (2, "2"), (4, "4"), (6, "6"), (8, "8")]:
        x = xmap(t_ms * 1e-3)
        svg.append(_line(x, py + ph, x, py + ph + 5, "#333", "1"))
        svg.append(_text(x, py + ph + 18, label, size="10", anchor="middle"))
    svg.append(_text(px + pw / 2, py + ph + 34, "time (ms) — biological τ axis", size="11", anchor="middle"))

    for c_mM in (0.0, 0.5, 1.0, 1.1):
        c = c_mM * 1e-3
        y = ymap(c)
        svg.append(_line(px - 5, y, px, y, "#333", "1"))
        svg.append(_text(px - 8, y + 4, f"{c_mM:g}", size="10", anchor="end"))
    ylab = _text(22, py + ph / 2, "literature-stimulus [Glu] (mM)", size="11", anchor="middle")
    ylab.set("transform", f"rotate(-90 22 {py + ph / 2:.1f})")
    svg.append(ylab)

    # quantity-type cards
    cards = [
        (
            COLOR_STIM,
            "biological τ",
            "1.2 ms",
            "E033 / C011",
            "literature stimulus timescale",
            "quantity type: biological τ (inference)",
        ),
        (
            COLOR_INTERROG,
            "interrogation",
            "14 s",
            "E045 / C031",
            f"14 s / 1.2 ms = {clock_ratio(clocks.interrogation_s, clocks.tau_s):,.0f} × τ",
            "clock ratio, not koff",
        ),
        (
            COLOR_SAMPLE,
            "sampling",
            "~1 min",
            "E046 / C031",
            f"60 s / 1.2 ms = {clock_ratio(clocks.sampling_s, clocks.tau_s):,.0f} × τ",
            "clock ratio, not koff",
        ),
    ]
    cx, cy = 530.0, 88.0
    for i, (color, kind, value, ids, line, note) in enumerate(cards):
        y = cy + i * 72
        svg.append(_rect(cx, y, 396, 66, fill="#fff", stroke=color, sw="2"))
        svg.append(_rect(cx, y, 8, 66, fill=color, stroke="none"))
        svg.append(_text(cx + 18, y + 18, kind, size="11", fill=color, weight="bold"))
        svg.append(_text(cx + 18, y + 38, f"{value}   {ids}", size="13", weight="bold"))
        svg.append(_text(cx + 18, y + 56, f"{line} — {note}", size="10", fill=COLOR_MUTED))

    nyq_ms = nyquist_interval_s(clocks.tau_s) * 1e3
    svg.append(
        _text(
            530,
            312,
            f"Nyquist sketch: τ/2 = {nyq_ms:.1f} ms (COMPUTATIONAL ILLUSTRATION, not a spec). Both architecture clocks ≫ 0.6 ms.",
            size="10",
            fill=COLOR_MUTED,
        )
    )
    svg.append(
        _text(
            530,
            328,
            "Panel A vs B do not share a linear time axis. Reconstructable shape on this cadence: no.",
            size="10",
            fill=COLOR_MUTED,
        )
    )

    # --- Panel B ---
    svg.append(_rect(16, 382, 928, 292, fill="#fff", stroke="#ddd", sw="1"))
    svg.append(
        _text(
            28,
            402,
            "B. Same literature stimulus under one 14 s rectangular interrogation window — waveform identity is lost",
            size="13",
            weight="bold",
        )
    )

    bx, by, bw, bh = 70.0, 418.0, 720.0, 188.0
    t_max_b = clocks.interrogation_s
    _plot_frame(svg, bx, by, bw, bh)
    svg.append(_rect(bx, by, bw, bh, fill=COLOR_INTERROG, stroke="none", opacity="0.12"))
    svg.append(
        _text(
            bx + 10,
            by + 16,
            "interrogation window = one 14 s ACV scan (E045)  →  one scalar; shape is not a degree of freedom",
            size="10",
            fill=COLOR_INTERROG,
        )
    )

    # needle: 1.2 ms is <1 px on this axis
    frac = axis_occupancy_fraction(clocks.tau_s, t_max_b)
    peak_y = by + 8
    svg.append(_line(bx + 1, by + bh, bx + 1, peak_y, COLOR_STIM, "2"))
    svg.append(
        _text(
            bx + 8,
            by + 36,
            "literature stimulus (1.2 ms) — narrower than one pixel on this 14 s axis",
            size="10",
            fill=COLOR_STIM,
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
            by + bh + 34,
            "time (s) — one interrogation window, not a sampling-interval axis",
            size="11",
            anchor="middle",
        )
    )
    for c_mM in (0.0, 1.1):
        c = c_mM * 1e-3
        y = by + bh * (1.0 - c / (clocks.peak_m * 1.12))
        svg.append(_line(bx - 5, y, bx, y, "#333", "1"))
        svg.append(_text(bx - 8, y + 4, f"{c_mM:g}", size="10", anchor="end"))
    ylab_b = _text(18, by + bh / 2, "literature-stimulus [Glu] (mM)", size="11", anchor="middle")
    ylab_b.set("transform", f"rotate(-90 18 {by + bh / 2:.1f})")
    svg.append(ylab_b)

    # inset: millisecond pulse so the lost waveform is still visible
    ix, iy, iw, ih = 790.0, 430.0, 140.0, 100.0
    svg.append(_rect(ix - 6, iy - 18, iw + 12, ih + 36, fill="#fff", stroke="#888", sw="1"))
    svg.append(_text(ix - 2, iy - 6, "inset: 0–8 ms (same stimulus)", size="9", fill=COLOR_MUTED))
    ipts, _, _, _ = _pulse_points(clocks, ix, iy, iw, ih, t_max_a, n=120)
    svg.append(_rect(ix, iy, iw, ih, fill="#fafafa", stroke="#000", sw="1"))
    ET.SubElement(
        svg,
        "polyline",
        attrib={"points": ipts, "fill": "none", "stroke": COLOR_STIM, "stroke-width": "1.8"},
    )
    svg.append(_text(ix + iw / 2, iy + ih + 12, "ms", size="9", anchor="middle", fill=COLOR_MUTED))

    # sampling glyph off the 14 s plot, as a labeled note not a second time axis
    svg.append(_rect(70, 648, 720, 18, fill="#fff", stroke="none"))
    svg.append(
        _text(
            70,
            660,
            "sampling (E046), other panel: next quantitative point ~1 min later — still not a waveform. Authors: basal, not synaptic transients (C031).",
            size="10",
            fill=COLOR_SAMPLE,
        )
    )

    svg.append(
        _text(
            20,
            702,
            "Protocol time ≠ koff (C007 empty). Journal Glu wait and thesis 10 nM plateau are incubation/plateau clocks — caption only, not these axes.",
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
    if frac >= 0.01:
        raise RuntimeError("1.2 ms event unexpectedly occupies a visible fraction of the 14 s axis")
    if shape_reconstructable(clocks.interrogation_s, clocks.sampling_s, clocks.tau_s):
        raise RuntimeError("ledger clocks unexpectedly pass the Nyquist sketch")
    return xml


def write_clock_table(path: Path, clocks: LedgerClocks) -> None:
    rows = [
        {
            "quantity_class": "biological_tau",
            "ledger_id": clocks.tau_id,
            "value_s": f"{clocks.tau_s:.6g}",
            "vs_tau": "1",
            "on_figure": "yes",
            "notes": "literature stimulus timescale; Clements inference E033",
        },
        {
            "quantity_class": "interrogation",
            "ledger_id": clocks.interrogation_id,
            "value_s": f"{clocks.interrogation_s:.6g}",
            "vs_tau": f"{clock_ratio(clocks.interrogation_s, clocks.tau_s):.6g}",
            "on_figure": "yes",
            "notes": "ACV scan clock; ratio is T/tau not koff",
        },
        {
            "quantity_class": "sampling",
            "ledger_id": clocks.sampling_id,
            "value_s": f"{clocks.sampling_s:.6g}",
            "vs_tau": f"{clock_ratio(clocks.sampling_s, clocks.tau_s):.6g}",
            "on_figure": "yes",
            "notes": "retina sampling interval after insertion",
        },
        {
            "quantity_class": "incubation",
            "ledger_id": clocks.incubation_id,
            "value_s": f"{clocks.incubation_s:.6g}",
            "vs_tau": f"{clock_ratio(clocks.incubation_s, clocks.tau_s):.6g}",
            "on_figure": "no",
            "notes": "journal 15 min Glu wait C006/E008; off-figure protocol time",
        },
        {
            "quantity_class": "plateau",
            "ledger_id": clocks.plateau_id,
            "value_s": f"{clocks.plateau_s:.6g}",
            "vs_tau": f"{clock_ratio(clocks.plateau_s, clocks.tau_s):.6g}",
            "on_figure": "no",
            "notes": "thesis 10 min 10 nM plateau C028/E042; off-figure protocol time",
        },
        {
            "quantity_class": "nyquist_sketch",
            "ledger_id": "derived_from_E033",
            "value_s": f"{nyquist_interval_s(clocks.tau_s):.6g}",
            "vs_tau": "0.5",
            "on_figure": "yes",
            "notes": "COMPUTATIONAL ILLUSTRATION tau/2; not a sensor spec",
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
    svg = nyquist_svg(clocks)
    caption = caption_text(clocks)
    _assert_clean_text(svg)
    _assert_clean_text(caption)
    (out / "nyquist.svg").write_text(svg, encoding="utf-8")
    (out / "CAPTION.md").write_text(caption, encoding="utf-8")
    write_clock_table(ROOT / "tables" / "clocks.csv", clocks)
    table = (ROOT / "tables" / "clocks.csv").read_text(encoding="utf-8")
    _assert_clean_text(table)
    print(out / "nyquist.svg")
    print(out / "CAPTION.md")


if __name__ == "__main__":
    main()
