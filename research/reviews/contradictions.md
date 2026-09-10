# Contradictions and limitations (Round 2)

Anti-thesis brief: glutamate aptamer sensors do **not** currently jointly match molecular recognition, selectivity, kinetics, architecture, and validation to neurochemical dynamics. Prefer primary experiments. Do not rescue the slogan if the evidence is narrower.

## Load-bearing contradictions

### 1. Kd, LOD, and construct are different objects (Wu vs Hu vs Xiao vs Abrantes)

| construct | quantity | value | source |
| --- | --- | --- | --- |
| 1d04 (Capture-SELEX isolate) | Kd_molecular | 12 µM | S001 abstract |
| truncated glu1 Fc-thiol E-AB | sensor_LOD | 0.0013 pM | S001 abstract |
| Hu Glu-apt Fc-thiol on AuED-MEA | cited Kd label | 12 µM **citation of Wu** | S002 methods |
| same Hu surface construct | electrochemical apparent Kd (Langmuir–Freundlich) | 1.8 nM | S002 §3.2 |
| same Hu construct | sensor_LOD | 32 pM PBS; 51.5 pM 50% serum | S002 Fig. 4h / S11 |
| Xiao glutamate aptamer | SPR Kd | 293 nM | S021 |
| Xiao same family on CNT FET | sensor_LOD | 10 fM in **0.1× PBS** | S021 |
| Abrantes NG-Apt-Glu (in silico, preprint) | claimed FET LOD | 1 aM in aCSF | S010 abstract |

These numbers cannot be averaged into “the glutamate aptamer affinity.” Truncation, surface tethering, transduction, and buffer each move the reported figure. Wu’s 12 µM and 0.0013 pM are **different constructs in the same abstract**.

### 2. No glutamate aptamer kon/koff, while biology is millisecond-scale

Inspected glutamate aptamer sensor papers (S001 abstract, S002 VoR, S021 VoR, S010 abstract) do not report kon or koff.

What exists instead:

- Ding 2024 ITC survey (not glutamate): kon 2×10^5 → 96 M⁻¹ s⁻¹ and koff 1.03×10⁻³ → 0.012 s⁻¹ as Kd goes 28 nM → 864 µM (abstract).
- Abeykoon 2025 tobramycin surface IPA: kon 3.5×10⁴ M⁻¹ s⁻¹, koff 1.39 s⁻¹, 2 ms **interrogation**.
- Clements 1992: inferred cleft peak 1.1 mM, τ 1.2 ms.
- Herman 2007: ambient slice glutamate near 25 nM.
- Hu 2025: Glu ACV after **15 min** incubation.
- Xiao 2025: FET response stabilized after **200 s**.
- Rutherford 2007 GlutOx: 500–800 ms in freely moving rats.
- Clay 2018 GlutOx model: simulated 0.73 s, experimental 0.8 ± 0.2 s.

A 15 min electrochemical wait and a 1.2 ms cleft transient are not the same kinetic claim. IPA’s 2 ms clock is measurement_time, not glutamate koff.

### 3. One Langmuir window cannot cover tonic nM and cleft mM

Rousseau 2023: a 1:1 Langmuir isotherm predicts an **81-fold** concentration span between 10% and 90% occupancy.

Herman ambient ~25 nM to Clements cleft 1.1 mM is a **44,000-fold** gap. Hu’s Glu semi-log window 0.1 nM–10 µM (10⁵-fold on a log plot, but still an analytical calibration, not a synaptic occupancy proof) does not make a single Kd a dual-compartment glutamate meter.

### 4. Sensor waveform ≠ free glutamate (even for protein sensors)

Armbruster 2020: iGluSnFR time courses often last 10–100 times longer than the extracellular lifetime of synaptically released glutamate; the indicator buffers and delays uptake. If a genetically encoded glutamate sensor already reports a filtered waveform, an unlabeled “aptamer keeps up with neurotransmission” claim is not licensed by LOD alone.

