# Goal Wave A — analysis tournament proposals

Not a finished poster. Not an implementation. Not group-final.

Lane: propose flagship computational/figure candidates that could **change** the scientific story, not decorate a slogan. Docking is a rejected foil. InstructNA-scale GPU training is out of scope.

Context this worker used (already in-tree): Mission 1 science-story gate = **REVISE**; recommended title is revised D (two biological regimes; occupancy-at-basal withdrawn as a finding; S066 clocks remain primary). Overnight T1 is not this mission’s result. Round 4 already implemented an evidence atlas and a 1:1 occupancy / empirical-kon sensitivity bundle. Those remain useful supporting glyphs. They are **not** re-nominated as the next flagship.

Scoring: locked analysis rubric in `.cursor/rules/scoring-rubric.mdc`, eight criteria, 0–10 each, max 80. Higher is better on every column. `required assumptions` is high when the analysis needs few dangerous assumptions (Round 4 convention: atlas 9, occupancy ODE 6). `risk of misleading interpretation` is high when the figure is hard to over-read. Totals from `python3 scripts/score_analyses.py`.

---

## How this wave differs from Round 4

Round 4 families (P1 occupancy/kinetics, P2 atlas, P3 construct audit, P4 omnibus time ladder, P5 FASTAptamer toy, P6 AI caution) answered “show the ledger honestly” and “can a diffusion-limit kon invert T5.” Mission 1 then **demoted** the occupancy half: Hu 1.8 nM is a Langmuir–Freundlich electrochemical EC50 on an AuED-MEA chip, not a 1:1 tissue Kd of the parylene-C probe; Probe 3 is gold-confounded; Herman/Clements are hippocampal transfers onto a retina experiment.

A next flagship has to be able to do at least one of:

1. Decide C vs revised D once occupancy-at-basal is no longer treated as measured.
2. Test whether the 81-fold 1:1 identity still governs **this** sensor’s isotherm.
3. Separate interrogation/sampling clocks from missing `kon`/`koff`.
4. Test “2D confinement” as an explanation of the 12 µM → 1.8 nM jump against documented E-AB interface effect sizes.
5. Challenge the free-glutamate millisecond spec itself (framing challenger).

Re-plotting `occupancy.svg` with the same 1:1 overlay of 1.8 nM would not change anyone’s mind. It would re-commit the defect Opus named.

---

## Scoring convention and tiny smoke checks

No analysis was implemented. Arithmetic below is **computational illustration** on already-tagged ledger numbers, plus three free-route feasibility lookups. No new `state/claims.csv` rows. No PDFs committed.

| Check | Route this session | Result | Use |
| --- | --- | --- | --- |
| Does S002 report Langmuir–Freundlich exponent *n*? | OA HTML/text of Hu 2025 *Biosens. Bioelectron.* DOI 10.1016/j.bios.2025.117992, §3.2 | LF is named; Ricci 2016 is cited; apparent Kd values 2.7 nM (ST), 1.8 nM (Glu), 49.6 µM (DA) are stated; **n is not stated** in the fit paragraph | A1 must scan *n* as a labeled hypothetical axis, never as Hu’s *n* |
| White 2008 packing-density apparent Kd | PMC2674396 HTML (S033, already core) | Fig. 3 caption numbers match E029: 327±64, 101±8, 127±35 µM vs cited solution ~100 µM | A5 uses E029 only |
| White 2008 SAM-thickness apparent Kd | same PMC HTML, later figure | 95±15, 86±5, 18±5 µM for C6/C3/C2 SAMs | **not in the ledger** — extract before plotting; do not treat as a claim yet |
| Moussawi 2011 tonic span | PMC3254064 HTML (S051, status `relevant`, not `core`) | Review states tonic extrasynaptic estimates range 0.02–30 µM, splitting slice electrophysiology 0.02–0.1 µM vs in vivo dialysis/voltammetry 1–30 µM | Sensitivity overlay only; do not promote S051 to `core` in this lane |
| Ames A1420 L-glutamine | public Sigma-Aldrich/Merck product components | 0.073 g/L L-glutamine | Arithmetic allowed; Hu Appendix II was **not** re-read as A1420 |

Labeled identities used as illustration, not new measurements:

