# Nightly research handoff

Canonical file for PI review. Not a finished poster. Not group-final.

Generated 2026-09-10. Commit SHA is in section 12 (filled after this file is committed).

## 1. Best current poster thesis

Present glutamate DNA-aptamer sensors have not jointly demonstrated the molecular recognition, selectivity, kinetics, architecture, and validation needed to measure neurochemical dynamics: published Kd, apparent Kd, and LOD values attach to non-transferable constructs, glutamate kon/koff are unreported, and a 15 min electrochemical incubation cannot be identified with an inferred 1.2 ms cleft transient.

Status: **provisional** (T1). Mean score 87/100. Human approval required before it is the group thesis.

## 2. Runner-up thesis and why it lost

**T5 (framing challenger, required diversity):** the interesting story is not “aptamers are too slow” but that the literature’s “better” nM apparent Kd / pM LOD numbers, if treated as occupancy Kd, are saturated at 25 nM and seconds-slow under a diffusion-limited kon **bound**, whereas the µM SELEX isolate could be kinetically near 1.2 ms and empty at tonic glutamate.

T5 tied T1 at mean 87. It lost the tie-break because the inversion depends on an assumed kon upper bound and on treating electrochemical EC50 as occupancy Kd. It is the flagship **calculation**, not the safest oral sentence.

## 3. Top verified primary sources (smallest set)

1. Wu 2022 S001 PMID 34783880 — 1d04 Kd 12 µM vs glu1 LOD 0.0013 pM (abstract only).
2. Hu 2025 S002 PMID 40992279 — Glu apparent Kd 1.8 nM; LOD 32 pM / 51.5 pM; 15 min wait; 12 µM is a Wu citation (VoR).
3. Xiao 2025 S021 PMID 40433802 — SPR Kd 293 nM; FET LOD 10 fM in 0.1× PBS; 200 s (PMC).
4. Herman 2007 S050 PMID 17804634 — ambient slice glutamate ~25 nM (PMC).
5. Clements 1992 S049 PMID 1359647 — inferred cleft 1.1 mM, τ 1.2 ms (abstract).
6. Rutherford 2007 S054 — GlutOx 500–800 ms in moving rats (PMC).
7. White 2008 S033 — packing density moves E-AB gain/apparent Kd; cocaine <4 s (PMC; not glutamate).
8. Abeykoon 2025 S004 — tobramycin IPA kon/koff and 2 ms clock (PMC; not glutamate).
9. Xie/Liu 2026 S046 — docking fails theophylline/caffeine selectivity (PMC).
10. InstructNA 2026 S007 — generated protein aptamers; many non-binders (PMC).
11. Armbruster 2020 S062 — iGluSnFR waveforms 10–100× free glutamate (PMC).
12. Park 2023 S023 — “Glutamate FET” row is PfGDH (caution, not a sensor).
13. Xu/Tanner 2026 S006 — tetrahedron interface, N-protein only (PMC).

Full table: `research/evidence/poster_numbers.md`.

## 4. Five most important scientific insights

1. **Kd ≠ LOD ≠ EC50 ≠ incubation time ≠ biological [Glu].** Wu’s 12 µM and 0.0013 pM are different constructs in one abstract. Hu’s 12 µM is a citation; 1.8 nM is a surface Langmuir–Freundlich apparent Kd; 32 pM is a blank+3SD LOD after 15 min.
2. **No glutamate aptamer kon/koff** in inspected sensor papers. “Too slow” is a gap, not a measured koff.
3. **One 1:1 Langmuir site has an 81-fold 10–90% window** (derived, C027). 25 nM vs 1.1 mM is ~44,000-fold. Dual-compartment sensing is not a single-Kd job.
4. **Occupancy inversion (simulation/bound):** using advertised numbers as occupancy Kd, 12 µM is empty at 25 nM but could unbind near 1.2 ms if kon is diffusion-limited; 1.8 nM is ~93% occupied at 25 nM and has t_off ~6 s under the same bound. Tighter is not automatically better for dynamics.
5. **Docking/InstructNA are hypothesis generation.** Docking inverted a 250,000-fold selectivity; InstructNA still produces non-binders and was not run on glutamate.

## 5. Three important contradictions / limitations

1. Hu 15 min ACV vs Clements 1.2 ms vs missing Glu rates (C006, C011, C007).
2. Park 2023 glutamate FET = malaria GDH, not neurotransmitter glutamate (C019).
3. Wu VoR closed; 1d04/glu1 details beyond the abstract are unverified. Clements is inference, not a chemical assay. Xiao 10 fM is 0.1× PBS.

