# Nightly research handoff

Canonical file for PI review. Not a finished poster. Not group-final.

**Current thesis:** revised D — `state/current_thesis.md`. Provisional storyboard: `poster/storyboards/revised_D.md`. Replacement flagship: **UNRESOLVED — MISSION 2 INPUT**.

**Mission 1 (2026-09-11):** science-story gate opened at **REVISE**. Occupancy-at-basal withdrawn as a finding; S066 clocks remain primary. Full record: [`reports/mission1_story_tournament.md`](mission1_story_tournament.md).  
**Mission 1 closure:** completed with gate **REVISE** and `group_final=false`. The earlier blind PASS review remains historical; PR #31 later invalidated the accepted flagship comparison. Closure: [`reports/mission1_closure.md`](mission1_closure.md). Gate JSON: `state/gates/science_story.json`.

Overnight T1/T5 (sections below marked historical) are **not** current consensus and were never group-final.

Generated 2026-09-11. Canonical working branch for this closure: `cursor/story-gate-closure-634f`. Not a finished poster. Not group-final.

## 1. Best current poster thesis

There is no generic glutamate-aptamer sensor: Hu’s retinal platform provides positive evidence within a slow/basal measurement regime, while readiness for rapid transients remains unmeasured because construct-specific solution-to-surface transfer, binding kinetics, and interrogation cadence have not been resolved together.

Status: **canonical working thesis, gate REVISE, not group-final** (`D_revised`). Herman ~25 nM and Clements ~1.1 mM come from **different hippocampal preparations** and are not a retinal range or an accepted representative surface-device span. Hu 1.8 nM is an AuED-MEA Langmuir–Freundlich apparent Kd, not the PaC probe’s molecular Kd.

## 2. Runner-up thesis and why it lost

**Candidate C (Mission 1 runner-up, supporting panel):** ultrasensitive working-range ceilings miss Herman ~25 nM from above (Wu glu1 top 1 nM; Abrantes preprint 10 pM). After C’s strong LOD form is deleted, what remains is occupancy/working-range/clocks — D’s content. Hu 32 pM is a real **PBS** LOD; 51.5 pM is the 50% serum LOD.

**Historical overnight T5** (not current): if advertised occupancy parameters are treated as Kd, the µM SELEX isolate is empty at 25 nM and *could* unbind near 1.2 ms under a diffusion-limited kon **bound**, while Hu’s 1.8 nM apparent Kd is ~93% occupied at 25 nM. That overlay is MODELED, not tissue occupancy, and is demoted.

Isolated Task R2 still liked T5/T4 as overnight finalists. Isolated Task R1 preferred T3. Do not average stacks. Those ranks are historical (`rounds/03/`).

## 3. Top verified primary sources (smallest set)

1. Wu 2022 S001 PMID 34783880 — 1d04 Kd 12 µM vs glu1 LOD 0.0013 pM (abstract only).
2. Hu 2025 journal S002 PMID 40992279 — Glu apparent Kd 1.8 nM (Langmuir–Freundlich); LOD 32 pM / 51.5 pM; 15 min wait; 12 µM is a Wu citation (VoR).
3. Hu 2025 thesis S066 DOI 10.18154/RWTH-2025-07238 — **strongest Glu-apt neural-tissue experiment**: in vitro mouse retina; 10 nM wait-to-plateau 10 min; PBS LOD 0.3 pM; Ames 10 nM–10 µM (poor SNR); ACV 14 s then 1 min sampling; authors: basal Glu, not synaptic transients.
4. Xiao 2025 S021 PMID 40433802 — SPR Kd 293 nM; FET LOD 10 fM in 0.1× PBS; 200 s (PMC).
5. Herman 2007 S050 PMID 17804634 — ambient slice glutamate ~25 nM (PMC).
6. Clements 1992 S049 PMID 1359647 — inferred cleft 1.1 mM, τ 1.2 ms (abstract).
7. Rutherford 2007 S054 — GlutOx 500–800 ms in moving rats (PMC).
8. White 2008 S033 — packing density moves E-AB gain/apparent Kd; cocaine <4 s (PMC; not glutamate).
9. Abeykoon 2025 S004 — tobramycin IPA kon/koff and 2 ms clock (PMC; not glutamate).
10. Ding 2024 S003 — ITC kon 96–2×10^5 M⁻¹ s⁻¹ across small-molecule DNA aptamers (abstract; not glutamate).
11. Xie/Liu 2026 S046 — docking fails theophylline/caffeine selectivity (PMC).
12. InstructNA 2026 S007 — generated protein aptamers; many non-binders (PMC).
13. Armbruster 2020 S062 — iGluSnFR waveforms 10–100× free glutamate (PMC).
14. Park 2023 S023 — “Glutamate FET” row is PfGDH (caution, not a sensor).
15. Xu/Tanner 2026 S006 — tetrahedron interface, N-protein only (PMC).
16. Helassa 2018 S060 — iGluu τ_off ~2 ms (protein benchmark, not aptamer).

