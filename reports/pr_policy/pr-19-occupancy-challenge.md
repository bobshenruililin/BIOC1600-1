# PR policy: occupancy-challenge (#19)

Not a merge. Not a gate change. Not group-final. Coordinator notes only.

**PR:** https://github.com/bobshenruililin/BIOC1600-1/pull/19  
**File added:** `rounds/goal-wave-a/occupancy-challenge.md`  
**Canonical files edited by this PR:** none (`state/gates/`, `poster/theses.md`, `reports/nightly_summary.md`, `analysis/accepted/` untouched).

## 1. What inference changes if this PR is accepted?

If accepted **as a review parked under `rounds/`:** the swarm records an adversarial argument that the occupancy/kinetics *package* should not be the flagship, while Mission 1 revised D can remain the REVISE *title* recommendation. That is a documentation change, not a gate change.

If treated as a **canonical flagship swap:** `reports/nightly_summary.md` §6 and `analysis/accepted/README.md` would become stale. This PR does not perform that swap. Do not infer it from merge of a `rounds/` file.

## 2. Which claims are new?

Review claims only (not promoted to `state/claims.csv` by this PR):

- Occupancy/kinetics should be **replaced** as flagship; atlas is the interim implemented flagship until a working-range-vs-poles panel exists.
- Hu OA text does not report Langmuir–Freundlich *n* next to the 1.8 nM Glu fit.
- Ricci 2016 is the 1:1 / 81-fold Account and does not license the LF overlay (`supports_claim=no` for “Ricci = LF”).
- `sensitivity.svg` uses non-glutamate C008/C010 `kon` with glutamate Kd (already listed under `do_not_promote` in `state/gates/science_story.json`).

## 3. Which claims are weakened?

- Overnight use of occupancy-at-basal θ≈0.93 as if it were a tissue finding on the PaC probe.
- Treating `sensitivity.svg` as a tested contradiction of T5 rather than a labeled chimeric-rate illustration.
- Unrevised D (occupancy-saturation-as-measured). The report says this does **not** fatally undermine **revised** D as a REVISE title.

## 4. Are all new numerical claims source-traceable?

The report recomputes the existing 12-row occupancy table (match) and quotes Hu OA / ledger C005, C011, C012, C008, C010, C027. It does not enter new glutamate `kon`/`koff`. Chimeric rates are labeled `computational illustration`. Ding VoR remains closed (`partial`).

## 5. Does the PR conflate constructs, quantities, matrices, or clocks?

No. The review’s load is that the **accepted figures** conflate LF EC50 with 1:1 Kd, AuED-MEA with PaC probe, and foreign `kon` with glutamate `koff`. The PR itself is a critique file.

## 6. Does it alter a science gate?

**No.** `state/gates/science_story.json` is not in the diff. Status remains **REVISE**. The PR body says occupancy withdrawal is not enough for PASS.

## 7. Does it make any canonical file stale?

Not unless a human later adopts “replace occupancy” into nightly §6 / accepted-analysis README. Today those files still name occupancy/kinetics as flagship. That split should stay visible until a human decision in `state/decisions.md`.

## 8. What should remain explicitly unresolved?

- Langmuir–Freundlich *n* on the Glu channel and on the PaC probe
- PaC-probe apparent Kd in Ames/tissue
- Glutamate aptamer `kon`/`koff`
- Overnight T1 vs Mission 1 revised D as the poster-facing sentence
- Whether working-range-vs-poles (A3) exists as an implemented figure (separate Mission 2 drafts; not this PR)

## Coordinator recommendation

**Hold. Do not merge automatically.** Safe later merge of the `rounds/` review is a documentation decision, not a science-story PASS.