- Herman 25 nM → Clements 1.1 mM is **44,000-fold** (C012, C011).
- 1:1 10–90% span is **81-fold** (C027). For Hill/LF occupancy θ = *c*^n / (*K*^n + *c*^n), 10–90% span is **81^(1/n)**. Covering 44,000-fold on that form would require *n* ≈ **0.41**. At *n* = 0.5 the span is 6,561-fold, still short of 44,000.
- 1:1 θ(25 nM) is **0.933** if Kd = 1.8 nM and **0.0021** if Kd = 12 µM (existing occupancy table; SIMULATION).
- Advertised 12 µM / 1.8 nM is a **6,667-fold** jump. White packing-density apparent Kds in E029 differ by **~3-fold** (327/101).
- 14 s / 1.2 ms = **11,667**; 60 s / 1.2 ms = **50,000** (C031 vs C011). This is a clock ratio, not a koff.
- 0.073 g/L L-glutamine / 146.14 g mol⁻¹ ≈ **0.50 mM**. Versus Ames Glu window 10 nM–10 µM (C030): stoichiometric excess **~50,000-fold to ~50-fold**. Excess is not an interference measurement.
- Thesis 0.3 pM LOD sits **~3,300-fold** below the 1 nM lowest PBS calibrant (C029/E043). MEA 32 pM is **~3-fold** below the 0.1 nM lowest PBS calibrant (C004/E007).

---

## A1. Langmuir–Freundlich *n*-span identity

**Question.** Mission 1’s load-bearing computation is “one 1:1 Langmuir site spans 81-fold; biology spans ~44,000-fold.” Hu fitted Langmuir–Freundlich, and *n* is unpublished. For which *n* would a single heterogeneous site cover both Herman 25 nM and Clements 1.1 mM? Does “we fitted LF” secretly rescue dual-regime coverage?

**Method.** Plot 10–90% concentration span vs *n* from the Hill/LF occupancy form θ = *c*^n / (*K*^n + *c*^n). Horizontal lines at 81 (*n* = 1) and 44,000 (C011/C012 ratio). Mark *n*\* = ln(81)/ln(44,000) ≈ 0.41 as the **algebraic** covering threshold, labeled COMPUTATIONAL ILLUSTRATION. Do **not** drop a point at Hu’s *n*. Optional second panel: 10–90% windows on a log-[Glu] axis for a few labeled hypothetical *n* values, with ticks at 25 nM and 1.1 mM, **no aptamer Kd on the axis**.

**Data.** C027 (1:1 identity), C011, C012. S002 §3.2 locates that LF was used and that *n* is absent. Ricci 2016 is a 1:1 Langmuir Account, not an LF source — do not cite it as the heterogeneity model.

**What would change.** If covering both poles requires *n* ≪ 1, “LF was fitted” is **not** a free pass: D’s mismatch survives as a statement about homogeneous sites and remains the default until *n* is reported. If a later extraction found *n* near 0.4, D’s uniqueness of 81-fold as *the* argument about **this** device would weaken, and B (heterogeneous surface) would rise.

**Falsifier.** Report *n* on the AuED-MEA Glu channel, and again on the PaC probe. If *n* ≈ 1, A1 collapses to C027. If *n* is low enough that 10–90% ≥ 44,000-fold, the two-regime occupancy argument must be rewritten as a statement about isotherm shape, not about “one Kd.”

**Do not.** Overlay 81-fold on the 1.8 nM EC50. Treat signal gain as occupancy without saying Hu assumed gain ∝ bound fraction for the ST example in §3.2.

| criterion | score |
| --- | ---: |
| scientific relevance | 10 |
| required assumptions | 7 |
| availability of public data | 8 |
| ability to run without paid resources | 10 |
| reproducibility | 10 |
| visual value | 9 |
| first-year explainability | 7 |
| low misleading risk | 6 |
| **total** | **67 / 80** |

---

## A2. Occupancy verdict as a Kd-band, not a Hu overlay

**Question.** Mission 1 withdrew “θ(25 nM) ≈ 0.93 on the retina probe” because that number is a double hop (LF → 1:1, chip → probe). If advertised occupancy parameters are treated only as a **band** from 1.8 nM to 12 µM, is basal occupancy determined or undetermined?

**Method.** 1:1 θ(*c*) = *c*/(*c*+Kd) vs log Kd, or a pair of θ(*c*) curves at the two advertised endpoints, with 25 nM and 1.1 mM ticks. Shade the band. Caption: SIMULATION; 1.8 nM is AuED-MEA Langmuir–Freundlich EC50 (C005); 12 µM is Wu 1d04 abstract Kd and Hu’s citation (C001, C021), **not** a paired 39-mer solution Kd; PaC-probe apparent Kd cell stays empty.

