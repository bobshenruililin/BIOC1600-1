# Literature scout — NEW PRIMARY SOURCES (goal wave A)

Lane: glutamate aptamers; glutamate biosensors (aptamer and non-aptamer comparators); small-molecule aptamer binding kinetics; immobilization effects; in vivo/in vitro glutamate concentration and time regimes.

Status of every record below: **candidate**. Nothing is promoted to `core`. This scout does not write `state/sources.csv` or `state/claims.csv`.

Assigned output shape follows `.cursor/agents/literature-scout.md`. This report does not synthesize a poster thesis.

Scout date: 2026-09-11. Routes: PubMed E-utilities, Europe PMC REST (lite + core), OpenAlex, Crossref, Unpaywall, publisher/PMC HTML. No paid APIs. No Sci-Hub. No PDFs committed to git.

Mission 1 ledger already contains S001–S066 (Wu 2022; Hu 2025/dissertation; Xiao 2025; Abrantes 2025 preprint; Ding & Liu 2024 kinetic ITC; Abeykoon 2025 IPA; Clements 1992; Herman 2007; Rutherford 2007; Clay 2018/2021; iGluSnFR 2013–2023; White 2008 packing density; MacDonald 2019 surface crowding; etc.). Candidates below were chosen because their DOIs/PMIDs are **absent** from `state/sources.csv` as of this checkout.

---

## Search strategy

### Terminology (run as separate queries, then combined)

Glutamate-aptamer discovery and sensors:

- TITLE/TITLE_ABS: `"glutamate aptamer"`, `"glutamic acid aptamer"`, `"L-glutamate aptamer"`, `aptasensor` + glutamate, `"Glu-apt"`, `1d04`, `glu1`, `"NG-Apt-Glu"`, `"Capture-SELEX"` + glutamate/glutamic.
- AUTH: Wu + Mayer + Offenhäusser; AUTH: Hu + Mayer + neurotransmitter + aptamer.
- OpenAlex `cites:W3214487455` (OpenAlex work ID for Wu 2022 DOI `10.1007/s00216-021-03783-w`; Europe PMC `CITES:` syntax returned 0).
- TITLE glutamate AND (aptamer OR aptasensor).
- Negative filters after retrieval: *Plasmodium* glutamate dehydrogenase (Park 2023 / Singh malaria aptasensors); peptide aptamers; iGluR-targeted RNA antagonists.

Kinetics of small-molecule aptamers:

- TITLE_ABS: aptamer AND (`kon` OR `koff` OR `"binding kinetics"` OR `"association rate"`) AND (`"small molecule"` OR theophylline OR ATP OR cocaine OR tobramycin OR glutamate).
- AUTH: Soh + `"aptamer switches"`.
- SPR / NMR / kinetic ITC terms for theophylline, ATP, folate Capture-SELEX.

Immobilization:

- TITLE_ABS: `"packing density"` AND aptamer AND (electrochemical OR `"E-AB"` OR immobilization).
- TITLE_ABS: `"surface crowding"` AND aptamer.
- TITLE: `"Quasi-Reversible Kinetics in Aptamer Self-Assembled Monolayers"`.

Glutamate concentration / time regimes and non-aptamer comparators:

- `"glutamate oxidase"` AND (microelectrode OR biosensor) AND (`"in vivo"` OR millisecond OR `"response time"`).
- TITLE: iGluSnFR4 / `"tailored deactivation"` / `"Imaging extrasynaptic glutamate"`.
- AUTH: Hascup, Diamond, Okubo, Bergles, Scimemi + glutamate + (clearance OR extrasynaptic OR resting OR ambient).
- `"ambient glutamate"` / `"tonic glutamate"` 2005–2026.

### What the searches actually returned (integrity)

