# Mission 3 entry

Not a finished poster. Not group-final. Do not start Mission 3 proper from chat history — start from this file.

**Branch:** `cursor/m2-int-honesty-245a` ([PR 32](https://github.com/bobshenruililin/BIOC1600-1/pull/32)). Canonical `main` is the PR 28 merge.

**Thesis:** `state/current_thesis.md` (one sentence). Gate **REVISE**. QUANTITATIVE FLAGSHIP **NONE**. READY FOR MISSION 3: **NO** until independent readiness judgments and a human row in `state/decisions.md`.

**Locked question:** What does Hu’s retinal ACV result establish, and what does it not? Storyboard: `poster/storyboards/mission3.md`. Mission-2 test-locked storyboard (keep for CI): `poster/storyboards/revised_D.md`.

## Paths

- Unknowns: `state/high_value_unknowns.md` — U2 (tissue identity) is not a substitute for U1 (paired 39-mer isotherm).
- Claims / evidence: `state/claims.csv`, `research/evidence/core_evidence.csv`, `research/evidence/poster_numbers.md`
- Nightly (PI; score-heavy): `reports/nightly_summary.md`
- Historical T1: `poster/storyboards/winner.md`
- PR provenance: `state/pr_disposition_register.md`

## Analyses

Accepted supporting (rebuild with `sh analysis/accepted/rebuild.sh`): `span_identity.svg`, `two_regime_clocks.svg`, `atlas.svg`. Demoted: `occupancy.svg`.

Rejected as flagship (isolated branches, not merged): sampling-clock `cursor/analysis-m2-sampling-634f` @ `5543ce7c6bc3c0b100e16f4ebeba85ddce218052`; LF-*n* `cursor/analysis-m2-lfn-634f` @ `93ddf2300edbaa7386c8baaadf4837592b7e7e27`; working-range `cursor/analysis-m2-working-range-634f` @ `449ea4fd3aaa5916ae73f2fcdc0b44937f3b7e52`.

## Highest-information experiment

If the claim is retinal identity: pharmacology plus scrambled/binding-null on **both** ACV legs, same shank and room-light protocol (U2), including Leg A’s post-insertion baseline. Do not substitute rates or U1.

## Validators

```bash
python3 scripts/check_structure.py
python3 scripts/validate_ledgers.py
python3 scripts/forbid_pdfs.py
python3 -m unittest discover -s tests -v
```

## Must not

Invert tissue ACV from printed `%gain`. Fill C007 from other ligands. Call either tissue leg MEASURED glutamate. Restore closed titles. Polish a final poster. Merge without a human decision.
