#!/usr/bin/env python3
"""Working-range bars vs biological poles. LEDGER bars; fold marks are SIMULATION."""

from __future__ import annotations

import csv
import math
import xml.etree.ElementTree as ET
from pathlib import Path

from ledger import (
    RangeBar,
    find_repo,
    glyph_note,
    load_ledger,
    load_poles,
    load_range_bars,
    pole_by_id,
    table_rows,
)

ROOT = Path(__file__).resolve().parent
REPO = find_repo(ROOT)
DEFAULT_CSV = REPO / "research/evidence/core_evidence.csv"


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


def working_range_svg(bars: list[RangeBar], poles) -> str:
    width, height = 1180, 610
    plot_x, plot_y = 330, 96
    plot_w, plot_h = 440, 340
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
    ET.SubElement(
        svg,
        "rect",
        attrib={"x": "0", "y": "0", "width": str(width), "height": str(height), "fill": "#fff"},
    )
    _text(
        svg,
        16,
        22,
        "analytical_working_range vs biological poles — LEDGER bars; folds are SIMULATION",
        size="14",
        weight="bold",
    )
    _text(
        svg,
        16,
        40,
        "Quantity types: analytical_working_range (bars), biological_concentration_range (solid ticks), EC50 (dashed tick), sensor_LOD (unconnected dots).",
        size="10",
        fill="#333",
    )
    _text(
        svg,
        16,
        56,
        "No occupancy θ. Constructs/matrices are not binned. Empty LOD cells stay empty. 0.3 pM is PBS sensor_LOD, not Ames/tissue.",
        size="10",
        fill="#333",
    )

    ET.SubElement(
        svg,
        "rect",
        attrib={
            "x": str(plot_x),
            "y": str(plot_y),
            "width": str(plot_w),
            "height": str(plot_h),
            "fill": "#fafafa",
            "stroke": "#000",
        },
    )

    decades = [
        (1e-18, "1 aM"),
        (1e-15, "1 fM"),
        (1e-12, "1 pM"),
        (1e-9, "1 nM"),
        (1e-6, "1 µM"),
        (1e-3, "1 mM"),
    ]
    for conc, lab in decades:
        x = xmap(conc)
        svg.append(_line(x, plot_y, x, plot_y + plot_h, "#ddd", "1"))
        _text(svg, x, plot_y + plot_h + 16, lab, size="10", anchor="middle")
    _text(
        svg,
        plot_x + plot_w / 2,
        plot_y + plot_h + 34,
        "log10 [glutamate] / M   (axis is concentration, not occupancy)",
        size="11",
        anchor="middle",
    )

    tonic = pole_by_id(poles, "herman_tonic")
    nmdar = pole_by_id(poles, "herman_nmdar_ec50")
    cleft = pole_by_id(poles, "clements_cleft")

    if tonic is not None:
        svg.append(_line(xmap(tonic.value_M), plot_y, xmap(tonic.value_M), plot_y + plot_h, "#1b7f3a", "2"))
    if nmdar is not None:
        svg.append(_line(xmap(nmdar.value_M), plot_y, xmap(nmdar.value_M), plot_y + plot_h, "#666", "1.5", dash="5 4"))
    if cleft is not None:
        svg.append(_line(xmap(cleft.value_M), plot_y, xmap(cleft.value_M), plot_y + plot_h, "#a31d1d", "2"))

    n = max(len(bars), 1)
    row_h = plot_h / n
    for i, bar in enumerate(bars):
        y = plot_y + i * row_h + row_h / 2
        is_ames = bar.evidence_id == "E044" and bar.span_field == "numerical_result"
        fill = "#1f6f8b" if is_ames else "#4c78a8"
        x1 = xmap(bar.lo_M)
        x2 = xmap(bar.hi_M)
        ET.SubElement(
            svg,
            "rect",
            attrib={
                "x": f"{x1:.2f}",
                "y": str(y - 9),
                "width": f"{max(x2 - x1, 1):.2f}",
                "height": "18",
                "fill": fill,
                "stroke": "#123",
                "stroke-width": "1.2" if is_ames else "0.8",
            },
        )
        if bar.lod_M is not None:
            cx = xmap(bar.lod_M)
            cy = y + 16
            ET.SubElement(
                svg,
                "circle",
                attrib={
                    "cx": f"{cx:.2f}",
                    "cy": str(cy),
                    "r": "4.5",
                    "fill": "none",
                    "stroke": "#6a3d9a",
                    "stroke-width": "1.6",
                },
            )
            lod_note = bar.lod_display
            if bar.lod_id == "E043":
                lod_note = "0.3 pM PBS LOD (not Ames)"
            _text(svg, cx + 8, cy + 3, lod_note, size="8", fill="#6a3d9a")

        _text(svg, 12, y + 4, bar.label, size="11")
        _text(svg, 12, y + 18, f"{bar.lo_display}–{bar.hi_display}  {bar.evidence_id}", size="9", fill="#444")
        _text(svg, plot_x + plot_w + 12, y + 4, glyph_note(bar, poles), size="9", fill="#222")

    axis_lab_y = plot_y + plot_h + 48
    if tonic is not None:
        _text(svg, xmap(tonic.value_M), axis_lab_y, "25 nM tonic", size="9", fill="#1b7f3a", anchor="middle")
        _text(svg, xmap(tonic.value_M), axis_lab_y + 12, f"{tonic.claim_id}/{tonic.evidence_id}", size="8", fill="#1b7f3a", anchor="middle")
    if nmdar is not None:
        _text(svg, xmap(nmdar.value_M) + 36, axis_lab_y, "NMDAR EC50 1.8 µM", size="9", fill="#555", anchor="middle")
        _text(svg, xmap(nmdar.value_M) + 36, axis_lab_y + 12, f"{nmdar.evidence_id} not aptamer Kd", size="8", fill="#555", anchor="middle")
    if cleft is not None:
        _text(svg, xmap(cleft.value_M) + 8, axis_lab_y, "1.1 mM cleft", size="9", fill="#a31d1d", anchor="start")
        _text(svg, xmap(cleft.value_M) + 8, axis_lab_y + 12, f"{cleft.claim_id}/{cleft.evidence_id}", size="8", fill="#a31d1d", anchor="start")

    legend_y = 548
    ET.SubElement(svg, "rect", attrib={"x": "16", "y": str(legend_y), "width": "18", "height": "10", "fill": "#4c78a8"})
    _text(svg, 38, legend_y + 9, "analytical_working_range bar (ledger copy)", size="10")
    ET.SubElement(svg, "rect", attrib={"x": "320", "y": str(legend_y), "width": "18", "height": "10", "fill": "#1f6f8b", "stroke": "#123"})
    _text(svg, 342, legend_y + 9, "Ames bar (matrix of the retina experiment)", size="10")
    ET.SubElement(
        svg,
        "circle",
        attrib={"cx": "640", "cy": str(legend_y + 5), "r": "4.5", "fill": "none", "stroke": "#6a3d9a", "stroke-width": "1.6"},
    )
    _text(svg, 650, legend_y + 9, "sensor_LOD (unconnected; not a range endpoint)", size="10")
    _text(
        svg,
        16,
        574,
        "Hippocampal poles overlaid on aptamer calibrations: literature comparison, not a retina [Glu] measurement. Transferable: no.",
        size="10",
        fill="#444",
    )
    _text(
        svg,
        16,
        590,
        "PBS 1 nM–1 mM is E044 comparator text, not a dedicated range numerical_result. 1.1 mM sits 1.1-fold above that 1 mM ceiling (SI-strict).",
        size="10",
        fill="#444",
    )
    return ET.tostring(svg, encoding="unicode")