**Data.** C001, C005, C012, C011, C021. Existing `occupancy_table.csv` already contains the two endpoint θ values.

**What would change.** If the band runs from ~0.2% to ~93% occupied at 25 nM, “saturated at basal” cannot be a finding. That is the revision that would make occupancy **support** revised D instead of contradicting the gate. It would also stop T5 from treating 1.8 nM as the occupancy Kd of the tissue device.

**Falsifier.** A measured apparent Kd of the Fc-thiol 39-mer on the PaC probe in Ames (or a paired solution+surface isotherm in one buffer). A band collapses to a point.

**Do not.** Keep the current test that asserts θ(25 nM) > 0.9 for “Hu.” That test encodes the illegal overlay.

| criterion | score |
| --- | ---: |
| scientific relevance | 9 |
| required assumptions | 6 |
| availability of public data | 9 |
| ability to run without paid resources | 10 |
| reproducibility | 10 |
| visual value | 8 |
| first-year explainability | 9 |
| low misleading risk | 5 |
| **total** | **66 / 80** |

Lower misleading score: the left edge still *looks* like “Hu is 93% occupied” unless the device and quantity type sit in the axis title.

---

## A3. Working-range bars versus biological poles

**Question.** Candidate C’s distinctive ledger observation does not need occupancy at all: some advertised analytical windows **miss Herman ~25 nM from above**. Independently, every inspected glutamate-aptamer working range except the PaC-probe **PBS** calibration (1 nM–1 mM) misses Clements 1.1 mM. If occupancy-at-basal is withdrawn, does the remaining mismatch live in **calibration ceilings**, not in θ?

**Method.** One log-[Glu] axis. Horizontal bars = reported `analytical_working_range` per construct/matrix, empty if missing. Vertical ticks: Herman ~25 nM (C012); Herman NMDAR EC50 1.8 µM (E035); Clements 1.1 mM (C011). Optional pale review band 0.02–30 µM from Moussawi PMC (S051, `relevant`, labeled review). LOD dots may be overplotted only if labeled `sensor_LOD` and not connected to range bars. Do not interpolate.

Rows that already exist:

| construct / matrix | range | source | vs 25 nM | vs 1.1 mM |
| --- | --- | --- | --- | --- |
| glu1 E-AB (abstract) | 0.01 pM–1 nM | E003 | ceiling **25-fold below** | misses |
| Abrantes NG-Apt-Glu FET (preprint abstract) | 1 aM–10 pM | E041 | ceiling **2,500-fold below** | misses |
| Xiao CNT FET, 0.1× PBS | 10 fM–100 nM | E026 | contains | ceiling 11-fold below |
| Hu AuED-MEA, PBS | 0.1 nM–10 µM | E007 | contains | ceiling 110-fold below |
| Hu PaC probe, PBS calibration | 1 nM–1 mM | E043/E044 comparator | contains | **contains** 1.1 mM |
| Hu PaC probe, Ames | 10 nM–10 µM | E044/C030 | contains | ceiling 110-fold below |

**Data.** `research/evidence/core_evidence.csv` range rows plus C012, C011, E035. Abrantes stays preprint.

**What would change.** This is the exhibit that can **swap C and D** after occupancy is demoted. If the poster’s punch is “ultrasensitive windows were optimized off the biological number the same papers cite,” C becomes the title and D’s 81-fold identity becomes a supporting derivation. If the punch is “even the windows that contain 25 nM still do not contain 1.1 mM **in the matrix used in tissue** (Ames),” D stays the title and C is Panel 2. Either outcome is a change relative to overnight T1 (“not jointly demonstrated”) and relative to T5 (kinetics inversion).

**Falsifier.** A glutamate aptamer calibration in Ames or tissue whose working range contains both a locked basal number and 1.1 mM on the **same** construct, or a decision that Clements 1.1 mM is the wrong right-hand pole for a retina electrode.

**Do not.** Bin Hu 32 pM with Wu 0.0013 pM or Abrantes 1 aM. Print 0.3 pM as an Ames/tissue LOD. Draw a third “extrasynaptic Kd” in the Moussawi band.

