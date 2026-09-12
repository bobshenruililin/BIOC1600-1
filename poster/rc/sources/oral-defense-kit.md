---
cursor:
  subagentId: "bc-b3984a05-2f1c-592c-a1db-2b9874fd3aaf"
---

# Mission 3 oral-defense kit

Architecture-independent. Not a poster layout. Does not choose among Mission 3 board architectures.

**Q3 aligned to freeze ledgers** (`internal/mission3/prototypes/hybrid-provenance.md` §2). Same-shank spikes are physiology on the shank, not a chemical ID of the faradaic current. Untraced directional copy (ACV `%gain` higher in dark; ON-pathway rates / Hz) dropped. Placement (large ACV disk vs small ephys) stays.

**Also aligned (communication only, after fidfix oral PASS / clocks SURVIVE):** Leg A is a **time comparison** (earlier vs later windows; settling untested), not a cartoon **rise**. Q8 selected picture is the **caption-only** B2 clocks card (14 s / ~1 min / 10 min). Do not select `protocol_clocks.svg` (1.2 ms lives there).

**Status.** Internal evaluation artifact. **Not FINAL. Not submission-ready. Not print-approved. Not externally approved.** Do not invoke Astra. Do not manufacture PASS. Not group-final.

**Governs this file:** `docs/mission3-constitution.md` (store). Science authority: `main` @ `3fa11240c85df9ebac58dcc6879494911968f75c`. Mission 3 may change how the freeze is taught. It may not change the freeze.

**Frozen object.** Hu measured retinal ACV signal-gain and interpreted it as glutamate, but the tissue experiment did not independently establish the analyte’s chemical identity.

**Locks.** Thesis D_revised (`state/current_thesis.md`). Gate **REVISE**. QUANTITATIVE FLAGSHIP **NONE** (intentional conclusion, not unfinished homework). Highest-information experiment **U2**. `MISSION2_85_HONEST` false. `group_final` false. READY FOR MISSION 3 true. Do not reopen Mission 2.

**Stamps to speak.** MEASURED / INFERRED / MODELED / UNKNOWN / PROPOSED.

**Locked question.** What does Hu’s retinal ACV result establish, and what does it not?

Sources (read only): `state/current_thesis.md`, `state/high_value_unknowns.md`, `reports/mission3_entry.md`, `poster/storyboards/mission3.md`, `analysis/accepted/figures/` captions, `poster/figures/mission3_boundary_glyph.CAPTION.md`.

---

## 10-second gist

Hu measured two retinal ACV signal-gain legs on a glutamate-aptamer shank and inferred glutamate. The tissue experiment did not chemically name the analyte. That naming experiment is locked U2, and it has not been run.

---

## 90-second spoken answer

**Prompt:** “What did Hu measure, and what would stop you calling it glutamate?”

Hu’s Ø 25 µm Fc-thiol 39-mer, in isolated mouse retina — not in vivo, not the journal AuED-MEA paper — **MEASURED** ACV signal-gain on two tissue legs with **unequal independent variables**, both referenced to a post-insertion baseline. Leg A compares current across earlier and later windows with light held on; the independent variable is **time**; settling is untested and is not the finding. Leg B is a later room-light on–off–on; the independent variable is **illumination**. Those are not two equally designed glutamate assays. The clocks that were actually run are 14 seconds per ACV scan and about one minute per point. Room lights, not the 500-millisecond LED vitality protocol.

The authors **INFER** both legs as glutamate, including the first-arm “successful detection of Glu” sentence. Chemical identity stays **UNKNOWN** on both. Printed spiked-buffer PBS and Ames percent-gain maps cannot invert tissue ACV to concentration or occupancy. Same-shank spikes are physiology on the shank, not a chemical ID of the faradaic current. Rapid-transient readiness is unmeasured: glutamate `kon`/`koff` is empty.

What would stop us calling it glutamate is the locked falsifier, **U2**: pharmacology plus a scrambled or binding-null probe on **both** ACV legs, same shank, same room-light protocol, including Leg A’s post-insertion baseline. If those arms **leave the currents intact**, reading those currents as glutamate occupancy is falsified. Do not substitute firing rates, a late-only split of Fig. 6.13, or a paired solution isotherm for that identity test. The course cannot pipette U2, so the gate stays REVISE, flagship none, not group-final.