CAPTION = """Figure (A3): Horizontal bars are reported `analytical_working_range` copied from `research/evidence/core_evidence.csv`. This is a LEDGER plot of calibration windows, not an occupancy figure and not a Kd figure. Fold-below annotations are SIMULATION / computational illustration (ratio of a literature pole to a reported ceiling). No interpolation. Empty cells stay empty.

Quantity types on this figure:
- `analytical_working_range` — bars (E003 glu1 0.01 pM–1 nM; E041 Abrantes preprint 1 aM–10 pM; E026 Xiao 10 fM–100 nM in 0.1× PBS; E007 Hu AuED-MEA 0.1 nM–10 µM in PBS; E044 Ames 10 nM–10 µM; E044 comparator PBS 1 nM–1 mM linear window).
- `biological_concentration_range` — solid vertical ticks: Herman ~25 nM tonic (C012/E034, hippocampal slice); Clements 1.1 mM cleft inference (C011/E032, cultured synapses). These are not retina measurements.
- `EC50` — dashed tick: Herman NMDAR EC50 1.8 µM (E035). Receptor EC50, not an aptamer Kd, not Hu 1.8 nM.
- `sensor_LOD` — unconnected open dots, paired only to the same construct/matrix. E043 0.3 pM is PBS calibration LOD (C029), not an Ames or tissue LOD. Ames has no sensor_LOD in the ledger, so that cell stays empty. Do not bin Hu 32 pM (E005) with Wu 0.0013 pM (E002) or Abrantes 1 aM (E040).

SI-strict containment (do not round 1.1 mM to 1 mM): no plotted bar contains both 25 nM and 1.1 mM. The PBS PaC ceiling is 1 mM, which is 1.1-fold below 1.1 mM. Ames and Hu MEA ceilings (10 µM) are 110-fold below 1.1 mM. Xiao's 100 nM ceiling is 11000-fold below 1.1 mM (not 11-fold). glu1's 1 nM ceiling is 25-fold below 25 nM; Abrantes' 10 pM ceiling is 2500-fold below 25 nM.

Hu electrochemical apparent Kd 1.8 nM is not plotted. Occupancy θ is not plotted. Moussawi 0.02–30 µM is not in `core_evidence.csv` and is not drawn.

Not Mission 1 close. Not group-final. Not a polished poster.
"""


def write_table(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main(csv_path: Path = DEFAULT_CSV) -> None:
    ledger = load_ledger(csv_path)
    bars = load_range_bars(ledger)
    poles = load_poles(ledger)
    out = ROOT / "figures"
    out.mkdir(exist_ok=True)
    (out / "working_range.svg").write_text(working_range_svg(bars, poles), encoding="utf-8")
    (out / "CAPTION.md").write_text(CAPTION, encoding="utf-8")
    write_table(ROOT / "tables" / "range_table.csv", table_rows(bars, poles))
    print(out / "working_range.svg")


if __name__ == "__main__":
    main()
