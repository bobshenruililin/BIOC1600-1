# Goal Wave A — Lane: SENSOR-ENGINEER CRITIQUE OF THE IDENTITY-INFERENCE ("wrong quantity") ARGUMENT

Worker: sensor-engineer reviewer, `bc-36d289f9-…-bb84`. Branch `cursor/identity-inference-critique-bb84`.
Date of retrieval: 2026-09-11. Access routes: PMC OA HTML (`pmc.ncbi.nlm.nih.gov`), Europe PMC REST (`search`, `fullTextXML`), NCBI `efetch` (`db=pmc`, for NIH author manuscripts). No paid APIs, no PDFs committed.

**Question assigned.** Does Hershey/Kennedy 2025 (PMID 40838767, PMC12418293) actually imply that a glutamate DNA-aptamer biosensor *reports the wrong quantity*, such that making it faster cannot fix usefulness?

**Verdict up front: QUALIFY** — keep the operational form, reject the strong form. Detail in §12.

Lane discipline: I read the primary text of the Kennedy paper myself before reading any other agent's summary of it, then read `rounds/goal-wave-a/opposing-case.md` (branch `cursor/opposing-case-wave-a-c406`) specifically to audit its transcription and its inference. I independently retrieved and inspected the two counter-sources in §6 and §7 rather than inheriting them. Numbers taken from repo ledgers or from other agents' files, and not re-inspected by me, are flagged inline as **inherited**.

---

## 1. What the opposing lane claims

`opposing-case.md` §3.6 (OC-16) and §7.1 make the Kennedy result the single strongest limiter in the whole project, on this reasoning:

> "an aptamer sensor, of any speed, any LOD and any architecture, reports **total free glutamate**… Both error directions are demonstrated in the same animals… Making the sensor faster makes it faster at measuring the wrong quantity."

and ranks it above the dynamic-range argument because "dynamic-range mismatch is a *fixable engineering error*… whereas the observable mismatch is a property of the analyte, not of the instrument."

That last clause is the load-bearing one, and it is the clause the primary source does not support. The dissociation Kennedy reports is, on the authors' own stated mechanism, a property of **how microdialysis recovers two differently-born molecules**, not a property of the analyte.

---

## 2. What was actually measured

All rows `primary-source-supported` from PMC12418293 unless noted. Locators are the paper's own section numbers.

| Axis | What the experiment actually is |
| --- | --- |
| Instrument | Microdialysis + offline benzoyl chloride derivatization + UPLC–MS/MS (Waters Quattro Ultima or Agilent 6410 triple quadrupole). §2.3 |
| Probe geometry | Custom side-by-side fused-silica probes, 40/100 µm i.d./o.d. capillaries inside a **250 µm o.d.** regenerated-cellulose membrane; **CMA12 Elite, 2 mm long, 0.5 mm o.d., 20 kDa MWCO** for Figures 1–2 and SI 1/3/5. §2.2 |
| Perfusion | 1 µL/min. §2.2 |
| Time constant | Fractions every 2 min (5 min for transporter-inhibition and minocycline). Authors state "the temporal resolution of the measurement of 2–5 min". §2.5, §3.2 |
| Recovery | Extraction fraction by stable-isotope loss: `Ed` 0.30 ± 0.03 (Gln), 0.29 ± 0.01 (Glu), n = 11. §3.1 |
| Apparent extracellular concentrations | Gln **179 ± 20 µM**; Glu **9.4 ± 0.6 µM** (n = 11). §3.1 |
| Species resolved | ¹³C₅-Glu (from probe-infused 2.5 µM ¹³C₅-Gln) vs endogenous ¹²C-Glu. §2.5, §3.2 |
| Neuronal channel magnitude | ¹³C₅-Glu steady state **144 ± 35 nM in dialysate** (n = 11). §3.2 |
| Tracer dose | Added ¹³C₅-Gln/¹³C₅-Glu were "less than 2% of their estimated in vivo concentrations". §3.2 |
| Pharmacology route | **Every** drug (TTX, ACPD, MCPG, MeAIB, riluzole, PDC, 75 mM K⁺) was retrodialysed through the same probe. §2.5 |
| Systemic stimuli | Tail pinch (10 min binder clip); minocycline 1 mg/mL drinking water for 2 weeks with probes implanted on treatment day 10. §2.5 |
| Animals | Male Sprague–Dawley; ketamine/dexdomitor for implantation, light isoflurane on the experiment day, then tethered to a Raturn. §2.4 |

Two things in that table are decisive and are not in the opposing lane's account.

**(a) The two "pools" are not sampled with equal efficiency, and the paper says so.** §4.2:

> "We speculate that the use of isotopically labeled Gln allows detection of Glu that is newly made and immediately released near the probe enabling distinction from the large background Glu due to the concentration gradients formed during infusion… **if ¹³C-Glu is formed preferentially near the probe, it is more likely to be captured immediately after release from a neuron than endogenous Glu formed farther away.** Detailed modeling would be useful in addressing these hypotheses."

