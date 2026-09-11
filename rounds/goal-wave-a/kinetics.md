# Kinetics vs biological timescales

Lane report for Goal Wave A. Independent re-inspection of free literature (PubMed, PMC, Europe PMC, publisher OA HTML, RWTH OA PDFs). No nested agents. No ledger writes. No poster.

**Question.** What do published glutamate (and closely related small-molecule) aptamer `kon`/`koff`, sensor `response_time`, `measurement_time`, and `biological_concentration_range` actually say about whether an aptamer sensor can “keep up with neurochemical signaling”?

**Short answer.** Glutamate DNA aptamers still have **no reported `kon`/`koff`**. Sensor papers report protocol clocks of **minutes** (Hu Glu wait 15 min; Hu thesis 10 min plateau and ~1 min retina sampling) or **hundreds of seconds** (Xiao FET stabilize 200 s). Biology is not one clock: inferred cleft transients are **millisecond / millimolar**, extrasynaptic phasic events are **tens of milliseconds / micromolar**, and tonic/ambient glutamate is **nanomolar** by NMDAR current (Herman ~25 nM; Chiu 25.6 ± 3.2 nM in NAc) but **micromolar** by dialysis and enzyme MEAs. “Keeping up with neurochemical signaling” is **not a well-posed claim** until the compartment is named. Protein glutamate indicators that *do* report `koff` still do not report free cleft glutamate.

---

## 1. Quantity vocabulary (do not collapse)

| Object | What it is | This lane |
|---|---|---|
| `Kd_molecular` | Equilibrium dissociation constant of a named oligo–ligand pair in a named phase | 1d04 12 µM (Wu abstract); Xiao SPR 293 nM; NG-Apt-Glu ELONA 10.3–25.1 mM |
| `EC50` / apparent Kd | Half-maximal **transduced** signal; may be Langmuir–Freundlich | Hu Glu 1.8 nM on AuED-MEA |
| `kon`, `koff` | Association/dissociation rates of a named construct | **Empty for glutamate DNA aptamers** |
| `sensor_LOD` | Blank + 3SD/3RSD of a signal | Wu glu1 0.0013 pM; Hu MEA 32 pM PBS / 51.5 pM 50% serum; Xiao FET 10 fM in 0.1× PBS |
| `analytical_working_range` | Calibration span | Not occupancy 10–90% |
| `response_time` | Time for the **sensor output** to follow a concentration step | Xiao 200 s stabilize; Kumakli ATP 80–140 ms under flow; Rutherford GlutOx 500–800 ms |
| `measurement_time` | Protocol wait or interrogation duration | Hu Glu 15 min wait; ACV 14 s/scan; IPA 2 ms pulse clock |
| `biological_concentration_range` | [Glu] of a named compartment and method | Cleft peak vs extrasynaptic phasic vs ambient vs bulk dialysis |

Never: treat LOD as Kd; treat 2 ms IPA as koff; treat 15 min incubation as synaptic response; transfer solution Kd onto a surface construct; use tobramycin/ITC rates as glutamate rates.

---

## 2. Search strategy and negative-search integrity

**Queries (Europe PMC REST + PubMed/PMC HTML, 2026-09-11).**

- `(glutamate OR "glutamic acid") AND aptamer AND (kon OR koff OR "association rate" OR "dissociation rate" OR "binding kinetics")` — 229 hits; none were glutamate DNA-aptamer `kon`/`koff`. Near-misses: MIP glutamate sensors; Abrantes in silico/ELONA; Hu/Wu equilibrium and LOD papers.
- `(glutamate OR "glutamic acid") AND aptamer AND (SELEX OR electrochemical OR FET OR SPR)` — glutamate sensor papers report Kd/LOD/incubation, not rates.
- Named-paper fetches: Wu PMID 34783880; Hu DOI 10.1016/j.bios.2025.117992 and RWTH thesis 10.18154/RWTH-2025-07238; Xiao PMC12376627; Abrantes 10.1101/2025.11.05.686731; Ohsawa 10.2116/analsci.24.167; Ding PMID 38785220; Chang PMC3983011; Abeykoon PMC13101946; Santos-Cancel PMC6207073; Kumakli PMC11059485; White PMC2674396; Rousseau PMC10750225; Clements PMID 1359647; Herman PMC2670936; Chiu PMC5388241; Okubo PMC2851965; Moussawi PMC3254064; Le Meur PMC2075557; Helassa PMC6003469; Marvin PMC4469972 / PMC6394230; Aggarwal PMC10250197; Armbruster PMC7255799; Rutherford PMC3482110; Clay PMC5881573; Zheng PMC5299514; Scimemi PMC2777263.

**Blocked / partial.** Wu VoR remains closed (abstract + JuSER metadata only). Ding 2024 VoR closed (abstract only). Clements 1992 VoR closed (PubMed abstract). Herman/Rutherford/Okubo: publisher blocks PMC XML; Herman and Rutherford inspected via PMC HTML; Okubo via PMC HTML. Xiao SPR sensorgrams live in SI Fig. S6; main text gives Kd only.

**Not used.** Sci-Hub / docksci copies of Clements.

