---
cursor:
  subagentId: "bc-f0fc0882-2a70-56fb-adde-acee542a7826"
---

# Round 1 literature scout 02 — binding kinetics

**Scout:** literature-scout 2 of 6  
**Lane (search focus, not a conclusion):** binding kinetics of glutamate aptamers and closely related small-molecule aptamers — `kon`, `koff`, `response_time` vs `measurement_time`, and whether kinetics were measured on the same construct used in a sensor.  
**Round:** 1 — candidates only; nothing promoted to `core`.  
**Status of all sources below:** `candidate`.  
**Date of searches:** 2026-09-11.  
**Routes used:** PubMed E-utilities, Europe PMC REST, Crossref REST, OpenAlex, Unpaywall (email `bioc1600-scout@example.org`), publisher/PMC/bioRxiv HTML. No Sci-Hub, no paid APIs, no PDFs written into git.

This record does **not** synthesize a poster thesis. Quantity types are not collapsed. Properties are not transferred across constructs, surfaces, or buffers unless the cited experiment used that same system.

## Assigned question (context only)

Can an aptamer keep up with neurochemical signaling? This lane asks only whether glutamate (and closely related small-molecule) aptamers have measured `kon`/`koff`, how sensor `response_time` relates to electrochemical/FET `measurement_time`, and whether those rates were collected on the sensor construct itself.

---

## Search strategy (negative-search integrity)

Phrase and field searches that treat “glutamate” as a neurotransmitter are dominated by false positives (glutamate dehydrogenase malaria antigens, PSMA/prostate, AMPA/kainate *receptor* aptamers, poly(glutamic acid) coatings). Queries that actually isolate L-glutamate *aptamers* are sparse.

| Query | Route | Result (this session) |
| --- | ---: | --- |
| `(glutamate OR glutamic) AND aptamer AND (kinetics OR kon OR koff OR SPR OR ITC OR stopped-flow)` | PubMed | 8 hits; **none** were L-glutamate oligonucleotide aptamer `kon`/`koff` papers (false positives: exosomes, PSMA, *P. falciparum* GDH, AMPA-receptor aptamer) |
| `"glutamate aptamer"[Title/Abstract]` and related phrases | PubMed | 130 hits; after title screening, true L-glutamate NA-aptamer sensors were Wu PMID 34783880, Hu PMID 40992279, plus peptide-aptamer Wang PMID 35623273 and many GDH/PSMA contaminants |
| `TITLE_ABS:"glutamate aptamer" AND (kinetics OR kon OR koff OR SPR OR ITC)` | Europe PMC | 1 hit: Abrantes bioRxiv 10.1101/2025.11.05.686731 |
| `("1d04" OR glu1 OR "glu1d04" OR "NG-Apt-Glu") AND aptamer AND (kinetics OR koff OR kon OR SPR OR ITC)` | Europe PMC | 9 hits; none reported `kon`/`koff` for those glutamate sequences |
| `OPEN_ACCESS:Y AND ((glutamate aptamer) AND (koff OR "association rate constant"))` | Europe PMC | 30 hits; titles inspected were not glutamate-aptamer binding kinetics |
| `interceptive pulsed amperometry OR "intermittent pulse amperometry" aptamer` | PubMed | 3 hits: PMID 38709872 (NPY, not kinetics of glutamate), **29762016**, **41231675** |
| `Ding Liu aptamer calorimetry` / kinetic ITC | PubMed | 22 hits; load-bearing small-molecule kinetic ITC is PMID **38785220** |
| `(tobramycin OR cocaine OR ATP OR theophylline OR dopamine) AND aptamer AND (koff OR "dissociation rate")` | PubMed | 3 hits: 30280568, 12614150, 41231675 |
| `aptamer AND glutamate AND (ITC OR SPR OR BLI OR MST)` | PubMed | 5 hits; true glutamic-acid SPR is Ohsawa PMID 18187867 (modified DNA, enantiomer SELEX); others false positive |
| OpenAlex search `glutamate aptamer binding kinetics` | OpenAlex | noisy review set; did not surface a glutamate `kon`/`koff` primary paper |
| Works citing Wu DOI 10.1007/s00216-021-03783-w | OpenAlex `cites:` filter | returned 0 (query failure; Crossref `is-referenced-by-count` for Wu is 32). Not treated as a negative scientific result |

**Near-misses inspected and not nominated in the 15-candidate set**

- Wang et al. PMID 35623273, DOI 10.1016/j.bioelechem.2022.108165 — *peptide* (not nucleic-acid) aptamer amperometric L-glutamate sensor; closed VoR; no abstract `kon`/`koff`.
- Ohsawa et al. PMID 18187867, DOI 10.2116/analsci.24.167 — arginine-modified DNA aptamers vs glutamic acid enantiomers; SPR in abstract; closed VoR; not the Wu/glu1 neurotransmitter-sensor lineage.
- Kuwahara et al. PMID 17150643 — 2005 symposium note on the same modified-DNA glutamic-acid selection.
- Morris et al. PMID 30280568 — cocaine *split*-aptamer single-molecule `koff` on glass; closed VoR.
- Sulliger et al. PMID 41504417, PMC12825375 — droplet FRET kinetics of *serotonin* stem-length variants; glutamate not studied; full PMC HTML inspected.
- Nakatsuka et al. PMID 30190311, PMC6663484 — dopamine/serotonin/glucose/S1P aptamer-FETs; `response_time` “on the order of seconds” (fig. S6 in the PMC HTML); **glutamate is not a target in this paper**.
- Arroyo-Currás et al. PMID 28069939, PMC5278471 — in-vivo E-AB, ~3 s SWV `measurement_time`, tobramycin/kanamycin/doxorubicin; glutamate appears only as a *comparator literature* neurotransmitter, not an aptamer target.
- Hu et al. PMID 37754115, PMC10527390 — truncated *serotonin* E-AB (same Mayer group as Wu/Hu glutamate papers); truncation/immobilization analog, not glutamate kinetics.

