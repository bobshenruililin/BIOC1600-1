# Round 1 literature scout 06 — wildcard lane

- **Scout:** literature-scout 6 of 6
- **Date:** 2026-09-11
- **Model:** cursor-grok-4.6-xhigh
- **Isolation:** did not read other scout reports, theses, `state/claims.csv`, or nightly summaries
- **Round 1 status:** candidates only; nothing promoted to `core`
- **Ledgers:** this file only; orchestrator may merge

## Assigned lane (wildcard)

**Question actually searched:** Is “can an aptamer keep up with neurochemical signaling?” a glutamate-aptamer-specific problem, or does the literature already show (i) non-aptamer glutamate sensors that resolve some neurodynamic clocks, (ii) nucleic-acid aptamer sensors that operate in vivo for *other* neurochemicals, and/or (iii) a biochemical reason glutamate itself is a hard aptamer target — such that usefulness is use-case- and construct-specific?

This sits beside the default framing. It does not assume that aptamer quality is “not a single number,” and it does not treat docking as evidence.

**Direction chosen because the literature supports it (not manufactured):**

1. Genetically encoded glutamate indicators (iGluSnFR family) were built expressly to visualize synaptic glutamate. `primary-source-supported`
2. Glutamate-oxidase microelectrodes report subsecond-to-second extrasynaptic glutamate in behaving rodents, with a documented enzyme/film `response_time` floor. `primary-source-supported`
3. Aptamer FETs for serotonin/dopamine operate in physiological buffer and, in one implantable study, in vivo — but reported FET `response_time` is seconds, not cleft milliseconds. `primary-source-supported`
4. A DNA glutamate aptasensor exists as an analytical ACV device; its `Kd_molecular` and `sensor_LOD` are different quantities and were not measured as synaptic kinetics. `primary-source-supported` (abstract-level for the sensor paper)
5. Tonic `biological_concentration_range` estimates disagree by ~100-fold across methods (NMDAR inference vs enzyme MEA vs microdialysis). `primary-source-supported` as a documented disagreement, not as a resolved number

## Search strategy

Free routes only: PubMed E-utilities, Europe PMC REST, Crossref, OpenAlex, Unpaywall (`email=bioc1600.scout@gmail.com`), PMC HTML, publisher OA HTML. No Sci-Hub, no paid APIs, no PDFs committed.

| Query (PubMed unless noted) | Hits (approx.) | What it yielded |
|---|---:|---|
| `iGluSnFR[Title/Abstract]` | 99 | Marvin 2013; Aggarwal 2023; related GECI/iGlu work |
| `"intensity-based glutamate-sensing fluorescent reporter"` OR `iGluSnFR[Title]` | 15 | core iGluSnFR papers |
| `iGluSnFR3` OR `SF-iGluSnFR` OR `iGlu_u` OR `u-iGluSnFR` | 14 | Helassa 2018; Aggarwal 2023; Coates 2020 |
| glutamate oxidase microelectrode (response time OR temporal resolution) (brain OR in vivo) | 13 | Huang 2020; Ganesana 2019; Wassum 2008 |
| (glutamate oxidase) AND (response time OR rise time OR t90) AND (in vivo OR brain) | 34 | Huang 2020; Wassum 2012; Hascup-related |
| `Hascup glutamate ceramic electrode` | 3 | Hascup 2008/2014; book chapter 21204381 |
| `"second-by-second" glutamate microelectrode` | 11 | Hascup 2008; Rutherford 2007; Konradsson-Geuken 2009 |
| `Gerhardt glutamate ceramic biosensor` | 4 | Pomerleau 2003; Burmeister 2013 |
| `Nakatsuka aptamer field-effect` | 11 | Nakatsuka 2018; Zhao 2021; Cheung 2019 |
| aptamer dopamine (FET OR transistor) (in vivo OR brain) | 33 | Zhao 2021; Gao 2022; Liu 2026 (closed) |
| aptamer serotonin (in vivo OR voltammetry OR FET) | 13 | Zhao 2021; Ahmad 2023; Nakatsuka 2021 |
| `"glutamate aptamer"` OR `"aptamer for glutamate"` OR `"L-glutamate aptamer"` | 130 | many false hits (AMPA-receptor aptamers, PSMA, PfGDH, peptide aptamers); Wu 2022 is the ligand-DNA aptasensor |
| `Wu electrochemical aptasensor glutamate 2022` | 1 | Wu 2022 PMID 34783880 |
| RNA aptamer glutamic acid OR L-glutamate SELEX | 23 | Ohsawa 2008; Kuwahara 2005; receptor-aptamer near-misses |
| `Majerfeld glutamate RNA` / `Yarus glutamate aptamer RNA` | 0 / 3 (off-target) | no verified Yarus glutamate-ligand RNA aptamer in these strings |
| `Clements` synaptic cleft glutamate time course | 2 | Clements 1992; Lester 1990 |
| Herman Jahr extracellular glutamate hippocampal | 2 | Herman 2007; Herman 2011 |
| `fast-scan cyclic voltammetry glutamate` | 75 | Kimble 2023 (enzyme-coupled FSCV; glutamate still nonelectroactive) |
| Europe PMC: AUTH Nakatsuka TITLE aptamer transistor | 7 | Nakatsuka 2018; Zhao 2021; related |
| Europe PMC / OpenAlex / Unpaywall on shortlisted DOIs | — | OA vs closed recorded per source |