## 6. Recommended flagship computational analysis

**Occupancy + diffusion-limited koff bound** (`analysis/accepted/occupancy_kinetics/`), with the **evidence atlas** (`analysis/accepted/atlas/`) so empty kon cells cannot be painted over.

It answers a biochemical question, uses only the ledger, is reproducible, is first-year explainable (θ = c/(c+Kd)), and remains useful if it contradicts “too slow” (the µM isolate’s bound is near 1.2 ms).

Not recommended: docking, InstructNA training, FASTAptamer without a licensed FASTQ.

## 7. Status of implemented analyses and tests

Accepted and replicated in a clean directory:

- Atlas tests + `atlas.svg`
- Occupancy/kinetics tests (81-fold identity; 1d04 empty at 25 nM; Hu saturated; t_off bounds) + `occupancy.svg` + `clocks.svg`

Repo command: `sh analysis/accepted/rebuild.sh` and `python3 -m unittest discover -s tests -v`.

Rejected: docking foil; FASTAptamer toy (does not answer the glutamate question).

## 8. Six-panel storyboard (text only)

See `poster/storyboards/winner.md`. Panels: two clocks; construct atlas; occupancy inversion; LOD ≠ occupancy; interface rewrite; joint-test scorecard.

## 9. Hardest five assessor questions

From `research/reviews/tanner_objections.md`:

1. Is 15 min the aptamer’s koff, or when you chose to scan?
2. Why is Hu’s 1.8 nM not “the” Kd?
3. Show the 81-fold 10–90% identity without a review.
4. Why not plot tobramycin IPA 2 ms as proof aptamers are fast enough?
5. What experiment would make you withdraw the thesis?

## 10. Swarm/prompt improvements that survived benchmarking

Observed failure: 4/4 isolated thesis writers refined the same frame. Adopted patch in `AGENTS.md`: at least one candidate must challenge the current framing. T5 exists because of that rule. Constitution, rubric, and safety files were not edited. Meta loop stopped after this one observed-failure class.

## 11. Failures, unresolved uncertainties, blockers

- Glutamate kon/koff unmeasured.
- No in vivo glutamate aptamer sensor in this ledger.
- Wu VoR inaccessible; JSTAGE Ohsawa PDF 500; MacDonald ACS 403 — those numbers were **not** entered.
- Abrantes millimolar ELONA Kd not in the abstract; not entered.
- Two Task red-teamers were launched in parallel; recorded scores are the dual locked-rubric passes in `rounds/03/scores_r1.json` and `scores_r2.json`.
- Analysis implemented on the swarm branch (sequential single writer) so nothing accepted exists only in an unmerged worktree.

## 12. Exact Git commit SHA

`SHA_PENDING_COMMIT`

## 13. Exact paths

- Evidence table: `research/evidence/core_evidence.csv`
- Poster numbers: `research/evidence/poster_numbers.md`
- Claims: `state/claims.csv`
- Contradictions: `research/reviews/contradictions.md`
- Citation audit: `research/reviews/citation_audit.md`
- Tanner objections: `research/reviews/tanner_objections.md`
- Scoreboard: `state/scoreboard.json`
- Winner thesis: `poster/theses.md`
- Storyboard: `poster/storyboards/winner.md`
- Figure 1 atlas: `analysis/accepted/atlas/figures/atlas.svg`
- Figure 2 occupancy: `analysis/accepted/occupancy_kinetics/figures/occupancy.svg`
- Figure 3 clocks: `analysis/accepted/occupancy_kinetics/figures/clocks.svg`
- Captions: `analysis/accepted/atlas/figures/CAPTION.md`, `analysis/accepted/occupancy_kinetics/figures/CAPTION.md`
- Rebuild: `analysis/accepted/rebuild.sh`

## Decisions for PI review tomorrow

1. **Tie-break:** keep T1 as the oral thesis and T5 as the computational panel, or flip them?
2. **May the poster show a diffusion-limited kon bound** if the word BOUND is unavoidable on the figure?
3. **Proceed with Wu abstract-only** 1d04/glu1 split, or block any 12 µM claim until the VoR is in hand?
4. **Show Abrantes 1 aM preprint** as a cautionary LOD, or omit unofficial numbers entirely?
5. **Is glutamate neurodynamics still the Topic 1 center**, or should the group pivot to interface/construct honesty without cleft milliseconds?
6. **Do not treat this file as group-final** until a human initials `state/decisions.md`.
7. **Out-of-repo experiment:** is IPA kon/koff on Hu’s Glu-apt worth proposing as future work, knowing this course cannot run it?
