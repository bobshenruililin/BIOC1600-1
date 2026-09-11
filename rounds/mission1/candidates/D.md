# Candidate D — Two biological regimes, not a generic glutamate sensor

**One-sentence thesis.** “Good glutamate sensor” is an illegitimate generic. Biology supplies **two** regimes (ambient/slow extracellular vs cleft/fast), not three occupancy windows. Current Glu-apt devices fail the slow problem on occupancy and clocks; millisecond cleft reporting is untested because `kon`/`koff` are missing — and missing `koff` does not by itself prove a rising edge at 1.1 mM is impossible.

**Program label.** Neurochemical scale matching (Mission 1 Program D).

**Trio.** Steelman `bc-8c323354`; red team `bc-6ee36931`; independent `bc-602c145b`.

**Trio verdict on this program (not a ranking of A–D).** Steelman: two regimes sharper than three; KEEP sharpened. Red team: **REVISE** — do not KEEP “three problems”; do not FAIL. Independent: two components, not three; load-bearing failure is **occupancy at basal**, not a missing third “slow extracellular” Kd.

---

## Why this could be the BIOC1600 story

Herman & Jahr 2007 (S050): synaptic glutamate transients “are superimposed on a low baseline concentration of glutamate in the extracellular space.” Ambient ~**25 nM** after efficacy scaling. That is **baseline + transient**, not three pools. “Extrasynaptic” is not Herman’s own compartment label (C012). Cited dialysis 1–4 µM is the contrast they reject, not a third design spec.

Clements et al. 1992 (S049, abstract): inferred free glutamate at **cultured hippocampal synapses**, peak **1.1 mM**, decay τ **1.2 ms** (C011). Transfer to retina or an aptamer electrode volume is `unknown`.

1:1 Langmuir 10–90% occupancy is exactly **81-fold** (`c10=Kd/9`, `c90=9 Kd`), independent of Kd (C027; Rousseau 2023). 25 nM → 1.1 mM is **44 000-fold**. One 1:1 site cannot cover tonic-to-cleft.

Occupancy overlay of **advertised** numbers (SIMULATION/BOUND):

| Advertised number | Quantity type | θ(25 nM) | θ(1.1 mM) |
|---|---|---|---|
| 1d04 12 µM | `Kd_molecular` (Wu abstract) | 0.21% | 98.9% |
| Hu 1.8 nM | LF apparent electrochemical Kd / `EC50`, **not** 1:1 molecular Kd | **93.3%** | ~100% |
| Xiao 293 nM | SPR `Kd_molecular` | 7.9% | ~100% |

Hu leftover unbound at 25 nM ≈ 6.7% if that overlay is believed. The only neural-tissue Glu-apt experiment already reports **basal occupancy failure** (Probe 3) and **authors disclaim synaptic transients** (C031). Wu glu1 advertised range **0.01 pM–1 nM** contains **neither** Herman tonic nor Clements cleft.

Photoreceptor glutamate is **graded**, not Clements quantal. Do not score Hu retina as a failed hippocampal-cleft sensor. Hu chose the basal/slow regime in tissue (authors). The journal MEA paper still sells brain-wide FoM (15 min wait, 32 pM LOD, “physiologically relevant … brain”).

---

## Load-bearing claims

1. **Two biological components, not three.** `primary-source-supported` from Herman’s own framing (S050).
2. **44 000-fold vs 81-fold.** Arithmetic on C011/C012/C027; `computational illustration`.
3. **Hu 1.8 nM must not be treated as 1:1 molecular Kd.** `primary-source-supported` (C005, C021, C026).
4. **S066 is basal/slow by the authors.** `primary-source-supported` (C031). Dual-mode is two clocks, two sites, one shank (H1–H3).
5. **No glutamate aptamer `kon`/`koff`.** `unresolved` (C007). Tobramycin IPA and Ding ITC are **not glutamate** (C008, C010). Do not quote `koff ≈ 1/1.2 ms`.
6. **τ_eq = 1/(kon c + koff) at 1.1 mM can be short even when t_off is long.** `computational illustration` (occupancy table). Red team: missing koff does **not** prove the sensor cannot do synapses.
7. **“Slower extracellular dynamics” is a clock and a method fight, not a third Kd.** Rutherford GlutOx: detection limit 0.2 µM (8× Herman 25 nM); “resting” 7.3 µM striatum / 44.9 µM PFC (S054). Minting a third occupancy problem from GlutOx “tonic” launders that fight into a design spec.
8. **Protein indicators already abandoned the generic.** Marvin iGluSnFR ~4 µM affinity “precludes quantitation of millimolar glutamate”; later affinity variants; Armbruster: waveforms 10–100× longer than free Glu in part because the indicator buffers (C024). Comparators, not aptamers.
9. **Glu vs Asp/Gln is an addition, not a replacement thesis.** C032 empty ratio; W1 REJECT as fifth story. If synapses are in scope, name interferent-realistic concentrations; do not invent millimolar cleft Asp.

