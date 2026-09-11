# Candidate C — LOD is not usefulness; occupancy at ambient is the paradox

**One-sentence thesis.** Extraordinary LODs do not make a glutamate aptamer sensor biologically useful. The load-bearing mismatch is occupancy (and working range) at the ambient concentration the biology papers actually report — not detection capability as such.

**Program label.** LOD paradox (Mission 1 Program C).

**Trio.** Steelman `bc-053dfcf9`; red team `bc-2496c55a`; independent `bc-baf29d39`.

**Trio verdict on this program (not a ranking of A–D).** Steelman: KEEP a sharpened form — **saturation-at-basal / working-range-in-matrix**, not “LOD too small.” Red team: **REVISE** the slogan “LOD distracts”; do not FAIL the underlying insight. Independent: LODs distract; the missing FoM is occupancy at ambient, not kinetics.

---

## Why this could be the BIOC1600 story

Papers lead with LOD. Wu glu1 **0.0013 pM** with range **0.01 pM–1 nM** (C002; S001 abstract). Abrantes preprint **1 aM** in aCSF with linear range **1 aM–10 pM** (C025). Xiao practical LOD **10 fM** in **0.1× PBS**, Ids span 10 fM–100 nM (C014). Hu MEA **32 pM** PBS / **51.5 pM** 50% serum (C004). Thesis probe **0.3 pM** PBS blank+3 RSD (C029).

Herman ambient glutamate is **~25 nM** (C012) = 25 000 pM. Clements inferred cleft peak is **1.1 mM** (C011).

If 1.8 nM (Hu LF apparent Kd) is overlaid as a 1:1 occupancy Kd, θ(25 nM) ≈ **0.93** (SIMULATION). Leftover unbound ≈ 6.7%. A still-lower LOD cannot create dynamic range for a cleft transient. Hu thesis Probe 3 is author-reported as **near saturation at basal** despite a 0.3 pM PBS LOD (C031). Ames linear window **10 nM–10 µM** with 41.6% blank noise (C030) is the matrix that actually bathes the retina experiment.

**Wildcard (C independent / C red team):** ultrasensitive **working-range ceilings miss Herman 25 nM from above**. Wu top-of-range 1 nM is 25-fold below 25 nM. Abrantes abstract ceiling 10 pM is 2500-fold below 25 nM. The LOD contest selects calibrations orthogonal to the tonic number the group uses as biology.

---

## Load-bearing claims

1. **Hu 32 pM already sits ~780-fold below 25 nM.** Arithmetic on C004 and C012; `computational illustration` as a ratio, numbers `primary-source-supported`. Strong form “you need aM LOD to see tonic glutamate” is false if Herman is the target and Hu is the sensor.
2. **Herman 25 nM was measured by NMDAR occupancy, not by an ultrasensitive chemical LOD.** `primary-source-supported` (S050).
3. **Hu 32 / 51.5 pM is matrix-matched blank+3SD, not a press-release vanity LOD.** `primary-source-supported` (C004). Limitation: 50% serum ≠ undiluted brain ECF.
4. **Wu 0.0013 pM and Abrantes 1 aM (and Xiao 10 fM in 0.1× PBS) are the misleading usefulness proxies.** `primary-source-supported` as advertised LODs; `hypothesis` that they are used as biological-usefulness proxies (Wu “great potential in vivo”; Abrantes leads with 1 aM).
5. **Same-family LODs do not reproduce 0.0013 pM.** Hu 32 pM and thesis 0.3 pM are related constructs, different devices/estimators. No independent replication of 0.0013 pM found. `hypothesis`.
6. **81-fold is 1:1 occupancy 10–90%, not Hu’s 10^5-fold semi-log calibration.** `review-supported` / `computational illustration` (C013, C027). Overlaying 81-fold on LF 1.8 nM is a mechanism caveat.
7. **Gold-nanostructure loss can mimic an occupancy ceiling** (Hu thesis Probe 3 / Fig. 6.16). Author-owned; do not treat Probe 3 as a measured basal [Glu] at the Langmuir ceiling.

---

## What the red team breaks

“LOD distracts from biological usefulness” as a slogan straw-mans analytical chemistry: LOD is a measurement-process FoM (Currie/IUPAC). The error is **using LOD as a biological proxy**, not reporting LOD.

Attack (1) fails in strong form (32 pM already “sees” 25 nM as an analytical concentration). It survives only vs enzyme GlutOx detection limit **0.2 µM** (S054) if Herman 25 nM is the target — and that is a different sensor class.

Attack (2): do **not** bin Hu 32/51.5 pM with Wu 0.0013 pM and Abrantes 1 aM. Serum 51.5 pM is real antifouling/recovery chemistry.

Attack (3): occupancy span and clock are the load-bearing paradox. Candidate C may be rejected **as the title** in favour of an occupancy/timescale story that keeps two vanity LODs as a supporting caution.

---

## Independent cut

The missing measurement is **θ at ambient glutamate on the construct used in tissue**, not a glutamate `koff` (which is also missing). Wu’s advertised range does not contain 25 nM. Ames already contains documented L-glutamine (public A1420: 0.073 g/L) while the selectivity panel never challenged Gln — that is a C032 hole, not proof of Gln interference (W1).

---

## Inference boundary

**Measured:** LOD/range numbers above; Probe 3 author saturation sentence; Ames SNR sentence.

**Inferred:** that 0.0013 pM is unstable as a glu1 property; that LOD contests *cause* wrong windows rather than merely coexist with them.

**Unknown:** Glu `kon`/`koff`; in-tissue [Glu]; whether Probe 3 is isotherm saturation or gold loss.

**Do not infer:** synaptic usefulness from sensor_LOD; solution Kd from surface EC50; 1× aCSF performance from Xiao 0.1× PBS; occupancy from LOD; Abrantes ELONA millimolar Kd.

---

## Falsifier

C-as-slogan dies if the poster’s only point is “LOD is bad.” C-as-paradox dies if a Glu-apt working range in the **tissue matrix** covers Herman ambient with θ in ~0.1–0.9 and the authors still lead with aM LOD as the usefulness claim — then LOD and occupancy have been aligned. C dies as title if occupancy/clocks already carry the same numbers without mentioning LOD.

---

## One-poster form

Left: vanity LOD vs working-range ceiling vs 25 nM (Wu, Abrantes). Right: Hu 32 pM as legitimate blank-noise vs Probe 3 saturation in Ames/tissue. Caption: two LOD definitions (3SD vs 3RSD) and PBS vs Ames.

**Must not claim:** Hu 32 pM is vanity; 0.3 pM is the retina-in-Ames LOD; 1.8 nM overlay is a measured tissue occupancy.

**Highest-value next step.** Occupancy (or at least a non-saturating calibration) of the PaC probe in Ames around 10–100 nM, with a scrambled-aptamer control — not a lower PBS LOD.
