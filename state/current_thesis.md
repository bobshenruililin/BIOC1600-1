# Current thesis (revised D)

Status: **canonical working thesis** after Mission 1.5. Not group-final (`state/decisions.md`).  
Storyboard: `poster/storyboards/revised_D.md`.  
Supersedes overnight T1/T5 as *current consensus*. Those texts remain historical in `poster/theses.md`, `analysis/candidates/theses/`, and `rounds/03/`.

Do not treat this file as a finished poster.

## One sentence

There is no generic glutamate-aptamer sensor: neurochemistry is two measurement regimes (slow/basal versus rapid transients); a 1:1 Langmuir site spans exactly 81-fold while two commonly cited hippocampal literature concentrations span ~44,000-fold; the only glutamate-aptamer experiment in nervous tissue in this ledger is positive evidence inside a basal/slow clock; occupancy on that retinal probe is unmeasured; missing `koff` does not prove slow kinetics.

## Full statement

**“Good glutamate sensor” is not a scalar.** Biology supplies two regimes that a poster must not collapse:

1. **Slow / basal extracellular measurement** — sustained or slowly changing ambient glutamate, sampled on seconds-to-minutes clocks.
2. **Rapid transient measurement** — brief, high-amplitude events (including inferred synaptic-cleft waveforms).

Herman & Jahr 2007 (S050 / C012) frame synaptic transients as superimposed on a low baseline in **acute hippocampal slice**. Ambient glutamate after efficacy scaling is about **25 nM**. That is Herman’s two-component sentence, not three occupancy windows, and not an extrasynaptic-only assay.

Clements et al. 1992 (S049 / C011, abstract-only) infer free glutamate at **cultured hippocampal synapses**: peak about **1.1 mM**, decay τ about **1.2 ms**. That is a kinetic inference, not a chemical concentration assay, and it is a **different hippocampal preparation** from Herman’s slices.

Those two numbers are **literature examples from different hippocampal experimental contexts**. They are not a measured retinal concentration range, not a specification for Hu’s parylene-C (PaC) probe, and not a license to treat retina as a failed hippocampal-cleft sensor. Photoreceptor glutamate is graded, not Clements-quantal.