Full table: `research/evidence/poster_numbers.md`.

## 4. Five most important scientific insights

1. **Kd ≠ LOD ≠ EC50 ≠ incubation time ≠ biological [Glu].** Wu’s 12 µM and 0.0013 pM are different constructs in one abstract. Hu’s 12 µM is a citation; 1.8 nM is a surface Langmuir–Freundlich apparent Kd; 32 pM is a blank+3SD LOD after 15 min.
2. **No glutamate aptamer kon/koff** in inspected sensor papers. “Too slow” is a gap, not a measured koff. Empirical SM-aptamer kon already in the ledger (C008/C010) is **not** transferable, but as a labeled envelope it kills T5’s 0.8 ms 1d04 claim.
3. **One 1:1 Langmuir site has an 81-fold 10–90% window** (derived, C027). This remains supporting biochemistry, not Hu’s fitted working range and not an accepted representative biological span. PR #31’s basal-pole and LF-*n* objections are candidate Mission-2 inputs.
4. **Occupancy vs clocks remains simulation/bound work.** The advertised-number overlays and assumed-`kon` curves are not PaC tissue occupancy or measured glutamate kinetics. Tighter/lower LOD is not automatically better, and `koff ≈ 1/1.2 ms` is a category error.
5. **The strongest Glu-apt biological experiment already exists and argues against synaptic milliseconds.** Hu thesis retina: light-on/off basal Glu, 1 min ACV, authors refuse synaptic transients. Docking/InstructNA remain hypothesis generation. Ames vs PBS shows buffer composition rewrites the same oligo after selection.

## 5. Three important contradictions / limitations

1. Hu journal 15 min ACV and Hu thesis 10 min / 1 min retina clocks vs Clements 1.2 ms vs missing Glu rates (C006, C028, C031, C011, C007).
2. Park 2023 glutamate FET = malaria GDH, not neurotransmitter glutamate (C019).
3. Wu VoR closed; 1d04/glu1 details beyond the abstract are unverified. Clements is inference. Xiao 10 fM is 0.1× PBS. Thesis Probe 3 saturates at basal Glu; Probe 4 is unstable. Scoring stacks disagree on which thesis to speak.

## 6. Flagship computational analysis — unresolved

No replacement flagship is accepted. Mission 2 must select and reproduce one after sensitivity analysis. PR #24 is a candidate **interrogation/sampling-timescale mismatch** analysis, not an accepted result; avoid “Nyquist” unless its formal signal assumptions are defended. PR #23’s working-range bars are also a candidate.

Supporting: the valid 81-fold identity (`span_identity.svg`), two-regime clocks (`two_regime_clocks.svg`), and evidence atlas (`atlas.svg`). The Herman-to-Clements endpoint comparison is not an accepted representative device span.