**Wildcard (not in the parent prompt).** (i) Chiu & Jahr 2017: resting extrasynaptic glutamate is also nanomolar in NAc, against a micromolar “nonsynaptic compartment” as a resting state. (ii) Natural glycine riboswitch SPR `ka` is extremely slow (Chang 2014) — an amino-acid nucleic-acid kinetic, **not glutamate DNA**. (iii) Helassa 2018: even a protein sensor with stopped-flow `koff` = 468 s⁻¹ cannot resolve free cleft glutamate.

---

## 3. Biological regimes — three (actually four) problems

These are **not** interchangeable `biological_concentration_range` numbers.

### 3.1 Synaptic cleft — phasic, millimolar, millisecond (inferred)

`primary-source-supported` — Clements, Lester, Tong, Jahr, Westbrook, *Science* 1992, PMID 1359647. **full_text_inspected: no** (abstract). Kinetic analysis of D-aminoadipate displacement from NMDARs at **cultured hippocampal synapses**. Glutamate **peaked at 1.1 mM** and **decayed with τ = 1.2 ms**. This is a **model-dependent inference**, not a chemical assay.

Helassa 2018 (PMC6003469, **full_text_inspected: yes**) restates that Clements estimate and then writes that “more recent studies using computational modeling and fluorescence anisotropy imaging in tissue suggest that it is closer to 100 μs,” citing Scimemi & Beato 2009 (PMC2777263) and Zheng et al. 2017 (PMC5299514).

- Scimemi 2009 is a **review** of methods and pitfalls of cleft-profile estimates (`review-supported` for “Clements-style estimates are approximate”). **full_text_inspected: yes** (Europe PMC HTML). It does not itself measure 100 µs.
- Zheng 2017 **measured diffusivity**, not clearance τ (`primary-source-supported` for D). Intra-cleft D/Df = **0.54 ± 0.03** at mossy-fiber–CA3 appositions; with free glutamate D ≈ 0.86 µm²/ms this points to **~0.46 µm²/ms** intra-cleft. **full_text_inspected: yes**. That is not a 100 µs lifetime.

`hypothesis` / Helassa interpretation: free cleft glutamate may be **faster than 1.2 ms**. Do not treat 100 µs as a Zheng measurement.

Moussawi et al. 2011 (PMC3254064, review, **full_text_inspected: yes**) compile cleft glutamate as **>1 mM for <10 ms**, returning to **<20 nM** between events. Compilation, not a new assay.

### 3.2 Extrasynaptic phasic — micromolar, tens of milliseconds (indicator-deconvolved)

`primary-source-supported` — Okubo et al., *PNAS* 2010, PMC2851965. **full_text_inspected: yes** (PMC HTML). Cerebellar parallel-fiber extrasynaptic imaging with L401C-EOS (`Kd` = **1.57 µM** — that is **indicator affinity**, not biological [Glu]). After deconvolution assuming first-order association, estimated extrasynaptic transients reached **micromolar concentrations for tens of milliseconds** after 2–5 pulses; average [Glu] in a **50 ms** window was **1–8 µM** depending on pulse number.

Do not transfer L401C-EOS `Kd` onto tissue concentration. The 1–8 µM figure is a **deconvolved estimate**.

### 3.3 Ambient / tonic — nanomolar by NMDAR current

`primary-source-supported` — Herman & Jahr, *J Neurosci* 2007, PMC2670936. **full_text_inspected: yes** (PMC HTML). Acute hippocampal slice; tonic NMDAR current vs nucleated-patch dose–response. Ambient glutamate **near 25 nM** after efficacy scaling (pre-scaling estimate **37.9 ± 10.8 nM**). NMDA `EC50` **37.7 µM** (nucleated patches). The paper uses **ambient/baseline**, not “extrasynaptic-only.” Contrasts microdialysis **1–4 µM**. Bath **2 µM** glutamate did not increase the standing current (uptake shields receptors). TTX vs 1 Hz Schaffer stimulation did not change the standing current (ambient is not vesicular overflow in this assay).

`primary-source-supported` — Le Meur, Galante, Angulo, Chatton, *J Physiol* 2007, PMC2075557. **full_text_inspected: yes**. Ambient glutamate of **non-synaptic origin** estimated **83–87 nM at 25 °C** from tonic NMDAR current. Still nanomolar.

`primary-source-supported` — **wildcard** Chiu & Jahr, *Cell Reports* 2017, PMC5388241. **full_text_inspected: yes**. Nucleus accumbens: standing NMDAR current equivalent to **25.6 ± 3.2 nM** glutamate (n = 19); adult rats **31.7 ± 8.7 nM** (n = 8). Title claim: extracellular glutamate is **nanomolar in both synaptic and non-synaptic compartments** at rest. Directly tests (and does not support) the Moussawi/Kalivas picture of a **micromolar resting extrasynaptic** compartment.

### 3.4 Bulk extracellular — micromolar by dialysis and enzyme electrodes (different method)

`review-supported` — Moussawi 2011; Featherstone & Shippy 2008 (PMC2322853, **full_text_inspected: yes**): microdialysis typically **1–5 µM** after recovery; some electrochemical microsensors **18–29 µM**; dialysis intervals often **≥1 min** (commonly 10–30 min).