| Query | Route | Result used |
| --- | --- | --- |
| TITLE_ABS `"glutamate aptamer"` | Europe PMC | hitCount = 1 (Abrantes preprint only) |
| PubMed Title/Abstract `"glutamate aptamer"` OR `"glutamic acid aptamer"` OR `"L-glutamate aptamer"` OR `"glutamate aptasensor"` | PubMed esearch | count = 0 (too strict; not treated as “no literature”) |
| (glutamate OR `"glutamic acid"`) AND (aptamer OR aptasensor) TITLE_ABS | Europe PMC | hitCount = 58; first page dominated by GDH, poly(glutamate) materials, iGluR aptamers, Wu/Hu already known |
| TITLE glutamate AND (aptamer OR aptasensor) | Europe PMC | hitCount = 6: Abrantes, Wu, Wang peptide, Singh PfGDH ×3 |
| OpenAlex citing Wu 2022 (`W3214487455`) | OpenAlex | 31 citing works; source of Wang 2024, Liu 2025, Hu TrAC 2023, Robbins-adjacent enzyme papers, Abrantes, Tabrizi enzymatic microneedle |
| Europe PMC `CITES:10.1007/s00216-021-03783-w` | Europe PMC | hitCount = 0 (syntax failure, not a scientific negative) |
| Unpaywall Wu 2022 | Unpaywall | `is_oa = false` (confirms Mission 1 closed VoR) |
| Unpaywall Wang 2024 | Unpaywall | hybrid CC-BY; Wiley HTML/PDF not retrieved in this environment (cookie/HTML stub) |

---

## Negative search and near-misses

**No new primary nucleic-acid SELEX of a free-glutamate aptamer was verified beyond the Wu 2022 family.** Hu 2025 (S002) and the Hu dissertation (S066) reuse a truncated Wu sequence. Abrantes 2025 (S010) computationally trims the 98-nt `glu1d04` sequence. Xiao 2025 (S021) reports an SPR Kd of 293 nM for a glutamate aptamer whose sequence is in SI, not independently re-selected in a second inspected paper. Ohsawa 2008 (S008) remains the modified-DNA / avidin-conjugate negative case.

Near-misses inspected and **not** nominated as glutamate-aptamer sensors:

- Jergova et al. 2025 *Commun Biol* DOI `10.1038/s42003-025-08772-8` PMID 41006757 PMC12475499 — RNA aptamers targeting **ionotropic glutamate receptors**, not free glutamate.
- Ingenito et al. 2025 *Sci Rep* DOI `10.1038/s41598-025-15323-y` PMID 40935837 PMC12426214 — GluK2-selective RNA aptamer (receptor, not ligand).
- Wang et al. 2022 *Bioelectrochemistry* DOI `10.1016/j.bioelechem.2022.108165` PMID 35623273 — peptide aptamer (already S013, rejected as non-nucleic-acid).
- Singh et al. malaria PfGDH aptasensors (PMID 29909195, 30308419, 29722521) — protein target named glutamate dehydrogenase, not neurotransmitter glutamate.
- Mettee et al. 2025 *Sensors* DOI `10.3390/s25144326` PMID 40732453 PMC12298936 — magnetite MRI contrast, not an aptamer.
- Tabrizi 2023 *Biosensors* DOI `10.3390/bios13080828` PMID 37622914 PMC10452303 — enzymatic microneedle glutamate; cites Wu but does not add an aptamer construct.
- Adediji et al. 2025 *Front Neurosci* DOI `10.3389/fnins.2025.1679591` PMID 41048356 PMC12491176 — enzyme Glu/GABA sensitivity via Pt roughening; incremental vs Robbins/Doughty, so not in the 14.
- Xie & Liu 2026 *ChemBioChem* DOI `10.1002/cbic.70393` PMID 42179008 — Capture-SELEX for **folate**, method cousin of Wu, not glutamate.
- Hariri et al. 2024 *Adv Mater* DOI `10.1002/adma.202304410` PMID 37975267 — modular aptamer switches in complex media (ATP-class); overlapping with Wilson 2019, not glutamate.
- Ritz et al. 2024 *ACS Appl Bio Mater* DOI `10.1021/acsabm.3c01254` PMID 38369768 — gold morphology for E-AB; closed VoR; immobilization-relevant but ATP/kanamycin-class, not glutamate.
- Crossref hit `10.26686/wgtn.27323574` (Wellington thesis title containing “free amino acids” E-AB) — not verified as a journal article; not nominated.
- bioRxiv/other preprint `10.64898/2026.06.12.731919` (“Ratiometric iGluSnFR imaging to assess tonic glutamate”) — unusual DOI prefix; not promoted without journal metadata.
- Hu, Li, Figueroa-Miranda et al. 2023 *TrAC* DOI `10.1016/j.trac.2023.117021` — neurotransmitter aptamer **review** that cites Wu (OpenAlex). Crossref verifies DOI/authors/year. Europe PMC DOI query hitCount = 0; PubMed title search returned 0 PMIDs. Closed (Unpaywall `is_oa = false`). **PMID left empty.** Not listed among the 14 because the glutamate-specific OA review Wang 2024 covers the same comparator map with a verified PMID.

