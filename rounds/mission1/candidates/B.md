# Candidate B — Construct non-identity (not a transformation mechanism)

**One-sentence thesis.** A number measured on one glutamate-aptamer construct, phase, or architecture is not the number of the next. Wu 1d04 `Kd_molecular` 12 µM, glu1 `sensor_LOD` 0.0013 pM, and Hu Langmuir–Freundlich 1.8 nM are different objects.

**Program label.** Construct transformation (Mission 1 Program B).

**Trio.** Steelman `bc-f16d3b77`; red team `bc-7cb3dc5d`; independent `bc-2dd31e8c`.

**Trio verdict on this program (not a ranking of A–D).** Steelman and independent: KEEP if framed as **construct non-identity**, not as “don’t mix Kd and LOD” alone. Red team: **FAIL as the strongest poster story**; survive only as a supporting hygiene panel. Occupancy overlay is a consequence of which number is promoted to Kd, not a B-specific discovery.

---

## Why this could be the BIOC1600 story

Wu’s own abstract already narrates two constructs: isolate **1d04** Kd **12 µM**, then **truncated glu1** E-AB LOD **0.0013 pM** (C001, C002, C003). Hu’s methods label the truncated Fc-thiol Glu-apt “Kd = 12 µM (Wu et al., 2022)” — a **citation**, not a remeasurement (C021) — then report surface apparent Kd **1.8 nM** from a Langmuir–Freundlich ACV fit (C005) and attribute the gap “among others” to 2D vs 3D confinement (C026). Xiao independently splits SPR Kd **293 nM** vs FET LOD **10 fM** in 0.1× PBS (C014). White 2008 (cocaine, `transferable=no` to Glu) shows packing density moves gain and apparent Kd; immobilization is not a null operation (C018).

That split is the most striking numerical exhibit in the ledger. A first-year can be taught not to average “the glutamate aptamer Kd.”

---

## Load-bearing claims

1. **1d04 Kd and glu1 LOD are different constructs in one abstract.** `primary-source-supported` (C001–C003). Wu VoR closed; `full_text_inspected=no`.
2. **Hu 12 µM is cited Wu, not a surface-oligo remeasurement.** `primary-source-supported` (C021).
3. **Hu 1.8 nM is electrochemical apparent Kd / EC50 (LF), not molecular Kd.** `primary-source-supported` (C005).
4. **Sequence identity can transfer while Kd does not.** Hu 39-mer matches the 5′ 39 nt of Lam 2022’s 98-nt Wu-cited string (`review-supported` for the map; Wu VoR not inspected). `transferable=yes` for the nucleotide string; `transferable=no` for Kd.
5. **Truncated glu1 / Hu 39-mer solution `Kd_molecular` is unknown.** `unresolved`.
6. **S066 does not inherit S002 MEA 1.8 nM / 32 pM.** Different device (PaC probe vs AuED-MEA), different matrices (Ames/tissue vs PBS/serum).

---

## What the red team breaks

Program B as a **mechanism** (“construct transformation / 2D confinement is what we discovered”) fails:

- Wu’s abstract is a successful-sensor pipeline, not a paired truncation-Kd experiment.
- Hu already wrote the confinement caveat. Repeating §3.2 is not a student result.
- **Wildcard (B red team):** in the same LF panel, DA apparent Kd **49.6 µM** ≈ cited **44 µM**. ST and Glu “transform”; DA does not. A uniform interface-physics law fails inside Hu’s table. The Glu jump is more economically **wrong quantity + wrong parent construct**.
- Some properties **do** transfer: sequence string; Au–thiol chemistry as method; White cocaine surface Kd sometimes matches solution Kd at low density; Daniel thrombin surface Kd extrapolates to solution Kd at low grafting. “Nothing transfers” is false.
- Ricci 2016, which Hu cites in the LF neighborhood, is a **1:1 Langmuir / 81-fold** Account and documents cocaine truncation shifting affinity up to 2800-fold. It does **not** develop Langmuir–Freundlich (`supports_claim=no` for “Ricci 2016 = LF”).
- Lam’s `12 ± 6 µM` is a review table citing Wu, not a Wu-abstract number. Do not poster ±6 as Wu.

**Red-team rubric as strongest story: 53/100 (discard).** Hygiene panel (“Kd, LOD, and electrochemical apparent Kd are different objects”) can survive.

---

## Independent cut

If B is framed as **construct non-identity**, it is a real BIOC1600 thesis: you may not move 12 µM onto glu1, nor 1.8 nM onto 1d04, nor journal MEA numbers onto the retina probe. If it is framed as a measured transformation of affinity by truncation or confinement, the experiment was not done. Occupancy-at-synapse pictures then become a **warning illustration** of promoting the wrong number to Kd, not a stronger biological result owned by B.

---

## Inference boundary

**Measured:** construct-tagged numbers above; Hu confinement sentence; DA 49.6 vs 44 µM as Hu reports them.

**Inferred:** 12 µM as Kd of the truncated Fc-thiol 39-mer; 2D confinement as *the* cause of 12 µM vs 1.8 nM; “construct transformation” as a biochemical mechanism.

**Unknown:** glu1 solution Kd; Wu truncation cut sites from VoR; LF heterogeneity exponent; Glu `kon`/`koff`.

**Do not promote:** Abrantes millimolar ELONA Kd (unverified; prior extraction found API `10.3`/`25.1` as funder IDs).

---

## Falsifier

B-as-mechanism dies if a paired solution vs surface `Kd_molecular` of the **same** 39-mer agrees near 1.8 nM (confinement is then a result) or near 12 µM (1.8 nM is then an isotherm/transduction number). B-as-hygiene dies only if those objects are shown to be the same measurement. Oral kill if the storyboard treats 12 µM → 1.8 nM as a measured truncation result.

---

## One-poster form

A construct×quantity table (C001, C002, C004, C005, C014, C021) with empty cells left empty. Not a SELEX flowchart as the title. Occupancy curves only if captioned as “if this advertised number were a 1:1 Kd.”

**Must not claim:** parent→truncated Kd transfer; Ricci 2016 as the LF paper; Lam ±6 as Wu; Park GDH; Tanner tetrahedron as glutamate immobilization proof (it is N-protein optical fiber, C015).

**Highest-value next step.** Wu VoR if it opens, or ITC/SPR `Kd_molecular` of Hu’s exact 39-mer in the PBS of the ACV isotherm.
