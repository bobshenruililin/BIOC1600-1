# Mission 1 closure — revised D canonical, flagship handed to Mission 2

Not a finished poster. Not group-final. Acceptance criteria were not weakened.

Date: 2026-09-11. Integration branch: `cursor/story-gate-closure-634f`.

Prior tournament: `reports/mission1_story_tournament.md`.

Earlier blind closure review: `research/reviews/premium/opus_story_closure.md`.
Post-closure challenge: PR #31, preserved in `state/pr_disposition_register.md` and `state/mission2_input_queue.md`.

## Verdict

Mission 1 is **complete**, but the science-story gate remains **REVISE** and `group_final` remains false.

Revised D is the canonical working thesis. Occupancy-at-basal remains withdrawn. Hu’s retinal result remains positive evidence within the slow/basal regime it actually demonstrated. Missing glutamate `koff` remains an empty cell, not proof that the aptamer is slow.

The former flagship — the 81-fold 1:1 Langmuir identity set against a roughly 44,000-fold Herman-to-Clements endpoint span — is withdrawn as the accepted flagship. The 81-fold identity remains valid supporting biochemistry. PR #31 argues that the biological endpoint depends on method and compartment and that Hu’s unreported Langmuir–Freundlich exponent can change the working-range conclusion. Those objections are preserved as the reason for withdrawal, while their source rows remain candidate evidence until Mission 2 runs the normal audit pipeline.

The replacement flagship is **unresolved** and is explicitly handed to Mission 2.

## Canonical state

The following files must agree:

- `state/current_thesis.md`: revised D, working thesis, not group-final.
- `state/gates/science_story.json`: `REVISE`, Mission 1 complete, ready for Mission 2.
- `state/scoreboard.json`: revised D current; no accepted flagship.
- `poster/theses.md`: revised D current; overnight T1/T5 historical.
- `poster/storyboards/revised_D.md`: provisional six-panel storyboard with a Mission-2 flagship placeholder.
- `reports/nightly_summary.md`: current handoff, not the earlier PASS state.
- `state/model_disagreements.md`: PR #31 and PR #24 objections visible.
- `state/pr_disposition_register.md`: exact contribution, evidential status, absorption target, branch, and head SHA for every PR #6–#31.
- `state/mission2_input_queue.md`: accepted facts separated from audited candidate evidence, analysis candidates, and unresolved hypotheses.

Historical reports and reviews are retained as provenance. Their PASS language records what that reviewer concluded at that point; it is not the current gate decision.

## Canonical revised-D boundary

Current one-sentence thesis:

> There is no generic glutamate-aptamer sensor: Hu’s retinal platform provides positive evidence within a slow/basal measurement regime, while readiness for rapid transients remains unmeasured because construct-specific solution-to-surface transfer, binding kinetics, and interrogation cadence have not been resolved together.

What remains accepted:

- Herman’s baseline-plus-superimposed-transients framing (C012).
- Clements’ 1.1 mM / 1.2 ms inference in its named cultured-hippocampal preparation (C011).
- Hu S066’s in-vitro retinal light-on/off ACV result and basal/slow protocol clocks (C031, C033, C034, C028, C030).
- PaC-probe occupancy in Ames/tissue is unmeasured; Hu 1.8 nM is a different-device Langmuir–Freundlich apparent fit (C005, C021, C026).
- The 1:1 10–90% identity is exactly 81-fold (C027/C013), as supporting biochemistry only.
- No glutamate-aptamer `kon`/`koff` is in the inspected canonical set (C007).

What is not accepted:

- Herman 25 nM and Clements 1.1 mM as a representative retinal or surface-electrode concentration range.
- The 81-fold-versus-44,000-fold comparison as the flagship.
- Hu 1.8 nM as a 1:1 molecular Kd or PaC tissue occupancy parameter.
- PR #31’s candidate basal rows merely because its review is persuasive.
- PR #24’s generated analysis merely because its clock ratios are striking.
- “Nyquist” as canonical terminology without a defended signal model, bandwidth, sampling operator, and reconstruction claim.

## Mission-2 analysis handoff

PR #24 is preserved as a candidate **interrogation/sampling-timescale mismatch** analysis. Its coarse observation compares Hu’s 14 s interrogation and roughly 60 s sampling cadence with a 1.2 ms literature waveform. It does not measure `koff`, does not establish spatial exposure at the GCL electrode, and is not accepted in this closure.

PR #23’s working-range bars are also a candidate. Mission 2 must test any selected analysis against basal-pole choice, quantity type, compartment, and Langmuir–Freundlich *n*. Proposal scores from PR #11 are provenance, not acceptance.

The complete queue is `state/mission2_input_queue.md`.

## Highest-information construct experiment

The paired solution/surface experiment from PR #21 remains the highest-information construct experiment:

1. Use the exact Hu Fc-thiol 39-mer, with unlabeled and labeled solution forms where feasible.
2. Use one justified buffer across the paired arms.
3. Include a binding-null point mutant in both arms.
4. Include L-glutamine and L-aspartate at concentrations justified for the intended biological medium.
5. Fit Langmuir and Langmuir–Freundlich models; report *n* with uncertainty.
6. Report achieved coverage and complete interface chemistry.
7. Treat PaC/Ames as a later, separately identified transfer.

If the locked question changes from sensor fitness to retinal chemical identity, substitute pharmacology plus a scrambled/binding-null probe. Do not combine both questions into an underpowered experiment.

## PR portfolio consolidation

PR #28 is the sole integration vehicle. After it merges, every other open Mission-1 PR is closed unmerged with a comment pointing to `state/pr_disposition_register.md` and the exact retained source head. Closing records consolidation, not scientific rejection. Source branches are kept until Mission 2 reproduces or explicitly rejects their relevant artifacts.

No candidate report is merged wholesale into the canonical ledger.

## Merge verification

Before merge, this branch must pass:

- locked-file hash verification;
- repository structure, ledger, PDF, and unit-test checks;
- clean rebuild of every accepted analysis;
- generated-versus-tracked figure comparison;
- canonical-state consistency checks;
- review of every newly mentioned claim for a ledger ID or explicit candidate/unresolved tag;
- independent evidence-representation review;
- an actual GitHub Actions `validate` check on the final head.

Local and independent-review results are recorded in the PR conversation. The PR must not merge if the final GitHub Actions check is absent or failing.

---

MISSION 1 STATUS: COMPLETE
SCIENCE STORY GATE: REVISE
CURRENT WORKING THESIS: REVISED D
FLAGSHIP ANALYSIS: UNRESOLVED — MISSION 2 INPUT
GROUP FINAL: NO
READY FOR MISSION 2: YES
