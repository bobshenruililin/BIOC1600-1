#!/usr/bin/env python3
"""Parse glutamate-aptamer analytical_working_range rows from the in-repo ledger.

Bars copy ledger spans. Fold-below ratios are computational illustration
(SIMULATION/ledger arithmetic). Empty numerical_result cells are omitted,
not filled. Occupancy θ is not computed.
"""

from __future__ import annotations

import csv
import re
import math
from dataclasses import dataclass
from pathlib import Path

PREFIX_TO_M = {
    "a": 1e-18,
    "f": 1e-15,
    "p": 1e-12,
    "n": 1e-9,
    "u": 1e-6,
    "µ": 1e-6,
    "μ": 1e-6,
    "m": 1e-3,
    "": 1.0,
}

CONC_TOKEN_RE = re.compile(
    r"([0-9]+(?:\.[0-9]+)?)\s*([aAfFpPnNuUµμ]|m)?M"
)
SPAN_RE = re.compile(
    r"([0-9]+(?:\.[0-9]+)?\s*[aAfFpPnNuUµμm]?M)"
    r"\s*[–—−-]\s*"
    r"([0-9]+(?:\.[0-9]+)?\s*[aAfFpPnNuUµμm]?M)"
)

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

POLE_SPECS = (
    {
        "pole_id": "herman_tonic",
        "evidence_id": "E034",
        "claim_id": "C012",
        "quantity_type": "biological_concentration_range",
        "label": "Herman ~25 nM tonic (slice)",
    },
    {
        "pole_id": "herman_nmdar_ec50",
        "evidence_id": "E035",
        "claim_id": "",
        "quantity_type": "EC50",
        "label": "Herman NMDAR EC50 1.8 µM",
    },
    {
        "pole_id": "clements_cleft",
        "evidence_id": "E032",
        "claim_id": "C011",
        "quantity_type": "biological_concentration_range",
        "label": "Clements 1.1 mM cleft (inference)",
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


@dataclass(frozen=True)
class Pole:
    pole_id: str
    evidence_id: str
    claim_id: str
    quantity_type: str
    label: str
    value_M: float
    display: str


def find_repo(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "research/evidence/core_evidence.csv").is_file():
            return candidate
    raise FileNotFoundError("core_evidence.csv not found above " + str(start))


def load_ledger(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["evidence_id"]: row for row in csv.DictReader(handle)}


def parse_conc_token(token: str) -> float | None:
    text = (token or "").strip()
    match = re.fullmatch(CONC_TOKEN_RE, text)
    if not match:
        return None
    coef = float(match.group(1))
    raw_prefix = match.group(2) or ""
    key = raw_prefix.replace("μ", "µ")
    if key == "µ":
        key = "u"
    else:
        key = key.lower()
    if key not in PREFIX_TO_M:
        return None
    return coef * PREFIX_TO_M[key]


def parse_conc_value_units(value: str, units: str) -> float | None:
    value = (value or "").strip()
    units = (units or "").strip()
    if not value:
        return None
    if units.lower() == "span":
        return None
    token = f"{value} {units}".strip()
    return parse_conc_token(token)


def extract_span_displays(text: str) -> tuple[str, str] | None:
    match = SPAN_RE.search(text or "")
    if not match:
        return None
    return match.group(1).strip(), match.group(2).strip()


def parse_span(text: str) -> tuple[float, float] | None:
    displays = extract_span_displays(text)
    if displays is None:
        return None
    lo = parse_conc_token(displays[0])
    hi = parse_conc_token(displays[1])
    if lo is None or hi is None or lo <= 0 or hi <= 0 or lo >= hi:
        return None
    return lo, hi


def format_fold(ratio: float) -> str:
    if ratio <= 0 or not math.isfinite(ratio):
        return ""
    nearest = round(ratio)
    if math.isclose(ratio, nearest, rel_tol=1e-8, abs_tol=1e-8):
        return str(int(nearest))
    nearest_tenth = round(ratio, 1)
    if math.isclose(ratio, nearest_tenth, rel_tol=1e-8, abs_tol=1e-8):
        return f"{nearest_tenth:.1f}"
    return f"{ratio:.3g}"


def contains(lo_M: float, hi_M: float, conc_M: float) -> bool:
    return lo_M <= conc_M <= hi_M


def ceiling_fold_below(hi_M: float, pole_M: float) -> float | None:
    if hi_M < pole_M:
        return pole_M / hi_M
    return None


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
    )


def load_range_bars(ledger: dict[str, dict[str, str]]) -> list[RangeBar]:
    """Copy analytical_working_range numerical_result spans. Omit if empty/unparseable.

    Extra PBS PaC bar: E044 comparator text 'PBS 1 nM-1 mM linear window' is already
    in the ledger. It is not a dedicated analytical_working_range numerical_result.
    If that comparator span cannot be parsed, the PBS bar is omitted.
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


def load_poles(ledger: dict[str, dict[str, str]]) -> list[Pole]:
    poles: list[Pole] = []
    for spec in POLE_SPECS:
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
            Pole(
                pole_id=spec["pole_id"],
                evidence_id=spec["evidence_id"],
                claim_id=spec["claim_id"],
                quantity_type=spec["quantity_type"],
                label=spec["label"],
                value_M=conc,
                display=display,
            )
        )
    return poles


def pole_by_id(poles: list[Pole], pole_id: str) -> Pole | None:
    for pole in poles:
        if pole.pole_id == pole_id:
            return pole
    return None


def verdict_vs_pole(bar: RangeBar, pole: Pole | None) -> dict[str, str]:
    """Ledger arithmetic. Empty strings when the pole is missing (do not invent)."""
    out = {
        "contains": "",
        "ceiling_fold_below": "",
        "note": "",
    }
    if pole is None:
        return out
    if contains(bar.lo_M, bar.hi_M, pole.value_M):
        out["contains"] = "yes"
        return out
    out["contains"] = "no"
    fold = ceiling_fold_below(bar.hi_M, pole.value_M)
    if fold is not None:
        out["ceiling_fold_below"] = format_fold(fold)
        out["note"] = f"ceiling {out['ceiling_fold_below']}-fold below {pole.display}"
    elif bar.lo_M > pole.value_M:
        out["note"] = f"floor above {pole.display}"
    return out


def classify_row(bar: RangeBar, poles: list[Pole]) -> dict[str, str]:
    tonic = pole_by_id(poles, "herman_tonic")
    cleft = pole_by_id(poles, "clements_cleft")
    vs_tonic = verdict_vs_pole(bar, tonic)
    vs_cleft = verdict_vs_pole(bar, cleft)
    return {
        "contains_25nM": vs_tonic["contains"],
        "fold_below_25nM": vs_tonic["ceiling_fold_below"],
        "note_25nM": vs_tonic["note"],
        "contains_1.1mM": vs_cleft["contains"],
        "fold_below_1.1mM": vs_cleft["ceiling_fold_below"],
        "note_1.1mM": vs_cleft["note"],
    }


def glyph_note(bar: RangeBar, poles: list[Pole]) -> str:
    """Short first-year note. Giant cleft folds on bars that already miss 25 nM
    are stored in the table, not printed as theater on the glyph."""
    verdict = classify_row(bar, poles)
    parts: list[str] = []
    if verdict["contains_25nM"] == "yes":
        parts.append("contains 25 nM")
    elif verdict["fold_below_25nM"]:
        parts.append(f"ceiling {verdict['fold_below_25nM']}-fold below 25 nM")
    elif verdict["contains_25nM"] == "no":
        parts.append("misses 25 nM")
    if verdict["contains_1.1mM"] == "yes":
        parts.append("contains 1.1 mM")
    elif verdict["contains_25nM"] == "yes" and verdict["fold_below_1.1mM"]:
        parts.append(f"ceiling {verdict['fold_below_1.1mM']}-fold below 1.1 mM")
    elif verdict["contains_1.1mM"] == "no":
        parts.append("misses 1.1 mM")
    return "; ".join(parts)


def table_rows(bars: list[RangeBar], poles: list[Pole]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for bar in bars:
        verdict = classify_row(bar, poles)
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
                "contains_25nM": verdict["contains_25nM"],
                "fold_below_25nM": verdict["fold_below_25nM"],
                "contains_1.1mM": verdict["contains_1.1mM"],
                "fold_below_1.1mM": verdict["fold_below_1.1mM"],
                "lod_id": bar.lod_id,
                "lod_display": bar.lod_display,
                "lod_matrix": bar.lod_matrix,
                "lod_quantity_type": bar.lod_quantity_type,
                "label_kind": "LEDGER bars; fold columns are SIMULATION/computational illustration",
            }
        )
    return rows