---

## ~3-minute spoken presentation

Architecture-independent. Do not pin this script to a six-panel board.

**Minute 0–1 — the object.** The construct is Hu’s Ø 25 µm Fc-thiol 39-mer on a parylene-C shank in **in vitro** isolated mouse retina (S066), not the AuED-MEA journal paper, not in vivo. What was **MEASURED** is ACV signal-gain referenced to a post-insertion baseline, on two legs with unequal independent variables. Leg A: current compared across earlier/later windows; IV is time; light held on; settling untested. Leg B: later room-light on–off–on; IV is illumination. Clocks actually run: 14 s per ACV scan, about 1 min per point (caption-only; not `protocol_clocks.svg`). Authors **INFER** both as glutamate. Identity is **UNKNOWN** until U2. Contribution is this construct’s evidence boundary, not a validation-chain slogan and not “the sensor failed.”

**Minute 1–2 — what does not name the current.** Printed PBS 11.86 %/decade and Ames 57.11 %/decade maps are MEASURED in buffer. Tissue ACV is a third, unprinted transfer. Insertion changes the interface. Ames blank noise is 41.6%. Those maps cannot invert tissue ACV to [Glu] or occupancy θ. Same-shank spikes are physiology on the shank, not a chemical ID of the faradaic current. The ACV electrode is the large bottom disk at the GCL/IPL border; spike sites are the small ephys contacts. Photoreceptor-terminal pool stays UNKNOWN. Ch. 7 “reliably resolve steady-state extracellular Glu” is not a licensed MEASURED reading of Fig. 6.13.

**Minute 2–3 — quantity splits, then U2.** 1.8 nM is AuED-MEA Langmuir–Freundlich apparent Kd in PBS, stored as `EC50`, not the PaC molecular Kd. 12 µM is Wu’s 1d04 abstract Kd and a methods citation, not a Hu remeasurement. Occupancy on the retinal probe is unmeasured. Herman ~25 nM is acute hippocampal slice; Clements ~1.1 mM / 1.2 ms is a kinetic inference at cultured hippocampal synapses — not a retinal range, not a device spec. Glutamate `kon`/`koff` is empty; missing `koff` does not prove slowness; 14 s is a protocol clock, not Nyquist and not `koff`. QUANTITATIVE FLAGSHIP is NONE as occupancy/Kd/LOD/tissue-[Glu] title. Selected clocks picture is caption-only (14 s / ~1 min / 10 min), not `protocol_clocks.svg`. Locked next experiment is **U2** (identity of both legs), not **U1** (construct/interface fitness). Gate stays REVISE because U2 is empty.

---

## Twelve hostile Q&As

Answers are freeze-faithful. Do not add numbers or citations that are not already in the freeze files.

### 1. Hu already wrote “successful detection of Glu.” Why isn’t that measured glutamate?

That sentence is the authors’ **INFERENCE** on Leg A’s post-insertion **time comparison** (current changed; settling untested), not a pharmacological identification. Claim 5 is MEASURED as ACV signal-gain; analyte identity is `unresolved` on both legs. Glu is MEASURED only where Glu was the spiked independent variable. Do not speak either S066 tissue leg as identified glutamate. Do not speak a cartoon **rise** as the IV.

### 2. Probes 1–2 modulate with room light and the authors report *p* < 0.05. Isn’t that glutamate?

Light-correlated ACV is MEASURED. Identity is still INFERRED. Probes 1–2 authors *p* < 0.05; Probes 3–4 ns. Reversible on–off–on is not licensed as a simple artefact, and it is also not a chemical ID. Unequal IVs are what was varied. Without U2, neither leg is identified glutamate.

### 3. There are spike recordings on the same shank. Doesn’t that confirm the chemistry?

No. Same-shank spikes are physiology on the shank, not a chemical ID of the faradaic current. The glutamate-aptamer ACV electrode is the large bottom disk at the GCL/IPL border; spike sites are the small ephys contacts. Whether that ACV site matches a photoreceptor-terminal narrative stays UNKNOWN. Do not collapse ephys = Leg A = Leg B. Thesis E is not a finding that ephys “disconfirms” glutamate.

