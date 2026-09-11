# Current poster thesis (revised D)

Not a finished poster. Not group-final (`state/decisions.md`).
Science-story gate remains **REVISE** (`state/gates/science_story.json`).

Recommended by Mission 1 (`reports/mission1_story_tournament.md`). Overnight T1/T5 ranking is **historical** (below). Do not treat T1 as this mission’s result.

## Current (Mission 1)

**There is no generic glutamate-aptamer sensor.** Neurochemistry is two regimes (Herman’s baseline plus superimposed transients). A 1:1 Langmuir site spans exactly 81-fold between 10% and 90% occupancy, while those literature concentrations span ~44,000-fold. The only neural-tissue Glu-apt experiment (Hu thesis S066) is already clock-limited to basal/slow sampling. Occupancy at that basal on the parylene-C probe in Ames or tissue is **unmeasured**, not shown saturated. Millisecond cleft reporting is **untested** — missing `koff` does not prove a millimolar rising edge is impossible.

Herman ~25 nM (C012) and Clements ~1.1 mM / 1.2 ms (C011, abstract-only) are hippocampal literature examples from **different preparations**, not a measured retinal concentration range. Hu’s 1.8 nM Langmuir–Freundlich apparent electrochemical Kd (C005) is an AuED-MEA number in PBS, not the PaC probe’s molecular Kd. A 1:1 overlay θ(25 nM)≈0.93 is a `computational illustration`, not tissue occupancy.

**Runner-up (panel, not title):** Candidate C — ultrasensitive working-range ceilings miss Herman ~25 nM from above (Wu glu1 top 1 nM; Abrantes preprint 10 pM). Hu 32 pM is a real **PBS** LOD (C004); 51.5 pM is the 50% serum LOD.

Supporting panels: B construct×quantity key; A same-oligo grade table. W1 (Asp/Gln) is a named unknown (C032), not a fifth title.

**Flagship analysis:** 81-fold 1:1 Langmuir identity (C027, `computational illustration`) versus the ~44,000-fold Herman-to-Clements span; demote the 1.8 nM overlay as tissue occupancy. Implemented with public ledger numbers in `analysis/accepted/occupancy_kinetics/`.

**Highest-information next experiment:** paired solution and surface isotherm of Hu’s Fc-thiol 39-mer in one buffer; report Langmuir–Freundlich *n*.

## Historical — overnight thesis tournament (2026-09-10)

**Superseded as current recommendation.** Files kept: `analysis/candidates/theses/`, `poster/storyboards/winner.md`, `rounds/03/`. Mission 1 explicitly did not adopt this ranking (`state/decisions.md`).

### Historical Stack A “winner” (mean 87 / 100; both scorers ≥85)

**Present glutamate DNA-aptamer sensors have not jointly demonstrated the molecular recognition, selectivity, kinetics, architecture, and validation needed to measure neurochemical dynamics:** published Kd, apparent Kd, and LOD values attach to non-transferable constructs, glutamate kon/koff are unreported, and a 15 min electrochemical incubation cannot be identified with an inferred 1.2 ms cleft transient.

Source: isolated writer T1. Historical storyboard: `poster/storyboards/winner.md`.

**Scoring was contested.** Isolated Task red-teamers invert this ranking (Task R1 winner T3; Task R2 finalists T5/T4). See `rounds/03/tournament_reconciliation.md`. Never group-final.

### Historical runner-up (mean 87 / 100)

**T5 framing challenger.** The distinctive story is not “aptamers are too slow” (that treats missing kon/koff as a negative result). If advertised occupancy parameters are taken at face value, the µM SELEX isolate is the one that could unbind near 1.2 ms under a diffusion-limited kon **bound**, while the nM surface apparent Kd is already occupied at 25 nM and would be seconds-slow under the same bound. T5 lost the Stack A tie-break because that inversion is a bound/simulation, not a glutamate kinetic measurement.

### Historical tournament table (do not average stacks)

| id | R1 | R2 | mean | historical Stack A decision |
| --- | ---: | ---: | ---: | --- |
| T1 | 89 | 85 | 87 | winner (tie-break: fewer extra assumptions) |
| T5 | 89 | 85 | 87 | runner-up (framing challenger; required diversity) |
| T4 | 88 | 84 | 86 | hold/finalist split |
| T2 | 87 | 83 | 85 | hold/finalist split |
| T3 | 83 | 78 | 80.5 | hold |

Isolated Task scores are **not** averaged into this table. Stack B: T3 86 / T1 79 (R1) and T5=T4 85 / T1 83 (R2).

No slogan was forced. “Aptamer quality is not a single number” is implied by the construct split but is not the current headline.
