#!/usr/bin/env python3
"""Load A4 clocks from the swarm ledgers. No invented glutamate kon/koff."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


def find_repo(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "research/evidence/core_evidence.csv").is_file():
            return candidate
    raise FileNotFoundError("core_evidence.csv not found above " + str(start))


REPO = find_repo(Path(__file__).resolve())
EVIDENCE_CSV = REPO / "research/evidence/core_evidence.csv"
CLAIMS_CSV = REPO / "state/claims.csv"

# Pins to the current ledger snapshot. If a number moves, tests fail; do not
# silently keep a stale value. These are not new measurements.
PINNED = {
    "E033": ("1.2", "ms"),       # Clements τ (stored as response_time)
    "E032": ("1.1", "mM"),       # Clements inferred peak
    "E034": ("25", "nM"),        # Herman ambient; pulse floor of the literature stimulus
    "E045": ("14", "s"),         # ACV interrogation / scan
    "E046": ("1", "min"),        # retina sampling interval
    "E008": ("15", "min"),       # journal Glu incubation; off-figure
    "E042": ("10", "min"),       # thesis 10 nM plateau; off-figure
}

TO_SECONDS = {"s": 1.0, "ms": 1e-3, "min": 60.0}
TO_MOLAR = {"M": 1.0, "mM": 1e-3, "µM": 1e-6, "uM": 1e-6, "nM": 1e-9, "pM": 1e-12}


@dataclass(frozen=True)
class LedgerClocks:
    tau_s: float
    peak_m: float
    basal_m: float
    interrogation_s: float
    sampling_s: float
    incubation_s: float
    plateau_s: float
    tau_id: str
    peak_id: str
    basal_id: str
    interrogation_id: str
    sampling_id: str
    incubation_id: str
    plateau_id: str
    c031_text: str


def load_csv(path: Path, key: str) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {row[key]: row for row in csv.DictReader(handle)}


def _pinned_value(rows: dict[str, dict[str, str]], eid: str, field: str) -> str:
    if eid not in rows:
        raise KeyError(f"missing {eid} in ledger")
    expected_value, expected_units = PINNED[eid]
    got_value = rows[eid][field].strip()
    got_units = rows[eid]["units"].strip()
    if got_value != expected_value or got_units != expected_units:
        raise ValueError(
            f"{eid} pin failed: expected {expected_value} {expected_units}, "
            f"got {got_value} {got_units}"
        )
    return got_value


def _to_seconds(value: str, units: str) -> float:
    if units not in TO_SECONDS:
        raise ValueError(f"unhandled time unit {units!r}")
    return float(value) * TO_SECONDS[units]


def _to_molar(value: str, units: str) -> float:
    if units not in TO_MOLAR:
        raise ValueError(f"unhandled concentration unit {units!r}")
    return float(value) * TO_MOLAR[units]


def load_clocks(evidence_csv: Path | None = None, claims_csv: Path | None = None) -> LedgerClocks:
    evidence = load_csv(evidence_csv or EVIDENCE_CSV, "evidence_id")
    claims = load_csv(claims_csv or CLAIMS_CSV, "claim_id")
    if "C031" not in claims:
        raise KeyError("missing C031")
    c031 = claims["C031"]["claim_text"]
    if "not synaptic transients" not in c031.lower() and "not synaptic" not in c031.lower():
        raise ValueError("C031 no longer states the basal-not-synaptic refusal")

    tau_s = _to_seconds(_pinned_value(evidence, "E033", "numerical_result"), PINNED["E033"][1])
    peak_m = _to_molar(_pinned_value(evidence, "E032", "numerical_result"), PINNED["E032"][1])
    basal_m = _to_molar(_pinned_value(evidence, "E034", "numerical_result"), PINNED["E034"][1])
    interrogation_s = _to_seconds(_pinned_value(evidence, "E045", "numerical_result"), PINNED["E045"][1])
    sampling_s = _to_seconds(_pinned_value(evidence, "E046", "numerical_result"), PINNED["E046"][1])
    incubation_s = _to_seconds(_pinned_value(evidence, "E008", "numerical_result"), PINNED["E008"][1])
    plateau_s = _to_seconds(_pinned_value(evidence, "E042", "numerical_result"), PINNED["E042"][1])

    return LedgerClocks(
        tau_s=tau_s,
        peak_m=peak_m,
        basal_m=basal_m,
        interrogation_s=interrogation_s,
        sampling_s=sampling_s,
        incubation_s=incubation_s,
        plateau_s=plateau_s,
        tau_id="E033",
        peak_id="E032",
        basal_id="E034",
        interrogation_id="E045",
        sampling_id="E046",
        incubation_id="E008",
        plateau_id="E042",
        c031_text=c031,
    )