**Load-bearing negative finding (tagged, not a thesis):** no free-route source inspected in this scout reported numerical `kon` or `koff` for glutamate aptamer constructs `1d04`, `glu1`, `glu1d04`, or `NG-Apt-Glu`. Tag: `unresolved` (absence of a measured rate is not proof that the rate is slow or fast).

---

## Candidates (n = 15)

### C02-01 — Wu et al., glutamate Capture-SELEX + truncated E-AB sensor

- **title:** Highly selective and sensitive detection of glutamate by an electrochemical aptasensor
- **year:** print 2022 (Anal. Bioanal. Chem. 414(4):1609–1622); online 2021-11-16. PubMed date “2022 Feb”. Do not collapse online/print.
- **journal:** Analytical and Bioanalytical Chemistry
- **authors:** Changtong Wu; Daria Barkova; Natalia Komarova; Andreas Offenhäusser; Mariia Andrianova; Ziheng Hu; Alexander Kuznetsov; Dirk Mayer
- **DOI:** 10.1007/s00216-021-03783-w
- **PMID:** 34783880
- **PMCID:** empty (PubMed and Europe PMC: none)
- **source_type:** primary
- **why it matters for this lane:** This is the Capture-SELEX origin of ssDNA aptamer `1d04` and the truncated, ferrocene-labelled, thiol-immobilized sensor construct `glu1` used for ACV glutamate sensing. The abstract reports a dissociation constant for `1d04` and a `sensor_LOD` / `analytical_working_range` for surface-bound `glu1`. It is the construct chain later papers truncate or multiplex. No `kon`/`koff` appear in the PubMed or Springer-landing abstract.
- **full_text_inspected:** no
- **access_route:** abstract-only (Unpaywall `is_oa=false` / `oa_status=closed`; Springer HTML is a paywall landing page with abstract + figure thumbnails; OpenAlex `any_repository_has_fulltext=false`)
- **limitation:** VoR not inspectable on free routes, so the **method** behind the `1d04` 12 µM dissociation constant is not verified here (ITC vs fluorescence vs other remains `unresolved`). `1d04` (selection construct) is not the same object as truncated surface-bound `glu1`. `Kd_molecular` of `1d04` is not transferable to `glu1` `sensor_LOD` or ACV working range. `transferable`: no.

**Tagged claims from inspectable text (abstract / landing page only)**

- Capture-SELEX in complex medium isolated ssDNA aptamer `1d04` with a reported dissociation constant of 12 µM. Tag: `primary-source-supported`. Quantity: `Kd_molecular` *if* the unread methods are a 1:1 solution measurement — method unread, so method identity is `unresolved`. Construct: `1d04`.
- Truncated sequence `glu1` was Fc-labelled at the 3′-end, Au–thiol immobilized with MCH backfill, and read by ACV. Tag: `primary-source-supported` (construct/architecture). Not a kinetic constant.
- `glu1` aptasensor `sensor_LOD` 0.0013 pM and `analytical_working_range` 0.01 pM–1 nM in the abstract, with selectivity claimed in tenfold-diluted human serum. Tag: `primary-source-supported` from abstract; figures unread. These are not `Kd_molecular` and not `kon`/`koff`.

---

### C02-02 — Hu et al., multiplex MEA including glutamate

- **title:** Potential-pulse-assisted co-immobilization of multiple aptamers on microelectrode arrays for multiplexed neurotransmitter detection
- **year:** 2025 (Crossref print/online 2025-12; PubMed “2025 Dec 15”; volume 290, article 117992)
- **journal:** Biosensors and Bioelectronics
- **authors:** Ziheng Hu; Ruifeng Zhu; Gabriela Figueroa-Miranda; Lingyan Feng; Andreas Offenhäusser; Dirk Mayer
- **DOI:** 10.1016/j.bios.2025.117992
- **PMID:** 40992279
- **PMCID:** empty
- **source_type:** primary
- **why it matters for this lane:** Same Mayer/Offenhäusser group as Wu. Abstract states multiplex electrochemical detection of serotonin, glutamate, and dopamine on one MEA, with glutamate “for the first time in multiplex detection.” Site-selective immobilization in 30 min is a **fabrication** clock, not `response_time` or `koff`. Needed to ask whether the glutamate channel uses `glu1` and whether any kinetic trace was collected on that immobilized oligo.
- **full_text_inspected:** no
- **access_route:** abstract-only. Metadata conflict: Unpaywall reports hybrid OA / CC-BY at the publisher DOI; Europe PMC lists `license=cc by` but `isOpenAccess=N`; Crossref licenses are Elsevier TDM, not CC; ScienceDirect HTML returned HTTP 403; Jülich repository URL `https://juser.fz-juelich.de/record/1049644` failed TLS in this environment. Treat as closed until a free HTML/PMC copy is actually retrieved.
- **limitation:** Sequence of the glutamate aptamer, buffer, and any `kon`/`koff`/`response_time` are not in the PubMed abstract. 30 min is not a binding rate. Do not assume it is Wu `glu1` without the unread methods. `transferable`: unknown.

**Tagged claims**

- Multiplex electrochemical detection including glutamate on an aptamer-MEA. Tag: `primary-source-supported` (abstract). Not a kinetic measurement.
- Potential-pulse-assisted co-immobilization of three aptamers on one chip in 30 min. Tag: `primary-source-supported`. Quantity: none of the ten ontology types (fabrication time).

---

### C02-03 — Abrantes et al., NG-Apt-Glu graphene FET (preprint)