**Date of searches:** 2026-09-11.

## Candidates (n = 15)

Identifiers verified against PubMed MEDLINE and, for DOI, Crossref and/or OpenAlex unless noted. Status for orchestrator merge: **`candidate`**. Transferable across constructs/architectures: **`unknown`** unless a cited experiment on the same construct is named.

---

### S06-01

- **title:** The time course of glutamate in the synaptic cleft
- **year:** 1992
- **journal:** Science
- **authors:** Clements JD; Lester RA; Tong G; Jahr CE; Westbrook GL
- **DOI:** 10.1126/science.1359647
- **PMID:** 1359647
- **PMCID:** (empty)
- **source_type:** primary
- **why it matters for THIS assigned lane:** This paper is the classic electrophysiological estimate of free cleft glutamate, not an aptamer or enzyme sensor. PubMed abstract: glutamate peaked at 1.1 millimolar and decayed with a time constant of 1.2 milliseconds at cultured hippocampal synapses (`biological_concentration_range` and a biological clearance clock; `primary-source-supported` at abstract level). The lane needs this clock because later enzyme papers explicitly contrast their `response_time` with synaptic milliseconds, and iGluSnFR papers treat millisecond clearance as the design target. `unresolved` from this scout whether the 1.1 mM / 1.2 ms numbers survive full-text kinetic assumptions; full text is closed.
- **full_text_inspected:** no
- **access_route:** abstract-only
- **limitation:** Cultured hippocampal synapses; antagonist-displacement inference, not a direct chemical sensor. Closed on Unpaywall/OpenAlex (`oa=False`). Do not treat 1.2 ms as a glutamate-aptamer `koff` or as an enzyme-sensor `response_time`.

---

### S06-02

- **title:** Extracellular glutamate concentration in hippocampal slice
- **year:** 2007
- **journal:** The Journal of Neuroscience
- **authors:** Herman MA; Jahr CE
- **DOI:** 10.1523/JNEUROSCI.3009-07.2007
- **PMID:** 17804634
- **PMCID:** PMC2670936
- **source_type:** primary
- **why it matters for THIS assigned lane:** Sets a competing tonic `biological_concentration_range`. PMC HTML (NIHMS102657): using NMDARs on CA1 pyramids in acute hippocampal slices, baseline extracellular glutamate is near 25 nM; superfusion of low-micromolar glutamate had no effect because transporters prevent access; authors suggest in vivo ambient glutamate is also nanomolar (abstract p.9736; Results estimate ~25 nM after dose–response scaling, Fig. 2E). `primary-source-supported` for the slice NMDAR-inference. The same paper reviews microdialysis reports of 1–4 µM in vivo (`review-supported` inside this primary paper, not independently re-extracted here). If tonic glutamate were micromolar, a high-affinity aptamer could be occupancy-saturated; if nanomolar, the opposite occupancy problem appears. The disagreement with enzyme-MEA micromolar tonic values (S06-06) is the wildcard fact: there is no single biological concentration number to “keep up with.”
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** Acute slice, P15–19 rat, NMDAR as the detector (not a chemical assay). Authors themselves flag uncertainty of extrapolating slice to intact brain. Do not transfer 25 nM to extracellular fluid sampled by a 100-µm oxidase electrode.

---

### S06-03

- **title:** An optimized fluorescent probe for visualizing glutamate neurotransmission
- **year:** 2013
- **journal:** Nature Methods
- **authors:** Marvin JS; Borghuis BG; Tian L; Cichon J; Harnett MT; Akerboom J; Gordus A; Renninger SL; Chen TW; Bargmann CI; Orger MB; Schreiter ER; Demb JB; Gan WB; Hires SA; Looger LL
- **DOI:** 10.1038/nmeth.2333
- **PMID:** 23314171
- **PMCID:** PMC4469972
- **source_type:** primary
- **why it matters for THIS assigned lane:** Existence proof that a *protein* glutamate reporter can visualize neurotransmission in vivo (worm, fish, mouse motor cortex). PMC NIHMS429924: soluble iGluSnFR `Kd_molecular` 107 ± 9 µM glutamate vs 145 ± 18 µM aspartate in vitro; membrane `Kd_molecular` 4 ± 1 µM on HEK293 and 4.9 ± 1.3 µM on neurons (Fig. 1b). Single-stimulus neuronal `response_time` reported as rise t½ = 15 ± 11 ms and decay t½ = 92 ± 11 ms (Fig. 2e). Introduction contrasts enzyme microelectrodes as having `response_time` “on the order of a second” and lacking cellular resolution (p. opening tools paragraph). `primary-source-supported` for this construct and those assays. The 25-fold soluble-to-membrane affinity shift is a no-transfer warning for any later aptamer surface immobilization.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** NIHMS author manuscript, not the typeset Nature PDF. iGluSnFR is GltI-cpGFP, not an aptamer. On-rate faster than their stopped-flow; `kon` not numerically reported here. Decay t½ is an optical `response_time`, not cleft clearance.

---