The authors also give the supporting observable: dialysate ¹³C-Glu/¹³C-Gln = 11% against endogenous Glu/Gln = 7%, i.e. "the probe is able to recover a higher fraction of the Gln converted to Glu for the infused forms."

**(b) The "neuronal" channel is an operational definition with a knob on it.** Its TTX sensitivity is a function of the infusion concentration: at 50 µM ¹³C₅-Gln the recovered ¹³C₅-Glu rose to 650 ± 50 nM (n = 3) and was **not** suppressed by TTX at all (§3.4, §4.2). TTX suppression at 2.5 µM is 62 ± 7%, not complete, and 50 µM TTX does not deepen it. The authors themselves allow a glial-glutaminase contribution and note the TTX-sensitive source "comes from a source that is only dependent on neuronal activity rather than directly released from neurons" as an unexcluded alternative (§4.1).

**Post-implantation interval is not stated in Methods §2.4** for the main experiments (only the minocycline cohort has a stated ~4-day interval by inference from "probes were implanted on the 10th day" of a 2-week treatment). This matters in §7.

---

## 3. Transcription audit of the opposing lane's OC-16 table

I checked every cell against the primary text. Most of it is accurate; three items are not safe to carry into a ledger.

| Cell | Primary text | Audit |
| --- | --- | --- |
| TTX: ¹³C −62 ± 7%, ¹²C unchanged, n = 3 | §3.4 | ✅ correct |
| ACPD: ¹³C −59 ± 9% (p ≤ 0.001, n = 4), blocked by MCPG; ¹²C unchanged | §3.4, Fig. 4 | ✅ correct |
| MeAIB: ¹³C −33 ± 8% (n = 11), ¹²C unchanged | §3.3 | ✅ correct |
| Riluzole: ¹³C −58 ± 3%, ¹²C −33 ± 4% | §3.3 | ✅ values correct; **n is internally inconsistent in the source** (text n = 8, Fig. 2 legend n = 6) |
| Tail pinch: "+155 ± 14%" ¹³C, ¹²C unchanged | §3.6, Fig. 7 | ⚠️ direction correct, **magnitude ambiguous in the source** — see below |
| 75 mM K⁺: "**+**160 ± 20%" ¹²C, no ¹³C increase | §3.6, §4.3 | ❌ most likely **to** 160% of basal (i.e. +60%), not +160% |
| PDC: ¹³C "+173 ± 8%", ¹²C "+342 ± 76%" | §3.5 | ❌ the paper says "increased… 173 ± 8% **relative to** that without PDC", i.e. to 173% (+73%); also **n inconsistent** (text n = 3, Fig. 5 legend n = 4) |
| "Both error directions are demonstrated **in the same animals**" | §3.6 | ❌ both species are co-measured in one dialysate, but tail pinch (n = 4) and high K⁺ (n = 4) are **separate experiments with separate protocols**; the pairing of the two error directions is across cohorts |

On the percent convention: the paper mixes "increased X%" with "increased to X%" within single sentences — §3.6 reads "increased only ¹²C-Glu (160 ± 20%…) …and decreased ¹²C-Gln **to** 48 ± 0.6%". The consistent reading is percent-of-basal throughout, which makes tail pinch **to** 155% (+55%) rather than +155%. I cannot resolve it from the text and I will not pick one. Tag: `unresolved` for the magnitude; `primary-source-supported` for the sign and significance.

**Other source-internal inconsistencies a citation auditor must record before any ledger write:**

- Abstract says "**500 mM** riluzole"; Methods §2.5 says **500 µM**. Abstract typo.
- ¹²C-Gln under 75 mM K⁺: "**48 ± 0.6%**" (§3.6) vs "**54 ± 1%**" (§4.3).
- Figure 1/2 experiments used higher-`Ed` probes than the ones used for the `Ed` calibration in §3.1 (stated in §3.2), so the 144 nM ¹³C₅-Glu and the 9.4 µM endogenous Glu were not obtained on the same probe type.

**"Opposite directions" is an overstatement of the dataset.** Genuinely opposite movement occurs in exactly one experiment — minocycline: ¹³C-Glu **+77 ± 23%** (only one time point significant) while endogenous Glu fell **75 ± 3%** (n = 10 treated vs 11 control, between-subject, systemic 2-week dosing). Every other manipulation is "one channel moves, the other is a null". The mission framing "can move in opposite/error directions" therefore rests on the weakest-controlled experiment in the paper. Tag: `unresolved`.

---

## 4. Four gaps between the experiment and the inference

### G1 — The dissociation is a recovery-geometry result on the authors' own account

This is the central objection. The mechanism the paper offers for *why the labeled channel is visible at all* (§4.2, quoted above) is that the tracer is born and captured inside a thin near-probe shell, whereas endogenous neuronal Glu released farther away is taken up before it reaches the membrane. That mechanism is simultaneously the explanation for the ¹²C null: a neuronal increment released at typical distances is filtered out **by the sampler**, not by chemistry.

