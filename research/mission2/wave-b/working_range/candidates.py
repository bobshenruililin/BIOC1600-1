#!/usr/bin/env python3
"""Candidate basal poles. Not claims.csv. Not a universal device spec.

OA rechecked this Mission 2 Wave B session (2026-09-12). Tagged candidate.
Do not average with C012. Do not splice into Clements as one span.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CandidatePole:
    pole_id: str
    status: str
    stamp: str
    quantity_type: str
    value_M: float
    display: str
    label: str
    method_class: str
    locator: str
    identifiers: str
    n: str
    transferable: str
    notes: str


# Values copied from OA HTML inspected this session. Not ledger rows.
CANDIDATE_POLES: tuple[CandidatePole, ...] = (
    CandidatePole(
        pole_id="hershey_capp_9p4uM",
        status="candidate",
        stamp="INFERRED",
        quantity_type="biological_concentration_range",
        value_M=9.4e-6,
        display="9.4 µM",
        label="Hershey Capp 9.4 µM (Ed-corrected total Glu)",
        method_class="C. microdialysis Ed-corrected Capp",
        locator="§3.1 body; PMC12418293 HTML; no figure/table for 9.4",
        identifiers="PMID 40838767; PMC12418293; DOI 10.1021/acschemneuro.5c00518",
        n="11",
        transferable="no",
        notes="Capp = Cout_endogenous/Ed. SD rat cortex. Not Herman 25 nM. Not retina.",
    ),
    CandidatePole(
        pole_id="hershey_dialysate_144nM",
        status="candidate",
        stamp="MEASURED",
        quantity_type="biological_concentration_range",
        value_M=144e-9,
        display="144 nM",
        label="Hershey uncorrected dialysate 13C5-Glu 144 nM",
        method_class="C. microdialysis dialysate (not Capp)",
        locator="Abstract; Fig. 1B; PMC12418293 HTML",
        identifiers="PMID 40838767; PMC12418293",
        n="11",
        transferable="no",
        notes="Uncorrected dialysate during 2.5 µM 13C5-Gln. Do not type as Capp.",
    ),
    CandidatePole(
        pole_id="hascup2010_pfc_34p7uM",
        status="candidate",
        stamp="MEASURED",
        quantity_type="biological_concentration_range",
        value_M=34.7e-6,
        display="34.7 µM",
        label="Hascup 2010 PFC resting 34.7 µM (GluOx MEA)",
        method_class="B. enzyme GluOx ceramic MEA",
        locator="§3.1 parenthetical; PMC2996468 HTML; not Table I",
        identifiers="PMID 20969570; PMC2996468; DOI 10.1111/j.1471-4159.2010.07066.x",
        n="41",
        transferable="no",
        notes="Long Evans rat PFC. Error SEM vs SD UNKNOWN. TTX % is a different n=7 experiment.",
    ),
    CandidatePole(
        pole_id="hascup2008_pfc_3p3uM",
        status="candidate",
        stamp="MEASURED",
        quantity_type="biological_concentration_range",
        value_M=3.3e-6,
        display="3.3 µM",
        label="Hascup 2008 mouse PFC resting 3.3 µM",
        method_class="B. enzyme GluOx ceramic MEA",
        locator="Abstract; Table 1 average; PMC3404456 HTML",
        identifiers="PMID 18024788; PMC3404456; DOI 10.1124/jpet.107.131698",
        n="",
        transferable="no",
        notes="C57BL/6 mouse PFC. Abstract this session: 3.3 µM. Table 1 n/SEM not re-opened (timeout). Do not average with 34.7 µM.",
    ),
    CandidatePole(
        pole_id="hascup2008_str_5p0uM",
        status="candidate",
        stamp="MEASURED",
        quantity_type="biological_concentration_range",
        value_M=5.0e-6,
        display="5.0 µM",
        label="Hascup 2008 mouse Str resting 5.0 µM",
        method_class="B. enzyme GluOx ceramic MEA",
        locator="Abstract; Table 1 average; PMC3404456 HTML",
        identifiers="PMID 18024788; PMC3404456",
        n="",
        transferable="no",
        notes="C57BL/6 mouse striatum. Abstract this session: 5.0 µM. Table 1 n/SEM not re-opened (timeout).",
    ),
)