### S06-04

- **title:** Ultrafast glutamate sensors resolve high-frequency release at Schaffer collateral synapses
- **year:** 2018
- **journal:** Proceedings of the National Academy of Sciences of the United States of America
- **authors:** Helassa N; Durst CD; Coates C; Kerruth S; Arif U; Schulze C; Wiegert JS; Geeves M; Oertner TG; Torok K
- **DOI:** 10.1073/pnas.1720648115
- **PMID:** 29735711
- **PMCID:** PMC6003469
- **source_type:** primary
- **why it matters for THIS assigned lane:** Directly tests whether a glutamate *indicator* can keep up with high-frequency synaptic release — the same “keep up” question asked of aptamers, asked of a protein. Europe PMC XML / PMC: parent iGluSnFR visualizes up to ~10 Hz; iGlu_f and iGlu_u have in-vitro `Kd_molecular` 137 µM and 600 µM; iGlu_u has sixfold faster in-vitro dissociation and fivefold faster synaptic kinetics vs iGluSnFR. Stopped-flow at 34 °C: τ_off = 4.3 ms (iGluSnFR), 2.1 ms (iGlu_f), 0.68 ms (iGlu_u) (`koff` as 1/τ_off for those fits). Synaptic fluorescence τ_off: 13.8 ± 3.8 ms, 5.2 ± 2.0 ms, 2.6 ± 1.0 ms. iGlu_u resolved individual events in 100 Hz trains; TBOA did not slow iGlu_u decay at sparse Schaffer synapses (diffusion-dominated clearance in that regime). Rate-limiting step is a conformational change after binding, not diffusion-limited `kon`. `primary-source-supported`. Speeding the indicator required *raising* `Kd_molecular` — a biochemical trade-off any glutamate aptamer would also face.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** Hippocampal slice culture, selected high-p_r boutons. Membrane HEK `Kd_molecular` (3.1 / 26 / 53 µM at 37 °C) differs from soluble values; do not transfer. Not an aptamer. PubMed AU lists Durst/Torok without diacritics; Crossref/PMC use Dürst/Török.

---

### S06-05

- **title:** Glutamate indicators with improved activation kinetics and localization for imaging synaptic transmission
- **year:** 2023
- **journal:** Nature Methods
- **authors:** Aggarwal A; Liu R; Chen Y; Ralowicz AJ; Bergerson SJ; Tomaska F; Mohar B; Hanson TL; Hasseman JP; Reep D; Tsegaye G; Yao P; Ji X; Kloos M; Walpita D; Patel R; Mohr MA; Tillberg PW; GENIE Project Team; Looger LL; Marvin JS; Hoppa MB; Konnerth A; Kleinfeld D; Schreiter ER; Podgorski K
- **DOI:** 10.1038/s41592-023-01863-6
- **PMID:** 37142767
- **PMCID:** PMC10250197
- **source_type:** primary
- **why it matters for THIS assigned lane:** iGluSnFR3 is the current protein-side answer to “can a glutamate sensor keep up *and* stay synaptic.” Europe PMC XML / Nature OA HTML: prior variants had low in vivo SNR, saturating activation kinetics, and extrasynaptic blur; iGluSnFR3.v857 shows rapid nonsaturating activation, optical minis, and in vivo single-AP transients in mouse visual cortex plus whisker-related input timing spanning tens of milliseconds in L4. `primary-source-supported` for those imaging assays. This is the empirical bar a glutamate *aptamer* optical or electronic sensor would have to match if the use-case is synaptic transmission rather than bulk extrasynaptic glutamate.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** Hybrid OA (CC BY). Still a genetically encoded PBP-FP fusion. Do not copy iGluSnFR3 `response_time` onto DNA aptamers. Exact `Kd_molecular` / `kon` / `koff` for v857 should be taken from Extended Data tables in extraction round, not guessed here.

---

### S06-06

- **title:** Second-by-second measures of L-glutamate in the prefrontal cortex and striatum of freely moving mice
- **year:** 2008
- **journal:** The Journal of Pharmacology and Experimental Therapeutics
- **authors:** Hascup KN; Hascup ER; Pomerleau F; Huettl P; Gerhardt GA
- **DOI:** 10.1124/jpet.107.131698
- **PMID:** 18024788
- **PMCID:** PMC3404456
- **source_type:** primary
- **why it matters for THIS assigned lane:** Enzyme-based ceramic MEA that *does* keep up with a defined in vivo use-case: tonic and phasic extrasynaptic glutamate in awake mice on a 1 s sampling grid. PMC NIHMS390173: MEAs detect low Glu on a subsecond scale (500–800 ms) vs AA/DOPAC; in-vitro `sensor_LOD` 0.9 ± 0.2 µM; sensitivity −8.6 ± 0.7 pA/µM; selectivity 146 ± 20 : 1 (n = 31 MEAs, 61 sites). Resting (tonic) Glu 3.3 µM PFC and 5.0 µM striatum (`biological_concentration_range` as reported by this architecture). TTX decreased resting Glu ~20%; THA increased ~60%. Viable 7 days in vivo. `primary-source-supported` for this GluOx MEA. Contrasts microdialysis `measurement_time` of minutes and Kennedy-group capillary electrophoresis `response_time` not faster than 10 s. This is “keeping up” with behavior-timescale extrasynaptic glutamate, **not** with Clements 1.2 ms cleft transients.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** Self-referenced oxidase/H2O2 amperometry; spatial scale hundreds of micrometres. Tonic micromolar values conflict with Herman 25 nM (S06-02); that conflict is evidence, not a bug to average away. Do not transfer 3.3–5.0 µM to NMDAR occupancy or to an aptamer calibration.