A 1:1 Langmuir site spans exactly **81-fold** between 10% and 90% occupancy (`c10 = Kd/9`, `c90 = 9 Kd`), independent of Kd (C027, `computational illustration`; Rousseau states the same identity, C013 `review-supported`). 25 nM → 1.1 mM is **44,000-fold** (`computational illustration` on C012 and C011). The 81-fold identity is a **biochemical design principle**. It is not a fitted working range of the retinal probe. Hu’s electrochemical calibration was Langmuir–Freundlich; the heterogeneity exponent *n* is unpublished, so a 10–90% window on that isotherm would be 81^(1/*n*), not 81.

**Hu’s retinal work is positive neural-tissue evidence within its demonstrated temporal regime.** Hu 2025 RWTH thesis (S066): **in vitro** isolated mouse retina, not the journal AuED-MEA paper (S002), not in vivo (C020). Authors: basal / sustained extracellular glutamate, **not** synaptic transients (C031). Clocks that were actually run: ~14 s/ACV scan, ~1 min/point after insertion, ~10 min plateau after a 10 nM glutamate step (C028, C031). Probes 1–2 produced light-correlated ACV changes in the direction expected for basal glutamate. That is a device-and-physiology feasibility result on a minutes-scale basal clock. It does not answer how much glutamate, from which pool, or with pharmacological identity.

**Occupancy on the retinal PaC probe is unmeasured.** The probe has no reported apparent Kd in Ames or tissue. Do not use Hu’s **1.8 nM** Langmuir–Freundlich apparent electrochemical fit (C005: AuED-MEA in PBS; stored as `EC50`) as the retinal probe’s molecular `Kd`. That number is a different device, a different isotherm class, and a different matrix. A 1:1 overlay θ(25 nM) ≈ 0.93 on 1.8 nM is a `computational illustration` of advertised numbers, not tissue occupancy. Probe 3/4 failed; Fig. 6.16 attributes failure to detached gold nanostructure, which can mimic early saturation (occupancy reading `unresolved`). Probes 1–2 still modulate with light, which is remaining dynamic range at whatever the retinal basal actually is, not a saturation measurement.

**Millisecond cleft reporting is untested, not disproven.** No glutamate aptamer `kon`/`koff` is in the inspected set (C007, `unresolved`). Tobramycin IPA (C008) and Ding ITC envelopes (C010) are not glutamate and must not be transferred. Missing `koff` does **not** prove slow kinetics: τ_eq = 1/(kon·*c* + koff) can be short at millimolar *c* even when t_off is long (`computational illustration`). Do not quote koff ≈ 1/1.2 ms. Interrogation time (IPA 2 ms, C009; ACV 14 s) is not binding koff.

Construct, matrix, device, and quantity type remain distinct. 12 µM is Wu’s 1d04 abstract `Kd_molecular` (C001) and, separately, a Wu **citation** in Hu’s methods (C021), not a Hu remeasurement. 32 pM / 51.5 pM are AuED-MEA LODs (C004). 0.3 pM is PaC-probe PBS blank+3 RSD with lowest calibrant 1 nM (C029), not Ames (C030). Xiao 293 nM is SPR `Kd_molecular`; 10 fM is FET LOD in 0.1× PBS (C014). Herman’s NMDAR EC50 1.8 **µM** on nucleated patches (E035) is not Hu’s 1.8 **nM** electrochemical apparent Kd.

Glu versus Asp/Gln/GABA is a named open figure of merit (C032), not a fifth title.

## Load-bearing claims (tagged)

| # | Claim | Tag | IDs |
|---|---|---|---|
| 1 | Herman: transients superimposed on a low baseline — two components, not three. | `primary-source-supported` | C012, S050 |
| 2 | 1:1 Langmuir 10–90% span is exactly 81-fold, independent of Kd. | `computational illustration` / `review-supported` | C027, C013 |
| 3 | 25 nM and 1.1 mM / 1.2 ms are hippocampal literature examples from **different preparations**, not a retinal range. | `primary-source-supported` as those papers’ own results; transfer to retina `unknown` | C012, C011 |
| 4 | S066 clocks and author basal/slow disclaimer. | `primary-source-supported` | C031, C028, C006 |
| 5 | S066 Probes 1–2: light-correlated ACV in vitro retina — positive evidence in that temporal regime. | `primary-source-supported` | C031, S066 |
| 6 | Occupancy at basal on the PaC probe in Ames/tissue is **unmeasured**. 1.8 nM is AuED-MEA LF apparent Kd, not PaC molecular Kd. | `unresolved` (empty PaC Kd); C005 `primary-source-supported` as a **different** device | C005, C021, C026 |
| 7 | Probe 3 is author-flagged gold-detachment failure; occupancy-ceiling reading unresolved. | `primary-source-supported` as failure analysis; occupancy `unresolved` | S066 Fig. 6.16 |
| 8 | No glutamate aptamer kon/koff. Missing koff does not prove a millimolar rising edge is impossible. | `unresolved` / `computational illustration` | C007, C008, C010 |
| 9 | Aptamer electrode reported at GCL/IPL border; light-dependence narrative invokes photoreceptor terminals. | `primary-source-supported` as the layer tension | S066; H2/H3 |
| 10 | Amino-acid selectivity panel lacks Asp/Gln/GABA. | `primary-source-supported` as an empty panel | C032 |

## Inference boundary

**Measured.** Herman two-component framing and ~25 nM in acute hippocampal slice. Clements abstract inference at cultured hippocampal synapses. Hu AuED-MEA 1.8 nM LF apparent Kd, 15 min wait, 32/51.5 pM LODs. Hu PaC-probe PBS/Ames calibrations, 10 min plateau, 14 s / 1 min retina clocks, Probes 1–2 light correlation, Probe 3/4 gold-detachment notes. Empty glutamate kon/koff search in the inspected set.

**Inferred (not claimed here).** That 25 nM is retinal or in vivo [Glu]. That 1.1 mM / 1.2 ms specifies an aptamer electrode volume. That 1.8 nM overlay is tissue occupancy. That missing koff means the oligo cannot follow a millimolar rising edge.

**Unknown.** PaC-probe apparent Kd and θ in Ames/tissue. Langmuir–Freundlich *n* on the MEA fit. Glutamate aptamer kon/koff on the 39-mer. Chemical identity of the S066 ACV change. Electrode-layer versus photoreceptor pool. Ames glutamine interference. In vivo glutamate aptamer sensor.

## Falsifier

- A PaC-probe isotherm in Ames/tissue that places θ in a useful band at a **measured** ambient [Glu] without saturating would fill the occupancy unknown (it would not make Herman/Clements a retinal range).
- Pharmacology plus a scrambled-aptamer probe that leaves the light-off ACV increase intact would falsify reading that increase as glutamate occupancy.
- A measured glutamate-aptamer `koff`/`kon` on the 39-mer would replace the empty kinetic cell; a short τ_eq at millimolar *c* with a matching interrogation clock would move the transient column from untested toward tested.
- Herman’s own two-component sentence still kills any three-regime occupancy-window title.

## Must not claim

- Extrasynaptic-only 25 nM.
- Herman 25 nM and Clements 1.1 mM as this retina experiment’s concentration range.
- Hu 1.8 nM as the retinal probe’s molecular Kd, or θ(25 nM)≈0.93 as measured tissue occupancy.
- Missing koff proves slow kinetics, or koff ≈ 1/1.2 ms.
- Hu retina failed as a hippocampal-cleft sensor.
- 0.3 pM as Ames or tissue LOD.
- In vivo glutamate aptamer sensing.
- Abrantes millimolar ELONA Kd (not in the ledger).
- Overnight T1 as this mission’s result.

## Supporting panels (titles retired)

- **C (runner-up):** ultrasensitive working-range ceilings miss Herman ~25 nM from above (Wu glu1 top 1 nM; Abrantes preprint 10 pM). Hu 32 pM is a real matrix-matched LOD and must not be binned with vanity LODs.
- **B:** construct × quantity key. Empty glutamate kon/koff cells stay empty. Non-transfer is hygiene, not a physical law (DA apparent Kd ≈ cited 44 µM in the same LF panel).
- **A:** same-oligo four-grade teaching table. “Fit for purpose” is not a title.

## Highest-value next step

`proposed experiment`: paired solution `Kd_molecular` and surface ACV apparent Kd of Hu’s exact Fc-thiol 39-mer in one buffer; fit Langmuir and Langmuir–Freundlich; report *n* and coverage.

If the biological question is retinal glutamate rather than sensor fitness, substitute pharmacological identity (TTX, CNQX/AP5, TBOA, scrambled aptamer). Do not do both and report neither.

## Historical note

Unrevised Candidate D claimed current devices “fail the slow problem on occupancy.” That occupancy half lacked primary evidence (1:1 overlay of an LF EC50 from a different device, plus gold-confounded Probe 3). Mission 1.5 **withdraws occupancy-as-finding**. The clocks half, the two-regime framing, the 81-fold identity, and the empty kon/koff cell remain.
