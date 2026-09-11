# PR policy: science-story PASS (#28)

Not a merge. Not group-final. Coordinator notes only. This file cannot convert REVISE into PASS.

**PR:** https://github.com/bobshenruililin/BIOC1600-1/pull/28  
**Branch:** `cursor/story-gate-closure-634f`  
**Child:** `bc-fd77051a-d8aa-4370-b133-8ad0103b634f`  
**Draft, OPEN, CI ledgers SUCCESS.** Not merged.

This is an independent eight-question review of the files on that branch. It is not a rewrite of the child’s closure report or of the Opus review.

Canonical tree on `main` still has `state/gates/science_story.json` = **REVISE**.

## 1. What inference changes if this PR is accepted?

If merged, the working tree would assert:

- Science-story gate **REVISE → PASS** (`state/gates/science_story.json`). All five `pass_criteria` flip from the Mission 1 mix (`false` / `"partial"` / `"qualified"`) to `true`.
- Overnight T1 is no longer poster-facing. Revised D becomes `state/current_thesis.md`, `poster/theses.md` §current, `reports/nightly_summary.md` §1, and `state/scoreboard.json` `current_best_thesis`.
- Flagship glyph is `span_identity.svg` (81-fold identity vs ~44,000-fold Herman-to-Clements span). `occupancy.svg` is demoted as overlay simulation. PaC occupancy stamped UNKNOWN.
- Hu retina is scored as **positive** neural-tissue evidence in a basal/slow clock (C033), not as a failed synaptic sensor.
- An orchestrator row is appended to `state/decisions.md` recording Mission 1.5 PASS. `group_final` stays false.
- Closure report footer: **READY FOR MISSION 2: YES**.

That is a gate change and a poster-sentence change. It is not a documentation-only tidy.