### 4. You have PBS 11.86 %/decade and Ames 57.11 %/decade. Why not invert tissue ACV?

Those maps are MEASURED in **buffer**. Tissue ACV is a third, unprinted transfer. Insertion changes the interface. Printed spiked-buffer `%gain` maps cannot invert tissue ACV to [Glu] or θ. Ames blank noise is 41.6%. No absolute tissue concentration is claimed. Do not recover θ from either printed `%gain` law; do not use slope ratio `57.11/11.86` as occupancy or identity. The honest bound is “cannot invert from the two reported buffer calibrations,” not “uncalibratable in principle.”

### 5. Hu’s Kd is 1.8 nM, so at Herman 25 nM the probe is ~93% occupied. Isn’t that the result?

1.8 nM is an AuED-MEA Langmuir–Freundlich **apparent electrochemical fit in PBS**, stored as `EC50` (C005). It is not the PaC probe’s molecular `Kd`. Occupancy on the retinal PaC probe in Ames/tissue is **unmeasured**. A 1:1 overlay θ(25 nM) ≈ 0.93 on 1.8 nM is a `computational illustration` of advertised numbers, not tissue occupancy. 12 µM is Wu’s 1d04 abstract `Kd_molecular` and, separately, a Wu citation in Hu’s methods — not a Hu remeasurement. Do not transfer parent to truncate, solution to surface, PBS to Ames, or MEA to PaC.

### 6. Why lock U2 instead of measuring the 39-mer’s real Kd first?

U1 answers construct/interface fitness: paired solution `Kd_molecular` and surface ACV apparent Kd of the exact Fc-thiol 39-mer, with a binding-null point mutant and L-glutamine/L-aspartate controls. It **cannot** establish what produced the retinal current. The locked question is identity of the tissue ACV. See the U2 vs U1 lock below. Do not blend U1 into the locked next experiment.

### 7. There is no glutamate `koff`, so the aptamer is too slow for synapses.

C007 is empty in the inspected set. Missing `koff` does **not** prove slow kinetics. τ_eq = 1/(kon·*c* + koff) can be short at millimolar *c* even when t_off is long (`computational illustration`). Do not quote koff ≈ 1/1.2 ms. Do not fill C007 from tobramycin IPA (C008) or Ding ITC (C010). Interrogation time (IPA 2 ms; ACV 14 s) is not binding `koff`. Millisecond cleft reporting is **untested, not disproven**. Authors interpret the retinal current as basal/sustained extracellular glutamate, not synaptic transients.

### 8. 14 s scans versus a 1.2 ms waveform — that’s Nyquist. The device cannot keep up.

14 s / ~1 min are MEASURED **protocol clocks**. 1.2 ms is Clements’ **INFERENCE** at cultured hippocampal synapses, a different preparation. PR #24 is a Mission-2 analysis **candidate**, not an accepted result. Do not call this “Nyquist” unless a formal signal model, bandwidth, sampling operator, and reconstruction claim are defended. Do not speak sampling-clock as Hu’s GCL spec. Selected picture is the **caption-only** B2 clocks card (14 s / ~1 min / 10 min plateau). Do **not** select `protocol_clocks.svg` — 1.2 ms is parked there. Identity still UNKNOWN.

### 9. Biology is 25 nM basal and 1.1 mM / 1.2 ms transients. Your sensor must cover that range.

Herman ~25 nM is MEASURED ambient glutamate in **acute hippocampal slice** (two components: transients on a low baseline — not three occupancy windows). Clements ~1.1 mM / 1.2 ms is an **INFERENCE** at **cultured hippocampal synapses**. Different hippocampal preparations. Not a retinal concentration range. Not a specification for Hu’s PaC probe. Not a license to call retina a failed hippocampal-cleft sensor. QUANTITATIVE FLAGSHIP is **NONE** as occupancy / Kd / LOD / tissue-[Glu] title. Do not restore 81-versus-44,000 as flagship.

### 10. Chapter 7 says the probe reliably resolves steady-state extracellular Glu. Why not put that on the board?