- **title:** Ultrasensitive graphene FET aptasensor for direct attomolar detection of glutamate in human clinical samples
- **year:** 2025 (bioRxiv posted 2025-11-07)
- **journal:** bioRxiv (posted-content; not a journal)
- **authors:** Mafalda Abrantes; Yolanda Blanco; Rafael P. Giacomazzi; Isabel P. Moreira; Patricia Monteiro; Jérôme Borme; Maria Vieira-Coelho; Sérgio F. Sousa; Carlos Briones; Luis Jacinto; Pedro Alpuim
- **DOI:** 10.1101/2025.11.05.686731
- **PMID:** empty
- **PMCID:** empty
- **source_type:** preprint
- **why it matters for this lane:** Full HTML inspected. The authors start from the 98-nt DNA sequence they name `glu1d04` (quoted 5′-GCATCAGTCCACTCGTGAGGTCGACTGATGAGGCTCGATCAGGAGCGCCGCTCGATCGCACTTTCACAGGATAGTAGTTGGTAGCGACCTCTGCTAGA-3′), cite Wu as [48], computationally truncate/mutate to 58-nt `NG-Apt-Glu`, and put **both** `NG-Apt-Glu` and `glu1` on the same gFET architecture. That is a same-platform construct comparison, not a license to copy Wu’s 12 µM number onto `NG-Apt-Glu`. They report ELONA `Kd` in the millimolar range, gFET `sensor_LOD` 1 aM in aCSF, and a protocol clock (20 transfer curves in <1 s after sample incubation; drift traces every 10 s). No `kon`/`koff`. Docking/MD are computational.
- **full_text_inspected:** yes (bioRxiv HTML `.../686731v1.full`)
- **access_route:** html. Conflict: Unpaywall `oa_status=green`; Europe PMC `isOpenAccess=N`; the bioRxiv HTML loaded.
- **limitation:** Preprint, not peer-reviewed VoR. ELONA `Kd` uses capturer-strand displacement (Hill fits, four capturers) — not a 1:1 SPR/`kon`/`koff` experiment and not the FET surface. Docking “binding sites” are `computational illustration`. `measurement_time` of the FET sweep is not a binding `response_time`. `transferable`: no (parent 98-nt vs 58-nt vs FET-bound vs ELONA capturer hybrids).

**Tagged claims (HTML)**

- `NG-Apt-Glu` is a designed truncation/mutant of the quoted `glu1d04` sequence attributed to Wu. Tag: `primary-source-supported` for what Abrantes *did*; Wu VoR unread so sequence identity vs Wu’s printed `1d04`/`glu1` is `unresolved` at the nucleotide level from this scout.
- Inhibition ELONA `Kd` values “in the millimolar range (from 10.3 to 25.1 mM)” depending on capturer. Tag: `primary-source-supported`. Quantity: not a clean `Kd_molecular` 1:1 oligo–glutamate constant; report as ELONA apparent `Kd` and do not transfer to FET.
- gFET `sensor_LOD` 1 aM and linearized range described as 1 aM–1 pM (abstract also 1 aM–10 pM — **internal range wording differs between abstract and results**; do not pick a single range silently). Tag: `primary-source-supported` with that locator conflict. Quantities: `sensor_LOD`, `analytical_working_range`. Matrix: aCSF.
- 20 transfer curves acquired in under 1 s after sample incubation; drift protocol measured every 10 s for 1 h. Tag: `primary-source-supported`. Quantity: `measurement_time` (instrument/protocol), not `kon`/`koff`.
- In silico 3D prediction, MD, and docking of glutamate onto two putative sites. Tag: `computational illustration`.

---

### C02-04 — Xiao et al., resettable CNT FET including glutamate

- **title:** In Situ Electrically Resettable Field-Effect Transistor Biosensors for Continuous and Multiplexed Neurotransmitter Detection
- **year:** 2025 (online 2025-05-28; print issue 12(31); PMC header Adv Sci (Weinh). 2025 May 28;12(31):e04497)
- **journal:** Advanced Science
- **authors:** Bo Xiao; Tingxian Li; Xianmao Cao; Yang Zhang; Jianping He; Mengmeng Xiao; Zhiyong Zhang
- **DOI:** 10.1002/advs.202504497
- **PMID:** 40433802
- **PMCID:** PMC12376627
- **source_type:** primary
- **why it matters for this lane:** Gold OA HTML inspected. Multiplex CNT FET includes a glutamate channel. Main text reports SPR-derived `Kd` values for “screened aptamers”: dopamine 20 nM, serotonin 10.5 nM, histamine 15 nM, **glutamate 293 nM** (Figure S6, supporting information — SI HTML/PDF **not** retrieved). Real-time `I_ds` traces for glutamate 10 fM–100 nM in 0.1× PBS. pH-reset addresses *probe–target separation* for reuse, which is related to practical `koff` but is an engineered pH switch, not the intrinsic glutamate–aptamer `koff`. Aptamer sequences are not in the main-text HTML.
- **full_text_inspected:** partial (main PMC HTML yes; Supporting Information no)
- **access_route:** pmc (gold OA)
- **limitation:** 293 nM is `Kd_molecular` from SPR of an unspecified glutamate oligo — **not** Wu `1d04` 12 µM and **not** a `kon`/`koff` pair. Sequence and SPR buffer are in unread SI. 12 h incubation in methods is immobilization, not `response_time`. 0.1× PBS is not CSF. `transferable`: no vs Wu `glu1` or Abrantes `NG-Apt-Glu`.

**Tagged claims**

