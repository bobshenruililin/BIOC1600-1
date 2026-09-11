# Nightly research handoff

Canonical file for PI review. Not a finished poster. Not group-final.

**Mission 1 (2026-09-11):** science-story gate = **REVISE**. Recommended title is revised two-regime matching (occupancy-at-basal withdrawn as a finding; S066 clocks remain primary). Full record: [`reports/mission1_story_tournament.md`](mission1_story_tournament.md). Gate JSON: `state/gates/science_story.json`. Overnight T1 below is **not** this mission’s result and is still not group-final.

Generated 2026-09-10. Canonical science-content branches after the overnight gate: `main` and `cursor/research-swarm-634f` (same SHA). Mission 1 work lives on `cursor/story-tournament-634f`. Not a finished poster. Not group-final.

## 1. Best current poster thesis

Present glutamate DNA-aptamer sensors have not jointly demonstrated the molecular recognition, selectivity, kinetics, architecture, and validation needed to measure neurochemical dynamics: published Kd, apparent Kd, and LOD values attach to non-transferable constructs, glutamate kon/koff are unreported, and electrochemical clocks (15 min journal MEA; 10 min / 1 min thesis probe) cannot be identified with an inferred 1.2 ms cleft transient.

Status: **provisional, contested** (T1, Stack A). Mean 87/100 on the orchestrator dual-pass. Isolated Task red-teamers invert the ranking. Human approval required.

## 2. Runner-up thesis and why it lost

**T5 (framing challenger, required diversity):** the interesting story is not “aptamers are too slow” (missing kon ≠ negative result). If advertised occupancy parameters are treated as Kd, the µM SELEX isolate is empty at 25 nM and *could* unbind near 1.2 ms under a diffusion-limited kon **bound**, while Hu’s 1.8 nM apparent Kd is ~93% occupied at 25 nM and seconds-slow under the same bound.

T5 tied T1 at Stack A mean 87. It lost the Stack A tie-break because the inversion depends on kon = 1×10^8 M⁻¹ s⁻¹ and on treating electrochemical EC50 as occupancy Kd.

**Overnight result that weakens T5 further:** using ledger small-molecule kon values that are **not glutamate** (C010 96–2×10^5 M⁻¹ s⁻¹; C008 3.5×10^4), even 12 µM t_off is **seconds**, not 0.8 ms. The rising-edge FoM at 1.1 mM, τ_eq = 1/(kon c + koff), can still be milliseconds. That is now a tested figure (`sensitivity.svg`), not a slogan.

Isolated Task R2 still liked T5/T4 as finalists. Isolated Task R1 preferred T3. Do not average stacks.

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
3. **One 1:1 Langmuir site has an 81-fold 10–90% window** (derived, C027). 25 nM vs 1.1 mM is ~44,000-fold. Hu’s 1.8 nM is **not** a 1:1 site; do not overlay 81-fold on a Freundlich EC50 without saying so. Dual-compartment sensing is not a single-Kd job.
4. **Occupancy vs clocks (simulation/bound):** 12 µM is empty at 25 nM (θ<0.01); 1.8 nM is ~93% occupied. Diffusion-limit t_off for 12 µM is ~0.8 ms; inside C010’s high-end kon it is ~0.4 s. Rising-edge τ_eq at 1.1 mM can still be ~9 ms at that kon. Tighter/lower LOD is not automatically better, and koff ≈ 1/1.2 ms is the wrong FoM at millimolar Glu.
5. **The strongest Glu-apt biological experiment already exists and argues against synaptic milliseconds.** Hu thesis retina: light-on/off basal Glu, 1 min ACV, authors refuse synaptic transients. Docking/InstructNA remain hypothesis generation. Ames vs PBS shows buffer composition rewrites the same oligo after selection.

## 5. Three important contradictions / limitations

1. Hu journal 15 min ACV and Hu thesis 10 min / 1 min retina clocks vs Clements 1.2 ms vs missing Glu rates (C006, C028, C031, C011, C007).
2. Park 2023 glutamate FET = malaria GDH, not neurotransmitter glutamate (C019).
3. Wu VoR closed; 1d04/glu1 details beyond the abstract are unverified. Clements is inference. Xiao 10 fM is 0.1× PBS. Thesis Probe 3 saturates at basal Glu; Probe 4 is unstable. Scoring stacks disagree on which thesis to speak.

## 6. Recommended flagship computational analysis

**Occupancy + diffusion-limited koff bound + empirical-kon sensitivity** (`analysis/accepted/occupancy_kinetics/`), with the **evidence atlas** (`analysis/accepted/atlas/`) so empty kon cells cannot be painted over.

It answers a biochemical question (which advertised number is empty vs saturated at 25 nM, and which FoM is t_off vs τ_eq), uses only the ledger, is reproducible, is first-year explainable (θ = c/(c+Kd) and 1/(kon c + koff)), and remains useful if it **contradicts** T5 (it now does, inside C008/C010).

Not recommended: docking, InstructNA training, FASTAptamer without a licensed FASTQ.

## 7. Status of implemented analyses and tests

Accepted:

- Atlas tests + `atlas.svg` (now includes Hu retina-probe 10 min / 0.3 pM; glutamate kon/koff cells remain empty)
- Occupancy/kinetics tests (81-fold identity; 1d04 empty at 25 nM; Hu saturated; diffusion t_off bounds; empirical-kon 1d04 t_off in seconds; τ_eq(cleft) ≪ t_off) + `occupancy.svg` + `clocks.svg` + `sensitivity.svg`

Repo command: `sh analysis/accepted/rebuild.sh` and `python3 -m unittest discover -s tests -v`.

Rejected: docking foil; FASTAptamer toy (does not answer the glutamate question).

Canonical copies: `analysis/accepted/figures/`.

**Best three figures for the handoff (verified, not “latest file”):**

| # | path | why it was kept | labels |
| --- | --- | --- | --- |
| 1 | `analysis/accepted/figures/atlas.svg` | Only plot that refuses to invent glutamate kon/koff | empty cells are empty; ledger units |
| 2 | `analysis/accepted/figures/occupancy.svg` | θ at 25 nM vs 1.1 mM from advertised Kd/EC50 | SIMULATION; nM/mM ticks |
| 3 | `analysis/accepted/figures/sensitivity.svg` | Can contradict T5 if empirical SM kon applies | BOUND/SIMULATION; NOT glutamate |

Rebuild inputs: `research/evidence/core_evidence.csv` (atlas) and ledger constants in `analysis/accepted/occupancy_kinetics/model.py`. Captions forbid “measured koff” / “proves”. `clocks.svg` remains as supporting.

## 8. Six-panel storyboard (text only)

See `poster/storyboards/winner.md`. Panels: two clocks; construct atlas; occupancy inversion + kon sensitivity; LOD ≠ occupancy; interface rewrite; joint-test scorecard **including the retina chapter**.

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
- Scoring-stack inversion (see `rounds/03/tournament_reconciliation.md`).
- Analysis implemented on the swarm branch (sequential single writer) so nothing accepted exists only in an unmerged worktree.
- Overnight PRs: PR #1 closed as superseded. This gate fast-forwards `main` so PR #2 is not left open/unresolved. The thesis is still not group-final.

## 12. Exact Git commit SHA

Canonical tree SHA (stamp; this is the commit to check out): `984af62f25127b43e7d2be248ca1c8123921b8a8`

Science content commit immediately under the stamp: `ce761714b8420df3288f71a78de8734be1a41148`

After pull: `git rev-parse HEAD` on `main` or `cursor/research-swarm-634f` must match the canonical SHA above.

## 13. Exact paths

- Nightly: `reports/nightly_summary.md`
- Evidence table: `research/evidence/core_evidence.csv`
- Poster numbers: `research/evidence/poster_numbers.md`
- Claims: `state/claims.csv`
- Contradictions: `research/reviews/contradictions.md`
- Citation audit: `research/reviews/citation_audit.md`
- Tanner objections: `research/reviews/tanner_objections.md`
- Scoreboard: `state/scoreboard.json`
- Scoring reconciliation: `rounds/03/tournament_reconciliation.md`
- Winner thesis: `poster/theses.md`
- Storyboard: `poster/storyboards/winner.md`
- Figure 1 atlas: `analysis/accepted/figures/atlas.svg`
- Figure 2 occupancy: `analysis/accepted/figures/occupancy.svg`
- Figure 3 sensitivity: `analysis/accepted/figures/sensitivity.svg`
- Supporting clocks: `analysis/accepted/figures/clocks.svg`
- Source code: `analysis/accepted/atlas/atlas.py`, `analysis/accepted/occupancy_kinetics/model.py`, `analysis/accepted/occupancy_kinetics/figures.py`
- Captions: `analysis/accepted/figures/occupancy.CAPTION.md`, `analysis/accepted/figures/atlas.CAPTION.md`
- Table: `analysis/accepted/occupancy_kinetics/tables/occupancy_table.csv`
- Rebuild: `analysis/accepted/rebuild.sh`
- Consolidation log: `rounds/consolidation.md`

## Decisions for PI review tomorrow

1. **Which scoring stack is authoritative?** Stack A orchestrator dual-pass (T1/T5) vs isolated Task red-team (R1: T3; R2: T5/T4). Do not average.
2. **May the poster show a 1×10^8 kon bound** now that `sensitivity.svg` shows C008/C010 put even 12 µM t_off in seconds? BOUND must be larger than the number if shown at all.
3. **Proceed with Wu abstract-only** 1d04/glu1 split, or block any 12 µM claim until the VoR is in hand?
4. **Center the Hu thesis retina chapter** as the strongest Glu-apt biological evidence (authors: basal / minutes, not synapses), or stay with the journal MEA paper only?
5. **Is cleft-millisecond neurodynamics still the Topic 1 center**, or should the group pivot to construct/interface honesty plus basal retinal Glu?
6. **Do not treat this file as group-final** until a human initials `state/decisions.md`.
7. **Show Abrantes 1 aM preprint** as a cautionary LOD, or omit unofficial numbers entirely? (Millimolar ELONA Kd still not entered.)