That Ch. 7 sentence is **not** a licensed MEASURED reading of Fig. 6.13. Boxes include all points; first-arm IQR is the variance reason for the **initial** light-on bin, not a finding that “Fig. 6.13 is not steady-state.” Whether a late-only rebin keeps *p* < 0.05 stays UNKNOWN. A late-only split names no analyte.

### 11. Ames lists Glu, Gln, and Asp. Isn’t the tissue current just medium?

Appendix II lists Glu/Gln/Asp as printed g/l; molarity is unconverted. Ames is not a Glu-free ionic twin of PBS and is **not** a demonstrated Ames confounder. Ames-loaded wording stays dropped. The selectivity panel (C032) is 100 nM Glu versus 10 µM serotonin, dopamine, tyrosine, lactate; Asp/Gln/GABA are absent. That empty panel is a named open figure of merit, not a fifth title, not a measured PaC Asp/Gln/GABA `%gain` ratio.

### 12. Probe 3 looks saturated. Occupancy-at-basal is the finding. Why is flagship NONE?

Probe 3/4 failed. Fig. 6.16A attributes failure to detached gold nanostructure, which can **mimic** early saturation; occupancy reading `unresolved`. Fig. 6.16A (gold loss) and Fig. 6.16B (1 kHz Z after cleaning) are distinct; do not collapse Fig. 6.12 (insertion peak drop) with Fig. 6.16B. Probes 1–2 still modulate with light: remaining dynamic range at whatever the retinal basal actually is, not a saturation measurement. Flagship NONE is an **accepted** Mission-2 result, not unfinished homework. Gate stays REVISE because U2 is empty; 85+ is still not honest on public evidence.

---

## Weakest answers (practice, not a layout vote)

These are the four answers first-years drop first. If a later poster makes any of them harder to say, that is a poster problem, not a science reopen.

1. **Q1 / Q2 identity.** Light-correlated ACV and Hu’s “successful detection” sentence are easy to recite as MEASURED glutamate. Speak MEASURED signal-gain, INFERRED Glu, UNKNOWN identity, every time.
2. **Q4 inversion.** “Cannot invert from the two printed buffer maps” is the freeze. “Uncalibratable in principle” is forbidden.
3. **Q5 occupancy.** θ(25 nM)≈0.93 is advertised-number math on a different device’s LF EC50. One spoken “so it’s saturated at basal” fails the oral.
4. **Q6 / Q7 substitutes.** U1 isotherms and empty `koff` do not name the retinal current. U2 is the identity test; C007 stays empty.

---

## Must not speak

If a sentence would say any of the following as a **result**, stop.

- Either S066 ACV leg as identified glutamate, including Hu’s “successful detection” sentence spoken as MEASURED Glu. Glu as MEASURED analyte of the tissue current. A cartoon **rise** as Leg A’s independent variable.
- In vivo glutamate aptamer sensing. S066 is in vitro isolated mouse retina, not S002.
- Herman 25 nM and Clements 1.1 mM as this retina experiment’s concentration range; extrasynaptic-only 25 nM; the Herman-to-Clements arithmetic as a settled span for a surface electrode.
- Hu 1.8 nM as the retinal probe’s molecular Kd, or θ(25 nM)≈0.93 as measured tissue occupancy.
- 12 µM as Hu’s measured 39-mer Kd (it is Wu 1d04 abstract / a methods citation).
- 0.3 pM as Ames or tissue LOD (it is PaC PBS blank+3 RSD; lowest calibrant 1 nM).
- 32 pM as the matrix-matched serum LOD (32 pM is PBS; 51.5 pM is 50% serum).
- Herman NMDAR EC50 1.8 **µM** as Hu’s 1.8 **nM**.
- Missing `koff` proves slow kinetics, or koff ≈ 1/1.2 ms. Filling C007 from other ligands.
- Hu retina failed as a hippocampal-cleft sensor.
- PR #24 as an accepted analysis, or “Nyquist” as a formal theorem without its signal assumptions.
- Ch. 7 “reliably resolve steady-state differences in extracellular Glu concentration” as MEASURED Fig. 6.13.
- Ephys spike-rate panels = Leg A = Leg B, or printed `%gain` maps = Leg A = Leg B, or Leg A and Leg B as two equally designed tissue Glu assays.
- ACV `%gain` higher in dark; ON-pathway rates / Hz (untraced; not freeze-ledger copy). Same-shank spikes name the faradaic current.
- Thesis E as a finding that ephys “disconfirms” glutamate.
- Tissue ACV “uncalibratable in principle.”
- Recovering θ from either printed `%gain` law; slope ratio `57.11/11.86` as occupancy or identity; `57.11 ≈ 57.6` Langmuir-max as identity.
- Ames as a Glu-free ionic twin of PBS, or Ames as a demonstrated confounder.
- Collapsing Fig. 6.12 with Fig. 6.16B. Calling reversible on–off–on a simple artefact.
- Occupancy-at-basal as a finding; 81-versus-44000 as flagship; dual-pole working-range bars; scale-map as title; THE basal spec; C_eq as tissue [Glu]; GluOx LOD bake-off; C032 as measured PaC Asp/Gln/GABA.
- Abrantes millimolar ELONA Kd (not in the ledger).
- Overnight T1 as this mission’s result. “Validation chain is the contribution” or a loaded-bottle retitle. Slogan “quality is not a single number” as the experiment.
- Docking or a predicted structure as proof of affinity or selectivity.
- Quantity collapse: LOD ≠ Kd ≠ occupancy ≠ `koff` ≠ `%gain` ≠ interrogation time.
- Gate PASS, group-final, FINAL, submission-ready, print-approved, or Astra-approved.