- SPR `Kd` glutamate 293 nM for the screened aptamer used in this paper. Tag: `primary-source-supported` for the main-text statement; SI sensorgrams unread so `kon`/`koff` from those sensorgrams are `unresolved`. Quantity: `Kd_molecular` (SPR), construct unnamed in main text.
- Practical detection limit 10 fM (in vitro, several transmitters). Tag: `primary-source-supported`. Quantity: `sensor_LOD`. Not `Kd_molecular`.
- Real-time three-channel `I_ds` for glutamate 10 fM–100 nM in 0.1× PBS. Tag: `primary-source-supported`. Quantity: calibration/`analytical_working_range` on the FET, not `kon`.
- Acidic intramolecular triplex used to force dissociation for reuse. Tag: `primary-source-supported` as a device reset mechanism. Not intrinsic `koff` of the glutamate complex at physiological pH.

---

### C02-05 — Abeykoon et al., IPA `kon`/`koff` of electrode-bound tobramycin aptamer

- **title:** Interrogation of Small Molecules to Surface-Bound Aptamer Binding Kinetics with Electrochemical Aptamer-Based Sensors Using Intermittent Pulse Amperometry
- **year:** 2025 (online 2025-11-13; print 2025-11-25; Anal. Chem. 97(46):25391–25397)
- **journal:** Analytical Chemistry
- **authors:** Sanduni W. Abeykoon; Warunika N. Dikella; Mirelis Santos-Cancel; Robert A. Lazenby; Ryan J. White
- **DOI:** 10.1021/acs.analchem.5c01604
- **PMID:** 41231675
- **PMCID:** PMC13101946
- **source_type:** primary
- **why it matters for this lane:** This is the only free-route paper inspected that reports **both** `kon` and `koff` for a small-molecule aptamer **on the same electrode-bound E-AB construct** used as the sensor, with a flow-injection protocol that also yields an equilibrium isotherm. Analyte is tobramycin (Rowe/Plaxco parent DNA sequence given), **not glutamate**. IPA `measurement_time` is milliseconds; binding phases are fitted as `kobs = kon[T] + koff`. Parallel SPR on similarly prepared gold **failed** to separate specific vs nonspecific tobramycin adsorption — a direct warning against transferring SPR kinetics even on “the same” thiol/MCH gold recipe.
- **full_text_inspected:** yes (PMC HTML; Unpaywall classifies this PMC file as `submittedVersion` / NIHMS. VoR may differ.)
- **access_route:** pmc
- **limitation:** Construct is parent tobramycin DNA aptamer `5′-HS-C6-GGGACTTGGTTTAGGTAATGAGTCCC-MB-3′` on gold under stated flow/buffer — **not** transferable to `glu1`/glutamate. Destabilized ATP sequence is listed in methods but the reported `kon`/`koff` in the Results section inspected here are the tobramycin fits. `transferable`: no.

**Tagged claims (PMC HTML)**

- For electrode-bound tobramycin aptamer, `kon` = 3.5×10^4 M^−1 s^−1 from the slope of `kobs` vs [T]; `koff` = 1.39 s^−1, concentration-independent; `Kd,kinetic` = 41±11 μM. Tag: `primary-source-supported`. Quantities: `kon`, `koff`; kinetic `Kd` is `koff/kon`, not a separate ontology slot — do not relabel it `Kd_molecular` of a soluble oligo.
- Equilibrium Langmuir fit on the same IPA data: 46±6 μM. Tag: `primary-source-supported`. Surface E-AB apparent affinity, not solution `Kd_molecular`.
- SPR on aptamer/MCH vs MCH-only gold showed adsorption in both channels; IPA reported conformational/faradaic change. Tag: `primary-source-supported`. Implication for this lane: SPR `kon`/`koff` on gold cannot be assumed equal to E-AB IPA rates even for tobramycin.

---

### C02-06 — Santos-Cancel et al., IPA 2 ms interrogation (tobramycin and ATP)

- **title:** Rapid Two-Millisecond Interrogation of Electrochemical, Aptamer-Based Sensor Response Using Intermittent Pulse Amperometry
- **year:** 2018 (online 2018-05-15; print 2018-06-22; ACS Sens. 3(6):1203–1209)
- **journal:** ACS Sensors
- **authors:** Mirelis Santos-Cancel; Robert A. Lazenby; Ryan J. White
- **DOI:** 10.1021/acssensors.8b00278
- **PMID:** 29762016
- **PMCID:** PMC6207073
- **source_type:** primary
- **why it matters for this lane:** Distinguishes **interrogation/`measurement_time`** (as fast as 2 ms; sub-ms sampled current after a pulse) from **binding `kobs`**. On E-AB surfaces, at 200 μM target, tobramycin `kobs` = 0.72±0.04 s^−1 and ATP `kobs` = 1.4±0.4 s^−1 (PMC HTML). The text writes `kobs = kon[T] + koff` but the inspected Results report **single-concentration `kobs`**, not a `kon`/`koff` pair (that pair is C02-05). Glutamate is absent.
- **full_text_inspected:** yes (PMC HTML, NIHMS author manuscript)
- **access_route:** pmc
- **limitation:** `kobs` at 200 μM is not `kon` or `koff`. 2 ms is `measurement_time`, not the binding `response_time` (`1/kobs` is seconds under those conditions). ATP and tobramycin constructs are not glutamate. `transferable`: no.

**Tagged claims**

- IPA interrogates E-AB current with time resolution as fast as 2 ms. Tag: `primary-source-supported`. Quantity: `measurement_time`.
- At 200 μM, tobramycin E-AB `kobs` = 0.72±0.04 s^−1; ATP E-AB `kobs` = 1.4±0.4 s^−1. Tag: `primary-source-supported`. Quantity: observed binding rate on those surfaces; not ontology `kon`/`koff` until a concentration series is fitted (see C02-05).

---

### C02-07 — Ding and Liu, kinetic ITC of DNA aptamers vs small molecules