**Demoted:** `occupancy.svg` 1:1 overlay of Hu 1.8 nM as if it were tissue occupancy. The overlay math remains tested; it is not a retinal finding. `sensitivity.svg` remains the figure that can contradict T5 inside C008/C010 (NOT glutamate).

Not recommended: docking, InstructNA training, FASTAptamer without a licensed FASTQ.

## 7. Status of implemented analyses and tests

Accepted:

- Atlas tests + `atlas.svg` (now includes Hu retina-probe 10 min / 0.3 pM; glutamate kon/koff cells remain empty)
- Occupancy/kinetics tests (81-fold identity; advertised-number overlay arithmetic; diffusion t_off bounds; empirical-kon 1d04 t_off in seconds; τ_eq(cleft) ≪ t_off) + `occupancy.svg` + `clocks.svg` + `sensitivity.svg`. These are supporting simulations/bounds, not tissue occupancy.

Repo command: `sh analysis/accepted/rebuild.sh` and `python3 -m unittest discover -s tests -v`.

Rejected: docking foil; FASTAptamer toy (does not answer the glutamate question).

Canonical copies: `analysis/accepted/figures/`.

**Supporting figures for the handoff (verified, not an accepted flagship):**

| # | path | why it was kept | labels |
| --- | --- | --- | --- |
| 1 | `analysis/accepted/figures/span_identity.svg` | valid 81-fold identity; endpoint comparison not accepted as representative; PaC occupancy UNKNOWN | MEASURED / MODELED / UNKNOWN / PROPOSED |
| 2 | `analysis/accepted/figures/two_regime_clocks.svg` | S066 basal/slow clocks vs untested transients | MEASURED vs UNKNOWN |
| 3 | `analysis/accepted/figures/atlas.svg` | Only plot that refuses to invent glutamate kon/koff | empty cells are empty; ledger units |

Demoted: `occupancy.svg` (overlay simulation, not tissue occupancy). Supporting: `sensitivity.svg`, `clocks.svg`.

## 8. Six-panel storyboard (text only)

See `poster/storyboards/revised_D.md`. Provisional panels: two regimes; Mission-2 flagship placeholder; Hu retina positive on a basal/slow clock; PaC occupancy UNKNOWN; construct atlas; proposed next measurement.

Historical overnight T1 storyboard: `poster/storyboards/winner.md` (superseded; occupancy inversion demoted).

No polished poster was generated.

## 9. Hardest five assessor questions

From `research/reviews/tanner_objections.md`:

1. Is 15 min (or 10 min, or 1 min) the aptamer’s koff, or when you chose to scan?
2. Why is Hu’s 1.8 nM not “the” Kd — and why is 81-fold illegal on a Freundlich EC50?
3. Show the 81-fold 10–90% identity without a review, then show τ_eq ≠ t_off at 1.1 mM.
4. Why not plot tobramycin IPA 2 ms, or T5’s 0.8 ms bound, as proof aptamers are fast enough?
5. Did Hu’s own retina chapter already do the biological experiment — and what clock did it actually have?

## 10. Swarm/prompt improvements that survived benchmarking

Observed failure: 4/4 isolated thesis writers refined the same frame. Adopted patch in `AGENTS.md`: at least one candidate must challenge the current framing. T5 exists because of that rule.

Second observed failure: orchestrator dual-pass scores ≠ isolated Task red-team scores. **Not patched by averaging.** Recorded both stacks. Constitution, rubric, and safety files were not edited.

## 11. Failures, unresolved uncertainties, blockers

- Glutamate kon/koff unmeasured.
- No in vivo glutamate aptamer sensor (S066 is in vitro retina).
- Wu VoR inaccessible; JSTAGE Ohsawa PDF 500; MacDonald ACS 403 — those numbers were **not** entered.
- Abrantes millimolar ELONA Kd still not entered. Second-extraction attempt this cycle: bioRxiv HTML/JATS HTTP 429; Europe PMC/API abstract has no ELONA Kd. Do not treat API tokens 10.3 / 25.1 (funder IDs) as affinity.
- Scoring-stack inversion is **historical** (`rounds/03/tournament_reconciliation.md`). Not current consensus.
- Analysis implemented on the swarm branch (sequential single writer) so nothing accepted exists only in an unmerged worktree.
- Mission-1 PRs are consolidated in `state/pr_disposition_register.md`. Closing them after PR #28 merges does not reject their science or delete their branches.

