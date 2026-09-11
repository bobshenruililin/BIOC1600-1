# Mission 1 close status (for human review)

Not a finished poster. Not group-final. Coordinator snapshot. Does not change the gate.

**Gate:** `science_story` = **REVISE** (`state/gates/science_story.json`, 2026-09-11). `group_final` = false.

**This file cannot convert REVISE into PASS.** A human must record the close choice in `state/decisions.md`.

## What the repo already recommends (Mission 1)

Canonical tournament: `reports/mission1_story_tournament.md`.  
Premium review (verbatim, do not rewrite): `research/reviews/premium/opus_story_gate.md`.  
Human log: `state/decisions.md` (2026-09-11 row).

Mission 1 recommended title: **revised D** (two biological regimes; occupancy-at-basal withdrawn as a finding; S066 clocks remain primary). Runner-up: **C** as a panel. Overnight T1 is listed under `do_not_promote` as this mission’s result.

Adversarial Grok note already in the tournament: D *as submitted* was not treated as materially stronger than C; *after named revisions* D is the title; still REVISE.

## What is still poster-facing overnight T1

These files still present T1 as current best / §1 thesis:

- `poster/theses.md`
- `state/scoreboard.json` (`current_best_thesis`: T1)
- `reports/nightly_summary.md` §1 (after a header that says Mission 1 recommended revised D)

That split is **unresolved**. Updating those files is a science-facing change. Do not auto-merge it. Do not treat coordinator preference as a vote.

## Human decisions required

1. Which sentence is poster-facing: overnight T1, or Mission 1 revised D?
2. May `state/scoreboard.json` name `D_revised` without implying PASS?
3. Keep all open research PRs on **hold** until (1) is recorded?

## Load-bearing vs withdrawn (existing tags only)

Already recorded; not re-derived here:

- S066 clocks are measured protocol/sampling times on the retina probe (`measurement_time`), authors refuse synaptic transients.
- Occupancy at basal on the PaC probe in Ames/tissue is **unmeasured**. 1:1 θ from Hu 1.8 nM LF EC50 on AuED-MEA is `computational illustration` and a device hop.
- 81-fold 10–90% is a 1:1 identity (C027). Hu fitted Langmuir–Freundlich; *n* is not a ledger number.
- No glutamate aptamer `kon`/`koff` in the inspected set.

## Open PRs relevant to close (hold; not merged)

| PR | Role | Gate? |
| --- | --- | --- |
| [#19](https://github.com/bobshenruililin/BIOC1600-1/pull/19) | Occupancy-challenge review | No. Body: withdrawal keeps revised D as REVISE; not PASS. |
| [#20](https://github.com/bobshenruililin/BIOC1600-1/pull/20) | Coordinator hold rationale for #19 | No. Documentation. |
| [#21](https://github.com/bobshenruililin/BIOC1600-1/pull/21) | 39-mer genealogy; paired isotherm still the recorded next experiment | No. Not a ledger promotion. Hold note: `reports/pr_policy/pr-21-construct-genealogy.md`. |

Wave A / analysis-implementation PRs (#6–#18 and later A3/A4 drafts) are **Mission 2 exploration**. They are not Mission 1 close. Default: hold.

A fuller PR-policy table for #6–#21 is assigned to a separate close-package worker (`reports/mission1_close_for_human.md` when that PR opens). This snapshot is the status you can review now.

## What must remain unresolved until you decide

- T1 vs revised D as the poster sentence
- Whether occupancy/kinetics remains the implemented flagship (nightly §6 vs #19)
- Glutamate `kon`/`koff`, PaC-probe apparent Kd, LF *n*
- Science-story PASS

## Recommended next experiment (already in the gate JSON)

Paired solution and surface isotherm of Hu Fc-thiol 39-mer in one buffer; report Langmuir–Freundlich *n*. `#21` argues this remains the highest-information Mission 1 follow-up. Treat that as a parked review, not as an auto-update of `state/gates/science_story.json`.