- **title:** Kinetic ITC of DNA Aptamers Binding for Small Molecules and Implications for Binding Assays and Biosensors
- **year:** 2024 (online 2024-07-05; print 2024-08; ChemBioChem 25(15), article e202400225)
- **journal:** ChemBioChem
- **authors:** Yuzhe Ding; Juewen Liu
- **DOI:** 10.1002/cbic.202400225
- **PMID:** 38785220
- **PMCID:** empty
- **source_type:** primary
- **why it matters for this lane:** PubMed/Crossref abstract states that kinetic ITC was used to extract `kon` and `koff` across DNA aptamers with `Kd` from 28 nM to 864 μM, with `kon` decreasing from 2×10^5 M^−1 s^−1 to 96 M^−1 s^−1 and `koff` increasing from 1.03×10^−3 s^−1 to 0.012 s^−1, and discusses beacon vs strand-displacement assay implications. This is **solution-phase ITC**, not an E-AB/FET surface, and the abstract does not name glutamate.
- **full_text_inspected:** no
- **access_route:** abstract-only. Conflict: Unpaywall `oa_status=hybrid`, license `cc-by-nc`, best location = publisher DOI (no PDF URL); Crossref VOR license `http://creativecommons.org/licenses/by-nc/4.0/`; Europe PMC `isOpenAccess=N`; Wiley HTML/PDF HTTP 403 from this host. Numbers below are **abstract-only**.
- **limitation:** Which aptamers sit at which `(kon, koff)` is unread. Solution ITC rates are not transferable to thiol-gold E-AB or FET-immobilized glutamate oligos. `transferable`: no.

**Tagged claims (abstract)**

- Kinetic ITC analysis of various DNA aptamers for small molecules yielded the `kon`/`koff` vs `Kd` trend quoted above. Tag: `primary-source-supported` *as an abstract-level summary*; per-aptamer table is `unresolved` until VoR is read. Quantities: `kon`, `koff`, `Kd_molecular` (ITC solution).
- Presence or absence of a glutamate aptamer in that ITC set: `unresolved`.

---

### C02-08 — Arroyo-Currás et al., chronoamperometric E-AB, 300 ms in vivo (tobramycin)

- **title:** Subsecond-Resolved Molecular Measurements in the Living Body Using Chronoamperometrically Interrogated Aptamer-Based Sensors
- **year:** 2018 (online 2017-11-21; print 2018-02-23; ACS Sens. 3(2):360–366)
- **journal:** ACS Sensors
- **authors:** Netzahualcóyotl Arroyo-Currás; Philippe Dauphin-Ducharme; Gabriel Ortega; Kyle L. Ploense; Tod E. Kippin; Kevin W. Plaxco
- **DOI:** 10.1021/acssensors.7b00787
- **PMID:** 29124939
- **PMCID:** empty
- **source_type:** primary
- **why it matters for this lane:** Abstract: chronoamperometry reports target via the **lifetime of current decay** (electron-transfer kinetics of the redox reporter), with **300 ms** time resolution for tobramycin in the living body. That 300 ms is `measurement_time` / interrogation, not aptamer–tobramycin `koff`. Calibration-free amplitude independence is an ET-kinetics feature, not ligand-binding `kon`.
- **full_text_inspected:** no
- **access_route:** abstract-only (Unpaywall closed)
- **limitation:** Tobramycin E-AB in blood/tissue, not glutamate. Do not equate reporter ET lifetime with ligand `koff`. `transferable`: no.

**Tagged claims (abstract)**

- Chronoamperometric E-AB measurement of tobramycin in situ in the living body with 300 ms time resolution. Tag: `primary-source-supported`. Quantity: `measurement_time`.
- Concentration reported from exponential current-decay lifetime. Tag: `primary-source-supported`. This is redox-reporter ET, not ligand `kon`/`koff`.

---

### C02-09 — Downs et al., electrochemical phase interrogation, subsecond E-AB

- **title:** Subsecond-Resolved Molecular Measurements Using Electrochemical Phase Interrogation of Aptamer-Based Sensors
- **year:** 2020 (online 2020-09-22; print 2020-10-20; Anal. Chem. 92(20):14063–14068)
- **journal:** Analytical Chemistry
- **authors:** Alex M. Downs; Julian Gerson; Kyle L. Ploense; Kevin W. Plaxco; Philippe Dauphin-Ducharme
- **DOI:** 10.1021/acs.analchem.0c03109
- **PMID:** 32959647
- **PMCID:** empty
- **source_type:** primary
- **why it matters for this lane:** Abstract contrasts SWV `measurement_time` of “a few seconds” with impedance **phase** interrogation that achieves **subsecond** resolution and multihour stability in undiluted whole blood. Another clock: interrogation method vs binding equilibration. Analyte is not named as glutamate in the abstract.
- **full_text_inspected:** no
- **access_route:** abstract-only (Unpaywall closed)
- **limitation:** Closed VoR; which aptamer/target was used for the subsecond traces is unread. Subsecond is `measurement_time` unless unread figures fit `kobs`. `transferable`: unknown (construct unread).

**Tagged claims (abstract)**

- SWV interrogation of this sensor class is typically limited to a few seconds; phase interrogation achieves subsecond temporal resolution in whole blood. Tag: `primary-source-supported`. Quantity: `measurement_time`.

---

### C02-10 — Kumakli et al., microscale E-AB, ATP association/dissociation times ~80 ms

