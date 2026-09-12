# Current thesis (revised D)

Status: **canonical working thesis** after Mission 1 closure. Science-story gate **REVISE**. Mission 2 science freeze: **FREEZE** at **REVISE** (evidence-boundary restatement; tournament 85+ still unreached). QUANTITATIVE FLAGSHIP: **NONE** (`unresolved` as title). Not group-final (`state/decisions.md`). READY FOR MISSION 3: **NO**.

Provisional storyboard: `poster/storyboards/revised_D.md`. The flagship analysis is unresolved: **NONE** as title; do not reopen selection as an open action.
Supersedes overnight T1/T5 as *current consensus*. Those texts remain historical in `poster/theses.md`, `analysis/candidates/theses/`, and `rounds/03/`.

Do not treat this file as a finished poster.

## One sentence

Hu’s Ø 25 µm Fc-thiol 39-mer MEASURES current on two tissue legs with unequal IVs—post-insertion rise (time; light on) and later on–off–on (illumination)—both INFERRED as glutamate. Printed `%gain` maps cannot invert tissue ACV; identity stays UNKNOWN until named U2. Rapid-transient readiness remains unmeasured.

## Full statement

**“Good glutamate sensor” is not a scalar.** Biology supplies two regimes that a poster must not collapse:

1. **Slow / basal extracellular measurement** — sustained or slowly changing ambient glutamate, sampled on seconds-to-minutes clocks.
2. **Rapid transient measurement** — brief, high-amplitude events (including inferred synaptic-cleft waveforms).

Herman & Jahr 2007 (S050 / C012) frame synaptic transients as superimposed on a low baseline in **acute hippocampal slice**. Ambient glutamate after efficacy scaling is about **25 nM**. That is Herman’s two-component sentence, not three occupancy windows, and not an extrasynaptic-only assay.

Clements et al. 1992 (S049 / C011, abstract-only) infer free glutamate at **cultured hippocampal synapses**: peak about **1.1 mM**, decay τ about **1.2 ms**. That is a kinetic inference, not a chemical concentration assay, and it is a **different hippocampal preparation** from Herman’s slices.

Those two numbers are **literature examples from different hippocampal experimental contexts**. They are not a measured retinal concentration range, not a specification for Hu’s parylene-C (PaC) probe, and not a license to treat retina as a failed hippocampal-cleft sensor. Clements’ quantal-cleft preparation is not evidence about photoreceptor release. Mission 1 therefore does not treat the arithmetic between those endpoints as a representative biological range for a surface electrode.