---

### S06-07

- **title:** Electroenzymatic glutamate sensing at near the theoretical performance limit
- **year:** 2020
- **journal:** The Analyst
- **authors:** Huang IW; Clay M; Wang S; Guo Y; Nie J; Monbouquette HG
- **DOI:** 10.1039/c9an01969c
- **PMID:** 31998887
- **PMCID:** PMC7117983
- **source_type:** primary
- **why it matters for THIS assigned lane:** States the enzyme-architecture ceiling in numbers. PMC NIHMS1554748: t90 `response_time` defined as time to 90% of steady-state current after a 0→40 µM Glut step with external mass transfer minimized = 0.080 ± 0.012 s (n = 5), vs prior ~1 s films; sensitivity 320 ± 19.6 nA µM−1 cm−2 (n = 18); `sensor_LOD` (S/N = 3) 0.70 ± 0.08 µM. Introduction: tools that match cellular spatial scale *and* “single-digit millisecond” synaptic signaling “have yet to emerge” for chemical neurotransmission. Model says performance approaches the theoretical limit **of this construction** (thin GluOx + PPD/Nafion on Pt). `primary-source-supported`. Wildcard implication: even an optimized oxidase electrode is ~80 ms in vitro, ~70× slower than Clements’ 1.2 ms biological clock — so “enzyme sensors already keep up with neurodynamics” is true only for a slower extrasynaptic clock, not for cleft transients.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** In-vitro step-response, not in vivo. Mathematical model is labeled as a model (`computational illustration` for the “theoretical limit” claim beyond the measured t90). Detection limit did not improve with sensitivity (noise-limited).

---

### S06-08

- **title:** Transient extracellular glutamate events in the basolateral amygdala track reward-seeking actions
- **year:** 2012
- **journal:** The Journal of Neuroscience
- **authors:** Wassum KM; Tolosa VM; Tseng TC; Balleine BW; Monbouquette HG; Maidment NT
- **DOI:** 10.1523/JNEUROSCI.5780-11.2012
- **PMID:** 22357857
- **PMCID:** PMC3548241
- **source_type:** primary
- **why it matters for THIS assigned lane:** Shows a *defined behavioral use-case* that enzyme glutamate sensors already serve: second-to-second BLA transients time-locked to lever pressing in freely moving rats. PMC HTML: silicon Pt MEA + GluOx; Nafion/polypyrrole keep `response_time` <1 s while rejecting AA/DA; self-referencing reveals rapid transients “potentially reflective of synaptic overspill.” `primary-source-supported` for this sensor and task. Related Wassum 2008 (PMID 19543440, PMC2699285, inspected) reports `sensor_LOD` under 1 µM and sub-1 s `response_time` in solution plus in vivo evoked/stress release. If the BIOC1600 question is “usefulness,” this is usefulness without an aptamer.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** “Synaptic overspill” is an interpretation (`hypothesis` relative to cleft contents). <1 s is not 1 ms. Immobilization chemistry (PPy/Nafion/GluOx) is not transferable to a thiol-DNA gold aptasensor.

---

### S06-09

- **title:** Ultrafast Glutamate Biosensor Recordings in Brain Slices Reveal Complex Single Exocytosis Transients
- **year:** 2019
- **journal:** ACS Chemical Neuroscience
- **authors:** Wang Y; Mishra D; Bergman J; Keighron JD; Skibicka KP; Cans AS
- **DOI:** 10.1021/acschemneuro.8b00624
- **PMID:** 30605606
- **PMCID:** (empty)
- **source_type:** primary
- **why it matters for THIS assigned lane:** Strongest *abstract-level* claim that an enzyme glutamate biosensor can resolve single submillisecond exocytosis events (~30 Hz bursts) in nucleus accumbens slices (GluOx on a gold-nanoparticle microelectrode; amperometry). `primary-source-supported` only as far as the PubMed/Crossref abstract; Unpaywall/OpenAlex mark the article closed. If the full paper’s spike-width analysis survives extraction, it would challenge Huang 2020’s ~80 ms t90 as a universal enzyme floor — likely because architecture (nanoparticle amperometry vs planar film t90) differs. That is exactly a no-property-transfer case.
- **full_text_inspected:** no
- **access_route:** abstract-only
- **limitation:** Closed. Publisher HTML was a Cloudflare interstitial. Do not enter spike-width numbers beyond the abstract’s “submillisecond” / “approximately 30 Hz.” Slice, not freely moving. MeSH lists Glutamic Acid as “pharmacology,” which is a cataloging oddity, not a reason to discard the paper.

---

### S06-10

