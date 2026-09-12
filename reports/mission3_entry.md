# Mission 3 entry

Not a finished poster. Not group-final. Do not start Mission 3 proper from chat history — start from this file.

**Branch:** `cursor/m2-int-honesty-245a` ([PR 32](https://github.com/bobshenruililin/BIOC1600-1/pull/32)). Canonical `main` is the PR 28 merge.

**Thesis:** `state/current_thesis.md` (one sentence). Gate **REVISE**. QUANTITATIVE FLAGSHIP **NONE** as occupancy/Kd/LOD/tissue-[Glu] title. Selected picture: `analysis/accepted/figures/protocol_clocks.svg`. Highest-information experiment: **U2**. READY FOR MISSION 3: **YES** after the 2026-09-12 PI decision in `state/decisions.md`. `group_final` false. Do not manufacture PASS. Do not reopen Mission 2.

**Locked question:** What does Hu’s retinal ACV result establish, and what does it not? Storyboard: `poster/storyboards/mission3.md`. Mission-2 test-locked storyboard (keep for CI): `poster/storyboards/revised_D.md`.

## Paths

- Unknowns: `state/high_value_unknowns.md` — **U2 locked** (tissue identity). U1 (paired 39-mer isotherm) is a different question and cannot establish what produced the retinal current.
- Claims / evidence: `state/claims.csv`, `research/evidence/core_evidence.csv`, `research/evidence/poster_numbers.md`
- Nightly (PI; score-heavy): `reports/nightly_summary.md`
- Historical T1: `poster/storyboards/winner.md`
- Central glyph (conceptual, no data pixels): `poster/figures/mission3_boundary_glyph.svg` (+ `.CAPTION.md`)
- Selected clocks picture: `analysis/accepted/figures/protocol_clocks.svg`
- PR provenance: `state/pr_disposition_register.md`

## Analyses

Accepted supporting (rebuild with `sh analysis/accepted/rebuild.sh`): `protocol_clocks.svg` (selected picture), `span_identity.svg`, `two_regime_clocks.svg`, `atlas.svg`. Demoted: `occupancy.svg`.

Rejected as flagship (isolated branches, not merged): sampling-clock `cursor/analysis-m2-sampling-634f` @ `5543ce7c6bc3c0b100e16f4ebeba85ddce218052`; LF-*n* `cursor/analysis-m2-lfn-634f` @ `93ddf2300edbaa7386c8baaadf4837592b7e7e27`; working-range `cursor/analysis-m2-working-range-634f` @ `449ea4fd3aaa5916ae73f2fcdc0b44937f3b7e52`.

## Highest-information experiment

**Locked: U2.** Pharmacology plus scrambled/binding-null on **both** ACV legs, same shank and room-light protocol, including Leg A’s post-insertion baseline. Directly tests the identity inference. U1 cannot establish what produced the retinal current. Do not substitute rates or U1.

## Validators

```bash
python3 scripts/check_structure.py
python3 scripts/validate_ledgers.py
python3 scripts/forbid_pdfs.py
python3 -m unittest discover -s tests -v
```

## Must not

Invert tissue ACV from printed `%gain`. Fill C007 from other ligands. Call either tissue leg MEASURED glutamate. Restore closed titles. Polish a final poster. Merge without a human decision.