An inference of the form "total free glutamate is the wrong observable" requires that the two channels differ in *what they are*. Here they differ in *where they were born relative to the membrane*. Those are different claims, and only the second is supported. A sensor whose transducing surface sits inside the release domain does not inherit a null produced by a recovery asymmetry it does not share.

Tag: `primary-source-supported` for the authors' stated mechanism; `hypothesis` for my inference that a different sampling geometry escapes the null (tested in §6).

### G2 — The neuronal share of total extracellular glutamate is unmeasured, so the magnitude claim has no support

The "wrong quantity" story is at bottom a magnitude claim: the neuronal contribution to total \[Glu\]ₑₓ is too small a share to be worth measuring. The experiment cannot supply that number, and a two-line consistency check shows why.

Suppose the tracer were proportional — that neurons draw on labeled and unlabeled Gln in proportion to local abundance. The paper states the added labeled species were "less than 2% of their estimated in vivo concentrations" (§3.2), so the labeled fraction of the precursor pool is *f* ≲ 0.02. The labeled steady state is 144 nM in dialysate, so proportional labeling implies total neuronally-derived Glu of ≳ 144 nM / 0.02 ≈ **7 µM in dialysate**. But total endogenous dialysate Glu is only about `Ed` × 9.4 µM ≈ 2.7 µM. The neuronally-derived pool would have to exceed the total pool that contains it. The assumption is not merely unlikely; it is arithmetically impossible. The conclusion survives the probe mismatch flagged in §3 (the 144 nM was collected on higher-`Ed` probes than the §3.1 calibration): even at the limiting case `Ed` = 1, total dialysate Glu would be 9.4 µM and the neuronal share would still have to be ~75%, contradicting the paper's own central finding that the endogenous pool is "primarily non-neuronal".

So the proportional-tracer assumption is false, which is exactly the authors' §4.2 position. But the consequence is the one the opposing lane skips: **the relative recovery efficiency of the two channels is unknown and large, so the enrichment cannot be inverted to size the neuronal component of total \[Glu\]ₑₓ.** The experiment establishes differential *regulation* of two operationally defined dialysate species. It does not establish what fraction of total extracellular glutamate is neuronal, and therefore does not establish that a total-Glu sensor has poor contrast — only that *this* total-Glu channel did, at *this* geometry.

Tag: `computational illustration` (the arithmetic, with its assumption stated and immediately falsified); `unresolved` for the neuronal share of total \[Glu\]ₑₓ.

### G3 — Retrodialysis pharmacology has the same radial gradient as the tracer

TTX, ACPD, MCPG, MeAIB, riluzole, PDC and 75 mM K⁺ were all delivered through the probe (§2.5). Drug concentration therefore decays with radial distance in the same direction as the tracer's, and in the *opposite* direction to the origin of the endogenous ¹²C signal. Tissue that is fully drugged is the tissue that makes ¹³C-Glu; tissue that contributes most of the ¹²C-Glu is partially or not drugged. Differential drug sensitivity between the two channels is therefore expected **even under a single-pool model**, with no compartmentalization required.

The paper does not test this. Its closing sentence names the open issue: "further study is required to better understand if the concentration gradients are important."

Important self-correction: **this objection does not apply to the tail pinch**, which is a systemic stimulus reaching all tissue equally. The tail pinch is the cleanest experiment in the paper, and G1 (not G3) is what limits it. The K⁺ experiment is also not a physiological-signalling test: 75 mM K⁺ raised GABA by 2270 ± 400% and halved ¹²C-Gln, and the authors' own explanation for the absent ¹³C response invokes suppression of the Glu-Gln cycle itself (§4.3) — i.e. the stimulus disabled the tracer's supply chain. Calling that a demonstrated astrocytic "false positive" for a deployed sensor is not supported.

Tag: `hypothesis` (gradient confound); `primary-source-supported` for the K⁺ numbers and the authors' shuttle-suppression explanation.

### G4 — The load-bearing cells are nulls at n = 3–4

Every "¹²C unchanged" cell that carries the argument is a failure to reject in **n = 3** (TTX, PDC, MCPG-alone) or **n = 4** (ACPD, tail pinch, K⁺). No equivalence testing, no power statement, and the paper itself documents substantial subject-to-subject variability in the ¹³C channel ("some variability from subject to subject", handled by per-subject normalization, §3.2). A null at n = 3 is weak evidence of absence, and the strong claim is built from a stack of them.

Tag: `unresolved`.

### The paper's own regional counter-statement

§4.3, in full:

> "A few previous studies have shown that this stimulus can evoke release of endogenous Glu in the mPFC that is TTX-sensitive. Those prior results indicate a significant increase in neuronal Glu evoked by tail pinch over the relatively high background. Our results indicate that in the motor cortex, the neuronal response is much more muted and **would not be detectable by recording only endogenous Glu**."

"Would not be detectable" is a **contrast/detectability** statement about one brain region, offered against prior work in which the same stressor *was* detectable in total endogenous glutamate in a different region. The authors are not claiming the observable is categorically wrong. Converting their sentence into "total free glutamate is the wrong observable" is a strengthening the source explicitly declines to make.

---