- **title:** Aptamer-field-effect transistors overcome Debye length limitations for small-molecule sensing
- **year:** 2018
- **journal:** Science
- **authors:** Nakatsuka N; Yang KA; Abendroth JM; Cheung KM; Xu X; Yang H; Zhao C; Zhu B; Rim YS; Yang Y; Weiss PS; Stojanovic MN; Andrews AM
- **DOI:** 10.1126/science.aao6750
- **PMID:** 30190311
- **PMCID:** PMC6663484
- **source_type:** primary
- **why it matters for THIS assigned lane:** Existence proof that DNA aptamer FETs can read small neurochemicals in physiological ionic strength — the Debye-length objection is experimentally addressed for this architecture. PMC NIHMS author manuscript: stem-loop aptamers for serotonin (`Kd_molecular` = 30 nM), dopamine (150 nM), glucose (10 mM), S1P (190 nM) from solution-phase SELEX/fluorescence (Fig. 1D–G). Sensing is conformational backbone gating, not analyte charge. `primary-source-supported` for those solution Kd values and FET detection in physiological buffer. Glutamate is **not** one of the four targets. This paper answers “can an aptamer keep up with Debye screening?” not “can it keep up with 1 ms glutamate.”
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** NIHMS manuscript (Europe PMC XML empty; eScholarship green-OA URL returned HTTP 403). Not in vivo. `Kd_molecular` from fluorescence SELEX is not FET `EC50` and not `koff`. Do not transfer dopamine/serotonin aptamer kinetics to glutamate.

---

### S06-11

- **title:** Implantable aptamer-field-effect transistor neuroprobes for in vivo neurotransmitter monitoring
- **year:** 2021
- **journal:** Science Advances
- **authors:** Zhao C; Cheung KM; Huang IW; Yang H; Nakatsuka N; Liu W; Cao Y; Man T; Weiss PS; Monbouquette HG; Andrews AM
- **DOI:** 10.1126/sciadv.abj7422
- **PMID:** 34818033
- **PMCID:** PMC8612678
- **source_type:** primary
- **why it matters for THIS assigned lane:** Closest existence proof that an *aptamer* neurochemical sensor can be implanted and detect stimulated transmitter release in vivo — but the transmitter is serotonin, not glutamate, and the clock is not synaptic milliseconds. Europe PMC XML / PMC: femtomolar `sensor_LOD` for serotonin in brain tissue homogenate; stimulated serotonin detected in vivo; authors cite prior aptamer-FET `response_time` “on the order of seconds”; a gelatin/aCSF addition experiment had a 12-min `response_time` attributed to diffusion over ~0.2 cm, not aptamer binding. `primary-source-supported`. Co-authors include Monbouquette (enzyme glutamate MEAs, S06-07/S06-08), i.e. the same labs already know both architectures. Wildcard: nucleic-acid recognition *plus* implantation is demonstrated; glutamate-specific SELEX + ms transduction is not.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** Serotonin aptamer from the Nakatsuka lineage. Femtomolar LOD in homogenate is `sensor_LOD`, not extracellular `biological_concentration_range`. Seconds-scale FET response does not “keep up” with Clements 1.2 ms. Do not transfer serotonin LOD to glutamate.

---

### S06-12

- **title:** Highly selective and sensitive detection of glutamate by an electrochemical aptasensor
- **year:** 2022
- **journal:** Analytical and Bioanalytical Chemistry
- **authors:** Wu C; Barkova D; Komarova N; Offenhausser A; Andrianova M; Hu Z; Kuznetsov A; Mayer D
- **DOI:** 10.1007/s00216-021-03783-w
- **PMID:** 34783880
- **PMCID:** (empty)
- **source_type:** primary
- **why it matters for THIS assigned lane:** The actual glutamate-*ligand* DNA aptasensor that a glutamate-aptamer poster would have to discuss. PubMed/Springer abstract (publisher flags Full HTML = N): Capture-SELEX in complex medium isolated aptamer **1d04** with `Kd_molecular` 12 µM; truncated surface probe **glu1** (3′-ferrocene, Au–thiol, MCH backfill) characterized by **alternating current voltammetry**; `sensor_LOD` 0.0013 pM; `analytical_working_range` 0.01 pM–1 nM; selectivity claimed in tenfold-diluted human serum. Authors state “great potential” for in vivo monitoring. `primary-source-supported` at abstract level for those named quantities on those named constructs. Wildcard: this is a defined *analytical* use-case (diluted serum ACV), not a demonstrated neurodynamic use-case. 1d04 `Kd_molecular` (12 µM) and glu1 `sensor_LOD` (0.0013 pM) are different quantity types on different constructs; transferring either to synaptic occupancy or to `koff` is forbidden.
- **full_text_inspected:** partial
- **access_route:** html
- **limitation:** Closed full text (Unpaywall `is_oa=False`). ACV `measurement_time` / incubation not in the abstract. No `kon`/`koff`. No in vivo data in the abstract. Springer HTML author list uses Offenhäusser; PubMed AU is Offenhausser. Truncation 1d04→glu1: properties are **not** transferable unless the paper’s own comparison (uninspected full text) shows it.

---

### S06-13