A 1:1 Langmuir site spans exactly **81-fold** between 10% and 90% occupancy (`c10 = Kd/9`, `c90 = 9 Kd`), independent of Kd (C027, `computational illustration`; Rousseau states the same identity, C013 `review-supported`). The 81-fold identity remains valid **supporting biochemistry**. It is not a fitted working range of the retinal probe. Hu’s electrochemical calibration was Langmuir–Freundlich; the heterogeneity exponent *n* is unpublished, so a 10–90% window on that isotherm would be 81^(1/*n*), not 81.

PR #31 challenged the former 81-fold-versus-44,000-fold flagship on two grounds: basal glutamate poles vary with method and compartment, and the unreported Langmuir–Freundlich exponent can change the working-range conclusion. Those objections are preserved in `state/model_disagreements.md` and `state/mission2_input_queue.md`; their candidate source rows are not promoted merely because the review is persuasive. The old comparison is withdrawn as the flagship. Mission 2 froze QUANTITATIVE FLAGSHIP: **NONE** (sampling-clock, dual-pole working-range bars, and occupancy overlay remain rejected; do not reopen “must choose a replacement” as an open action).

**Hu’s retinal work is two MEASURED tissue-current legs with unequal IVs; analyte identity is UNKNOWN on both.** Hu 2025 RWTH thesis (S066): **in vitro** isolated mouse retina, not the journal AuED-MEA paper (S002), not in vivo (C020). Authors interpret the current as basal / sustained extracellular glutamate, **not** synaptic transients (C031, C033). Clocks that were actually run: 14 s/ACV scan, 1 min/point after insertion, 10 min plateau after a 10 nM glutamate step (C028, C031, E045). Two experimental legs (C033 / E046, Fig. 6.13) vary **unequal independent variables**, not two equally designed Glu assays: (A) post-insertion `%gain` rise (time; light held on) from a dashed baseline (authors: “successful detection of Glu”); (B) later room-light on–off–on (illumination) (Probes 1–2 authors p < 0.05; Probes 3–4 ns). Room lights, not the 500 ms LED vitality protocol. Printed PBS/Ames `%gain` maps (PBS 11.86 %/decade; Ames 57.11 %/decade) cannot invert tissue ACV to [Glu] or θ; Ames blank noise 41.6% (C030 / E044) — no absolute tissue concentration is claimed. Ch. 7 “reliably resolve steady-state differences in extracellular Glu concentration” is not a licensed MEASURED reading of Fig. 6.13 (boxes include all points; first-arm IQR is the variance reason for the **initial** light-on bin, not a finding that “Fig. 6.13 is not steady-state”; late-only rebin *p* stays UNKNOWN). The glutamate-aptamer ACV electrode is the large bottom electrode at the GCL/IPL border on the same probe as spikes (C034 / E045). Whether that site matches a photoreceptor-terminal narrative remains UNKNOWN. Same-shank ON-pathway firing rates higher in light do not identify the ACV analyte. Spike maps are not Leg A and are not Leg B.

**Occupancy on the retinal PaC probe is unmeasured.** The probe has no reported apparent Kd in Ames or tissue. Do not use Hu’s **1.8 nM** Langmuir–Freundlich apparent electrochemical fit (C005: AuED-MEA in PBS; stored as `EC50`) as the retinal probe’s molecular `Kd`. That number is a different device, a different isotherm class, and a different matrix. A 1:1 overlay θ(25 nM) ≈ 0.93 on 1.8 nM is a `computational illustration` of advertised numbers, not tissue occupancy. Do not recover θ from either printed `%gain` law; do not use slope ratio `57.11/11.86` as occupancy or identity. Probe 3/4 failed; Fig. 6.16A attributes failure to detached gold nanostructure, which can mimic early saturation (occupancy reading `unresolved`). Fig. 6.16A (gold loss) and Fig. 6.16B (1 kHz Z after cleaning) are distinct operations; do not collapse Fig. 6.12 (insertion peak drop) with Fig. 6.16B. Probes 1–2 still modulate with light, which is remaining dynamic range at whatever the retinal basal actually is, not a saturation measurement.

**Millisecond cleft reporting is untested, not disproven.** No glutamate aptamer `kon`/`koff` is in the inspected set (C007, `unresolved`). Tobramycin IPA (C008) and Ding ITC envelopes (C010) are not glutamate and must not be transferred. Missing `koff` does **not** prove slow kinetics: τ_eq = 1/(kon·*c* + koff) can be short at millimolar *c* even when t_off is long (`computational illustration`). Do not quote koff ≈ 1/1.2 ms. Interrogation time (IPA 2 ms, C009; ACV 14 s) is not binding koff.

PR #24 is a Mission-2 **analysis candidate**, not an accepted result. Its coarse observation is an interrogation/sampling-timescale mismatch between the 14 s scan / roughly 60 s sampling clocks and a 1.2 ms literature waveform. Do not call this “Nyquist” in canonical recommendations unless a formal signal model, bandwidth, sampling operator, and reconstruction claim are defended.

Construct, matrix, device, and quantity type remain distinct. 12 µM is Wu’s 1d04 abstract `Kd_molecular` (C001) and, separately, a Wu **citation** in Hu’s methods (C021), not a Hu remeasurement. 32 pM / 51.5 pM are AuED-MEA LODs (C004). 0.3 pM is PaC-probe PBS blank+3 RSD with lowest calibrant 1 nM (C029), not Ames (C030). Xiao 293 nM is SPR `Kd_molecular`; 10 fM is FET LOD in 0.1× PBS (C014). Herman’s NMDAR EC50 1.8 **µM** on nucleated patches (E035) is not Hu’s 1.8 **nM** electrochemical apparent Kd.

Glu versus Asp/Gln/GABA is a named open figure of merit (C032), not a fifth title. Appendix II lists Glu/Gln/Asp as printed g/l (molarity unconverted). Ames is not a Glu-free ionic twin of PBS and is not a demonstrated Ames confounder. Ames-loaded wording stays dropped.

## Load-bearing claims (tagged)

| # | Claim | Tag | IDs |
|---|---|---|---|
| 1 | Herman: transients superimposed on a low baseline — two components, not three. | `primary-source-supported` | C012, S050 |
| 2 | 1:1 Langmuir 10–90% span is exactly 81-fold, independent of Kd; it is supporting biochemistry, not Hu’s fitted range. | `computational illustration` / `review-supported` | C027, C013 |
| 3 | 25 nM and 1.1 mM / 1.2 ms are hippocampal literature examples from **different preparations**, not a retinal range or an accepted device specification. | `primary-source-supported` as those papers’ own results; transfer to retina `unknown` | C012, C011 |
| 4 | S066 clocks and author basal/slow disclaimer. | `primary-source-supported` | C031, C028, C006 |
| 5 | S066 ACV on a Glu-aptamer electrode in vitro retina (14 s scan, ~1 min/point; room lights, not 500 ms LED). Two MEASURED tissue-current legs with unequal IVs: (A) post-insertion rise (time; light on); (B) later on–off–on (illumination). Authors interpret both as glutamate. Analyte identity UNKNOWN on both. Printed `%gain` maps cannot invert tissue ACV. Ames SNR poor; no absolute [Glu]. | `primary-source-supported` as ACV; identity `unresolved` | C033, E046, C030, E044 |
| 6 | Occupancy at basal on the PaC probe in Ames/tissue is **unmeasured**. 1.8 nM is AuED-MEA LF apparent Kd, not PaC molecular Kd. | `unresolved` (empty PaC Kd); C005 `primary-source-supported` as a **different** device | C005, C021, C026 |
| 7 | Probe 3 is author-flagged gold-detachment failure; occupancy-ceiling reading unresolved. | `primary-source-supported` as failure analysis; occupancy `unresolved` | S066 Fig. 6.16; E046 notes |
| 8 | No glutamate aptamer kon/koff. Missing koff does not prove a millimolar rising edge is impossible. | `unresolved` / `computational illustration` | C007, C008, C010 |
| 9 | Aptamer ACV electrode at the GCL (large bottom electrode), same probe as spikes. IPL-border versus photoreceptor-terminal narrative remains UNKNOWN. | `primary-source-supported` as GCL placement (C034/E045); pool `unresolved` | C034, E045 |
| 10 | Amino-acid selectivity panel lacks Asp/Gln/GABA. | `primary-source-supported` as an empty panel | C032 |
| 11 | QUANTITATIVE FLAGSHIP: NONE (unresolved as title). PRs #23/#24 remain rejected-as-flagship analysis candidates; PR #31 is a candidate challenge. | `unresolved` | `state/mission2_input_queue.md` |

## Inference boundary

**Measured.** Herman two-component framing and ~25 nM in acute hippocampal slice. Clements abstract inference at cultured hippocampal synapses. Hu AuED-MEA 1.8 nM LF apparent Kd, 15 min wait, 32 pM PBS LOD and 51.5 pM 50% serum LOD. Hu PaC-probe PBS/Ames calibrations including 41.6% Ames blank noise, 10 min plateau, 14 s / 1 min retina clocks, both ACV legs as current with unequal IVs (C033), GCL/IPL-border bottom electrode (C034), Probe 3/4 gold-detachment notes. Empty glutamate kon/koff search in the inspected set. Glu is MEASURED only where Glu was the spiked IV.

**Inferred (not claimed here).** That 25 nM is retinal or in vivo [Glu]. That 1.1 mM / 1.2 ms specifies an aptamer electrode volume. That 1.8 nM overlay is tissue occupancy. That missing koff means the oligo cannot follow a millimolar rising edge. That either S066 ACV leg is chemically glutamate. That the first-arm rise is occupancy of prevailing tissue Glu rather than interface settling. That `%gain` ∝ θ.

**Unknown.** PaC-probe apparent Kd and θ in Ames/tissue. Langmuir–Freundlich *n* on the MEA fit. Glutamate aptamer kon/koff on the 39-mer. Chemical identity of both S066 ACV legs, including the post-insertion baseline-rise “successful detection” sentence. Electrode-layer versus photoreceptor pool. Asp/Gln/GABA `%gain` ratios on this film. Tissue transfer function. Post-insert Ntot. Whether a late-only rebin of Fig. 6.13 keeps *p* < 0.05. In vivo glutamate aptamer sensor. QUANTITATIVE FLAGSHIP remains NONE (unresolved as title). Mission 2 froze an evidence-boundary thesis at REVISE; 85+ remains unreached on public evidence. Four empties stay four cells, not one slogan.

**Modeled (illustration only).** Slope ratio 57.11/11.86. Do not convert Appendix II g/l to claimed molarity. Do not treat C_eq as tissue [Glu].

## Falsifier

- A PaC-probe isotherm in Ames/tissue that places θ in a useful band at a **measured** ambient [Glu] without saturating would fill the occupancy unknown (it would not make Herman/Clements a retinal range).
- Pharmacology plus a scrambled/binding-null probe on **both** ACV legs, same shank and room-light protocol, that leaves the currents intact would falsify reading those currents as glutamate occupancy. Do not substitute rates for identity if the claim is U2. An optional late-only split of Fig. 6.13 does not name the analyte.
- A measured glutamate-aptamer `koff`/`kon` on the 39-mer would replace the empty kinetic cell; a short τ_eq at millimolar *c* with a matching interrogation clock would move the transient column from untested toward tested.
- Herman’s own two-component sentence still kills any three-regime occupancy-window title.

## Must not claim

- Extrasynaptic-only 25 nM.
- Herman 25 nM and Clements 1.1 mM as this retina experiment’s concentration range.
- The Herman-to-Clements arithmetic as a settled, representative biological span for a surface electrode.
- PR #24 as an accepted analysis, or “Nyquist” as a formal theorem without its signal assumptions.
- Hu 1.8 nM as the retinal probe’s molecular Kd, or θ(25 nM)≈0.93 as measured tissue occupancy.
- Missing koff proves slow kinetics, or koff ≈ 1/1.2 ms.
- Hu retina failed as a hippocampal-cleft sensor.
- 0.3 pM as Ames or tissue LOD.
- In vivo glutamate aptamer sensing.
- Abrantes millimolar ELONA Kd (not in the ledger).
- Overnight T1 as this mission’s result.
- Either S066 ACV leg as identified glutamate (including Hu’s baseline-rise “successful detection” sentence). Glu as MEASURED analyte of the tissue current.
- Thesis E as a finding that the designated ephys cross-check “disconfirms” glutamate.
- Tissue ACV “uncalibratable in principle” rather than: cannot invert from the two reported buffer calibrations.
- Occupancy-at-basal, 81-versus-44000 as flagship, Nyquist/sampling-clock as Hu GCL spec, dual-pole working-range bars, scale-map as title, THE basal spec, C_eq as tissue [Glu], GluOx LOD bake-off, filled C007, or C032 as measured PaC Asp/Gln/GABA.
- Ch. 7 “reliably resolve steady-state differences in extracellular Glu concentration” as a licensed / MEASURED reading of Fig. 6.13.
- Spike maps = Leg A = Leg B, or Leg A and Leg B as two equally designed tissue Glu assays.
- Ames `%gain` map as a Glu-free ionic twin of PBS (Appendix II already lists Glu/Gln/Asp as g/l; molarity unconverted).
- Recovering θ from either printed `%gain` law; using slope ratio `57.11/11.86` as occupancy or identity; `57.11 ≈ 57.6` Langmuir-max as identity.
- Collapsing Fig. 6.12 (insertion peak drop) with Fig. 6.16B (1 kHz Z after cleaning).
- Calling reversible on–off–on a simple artefact.
- “Validation chain is the contribution” or a loaded-bottle retitle. Contribution remains this construct’s evidence boundary.

## Supporting panels (titles retired)

- **C (runner-up):** ultrasensitive working-range ceilings miss Herman ~25 nM from above (Wu glu1 top 1 nM; Abrantes preprint 10 pM). Hu **32 pM is a PBS LOD** (C004); **51.5 pM is the 50% serum LOD**. Neither is vanity; 32 pM is not the matrix-matched serum number.
- **B:** construct × quantity key. Empty glutamate kon/koff cells stay empty. Non-transfer is hygiene, not a physical law. A dopamine near-match in Hu’s Langmuir–Freundlich panel is recorded in Mission 1 dossiers and is **not** a `claims.csv` row.
- **A:** same-oligo four-grade teaching table. “Fit for purpose” is not a title.

## Highest-value next step

If the locked question is retinal tissue identity, the highest-information next experiment is unknown 2: pharmacology plus scrambled/binding-null on **both** ACV legs, same shank and room-light protocol. Do not substitute rates for identity if the claim is U2. An optional existing-trace split of Fig. 6.13 (late light-on vs off vs return) does not name the analyte.

If a human locks construct fitness, unknown 1: paired solution `Kd_molecular` and surface ACV apparent Kd of Hu’s exact Fc-thiol 39-mer in one justified buffer; include a binding-null point mutant in both arms and L-glutamine/L-aspartate controls at concentrations justified for the intended medium; fit Langmuir and Langmuir–Freundlich; report *n* with uncertainty, coverage, and complete interface chemistry.

Do not blend them. The course cannot pipette either. Mission 2 science freeze is **FREEZE** at **REVISE**; 85+ is still not honest on public evidence while U2 is empty.

## Historical note

Unrevised Candidate D claimed current devices “fail the slow problem on occupancy.” That occupancy half lacked primary evidence (1:1 overlay of an LF EC50 from a different device, plus gold-confounded Probe 3). Mission 1 closure **withdraws occupancy-as-finding**. The clocks half, the two-regime framing, the 81-fold identity as supporting biochemistry, and the empty kon/koff cell remain. The 81-fold-versus-44,000-fold comparison is no longer the flagship. Mission 2 froze QUANTITATIVE FLAGSHIP: **NONE**.