## 5. What the paper *does* establish for a sensor engineer

Two things, and they are worth keeping.

**S1.** Basal total free glutamate recovered from rat cortex by a 250–500 µm probe on a 2-min clock is dominated by a pool insensitive to local TTX and to an mGluR agonist. This is consistent across the paper's cited prior literature (its refs 22–27) and reproduced here with an internal positive control (the ¹³C channel *does* respond). Any sensor that reproduces that sampling geometry and clock and reports total free Glu inherits that background. Tag: `primary-source-supported`. Quantity: `biological_concentration_range`. Transferable: **to same-geometry samplers only**.

**S2.** In the same animals, with the same probe and the same `Ed` correction, extracellular **Gln is 179 ± 20 µM against Glu 9.4 ± 0.6 µM** — a ~19-fold excess of glutamate's γ-amide. This is a *measured* selectivity specification for any glutamate recognition element, and per `C032` the only glutamate-aptamer selectivity panel in our ledger (Hu thesis: 100 nM Glu vs 10 µM serotonin, dopamine, tyrosine, lactate) omits glutamine and aspartate entirely. Tag: `primary-source-supported`. Quantity: `biological_concentration_range`. Transferable: **yes as a specification**, no as a cross-reactivity result.

S2 is, in my assessment, the more useful output of this paper for our poster than the compartmentalization story — and the opposing lane ranked it second.

---

## 6. Independent counterexample: a total-glutamate sensor did report a TTX-blocked stressor event

Retrieved and inspected by me (Europe PMC `fullTextXML`, PMC2996468), not inherited:

> Hascup ER, Hascup KN, Stephens M, Pomerleau F, Huettl P, Gratton A, Gerhardt GA. *Rapid microelectrode measurements and the origin and regulation of extracellular glutamate in rat prefrontal cortex.* J Neurochem 2010. **PMID 20969570, PMC2996468.** `full_text_inspected = yes`.

What it is: ceramic-based enzyme microelectrode array, Pt sites dip-coated with Nafion, two sites coated with L-glutamate oxidase and **two sentinel sites coated identically but without GluOx** (self-referencing subtraction of electroactive interferents), +0.7 V vs Ag/AgCl, FAST16 acquisition, **second-by-second**, **awake** Long Evans rats (awake specifically because anesthetics depress resting glutamate), PFC. Drugs pressure-ejected through a 33-gauge cannula whose tip sits ~100 µm from the MEA tip.

What it found, all `primary-source-supported`:

| Manipulation | Effect on **total** extracellular glutamate |
| --- | --- |
| Local TTX | **~40% decline** in resting glutamate (n = 7 TTX vs n = 5 citrate, p < 0.01) |
| ω-conotoxin MVIIC | ~50% decrease |
| LY379268 (mGluR2/3 agonist) | ~20% decrease |
| LY341495 (mGluR2/3 antagonist) | ~40% increase |
| TBOA (uptake block) | ~120% increase |
| **5-min tail pinch after local TTX** | glutamate response to the stressor **completely blocked** (n = 6 per group; significant attenuation during stressor minutes 3–5 and minutes 1–4 after) |

Authors' conclusion, verbatim: "PFC resting glutamate levels in rats as measured by the MEA technology are at least 40-50% derived from neurons… the impulse flow-dependent glutamate release from a physiologically-evoked event is entirely neuronally derived."

And their stated reason, which is precisely G1: "The MEA technology involves measures on a second-by-second interval with a microelectrode that resides directly within the extracellular space of the brain that was closer to the glutamatergic synapses than a microdialysis probe. Also, less damage was produced by the MEA as compared to microdialysis probes."

**This is a direct empirical refutation of the strong form.** GluOx has no isotope channel; it measures total free glutamate. A total-glutamate sensor, made smaller and faster and placed closer, reported a TTX-abolished, physiologically evoked glutamate event and a TTX-sensitive tonic component — the two things Kennedy's ¹²C channel could not see. "An aptamer sensor of any speed, any LOD and any architecture reports the wrong quantity" is falsified by an existing sensor that reports the right one.

**Honest limitations of this counterexample, none of which I will suppress:**