## 12. Exact Git commit SHA

Read the final canonical merge SHA from PR #28. The pre-reset science SHA `c87ebe410581744928e0680f9c4c6e2984cb902e` is historical and still contains the superseded PASS/flagship state.

Do **not** use overnight SHA `984af62f25127b43e7d2be248ca1c8123921b8a8` as current science content.

## 13. Exact paths

- Nightly: `reports/nightly_summary.md`
- Current thesis: `state/current_thesis.md`
- High-value unknowns: `state/high_value_unknowns.md`
- Model disagreements: `state/model_disagreements.md`
- Mission 1.5 closure: `reports/mission1_closure.md`
- Evidence table: `research/evidence/core_evidence.csv`
- Poster numbers: `research/evidence/poster_numbers.md`
- Claims: `state/claims.csv`
- Contradictions: `research/reviews/contradictions.md`
- Citation audit: `research/reviews/citation_audit.md`
- Tanner objections: `research/reviews/tanner_objections.md`
- Scoreboard: `state/scoreboard.json`
- Historical scoring reconciliation: `rounds/03/tournament_reconciliation.md`
- Current storyboard: `poster/storyboards/revised_D.md`
- Historical T1 storyboard: `poster/storyboards/winner.md`
- Supporting span identity: `analysis/accepted/figures/span_identity.svg`
- Figure 2 two-regime clocks: `analysis/accepted/figures/two_regime_clocks.svg`
- Figure 3 atlas: `analysis/accepted/figures/atlas.svg`
- Demoted occupancy overlay: `analysis/accepted/figures/occupancy.svg`
- Supporting sensitivity / clocks: `analysis/accepted/figures/sensitivity.svg`, `analysis/accepted/figures/clocks.svg`
- Source code: `analysis/accepted/atlas/atlas.py`, `analysis/accepted/occupancy_kinetics/model.py`, `analysis/accepted/occupancy_kinetics/figures.py`
- Captions: `analysis/accepted/figures/occupancy.CAPTION.md`, `analysis/accepted/figures/atlas.CAPTION.md`
- Table: `analysis/accepted/occupancy_kinetics/tables/occupancy_table.csv`
- Rebuild: `analysis/accepted/rebuild.sh`
- Consolidation log: `rounds/consolidation.md` (historical overnight merge)
- Mission-2 input queue: `state/mission2_input_queue.md`
- PR disposition register: `state/pr_disposition_register.md`

## Decisions for PI review

1. **Do not treat overnight T1 as current.** Canonical thesis is revised D. Scoring-stack inversion is a historical process hole, not a title fight.
2. **Which analysis should Mission 2 reproduce and nominate as flagship?** PR #24’s interrogation/sampling-timescale mismatch and PR #23’s working-range bars are candidates only. The 81-fold identity is supporting.
3. **Proceed with Wu abstract-only** 1d04/glu1 split, or block any 12 µM claim until the VoR is in hand?
4. Hu thesis retina chapter is the strongest Glu-apt biological evidence in this ledger (authors: basal / minutes, not synapses) **and** is positive within that regime.
5. Two-regime matching is the current title; cleft-millisecond reporting remains UNKNOWN, not disproven.
6. **Do not treat this file as group-final** until a human initials `state/decisions.md`.
7. **Show Abrantes 1 aM preprint** as a cautionary LOD, or omit unofficial numbers entirely? (Millimolar ELONA Kd still not entered.)
8. PR #6 enzyme-comparator wildcard: keep unpromoted until the normal audit pipeline.