---

## Identifiers attempted but not verified

| Attempt | Outcome |
| --- | --- |
| PMID for Hu *TrAC* 2023 DOI `10.1016/j.trac.2023.117021` | Crossref and OpenAlex agree on DOI; PubMed title search count = 0; Europe PMC DOI search hitCount = 0. PMID empty. |
| Europe PMC `CITES:` Wu 2022 DOI | 0 hits; citing set recovered via OpenAlex work ID `W3214487455` (31 works). |
| Wiley VoR HTML/PDF for Wang 2024 despite Unpaywall CC-BY | This environment received a 5–6 kB cookie stub, not the article. Abstract used; VoR not inspected. |
| PMC OAI full text for Okubo PMC2851965, Diamond PMC6725141, Bergles PMC25121 | OAI GetRecord returned 478-byte errors; NCBI PMC HTML succeeded for all three. |
| Peer-reviewed journal version of Abrantes NG-Apt-Glu | OpenAlex citing list and Europe PMC still show only bioRxiv `10.1101/2025.11.05.686731` (already S010). |
| Glutamate aptamer `kon`/`koff` | No verified glutamate-aptamer kinetic paper. Chang, Latham, Wilson, Ding/Liu (S003), Abeykoon (S004) remain non-glutamate. |

---

## Candidates (14)

### C1. Aggarwal et al. 2026 — iGluSnFR4f / iGluSnFR4s

- **title:** Glutamate indicators with increased sensitivity and tailored deactivation rates
- **year:** 2026
- **journal:** Nature Methods
- **authors:** Aggarwal Abhi; Negrean Adrian; Chen Yang; Iyer Rishyashring; Reep Daniel; Liu Anyi; Palutla Anirudh; Xie Michael E.; MacLennan Bryan J.; Hagihara Kenta M.; Kinsey Lucas W.; Sun Julianna L.; Yao Pantong; Zheng Jihong; Tsang Arthur; Tsegaye Getahun; Zhang Yonghai; Patel Ronak H.; Arthur Benjamin J.; Hiblot Julien; Leippe Philipp; Tarnawski Miroslaw; Marvin Jonathan S.; Vevea Jason D.; Turaga Srinivas C.; Tebo Alison G.; Carandini Matteo; Rossi L. Federico; Kleinfeld David; Konnerth Arthur; Svoboda Karel; Turner Glenn C.; Hasseman Jeremy P.; Podgorski Kaspar
- **DOI:** 10.1038/s41592-025-02965-z
- **PMID:** 41436654
- **PMCID:** PMC12904790
- **source_type:** primary
- **why it matters for THIS assigned lane:** Mission 1 already has iGluSnFR (S058), affinity variants (S059), Helassa iGluu (S060), and iGluSnFR3 (S061). This is the fourth-generation pair with **engineered deactivation**: the discussion states iGluSnFR4f deactivation 26 ms and iGluSnFR4s 153 ms, with rise times <2 ms for single-AP axonal transients in vivo. The introduction states that one AP typically releases a few thousand glutamate molecules that are “cleared from the synaptic cleft in less than 1 ms” (citation, not a new chemical assay). That split — indicator deactivation vs free-glutamate lifetime — is the optical-comparator clock the poster still lacks after iGluSnFR3.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** Protein fluorescent indicator, not an aptamer. Deactivation times are sensor properties (`response_time` of the indicator), not `koff` of a nucleic-acid receptor and not the biological clearance time. Soluble-protein titrations in Extended Data are not transferred here. Preprint DOI `10.1101/2025.03.20.643984` is the same work; use the VoR.

