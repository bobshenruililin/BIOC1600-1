# BIOC1600 Mission 3 cold Astra audit

Use this prompt exactly once, after the Mission 3 materialization and release gates pass. Replace the three bracketed fields and attach the indexed images and evidence bundle.

---

Act as the independent scientific-communication and release auditor for this BIOC1600 Mission 3 candidate. Perform one bounded audit of the supplied package.

Do not spawn agents, browse, edit files, run builds, conduct broad research, or restart architecture selection. Cursor/Sol owns implementation and routine validation.

## Audit target

- Candidate commit: `[SHA]`
- Poster render SHA-256: `[HASH]`
- Bundle index: `[PATH]`

Inspect only this identified candidate. If required images are inaccessible, source evidence needed for a central claim is absent, or artifact versions conflict, return `INCOMPLETE` with the exact missing items. Never substitute source-text inspection for visual inspection.

## Read order

First inspect the whole poster and readable crops. Before opening the scientific rationale or reviewer history, record briefly:

- what appears measured;
- what appears concluded about glutamate/analyte identity;
- what experiment appears to come next.

Then read the frozen science, original evidence excerpts, U2 specification, talks, provenance, and release evidence. Open previous reviewer verdicts last. Preserve your initial visual interpretation in the report.

## Decision

Decide whether this candidate is scientifically faithful, understandable, and defensible enough to advance to human/PI visual approval.

Frozen state remains `D_revised`; science gate `REVISE`; Mission 2 `FREEZE`; quantitative flagship `NONE`; next experiment `U2`; `group_final=false`. Your audit does not alter these states or authorize merging.

Concentrate on:

1. Whether visual emphasis, arrows, schematics, labels, and speech preserve measured ACV signal-gain versus inferred glutamate and unresolved tissue chemical attribution. Check both unjustified identification and unjustified claims that the signal is not glutamate.
2. Whether “one unnamed analyte” implies unsupported single-species or shared identity across the two legs. Identify the smallest wording or graphic correction if needed.
3. Whether Leg A, Leg B, calibration, construct identity, selectivity, and biological clocks retain their actual experimental scope. Check the consequential 1.8 nM, 12 µM, C028, and C032 qualifications against supplied original evidence.
4. Whether displayed U2 tests the stated uncertainty in both legs, including Leg A. Examine controls, competing explanations, outcome interpretation, and residual ambiguity. Do not imply U2 guarantees definitive chemical identification unless its design supports that claim.
5. Whether flagship `NONE` is communicated as an evidence-bounded result while retaining useful measured quantities and positive experimental findings.
6. Whether poster and talks agree, and whether release claims refer to this render rather than earlier wireframes or inherited review verdicts.

For each consequential finding provide:

- exact panel/phrase and source or claim locator;
- the incorrect inference or release failure it creates;
- the smallest sufficient repair;
- an observable acceptance test Cursor/Sol can execute.

Classify findings as:

- `SCIENCE FATAL`: supplied evidence establishes a central contradiction that cannot be repaired while preserving the freeze. Cite the contradiction and narrowly identify the PI decision required.
- `MUST FIX`: a communication, provenance, experimental-description, or release defect repairable within the freeze.
- `OPTIONAL`: preference without a demonstrated comprehension or fidelity consequence.

Communication severity alone does not justify reopening Mission 2. Missing evidence is an audit limitation, not proof of a scientific contradiction. Previous PASS/HOLD labels are historical evidence, not votes.

## Return

Use at most 900 words, excluding evidence essential to report additional science fatals. Return:

- audited SHA and render hash;
- initial visual interpretation;
- `ADVANCE` / `ADVANCE AFTER SPECIFIED FIXES` / `HOLD—PI SCIENCE DECISION` / `INCOMPLETE`;
- strongest reason;
- all science fatals and up to five prioritized MUST FIX items, grouping related defects;
- U2: coherent as proposed / repair description / concrete fatal, with reason;
- flagship `NONE`: defensible / concrete objection, with reason;
- at most two optional improvements;
- unchecked limitations.

Stop after this report. Do not propose another review round or fill a finding quota. If no consequential defect is demonstrated, say so and advance the candidate to human/PI review.
