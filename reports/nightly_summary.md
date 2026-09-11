# Nightly research handoff

Canonical file for PI review. Not a finished poster. Not group-final.

**Mission 1 (2026-09-11):** science-story gate = **REVISE**. Recommended title is revised D (two regimes; occupancy-at-basal withdrawn as a finding; S066 clocks remain primary). Full record: [`reports/mission1_story_tournament.md`](mission1_story_tournament.md). Gate JSON: `state/gates/science_story.json`. Overnight T1 below is **not** this mission’s result and is still not group-final.

This file now carries that recommendation in §1. It does **not** convert the gate to PASS. Human approval still required for group-final.

Generated 2026-09-11. Not a finished poster. Not group-final.

## 1. Best current poster thesis

There is no generic glutamate-aptamer sensor. Neurochemistry is two regimes (Herman’s baseline plus superimposed transients). A 1:1 Langmuir site spans exactly 81-fold between 10% and 90% occupancy, while those literature concentrations span ~44,000-fold. The only neural-tissue Glu-apt experiment (Hu thesis S066) is already clock-limited to basal/slow sampling. Occupancy at that basal on the parylene-C probe in Ames or tissue is **unmeasured**, not shown saturated. Millisecond cleft reporting is **untested** — missing `koff` does not prove a millimolar rising edge is impossible.

Status: **recommended working thesis, not group-final** (`D_revised`). Gate remains **REVISE**. Herman ~25 nM and Clements ~1.1 mM come from **different hippocampal preparations** and are not a retinal range. Hu 1.8 nM is an AuED-MEA Langmuir–Freundlich apparent Kd, not the PaC probe’s molecular Kd.

## 2. Runner-up thesis and why it lost

**Candidate C (Mission 1 runner-up, supporting panel):** ultrasensitive working-range ceilings miss Herman ~25 nM from above (Wu glu1 top 1 nM; Abrantes preprint 10 pM). After C’s strong LOD form is deleted, what remains is occupancy/working-range/clocks — D’s content. Hu 32 pM is a real **PBS** LOD; 51.5 pM is the 50% serum LOD.

**Historical overnight T5** (not current): if advertised occupancy parameters are treated as Kd, the µM SELEX isolate is empty at 25 nM and *could* unbind near 1.2 ms under a diffusion-limited kon **bound**, while Hu’s 1.8 nM apparent Kd is ~93% occupied at 25 nM. That overlay is MODELED, not tissue occupancy, and is demoted as a finding.

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
3. **One 1:1 Langmuir site has an 81-fold 10–90% window** (derived, C027). 25 nM vs 1.1 mM is ~44,000-fold. Hu’s 1.8 nM is **not** a 1:1 site; do not overlay 81-fold on a Freundlich EC50 without saying so. Dual-compartment sensing is not a single-Kd job.
4. **Occupancy overlay is not a tissue finding.** 12 µM empty at 25 nM and 1.8 nM ~93% occupied are `computational illustration` on advertised Kd/EC50, including a device hop (AuED-MEA → PaC probe). PaC occupancy in Ames/tissue is **unmeasured**.
5. **The strongest Glu-apt biological experiment already exists and is clock-limited to basal/slow sampling.** Hu thesis retina: authors refuse synaptic transients; 14 s/ACV then ~1 min sampling. Missing `koff` does not prove a millimolar rising edge is impossible. Docking/InstructNA remain hypothesis generation.

## 5. Three important contradictions / limitations

1. Hu journal 15 min ACV and Hu thesis 10 min / 1 min retina clocks vs Clements 1.2 ms vs missing Glu rates (C006, C028, C031, C011, C007).
2. Park 2023 glutamate FET = malaria GDH, not neurotransmitter glutamate (C019).
3. Wu VoR closed; 1d04/glu1 details beyond the abstract are unverified. Clements is inference. Xiao 10 fM is 0.1× PBS. Thesis Probe 3 saturates at basal Glu; Probe 4 is unstable. Scoring stacks disagree on overnight T1 vs T5; that fight is historical, not the Mission 1 title fight.

## 6. Recommended flagship computational analysis

**81-fold 1:1 Langmuir identity** (C027) versus the ~44,000-fold span between two **hippocampal literature examples** (C012, C011), implemented in `analysis/accepted/occupancy_kinetics/` from public ledger numbers only. Demote `occupancy.svg` as a tissue-occupancy finding: it remains a labeled SIMULATION of advertised Kd/EC50, including a device hop.

Supporting: evidence atlas (`atlas.svg`) so empty glutamate kon/koff cells stay empty; `sensitivity.svg` can contradict overnight T5 inside non-glutamate C008/C010 envelopes (do not transfer those rates).

Not recommended: docking, InstructNA training, FASTAptamer without a licensed FASTQ.

## 7. Status of implemented analyses and tests

Accepted:

- Atlas tests + `atlas.svg` (now includes Hu retina-probe 10 min / 0.3 pM; glutamate kon/koff cells remain empty)
- Occupancy/kinetics tests (81-fold identity; 1d04 empty at 25 nM; Hu saturated overlay math; diffusion t_off bounds; empirical-kon 1d04 t_off in seconds; τ_eq(cleft) ≪ t_off) + `occupancy.svg` + `clocks.svg` + `sensitivity.svg`

Repo command: `sh analysis/accepted/rebuild.sh` and `python3 -m unittest discover -s tests -v`.