**LOD-estimator inset (optional, not a ninth analysis).** Thesis 0.3 pM is ~3,300-fold below the 1 nM calibrant; MEA 32 pM is ~3-fold below 0.1 nM. That is caption hygiene for any bar that also shows an LOD.

| criterion | score |
| --- | ---: |
| scientific relevance | 10 |
| required assumptions | 9 |
| availability of public data | 10 |
| ability to run without paid resources | 10 |
| reproducibility | 10 |
| visual value | 9 |
| first-year explainability | 10 |
| low misleading risk | 7 |
| **total** | **75 / 80** |

---

## A4. Interrogation Nyquist: architecture vs a 1.2 ms waveform

**Question.** The overnight fight was “aptamers too slow” vs “missing koff is not a negative result.” Hu’s own retina chapter already chose a cadence: 14 s/ACV scan, then ~1 min/point, and the authors refuse synaptic transients (C031). Can this device report the **shape** of a 1.2 ms cleft inference *even if* binding were infinitely fast?

**Method.** Two-panel figure, not the omnibus `clocks.svg` log axis.

- Panel A (primary, first-year): literature-derived Clements-like pulse (25 nM + 1.1 mM decaying with τ = 1.2 ms; labeled literature stimulus, not a new measurement) drawn on a millisecond axis, next to one 14 s ACV box and one 60 s sample. Caption: the sensor cannot reconstruct that waveform at this cadence. Authors already say this.
- Panel B (optional, still no invented kon): same pulse under a rectangular 14 s averaging window to show that **waveform identity is lost**. Do **not** convert the pulse integral into an “equivalent nM at the electrode.” A 25 µm GCL/IPL-border electrode is not a cleft. Spatial dilution is unmeasured; inventing it would be a new model, not a ledger result.

Separate glyphs by quantity type: biological τ, interrogation, sampling. Keep IPA 2 ms (C009) and GlutOx 500–800 ms (C022) off this figure or on a clearly labeled “other molecule / other class” footnote. They are methods lessons, not glutamate rates.

**Data.** C031, E045, E046, C011, C006, C028. No glutamate `kon`/`koff`.

**What would change.** If the limiting failure at the cleft is **interrogation/sampling**, then (i) missing koff no longer organizes the poster, (ii) T5’s diffusion-limit inversion becomes a side calculation about a different FoM, (iii) revised D’s clock half becomes the whole cleft column, and (iv) the highest-information kinetic experiment is no longer required to kill millisecond reporting on **this** architecture — it is required only if the group switches to IPA/fast interrogation on the same oligo.

**Falsifier.** A glutamate-aptamer recording whose sampling interval is sub-millisecond to few-millisecond **and** whose authors claim synaptic transients, or a locked decision that the biological spec is basal/graded photoreceptor glutamate rather than a 1.2 ms hippocampal cleft pulse. The second falsifier is a framing change, not a new number.

**Do not.** Caption “the aptamer is 10,000-fold too slow.” Protocol time ≠ koff (sensor-engineer review). Do not plot a 94 nM “mean-equivalent” from (1.1 mM × 1.2 ms)/14 s as if that were the concentration at the PaC electrode.

| criterion | score |
| --- | ---: |
| scientific relevance | 10 |
| required assumptions | 8 |
| availability of public data | 10 |
| ability to run without paid resources | 10 |
| reproducibility | 10 |
| visual value | 9 |
| first-year explainability | 10 |
| low misleading risk | 7 |
| **total** | **74 / 80** |

---

## A5. Documented E-AB apparent-Kd fold shifts vs the 12 µM → 1.8 nM jump

**Question.** Hu attributes the gap between cited solution Kd 12 µM and electrochemical apparent Kd 1.8 nM to 2D confinement “among others” (C026). White 2008, the ledger’s packing-density paper, moves cocaine apparent Kd by about **3-fold** across densities (E029) around a ~100 µM solution value. Is a **6,667-fold** glutamate jump inside the documented E-AB interface envelope, or is it the wrong parent construct plus the wrong quantity type?

**Method.** Bar chart of **fold change in apparent Kd**, not a new isotherm. Bars: White packing-density max/min from E029; White vs cited solution ~100 µM; Hu advertised 12 µM/1.8 nM as a **citation-to-EC50 ratio**, labeled as such. Same-paper SAM-thickness Kds (95, 86, 18 µM in PMC2674396) may be added only after extraction into `core_evidence.csv`. DA 49.6 µM vs cited 44 µM sits in S002 §3.2 OA text but is **not** a `claims.csv` row — extract before plotting; it is the in-panel counterexample Mission 1 already uses narratively.