`primary-source-supported` — Rutherford et al., *J Neurochem* 2007, PMC3482110. **full_text_inspected: yes**. **Glutamate oxidase** ceramic MEA in freely moving rats: **response_time 500–800 ms**; data in this paper recorded at **1 s** intervals; detection limit **0.2 µmol/L**. Resting Glu **7.3 ± 0.9 µmol/L** (striatum) vs **44.9 ± 4.7 µmol/L** (PFC) in freely moving animals. Enzyme comparator, **not aptamer**. These micromolar “resting” values **must not be averaged** with Herman 25 nM: different method, volume, and likely tissue disruption.

`primary-source-supported` — Clay & Monbouquette 2018, PMC5881573. **full_text_inspected: yes**. Simulated GlutOx **response_time 0.73 s**, matching experimental **0.8 ± 0.2 s**. Authors note synaptic signaling is thought to be **millisecond**, much faster than GlutOx to date.

**Inference boundary.** Nanomolar (NMDAR current, intact uptake, slice) and micromolar (dialysis / enzyme MEA / some in vivo voltammetry) are **method-defined**. A glutamate aptamer sensor cannot “match biological concentration” without naming the method and compartment.

---

## 4. Glutamate DNA aptamers: what was actually timed

### 4.1 `kon` / `koff` — empty

`unresolved` — No glutamate DNA aptamer `kon` or `koff` was found in Wu abstract, Hu 2025 VoR, Hu 2025 thesis OA text, Xiao 2025 main text, or Abrantes 2025 preprint HTML. Ohsawa 2008 explicitly says kinetic parameters **could not be estimated** (box-type SPR) and that they **did not obtain an aptamer to free glutamic acid**.

Do not substitute tobramycin IPA, Ding ITC, Chang SPR, or iGluSnFR rates.

### 4.2 Wu 2022 — two constructs, no rates

`primary-source-supported` — Wu et al., *Anal Bioanal Chem*, PMID 34783880, DOI 10.1007/s00216-021-03783-w. **full_text_inspected: partial** (PubMed/Europe PMC abstract; VoR closed; JuSER record has abstract only).

- Capture-SELEX isolate **1d04**: `Kd_molecular` **12 µM** in complex medium.
- Truncated **glu1** Fc-thiol E-AB: `sensor_LOD` **0.0013 pM**; `analytical_working_range` **0.01 pM–1 nM**; selectivity in **10-fold diluted human serum**.

These are **different constructs**. The abstract contains no incubation time, no `kon`/`koff`, no in vivo experiment. Future-tense “in vivo monitoring” is not a measurement.

### 4.3 Hu 2025 MEA — apparent Kd and a 15 min wait

`primary-source-supported` — Hu, Zhu, Figueroa-Miranda, Feng, Offenhäusser, Mayer, *Biosens Bioelectron* 2025, DOI 10.1016/j.bios.2025.117992. RWTH OA PDF. **full_text_inspected: yes**.

Construct: Fc- and thiol-modified **Glu-apt** `5′-HS-C6-GCATCAGTCCACTCGTGAGGTCGACTGATGAGGCTCGAT-Fc-3′`, cited as Wu 2022 **Kd = 12 µM** (citation, not a remeasurement).

| Quantity | Value | Locator | Type |
|---|---|---|---|
| Cited solution Kd | 12 µM | Experimental sequences | `Kd_molecular` **citation** |
| Electrochemical apparent Kd | **1.8 nM** (Langmuir–Freundlich) | §3.2 | `EC50` |
| PBS LOD | **32 pM** (blank + 3 SD) | Fig. 4h | `sensor_LOD` |
| 50% serum LOD | **51.5 pM** | §3.4 | `sensor_LOD` |
| Semi-log window | **0.1 nM–10 µM** | Fig. 4e | `analytical_working_range` |
| Glu ACV wait | **15 min** (DA 10 min) | §3.2; Fig. S8 | `measurement_time` |

Authors attribute 12 µM vs 1.8 nM to **2D confinement** among other factors. That is their interpretation (`primary-source-supported` that they contrast the numbers; `hypothesis` that confinement is the cause).

The 15 min wait is a **chosen assay incubation**, “in accordance with the optimized signal-time dependence.” It is **not** a fitted `koff`. It **cannot** be identified with a 1.2 ms cleft τ.

### 4.4 Hu 2025 thesis — 10 min plateau; retina is basal, not synaptic

`primary-source-supported` — Hu Z, RWTH dissertation, DOI 10.18154/RWTH-2025-07238. OA PDF text extract. **full_text_inspected: yes**. Same Glu-apt family. PDF not stored in git.

| Quantity | Value | Locator | Type |
|---|---|---|---|
| 10 nM Glu wait-to-plateau | **~10 min** | Fig. 6.6; §6.2 | `measurement_time` (authors: association/dissociation steady state) |
| PBS LOD | **0.3 pM** (blank + 3 RSD) | Fig. 6.7 | `sensor_LOD` |
| PBS linear window | **1 nM–1 mM** | Fig. 6.7 | `analytical_working_range` |
| Ames linear window | **10 nM–10 µM**; blank noise 41.6% | Fig. 6.9A | `analytical_working_range` |
| ACV scan | **14 s / point** | §6.3 | `measurement_time` (interrogation) |
| Retina sampling | **~1 min / point** | §6.3 | `measurement_time` (sampling interval) |