- **title:** Arginine-modified DNA aptamers that show enantioselective recognition of the dicarboxylic acid moiety of glutamic acid
- **year:** 2008
- **journal:** Analytical Sciences
- **authors:** Ohsawa K; Kasamatsu T; Nagashima J; Hanawa K; Kuwahara M; Ozaki H; Sawai H
- **DOI:** 10.2116/analsci.24.167
- **PMID:** 18187867
- **PMCID:** (empty)
- **source_type:** primary
- **why it matters for THIS assigned lane:** Biochemical constraint, not a sensor paper. PubMed/JSTAGE abstract: glutamic-acid binders were screened from a **chemically modified** DNA pool containing arginine residues (17 SELEX rounds); SPR on three sequenced clones; two distinguished D- vs L-dicarboxylic acid, one did not. `primary-source-supported` for modified-DNA SELEX against glutamic acid. Precursor symposium note Kuwahara 2005 (PMID 17150643, DOI 10.1093/nass/49.1.81) describes the same arginine-dUTP library strategy (`partial`/abstract). Wildcard: unmodified polyanionic DNA/RNA vs anionic glutamate is a plausible SELEX difficulty; this paper is evidence that workers used cationic base modifications to bind glutamate, **not** proof that unmodified aptamers cannot exist (Wu 2022 claims an ssDNA 1d04). Fatal-reason hypothesis remains `unresolved`.
- **full_text_inspected:** partial
- **access_route:** html
- **limitation:** JSTAGE full HTML of methods/SPR tables was not obtained (landing + abstract). No `Kd_molecular` number in the abstract; do not invent one. Not a biosensor; no kinetics; not brain. Do not treat enantioselectivity of modified DNA as selectivity of glu1/1d04.

---

### S06-14

- **title:** Aptamer Renaissance for Neurochemical Biosensing
- **year:** 2024
- **journal:** ACS Nano
- **authors:** Stuber A; Nakatsuka N
- **DOI:** 10.1021/acsnano.3c09576
- **PMID:** 38236046
- **PMCID:** PMC10832038
- **source_type:** review
- **why it matters for THIS assigned lane:** OA perspective from an aptamer-FET lab stating the specs the wildcard lane is testing. Europe PMC XML: neurochemical biosensors should be label-free, spatially local, and “real-time monitoring with fast kinetics” to capture dynamic brain processes; FSCV offers millisecond `response_time` but spatial/selectivity trade-offs; genetically encoded optical sensors have their own limits; “Designing aptamers with adequate affinities for certain small molecules has proven difficult.” `review-supported`. Useful as a map, not as primary kinetics. Correction: PMID 38713192 / PMC11112726 (not separately extracted).
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** Perspective, not a glutamate dataset. Do not treat review sentences about “fast kinetics” as measured `koff` of any glutamate aptamer.

---

### S06-15

- **title:** Continuous Real-Time Detection of Serotonin Using an Aptamer-Based Electrochemical Biosensor
- **year:** 2023
- **journal:** Biosensors
- **authors:** Ahmad HMN; Andrade A; Song E
- **DOI:** 10.3390/bios13110983
- **PMID:** 37998158
- **PMCID:** PMC10669129
- **source_type:** primary
- **why it matters for THIS assigned lane:** Counterexample to a naive “aptamers for other neurochemicals already keep up.” Europe PMC XML: electrochemical aptamer serotonin sensor in a microfluidic flow cell; single-frequency EIS `response_time` approximately 1 min to a step change; `analytical_working_range` 25–150 nM in continuous flow; `sensor_LOD` 5.6 nM; cites Nakatsuka serotonin aptamer `Kd_molecular` 30 nM. Aimed at organ-on-chip, not synaptic clefts. `primary-source-supported` for this EIS device. Wildcard: “aptamer” + “real-time” in a title does not imply millisecond or even second-scale neurodynamics; `measurement_time` of the interrogation method can dominate.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** In-vitro buffer/microfluidics, not in vivo. Uses the Nakatsuka serotonin sequence; do not transfer 1 min EIS `response_time` to FET seconds (Zhao) or to a glutamate ACV aptasensor (Wu).

---

## Near-misses (inspected enough to exclude from the 15, or keep as warnings)