---

## What the red team breaks

Do not KEEP “three neurochemical problems.” The middle extrasynaptic band is mostly **tool-class and time**; [Glu] for that band is unspecified across ~10³-fold (Moussawi review span 0.02–30 µM, `review-supported`).

Do not FAIL D: occupancy at basal plus named clocks is still the course-level question.

Revised D FoMs: (i) basal occupancy on the construct in the matrix; (ii) pulse occupancy **and** falling-edge koff **if** synapses are in scope; (iii) Glu vs Asp/Gln at interferent-realistic concentrations. LOD is not that list.

Journal Hu still sold brain-wide usefulness while the thesis experiment is basal/slow — Candidate D must not pretend the authors only ever claimed retina basal Glu.

**Wildcard (D independent):** Herman nucleated-patch glutamate **EC50 1.8 µM** vs Hu electrochemical apparent Kd **1.8 nM**. Same digits, 1000-fold, different quantity types. A poster that prints “1.8” without unit and quantity tag invents a sensor that sits on NMDARs.

---

## Independent cut

The defensible story is occupancy-at-basal as the filter, with millisecond cleft reporting presently **untestable** for Glu-apt (no koff, no cleft-relevant amino-acid selectivity, S066 authors decline the interpretation). “Good glutamate sensor” as a scalar — especially pM/aM LOD — hides a 2-axis spec: **isotherm placement at the concentration you sit in** × **clock = binding + interrogation**.

---

## Inference boundary

**Measured:** Herman ambient framing and 25 nM; Clements abstract inference; Hu clocks and Probe 3; empty Glu kon/koff search.

**Inferred:** that 25 nM is retinal or in vivo [Glu]; that Clements specifies an aptamer electrode; that 1.8 nM overlay is tissue occupancy.

**Unknown:** Glu-apt koff; whether τ_eq at millimolar cleft concentrations would be fast enough on these oligos; in vivo Glu-apt.

E-AB time resolution = equilibration + electrochemical analysis (Rousseau). IPA 2 ms is interrogation, not Glu koff (C009). Diffusion-limited t_off for 1.8 nM at kon=10^8 is ~5.6 s as an **upper-speed bound**, not a measurement.

---

## Falsifier

D-as-three-regimes dies on Herman’s own two-component sentence. D-as-occupancy-at-basal dies if a Glu-apt in tissue reports θ in a useful band at a measured ambient [Glu] without saturating. D-as-“cannot do synapses because no koff” dies if τ_eq at 1.1 mM is measured short and the interrogation clock matches. A scrambled-aptamer or TTX/CNQX/TBOA control that leaves the S066 light-off ACV increase intact falsifies reading that increase as photoreceptor glutamate occupancy.

---

## One-poster form

Two columns: basal/slow vs cleft/fast. Numbers: 25 nM, 1.1 mM, 81-fold, 44 000-fold, S066 1 min / basal / Probe 3, empty kon/koff cell. Footnote: 1.8 nM is LF overlay; 1.8 µM is NMDAR EC50. Do not draw a third extrasynaptic Kd.

**Must not claim:** extrasynaptic-only 25 nM; koff ≈ 1/1.2 ms; GlutOx/iGluSnFR performance transfer; Hu failed as a hippocampal-cleft sensor; in vivo Glu-apt.

**Highest-value next step.** If the poster’s biological question is basal retina Glu: pharmacological identity + Ames occupancy, not a faster scan. If synapses are in scope: IPA-style `kon`/`koff` on the 39-mer **and** a µM-scale isotherm — still would not be a tissue cleft measurement until done in tissue.