Authors (verbatim sense): electrophysiology captures millisecond spikes; electrochemical Glu is averaged over **~one minute per point** and reports **sustained basal Glu**, “rather than the fast, transient release events associated with individual synaptic activity.” Probe 3 near basal saturation; Probe 4 unstable; gold nanostructure can detach after insertion.

This is the strongest Glu-apt experiment in nervous tissue in the inspected set. It **does not** fill `kon`/`koff`. It **does** show the authors themselves refuse a synaptic-transient reading. Ames vs PBS shows **buffer composition rewrites** the working window (`transferable: no`).

### 4.5 Xiao 2025 — SPR Kd vs FET LOD vs 200 s stabilize

`primary-source-supported` — Xiao et al., *Adv Sci* 2025, PMC12376627. **full_text_inspected: yes** (main text; SI Fig. S6 not separately opened).

- SPR `Kd_molecular` glutamate aptamer **293 nM** (DA 20 nM; 5-HT 10.5 nM; HIS 15 nM). No `kon`/`koff` in the main-text SPR paragraph.
- CNT FET `sensor_LOD` **10 fM** in **0.1× PBS**. Glutamate calibration span **10 fM–100 nM** (Fig. 3f); other NTs 10 fM–100 µM.
- Multiplex real-time: 10 nM target; “sensor response **stabilized after 200 s**,” then 40 s acidic reset (Fig. 5e). `response_time` **200 s**. Reset is a **pH step**, not `koff`.

Do not transfer 293 nM SPR Kd onto 10 fM FET LOD, or 0.1× PBS onto aCSF/ECF.

### 4.6 Abrantes 2025 preprint — millimolar ELONA Kd vs attomolar FET LOD

`primary-source-supported` (preprint) — Abrantes et al., bioRxiv 10.1101/2025.11.05.686731. **full_text_inspected: yes** (HTML).

- In silico truncation of 98-nt glu1d04 to 58-nt **NG-Apt-Glu**. Docking scores are **computational illustration**.
- Inhibition ELONA `Kd_molecular` **10.3–25.1 mM**; %LOS 15.4–61.8 (Fig. 1D).
- gFET `sensor_LOD` **1 aM** in 1× aCSF; linear **1 aM–10 pM**; 24 mV/decade.
- Clinical CSF: **10 min** drop incubation (`measurement_time`). Drift test: VDIRAC every **10 s** for 1 h.

Millimolar ELONA Kd and attomolar FET LOD on related sequences are **not one affinity**. Preprint, not VoR.

### 4.7 Ohsawa 2008 — the one glutamate-adjacent SPR kinetic attempt

`primary-source-supported` — Ohsawa et al., *Anal Sci* 2008, 10.2116/analsci.24.1.167. **full_text_inspected: yes** (J-STAGE HTML/PDF).

Arginine-modified DNA vs **avidin–glutamate conjugates**, not free glutamate. Equilibrium `Kd` e.g. aptamer 2–AvD **720 ± 28 µM**; aptamer 6–AvD **810 ± 30 µM**. “Estimation of kinetic parameters … was difficult because the box-type sensorgrams … indicated that association and dissociation … were **rapid processes**.” Authors: “we could not obtain an aptamer bound to the glutamic acid.”

Rapid box-type SPR on **conjugates** is not a free-glutamate `koff`, and they state the free-amino-acid selection failed.

---

## 5. Related small-molecule aptamer kinetics (analogs, not transferable)

Use only as **method existence proofs** and as an empirical envelope that **contradicts** “diffusion-limited 12 µM unbinds in 0.8 ms.” `transferable: no`.