### C2. Yang et al. 2023 — functional-group-guided small-molecule aptamers (glutamate called out)

- **title:** A functional group–guided approach to aptamers for small molecules
- **year:** 2023
- **journal:** Science
- **authors:** Yang Kyungae; Mitchell Noelle M.; Banerjee Saswata; Cheng Zhenzhuang; Taylor Steven; Kostic Aleksandra M.; Wong Isabel; Sajjath Sairaj; Zhang Yameng; Stevens Jacob; Mohan Sumit; Landry Donald W.; Worgall Tilla S.; Andrews Anne M.; Stojanovic Milan N.
- **DOI:** 10.1126/science.abn9859
- **PMID:** 37262137
- **PMCID:** PMC10686217
- **source_type:** primary
- **why it matters for THIS assigned lane:** Primary SELEX/characterization of 27 target–aptamer pairs, including amino acids. The inspected PMC author manuscript states that a Cu(II)-cofactor amino-acid strategy “would not work for amino acids that carry a chelating group beyond 2-aminoethanoate, e.g., glutamate.” That is a **construct-level reason glutamate is a hard SELEX target**, independent of Wu’s Capture-SELEX success. It is not a Kd for 1d04/glu1.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** The glutamate sentence is a negative-design statement, not a glutamate aptamer measurement. Do not transfer leucine/phenylalanine affinities onto glutamate. VoR is Science; inspected text is the PMC author manuscript (Unpaywall also lists a green submitted PDF).

### C3. Wilson et al. 2019 — independent control of aptamer-switch thermodynamics and kinetics

- **title:** Independent control of the thermodynamic and kinetic properties of aptamer switches
- **year:** 2019
- **journal:** Nature Communications
- **authors:** Wilson Brandon D.; Hariri Amani A.; Thompson Ian A. P.; Eisenstein Michael; Soh H. Tom
- **DOI:** 10.1038/s41467-019-13137-x
- **PMID:** 31699984
- **PMCID:** PMC6838323
- **source_type:** primary
- **why it matters for THIS assigned lane:** Mission 1 kinetics papers (Ding/Liu ITC; Abeykoon IPA; Plaxco interrogation-time ladder) do not include a design that **decouples Kd from temporal response**. This intramolecular strand-displacement (ISD) ATP aptamer-switch paper shows that displacement-strand length and linker length tune `KDeff` and `kobs` separately from the parent aptamer’s `KDapt`/`konapt`/`koffapt`. If the poster treats “aptamer speed” as locked to affinity, this is the counterexample architecture (still not glutamate).
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** ATP switch in solution fluorescence, not glutamate, not surface E-AB. Parent aptamer kinetics remain fixed; only the switch module is tuned. Sequences with `LDS = 5` were faster than the detector and were omitted from some kinetic panels.

### C4. Chang et al. 2014 — SPR kon/koff panel for small-molecule aptamers

- **title:** Kinetic and equilibrium binding characterization of aptamers to small molecules using a label-free, sensitive, and scalable platform
- **year:** 2014
- **journal:** Analytical Chemistry
- **authors:** Chang Andrew L.; McKeague Maureen; Liang Joe C.; Smolke Christina D.
- **DOI:** 10.1021/ac5001527
- **PMID:** 24548121
- **PMCID:** PMC3983011
- **source_type:** primary
- **why it matters for THIS assigned lane:** Mission 1’s small-molecule kinetic envelope is Ding/Liu ITC (S003, abstract-only) plus tobramycin E-AB IPA (S004). Chang reports a **surface SPR** 1:1 kinetic fit for the theophylline RNA aptamer: `ka` (1.5 ± 0.1) × 10^5 M^−1 s^−1, `kd` 0.063 ± 0.004 s^−1, `KD` 430 ± 40 nM, plus a 12-aptamer table spanning pM–µM `KD` under one platform. That is a primary, same-method kinetic atlas for occupancy-clock bounds — still not glutamate.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** Aptamers are captured by a poly(A)/poly(T) linker on a CM5 chip (`surface-bound`, not the Wu/Hu gold/MCH E-AB). No glutamate row. Do not treat theophylline `ka` as a glutamate `kon`.

### C5. Latham, Zimmermann & Pardi 2009 — folding-limited apparent kon