- **title:** Microscale, Electrochemical, Aptamer-Based Sensors for Enhanced Small-Molecule Detection at Millisecond Time Scales
- **year:** 2023 (online 2023-11-21; print 2023-12-22; ACS Sens. 8(12):4521–4530)
- **journal:** ACS Sensors
- **authors:** Hope Kumakli; Marie Baldwin; Sanduni W. Abeykoon; Ryan J. White
- **DOI:** 10.1021/acssensors.3c01055
- **PMID:** 38104257
- **PMCID:** PMC11059485
- **source_type:** primary
- **why it matters for this lane:** PMC HTML inspected. Nanostructured ~500 nm-radius gold E-AB, ATP aptamer sequence given in methods. Under flow, IPA at 100 μs δt / 20 ms boxcar: **association time 80 ms and dissociation time 80 ms** after injection. These are **observed phase durations under that flow geometry**, not necessarily `1/koff` of a well-mixed 1:1 model (the outlet–sensor distance is used to create a bolus). Title/PubMed use “Time Scales”; NIHMS HTML title uses “Timescales” — spelling disagreement only.
- **full_text_inspected:** yes (PMC HTML, NIHMS1985597)
- **access_route:** pmc
- **limitation:** ATP construct, flow-defined bolus, microelectrode — not glutamate, not Wu `glu1`. 80 ms is an observed `response_time`/`recovery` under flow, not a reported `kon` in M^−1 s^−1. `transferable`: no.

**Tagged claims**

- Microelectrode ATP E-AB under stated flow: association time 80 ms and dissociation time 80 ms at 20 ms averaged IPA resolution. Tag: `primary-source-supported`. Quantity: `response_time` (observed association/dissociation duration), distinct from `measurement_time` (20 ms averaging; 100 μs pulse).

---

### C02-11 — Wilson et al., ISD aptamer switches, ATP parent, 170 ms–3 s

- **title:** Independent control of the thermodynamic and kinetic properties of aptamer switches
- **year:** 2019 (online 2019-11-07; Nat. Commun. volume 10; Crossref page field empty; literature/PMC cite article 5079)
- **journal:** Nature Communications
- **authors:** Brandon D. Wilson; Amani A. Hariri; Ian A. P. Thompson; Michael Eisenstein; H. Tom Soh
- **DOI:** 10.1038/s41467-019-13137-x
- **PMID:** 31699984
- **PMCID:** PMC6838323
- **source_type:** primary
- **why it matters for this lane:** Gold OA. From one **parent ATP aptamer**, intramolecular strand-displacement (ISD) switches were tuned to effective `Kd` 10 μM–40 mM and **binding kinetics 170 ms–3 s** (fluorescence, solution-phase switches; two-site ATP model in SI). Shows that even for one parent sequence, kinetics are **construct-dependent** (displacement-strand length/mismatches). Not glutamate; not an immobilized E-AB unless separately shown.
- **full_text_inspected:** partial (PMC HTML yes; Nature landing also retrieved as cookie-walled preview; SI not fully extracted)
- **access_route:** pmc
- **limitation:** Solution fluorescence ISD constructs ≠ electrode-bound ATP E-AB ≠ glutamate aptamers. “170 ms to 3 s” is a kinetic-response window for those switches, not a universal small-molecule `koff`. `transferable`: no.

**Tagged claims**

- ISD series from one ATP parent: effective dissociation constants 10 μM–40 mM and binding kinetics 170 ms–3 s. Tag: `primary-source-supported`. Quantities: construct-dependent apparent `Kd_molecular`; kinetic window as `response_time` of the switch, not named `kon`/`koff` in the abstract sentence (per-construct rates may be in unread SI).
- Aptamer-beacon kinetics are described as typically minutes–hours vs ISD hundreds of milliseconds, in the PMC discussion text. Tag: `primary-source-supported` as the authors’ comparison in that paper; not a glutamate measurement.

---

### C02-12 — Jucker et al., theophylline RNA, conformationally limited association

- **title:** Role of a heterogeneous free state in the formation of a specific RNA-theophylline complex
- **year:** 2003 (online 2003-02-11; print 2003-03-11 / Crossref print 2003-03-01; Biochemistry 42(9):2560–2567)
- **journal:** Biochemistry
- **authors:** Fiona M. Jucker; Rebecca M. Phillips; Scott A. McCallum; Arthur Pardi
- **DOI:** 10.1021/bi027103+
- **PMID:** 12614150
- **PMCID:** empty
- **source_type:** primary
- **why it matters for this lane:** Classic **solution RNA–small-molecule** kinetic mechanism: association becomes theophylline-independent at high ligand (conformational change rate-limiting); Mg^2+ absence drops affinity >10,000-fold **primarily via increased dissociation rate** (abstract). Shows why a single `Kd_molecular` does not determine speed, and why buffer (divalent ions) cannot be transferred. Not glutamate; RNA not DNA; not a sensor surface.
- **full_text_inspected:** no
- **access_route:** abstract-only (Unpaywall closed)
- **limitation:** Numerical `kon`/`koff` are in the unread VoR/figures. Abstract is qualitative on the Mg^2+ `koff` effect. `transferable`: no.

**Tagged claims (abstract)**

- High-theophylline association rate becomes ligand-independent, implying a conformational step. Tag: `primary-source-supported`.
- Without Mg^2+, affinity drops >10,000-fold, attributed primarily to faster complex dissociation. Tag: `primary-source-supported`. Quantities: fold-change in affinity; `koff` direction, numbers unread.

---

### C02-13 — Idili et al., phenylalanine E-AB, 12 s in vivo vs 5 s equilibration in vitro

- **title:** Seconds-Resolved, In Situ Measurements of Plasma Phenylalanine Disposition Kinetics in Living Rats
- **year:** 2021 (online 2021-02-17; print 2021-03-02; Anal. Chem. 93(8):4023–4032)
- **journal:** Analytical Chemistry
- **authors:** Andrea Idili; Julian Gerson; Tod Kippin; Kevin W. Plaxco
- **DOI:** 10.1021/acs.analchem.0c05024
- **PMID:** 33594890
- **PMCID:** PMC9840908
- **source_type:** primary
- **why it matters for this lane:** Closely related **amino-acid** small-molecule E-AB. PMC HTML: in vitro, at “few tens of micromolar” phenylalanine, the sensor “equilibrates to bidirectional concentration changes within the 5 s required to collect a single square wave voltammogram”; in vivo temporal resolution **12 s**. Those clocks are `measurement_time` / protocol equilibration on **that** phenylalanine aptamer, not glutamate `koff`. Table 1 kinetic parameters are **PK of phenylalanine in the rat**, not aptamer `kon`.
- **full_text_inspected:** yes (PMC9840908 HTML)
- **access_route:** pmc
- **limitation:** Phenylalanine aptamer ≠ glutamate aptamer. 5 s is bounded by the SWV scan, so binding could be faster than 5 s (`unresolved`). PMC ID: Europe PMC and the 2026-09-11 PubMed esummary agree `PMC9840908`. An earlier esummary call in this same session returned `PMC4728993` for this PMID — treat `PMC4728993` as **unverified/wrong**. `transferable`: no.