**Data.** E029, C001, C005, C021, C018, C026. Cocaine ≠ glutamate. Transferable: **no**.

**What would change.** If documented packing-density shifts are order-unity and the Glu jump is ~10^3–10^4, B’s “confinement transformed affinity” title stays dead, and the economical reading (wrong quantity + wrong parent 1d04 vs truncated Fc-thiol surface oligo) gets a quantitative foil. If a later extraction showed E-AB apparent Kd moving by thousands-fold with packing or SAM chemistry **for a small-molecule DNA aptamer**, B would rise and the paired-isotherm experiment would be even more urgent.

**Falsifier.** Paired solution and surface Kd of the **same** 39-mer in one buffer (Mission 1 next experiment). If both land near 12 µM, 1.8 nM is transduction. If both land near 1.8 nM, confinement/selection-to-surface is a result.

**Do not.** Draw an arrow “White proves Hu’s jump is impossible.” Different molecule, different SAM, different fit family (White used hyperbolic / 1:1-like fits; Hu used LF).

| criterion | score |
| --- | ---: |
| scientific relevance | 8 |
| required assumptions | 5 |
| availability of public data | 9 |
| ability to run without paid resources | 10 |
| reproducibility | 9 |
| visual value | 8 |
| first-year explainability | 8 |
| low misleading risk | 4 |
| **total** | **61 / 80** |

---

## A6. Same PaC probe, PBS vs Ames working-range rewrite

**Question.** The only neural-tissue glutamate-aptamer experiment calibrates the **same** oligo on the **same** parylene-C probe in PBS (1 nM–1 mM linear window used for the 0.3 pM LOD) and in Ames (10 nM–10 µM, 41.6% blank noise, authors: poor quantitative SNR) (E043, E044, C029, C030). Does matrix, not sequence, already forbid the cleft pole on the device that went into retina?

**Method.** Two bars, one construct. PBS 1 nM–1 mM vs Ames 10 nM–10 µM. Ticks at 25 nM and 1.1 mM. Annotate 41.6% Ames blank noise as author-reported SNR, not as an occupancy. Empty cell: PaC apparent Kd in Ames/tissue.

**Data.** C029, C030, E043, E044, C012, C011. No property transfer from the AuED-MEA 1.8 nM.

**What would change.** A first-year can defend “the tissue buffer collapsed the ceiling 100-fold and left 1.1 mM outside the window” without mentioning Kd. That would make matrix the hidden variable inside revised D, and would make “tighter LOD in PBS” look like the wrong optimization target. Combined with A3 it is one figure; kept separate because A3’s punch can be true even if A6 were omitted, and A6 does not need Wu or Abrantes.

**Falsifier.** Ames (or retina-matched) calibration of this probe whose linear window includes 1.1 mM with usable SNR, or a locked decision that the retina task is basal-only so 10 µM is an adequate ceiling.

| criterion | score |
| --- | ---: |
| scientific relevance | 9 |
| required assumptions | 8 |
| availability of public data | 10 |
| ability to run without paid resources | 10 |
| reproducibility | 10 |
| visual value | 8 |
| first-year explainability | 9 |
| low misleading risk | 7 |
| **total** | **71 / 80** |

---

## A7. Ames glutamine stoichiometric excess (wildcard, not a title)

**Question.** W1 was correctly rejected as a fifth thesis because the exhibit is an empty selectivity cell (C032). The open FoM still matters: public Ames A1420 lists L-glutamine at 0.073 g/L. Relative to the Ames glutamate window that actually bathed the retina experiment, how large is the **stoichiometric** Gln excess, and did the selectivity panel ever challenge it?

**Method.** One bar: [Gln]_A1420 ≈ 0.50 mM (arithmetic on the vendor sheet, MW 146.14 g mol⁻¹) vs Ames Glu calibrants 10 nM–10 µM and vs the 100 nM Glu used in Fig. 6.8A. Second panel: interferent class actually tested (10 µM ST/DA/Tyr/Lac) vs missing Asp/Gln/GABA. Caption: excess ≠ cross-reactivity; Hu blamed Ames SNR on ionic strength/folding, not on a Gln experiment (W1). Vendor identity of Hu’s Ames remains `unresolved`.