- **title:** NMR chemical exchange as a probe for ligand-binding kinetics in a theophylline-binding RNA aptamer
- **year:** 2009
- **journal:** Journal of the American Chemical Society
- **authors:** Latham Michael P.; Zimmermann Grant R.; Pardi Arthur
- **DOI:** 10.1021/ja900695m
- **PMID:** 19317486
- **PMCID:** PMC2752443
- **source_type:** primary
- **why it matters for THIS assigned lane:** ZZ-exchange NMR in **zero Mg2+** gives apparent `kon` = 600 ± 57 M^−1 s^−1 because the free RNA is mostly inactive (conformational selection). With Mg2+, literature Kd is ~300 nM (cited, not remeasured here as a kinetic). This is the primary experiment that falsifies a blanket “diffusion-limited kon” assumption for small-molecule aptamers — directly relevant to Mission 1 open question on occupancy-clock `kon` priors.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** Theophylline RNA, not glutamate DNA. Apparent `kon` is condition-specific (no Mg2+, 15 °C). Do not transfer 600 M^−1 s^−1 onto glu1/Hu Glu-apt.

### C6. Wang, Yang, Chen & Li 2024 — miniaturized electrochemical glutamate platforms (review)

- **title:** Miniaturized electrochemical sensing platforms for quantitative monitoring of glutamate dynamics in the central nervous system
- **year:** 2024
- **journal:** Angewandte Chemie International Edition
- **authors:** Wang Qi; Yang Chunyu; Chen Shulin; Li Jinghua
- **DOI:** 10.1002/anie.202406867
- **PMID:** 38829963
- **PMCID:** (empty — not in Europe PMC as PMC)
- **source_type:** review
- **why it matters for THIS assigned lane:** Glutamate-specific electrochemical review (enzyme, nanomaterial, and, per OpenAlex, a Wu 2022 citation). Abstract: real-time continuous monitoring of glutamate concentration and dynamics in living organisms; co-design of materials for electrochemical glutamate sensors. Mission 1 has no 2024 glutamate-sensor review that maps aptamer vs GlutOx vs other electrochemical architectures onto CNS timescales.
- **full_text_inspected:** no
- **access_route:** abstract-only
- **limitation:** Unpaywall reports hybrid CC-BY publishedVersion at Wiley; this scout retrieved only the Europe PMC abstract (Wiley HTML/PDF stub). Treat claims as abstract-level until VoR is inspected. Review, not a new aptamer.

### C7. Liu, Liu, Yin & Tian 2025 — electrochemical glutamate at cleft edge vs peri-soma

- **title:** Electrochemical sensor toolkit for simultaneous glutamate detection at edge of cleft and peri-soma
- **year:** 2025
- **journal:** Cell Chemical Biology
- **authors:** Liu Jie; Liu Yuandong; Yin Dongmin; Tian Yang
- **DOI:** 10.1016/j.chembiol.2025.05.002
- **PMID:** 40466640
- **PMCID:** (empty)
- **source_type:** primary
- **why it matters for THIS assigned lane:** Abstract: electrochemical toolkit with spatial resolution of ~60 nm using a **biologically engineered glutamate-binding protein** plus ferrocene labels; simultaneous readout at “edge of synaptic cleft” and peri-soma; conjugation chemistry claimed to improve sensitivity up to 32-fold. OpenAlex lists it as citing Wu 2022. This is a non-aptamer comparator that claims **cleft-adjacent** electrochemical glutamate — the spatial claim Mission 1’s aptamer devices (MEA, retina probe) do not make.
- **full_text_inspected:** no
- **access_route:** abstract-only
- **limitation:** Unpaywall `is_oa = false`. Protein receptor, not nucleic-acid aptamer. “Edge of cleft” is the authors’ spatial claim in the abstract; geometry and calibration were not inspected. Do not transfer their sensitivity fold-change onto Hu/Wu devices.

### C8. Robbins et al. 2024 — chronic in vivo GlutOx on nanoPt