| Item | IDs | Why near-miss |
|---|---|---|
| RNA aptamers for AMPA or kainate *receptors* | Huang 2021 PMID 34509496 PMC9284364; Jaremko 2020 PMID 32161119; Ingenito 2025 PMID 40935837; Lee 2014 PMID 24708087; Du 2007 PMID 17588619 | Bind the receptor protein, not L-glutamate. Dominate `"glutamate aptamer"` search noise. |
| Peptide aptamer L-glutamate amperometric sensor | Wang W 2022 PMID 35623273 DOI 10.1016/j.bioelechem.2022.108165 | Closed; **peptide**, not nucleic acid. |
| Bacterial glutamine aptamers/riboswitches | Ames 2011 PMID 21282981 PMC3127080 | Glutamine, not glutamate; PMC HTML retrieved but off-target. |
| Arginine-modified DNA library symposium | Kuwahara 2005 PMID 17150643 | Two-page methods note; parent of Ohsawa 2008. |
| Kinetic mechanisms of iGluSnFR affinity variants | Coates 2020 PMID 31787209 PMC6950763 DOI 10.1016/j.bpj.2019.11.006 | OA; `kon`/`koff` of **protein** indicators (iGlu_h/m/l). Supports S06-04 mechanism; not a new architecture. Full text inspected (PMC HTML). |
| Enzyme MEA in vivo (Venton) | Ganesana 2019 PMID 30731343 PMC6449154 | 50 µm GluOx wire; linear 5–150 µM; `response_time` within 2 s; `sensor_LOD` 0.044 µM; stimulated glutamate in STN slices and in vivo. Redundant with Hascup/Huang/Wassum for the lane. Full text inspected. |
| Enzyme FSCV glutamate+dopamine | Kimble 2023 PMID 37962541 PMC10683757 DOI 10.1021/acssensors.3c01267 | OA; still GluOx; glutamate is nonelectroactive; linear 25 µM–1 mM; `kM` 1.0 ± 0.1 mM (half-maximal current, not `Kd_molecular`). Shows FSCV “glutamate” hits are enzyme-coupled. |
| ATP E-AB in 3D astrocyte culture | Santos-Cancel 2019 PMID 30754968 PMC6469990 | Seconds-scale square-wave voltammetry ATP aptamer in culture media; not glutamate; not in vivo. Full text inspected. |
| Resting-glutamate pharmacology on enzyme MEAs | Hascup ER 2010 PMID 20969570 PMC2996468 | Complements S06-06 (TTX ~40% of resting MEA glutamate in rat PFC). Not listed separately to avoid stacking Gerhardt papers. Full text inspected. |
| iGluSnFR cortical maps | Xie 2016 PMID 26818514 PMC6604822 | Application paper, not a new sensor. |
| Mirror-image L-DNA dopamine in vivo | Liu Y 2026 PMID 41649404 DOI 10.1021/jacs.5c22265 | Crossref/OpenAlex closed; not inspected beyond metadata; dopamine not glutamate. |
| Aptamer-graphene in vivo (bioRxiv) | Wu G 2023 PMID 37905115 PMC10614860 DOI 10.1101/2023.10.18.562080 | Preprint; not glutamate-focused in the title screen. |
| Phenylalanine aptamer FET | Cheung 2019 PMID 31631652 PMC6957227 | Amino-acid aptamer FET, but Phe not Glu. |
| PSMA / PfGDH / prostate “glutamate” aptamer hits | e.g. Singh 2019 PMID 30308419; Campos-Fernández 2021 PMID 33794195 | Enzyme or cancer-antigen targets, not neurotransmitter glutamate. |

## Negative searches (what was actually investigated)

1. **Yarus/Majerfeld glutamate RNA aptamer:** PubMed `Majerfeld glutamate RNA` = 0. `Yarus glutamate aptamer RNA` returned AMPA-receptor and origin-of-life papers, not a glutamate-ligand aptamer. Cannot claim a classical RNA glutamate aptamer from this search.
2. **Unmodified DNA/RNA glutamate aptamer with measured `kon`/`koff`:** not found among the ligand-aptamer hits. Wu 2022 reports `Kd_molecular` for 1d04, not rates. `unresolved`.
3. **Implantable glutamate *aptamer* FET analogous to Zhao 2021 serotonin:** not found in Nakatsuka/Zhao/dopamine-FET searches.
4. **Direct FSCV of glutamate without an enzyme:** literature treats glutamate as nonelectroactive (Kimble 2023 abstract/XML). Hits are enzyme-coupled or dual DA+GluOx.
5. **Fatal proof that glutamate cannot be bound by nucleic acids:** not found. Counter-evidence at abstract level: Wu 2022 1d04; Ohsawa 2008 modified DNA. Anionic-ligand difficulty remains `hypothesis`.
6. **Enzyme sensors matching Clements 1.2 ms as a planar-film t90:** Huang 2020 measures 80 ms and says single-digit-ms chemical tools “have yet to emerge.” Wang 2019 abstract claims submillisecond *exocytosis spikes* on a different electrode; full text closed, so the contradiction is `unresolved` pending extraction.
7. **Single agreed tonic glutamate concentration:** actively contradicted (Herman ~25 nM NMDAR-slice vs Hascup 3.3–5.0 µM oxidase-MEA vs microdialysis 1–4 µM as cited by Herman).

## Identifiers attempted but not verified (or metadata disagreement)