| Source | Construct | `kon` | `koff` | Notes |
|---|---|---|---|---|
| Abeykoon 2025 PMC13101946 **yes** | Surface tobramycin parent aptamer, IPA, tris, 12 mL/min | **3.5×10⁴ M⁻¹ s⁻¹** | **1.39 s⁻¹** | Kinetic Kd 41 ± 11 µM vs eq 46 ± 6 µM. Mass-transport caveats in text. |
| Santos-Cancel 2018 PMC6207073 **yes** | Tobramycin / ATP E-AB | not a glutamate koff | — | IPA **2 ms** is `measurement_time` (pulse clock). Apparent tobramycin Kd ~5.0 ± 0.6 µM by voltammetry in this paper — **different interrogation**, not Abeykoon. |
| Kumakli 2023 PMC11059485 **yes** | Destabilized ATP E-AB on ~500 nm microelectrodes | — | association/dissociation **80 ms** (micro) vs **140 ms** (macro) under flow | Authors: mass transport. Kd 315 µM (dendritic micro) vs 400 µM (planar) in this paper. **ATP, not Glu.** |
| Ding 2024 PMID 38785220 **no** (abstract) | Various DNA aptamers, kinetic ITC | **2×10⁵ → 96 M⁻¹ s⁻¹** as Kd 28 nM → 864 µM | **1.03×10⁻³ → 0.012 s⁻¹** | Survey endpoints, **not glutamate**, not per-construct table (VoR closed). |
| Chang 2014 PMC3983011 **yes** | Theophylline RNA SPR | **(1.5 ± 0.1)×10⁵ M⁻¹ s⁻¹** | **0.063 ± 0.004 s⁻¹** | Kinetic Kd 430 ± 40 nM vs eq 340 ± 20 nM. |
| Chang 2014 same table | Natural **glycine** riboswitch, 5 mM Mg | **28 ± 5 M⁻¹ s⁻¹** | **(5.6 ± 2.5)×10⁻³ s⁻¹** | Amino-acid RNA; at 20 mM Mg, `ka` **(7.2 ± 1.0)×10²**. Shows how slow an amino-acid nucleic acid **can** be. **Not Glu DNA.** |
| Chang 2014 same table | DNA ATP aptamer | **cannot be uniquely determined** | — | Equilibrium Kd **8.8 ± 3.0 µM** only. SPR does not always resolve small-molecule rates. |
| White 2008 PMC2674396 **yes** | Cocaine E-AB | — | equilibrates **faster than ~4 s** DPV dead time | Thrombin **11–20 min** as density rises. Immobilization is not null. **Not Glu.** |
| Rousseau 2023 PMC10750225 **yes** | Perspective | cites Chang ka 10⁴–10⁵; ATP often too fast for SPR | Langmuir **81-fold** 10–90% occupancy | Time resolution = binding + analysis time. Tobramycin ~4 s / ATP ~2 s in one cited flow study attributed to **mixing**. |

**Computational illustration only (do not quote as glutamate kinetics).** If one *illegally* transferred Ding/Abeykoon `kon` onto advertised Glu occupancy parameters, 1d04 12 µM `t_off = 1/(kon Kd)` would be **seconds**, not 0.8 ms (already tabulated in `analysis/accepted/occupancy_kinetics/tables/occupancy_table.csv`, labeled SIMULATION/BOUND). A diffusion-ceiling `kon` = 1×10⁸ M⁻¹ s⁻¹ is an **upper bound**, not a measurement. Rising-edge `τ_eq = 1/(kon c + koff)` at 1.1 mM is **not** `t_off`.

---

## 6. Protein glutamate sensors: the only literature that actually measures rates

These are **not aptamers**. They are the existence proof of what “keeping up” required in the indicator field.

`primary-source-supported` — Marvin et al. 2013, PMC4469972. **full_text_inspected: yes**. iGluSnFR on-neuron affinity **4.9 ± 1.3 µM**. That is **sensor `Kd_molecular`**, not biological [Glu].

`primary-source-supported` — Marvin et al. 2018, PMC6394230. **full_text_inspected: yes**. Original iGluSnFR “**too slow to follow fast synaptic transients**.”

`primary-source-supported` — Helassa et al. 2018, PMC6003469. **full_text_inspected: yes**. Stopped-flow at 20 °C: iGluSnFR `koff` **110 s⁻¹** (τ_off = 9 ms); iGlu_f **283 s⁻¹** (4 ms); iGlu_u **468 s⁻¹** (2 ms). In vitro `Kd` 33 / 137 / **600 µM**; on HEK membranes at 37 °C **3.1 ± 0.3 / 26 ± 2 / 53 ± 4 µM** — **solution Kd does not transfer to membrane**. Synaptic fluorescence τ_off **13.8 ± 3.8 / 5.2 ± 2.0 / 2.6 ± 1.0 ms**. iGlu_u resolves 100 Hz release; **TBOA did not slow** iGlu_u decay (sparse Schaffer: diffusion, not uptake). Authors: **even iGlu_u cannot resolve true free cleft glutamate**. During the transient, **on-rate, not overall affinity**, determined how many indicator molecules bound.

`primary-source-supported` — Armbruster, Dulla, Diamond 2020, PMC7255799. **full_text_inspected: yes**. iGluSnFR time courses often last **10–100 times longer** than the extracellular lifetime of synaptically released glutamate; the indicator **buffers** glutamate and slows uptake. Waveform ≠ free [Glu].

`primary-source-supported` — Aggarwal et al. 2023, PMC10250197. **full_text_inspected: yes**. iGluSnFR3 improved synaptic vs extrasynaptic specificity. Still a protein indicator.

**BIOC1600 point.** The protein-sensor field had to **measure `koff`**, **lower affinity to speed unbinding**, and still warns that the report is occupancy-filtered. An unlabeled aptamer LOD does not skip that ladder.

---

## 7. Occupancy is not kinetics

`computational illustration` — 1:1 Langmuir 10–90% occupancy span is exactly **81-fold** (`c10 = Kd/9`, `c90 = 9 Kd`), independent of Kd. Rousseau 2023 states this; it also follows from algebra (C027 in the swarm ledger).

Herman 25 nM to Clements 1.1 mM is a **44,000-fold** gap. One 1:1 site cannot be 10–90% occupied in both compartments. Hu’s **0.1 nM–10 µM** semi-log calibration is an **analytical working range**, not proof of dual-compartment occupancy.