- **title:** Improving sensitivity and longevity of in vivo glutamate sensors with electrodeposited NanoPt
- **year:** 2024
- **journal:** ACS Applied Materials & Interfaces
- **authors:** Robbins Elaine M.; Wong Benjamin; Pwint May Yoon; Salavatian Siamak; Mahajan Aman; Cui Xinyan Tracy
- **DOI:** 10.1021/acsami.4c06692
- **PMID:** 39078097
- **PMCID:** PMC11310907
- **source_type:** primary
- **why it matters for THIS assigned lane:** Primary **in vivo** glutamate oxidase MEA comparator after Rutherford 2007 (S054). Inspected PMC HTML: GlutOx + H2O2 oxidation is described as the in vivo gold standard; almost no chronic glutamate sensing despite weeks of in vitro life; smooth Pt sensors failed after 3 days in vivo; nanoPt used in rat striatum after TBI and for simultaneous GLU/GABA on an MEA. Calibrations in the inspected text use 10 µM–1 mM glutamate standards.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** Enzyme electrode, not aptamer. In vivo failure mode is enzyme/H2O2/Pt, not nucleic-acid unfolding. Do not treat 10 µM–1 mM calibration span as a biological concentration range.

### C9. Doughty et al. 2020 — replaceable microwire Glu + GABA in vitro and in vivo

- **title:** Novel microwire-based biosensor probe for simultaneous real-time measurement of glutamate and GABA dynamics in vitro and in vivo
- **year:** 2020
- **journal:** Scientific Reports
- **authors:** Doughty P. Timothy; Hossain Imran; Gong Chenggong; Ponder Kayla A.; Pati Sandipan; Arumugam Prabhu U.; Murray Teresa A.
- **DOI:** 10.1038/s41598-020-69636-1
- **PMID:** 32728074
- **PMCID:** PMC7392771
- **source_type:** primary
- **why it matters for THIS assigned lane:** Enzyme Glu + reagent-free GABA on a **replaceable** microwire for slice and in vivo use. Inspected text: stimulation-evoked Glu/GABA peaks have rise, decay, and FDHM reported in **seconds** (Fig. 6/9); FAST-16 MkIII amperometry at +0.7 V. This is a documented in vivo glutamate **phasic** electrochemical comparator whose time base is seconds, not milliseconds — the same order as Hu ACV point spacing (S066, 14 s/1 min), not Clements’ 1.2 ms.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** Enzyme, not aptamer. Peak times are stimulation-evoked extracellular transients filtered by enzyme/diffusion, not synaptic-cleft free glutamate. Linear-range numbers in Fig. 2 were not copied here without a second pass on the figure table.

### C10. Hascup et al. 2010 — origin of resting extracellular glutamate on GlutOx MEAs

- **title:** Rapid microelectrode measurements and the origin and regulation of extracellular glutamate in rat prefrontal cortex
- **year:** 2010
- **journal:** Journal of Neurochemistry
- **authors:** Hascup Erin R.; Hascup Kevin N.; Stephens Michelle; Pomerleau Francois; Huettl Peter; Gratton Alain; Gerhardt Greg A.
- **DOI:** 10.1111/j.1471-4159.2010.07066.x
- **PMID:** 20969570
- **PMCID:** PMC2996468
- **source_type:** primary
- **why it matters for THIS assigned lane:** Awake-rat PFC, enzyme MEA, second-by-second resting glutamate. Inspected NIHPA XML: resting glutamate for the Long Evans rats in this study **34.7 µM ± 11.8 µM (n = 41)**; local TTX produced a ~40% decline; authors conclude 40–50% of the MEA resting signal is neuronal. This is a primary **biological_concentration_range** that sits orders of magnitude above Herman 2007 ambient ~25 nM (S050) and in the same method family as Rutherford 2007 (S054). Occupancy-at-basal for any glutamate receptor (aptamer or enzyme) is not the same number in these two experimental systems.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** GlutOx MEA resting micromolar values are not NMDAR-inferred ambient nanomolar values. Do not average them. Dialysis comparison in the paper is literature, not a new dialysis assay. Not an aptamer.

### C11. Okubo et al. 2010 — extrasynaptic glutamate imaging (EOS)