- Different brain region (PFC vs Kennedy's motor cortex), and Kennedy's §4.3 says the motor-cortex response is regionally muted. This is a genuine confound between the two studies, not a clean head-to-head.
- Hascup's drug delivery is also local and also imprecise; the authors state "we were not able to reliably show comprehensive depletion of tonic glutamate with local TTX administration" and attribute it to cannula placement variability.
- Enzyme-electrode selectivity is contested by the very paper under review: Kennedy's Introduction names "methodological issues with sensor electrodes, such as effects of enzyme immobilization on selectivity" (citing Vasylieva 2013) alongside the spatial-domain explanation.
- The two methods disagree about the baseline as well, not just the pharmacology: Hascup's Table I lists striatal resting glutamate as **0.18–1.3 µM by microdialysis vs 7.2 ± 1.2 µM by MEA**. Whichever technique is right about the pharmacology, at most one is right about the concentration.
- Resting glutamate on a self-referencing MEA is itself a *difference* between two coated sites, i.e. a subtraction with its own assumptions.

The reconciliation between S1 and this result is `unresolved`. But "unresolved between two methods" is a very different project position from "the observable is wrong."

---

## 7. Probe class is a measured variable, not a rhetorical one

Retrieved and inspected by me (NCBI `efetch db=pmc id=2743756`), not inherited:

> Jaquins-Gerstl A, Michael AC. *Comparison of the brain penetration injury associated with microdialysis and voltammetry.* J Neurosci Methods 2009. **PMID 19559724, PMC2743756.** `full_text_inspected = yes`.

Verified content: vertical concentric microdialysis probes **280 µm o.d., 4 mm long** vs carbon-fibre microcylinders **7 µm diameter, 400 µm long**; microdialysis probes are "at least 10,000 times larger than carbon fiber voltammetric microelectrodes (volume:volume)". At 1, 4 and 24 h, microdialysis tracks are surrounded by PECAM-immunoreactive vessels devoid of perfused nanobeads plus a diffuse PECAM halo, with elevated GFAP; carbon-fibre tracks show none of these and no significant GFAP elevation. Their Discussion summarizes their prior voltammetry-near-probe work: at 1 mm from the probe, evoked DA release is normal; **at ~200 µm it is decreased by 90%; in contact with the probe surface it is abolished.**

Two corrections to how this source is being used elsewhere in the swarm:

- The authors attach a caveat the opposing lane omits: "these prior studies were performed after 4-hr and 16-hr implantations, which are shorter than the recommended 24 hrs, due to the use of an anesthetized preparation."
- The specific figures "~75% of the track circumference" and "carbon-fibre injury confined to ~3 µm by EM" appear in `opposing-case.md` §3.5; I did **not** locate either in the text I retrieved and I am not carrying them forward.

Relevance here: Kennedy's probes (250 µm and 500 µm o.d.) are in the class shown to suppress evoked release in the tissue immediately around them, and Kennedy's Methods do not state the implantation-to-measurement interval for the main experiments. The paper concedes the general point itself (§4.4): "These results do not rule out the possibility that some endogenous Glu that is detected normally by microdialysis is artifactual." A null on evoked total glutamate, measured through a shell of tissue in which evoked release is known to be suppressed, is not a clean measurement of whether total glutamate reports neuronal release. Tag: `hypothesis` for the application to Kennedy; `primary-source-supported` for the Jaquins-Gerstl observations.

---

## 8. Architecture-by-architecture inference — no property transfer

What Kennedy licenses for each transducer. Nothing below transfers a measured value across architectures.

| | Aptamer electrode (E-AB / FET) | GluOx MEA | iGluSnFR |
| --- | --- | --- | --- |
| Isotope channel | none | none | none |
| Chemical observable | total free Glu at the recognition layer | total free Glu at the Pt site, via H₂O₂ | total free Glu at the indicator |
| Orthogonal selectivity channel | none in our ledger's glutamate devices (the Hu MEA is multi-**analyte**, not sentinel-subtracted) | **yes** — sentinel site, verified §6 | spectral / expression-restricted |
| Spatial scale of existing glutamate devices | hundreds of µm (Hu AuED-MEA; Hu PaC intraretinal probe) — **inherited** from `C028`–`C031` | Pt sites on a ceramic shank; carbon-fibre-class trauma per §7 | optical voxel, expression-targetable |
| Clock, as measured | 15 min incubation (`C006`), ~10 min plateau (`C028`), 14 s scan / ~1 min sampling (`C031`) — **inherited** | 500–800 ms (`C022`), second-by-second verified §6 | 10–100× longer than free-Glu lifetime, partly because the indicator buffers glutamate (`C024`) — **inherited** |
| Does Kennedy's null transfer? | **Not by property transfer.** It transfers only if the device reproduces the sampling geometry — which today's do, or worse | **No** — falsified for this architecture by §6 | **No** — the compartment distinction is spatial, and this architecture's discrimination axis is spatial/genetic rather than chemical (`hypothesis`; I did not inspect a cell-type-targeting primary source) |

The sharpest statement available about the aptamer route is therefore *not* "it measures the wrong quantity faster". It is the opposite and it is worse:

> **Relative to the microdialysis experiment that produced the null, today's glutamate aptamer devices are slower (minutes vs 2 min), comparable or larger in sampling scale, have no separation step, no isotope channel and no sentinel-subtraction channel.** They are not a fast instrument pointed at the wrong quantity; they are a slower instrument pointed at the same quantity with fewer selectivity channels.

Tag: `hypothesis`, assembled from `primary-source-supported` device parameters (inherited ledger rows `C006`, `C028`, `C031`) and the verified Kennedy parameters in §2.

---

## 9. A sensor-engineering objection neither lane has raised: the recognition layer is a glutamate sink

The whole debate — the "wrong quantity" story *and* the opposing lane's occupancy table (OC-5) — assumes the sensor is a passive reporter of a concentration that exists independently of it. Kennedy's own experiment shows that assumption failing for a probe: infusing Gln at ~1.4% of ambient (2.5 µM against 179 µM) generates a measurable, TTX-sensitive glutamate efflux. `C024` records the same failure mode for iGluSnFR, whose time courses run 10–100× longer than the free-Glu lifetime **partly because the indicator buffers glutamate** (inherited).

For a dense, high-affinity aptamer monolayer this is quantifiable with two numbers and no fitted parameters. Define the **monolayer depletion depth** h\* = Γ / (C·N_A): the thickness of extracellular fluid at concentration C whose entire glutamate content equals the sensor's site inventory Γ.

Using Γ = 1.43 × 10¹³ sites/cm² (Hu PA immobilization density, **inherited** from `research/reviews/sensor_engineer.md`, not re-inspected by me):

| Concentration anchor | h\* |
| --- | ---: |
| 25 nM (Herman & Jahr ambient, `C012`, inherited) | **9.5 mm** |
| 9.4 µM (Kennedy rat cortex ECF, §3.1, verified) | **25 µm** |
| 1.1 mM (Clements inferred cleft peak, `C011`, inherited) | **0.22 µm** |

```python
NA = 6.02214076e23
G  = 1.43e13                      # sites cm^-2
for C in (25e-9, 9.4e-6, 1.1e-3): # mol L^-1
    print(C, 1e4 * G / (C * NA / 1000), "um")
```

Assumptions, stated because they are strong: full occupancy, planar geometry, one glutamate per site, no resupply during equilibration, and Γ taken from a review file rather than re-inspected. Tag: `computational illustration`.

Two consequences.

1. **It constrains the opposing lane's occupancy argument.** OC-5 computes θ = 0.9998 for a 1.8 nM-apparent-Kd device at 9.4 µM and concludes the sensor is "pinned". That is an equilibrium statement that presumes enough glutamate is locally available to fill the sites. At 25 nM ambient, filling this monolayer would require draining the glutamate from ~9.5 mm of extracellular fluid — against active EAAT uptake. Either the device never approaches the computed occupancy in tissue, or it is reporting a *flux* sustained by release and competing with uptake, not an equilibrium concentration. The occupancy table has an unstated mass-balance assumption, and the "pinned everywhere" conclusion is not safe without it.
2. **It prices the fix.** The remedy G1 implies — smaller device, placed inside the release domain — is not free. At cleft-scale concentrations h\* falls to ~0.2 µm, i.e. the sensor's site inventory becomes comparable to the glutamate in the volume it is trying to observe. Approaching the source and binding tightly are in direct tension, and this is exactly the failure mode already documented for iGluSnFR.

This is the wildcard direction for this lane. It is not a refutation of anything; it is a missing axis.

---

## 10. Inference boundary

**Measured (by others, in sources I inspected):** rat cortical extracellular Gln 179 ± 20 µM and Glu 9.4 ± 0.6 µM (n = 11, `Ed`-corrected); dialysate ¹³C₅-Glu 144 ± 35 nM (n = 11); differential drug and stimulus sensitivity of the two dialysate species at the percentages in §3 with the noted convention ambiguity; ~40% TTX-sensitive tonic glutamate and complete TTX block of the tail-pinch response on a second-by-second GluOx MEA in awake rat PFC (n = 6–7); 280 µm vs 7 µm probe geometries with 90% suppression of evoked DA release at ~200 µm from a dialysis probe.

**Inferred (by me):** that the Kennedy dissociation is substantially attributable to differential recovery rather than to a chemical property of the analyte (G1, resting on the authors' own §4.2); that retrodialysis gradients could reproduce differential drug sensitivity under a single-pool model (G3); the monolayer depletion depths (§9); the architecture table (§8).

**Unknown:** the neuronal fraction of total extracellular glutamate in any region (G2); the relative recovery efficiency of the two dialysate channels; the reconciliation between microdialysis and enzyme-MEA pharmacology *and* baselines (§6); every kinetic constant for every glutamate aptamer (`C007`); glutamate-aptamer cross-reactivity to glutamine at 179 µM (`C032`); whether any glutamate aptamer device can be built in the ≤ tens-of-µm class at all.

---

## 11. Falsifier for *my own* position

I am arguing that the limiter is sampling domain, not observable identity. The observation that would materially weaken me:

> A small, low-trauma, fast **total**-glutamate sensor (carbon-fibre-class or GluOx-MEA-class, sub-second, sentinel-subtracted) placed inside the release domain, co-located with a Kennedy-protocol ¹³C₅-Gln microdialysis channel in the same animal and region, shows **no** stressor-evoked, TTX-abolished signal while the co-sampled ¹³C channel does.

If that is observed, "wrong quantity" is upgraded from qualify to keep, and the project should stop optimizing sensor speed. Note that the closest existing approximation to this experiment (Hascup, §6) currently points the other way, but in a different region and without a co-located tracer channel.

---

## 12. Required outputs

### Keep / qualify / reject

**QUALIFY.**

**Keep (operational form, `primary-source-supported` observations + `hypothesis` extension):** for a device that reports total free glutamate from bulk cortical extracellular fluid at a hundreds-of-µm sampling scale on a minutes clock, the neuronally-derived component of the basal signal is small enough that local TTX and an mGluR agonist produce no detectable change, and a stressor that demonstrably drove neuronal release produced no detectable change either. Speed alone does not repair that — and the glutamate aptamer devices in our ledger are *slower* and no smaller than the probe that produced the null. Also keep, and promote: glutamine at 179 ± 20 µM against glutamate at 9.4 ± 0.6 µM is a measured selectivity specification that no glutamate aptamer has been tested against.

**Reject (strong form: "reports the wrong quantity", "faster cannot fix usefulness"):** on four grounds, in descending strength.
1. The paper's §4.2 attributes the visibility of the neuronal channel to a **recovery-geometry** advantage of the tracer. A dissociation generated by differential recovery cannot be used to argue that the observable itself is wrong.
2. Hascup et al. 2010 (verified independently, §6): a total-glutamate sensor with no isotope channel, made smaller and second-by-second, saw ~40% TTX-sensitive tonic glutamate and a **completely TTX-blocked tail-pinch response**. An existing total-Glu architecture reports the event Kennedy's ¹²C channel missed.
3. Kennedy's own §4.3 frames the motor-cortex ¹²C null as a **detectability** result and contrasts it with prior mPFC studies where the same stressor did move endogenous glutamate. Detectability against a background is a contrast statement, not an identity statement.
4. The experiment cannot size the neuronal share of total \[Glu\]ₑₓ (G2), and the magnitude claim needs that number.

**What survives, honestly:** no binding- or enzyme-based transducer can reproduce the isotope channel. If metabolic labeling were the *only* route to source attribution, that route would be closed to aptamers permanently. Kennedy does not show it is the only route; Hascup attributes pharmacologically with a total sensor and it works.

**Replacement sentence for the poster:** the limiting variable is **the sampling volume relative to the glutamate release domain**, of which speed is one axis and probe size/placement is the other — and today's glutamate aptamer devices are worse than a microdialysis probe on both. That is a falsifiable engineering claim; "wrong quantity" is not.

### One flagship analysis implication

**The flagship occupancy analysis must acquire a mass-balance constraint before it can be shown.** Concretely: add one panel plotting the monolayer depletion depth h\* = Γ/(C·N_A) across the biological concentration span (§9), using Hu's measured site density and the three verified concentration anchors, alongside the existing 1:1 Langmuir θ curve. It needs no fitted constants and no invented numbers, it is explainable by a first-year student in one sentence ("the sensor's own binding sites can hold more glutamate than the fluid around them contains"), and it does the discriminating work: it shows that the equilibrium-occupancy argument — the project's current flagship and the opposing lane's runner-up limiter — is only valid where local resupply exceeds the sensor's own sink capacity. Labeled as a simulation in caption, ledger and nightly summary.

### Highest-information next experiment

**Co-locate the two measurements in one animal.** Run the Kennedy ¹³C₅-Gln retrodialysis protocol unchanged, with a fast total-glutamate sensor implanted at a defined, measured distance from the dialysis membrane, and apply the 10-min tail pinch with and without TTX.

- If the near-field total-Glu channel reports the TTX-abolished event that the co-sampled ¹²C dialysate channel misses, the observable is not wrong, the limiter is sampling domain, and the project's title changes.
- If it also misses it, "wrong quantity" is upgraded to keep and speed optimization should stop.

Version 1 requires **no aptamer at all** — use a GluOx MEA, whose sub-second response and sentinel channel are already established (`C022`, §6) — and it uses only techniques both groups already run. It is the only experiment I can identify that separates G1 from the identity claim rather than adding another single-method measurement to a two-method disagreement. The aptamer version becomes meaningful only once a glutamate aptamer device exists in the ≤ tens-of-µm class, which per `C020`/`C031` it does not.

Tag: `proposed experiment`.

---

## 13. Records proposed to the orchestrator

This lane writes no ledger rows. Lane-local IDs (`SE-n`) to avoid colliding with other Wave A proposals; highest existing source is `S066`.

| # | Proposed record | Tag | Source | Quantity type | Value | Construct / system | Transferable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SE-1 | Hershey/Kennedy 2025 rat cortex, `Ed`-corrected: Gln 179 ± 20 µM vs Glu 9.4 ± 0.6 µM, n = 11, same probe and animals | primary-source-supported | PMID 40838767 / PMC12418293 §3.1 | biological_concentration_range | 179 / 9.4 | µM; rat cortex microdialysis | as a **specification** yes; as a cross-reactivity result no |
| SE-2 | Dialysate ¹³C₅-Glu steady state 144 ± 35 nM (n = 11) from 2.5 µM ¹³C₅-Gln infusion | primary-source-supported | ibid. §3.2 | biological_concentration_range | 144 ± 35 | nM in dialysate, **not** `Ed`-corrected | no |
| SE-3 | TTX 2 µM suppressed ¹³C₅-Glu 62 ± 7% (n = 3) with endogenous ¹²C-Glu unchanged; ACPD 200 µM suppressed it 59 ± 9% (n = 4), MCPG-reversible, ¹²C unchanged | primary-source-supported | ibid. §3.4 | biological_concentration_range | −62 / −59 | %; rat cortex, **retrodialysed** drug | no |
| SE-4 | Tail pinch changed ¹³C₅-Glu (TTX-abolished, n = 4) with ¹²C-Glu unchanged; **percent convention ambiguous in source** (155% *of* vs *increase of* 155%) | primary-source-supported (sign); unresolved (magnitude) | ibid. §3.6, Fig. 7 | biological_concentration_range | see note | %; rat motor cortex | no |
| SE-5 | The tracer's TTX sensitivity is abolished at 50 µM ¹³C₅-Gln infusion (650 ± 50 nM recovered, n = 3): the "neuronal" channel is protocol-dependent | primary-source-supported | ibid. §3.4, §4.2 | — | — | operational definition caveat | n/a |
| SE-6 | Authors attribute the labeled channel's visibility to preferential formation and capture near the probe (dialysate ¹³C-Glu/¹³C-Gln 11% vs endogenous 7%) | primary-source-supported | ibid. §4.2 | — | 11 / 7 | %; recovery-geometry statement | n/a |
| SE-7 | Hascup 2010: local TTX reduced resting PFC glutamate ~40% (n = 7 vs 5) and completely blocked the 5-min tail-pinch glutamate response (n = 6/group) on a second-by-second self-referencing GluOx MEA in awake rats | primary-source-supported | PMID 20969570 / PMC2996468, §3.7, Discussion | biological_concentration_range | ~40 | %; rat PFC, enzyme MEA | no — enzyme MEA, not aptamer |
| SE-8 | Hascup Table I: striatal resting glutamate 0.18–1.3 µM by microdialysis vs 7.2 ± 1.2 µM by MEA | primary-source-supported | ibid. Table I | biological_concentration_range | 0.18–1.3 / 7.2 | µM | no |
| SE-9 | Jaquins-Gerstl 2009: 280 µm o.d. dialysis probe vs 7 µm carbon fibre; evoked DA release −90% at ~200 µm from the probe, abolished at contact (authors' caveat: 4 h and 16 h anesthetized implants) | primary-source-supported | PMID 19559724 / PMC2743756, §4 | signal_gain | 90 | %; rat striatum, dopamine | no — geometric argument only |
| SE-10 | Monolayer depletion depth h\* = Γ/(C·N_A) at Γ = 1.43 × 10¹³ cm⁻²: 9.5 mm at 25 nM, 25 µm at 9.4 µM, 0.22 µm at 1.1 mM | computational illustration | §9; Γ inherited, not re-inspected | analytical_working_range | see table | derived mass-balance identity | yes (algebra only) |
| SE-11 | Source-internal inconsistencies in PMC12418293: abstract "500 mM riluzole" vs Methods 500 µM; riluzole n = 8 (text) vs 6 (Fig. 2); PDC n = 3 (text) vs 4 (Fig. 5); ¹²C-Gln under K⁺ 48 ± 0.6% (§3.6) vs 54 ± 1% (§4.3); Fig. 1–2 probes had higher `Ed` than the §3.1 calibration probes | unresolved | ibid., locators as listed | — | — | transcription hazard | n/a |

---

## 14. Research Effort Standard items addressed by this lane

- **Best supporting case for the reviewed claim:** §5 (S1, S2) and §2 — the basal TTX/mGluR insensitivity of bulk dialysate glutamate is real, replicated in the paper's cited literature, and internally controlled by a responsive ¹³C channel.
- **Best opposing case:** §4 (G1–G4), §6, §7.
- **Context for the conflict:** §6 limitations — region (PFC vs motor cortex), probe class, enzyme-immobilization selectivity, local-delivery precision, and a baseline disagreement of roughly an order of magnitude between the two methods.
- **Inference boundary:** §10.
- **Falsifier of my own position:** §11.
- **Highest-information next step:** §12.
- **Independent thought:** I read the primary source before the opposing lane's summary, and independently retrieved both counter-sources; §3 and §7 record where the opposing lane's transcription does not survive audit.
- **Wildcard:** §9, the recognition layer as a glutamate sink — a direction specified by neither the parent prompt nor any other lane, which turns out to constrain the project's current flagship analysis.
- **Negative-search integrity:** I did not run a fresh literature sweep; this lane is a critique of a specified inference. The three sources in §2/§6/§7 were retrieved by PMCID and by one Europe PMC title/author query (`AUTH:"Hascup ER" AND TITLE:"Rapid microelectrode measurements"`, 1 hit). Two claims I could not verify and therefore did not carry are named in §7. One iGluSnFR claim in §8 is tagged `hypothesis` because I did not inspect a cell-type-targeting primary source.
- **Not optimizing for agreement:** this lane reduces the strength of the result the opposing lane nominated as the project's single strongest limiter, and separately constrains the occupancy analysis that the tournament currently lists as flagship.