| Attempt | Outcome |
|---|---|
| DOI `10.1523/JNEUROSCI.1991-07.2007` (guessed Herman pattern) | Crossref/OpenAlex/Unpaywall HTTP 404. Correct DOI is `10.1523/JNEUROSCI.3009-07.2007` (PubMed AID + Crossref title match). |
| Europe PMC `fullTextXML` for PMC4469972, PMC2670936, PMC3404456, PMC7117983, PMC6663484, PMC6950763, PMC6469990, PMC3548241, PMC2996468, PMC6449154, PMC3127080 | Empty body (0 bytes). PMC HTML succeeded for the same IDs. |
| Unpaywall/eScholarship green OA for Nakatsuka 2018 (`https://escholarship.org/uc/item/7r0256kf`) | HTTP 403 CloudFront. Used PMC6663484 instead. |
| ACS/Science/J Neurosci publisher HTML (Wang 2019, Clements 1992, Zhao publisher page, Herman J Neurosci `.full`) | Cloudflare “Just a moment…” interstitials (~5–6 KB). Not counted as full text. |
| Wu 2022 Springer: page metadata `"Full HTML":"N"`, `"accessDecision":"NoAccess"` | Abstract extracted from `Abs1-content`; article body not available. |
| Ohsawa 2008 JSTAGE `_html/-char/en` | 19 KB chrome; `_article/-char/en` 83 KB landing/abstract, not SPR tables. |
| PMID 21204381 Hascup book chapter “Second-by-Second Measures of L-Glutamate…” | PubMed summary lacked journal/DOI in esummary; not used as a candidate. |
| PubMed AU vs publisher spelling | Offenhausser vs Offenhäusser (Wu); Durst/Torok vs Dürst/Török (Helassa); Stojanovic vs Stojanović (Nakatsuka). Recorded, not silently “corrected.” |
| iGluSnFR unquoted query `iGluSnFR glutamate sensor OR indicator` | 5,190,786 hits (Boolean explosion). Replaced with `iGluSnFR[Title/Abstract]`. |

## Inference boundary (lane, not poster thesis)

**Measured in the inspected sources**

- Cleft-scale biological clock inferred from NMDA antagonist displacement (Clements abstract).
- Tonic glutamate inferred from NMDAR standing current in slice (~25 nM, Herman).
- Tonic glutamate reported by GluOx MEAs in awake rodents (µM, Hascup).
- Protein-indicator `Kd_molecular`, optical rise/decay, and (Helassa) stopped-flow τ_off.
- Enzyme-film t90 ~80 ms and ~1 s class MEAs used in behavior.
- Aptamer-FET serotonin/dopamine `Kd_molecular` in solution and in vivo serotonin detection with seconds-scale FET response.
- Glutamate DNA aptamer 1d04 `Kd_molecular` 12 µM and glu1 ACV `sensor_LOD` 0.0013 pM (abstract).
- EIS serotonin aptamer `response_time` ~1 min.

**Inferred (not claimed as fact beyond the papers)**

- “Keeping up” is use-case relative: synaptic imaging vs extrasynaptic behavior vs diluted-serum analytics. `hypothesis` at thesis level; each use-case has primary support.
- Enzyme sensors do **not** automatically match 1 ms cleft transients even when they match 1 s behavior. `primary-source-supported` for Huang’s t90 vs Clements’ abstract clock, with Wang 2019 as a possible architecture-specific exception (`unresolved`).
- Aptamers already work in vivo for serotonin (Zhao) and already exist for glutamate as an ACV assay (Wu); those successes are not interchangeable. `primary-source-supported` as separate constructs.

**Unknown / high-information next extraction**

- Full text of Wu 2022: ACV scan time, incubation, 1d04 vs glu1 comparison, serum protocol, any kinetic traces.
- Full text of Wang 2019: how “submillisecond” is defined vs Huang t90.
- `kon`/`koff` for 1d04/glu1: not found. `unresolved`.
- Unmodified vs modified DNA as a glutamate SELEX constraint: Ohsawa vs Wu; needs extraction, not slogan.

**Falsifier for this wildcard reading**

- A glutamate nucleic-acid aptamer, on a named construct, with measured `koff`/`response_time` that tracks synaptic transients in the same preparation used for iGluSnFR3 or Helassa iGlu_u, without transferring Kd from 1d04 or LOD from glu1.

**What this scout is not**

- Not a poster thesis. Not a claim that aptamers cannot work. Not a claim that enzyme sensors “solve” glutamate sensing. Not promotion of any source to `core`.

## Suggested quantity types for later extraction (do not collapse)

| Object | Example from this lane | Type |
|---|---|---|
| Cleft peak / τ | Clements 1.1 mM / 1.2 ms (abstract) | `biological_concentration_range` / biological τ (not sensor `response_time`) |
| Ambient slice glutamate | Herman ~25 nM | `biological_concentration_range` |
| MEA tonic glutamate | Hascup 3.3 / 5.0 µM | `biological_concentration_range` (this architecture) |
| iGluSnFR soluble vs membrane Kd | Marvin 107 µM vs ~4–5 µM | `Kd_molecular` (phase-specific) |
| iGlu_u Kd and τ_off | Helassa 600 µM soluble; τ_off 0.68 ms at 34 °C | `Kd_molecular`, `koff` |
| Enzyme t90 | Huang 0.080 ± 0.012 s to 40 µM | `response_time` |
| Enzyme LOD | Huang 0.70 µM; Hascup 0.9 µM; Ganesana 0.044 µM | `sensor_LOD` |
| 1d04 Kd | Wu 12 µM | `Kd_molecular` |
| glu1 LOD / range | Wu 0.0013 pM; 0.01 pM–1 nM | `sensor_LOD`, `analytical_working_range` |
| Serotonin aptamer Kd | Nakatsuka 30 nM fluorescence | `Kd_molecular` |
| Aptamer FET / EIS clocks | Zhao seconds (12 min diffusion case); Ahmad ~1 min | `response_time` / `measurement_time` |

## Files / integrity

- No PDFs added to git.
- No edits to hash-locked rules, `state/claims.csv`, or core promotion.
- Nominating agent for merge: `literature-scout-06`.
