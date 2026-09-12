# Codex handoff: BIOC1600 PR portfolio reset

## Verified local state

- Final verified commit: `48f817e3a947087e09e33add6be76c830f529ae3`
- Short SHA: `48f817e`
- Local branch: `pr-28`
- Comparison base: `origin/main` at `9819f0a77d85665915e01069e667ce89e6b38576`
- Working tree was clean before these two handoff artifacts were created.

## Concise change summary

The patch repairs PR #28 into the sole Mission-1 integration vehicle while keeping the science-story gate at `REVISE` and `group_final=false`.

- Records Mission 1 as complete, revised D as the canonical working thesis, and Mission 2 as ready to begin.
- Keeps occupancy-at-basal withdrawn and treats Hu's retinal result as positive evidence only for its demonstrated basal/slow regime.
- Retains the 81-fold 1:1 Langmuir identity as supporting biochemistry, but withdraws the Herman-to-Clements comparison as the accepted flagship.
- Records flagship selection as unresolved Mission-2 work. PR #24 is only an analysis candidate; its interrogation/sampling-timescale framing is not accepted canonically and canonical text does not use “Nyquist.”
- Preserves PR #31's basal-pole and Langmuir–Freundlich objections as the reason the original flagship was replaced, without promoting the challenger report as accepted evidence.
- Keeps the paired solution/surface 39-mer experiment as the highest-information construct experiment, including a binding-null control and biologically meaningful glutamine/aspartate interferent controls.
- Adds `state/pr_disposition_register.md`, covering every open PR #6–#31 with contribution, evidential status, absorption target, branch, and exact head SHA.
- Adds `state/mission2_input_queue.md`, separating accepted facts, audited candidate evidence, analysis candidates, unresolved hypotheses, and the proposed experiment.
- Aligns the canonical thesis, gate, scoreboard, nightly summary, closure report, storyboard, claims, analyses, captions, and tests with the same state.
- Corrects stale “Probe 3 saturation” wording: the early plateau is confounded by gold-nanostructure detachment, and PaC-probe occupancy remains unmeasured.
- Corrects the two-regime figure so PBS-like probe calibration, Ames calibration, and retinal recording are explicitly distinct contexts.

## Validation results

Validation was run from a clean detached worktree at `48f817e3a947087e09e33add6be76c830f529ae3`.

- Accepted-analysis rebuild: PASS. `sh analysis/accepted/rebuild.sh` completed and left the checkout clean, confirming generated figures match tracked versions byte-for-byte.
- Locked-file hashes: PASS. All 3 entries in `state/LOCKED_FILES.sha256` verified `OK`.
- Structure check: PASS — 33 files, 9 directories, 9 agents.
- Ledger validation: PASS.
- PDF policy check: PASS.
- Repository tests: PASS — 18/18.
- Atlas tests: PASS — 4/4.
- Occupancy/kinetics tests: PASS — 14/14.
- Patch whitespace check: PASS (`git diff --check`).

No GitHub Actions result is claimed. The repaired commit still needs an actual `validate` check on GitHub before merge.

## Independent Astra review

An independent GPT-6 Astra evidence-representation review initially returned `REVISE` with three findings:

1. Stale saturation language remained in the nightly summary and claims.
2. The two-regime clocks figure transferred calibration timing into the retinal-recording context too loosely.
3. Raw scout material was classified too strongly in the handoff queue.

The final commit resolves all three:

- Replaced saturation language with the measured early plateau plus the gold-detachment confound; occupancy is explicitly unmeasured.
- Split and labeled PBS-like probe calibration, Ames calibration, and retina recording, including the 41.6% Ames blank-noise limitation and the 14-second scan/about-one-minute recording cadence.
- Classified raw scouts as source-candidate/scout provenance rather than audited canonical evidence.

The same reviewer then returned:

> PASS — evidence-representation fidelity. All prior P1/P2/P3 findings are resolved. Remaining merge-blocking defects: none.

This was a representation-fidelity review, not a request to award the science-story gate `PASS`; the canonical gate intentionally remains `REVISE`.

## Remaining caveats for Cursor

- Do not merge the current remote PR #28 unchanged. Apply `codex-reset.patch` to the PR #28 branch, confirm the resulting tree corresponds to local commit `48f817e`, and retitle the PR to: `Canonicalize revised D and hand the unresolved flagship to Mission 2`.
- Last confirmed remote PR #28 head was `1eeffb406508f17f0668b372c1c685deabff39f1`; no branch ref was moved, no commit was pushed, and no PR was merged or closed by Codex.
- Two interrupted GitHub-integration attempts may have created unreachable blob/tree objects through the GitHub API. They did not include a successful ref update and have no effect on repository history or PR content.
- Run and require the repository's actual GitHub Actions `validate` check on the applied commit. Do not rely on this handoff or PR-body statements as a substitute.
- Merge #28 only if the remote diff, canonical state, and CI match this verified local state. Keep `science_story=REVISE`, `group_final=false`, and the flagship unresolved.
- Only after #28 merges should Cursor post provenance-preserving comments and close the absorbed PRs. Keep their source branches until Mission 2 reproduces or explicitly rejects the relevant artifacts.
- Do not promote persuasive challenger claims merely because they appear in the disposition register or Mission-2 queue; preserve their accepted/candidate/unresolved boundaries.
- The six-panel storyboard remains provisional until Mission 3.

## Patch contents

`codex-reset.patch` is a five-commit mail-format patch series from `origin/main` through `48f817e`:

1. `4d74b81` — Canonicalize revised D and demote the 1.8 nM occupancy overlay.
2. `c87ebe4` — Pass the science-story gate on existing criteria after Opus closure review.
3. `1eeffb4` — Stamp Mission 1.5 canonical science SHA.
4. `95e4bd0` — Reset Mission 1 gate and consolidate PR handoff.
5. `48f817e` — Resolve independent evidence-representation review.

The later two commits deliberately reverse the earlier `PASS` state while preserving useful canonicalization work from the first three.