---

## Allowed existing figures

Use only files that already exist. Do not invent Fig. 6.13 pixels. Do not reopen rejected-as-flagship branches (sampling-clock, LF-*n*, working-range) as Mission 3 titles. Flagship NONE does not prohibit these supporting pictures.

**Mission 3 selected clocks picture:** caption-only B2 card (14 s / ~1 min / 10 min). `protocol_clocks.svg` is **not** selected — 1.2 ms is parked on that file (fidelity F2).

| Path | May claim | Must not claim |
| --- | --- | --- |
| Caption-only B2 clocks card | **Selected** Mission 3 clocks picture. MEASURED protocol times 14 s / ~1 min / 10 min plateau. Not a current ID. Not Nyquist. | 1.2 ms tick; Nyquist; synaptic-speed verdict; Leg A/B; `protocol_clocks.svg` as the pointed file |
| `analysis/accepted/figures/protocol_clocks.svg` | **Parked / not selected.** Ledgered protocol times versus 1.2 ms INFERENCE (E033). Identity remains UNKNOWN. | Pointing at this file in the oral; Nyquist; t_off; kon; tissue [Glu]; identified glutamate; a Hu GCL device spec; filling C007. |
| `analysis/accepted/figures/two_regime_clocks.svg` | Supporting cartoon. Left: MEASURED ACV signal-gain clocks on S066 probe calibration (10 nM step, ~10 min plateau), Ames calibration (41.6% blank noise), and in vitro retina (14 s / ~1 min). Names Leg A (time; light on) and Leg B (illumination). Right: rapid transients UNKNOWN. PROPOSED: U2 on both legs. Calibration clocks ≠ tissue-recording clocks. | Identified glutamate; Fig. 6.13 pixels; missing koff as proof of slowness; occupancy/Kd/LOD/tissue-[Glu] as flagship. |
| `analysis/accepted/figures/span_identity.svg` | Supporting. MODELED 1:1 Langmuir 10–90% span is exactly 81-fold, independent of Kd. Herman ~25 nM MEASURED in acute hippocampal slice. Clements ~1.1 mM INFERENCE at cultured hippocampal synapses. PaC occupancy UNKNOWN. | 81-versus-44,000 as flagship; Herman/Clements as a retinal or device span; 1.8 nM as tissue occupancy; Hu’s fitted working range (LF *n* unpublished; 10–90% on that isotherm would be 81^(1/*n*), not 81). |
| `analysis/accepted/figures/atlas.svg` | Supporting construct × quantity grid from a selected subset of `core_evidence.csv`. Green cells copy selected ledger numbers. Glutamate kon/koff stay empty. 32 pM is PBS (E005); 51.5 pM is 50% serum (E006); 0.3 pM is PaC PBS (E043), not Ames. Cleft 1.2 ms is stored under response_time as kinetic inference. | Heatmap of affinity; treating grey em-dashes as all genuine empties (some are curated omissions); transferring a number across construct/matrix/quantity type. |
| `poster/figures/mission3_boundary_glyph.svg` | CONCEPTUAL glyph. No data pixels. Two unequal-IV legs; both MEASURED as ACV `%gain` vs post-insertion baseline; both INFERRED as glutamate; identity UNKNOWN until U2. Buffer maps cannot invert tissue ACV; same-shank spikes do not name the current; GCL/IPL-border vs photoreceptor pool UNKNOWN. | Fig. 6.13 traces; inverted [Glu]; occupancy; a pharmacological ID that was not done. |
| `analysis/accepted/figures/occupancy.svg` | DEMOTED. MODELED 1:1 Langmuir overlay of **advertised** numbers. Vertical lines are hippocampal literature examples. Hu 1.8 nM is AuED-MEA LF apparent Kd in PBS. LOD is not occupancy. | Tissue occupancy; PaC Kd; occupancy-at-basal as a finding; flagship title. Prefer not to show unless the SIMULATION stamp is spoken first. |
| `analysis/accepted/figures/sensitivity.svg` | Supporting BOUND/SIMULATION: t_off vs assumed kon. Orange band = Ding ITC (C010); purple = tobramycin IPA (C008). Those rates are **not glutamate**. Caption: if they applied, even 12 µM t_off is seconds, not 0.8 ms; rising-edge τ_eq at 1.1 mM can still be milliseconds. | Glutamate kon/koff; proof that the 39-mer is slow; koff ≈ 1/1.2 ms. |
| `analysis/accepted/figures/clocks.svg` | Supporting omnibus log-time axis only if **labeled**. Cleft τ is inference. t_off values are diffusion-limited BOUNDS, not measured glutamate koff. Hu 15 min and Xiao 200 s are protocol times. GlutOx 500 ms is an enzyme comparator, not an aptamer. | Unlabeled use; Nyquist; aptamer koff; “our LOD beats GluOx.” Prefer `protocol_clocks.svg` over this file. |

Rebuild (do not hand-edit SVGs): `sh analysis/accepted/rebuild.sh`.

Captions: `analysis/accepted/figures/occupancy.CAPTION.md` (also carries `two_regime_clocks`; there is no separate `two_regime.CAPTION.md`), `analysis/accepted/figures/atlas.CAPTION.md`, `poster/figures/mission3_boundary_glyph.CAPTION.md`.

---

## U2 vs U1 (one paragraph; locked)

**U2 is locked** because it is the experiment that tests the identity inference: pharmacology plus scrambled/binding-null on **both** ACV legs, same shank and room-light protocol, including Leg A’s post-insertion baseline. If those arms leave the currents intact, reading the currents as glutamate occupancy is falsified; rates, a late-only split of Fig. 6.13, and same-shank ephys do not substitute. **U1** is paired solution `Kd_molecular` and surface ACV apparent Kd of Hu’s exact Fc-thiol 39-mer, with a binding-null point mutant and L-glutamine/L-aspartate controls — construct/interface fitness, including whether the 1.8 nM MEA number is affinity or transduction. U1 cannot name what produced the retinal current. Do not blend U1 into the locked next experiment. The course cannot pipette U2; that is why the gate stays REVISE and 85+ remains unreached on public evidence, not a reason to promote occupancy, Kd, LOD, or tissue-[Glu] as flagship.

---

## Inference boundary (speak, then stop)

**Measured.** Two S066 ACV signal-gain legs with unequal IVs, post-insertion baseline, 14 s / ~1 min clocks, GCL/IPL-border bottom electrode, Ames 41.6% blank noise, buffer calibrations, Herman ~25 nM in acute hippocampal slice, empty glutamate kon/koff search, empty Asp/Gln/GABA panel.

**Inferred, not claimed here.** That either tissue leg is chemically glutamate. That 25 nM is retinal [Glu]. That 1.8 nM overlay is tissue occupancy. That `%gain` ∝ θ. That missing koff means the oligo cannot follow a millimolar rising edge.

**Unknown until U2.** Chemical identity of both tissue ACV legs.

QUANTITATIVE FLAGSHIP: **NONE**. Gate: **REVISE**. Not group-final. Not FINAL. Not submission-ready.