If Hu 1.8 nM were treated as a 1:1 occupancy Kd (it is Langmuir–Freundlich electrochemical apparent Kd — **do not**), θ(25 nM) would already be high. If 1d04 12 µM were treated as occupancy Kd, θ(25 nM) would be ~0.2%. Those overlays live in `analysis/accepted/occupancy_kinetics/` and are **SIMULATION**. They do not become `koff`.

---

## 8. Clock ladder (measured objects only)

Empty cells stay empty. IPA 2 ms is the **interrogation clock**, not glutamate unbinding.

| Clock | Object | Value | Construct / system | Tag |
|---|---|---|---|---|
| Cleft τ | inferred free [Glu] lifetime | 1.2 ms (maybe faster) | cultured hippocampal synapses | Clements abstract; Helassa interpretation |
| iGlu_u stopped-flow τ_off | protein `koff` | 2 ms (20 °C) | iGlu_u in vitro | Helassa primary |
| iGlu_u synaptic τ_off | indicator waveform | 2.6 ± 1.0 ms | Schaffer boutons | Helassa primary |
| iGluSnFR vs free Glu | filtered report | 10–100× longer | brain / simulations as in paper | Armbruster primary |
| Extrasynaptic phasic | deconvolved [Glu] | µM for tens of ms; 1–8 µM in 50 ms window | PF stimulation, L401C-EOS | Okubo primary |
| GlutOx t90-like | enzyme electrode | 500–800 ms; model 0.73 s / exp 0.8 ± 0.2 s | freely moving rat / model | Rutherford; Clay |
| ATP E-AB under flow | sensor step | 80–140 ms | ATP, mass transport | Kumakli |
| Xiao FET | stabilize | 200 s | Glu aptamer, 0.1× PBS | Xiao |
| Hu MEA | protocol wait | 15 min Glu | Glu-apt AuED-MEA | Hu journal |
| Hu probe | wait-to-plateau | 10 min at 10 nM | Glu-apt PaC probe | Hu thesis |
| Hu retina | sampling | ~1 min / 14 s scan | in vitro mouse retina | Hu thesis |
| IPA | interrogation | 2 ms | tobramycin/ATP E-AB | Santos-Cancel; Abeykoon |
| Glu aptamer `kon`/`koff` | binding rates | **empty** | all inspected Glu DNA aptamers | unresolved |

---

## 9. Measured vs inferred

**Measured (inspectable primary text).**

- Wu abstract: 1d04 Kd 12 µM; glu1 LOD 0.0013 pM (different constructs).
- Hu MEA: 1.8 nM apparent Kd; 32 pM / 51.5 pM LOD; 15 min Glu wait; 0.1 nM–10 µM semi-log.
- Hu thesis: 10 min plateau; 0.3 pM PBS LOD; Ames 10 nM–10 µM; 14 s ACV; 1 min retina points; authors deny synaptic transients.
- Xiao: SPR 293 nM; FET 10 fM in 0.1× PBS; 200 s stabilize.
- Abrantes preprint: ELONA 10.3–25.1 mM; FET 1 aM; 10 min CSF incubation.
- Herman ~25 nM ambient; Chiu 25.6 nM NAc; Le Meur 83–87 nM.
- Helassa iGlu_u koff/τ_off; Armbruster 10–100×; Okubo 1–8 µM / tens of ms; Rutherford 500–800 ms; Clay 0.73 / 0.8 s.
- Abeykoon tobramycin kon/koff; Chang theophylline and glycine rates; Kumakli ATP 80–140 ms.

**Inferred (model, citation, or transfer).**

- Clements 1.1 mM / 1.2 ms (kinetic inference).
- Helassa “~100 µs” free-cleft claim (cites review + diffusivity paper; Zheng did not measure 100 µs).
- Hu “2D confinement explains 12 µM vs 1.8 nM.”
- Any `t_off` computed from Kd and an assumed `kon`.
- Any statement that glu1 LOD, Hu 1.8 nM, Xiao 293 nM, and Abrantes millimolar Kd describe one molecule.
- Moussawi micromolar resting extrasynaptic compartment (Chiu 2017 is a primary counterexample at rest).
- “Aptamers are too slow” as a measured glutamate `koff`.
- “12 µM unbinds in 0.8 ms” (T5-style bound using diffusion-limited `kon`).

**Unknown.**

- `kon`/`koff` of 1d04, glu1, Hu Glu-apt, Xiao Glu aptamer, NG-Apt-Glu — in solution **or** on the sensor surface, in PBS **or** Ames/aCSF.
- Whether the 10–15 min electrochemical plateau is binding kinetics, mass transport, or an operator-chosen wait longer than equilibration.
- PaC-probe apparent Kd in Ames/tissue (empty).
- In vivo glutamate aptamer sensor (Hu retina is **in vitro**).

---

## 10. Is “keeping up with neurochemical signaling” well-posed?

**No, not as a single claim.**

Neurochemical signaling is at least four problems:

1. **Cleft transients** — mM, ≲1 ms (inferred; possibly faster). Requires fast `kon` at high c **and** fast `koff` so the report can fall. Protein sensors with measured millisecond `koff` still do not report free [Glu] (Helassa, Armbruster). No glutamate aptamer rates exist. Hu’s own retina paper refuses this reading.
2. **Extrasynaptic phasic spillover** — µM, tens of ms (Okubo, deconvolved). A plausible **named** target if (and only if) surface `koff` is tens of s⁻¹ and the probe sits outside the cleft without saturating at basal nM. Unmeasured.
3. **Tonic/ambient** — nM by NMDAR current, activity-independent in Herman’s assay; also nM outside the cleft at rest (Chiu). Minutes-scale electrochemical sampling can in principle address **basal** shifts (Hu thesis light-on/off). That is signaling of a sort, not synaptic waveforms. Occupancy at 25 nM depends on the **surface** isotherm, which is not the Wu 12 µM citation.
4. **Bulk dialysis/MEA extracellular** — µM, seconds to minutes. Enzyme electrodes already operate here (Rutherford). Matching GlutOx 0.5–0.8 s is a different, easier claim than matching 1.2 ms, and it is **still not demonstrated** for Glu-apt (15 min / 200 s / 1 min clocks).

A slogan that the aptamer is “too slow” treats missing `koff` as a negative result. A slogan that “µM SELEX isolates keep up under diffusion-limited `kon`” treats an upper-bound simulation as a measurement and ignores Helassa’s warning that even 2 ms indicator `koff` is not free glutamate. Both slogans collapse clocks.

The well-posed restatement:

> For a **named construct, surface, and buffer**, do measured `kon`/`koff` and the **interrogation clock** jointly allow the sensor occupancy to track **[named glutamate compartment]** without saturating at basal levels or buffering the signal?

That experiment has not been published for any glutamate DNA aptamer.

---

## 11. Highest-information next experiment (or reanalysis)

**Flagship experiment (proposed experiment).**  
**IPA (or SPR/BLI with mass-transport controls) `kobs` vs [Glu] on the Hu Fc-thiol Glu-apt, at the packing density used on the MEA/PaC probe, in Ames or aCSF — not only PBS — plus a step-down dissociation.**

Why this one:

- Fills the empty glutamate `kon`/`koff` cell on the **construct that actually entered tissue**.
- Uses a method already shown to yield surface rates for a small molecule (Abeykoon tobramycin) without pretending those rates transfer.
- Distinguishes `measurement_time` (IPA 2 ms vs ACV 14 s vs 15 min wait) from binding `koff`.
- Concentrations to include on the **same chip**: ~25 nM (Herman/Chiu ambient), ~1–10 µM (Okubo extrasynaptic / dialysis-like), ~100 µM–1 mM (cleft-like step). Report `kobs([c])`, intercept `koff`, slope `kon`, kinetic Kd vs electrochemical apparent 1.8 nM.
- Falsifiers: (i) if surface `koff` ≪ 1 s⁻¹, extrasynaptic tens-of-ms and cleft ms are out of scope; (ii) if kinetic Kd stays ~nM, basal 25 nM saturates occupancy regardless of speed; (iii) if 10 min plateau persists under high flow and fast interrogation, the wait is not mass-transport-limited mixing.

**Second, cheaper reanalysis if Wu VoR is obtained.** Extract 1d04 vs glu1 time courses, truncation map, and any SPR/ITC. Still will not replace a surface kinetic on the Hu probe.

**Do not implement as flagship:** docking; InstructNA training; filling empty Glu `kon` with tobramycin; quoting occupancy-table `t_off` as measured.

**Flagship analysis for the poster storyboard (computational illustration, already built).** A **measured-clocks-only** ladder (section 8), with empty Glu `kon`/`koff` cells, not the diffusion-limited `t_off` overlay as the oral figure. The existing occupancy/sensitivity figures remain useful **only** if captions keep SIMULATION/BOUND and “NOT glutamate.”

---

## 12. Recommendations to the parent project

**Scientific story (this lane).**  
Present glutamate DNA-aptamer sensors have protocol clocks of minutes (or 200 s FET stabilize) and **no published `kon`/`koff`. “Keeping up with neurochemical signaling” is ill-posed until synaptic vs extrasynaptic-phasic vs tonic/basal is named. The only Glu-apt experiment in neural tissue (Hu retina) is explicitly a basal, minute-averaged measurement. Protein glutamate indicators show that even measured millisecond `koff` still reports a filtered occupancy waveform.

This **does not** license “aptamers cannot be fast” (cocaine E-AB <4 s; IPA 2 ms interrogation; ATP 80–140 ms under flow — all **other** targets). It **does** block identifying 15 min incubation or 1.8 nM apparent Kd with 1.2 ms cleft clearance.

**Flagship analysis.** Measured-clocks ladder + empty rate cells. Keep occupancy overlays labeled simulation.

**Highest-information experiment.** Surface `kon`/`koff` of Hu Glu-apt in Ames/aCSF by IPA (or equivalent), concentration series spanning the three biological regimes.

---

## Appendix A. Claim tags (this report)

