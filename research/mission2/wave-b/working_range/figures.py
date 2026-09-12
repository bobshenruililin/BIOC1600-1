#!/usr/bin/env python3
"""Working-range bars vs named poles. LEDGER bars; folds MODELED.

Herman 25 nM and Clements 1.1 mM are separate hippocampal literature examples.
They are not spliced into one device specification. Candidate Hershey/Hascup
poles are tagged CANDIDATE. Occupancy θ is not plotted. 81-versus-44000 is
not the flagship glyph.
"""

from __future__ import annotations

import csv
import math
import xml.etree.ElementTree as ET
from pathlib import Path

from candidates import CANDIDATE_POLES
from ledger import (
    CanonicalPole,
    RangeBar,
    find_repo,
    load_canonical_poles,
    load_ledger,
    load_range_bars,
    pole_by_id,
)
from model import (
    occupancy_c10_c90,
    occupancy_span_10_90,
    n_for_span,
    verdict,
)
from units import format_fold

ROOT = Path(__file__).resolve().parent
REPO = find_repo(ROOT)
DEFAULT_CSV = REPO / "research/evidence/core_evidence.csv"

CAPTION = """Figure (Mission 2 Wave B candidate, not accepted): Horizontal bars are reported `analytical_working_range` copied from `research/evidence/core_evidence.csv`. LEDGER calibration windows, not occupancy and not Kd. Fold-below numbers are MODELED ratios (pole / ceiling) when the ceiling is below the pole. Empty LOD cells stay empty. No interpolation.

Quantity types:
- `analytical_working_range` — bars (E003 glu1 0.01 pM–1 nM abstract; E041 Abrantes preprint 1 aM–10 pM aCSF; E026 Xiao 10 fM–100 nM in 0.1× PBS; E007 Hu AuED-MEA 0.1 nM–10 µM PBS; E044 Ames 10 nM–10 µM; E044 comparator PBS 1 nM–1 mM). Ames/PBS PaC spans are ledger pins (S066 OA PDF not re-opened this session).
- `biological_concentration_range` — solid ticks: Herman ~25 nM (C012/E034, INFERRED ambient in acute hippocampal slice; standing currents are MEASURED). Clements 1.1 mM (C011/E032, INFERRED cleft peak at cultured synapses, abstract). These are different hippocampal preparations. They are not one device spec and not a retinal range.
- `EC50` — dashed tick: Herman converted Glu NMDAR EC50 ~1.8 µM (E035). OA this session: NMDA EC50 37.7 µM is MEASURED (nucleated patch Hill fit); × 0.048 conversion ≈ 1.81 µM is INFERRED. Receptor EC50, not Hu electrochemical EC50, not a basal pole.
- `sensor_LOD` — unconnected open dots, same construct/matrix only. E043 0.3 pM is PBS, not Ames. Ames LOD cell empty. Do not bin Hu 32 pM with Wu 0.0013 pM or Abrantes 1 aM.
- CANDIDATE ticks (open): Hershey Capp 9.4 µM (INFERRED), Hershey 144 nM dialysate (MEASURED), Hascup 2010 34.7 µM (MEASURED), Hascup 2008 3.3 / 5.0 µM (MEASURED). Not `claims.csv`. Not averaged with 25 nM.

SI-strict containment: no plotted bar contains both C012 25 nM and C011 1.1 mM. Xiao 100 nM vs 1.1 mM is 11000-fold, not 11-fold. PBS PaC 1 mM is 1.1-fold below 1.1 mM. Ames contains 25 nM and the candidate 3.3 / 5.0 / 9.4 µM poles and misses Hascup 2010 34.7 µM (3.47-fold below). Containment is geometric on the reported span, not SNR-qualified quantification (Ames 41.6% blank noise).

Hu 1.8 nM Langmuir–Freundlich electrochemical EC50 (C005) is not plotted. Occupancy θ is not plotted. Hu fitted n is UNKNOWN. Occupancy 10–90% width is MODELED as 81^(1/n); that algebra does not change device-bar arithmetic and does not restore 81-versus-44000 as flagship.

Not Mission 1 close. Not group-final. Not a polished poster. Not `analysis/accepted/`.
"""