**Tagged claims**

- In vivo phenylalanine E-AB: few-micromolar precision, 12 s temporal resolution. Tag: `primary-source-supported`. Quantity: `measurement_time`.
- In vitro, at tens of µM Phe, bidirectional equilibration within one 5 s SWV. Tag: `primary-source-supported`. Quantity: observed sensor `response_time` **upper-bounded** by `measurement_time`.
- α/β half-lives in Table 1 are animal PK, not `koff`. Tag: `primary-source-supported` as PK; do not store as aptamer `koff`.

---

### C02-14 — Zhao et al., aptamer-FET neuroprobes (serotonin in vivo; glutamate not measured)

- **title:** Implantable aptamer-field-effect transistor neuroprobes for in vivo neurotransmitter monitoring
- **year:** 2021 (print/online 2021-11-26; Sci. Adv. 7(48); article eabj7422)
- **journal:** Science Advances
- **authors:** Chuanzhen Zhao; Kevin M. Cheung; I-Wen Huang; Hongyan Yang; Nako Nakatsuka; Wenfei Liu; Yan Cao; Tianxing Man; Paul S. Weiss; Harold G. Monbouquette; Anne M. Andrews
- **DOI:** 10.1126/sciadv.abj7422
- **PMID:** 34818033
- **PMCID:** PMC8612678
- **source_type:** primary
- **why it matters for this lane:** Gold OA HTML. Aptamer-FET neuroprobes for **serotonin** (and prior dopamine work). Authors state aptamer-FET `response_time` “on the order of seconds” (citing their earlier work), while a 12 min apparent response in gelatin/aCSF is **diffusion** over ~0.2 cm, not binding `koff`. Gate-sweep `measurement_time` ~5 s; prior `I_ds` ~2 s. Glutamate appears as an aptamer **being developed**, not as a measured channel. Explicitly contrasts seconds chemical resolution with ~100 ms LFP.
- **full_text_inspected:** yes (PMC HTML)
- **access_route:** pmc
- **limitation:** No glutamate `kon`/`koff`. Seconds-scale FET `response_time` is for other transmitter aptamers/architectures. Title hyphenation: PubMed ASCII hyphen vs Crossref en-dash — same paper. `transferable`: no.

**Tagged claims**

- Authors’ prior aptamer-FET `response_time` on the order of seconds; 12 min in the gelatin experiment attributed to diffusion. Tag: `primary-source-supported`. Quantities: `response_time` vs transport delay; not `koff`.
- Instrument `measurement_time` ~5 s per gate sweep; ~2 s in prior real-time `I_ds`. Tag: `primary-source-supported`.
- Glutamate listed among aptamers “being developed,” not as data in this paper. Tag: `unresolved` for glutamate kinetics.

---

### C02-15 — Rahbarimehr et al., E-AB “lost” Kd vs solution affinity

- **title:** Finding the Lost Dissociation Constant of Electrochemical Aptamer-Based Biosensors
- **year:** 2023 (online 2023-01-13; print 2023-01-31; Anal. Chem. 95(4):2229–2237)
- **journal:** Analytical Chemistry
- **authors:** Erfan Rahbarimehr; Hoi Pui Chao; Zachary R. Churcher; Sladjana Slavkovic; Yunus A. Kaiyum; Philip E. Johnson; Philippe Dauphin-Ducharme
- **DOI:** 10.1021/acs.analchem.2c03566
- **PMID:** 36638814
- **PMCID:** empty
- **source_type:** primary
- **why it matters for this lane:** Abstract: SWV-interrogated E-AB sensors often show µM–mM apparent affinity even when the **same aptamer sequences** have nM–µM affinity in solution methods. That is a primary-literature warning against transferring `Kd_molecular` (and therefore any `kon`/`koff` inferred from it) from solution to the E-AB surface — the exact failure mode this lane must not commit for glutamate `1d04` → `glu1`.
- **full_text_inspected:** no
- **access_route:** abstract-only (Unpaywall closed)
- **limitation:** Closed VoR; which aptamers illustrate the nM–µM vs µM–mM gap is unread. Not a glutamate paper. Does not itself report `kon`/`koff`. `transferable`: the paper’s point is that solution→surface transfer is **not** generally valid (`no`).

**Tagged claims (abstract)**

- Some SWV E-AB sensors report much weaker apparent affinity than solution characterization of the parent aptamer. Tag: `primary-source-supported` at abstract level. Quantities: surface apparent affinity (often stored as `EC50` or sensor `Kd`, **not** `Kd_molecular`) vs solution `Kd_molecular`.

---

## Same-construct check (lane-specific)