- **title:** Imaging extrasynaptic glutamate dynamics in the brain
- **year:** 2010
- **journal:** Proceedings of the National Academy of Sciences
- **authors:** Okubo Yohei; Sekiya Hiroshi; Namiki Shigeyuki; Sakamoto Hirokazu; Iinuma Sho; Yamasaki Miwako; Watanabe Masahiko; Hirose Kenzo; Iino Masamitsu
- **DOI:** 10.1073/pnas.0913154107
- **PMID:** 20308566
- **PMCID:** PMC2851965
- **source_type:** primary
- **why it matters for THIS assigned lane:** Hybrid AMPAR-based fluorescent indicator EOS, mostly extrasynaptic. Inspected NCBI PMC HTML: K716A-EOS Kd = 174 nM; L401C-EOS Kd = 1.57 µM (indicator affinities, not biological concentrations). Deconvolution of L401C-EOS (assuming first-order indicator kinetics) gives extrasynaptic transients that “reached micromolar concentrations for tens of milliseconds”; **average 1–8 µM within a 50-ms window** after 2–5 pulses at 100 Hz (Fig. 4C–D). Also in vivo sensory-evoked extrasynaptic signals in cortex. This is a **third concentration/time compartment** between Clements’ cleft peak (S049) and Herman tonic nanomolar (S050).
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** EOS is a protein/small-molecule hybrid indicator; deconvolution assumes first-order association. Concentrations are extrasynaptic estimates after stimulation, not aptamer occupancy. Indicator Kd must not be used as LOD or as biological [Glu].

### C12. Diamond 2005 — extrasynaptic glutamate clearance time course

- **title:** Deriving the glutamate clearance time course from transporter currents in CA1 hippocampal astrocytes: transmitter uptake gets faster during development
- **year:** 2005
- **journal:** The Journal of Neuroscience
- **authors:** Diamond Jeffrey S.
- **DOI:** 10.1523/jneurosci.5125-04.2005
- **PMID:** 15772350
- **PMCID:** PMC6725141
- **source_type:** primary
- **why it matters for THIS assigned lane:** Astrocytic synaptically activated transporter currents (STCs) in rat CA1 slices; deconvolution to recover clearance, not just the filtered STC. Inspected NCBI PMC HTML: “glutamate can be cleared from the extrasynaptic space **within 1 ms**. Clearance is fastest in adult neuropil.” Adult STCs are faster than P12–P14. This is the clearance clock that Armbruster 2020 (S062) later contrasts with iGluSnFR waveforms. Mission 1 did not ledger this primary.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** Clearance inferred from transporter currents plus a filter model, not a chemical glutamate assay. Temperature, age, and TBOA conditions are specific. Monte Carlo diffusion in the paper is a simulation (label as such if used). Not an aptamer.

### C13. Bergles, Dzubay & Jahr 1997 — extrasynaptic glutamate time course at Bergmann glia

- **title:** Glutamate transporter currents in Bergmann glial cells follow the time course of extrasynaptic glutamate
- **year:** 1997
- **journal:** Proceedings of the National Academy of Sciences
- **authors:** Bergles Dwight E.; Dzubay Jeffrey A.; Jahr Craig E.
- **DOI:** 10.1073/pnas.94.26.14821
- **PMID:** 9405697
- **PMCID:** PMC25121
- **source_type:** primary
- **why it matters for THIS assigned lane:** Outside-out patches: transporter currents activate in **<1 ms**. Climbing-fiber-evoked glial AMPA and transporter currents imply glutamate escapes the cleft and reaches glia shortly after release. Comparison with patch concentration–response: extrasynaptic glutamate at Bergmann glial membranes **reaches a lower concentration than the cleft and remains elevated for many milliseconds**. Together with Clements (cleft) and Diamond (clearance ≤1 ms in CA1 adult), this is a primary extrasynaptic **dwell-time** measurement in cerebellum.
- **full_text_inspected:** yes
- **access_route:** pmc
- **limitation:** Cerebellar climbing fiber / Bergmann glia, not hippocampus or cortex. Transporter/AMPA kinetics as reporters, not a glutamate aptamer. “Many milliseconds” is qualitative in the inspected opening; do not invent a single tau.

### C14. Shojaee et al. 2026 — quasi-reversible kinetics in aptamer SAMs

