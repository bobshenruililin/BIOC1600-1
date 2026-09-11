# PR policy: construct-genealogy (#21)

Not a merge. Not a gate change. Not group-final. Coordinator notes only.

**PR:** https://github.com/bobshenruililin/BIOC1600-1/pull/21  
**File added:** `rounds/goal-wave-a/construct-genealogy.md`  
**Canonical files edited by this PR:** none.

## 1. What inference changes if this PR is accepted?

If accepted as a `rounds/` review: the swarm records that Hu’s tissue DNA is Wu `glu1` (ESM), that 12 µM attaches to 98-nt `glu1d04`/`1d04` not to the 39-mer, and that the gate’s paired 39-mer isotherm remains the Mission 1 next experiment. Sequence identity is no longer “behind the Wu VoR.”

It does **not** fill `Kd_molecular` of the 39-mer. It does not change `state/gates/science_story.json`.

## 2. Which claims are new?

Review claims only (not ledger promotions in this PR): `glu1` letter-for-letter identity with the Hu 39-mer from OA ESM; truncation architecture (primer + N10 + docking 11-mer); Hu used glu1 only among Wu’s listed truncations.

## 3. Which claims are weakened?

Silent citation of Wu 12 µM onto the Fc-thiol 39-mer as if it were that oligo’s `Kd_molecular`. “Open Wu VoR” as the highest-value next step for **sequence** identity.

## 4. Are all new numerical claims source-traceable?

Packing comparison (~17-fold vs Wu glu1/MCH) is taken from the genealogy report’s reading of Hu Fig. 6.5 vs Wu ESM coverage. Treat as review until extractors promote a tagged row. No glutamate `kon`/`koff` invented. Xiao SI sequence not retrieved.

## 5. Does the PR conflate constructs, quantities, matrices, or clocks?

No. It separates 98-nt parent Kd, 39-mer empty Kd, AuED 1.8 nM LF EC50, and PaC-probe empty apparent Kd. It warns not to pair Wu MCH coverage with Hu’s 1.8 nM.

## 6. Does it alter a science gate?

**No.** Status remains **REVISE**. Next-experiment string in the gate JSON is unchanged; the report argues it is still the right experiment.

## 7. Does it make any canonical file stale?

`reports/mission1_story_tournament.md` / candidate B language that truncation cuts wait on Wu VoR would be stale **if** a human adopts the ESM identity. This PR does not edit those files.

## 8. What should remain explicitly unresolved?

- Solution and surface `Kd_molecular` / LF *n* of the Fc-thiol 39-mer
- Whether glutamate still uses the docking module after dropping N42 (`hypothesis`)
- Xiao SI sequence vs glu1
- Wu VoR fit of 12 µM (still on 1d04 in abstract/ESM as reported here)
- T1 vs revised D as poster sentence

## Coordinator recommendation

**Hold. Do not merge automatically.** Documentation merge of the `rounds/` file is a later human choice, not PASS.