LF_CAPTION = """Figure (MODELED occupancy-window width, not a device bar): For θ = c^n/(Kd^n + c^n) with Kd as c50, the 10–90% occupancy span is exactly 81^(1/n). n=1 → 81; n=0.5 → 6561; n=2 → 9. Hu fitted n is UNKNOWN. 1.8 nM is C005 EC50, not occupancy Kd, so this panel is not PaC tissue occupancy. The withdrawn 81-versus-44000 comparison is not plotted. Pairing Herman 25 nM with Clements 1.1 mM as one device spec is refused even if n were later measured.
"""


def _line(x1, y1, x2, y2, stroke="#333", width="1", dash=""):
    attrib = {
        "x1": str(x1),
        "y1": str(y1),
        "x2": str(x2),
        "y2": str(y2),
        "stroke": stroke,
        "stroke-width": width,
    }
    if dash:
        attrib["stroke-dasharray"] = dash
    return ET.Element("line", attrib=attrib)


def _text(svg, x, y, content, size="11", fill="#111", anchor="start", weight="normal"):
    el = ET.SubElement(
        svg,
        "text",
        attrib={
            "x": str(x),
            "y": str(y),
            "font-size": size,
            "font-family": "sans-serif",
            "fill": fill,
            "text-anchor": anchor,
            "font-weight": weight,
        },
    )
    el.text = content
    return el


def classify_vs_canonical(bar: RangeBar, poles: list[CanonicalPole]) -> dict[str, str]:
    tonic = pole_by_id(poles, "herman_tonic")
    cleft = pole_by_id(poles, "clements_cleft")
    vs_tonic = verdict(bar.lo_M, bar.hi_M, tonic.value_M) if tonic else {"contains": "", "ceiling_fold_below": "", "note": ""}
    vs_cleft = verdict(bar.lo_M, bar.hi_M, cleft.value_M) if cleft else {"contains": "", "ceiling_fold_below": "", "note": ""}
    return {
        "contains_25nM": vs_tonic["contains"],
        "fold_below_25nM": vs_tonic["ceiling_fold_below"],
        "note_25nM": vs_tonic["note"],
        "contains_1.1mM": vs_cleft["contains"],
        "fold_below_1.1mM": vs_cleft["ceiling_fold_below"],
        "note_1.1mM": vs_cleft["note"],
    }


def glyph_note(bar: RangeBar, poles: list[CanonicalPole]) -> str:
    """Canonical C012/C011 notes only. Giant cleft folds on bars that already miss
    25 nM stay in the table. Do not print a 25 nM–1.1 mM device-spec slogan."""
    v = classify_vs_canonical(bar, poles)
    parts: list[str] = []
    if v["contains_25nM"] == "yes":
        parts.append("contains C012 25 nM")
    elif v["fold_below_25nM"]:
        parts.append(f"ceiling {v['fold_below_25nM']}-fold below C012 25 nM")
    elif v["contains_25nM"] == "no":
        parts.append("misses C012 25 nM")
    if v["contains_1.1mM"] == "yes":
        parts.append("contains C011 1.1 mM")
    elif v["contains_25nM"] == "yes" and v["fold_below_1.1mM"]:
        parts.append(f"ceiling {v['fold_below_1.1mM']}-fold below C011 1.1 mM")
    elif v["contains_1.1mM"] == "no":
        parts.append("misses C011 1.1 mM")
    return "; ".join(parts)