- **title:** Voltammetric analysis of quasi-reversible kinetics in aptamer self-assembled monolayers: toward rational E-AB sensor design
- **year:** 2026
- **journal:** ACS Sensors
- **authors:** Shojaee Maryam; Liu Yu; Cass Anthony; Wu Zixuan; Ashraf Adnan; Napoli Francesca; Patel Neel; Liang Shaolin
- **DOI:** 10.1021/acssensors.5c03661
- **PMID:** 41988853
- **PMCID:** (empty)
- **source_type:** primary
- **why it matters for THIS assigned lane:** Immobilization lane after White 2008 packing density (S033) and MacDonald 2019 surface crowding (S038). Abstract: E-AB sensors are surface-bound systems whose **electron-transfer kinetics are quasi-reversible on typical measurement timescales**; voltammetric characterization of an aptamer SAM aimed at rational E-AB design. That is a different immobilization observable (ET rate vs packing density vs apparent Kd).
- **full_text_inspected:** no
- **access_route:** abstract-only
- **limitation:** Unpaywall `is_oa = false`. Abstract does not name glutamate. Electron-transfer kinetics ≠ binding `kon`/`koff`. Do not transfer SAM ET rates onto Hu Glu-apt ACV wait times.

---

## Lane coverage of this scout (candidates only)

| Lane | New candidates | Still empty after this search |
| --- | --- | --- |
| Glutamate nucleic-acid aptamer SELEX / sequence | C2 (Yang: glutamate as a failed/hard amino-acid class); no new SELEX hit | Independent glutamate aptamer with measured `kon`/`koff` |
| Glutamate aptamer sensors | none new (Wu/Hu/Xiao/Abrantes already ledgered) | Peer-reviewed in vivo glutamate **aptamer** sensor |
| Small-molecule aptamer kinetics | C3, C4, C5 | Glutamate-specific kinetics |
| Immobilization | C14 (abstract); Yang/Chang are surface assays of other targets | Glutamate aptamer surface vs solution Kd on the same construct |
| Concentration / time regimes | C1, C7, C10, C11, C12, C13 | Single agreed basal extracellular [Glu] |
| Non-aptamer glutamate biosensor comparators | C6, C7, C8, C9, C10 | — |

---

## The 5 sources most likely to change the poster’s scientific story

1. **Hascup 2010 (C10)** — If the poster’s occupancy-at-basal story uses Herman 2007 ~25 nM as “the” extracellular glutamate, this MEA resting value (34.7 ± 11.8 µM, n = 41, awake PFC, ~40% TTX-sensitive) is a primary experimental counter-range from the same enzyme-electrode family the poster already treats as a temporal gold standard (Rutherford S054). The story has to name **which extracellular compartment and method**, not a single basal number.

2. **Okubo 2010 (C11)** — Adds an extrasynaptic stimulated regime (about 1–8 µM averaged over 50 ms; micromolar for tens of milliseconds) between Clements’ cleft millimolar/millisecond inference and tonic nanomolar. A glutamate aptamer can “keep up” with one of these and fail the others. That three-regime map is not in the Mission 1 source table.

3. **Yang 2023 (C2)** — Primary SELEX paper that explicitly flags glutamate’s extra chelating carboxylate as a reason a successful amino-acid aptamer strategy does not transfer. The poster’s scarcity of glutamate aptamers is then a **chemical-selection fact**, not only a “we didn’t look” fact — without conferring Wu’s 12 µM Kd on any other construct.

4. **Latham 2009 (C5)** — Apparent `kon` of 600 M^−1 s^−1 for a canonical small-molecule RNA aptamer when the free fold is mostly inactive. Occupancy clocks that assume diffusion-limited association are then a **hypothesis**, not a bound, until glutamate-aptamer `kon` is measured on the same construct and conditions.

5. **Aggarwal 2026 (C1)** — Best current optical comparator: iGluSnFR4f/4s deactivate in 26 ms / 153 ms while the same paper restates cleft clearance <1 ms. The poster can no longer say “protein glutamate sensors are millisecond-class, aptamers are not” as a single contrast; the optical tools are **tuned**, still slower than free glutamate, and still not nucleic acids. That is the honest comparator for “can an aptamer keep up with neurochemical signaling.”