It would also disagree with [PR #27](https://github.com/bobshenruililin/BIOC1600-1/pull/27), which keeps the gate **REVISE** and asks a human to choose T1 vs revised D before rewriting canonical files.

## 2. Which claims are new?

Ledger promotions on the PR branch (not on `main`):

- **C033** — light-on/off glutamate ACV in vitro retina; authors: basal, not synaptic transients. Tag `primary-source-supported`, locator S066 §6.3 / Fig. 6.13. Notes: not a pharmacological identification. Quantity type stored as `signal_gain` with empty value.
- **C034** — glutamate ACV on the large bottom electrode at the GCL. Tag `primary-source-supported`, locator S066 §6.3. Value 14 s stored as `measurement_time` on a placement sentence.

New canonical artifacts: `state/current_thesis.md`, `poster/storyboards/revised_D.md`, `state/high_value_unknowns.md`, `state/model_disagreements.md`, `reports/mission1_closure.md`, `research/reviews/premium/opus_story_closure.md`, `span_identity.svg`, `two_regime_clocks.svg`.

The PASS status itself is a new project inference, not a new wet-lab result.

## 3. Which claims are weakened?

- Occupancy-at-basal as a **finding** (already withdrawn in Mission 1’s recommended revised D; this PR withdraws it in canonical poster files, not only in the tournament report).
- Overnight T1 / T5 as current consensus.
- `occupancy.svg` as flagship; 1.8 nM 1:1 overlay as tissue occupancy.
- Unrevised Candidate D’s “fail the slow problem on occupancy.”

Residual tension: nightly §4 still recites overlay occupancy numbers (12 µM empty at 25 nM; 1.8 nM ~93% occupied) as an “insight,” while §6 demotes that glyph. The overlay math is still tested. The PR renames the test so the name cannot reassert tissue saturation.

## 4. Are all new numerical claims source-traceable?

The load-bearing numbers in the revised-D sentence are already ledgered on `main`: Herman ~25 nM (C012), Clements ~1.1 mM / 1.2 ms (C011, abstract-only), 81-fold (C027), ~44,000-fold as arithmetic on those two, S066 clocks (C028/C031), Hu 1.8 nM as AuED-MEA LF `EC50` (C005). No glutamate `kon`/`koff` is invented (C007 stays empty).

C033/C034 are promotions from already-inspected S066 extract rows (E046/E045), not a new search. C033 does not fill chemical identity. C034 does not fill the photoreceptor-pool question.

Opus 5 (`bc-7da27ff4-88b3-5acc-b4cc-ad86a0beaa66`) independently checked `span_identity.svg` coordinates for 25 nM, 1.1 mM, 81-fold, and absence of a 1.8 nM flagship glyph. That arithmetic check is recorded verbatim. It is not a second extraction of S066.

## 5. Does the PR conflate constructs, quantities, matrices, or clocks?

The canonical thesis text is careful: AuED-MEA 1.8 nM ≠ PaC molecular Kd; Herman slice ≠ Clements culture ≠ retina; 32 pM PBS LOD ≠ 51.5 pM serum LOD ≠ 0.3 pM PaC PBS LOD; interrogation time ≠ `koff`.

Stretch points (not invented numbers, but ontology strain):

- C033 types a light-on/off ACV **experiment** as `signal_gain` with an empty value.
- C034 stores the 14 s scan clock on a **placement** claim.
- The one-sentence thesis says “positive evidence” while C033 notes “Not a pharmacological identification” and `high_value_unknowns.md` still lists chemical identity of the ACV as unknown.

Those are the same tensions Mission 1 already recorded (H2 vs C031; S066 as strongest neural-tissue experiment **and** not a chemical identification). The PR displays them; it does not close them.

## 6. Does it alter a science gate?

**Yes.** `science_story` status becomes **PASS**. `group_final` remains false.

That is the load-bearing reason this PR stays on hold.

Mission 1 already recommended revised D **after** named occupancy withdrawals and still recorded **REVISE** (`reports/mission1_story_tournament.md` §13; `research/reviews/premium/opus_story_gate.md`). Adversarial Grok: D *as submitted* was not materially stronger than C; *after named revisions* D is the title; gate still REVISE.

This PR’s argument is that Mission 1 left those revisions in the tournament report while `poster/theses.md` / scoreboard / nightly §1 still showed T1. Repairing that split is a real stale-file problem. Converting the **gate** from REVISE to PASS is a second, separate act.

The Opus closure packet asked only: *Do the named revisions resolve the reasons this gate previously failed?* That is a repair check. Opus graded all five original bullets PASS and named **no fatal defect**, and also listed residual defects “that must be closed before anything is printed,” with an explicit note that a convention treating any required change as REVISE should keep that list. The child then reports those residuals closed in the same mission (C033/C034 promotion, Ames 41.6% note, overlay test rename, axis label). Opus did not re-review after those edits. Opus was forbidden to read `reports/nightly_summary.md`, `poster/theses.md`, and `state/scoreboard.json` — the files that become student-facing if this merges.

`criteria_not_weakened: true` is a self-assertion in the gate JSON. The five criterion *names* are unchanged. The recorded *grades* are flipped.

CI ledgers SUCCESS is not a science PASS.

[PR #19](https://github.com/bobshenruililin/BIOC1600-1/pull/19) already argued: occupancy withdrawal keeps revised D as **REVISE**, not PASS.

## 7. Does it make any canonical file stale?

If merged:

- `reports/mission1_story_tournament.md` and `research/reviews/premium/opus_story_gate.md` become **prior** (the PR points at them as `prior_report` / `prior_opus_review`). Those files stay historically true as the Mission 1 REVISE record.
- [PR #27](https://github.com/bobshenruililin/BIOC1600-1/pull/27) close package (REVISE; human chooses T1 vs D) would be stale as an operating instruction.
- Open Wave A / A3 / A4 PRs (#6–#26) still assume the pre-#28 split. They stay holds; this PR does not merge them. It evaluated #6 (unpromoted) and #7 (audit checklist) only.
- Tests in `tests/test_canonical_state.py` lock revised D as current and T1 as historical. They do not assert the string `PASS` in the gate JSON, but they do lock the poster-sentence rewrite.

If **not** merged: the T1 vs revised D split on `main` remains. That split was already the Mission 1 close problem. Holding #28 preserves the split rather than silently picking D+PASS.

## 8. What should remain explicitly unresolved?

- Human choice: overnight T1 vs Mission 1 revised D as the poster sentence.
- Human choice: science-story **PASS** vs **REVISE** after the occupancy withdrawal is written into canonical files.
- Group-final (still false on both trees).
- PaC-probe apparent Kd / θ in Ames or tissue.
- Langmuir–Freundlich *n* on the 39-mer.
- Glutamate aptamer `kon`/`koff`.
- Chemical identity of the S066 ACV (pharmacology + scrambled aptamer).
- Whether occupancy/kinetics, 81-fold `span_identity`, A3 working-range, or A4 Nyquist is the flagship analysis.
- READY FOR MISSION 2 (this coordinator does not start full Mission 2 execution as merged work).

Highest-information next experiment on both the Mission 1 gate JSON and this PR’s gate JSON remains: paired solution and surface isotherm of Hu’s Fc-thiol 39-mer in one buffer; report Langmuir–Freundlich *n*. If the question is retinal biology rather than sensor fitness, substitute pharmacological identity. Do not do both and report neither.

## Coordinator recommendation

**Hold. Do not merge. Do not treat CI green or a child PASS as a human close.**

What a human can usefully accept later, without taking PASS:

- Revised D as the *recommended* working sentence (already Mission 1’s recommendation).
- Occupancy-as-finding withdrawn in poster-facing files.
- Flagship 81-fold identity; PaC occupancy UNKNOWN.
- C033/C034 as inspected S066 promotions, still not a pharmacological ID.

What a human must decide explicitly in `state/decisions.md` before this PR can merge:

1. Is the poster sentence overnight T1 or revised D?
2. Does repairing the stale T1 files convert the science-story gate to PASS, or does it stay REVISE until the 39-mer isotherm / pharmacological identity lands?
3. May Mission 2 drafts (A3/A4/wildcard) start as merged work?

Until those rows exist, `main` stays REVISE, #6–#28 stay hold, and premium reviews stay verbatim.