def range_table_rows(bars: list[RangeBar], poles: list[CanonicalPole]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for bar in bars:
        v = classify_vs_canonical(bar, poles)
        rows.append(
            {
                "row_id": bar.row_id,
                "evidence_id": bar.evidence_id,
                "span_field": bar.span_field,
                "label": bar.label,
                "construct": bar.construct,
                "matrix": bar.matrix,
                "lo_display": bar.lo_display,
                "hi_display": bar.hi_display,
                "lo_M": f"{bar.lo_M:.6e}",
                "hi_M": f"{bar.hi_M:.6e}",
                "quantity_type": "analytical_working_range",
                "stamp": bar.stamp,
                "contains_C012_25nM": v["contains_25nM"],
                "fold_below_C012_25nM": v["fold_below_25nM"],
                "contains_C011_1.1mM": v["contains_1.1mM"],
                "fold_below_C011_1.1mM": v["fold_below_1.1mM"],
                "lod_id": bar.lod_id,
                "lod_display": bar.lod_display,
                "lod_matrix": bar.lod_matrix,
                "lod_quantity_type": bar.lod_quantity_type,
                "label_kind": "LEDGER bars; fold columns MODELED; C012 and C011 are separate named examples not one device spec",
            }
        )
    return rows


def basal_sensitivity_rows(bars: list[RangeBar], poles: list[CanonicalPole]) -> list[dict[str, str]]:
    tonic = pole_by_id(poles, "herman_tonic")
    cleft = pole_by_id(poles, "clements_cleft")
    rows: list[dict[str, str]] = []

    def add(bar: RangeBar, pole_id: str, status: str, stamp: str, display: str, value_M: float, label: str) -> None:
        v = verdict(bar.lo_M, bar.hi_M, value_M)
        rows.append(
            {
                "bar_id": bar.row_id,
                "bar_label": bar.label,
                "pole_id": pole_id,
                "pole_status": status,
                "pole_stamp": stamp,
                "pole_display": display,
                "pole_label": label,
                "contains": v["contains"],
                "ceiling_fold_below": v["ceiling_fold_below"],
                "note": v["note"],
            }
        )

    for bar in bars:
        if tonic:
            add(bar, tonic.pole_id, tonic.status, tonic.stamp, tonic.display, tonic.value_M, tonic.label)
        if cleft:
            add(bar, cleft.pole_id, cleft.status, cleft.stamp, cleft.display, cleft.value_M, cleft.label)
        for cand in CANDIDATE_POLES:
            add(bar, cand.pole_id, cand.status, cand.stamp, cand.display, cand.value_M, cand.label)
    return rows


def lf_n_rows() -> list[dict[str, str]]:
    rows = []
    for n in (0.5, 0.7, 1.0, 1.5, 2.0):
        span = occupancy_span_10_90(n)
        c10, c90 = occupancy_c10_c90(1.8e-9, n)
        v25 = verdict(c10, c90, 25e-9)
        v11 = verdict(c10, c90, 1.1e-3)
        rows.append(
            {
                "n": f"{n:g}",
                "occupancy_10_90_span": format_fold(span),
                "if_1p8nM_were_c50_c10_M": f"{c10:.6e}",
                "if_1p8nM_were_c50_c90_M": f"{c90:.6e}",
                "illegal_overlay_contains_25nM": v25["contains"],
                "illegal_overlay_contains_1.1mM": v11["contains"],
                "label_kind": "MODELED 81^(1/n); 1.8 nM is C005 EC50 NOT occupancy Kd; overlay is computational illustration",
            }
        )
    return rows


def n_sensitivity_identity_rows() -> list[dict[str, str]]:
    """Inverse n* for named ratios. Labeled. Not a fitted n. Not flagship."""
    specs = (
        ("C011/C012 withdrawn pairing", 1.1e-3 / 25e-9, "WITHDRAWN_PAIRING; two named hippocampal examples; not a device spec"),
        ("C011 / Hershey Capp 9.4 µM", 1.1e-3 / 9.4e-6, "CANDIDATE left pole; unlike quantities; MODELED"),
        ("C011 / Hascup 2010 34.7 µM", 1.1e-3 / 34.7e-6, "CANDIDATE left pole; unlike quantities; MODELED"),
        ("C011 / Hascup 2008 PFC 3.3 µM", 1.1e-3 / 3.3e-6, "CANDIDATE left pole; unlike quantities; MODELED"),
    )
    rows = []
    for name, ratio, note in specs:
        n_star = n_for_span(ratio)
        rows.append(
            {
                "pairing_name": name,
                "concentration_ratio": format_fold(ratio),
                "n_star_ln81_over_ln_ratio": f"{n_star:.6f}",
                "occupancy_span_at_n_star": format_fold(occupancy_span_10_90(n_star)),
                "note": note,
            }
        )
    return rows


def working_range_svg(bars: list[RangeBar], poles: list[CanonicalPole]) -> str:
    width, height = 1320, 700
    plot_x, plot_y = 340, 110
    plot_w, plot_h = 520, 360
    cmin, cmax = 1e-18, 3e-3

    def xmap(conc: float) -> float:
        lg = (math.log10(conc) - math.log10(cmin)) / (math.log10(cmax) - math.log10(cmin))
        return plot_x + lg * plot_w

    svg = ET.Element(
        "svg",
        attrib={
            "xmlns": "http://www.w3.org/2000/svg",
            "width": str(width),
            "height": str(height),
            "viewBox": f"0 0 {width} {height}",
        },
    )
    ET.SubElement(svg, "rect", attrib={"x": "0", "y": "0", "width": str(width), "height": str(height), "fill": "#fff"})
    _text(svg, 16, 22, "analytical_working_range vs named poles — LEDGER bars; folds MODELED; not occupancy", size="14", weight="bold")
    _text(svg, 16, 40, "MEASURED bars = advertised calibration spans. C012 25 nM INFERRED (slice NMDAR). C011 1.1 mM INFERRED (culture cleft). Not one device spec.", size="10", fill="#333")
    _text(svg, 16, 56, "No occupancy θ. No 81-versus-44000 flagship. Candidate Hershey/Hascup ticks are not claims.csv. Empty LOD cells stay empty. 0.3 pM is PBS sensor_LOD, not Ames/tissue.", size="10", fill="#333")
    _text(svg, 16, 72, "Quantity types: analytical_working_range (bars), biological_concentration_range (solid ticks), EC50 (dashed), sensor_LOD (open dots), CANDIDATE (dotted).", size="10", fill="#333")

    ET.SubElement(
        svg,
        "rect",
        attrib={"x": str(plot_x), "y": str(plot_y), "width": str(plot_w), "height": str(plot_h), "fill": "#fafafa", "stroke": "#000"},
    )

    # log ticks
    for exp in range(-18, -2):
        x = xmap(10.0**exp)
        svg.append(_line(x, plot_y + plot_h, x, plot_y + plot_h + 6, width="1"))
        if exp in (-18, -15, -12, -9, -6, -3):
            label = { -18: "1 aM", -15: "1 fM", -12: "1 pM", -9: "1 nM", -6: "1 µM", -3: "1 mM"}[exp]
            _text(svg, x, plot_y + plot_h + 20, label, size="10", anchor="middle")
    _text(svg, plot_x + plot_w / 2, plot_y + plot_h + 38, "glutamate concentration (log10)", size="11", anchor="middle")

    nbar = len(bars)
    row_h = plot_h / max(nbar, 1)
    colors = ["#6b4c9a", "#3d5a80", "#2a9d8f", "#e9c46a", "#f4a261", "#264653"]

    tonic = pole_by_id(poles, "herman_tonic")
    cleft = pole_by_id(poles, "clements_cleft")
    nmdar = pole_by_id(poles, "herman_nmdar_ec50")

    # candidate dotted ticks first (behind bars)
    cand_colors = "#6c757d"
    for cand in CANDIDATE_POLES:
        x = xmap(cand.value_M)
        svg.append(_line(x, plot_y, x, plot_y + plot_h, stroke=cand_colors, width="1", dash="2 3"))

    if nmdar:
        x = xmap(nmdar.value_M)
        svg.append(_line(x, plot_y, x, plot_y + plot_h, stroke="#888", width="1.5", dash="6 4"))
    if tonic:
        x = xmap(tonic.value_M)
        svg.append(_line(x, plot_y, x, plot_y + plot_h, stroke="#1d3557", width="2"))
    if cleft:
        x = xmap(cleft.value_M)
        svg.append(_line(x, plot_y, x, plot_y + plot_h, stroke="#9b2226", width="2"))

    for i, bar in enumerate(bars):
        y = plot_y + (i + 0.5) * row_h
        x1, x2 = xmap(bar.lo_M), xmap(bar.hi_M)
        ET.SubElement(
            svg,
            "rect",
            attrib={
                "x": str(min(x1, x2)),
                "y": str(y - 10),
                "width": str(abs(x2 - x1)),
                "height": "20",
                "fill": colors[i % len(colors)],
                "stroke": "#111",
                "fill-opacity": "0.85",
            },
        )
        if bar.lod_M is not None:
            lx = xmap(bar.lod_M)
            ET.SubElement(
                svg,
                "circle",
                attrib={"cx": str(lx), "cy": str(y), "r": "4.5", "fill": "none", "stroke": "#111", "stroke-width": "1.5"},
            )
        _text(svg, plot_x - 10, y + 4, bar.label, size="10", anchor="end")
        _text(svg, plot_x + plot_w + 8, y + 4, glyph_note(bar, poles), size="9", fill="#222")

    # top labels for canonical ticks — separate, no connecting band
    if tonic:
        _text(svg, xmap(tonic.value_M), plot_y - 28, "C012 ~25 nM", size="10", anchor="middle", weight="bold", fill="#1d3557")
        _text(svg, xmap(tonic.value_M), plot_y - 14, "INFERRED slice", size="9", anchor="middle", fill="#1d3557")
    if nmdar:
        _text(svg, xmap(nmdar.value_M), plot_y - 28, "E035 1.8 µM EC50", size="9", anchor="middle", fill="#555")
        _text(svg, xmap(nmdar.value_M), plot_y - 14, "receptor, dashed", size="9", anchor="middle", fill="#555")
    if cleft:
        _text(svg, xmap(cleft.value_M), plot_y - 28, "C011 1.1 mM", size="10", anchor="middle", weight="bold", fill="#9b2226")
        _text(svg, xmap(cleft.value_M), plot_y - 14, "INFERRED culture", size="9", anchor="middle", fill="#9b2226")

    _text(svg, 16, plot_y + plot_h + 64, "CANDIDATE basal ticks (dotted; not averaged; not retina): Hershey Capp 9.4 µM INFERRED; Hershey 144 nM dialysate MEASURED; Hascup 2008 3.3 / 5.0 µM MEASURED; Hascup 2010 34.7 µM MEASURED.", size="10", fill="#444")
    _text(svg, 16, plot_y + plot_h + 82, "Ames 10 nM–10 µM contains C012 25 nM and candidate 3.3 / 5.0 / 9.4 µM, and misses Hascup 2010 34.7 µM. No bar contains C011 1.1 mM (PBS 1 mM is 1.1-fold short). UNKNOWN: Hu n; PaC occupancy; retinal [Glu]. PROPOSED: 39-mer isotherm reporting n.", size="10", fill="#444")
    _text(svg, 16, plot_y + plot_h + 100, "Open circles = sensor_LOD, same construct/matrix. Ames LOD empty. 0.3 pM PBS LOD (not Ames). Hu electrochemical EC50 not plotted.", size="10", fill="#444")
    _text(svg, 16, height - 18, "Not accepted flagship. Withdrawn occupancy-span pairing is not this glyph. Isolated Mission 2 Wave B candidate.", size="10", fill="#666")

    return ET.tostring(svg, encoding="unicode")


def lf_n_svg() -> str:
    width, height = 720, 420
    plot_x, plot_y, plot_w, plot_h = 70, 50, 500, 280
    nmin, nmax = 0.45, 2.4
    ymin, ymax = 4.0, 2e4  # occupancy fold

    def xmap(n: float) -> float:
        return plot_x + (n - nmin) / (nmax - nmin) * plot_w

    def ymap(span: float) -> float:
        lg = (math.log10(span) - math.log10(ymin)) / (math.log10(ymax) - math.log10(ymin))
        y = plot_y + plot_h * (1 - lg)
        return min(max(y, plot_y), plot_y + plot_h)

    svg = ET.Element("svg", attrib={"xmlns": "http://www.w3.org/2000/svg", "width": str(width), "height": str(height)})
    ET.SubElement(svg, "rect", attrib={"x": "0", "y": "0", "width": str(width), "height": str(height), "fill": "#fff"})
    _text(svg, 16, 22, "MODELED occupancy 10–90% span = 81^(1/n)  — not a device bar; withdrawn pairing not plotted", size="12", weight="bold")
    ET.SubElement(svg, "rect", attrib={"x": str(plot_x), "y": str(plot_y), "width": str(plot_w), "height": str(plot_h), "fill": "#fafafa", "stroke": "#000"})

    ns = [nmin + i * 0.02 for i in range(int((nmax - nmin) / 0.02) + 1)]
    pts = " ".join(f"{xmap(n):.2f},{ymap(occupancy_span_10_90(n)):.2f}" for n in ns)
    ET.SubElement(svg, "polyline", attrib={"points": pts, "fill": "none", "stroke": "#1d3557", "stroke-width": "2"})

    # mark n=1 → 81 only (the Langmuir case). Do not mark 44000.
    svg.append(_line(xmap(1.0), plot_y, xmap(1.0), plot_y + plot_h, stroke="#2a9d8f", width="1.5", dash="4 3"))
    svg.append(_line(plot_x, ymap(81), plot_x + plot_w, ymap(81), stroke="#2a9d8f", width="1", dash="4 3"))
    _text(svg, xmap(1.0) + 6, ymap(81) - 8, "n=1 → 81-fold", size="11", fill="#1d3557")

    for nlab, slabel in ((0.5, "n=0.5 → 6561"), (2.0, "n=2 → 9")):
        ET.SubElement(svg, "circle", attrib={"cx": str(xmap(nlab)), "cy": str(ymap(occupancy_span_10_90(nlab))), "r": "4", "fill": "#e76f51"})
        _text(svg, xmap(nlab) + 8, ymap(occupancy_span_10_90(nlab)) + 4, slabel, size="10")

    _text(svg, plot_x + plot_w / 2, plot_y + plot_h + 28, "Langmuir–Freundlich n (UNKNOWN for Hu)", size="11", anchor="middle")
    _text(svg, 16, plot_y + plot_h / 2, "10–90 fold", size="10", anchor="middle")
    # rotate-like placement: just put y-axis ticks
    for span in (9, 81, 6561):
        _text(svg, plot_x - 8, ymap(span) + 4, str(span), size="9", anchor="end")

    _text(svg, 16, height - 36, "Hu n UNKNOWN. C005 electrochemical EC50 is not occupancy Kd. Measuring n does not license Herman+Clements as a device spec.", size="10", fill="#333")
    _text(svg, 16, height - 18, "UNKNOWN: fitted n. PROPOSED: report n on the exact 39-mer isotherm. Not analysis/accepted/.", size="10", fill="#333")
    return ET.tostring(svg, encoding="unicode")


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    ledger = load_ledger(DEFAULT_CSV)
    bars = load_range_bars(ledger)
    poles = load_canonical_poles(ledger)

    fig_dir = ROOT / "figures"
    tab_dir = ROOT / "tables"
    fig_dir.mkdir(parents=True, exist_ok=True)
    tab_dir.mkdir(parents=True, exist_ok=True)

    (fig_dir / "working_range.svg").write_text(working_range_svg(bars, poles), encoding="utf-8")
    (fig_dir / "lf_n_span.svg").write_text(lf_n_svg(), encoding="utf-8")
    (fig_dir / "CAPTION.md").write_text(CAPTION.strip() + "\n\n" + LF_CAPTION.strip() + "\n", encoding="utf-8")

    _write_csv(tab_dir / "range_table.csv", range_table_rows(bars, poles))
    _write_csv(tab_dir / "basal_pole_sensitivity.csv", basal_sensitivity_rows(bars, poles))
    _write_csv(tab_dir / "lf_n_span.csv", lf_n_rows())
    _write_csv(tab_dir / "n_star_named_ratios.csv", n_sensitivity_identity_rows())


if __name__ == "__main__":
    main()