| Construct | Kinetics measured on that object? | Sensor used that same object? |
| --- | --- | --- |
| Wu `1d04` | `unresolved` (unread VoR); abstract gives a dissociation constant only | Sensor uses truncated `glu1`, not full `1d04` |
| Wu `glu1` on Au / ACV | no `kon`/`koff` in inspectable text | yes, that is the sensor |
| Abrantes `NG-Apt-Glu` | ELONA apparent `Kd` (mM), not `kon`/`koff`; docking is computational | yes, gFET uses `NG-Apt-Glu`; they also ran `glu1` on gFET as comparator |
| Xiao glutamate aptamer | SPR `Kd` 293 nM; `kon`/`koff` unread (SI) | FET uses a pH-switch-appended version of “the” screened aptamer; sequence unread |
| Hu 2025 glutamate channel | unread | multiplex MEA; sequence unread |
| Abeykoon tobramycin parent DNA on Au | **yes** — IPA `kon` and `koff` | **yes** — same E-AB surface |
| Santos-Cancel tobramycin/ATP E-AB | `kobs` at 200 μM, not separated `kon`/`koff` | yes |
| Ding ITC DNA aptamers | abstract `kon`/`koff` in solution | not a glutamate sensor; surface not claimed |
| Wilson ATP ISD switches | 170 ms–3 s kinetic window in solution fluorescence | not the E-AB/FET glutamate devices |
| Kumakli ATP micro-E-AB | 80 ms assoc./dissoc. under flow | yes, that micro-E-AB |
| Idili phenylalanine E-AB | equilibration ≤5 s in vitro (SWV-limited) | yes, that Phe E-AB |

---

## Quantity-type reminders from this lane (not a thesis)

- `Kd_molecular`: Wu `1d04` 12 µM (method unread); Xiao SPR glutamate 293 nM (sequence unread); Abrantes ELONA 10.3–25.1 mM (capturer assay); Ding ITC range 28 nM–864 μM (which aptamers unread); Wilson ATP ISD 10 μM–40 mM (construct series).
- `kon` / `koff`: numerical pair on a **sensor construct** found only for **tobramycin E-AB** (C02-05). Ding abstract gives a cross-aptamer ITC envelope. Glutamate: empty.
- `sensor_LOD` / `analytical_working_range`: Wu `glu1` ACV; Abrantes gFET; Xiao FET — not rates.
- `response_time`: Kumakli 80 ms flow assoc./dissoc. (ATP); Zhao/Nakatsuka FET “seconds” (non-glutamate); Wilson ISD 170 ms–3 s (ATP switches); Idili ≤5 s (Phe, SWV-limited).
- `measurement_time`: Santos-Cancel IPA 2 ms; Abeykoon IPA milliseconds; Arroyo-Currás chronoamperometry 300 ms; Downs subsecond phase vs few-second SWV; Idili 12 s in vivo / 5 s SWV; Zhao ~5 s sweep / ~2 s `I_ds`; Abrantes <1 s for 20 FET curves after incubation.

---

## Identifiers attempted but not verified (or conflicting)

| Identifier | What happened |
| --- | --- |
| PMC4728993 | One PubMed esummary response in this session attached this PMC to PMID 33594890 (Idili). Later esummary + Europe PMC + the HTML at PMC9840908 identify Idili as **PMC9840908**. Do not use PMC4728993 for Idili. |
| PMC6856101 | Guessed as Wilson 2019; HTML is an unrelated AML/mebendazole paper. Wilson is **PMC6838323**. |
| PMC3787420, PMC4134667, PMC3983011, PMC4928482 | Spurious PMC fields from a mixed PubMed XML parse earlier in the session; **not** used. Verified PMIDs use the esummary/Europe PMC PMC column in the candidate list. |
| Unpaywall hybrid for Ding 10.1002/cbic.202400225 and Hu 10.1016/j.bios.2025.117992 | OA flags disagree with HTTP 403 fetches and with Crossref license types. Not treated as inspected full text. |
| OpenAlex `cites:` Wu DOI | 0 hits vs Crossref citation count 32 — **tooling failure**, not a citation vacuum. |
| PMID 41851736 / 41231675 as a combined `PMID:… OR PMID:…` ESearch | ESearch interpreted poorly (thousands of hits). Individual PMID lookups for 41231675 succeeded; 41851736 was **not** re-fetched as a kinetics candidate (out of lane; Tanner tetrahedron lead). |
| Abrantes PMID | none assigned at search time (Europe PMC preprint `PPR1115530`). |
| Wilson Crossref `page` | empty; article number 5079 used in other papers’ bibliographies and consistent with Nat. Commun. volume 10 (2019) but not copied from a Crossref `article-number` field in the payload retrieved here. |

---

## Wildcard direction examined

**Computational truncation + ELONA of the Wu lineage (Abrantes 2025 preprint)** and **a second glutamate SPR `Kd` (Xiao 293 nM)** were not specified in the parent lane prompt beyond “closely related.” They were pursued because they are the only other free-route glutamate-aptamer primary/preprint items that even mention affinity or time. They still do **not** supply glutamate `kon`/`koff`. Docking in Abrantes remains `computational illustration`. Xiao SI SPR sensorgrams are the highest-value unread glutamate-kinetics object identified.

---

## Highest-information next reads (for extractors, not done here)

1. Wu VoR methods: how 12 µM was measured; any time traces; exact `1d04` vs `glu1` sequences.  
2. Xiao Figure S6 SPR: glutamate `kon`/`koff` if fitted; oligo sequence vs Wu.  
3. Ding VoR table: whether any glutamate/amino-acid aptamer is in the ITC set; per-row `kon`/`koff`.  
4. Hu 2025 methods: glutamate oligo identity and any chronoamperometry/IPA/`t90`.  
5. Abeykoon VoR vs NIHMS: confirm tobramycin `kon`/`koff` numbers typeset in the publisher version.

---

## Integrity notes

- No source promoted to `core`.  
- No ledger (`state/claims.csv`, `state/sources.csv`) edited.  
- No PDFs stored in the repository.  
- Other scout reports, theses, claims ledgers, and nightly summaries were not used as evidence.  
- Model IDs: this scout used the parent worker; no `grok-4.7` identifier invented.
