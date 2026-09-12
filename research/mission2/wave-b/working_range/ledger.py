#!/usr/bin/env python3
"""Parse glutamate-aptamer analytical_working_range rows from the in-repo ledger.

Bars copy ledger spans. Fold-below ratios are MODELED ledger arithmetic.
Empty numerical_result cells are omitted, not filled. Occupancy θ is not a bar.
Herman 25 nM and Clements 1.1 mM are separate named examples, not one device spec.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

from units import parse_conc_value_units, extract_span_displays, parse_span

# Join range row → sensor_LOD on the same construct/matrix only.
# Ames (E044 numerical_result) has no Ames LOD in the ledger: leave empty.
# Do not pair E043 0.3 pM (PBS) with the Ames bar. Do not pair E006 serum LOD
# with the PBS MEA range.
LOD_FOR_RANGE: dict[tuple[str, str], str | None] = {
    ("E003", "numerical_result"): "E002",
    ("E007", "numerical_result"): "E005",
    ("E026", "numerical_result"): "E025",
    ("E041", "numerical_result"): "E040",
    ("E044", "numerical_result"): None,
    ("E044", "comparator"): "E043",
}

SHORT_LABEL = {
    ("E003", "numerical_result"): "glu1 E-AB (abstract; matrix unspecified)",
    ("E007", "numerical_result"): "Hu AuED-MEA, PBS",
    ("E026", "numerical_result"): "Xiao CNT FET, 0.1× PBS",
    ("E041", "numerical_result"): "Abrantes NG-Apt-Glu FET, aCSF (preprint)",
    ("E044", "numerical_result"): "Hu PaC probe, Ames (retina bath)",
    ("E044", "comparator"): "Hu PaC probe, PBS (E044 comparator window)",
}

DISPLAY_ORDER = [
    ("E041", "numerical_result"),
    ("E003", "numerical_result"),
    ("E026", "numerical_result"),
    ("E007", "numerical_result"),
    ("E044", "comparator"),
    ("E044", "numerical_result"),
]

# Canonical poles from core_evidence.csv only. Clements is not a basal.
CANONICAL_POLE_SPECS = (
    {
        "pole_id": "herman_tonic",
        "evidence_id": "E034",
        "claim_id": "C012",
        "quantity_type": "biological_concentration_range",
        "stamp": "INFERRED",
        "label": "Herman ~25 nM ambient (acute hippocampal slice NMDAR)",
        "role": "canonical_basal_example",
    },
    {
        "pole_id": "herman_nmdar_ec50",
        "evidence_id": "E035",
        "claim_id": "",
        "quantity_type": "EC50",
        "stamp": "INFERRED",
        "label": "Herman NMDAR Glu EC50 1.8 µM (converted from NMDA 37.7 µM; not Hu 1.8 nM)",
        "role": "receptor_ec50_not_basal",
    },
    {
        "pole_id": "clements_cleft",
        "evidence_id": "E032",
        "claim_id": "C011",
        "quantity_type": "biological_concentration_range",
        "stamp": "INFERRED",
        "label": "Clements 1.1 mM peak (cultured hippocampal synapses)",
        "role": "canonical_cleft_example_not_basal",
    },
)


@dataclass(frozen=True)
class RangeBar:
    row_id: str
    evidence_id: str
    span_field: str
    label: str
    construct: str
    matrix: str
    lo_M: float
    hi_M: float
    lo_display: str
    hi_display: str
    source_id: str
    lod_id: str
    lod_M: float | None
    lod_display: str
    lod_matrix: str
    lod_quantity_type: str
    stamp: str


@dataclass(frozen=True)
class CanonicalPole:
    pole_id: str
    evidence_id: str
    claim_id: str
    quantity_type: str
    stamp: str
    label: str
    role: str
    value_M: float
    display: str
    status: str


def find_repo(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "research/evidence/core_evidence.csv").is_file():
            return candidate
    raise FileNotFoundError("core_evidence.csv not found above " + str(start))


def load_ledger(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["evidence_id"]: row for row in csv.DictReader(handle)}


def _lod_fields(ledger: dict[str, dict[str, str]], range_key: tuple[str, str]) -> tuple[str, float | None, str, str, str]:
    lod_id = LOD_FOR_RANGE.get(range_key)
    if not lod_id:
        return "", None, "", "", ""
    rec = ledger.get(lod_id)
    if not rec:
        return "", None, "", "", ""
    if (rec.get("quantity_type") or "").strip() != "sensor_LOD":
        return "", None, "", "", ""
    value = (rec.get("numerical_result") or "").strip()
    if not value:
        return "", None, "", "", ""
    conc = parse_conc_value_units(value, rec.get("units") or "")
    if conc is None:
        return "", None, "", "", ""
    display = f"{value} {(rec.get('units') or '').strip()}".strip()
    return lod_id, conc, display, rec.get("matrix") or "", "sensor_LOD"


def _bar_from_record(
    rec: dict[str, str],
    span_field: str,
    span_text: str,
    ledger: dict[str, dict[str, str]],
    matrix_override: str = "",
) -> RangeBar | None:
    parsed = parse_span(span_text)
    displays = extract_span_displays(span_text)
    if parsed is None or displays is None:
        return None
    eid = rec["evidence_id"]
    key = (eid, span_field)
    lod_id, lod_M, lod_display, lod_matrix, lod_q = _lod_fields(ledger, key)
    matrix = matrix_override or rec.get("matrix") or ""
    stamp = "MEASURED"
    if eid in {"E003", "E041"}:
        stamp = "MEASURED"  # as advertised; abstract/preprint caveats live in notes
    return RangeBar(
        row_id=f"{eid}:{span_field}",
        evidence_id=eid,
        span_field=span_field,
        label=SHORT_LABEL.get(key, f"{rec.get('aptamer_construct') or eid} | {matrix}"),
        construct=rec.get("aptamer_construct") or "",
        matrix=matrix,
        lo_M=parsed[0],
        hi_M=parsed[1],
        lo_display=displays[0],
        hi_display=displays[1],
        source_id=rec.get("source_id") or "",
        lod_id=lod_id,
        lod_M=lod_M,
        lod_display=lod_display,
        lod_matrix=lod_matrix,
        lod_quantity_type=lod_q,
        stamp=stamp,
    )


def load_range_bars(ledger: dict[str, dict[str, str]]) -> list[RangeBar]:
    """Copy analytical_working_range numerical_result spans. Omit if empty/unparseable.

    Extra PBS PaC bar: E044 comparator text 'PBS 1 nM-1 mM linear window' is already
    in the ledger. It is not a dedicated analytical_working_range numerical_result.
    E026 comparator (interferent span) is not read.
    """
    bars: list[RangeBar] = []
    for rec in ledger.values():
        if (rec.get("quantity_type") or "").strip() != "analytical_working_range":
            continue
        text = (rec.get("numerical_result") or "").strip()
        if not text:
            continue
        bar = _bar_from_record(rec, "numerical_result", text, ledger)
        if bar is not None:
            bars.append(bar)

    e044 = ledger.get("E044")
    if e044:
        bar = _bar_from_record(
            e044,
            "comparator",
            e044.get("comparator") or "",
            ledger,
            matrix_override="PBS (E044 comparator; not Ames)",
        )
        if bar is not None:
            bars.append(bar)

    rank = {key: i for i, key in enumerate(DISPLAY_ORDER)}

    def sort_key(bar: RangeBar) -> tuple[int, str]:
        return rank.get((bar.evidence_id, bar.span_field), 1000), bar.row_id

    bars.sort(key=sort_key)
    return bars


def load_canonical_poles(ledger: dict[str, dict[str, str]]) -> list[CanonicalPole]:
    poles: list[CanonicalPole] = []
    for spec in CANONICAL_POLE_SPECS:
        rec = ledger.get(spec["evidence_id"])
        if not rec:
            continue
        if (rec.get("quantity_type") or "").strip() != spec["quantity_type"]:
            continue
        value = (rec.get("numerical_result") or "").strip()
        if not value:
            continue
        conc = parse_conc_value_units(value, rec.get("units") or "")
        if conc is None:
            continue
        display = f"{value} {(rec.get('units') or '').strip()}".strip()
        poles.append(
            CanonicalPole(
                pole_id=spec["pole_id"],
                evidence_id=spec["evidence_id"],
                claim_id=spec["claim_id"],
                quantity_type=spec["quantity_type"],
                stamp=spec["stamp"],
                label=spec["label"],
                role=spec["role"],
                value_M=conc,
                display=display,
                status="canonical_ledger",
            )
        )
    return poles


def pole_by_id(poles: list[CanonicalPole], pole_id: str) -> CanonicalPole | None:
    for pole in poles:
        if pole.pole_id == pole_id:
            return pole
    return None