| ID | Claim | Tag | Transferable |
|---|---|---|---|
| K1 | No inspected Glu DNA-aptamer paper reports kon/koff | unresolved (absence) | no |
| K2 | 1d04 Kd 12 µM ≠ glu1 LOD 0.0013 pM | primary-source-supported | no |
| K3 | Hu electrochemical apparent Kd 1.8 nM ≠ cited 12 µM | primary-source-supported | no |
| K4 | Hu Glu ACV wait 15 min | primary-source-supported | no |
| K5 | Hu thesis 10 min plateau at 10 nM; retina ~1 min sampling, basal not synaptic | primary-source-supported | no |
| K6 | Xiao SPR 293 nM; FET 10 fM in 0.1× PBS; stabilize 200 s | primary-source-supported | no |
| K7 | NG-Apt-Glu ELONA Kd 10.3–25.1 mM vs FET 1 aM | primary-source-supported (preprint) | no |
| K8 | Clements peak 1.1 mM, τ 1.2 ms | primary-source-supported (abstract inference) | unknown |
| K9 | Herman ambient ~25 nM in slice | primary-source-supported | no |
| K10 | Chiu resting NAc synaptic and non-synaptic both nM | primary-source-supported | no |
| K11 | Okubo extrasynaptic 1–8 µM in 50 ms window (deconvolved) | primary-source-supported | no |
| K12 | Langmuir 81-fold 10–90% | computational illustration / review-supported | yes (algebra) |
| K13 | Abeykoon tobramycin kon 3.5×10⁴, koff 1.39 s⁻¹ | primary-source-supported | no |
| K14 | IPA 2 ms is interrogation, not koff | primary-source-supported | n/a |
| K15 | Helassa iGlu_u koff 468 s⁻¹ (20 °C); synaptic τ_off 2.6 ms; still not free cleft Glu | primary-source-supported | no |
| K16 | Armbruster iGluSnFR 10–100× longer than free Glu lifetime | primary-source-supported | no |
| K17 | Rutherford GlutOx 500–800 ms | primary-source-supported | no |
| K18 | “Keeping up with neurochemical signaling” as a single aptamer spec | hypothesis (ill-posed) | n/a |
| K19 | Surface Glu-apt IPA/SPR kobs vs [Glu] in Ames/aCSF | proposed experiment | n/a |

## Appendix B. Sources inspected this lane

| Paper | DOI / PMID / PMCID | full_text_inspected | access_route |
|---|---|---|---|
| Wu 2022 | 10.1007/s00216-021-03783-w / 34783880 | partial | abstract-only |
| Hu 2025 journal | 10.1016/j.bios.2025.117992 / 40992279 | yes | rwth-oa-pdf |
| Hu 2025 thesis | 10.18154/RWTH-2025-07238 | yes | rwth-oa-pdf-text |
| Xiao 2025 | 10.1002/advs.202504497 / PMC12376627 | yes | pmc |
| Abrantes 2025 preprint | 10.1101/2025.11.05.686731 | yes | html |
| Ohsawa 2008 | 10.2116/analsci.24.1.167 | yes | html |
| Ding 2024 | 10.1002/cbic.202400225 / 38785220 | no | abstract-only |
| Chang 2014 | 10.1021/ac5001527 / PMC3983011 | yes | pmc |
| Abeykoon 2025 | 10.1021/acs.analchem.5c01604 / PMC13101946 | yes | pmc |
| Santos-Cancel 2018 | 10.1021/acssensors.8b00278 / PMC6207073 | yes | pmc |
| Kumakli 2023 | 10.1021/acssensors.3c01055 / PMC11059485 | yes | pmc |
| White 2008 | 10.1021/la800801v / PMC2674396 | yes | pmc |
| Rousseau 2023 | 10.1149/2754-2726/ad15a1 / PMC10750225 | yes | pmc |
| Clements 1992 | 10.1126/science.1359647 / 1359647 | no | abstract-only |
| Herman 2007 | 10.1523/JNEUROSCI.3009-07.2007 / PMC2670936 | yes | pmc-html |
| Chiu 2017 | 10.1016/j.celrep.2017.02.047 / PMC5388241 | yes | pmc |
| Le Meur 2007 | PMC2075557 | yes | pmc-html |
| Okubo 2010 | PMC2851965 | yes | pmc-html |
| Moussawi 2011 | PMC3254064 | yes | pmc |
| Featherstone 2008 | PMC2322853 | yes | pmc |
| Helassa 2018 | 10.1073/pnas.1720648115 / PMC6003469 | yes | pmc |
| Marvin 2013 | PMC4469972 | yes | pmc |
| Marvin 2018 | PMC6394230 | yes | pmc |
| Aggarwal 2023 | PMC10250197 | yes | pmc |
| Armbruster 2020 | PMC7255799 | yes | pmc |
| Zheng 2017 | PMC5299514 | yes | pmc-html |
| Scimemi 2009 | PMC2777263 | yes | europepmc-html |
| Rutherford 2007 | PMC3482110 | yes | pmc-html |
| Clay 2018 | PMC5881573 | yes | pmc |

Round 0/1 rule: this lane **promotes nothing to `core`**. Orchestrator owns ledgers.