Rejected: docking foil; FASTAptamer toy (does not answer the glutamate question).

Canonical copies: `analysis/accepted/figures/`.

**Best three figures for the handoff (verified, not “latest file”):**

| # | path | why it was kept | labels |
| --- | --- | --- | --- |
| 1 | `analysis/accepted/figures/atlas.svg` | Only plot that refuses to invent glutamate kon/koff | empty cells are empty; ledger units |
| 2 | `analysis/accepted/figures/occupancy.svg` | 81-fold identity lives here; θ overlay is SIMULATION not tissue occupancy | SIMULATION; nM/mM ticks |
| 3 | `analysis/accepted/figures/sensitivity.svg` | Can contradict T5 if empirical SM kon applies | BOUND/SIMULATION; NOT glutamate |

Rebuild inputs: `research/evidence/core_evidence.csv` (atlas) and ledger constants in `analysis/accepted/occupancy_kinetics/model.py`. Captions forbid “measured koff” / “proves”. `clocks.svg` remains as supporting.

## 8. Six-panel storyboard (text only)

Current recommendation: `reports/mission1_story_tournament.md` §4 (revised D). Historical overnight T1 storyboard: `poster/storyboards/winner.md` (superseded as current; occupancy inversion demoted as a finding).

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
- PaC-probe apparent Kd / θ in Ames or tissue unmeasured; Langmuir–Freundlich *n* unpublished.
- Wu VoR inaccessible; JSTAGE Ohsawa PDF 500; MacDonald ACS 403 — those numbers were **not** entered.
- Abrantes millimolar ELONA Kd still not entered. Second-extraction attempt this cycle: bioRxiv HTML/JATS HTTP 429; Europe PMC/API abstract has no ELONA Kd. Do not treat API tokens 10.3 / 25.1 (funder IDs) as affinity.
- Scoring-stack inversion is **historical** (`rounds/03/tournament_reconciliation.md`). Not current recommendation.
- Science-story gate remains **REVISE**. Occupancy-as-finding withdrawn; that withdrawal does not by itself convert the gate to PASS.
- Open research PRs stay on hold until a human records the remaining close choices.

## 12. Exact Git commit SHA

Canonical tree SHA for this poster-file alignment (stamp after commit on `cursor/story-on-poster-245a`). Check out that branch; do **not** treat overnight SHA `984af62f25127b43e7d2be248ca1c8123921b8a8` as current §1 content.

After this PR’s commit: `git rev-parse HEAD` on `cursor/story-on-poster-245a`.

## 13. Exact paths

- Nightly: `reports/nightly_summary.md`
- Mission 1 tournament: `reports/mission1_story_tournament.md`
- Evidence table: `research/evidence/core_evidence.csv`
- Poster numbers: `research/evidence/poster_numbers.md`
- Claims: `state/claims.csv`
- Contradictions: `research/reviews/contradictions.md`
- Citation audit: `research/reviews/citation_audit.md`
- Tanner objections: `research/reviews/tanner_objections.md`
- Scoreboard: `state/scoreboard.json`
- Historical scoring reconciliation: `rounds/03/tournament_reconciliation.md`
- Current thesis: `poster/theses.md`
- Historical T1 storyboard: `poster/storyboards/winner.md`
- Gate: `state/gates/science_story.json`
- Figure 1 atlas: `analysis/accepted/figures/atlas.svg`
- Figure 2 occupancy (demoted as tissue finding; 81-fold identity tested here): `analysis/accepted/figures/occupancy.svg`
- Figure 3 sensitivity: `analysis/accepted/figures/sensitivity.svg`
- Supporting clocks: `analysis/accepted/figures/clocks.svg`
- Source code: `analysis/accepted/atlas/atlas.py`, `analysis/accepted/occupancy_kinetics/model.py`, `analysis/accepted/occupancy_kinetics/figures.py`
- Captions: `analysis/accepted/figures/occupancy.CAPTION.md`, `analysis/accepted/figures/atlas.CAPTION.md`
- Table: `analysis/accepted/occupancy_kinetics/tables/occupancy_table.csv`
- Rebuild: `analysis/accepted/rebuild.sh`
- Consolidation log: `rounds/consolidation.md` (historical overnight merge)

## Decisions for PI review

1. **Poster sentence is revised D** in this file and `poster/theses.md`, matching the 2026-09-11 `state/decisions.md` row. Overnight T1 is historical. Confirm or revert.
2. **Keep the science-story gate REVISE** (this PR). Do not take child PR #28 PASS without an explicit human row.
3. **May the poster show a 1×10^8 kon bound** now that `sensitivity.svg` shows C008/C010 put even 12 µM t_off in seconds? BOUND must be larger than the number if shown at all. Flagship no longer depends on that bound.
4. **Proceed with Wu abstract-only** 1d04/glu1 split, or block any 12 µM claim until the VoR is in hand?
5. Hu thesis retina chapter is the strongest Glu-apt biological evidence in this ledger (authors: basal / minutes, not synapses).
6. **Do not treat this file as group-final** until a human initials `state/decisions.md`.
7. **Show Abrantes 1 aM preprint** as a cautionary LOD, or omit unofficial numbers entirely? (Millimolar ELONA Kd still not entered.)
8. Mission 2 drafts (A3/A4/wildcard) stay parked until you say otherwise.