**Data.** C030, C032, W1 note, public A1420 components. Do not invent Asp/Glu masses for Ames. Do not use Abrantes 1 pM Gln vs 10 aM Glu on a different in silico construct.

**What would change.** If the group accepts that a ~0.5 mM adjacent amino acid sat in the tissue buffer unchallenged, chemical identity of the strongest Glu-apt neural-tissue signal becomes a load-bearing unknown inside **every** title. That does not replace two-regime matching, but it can demote S066 from “basal glutamate was recorded” to “a light-correlated ACV change was recorded.” Pharmacological identification then outranks another LOD.

**Falsifier.** Matched Glu/Asp/Gln/GABA ACV on the Fc-thiol 39-mer in PBS and in the Ames actually used, including the documented Gln mass. A null at 0.5 mM Gln would retire this panel.

| criterion | score |
| --- | ---: |
| scientific relevance | 8 |
| required assumptions | 6 |
| availability of public data | 7 |
| ability to run without paid resources | 10 |
| reproducibility | 8 |
| visual value | 7 |
| first-year explainability | 8 |
| low misleading risk | 5 |
| **total** | **59 / 80** |

---

## A8. iGluSnFR waveform inflation as a spec challenger

**Question.** The central question treats inferred free-glutamate 1.2 ms as the thing an aptamer must “keep up with.” Armbruster 2020 reports iGluSnFR fluorescence time courses often **10–100× longer** than the extracellular lifetime of synaptically released glutamate, in part because the indicator buffers glutamate (C024). If the field’s protein gold-standard already reports a filtered waveform, is “match Clements τ” the right aptamer spec, or the wrong comparison class?

**Method.** Two traces conceptually (not new imaging): free-Glu τ (Clements, abstract inference) vs iGluSnFR waveform duration as a 10–100× band (C024). Place Hu 14 s / 1 min **off** that band, as a third class (electrochemical sampling), not as a fourth iGluSnFR. Helassa 2018 iGluu τ_off ~2 ms is S060 (`relevant`, not `core`); this worker did **not** re-inspect that PMC. Use it only if a later extractor promotes a locator.

**Data.** C024, C011, C031. Protein ≠ aptamer. Transferable: **no**.

**What would change.** This is the required framing challenge: maybe millisecond free-Glu is not a sensor spec that any indicator meets, so Topic 1 should lock a **named filtered task** (basal retina, extrasynaptic micromolar, iGluSnFR-like transients) rather than score aptamers against an inferred cleft waveform. If the group rejects that move, A8 still fences iGluSnFR as a comparator so nobody says “iGluSnFR is 2 ms therefore DNA can be too.”

**Falsifier.** A glutamate DNA-aptamer waveform validated against a glutamate optical indicator **and** against a transporter/current estimate of free Glu on the same preparation. Without that, A8 cannot promote “aptamers should be iGluSnFR-like” as a finding.

**Do not.** Dock an aptamer into iGluSnFR’s binding site. Equate fluorescence lifetime, τ_off, and ACV sampling.

| criterion | score |
| --- | ---: |
| scientific relevance | 7 |
| required assumptions | 5 |
| availability of public data | 8 |
| ability to run without paid resources | 10 |
| reproducibility | 8 |
| visual value | 8 |
| first-year explainability | 6 |
| low misleading risk | 4 |
| **total** | **56 / 80** |

---

## Rejected foils (do not implement as flagship)

| foil | why |
| --- | --- |
| Molecular docking of a glutamate aptamer | C017: docking failed theophylline/caffeine selectivity. No Glu-aptamer crystal in the ledger. Constitution: docking is hypothesis generation. Attractive poses are the failure mode P6 was written to block. |
| InstructNA-scale GPU training | Out of scope. C016 is already the wet-lab caution (many generated sequences are non-binders, and not glutamate). |
| FASTAptamer toy counts | Round 4 P5: no licensed public glutamate FASTQ to bundle; a toy table does not answer the glutamate question. |
| Re-electing `occupancy.svg` Hu 1.8 nM 1:1 overlay | Mission 1 named this as the occupancy defect. Keep the 81-fold identity **without** an aptamer number (C027). |
| Cleft-pulse “equivalent nM” at the PaC electrode | Requires an unmeasured spatial-dilution model. Would be read as a concentration. |
| Omnibus log-time ladder mixing IPA, GlutOx, thrombin, and Glu ACV | Round 4 P4; O2 already flags the collapse. A4 replaces it. |

---

