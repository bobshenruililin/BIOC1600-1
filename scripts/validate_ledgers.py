#!/usr/bin/env python3
"""Validate swarm CSV/JSON ledgers and locked-file hashes."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CLAIM_TAGS = {
    "primary-source-supported",
    "review-supported",
    "computational illustration",
    "hypothesis",
    "proposed experiment",
    "unresolved",
}

QUANTITY_TYPES = {
    "Kd_molecular",
    "kon",
    "koff",
    "EC50",
    "sensor_LOD",
    "analytical_working_range",
    "signal_gain",
    "response_time",
    "measurement_time",
    "biological_concentration_range",
    "",
}

INSPECTED = {"yes", "partial", "no", ""}
SOURCE_STATUS = {"candidate", "relevant", "core", "rejected", ""}
SOURCE_TYPES = {"primary", "review", "computational", "preprint", ""}
TRANSFERABLE = {"yes", "no", "unknown", ""}

PMID_RE = re.compile(r"^\d+$")
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)

LOCKED = [
    ".cursor/rules/research-constitution.mdc",
    ".cursor/rules/scoring-rubric.mdc",
    ".cursor/rules/safety-and-integrity.mdc",
]

SOURCES_FIELDS = [
    "source_id",
    "doi",
    "pmid",
    "pmcid",
    "title",
    "year",
    "journal",
    "authors",
    "source_type",
    "full_text_inspected",
    "access_route",
    "scout_lane",
    "status",
    "rejection_reason",
    "nominating_agent",
    "notes",
]

CLAIMS_FIELDS = [
    "claim_id",
    "claim_text",
    "evidential_status",
    "source_id",
    "locator",
    "quantity_type",
    "value",
    "units",
    "construct",
    "system",
    "transferable",
    "notes",
]

EVIDENCE_FIELDS = [
    "evidence_id",
    "source_id",
    "extractor_id",
    "system",
    "aptamer_construct",
    "experimental_manipulation",
    "comparator",
    "quantity_type",
    "numerical_result",
    "units",
    "matrix",
    "limitation",
    "locator",
    "full_text_inspected",
]

GUESS_TOKENS = {"TODO", "TBD", "approx", "estimated", "~", "n/a", "NA", "N/A"}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"{path} has no header")
        rows = list(reader)
        return list(reader.fieldnames), rows


def check_ids(rows: list[dict[str, str]], field: str, errors: list[str], label: str) -> None:
    seen: set[str] = set()
    for i, row in enumerate(rows, start=2):
        value = (row.get(field) or "").strip()
        if not value:
            errors.append(f"{label}:{i} empty {field}")
            continue
        if value in seen:
            errors.append(f"{label}:{i} duplicate {field}={value}")
        seen.add(value)


def check_identifier(row: dict[str, str], line: int, label: str, errors: list[str]) -> None:
    doi = (row.get("doi") or "").strip()
    pmid = (row.get("pmid") or "").strip()
    if doi and not DOI_RE.match(doi):
        errors.append(f"{label}:{line} invalid DOI {doi!r}")
    if pmid and not PMID_RE.match(pmid):
        errors.append(f"{label}:{line} invalid PMID {pmid!r}")


def looks_like_guess(value: str) -> bool:
    text = value.strip()
    if not text:
        return False
    return any(token.lower() in text.lower() for token in GUESS_TOKENS)


def main() -> int:
    errors: list[str] = []

    lock_path = ROOT / "state/LOCKED_FILES.sha256"
    if not lock_path.is_file():
        errors.append("missing state/LOCKED_FILES.sha256")
    else:
        expected = {}
        for line in lock_path.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            digest, rel = line.split(None, 1)
            expected[rel.strip()] = digest.strip()
        for rel in LOCKED:
            path = ROOT / rel
            digest = sha256_file(path)
            if expected.get(rel) != digest:
                errors.append(f"hash mismatch for {rel}")
        if set(expected) != set(LOCKED):
            errors.append("LOCKED_FILES.sha256 path set does not match constitution files")

    sources_path = ROOT / "state/sources.csv"
    header, sources = read_csv(sources_path)
    if header != SOURCES_FIELDS:
        errors.append(f"sources.csv unexpected header: {header}")
    check_ids(sources, "source_id", errors, "sources.csv")
    for i, row in enumerate(sources, start=2):
        check_identifier(row, i, "sources.csv", errors)
        if (row.get("source_type") or "") not in SOURCE_TYPES:
            errors.append(f"sources.csv:{i} bad source_type")
        if (row.get("full_text_inspected") or "") not in INSPECTED:
            errors.append(f"sources.csv:{i} bad full_text_inspected")
        if (row.get("status") or "") not in SOURCE_STATUS:
            errors.append(f"sources.csv:{i} bad status")
        if (row.get("status") or "") == "core":
            # Allowed later; Round 0 check_structure forbids rows entirely.
            pass

    claims_path = ROOT / "state/claims.csv"
    header, claims = read_csv(claims_path)
    if header != CLAIMS_FIELDS:
        errors.append(f"claims.csv unexpected header: {header}")
    check_ids(claims, "claim_id", errors, "claims.csv")
    for i, row in enumerate(claims, start=2):
        tag = (row.get("evidential_status") or "").strip()
        if tag not in CLAIM_TAGS:
            errors.append(f"claims.csv:{i} bad evidential_status {tag!r}")
        q = (row.get("quantity_type") or "").strip()
        if q not in QUANTITY_TYPES:
            errors.append(f"claims.csv:{i} bad quantity_type {q!r}")
        if (row.get("transferable") or "") not in TRANSFERABLE:
            errors.append(f"claims.csv:{i} bad transferable")
        if looks_like_guess(row.get("value") or ""):
            errors.append(f"claims.csv:{i} guessed value {row.get('value')!r}")
        if (row.get("value") or "").strip() and not (row.get("units") or "").strip():
            errors.append(f"claims.csv:{i} value without units")

    evidence_path = ROOT / "research/evidence/core_evidence.csv"
    header, evidence = read_csv(evidence_path)
    if header != EVIDENCE_FIELDS:
        errors.append(f"core_evidence.csv unexpected header: {header}")
    check_ids(evidence, "evidence_id", errors, "core_evidence.csv")
    for i, row in enumerate(evidence, start=2):
        q = (row.get("quantity_type") or "").strip()
        if q not in QUANTITY_TYPES:
            errors.append(f"core_evidence.csv:{i} bad quantity_type {q!r}")
        if (row.get("full_text_inspected") or "") not in INSPECTED:
            errors.append(f"core_evidence.csv:{i} bad full_text_inspected")
        if looks_like_guess(row.get("numerical_result") or ""):
            errors.append(f"core_evidence.csv:{i} guessed numerical_result")
        if (row.get("numerical_result") or "").strip() and not (row.get("units") or "").strip():
            errors.append(f"core_evidence.csv:{i} numerical_result without units")

    scoreboard = json.loads((ROOT / "state/scoreboard.json").read_text(encoding="utf-8"))
    if "theses" not in scoreboard or "analyses" not in scoreboard:
        errors.append("scoreboard.json missing theses or analyses")

    model = json.loads((ROOT / "state/model_config.json").read_text(encoding="utf-8"))
    if model.get("parent_model") != "cursor-grok-4.6-xhigh":
        errors.append("model_config parent_model must be cursor-grok-4.6-xhigh")
    if "4.7" in json.dumps(model.get("available_grok_ids")):
        errors.append("model_config must not list grok-4.7 as available")

    if errors:
        print("validate_ledgers: FAIL")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("validate_ledgers: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