### 5. Reviews mislabel glutamate

Park 2023 Table 1 row “Glutamate FET” cites Singh 2019 *P. falciparum* glutamate dehydrogenase, not neurotransmitter glutamate. Do not harvest that row into a neurotransmitter aptasensor table.

### 6. In vivo leap is not done for glutamate aptamers

Zhao 2021 and Wu 2022 Nano Lett show implantable aptamer FETs for **serotonin** and **dopamine**. Hu 2025 ends with intended future in vitro/in vivo NT work. No verified in vivo glutamate aptamer sensor in this ledger.

### 7. Docking / generative AI is hypothesis generation

Xie/Liu 2026: docking scores fail to separate theophylline from caffeine despite a cited 250,000-fold experimental affinity difference. InstructNA improves some SPR hit rates on **protein** targets and still produces many non-binders. Abrantes designs NG-Apt-Glu in silico; that is not a SELEX-validated glutamate Kd in the inspected abstract.

## Limitations that are not contradictions but block overclaim

- Wu VoR closed; 1d04 vs glu1 details beyond the abstract are unverified.
- Clements is a kinetic inference, not a chemical assay; cultured synapses.
- Herman 25 nM is slice ambient glutamate with intact transport, not a free extrasynaptic-only number.
- Xiao 0.1× PBS is not 1× aCSF and not in vivo.
- Ohsawa 2008 and MacDonald 2019 numbers were **not** re-verified this session; they stay out of `claims.csv`.
- Clay 2021 (in vitro calibration ≠ in vivo [Glu]) remains abstract-only.

## What this does to the slogan

“Aptamer quality is not a single number” is **directionally supported** (Kd ≠ LOD ≠ EC50 ≠ incubation time ≠ biological [Glu]). It is too broad as a poster thesis: the defensible claim is about **glutamate aptamer sensors and neurochemical timescales**, not aptamers in general.

## Hunter error log (this round)

A prior contradiction pass stated Clay 2018 t90 0.73–0.8 s was absent. Re-inspection of PMC5881573 found: “The simulated response time, 0.73 s, also matches very closely with experimental response times (0.8 ± 0.2 s).” That sentence is now C023. The hunter is not an authority over the paper.

## Papers that weaken the *generalization* “aptamers cannot keep up”

These do **not** supply glutamate kon/koff. They weaken treating “too slow” as a property of aptamers rather than of the glutamate papers we have.

| paper | what it shows | limit |
| --- | --- | --- |
| White 2008 S033 | cocaine E-AB equilibrates faster than ~4 s scan dead time | cocaine, not glutamate |
| Abeykoon 2025 S004 / Santos-Cancel 2018 S025 | IPA interrogation 2 ms; tobramycin surface kon/koff measurable | not glutamate; 2 ms is the clock |
| Arroyo-Currás 2018 S026 | chronoamperometric E-AB in living body on ~300 ms scale | tobramycin in vivo, not glutamate |
| Kumakli 2023 S029 | ATP E-AB microelectrode 80–140 ms under flow | mass transport, ATP, not glutamate |
| Zhao 2021 S018 / Wu 2022 S019 | implantable aptamer FETs in vivo | serotonin / dopamine, not glutamate |
| Helassa 2018 S060 | iGluu τ_off ~2 ms can follow 100 Hz release | protein indicator, not aptamer |

**Hard contradiction to T1?** No. T1 already says joint competence is undemonstrated, not that koff was measured slow.

**Hard contradiction to T5?** If measured glutamate koff at 1.8 nM apparent Kd is ≫ 0.18 s⁻¹, the diffusion bound using that EC50 as molecular Kd fails. That experiment does not exist in the ledger.

## Occupancy identity is no longer review-only

C027 derives the 81-fold 10–90% Langmuir span algebraically. Rousseau 2023 remains a community statement of the same identity, not the sole evidence.