## Scoreboard (this worker, one pass)

| id | rel | assum | data | unpaid | repro | visual | FY | low-mislead | total | role |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| A3 working-range vs poles | 10 | 9 | 10 | 10 | 10 | 9 | 10 | 7 | **75** | can swap C vs D |
| A4 interrogation Nyquist | 10 | 8 | 10 | 10 | 10 | 9 | 10 | 7 | **74** | can retire “too slow” |
| A6 PBS vs Ames window | 9 | 8 | 10 | 10 | 10 | 8 | 9 | 7 | **71** | matrix as hidden variable |
| A1 LF *n*-span | 10 | 7 | 8 | 10 | 10 | 9 | 7 | 6 | **67** | tests 81-fold on this sensor |
| A2 occupancy Kd-band | 9 | 6 | 9 | 10 | 10 | 8 | 9 | 5 | **66** | implements occupancy demotion |
| A5 interface fold envelope | 8 | 5 | 9 | 10 | 9 | 8 | 8 | 4 | **61** | tests confinement story |
| A7 Ames Gln excess | 8 | 6 | 7 | 10 | 8 | 7 | 8 | 5 | **59** | wildcard chemical identity |
| A8 iGluSnFR spec challenge | 7 | 5 | 8 | 10 | 8 | 8 | 6 | 4 | **56** | framing challenger |

Two independent `poster-red-team` scorers are still required before any of these totals enter `state/scoreboard.json`. These integers are one worker’s rubric pass, not a tournament result.

If a single flagship figure is wanted, A3+A6 are one two-panel plot (cross-paper bars + same-probe PBS/Ames). A4 should remain a separate panel so clocks do not collapse back onto a concentration axis.

---

## Relation to the highest-information next experiment

Mission 1’s proposed experiment — paired solution and surface isotherm of the exact Fc-thiol 39-mer in one buffer, Langmuir and Langmuir–Freundlich, report *n*, report coverage — still dominates A1, A2, and A5. It does **not** substitute for A3, A4, A6, or A7:

- A3/A6 are already constrained by reported windows; a new Kd does not put 1.1 mM inside Ames 10 µM.
- A4 is already constrained by the authors’ 14 s / 1 min cadence.
- A7 is a selectivity experiment (Glu/Asp/Gln/GABA in PBS and Ames), not an isotherm.

A glutamate `kon`/`koff` on that oligo (IPA/SPR, controlled mass transport) would replace the Round 4 sensitivity envelope and would still leave A4 standing on this ACV architecture.

---

## Top two, and why they could alter the scientific story

**1. A3 — working-range bars versus biological poles (75/80).**  
Once occupancy-at-basal is no longer a finding, the remaining quantitative mismatch in the ledger is a **window** mismatch, not a θ mismatch. Ultrasensitive glu1 and Abrantes ceilings sit below Herman ~25 nM; Hu Ames (the matrix of the retina experiment) contains 25 nM and still sits 110-fold below 1.1 mM; the same PaC probe in PBS was calibrated to 1 mM. That figure can make Candidate C the title (“the LOD contest selected the wrong window”) or lock revised D (“two regimes, and the tissue matrix already drops the fast pole”). Either way it displaces overnight T1’s joint-demonstration slogan and T5’s kinetics inversion, using only `analytical_working_range` rows and labeled biological ticks. No invented kon, no 1:1 overlay of 1.8 nM.

**2. A4 — interrogation Nyquist / two-clock retina panel (74/80).**  
This is the analysis that can end the “are aptamers too slow?” frame without measuring glutamate rates. A 14 s scan and a 1 min sample cannot reconstruct a 1.2 ms inferred cleft waveform even at infinite kon. Hu’s authors already refuse synaptic transients; the computation is to make that refusal the **cleft column** of the poster rather than a caption under a missing-koff cell. If A4 is accepted, missing koff stays an open molecular fact (C007) but stops organizing Topic 1; IPA becomes the architecture to switch to, not a tobramycin number to plot as glutamate; and the next experiment that would actually reopen millisecond reporting is a fast-interrogation construct, not another PBS LOD.

**Runner that should still be built if the flagship stays D’s 81-fold identity: A1.** It is the only proposal that can falsify “81 vs 44,000” as a claim about **Hu’s** isotherm rather than about a generic 1:1 site. It is not top-two only because *n* is unpublished, so the figure is a sensitivity axis until the paired-isotherm experiment reports it.
