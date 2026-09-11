# Round 1 literature scout 03

```
scout_id: scout-03
lane: glutamate aptamer biosensor architectures (transduction, sensor_LOD, analytical_working_range, signal_gain, response_time, measurement_time, matrix)
round: 1
status_rule: candidates only; nothing promoted to core
isolation: did not read other scout reports, theses, claims ledgers, or nightly summaries for conclusions
model: cursor-grok-4.6-xhigh
date: 2026-09-11
```

Assigned search focus (not a conclusion): glutamate aptamer biosensor architectures — transduction method, `sensor_LOD`, `analytical_working_range`, `signal_gain`, `response_time`, `measurement_time`, matrix (buffer vs serum vs tissue). Properties are not transferred across constructs, surfaces, buffers, or architectures unless the cited experiment on that same system supports it.

This record does **not** synthesize a poster thesis. All sources below are **candidates**.

---

## Search strategy (negative-search integrity)

Free routes only: Europe PMC REST, PubMed E-utilities, Crossref, Unpaywall, OpenAlex, PMC HTML, publisher OA HTML, bioRxiv HTML, RWTH Publications / institutional OA PDF. No Sci-Hub, no paid APIs, no copyrighted PDFs committed to git.

| Query / route | What it returned that is on-lane | Near-miss / noise |
| --- | --- | --- |
| Europe PMC `glutamate aptamer sensor` | Xiao 2025 CNT FET (PMID 40433802); Hu 2025 MEA (PMID 40992279); Maldonado 2025 Si-nanoribbon (PMID 41104714) buried in a large hit list | Many 2026 reviews that mention aptamers and glutamate only in passing |
| Europe PMC `glutamate aptasensor` | Abrantes 2025 bioRxiv DOI 10.1101/2025.11.05.686731 | Unrelated aptasensors (PSMA, *S. suis*, malaria) |
| Europe PMC `TITLE:glutamate AND (aptamer OR aptasensor) AND (LOD OR electrochemical OR FET OR transistor)` | Wu 2022 (PMID 34783880); Wang 2022 peptide (PMID 35623273); Abrantes preprint | Singh 2018/2019 *Plasmodium* **glutamate dehydrogenase** aptasensors; Ahmadian-Alam 2024 **polymer** receptor; enzymatic / non-aptamer glutamate electrodes |
| Europe PMC `AUTH:Hu AND AUTH:Mayer AND glutamate AND aptamer` | Wu 2022; Hu 2025 MEA | — |
| Europe PMC `glu1 AND aptamer AND glutamate` | Wu 2022 only (among real papers) | Conference poster dumps |
| Crossref + Unpaywall + OpenAlex DOI lookups | Bibliographic confirmation; OA flags | Hu 2025 journal: Europe PMC `isOpenAccess=N` vs Unpaywall `hybrid` CC BY |
| PMC HTML | Xiao PMC12376627; Park PMC10136356; Downs PMC9840907; Rousseau PMC10750225 | Park Table 1 row “Glutamate / FET” is PfGDH, not neurotransmitter glutamate |
| RWTH Publications OA PDF | Hu 2025 journal VoR (CC BY) and Hu 2025 dissertation PDF | Institutional DOI `10.18154/rwth-2025-07238` not in Crossref (404) |
| bioRxiv HTML (via OA fetch) | Abrantes preprint full text | Not peer-reviewed |
| PubMed esummary for PMIDs 34783880, 40992279, 35623273, 40433802, 41104714, 37185488, 36205360, 30308419, 38152504 | Identifier agreement except items listed below | TrAC 10.1016/j.trac.2023.117021: no PMID recovered from PubMed DOI search |
| Web / Europe PMC for optical glutamate nucleic-acid aptasensors (`fluorescence`, `SPR sensor`, `SERS`, `colorimetric` + glu1/1d04) | No primary optical glutamate DNA-aptamer sensor with extractable `sensor_LOD` found | SPR used as **affinity** assay (Xiao SI), not as the glutamate quantification architecture; iGluSnFR is a protein indicator, not an aptamer |

**In vivo glutamate nucleic-acid aptasensor:** not found as a peer-reviewed primary paper. Closest tissue matrix is Hu dissertation Chapter 6 (ex vivo mouse retina). Hu 2025 *Biosens. Bioelectron.* states in vivo NT-release recording as future work (`primary-source-supported` for that statement of intent only).

---

## Quantity and transfer rules used while reading

Tagged quantities are kept separate: `Kd_molecular`, `kon`, `koff`, `EC50`, `sensor_LOD`, `analytical_working_range`, `signal_gain`, `response_time`, `measurement_time`, `biological_concentration_range`.

Do not treat Wu 1d04 solution `Kd_molecular` as glu1/`Glu-apt` surface affinity. Do not treat any architecture’s `sensor_LOD` or incubation time as a property of another architecture. Peptide aptamers, polymer receptors, enzyme electrodes, mGluR FETs, and *Plasmodium* GDH aptasensors are different systems.

---

## Candidates (n = 13)

### C03-01

- **title:** Highly selective and sensitive detection of glutamate by an electrochemical aptasensor
- **year:** print 2022 (PubMed: 2022 Feb); online 2021-11-16 (Crossref issued / Europe PMC `firstPublicationDate`)
- **journal:** Analytical and Bioanalytical Chemistry (PubMed source `Anal Bioanal Chem`; Crossref container-title matches). JuSER record 904340 labels the same DOI as “Fresenius' journal of analytical chemistry 44” — **metadata disagreement; JuSER journal string not used**.
- **authors:** Wu C; Barkova D; Komarova N; Offenhäusser A; Andrianova M; Hu Z; Kuznetsov A; Mayer D (PubMed/Europe PMC/Crossref agree on this set)
- **DOI:** 10.1007/s00216-021-03783-w
- **PMID:** 34783880
- **PMCID:** (empty; none on PubMed/Europe PMC/Unpaywall)
- **source_type:** primary
- **why it matters for THIS assigned lane:** Founding nucleic-acid electrochemical architecture for free glutamate: Capture-SELEX parent **1d04** plus truncated surface construct **glu1**, 3′-ferrocene, Au–thiol, MCH backfill, **alternating current voltammetry**. Abstract reports construct-specific `sensor_LOD` and `analytical_working_range` and a **tenfold-diluted human serum** matrix. Later MEA, gFET, and dissertation probes reuse or truncate this sequence family; those later numbers must not be read back onto this gold-macroelectrode ACV device.
- **full_text_inspected:** no
- **access_route:** abstract-only (Unpaywall `closed`; OpenAlex `oa_status=closed`; Europe PMC not in EPMC)
- **limitation:** VoR closed. Abstract `Kd_molecular` 12 µM is for **1d04**, not demonstrated here for truncated **glu1**. Abstract `sensor_LOD` 0.0013 pM and range 0.01 pM–1 nM are **glu1 ACV on gold**, not transferable to FETs or MEAs. `response_time` / `measurement_time` / `signal_gain` equation not in the abstract. No PMCID.

**Abstract-supported quantities (this architecture only):** `Kd_molecular` (1d04) = 12 µM `primary-source-supported` (abstract). `sensor_LOD` (glu1 ACV) = 0.0013 pM `primary-source-supported` (abstract). `analytical_working_range` (glu1 ACV) = 0.01 pM–1 nM `primary-source-supported` (abstract). Matrix: tenfold diluted human serum `primary-source-supported` (abstract). `transferable`: no (parent vs truncated; solution Kd vs surface sensor).

---

### C03-02

- **title:** Potential-pulse-assisted co-immobilization of multiple aptamers on microelectrode arrays for multiplexed neurotransmitter detection
- **year:** 2025 (PubMed pubdate 2025 Dec 15; epub 2025 Sep 13; Crossref issued 2025-12)
- **journal:** Biosensors and Bioelectronics
- **authors:** Hu Z; Zhu R; Figueroa-Miranda G; Feng L; Offenhäusser A; Mayer D
- **DOI:** 10.1016/j.bios.2025.117992
- **PMID:** 40992279
- **PMCID:** (empty)
- **source_type:** primary
- **why it matters for THIS assigned lane:** Distinct architecture from Wu 2022: **Au electrodeposited nanostructured MEA**, potential-pulse-assisted site-selective immobilization (~5 min PA vs hours of drop-casting), thiol-PEG backfill, **ACV** multiplex of serotonin / glutamate / dopamine on one chip. Reports Glu-channel `sensor_LOD`, semi-log `analytical_working_range`, `signal_gain` fit, **15 min Glu incubation** (`response_time` toward steady ACV signal, not kon), and **PBS vs 50% human serum vs aCSF** matrices. Surface Langmuir–Freundlich parameter for the Glu channel is not the Wu 1d04 solution Kd.
- **full_text_inspected:** yes (RWTH Publications OA PDF of the CC BY VoR; Unpaywall `is_oa=true`, `oa_status=hybrid`, license CC BY. Europe PMC flags `isOpenAccess=N` — **OA-status disagreement recorded**, full text was inspected via the OA PDF.)
- **access_route:** unpaywall
- **limitation:** Not tissue and not in vivo (authors state that as future work). Glu sequence is a truncated Fc-labeled strand citing Wu `Kd = 12 μM`; that citation is **1d04 solution Kd transferred onto the truncated surface construct** by the authors (`transferable`: no unless a same-construct experiment is shown). Do not transfer this MEA `sensor_LOD` 32 pM onto Wu’s macroelectrode or onto FET papers.

**Inspected quantities (this MEA ACV architecture only):**

| Quantity | Value as reported | Matrix / condition | Tag |
| --- | --- | --- | --- |
| transduction | ACV; Glu is signal-on (peak current increases); ST/DA are signal-off | PBS | `primary-source-supported` |
| cited solution Kd (Glu-apt line) | 12 μM, citing Wu 2022 | not re-measured here | authors’ transfer from 1d04; treat as `unresolved` for this truncated surface strand |
| surface Langmuir–Freundlich parameter (Glu channel) | 1.8 nM | electrode interface | not `Kd_molecular` in solution; do not collapse with 12 μM |
| `sensor_LOD` Glu | 32 pM (blank + 3 SD) | buffer/PBS calibration | `primary-source-supported` |
| `analytical_working_range` Glu | 0.1 nM–10 μM (semi-log) | same | `primary-source-supported` |
| `signal_gain` Glu | Signal gain (%) = 25.24 lg C + 62.42 (R = 0.99) | same | `primary-source-supported` |
| incubation toward stable ACV (Glu) | 15 min (Fig. S8; DA 10 min) | same | closer to `response_time` of the assay than to `measurement_time` of a single ACV sweep |
| `sensor_LOD` Glu in serum | 51.5 pM | 50% human serum | `primary-source-supported`; **not** the PBS 32 pM |
| recovery | Glu 97.3%–116.8% in 50% serum; aCSF recoveries 101.1%–111.0% (all three analytes, Table S2) | serum / aCSF | `primary-source-supported` |
| multiplex test spikes | ST 10 nM, Glu 10 nM, DA 100 μM | PBS | `primary-source-supported` |

`transferable`: no to other architectures.

---

### C03-03

- **title:** Electrochemical Aptamer-Based Biosensing Platforms for Multiple Neurotransmitters Analysis
- **year:** 2025 (oral defense 14 Aug 2025; authorship declaration dated 18 Aug 2025)
- **journal:** (empty — RWTH Aachen doctoral dissertation, Fakultät für Mathematik, Informatik und Naturwissenschaften)
- **authors:** Hu, Ziheng
- **DOI:** Crossref and Unpaywall return **404** for `10.18154/rwth-2025-07238` (that string appears in RWTH/web snippets; **not verified** as a Crossref DOI). Locator used: `https://publications.rwth-aachen.de/record/1017243`
- **PMID:** (empty)
- **PMCID:** (empty)
- **source_type:** primary
- **why it matters for THIS assigned lane:** Only glutamate **nucleic-acid aptamer** device found in this scout that is actually inserted into **nervous tissue** (ex vivo mouse retina on a parylene-C probe). Dual-modal: Ø 25 µm AuED electrode ACV glutamate + Ø 15 µm electrophysiology. Reports a **different** `sensor_LOD` / `analytical_working_range` / `signal_gain` on the probe than on the AuED-MEA chip in C03-02, plus Ames medium vs PBS vs 50% serum, ACV `measurement_time` (~14 s/sweep; 1 min sampling), and an explicit statement that electrochemical sampling averages ~1 min and cannot resolve millisecond synaptic transients.
- **full_text_inspected:** yes (institutional OA PDF)
- **access_route:** other (RWTH Publications OA PDF)
- **limitation:** Thesis, not a journal VoR. Chapter 5 overlaps C03-02; Chapter 6 (retina) was not found as a separate peer-reviewed article. Probe-to-probe failures after gold nanostructure detachment. Ames medium calibration is **not** the PBS calibration.

**Inspected quantities (intraretinal-probe ACV architecture only; do not transfer to C03-02 MEA):**

| Quantity | Value as reported | Matrix | Tag |
| --- | --- | --- | --- |
| incubation to plateau (10 nM Glu) | ~10 min (1–20 min series, Fig. 6.6) | buffer | `response_time` of this assay `primary-source-supported` |
| `analytical_working_range` | 1 nM–1 mM (linear in semi-log); concentrations tested 1 nM–2 mM | buffer | `primary-source-supported` |
| `signal_gain` | (%) = 11.86 log C + 44.3 (R = 0.99) | buffer | `primary-source-supported` |
| `sensor_LOD` | 0.3 pM (blank + 3×RSD) | buffer | `primary-source-supported` |
| Ames medium range | 10 nM–10 μM; Signal gain (%) = 57.11 log C − 38.9; blank noise 41.6% | Ames | **different matrix**; `primary-source-supported` |
| ACV sampling | one point every 14 s; consecutive recordings at 1 min | retina | `measurement_time` `primary-source-supported` |
| tissue experiment | in vitro mouse retina; light on/off; some probes ns | tissue | `primary-source-supported` for relative light-linked signal, not for synaptic-timescale glutamate |
| author comparison to MEA | probe LOD “more than 100-times smaller” than “classical MEA” | — | comparison **inside this thesis**; still two architectures (`transferable`: no as a general law) |

---

### C03-04

- **title:** Ultrasensitive graphene FET aptasensor for direct attomolar detection of glutamate in human clinical samples
- **year:** 2025 (Crossref issued 2025-11-07; Europe PMC `firstPublicationDate` 2025-11-07)
- **journal:** bioRxiv (posted-content; not a peer-reviewed journal)
- **authors:** Abrantes M; Blanco Y; Giacomazzi RP; Moreira IP; Monteiro P; Borme J; Vieira-Coelho M; Sousa SF; Briones C; Jacinto L; Alpuim P (Crossref given names: Mafalda Abrantes; Yolanda Blanco; Rafael P. Giacomazzi; Isabel P. Moreira; Patricia Monteiro; Jérôme Borme; Maria Vieira-Coelho; Sérgio F. Sousa; Carlos Briones; Luis Jacinto; Pedro Alpuim)
- **DOI:** 10.1101/2025.11.05.686731
- **PMID:** (empty)
- **PMCID:** (empty)
- **source_type:** preprint
- **why it matters for THIS assigned lane:** Different transduction: **electrolyte-gated graphene FET** with PBASE-immobilized 58-nt **NG-Apt-Glu** (3′-trim of the 98-nt glu1d04 family). Reports `sensor_LOD` and `analytical_working_range` in **1× aCSF**, Dirac-voltage `signal_gain` in mV/decade, **human CSF** (10 min incubation), and a same-chip comparison of NG-Apt-Glu vs **glu1**. Also reports solution-phase ELONA `Kd_molecular` in the **millimolar** range — a different quantity from the attomolar device LOD.
- **full_text_inspected:** yes (bioRxiv HTML/PDF text)
- **access_route:** html
- **limitation:** Preprint. Docking/MD are `computational illustration`. ELONA used 10–50 mM glutamate. Calibration incubates each standard **1 h** then rinses; that is not a synaptic `response_time`. Linear-range wording **disagrees inside the paper** (see below). Authors’ Table 1 comparison to other glutamate sensors must not be used to transfer LODs.

**Inspected quantities (this gFET + named aptamer only):**

| Quantity | Value as reported | Notes | Tag |
| --- | --- | --- | --- |
| ELONA `Kd_molecular` NG-Apt-Glu | 10.3–25.1 mM; %LOS 15.4–61.8 | selection buffer; four capturers | `primary-source-supported` |
| docking scores | site B 33.86 vs site A 30.15 | not a Kd | `computational illustration` |
| `sensor_LOD` NG-Apt-Glu gFET | 1 aM | 1× aCSF | `primary-source-supported` (preprint) |
| `analytical_working_range` | abstract: 1 aM–10 pM; body: linearized up to 1 pM, saturating at 1 pM; Fig. 2E caption: “1 aM … to 10 pM (1×10⁻¹⁰ M)” — **10 pM ≠ 10⁻¹⁰ M** (that is 100 pM) | do not pick a silent “best” value | `unresolved` which range is intended |
| sensitivity (`signal_gain`) | 24 mV/decade | 1× aCSF | `primary-source-supported` |
| glu1 **on these same gFETs** | LOD 10 aM; range 10 aM–0.1 pM; 13 mV/decade | same architecture, different construct | `primary-source-supported`; **not** Wu 2022 ACV LOD |
| calibration incubation | 1 h per concentration | aCSF | not `response_time` of binding kinetics |
| CSF protocol | 20 µL CSF, 10 min incubation, then rinse / transconductance | human CSF | `measurement_time`/`assay time` `primary-source-supported` |
| normal-operation readout | “a series of 20 transfer curves is acquired in under 1 second after sample incubation” | electronics | `measurement_time` of the FET sweep, **after** incubation |
| n | AD n=10, control n=6 | clinical CSF | sample size as stated; not a synaptic study |

`transferable`: no to ACV gold sensors.

---

### C03-05

- **title:** In Situ Electrically Resettable Field-Effect Transistor Biosensors for Continuous and Multiplexed Neurotransmitter Detection
- **year:** 2025 (epub 2025 May 28; collection 2025 Aug; Crossref print 2025-08)
- **journal:** Advanced Science
- **authors:** Xiao B; Li T; Cao X; Zhang Y; He J; Xiao M; Zhang Z
- **DOI:** 10.1002/advs.202504497
- **PMID:** 40433802
- **PMCID:** PMC12376627
- **source_type:** primary
- **why it matters for THIS assigned lane:** Third FET family: **CNT thin-film FET**, AuNP/HfO₂, thiolated aptamers, MCH, liquid-gate real-time `I_ds`. Glutamate is one of four analytes. Reports SPR `Kd_molecular` for the glutamate aptamer, a **practical** `sensor_LOD` of 10 fM in **0.1× PBS**, glutamate calibration **10 fM–100 nM** (narrower than DA/5-HT/histamine traces in the same figures), 1 h static incubation vs real-time traces, ~200 s to stabilize at 10 nM, 40 s pH reset, and **10-fold-diluted PC12 culture medium** — not serum, aCSF, or tissue.
- **full_text_inspected:** yes (PMC HTML)
- **access_route:** pmc
- **limitation:** 0.1× PBS is not physiological ionic strength (Debye-length caveat for FET `sensor_LOD`). SPR Kd and FET LOD are different quantity types. Aptamer sequences are in Table S1 (SI not fully re-typed here). “Real-time” in the abstract is not millisecond neurotransmission; reset pauses readout at V_CE = +0.8 V. Do not transfer 10 fM to Hu ACV or Abrantes gFET.

**Inspected quantities (CNT FET, 0.1× PBS unless noted):**

| Quantity | Glutamate-specific report | Tag |
| --- | --- | --- |
| SPR `Kd_molecular` | 293 nM (paper writes “293 nm”; same unit style as “dopamine (20 nm)”) | `primary-source-supported` |
| practical `sensor_LOD` | 10 fM for all four NTs including glutamate | `primary-source-supported` in 0.1× PBS |
| glutamate calibration window in real-time panels | 10 fM–100 nM (Fig. 3f); others shown to 100 µM | `primary-source-supported` |
| static transfer-curve incubation | 1 h in 0.1× PBS | assay incubation, not kon |
| real-time stabilization | ~200 s after 10 nM target | `response_time` of this real-time `I_ds` trace |
| PDR reset | V_CE = 0.8 V for 40 s; “within 1 min” unbound | reset time, not glutamate koff in tissue |
| complex matrix | PC12 medium and 10-fold diluted culture supernatants | not undiluted CSF/serum/tissue |

---

### C03-06

- **title:** Rapid Multianalyte Quantification of Brain Chemistry Using Si-Nanoribbon Bio-Field-Effect Transistor Sensors
- **year:** 2025 (epub 2025 Oct 17; print 2025 Oct 29)
- **journal:** ACS Applied Materials & Interfaces
- **authors:** Maldonado J; Rajagopalan V; Gu Y; Eid T; Spencer DD; Zaveri HP
- **DOI:** 10.1021/acsami.5c15695
- **PMID:** 41104714
- **PMCID:** (empty)
- **source_type:** primary
- **why it matters for THIS assigned lane:** Fourth FET architecture: **CMOS Si-nanoribbon bio-FET**. Aptamers for **lactate and glutamate**; **monoclonal antibody** for GABA (mixed receptor types on one platform). Abstract reports glutamate `sensor_LOD` 58 fM and quantification **within 10 min** in buffer **and aCSF**.
- **full_text_inspected:** no
- **access_route:** abstract-only (Unpaywall closed)
- **limitation:** Sequence, immobilization chemistry, `Kd_molecular`, `signal_gain`, and whether 10 min is incubation vs electronics `measurement_time` are not in the abstract. GABA channel is **not** an aptamer. Do not transfer 58 fM to other FETs. “Continuous real-time” language in the opening sentence is not evidenced as subsecond glutamate kinetics by the abstract.

**Abstract-supported quantities:** `sensor_LOD` glutamate = 58 fM `primary-source-supported` (abstract; matrix named as buffer and aCSF together — which matrix the 58 fM belongs to is **not split** in the abstract → treat matrix assignment as `unresolved` until VoR). Assay time “within 10 min” → `measurement_time` or incubation; not distinguished. `transferable`: unknown.

---

### C03-07

- **title:** A peptide aptamer based electrochemical amperometric sensor for sensitive L-glutamate detection
- **year:** 2022 (epub 2022 May 18; print 2022 Aug)
- **journal:** Bioelectrochemistry
- **authors:** Wang W; He Y; Gao Y; Gao H; Deng L; Gui Q; Cao Z; Yin Y; Feng Z
- **DOI:** 10.1016/j.bioelechem.2022.108165
- **PMID:** 35623273
- **PMCID:** (empty)
- **source_type:** primary
- **why it matters for THIS assigned lane:** Explicit **non-nucleic-acid** glutamate “aptamer”: ferrocene-peptide on gold, **amperometry** at 0.10 V in PBS. Gives a `response_time` (“optimum response within 200 s”) and `sensor_LOD` 1.00×10⁻¹⁰ M with two sensitivity segments, plus **100-fold diluted mouse serum** vs HPLC. Needed so peptide-sensor numbers are not merged with DNA glu1/NG-Apt-Glu devices.
- **full_text_inspected:** no
- **access_route:** abstract-only
- **limitation:** Peptide, not SELEX nucleic acid. Umami/CNS framing; not a neuroprobe. Do not transfer LOD or 200 s to DNA aptasensors. Abrantes Table 1 restates this paper’s LOD as 0.1 nM — that secondary table is not an independent measurement.

**Abstract-supported quantities:** `response_time` ≤ 200 s at 0.10 V in PBS `primary-source-supported`. `sensor_LOD` 1.00×10⁻¹⁰ M `primary-source-supported`. Sensitivity 0.1572 μA/M (1.00×10⁻⁷–1.00×10⁻³ M) and 0.0293 μA/M (1.00×10⁻¹⁰–1.00×10⁻⁷ M) `primary-source-supported`. Matrix: PBS; mouse serum 100-fold diluted `primary-source-supported`. `transferable`: no.

---

### C03-08

- **title:** Recent Advances in Aptamer-Based Sensors for Sensitive Detection of Neurotransmitters
- **year:** 2023 (2023-03-23)
- **journal:** Biosensors (Basel)
- **authors:** Park JH; Eom YS; Kim TH
- **DOI:** 10.3390/bios13040413
- **PMID:** 37185488
- **PMCID:** PMC10136356
- **source_type:** review
- **why it matters for THIS assigned lane:** OA table of neurotransmitter aptasensor architectures (FET, electrochemistry, optical). Directly useful as a **caution**: Table 1 and the following paragraph list **“Glutamate / FET / 100 fM–10 nM / 16.7, 48.6 pM”** while citing Singh et al. 2019, whose actual analyte is *P. falciparum* **glutamate dehydrogenase**, not glutamate. Demonstrates how secondary tables can collapse the wrong analyte into this lane.
- **full_text_inspected:** yes (PMC HTML)
- **access_route:** pmc
- **limitation:** Review. Glutamate-neurotransmitter DNA aptasensors are essentially absent except via that mis-labeled row (Wu 2022 is not the glutamate FET row). Use for error-checking, not as a source of LODs.

Claim: Park’s glutamate FET row is PfGDH, not Glu `primary-source-supported` by reading Park PMC **and** Singh 2019 identifiers (C03-11). `review-supported` only for the existence of the table; **not** for glutamate `sensor_LOD`.

---

### C03-09

- **title:** Development of an aptamer-based field effect transistor biosensor for quantitative detection of Plasmodium falciparum glutamate dehydrogenase in serum samples
- **year:** 2019 (epub 2018-09-26; print 2019 Jan)
- **journal:** Biosensors and Bioelectronics
- **authors:** Singh NK; Thungon PD; Estrela P; Goswami P
- **DOI:** 10.1016/j.bios.2018.09.085
- **PMID:** 30308419
- **PMCID:** (empty)
- **source_type:** primary
- **why it matters for THIS assigned lane:** Identifier-level control for C03-08. Target is **PfGDH protein**, aptamer NG3, extended-gate FET, `sensor_LOD` 16.7 pM (buffer) and 48.6 pM (serum), range 100 fM–10 nM. Those numbers must not enter glutamate-neurotransmitter architecture comparisons.
- **full_text_inspected:** no
- **access_route:** abstract-only (Unpaywall not re-queried as OA; Europe PMC closed)
- **limitation:** Not glutamate. Included only to block property transfer from the Park table.

---

### C03-10

- **title:** Real-Time, In Vivo Molecular Monitoring Using Electrochemical Aptamer Based Sensors: Opportunities and Challenges
- **year:** 2022 (epub 2022 Oct 7; print 2022 Oct 28)
- **journal:** ACS Sensors
- **authors:** Downs AM; Plaxco KW
- **DOI:** 10.1021/acssensors.2c01428
- **PMID:** 36205360
- **PMCID:** PMC9840907
- **source_type:** review
- **why it matters for THIS assigned lane:** Architecture-level distinction between **seconds-scale in vivo E-AB** (SWV) vs **sub-second interrogation** (chronoamperometry, IPA, EIS) vs **binding/equilibration**. States E-AB has been shown in veins and solid tissues of live animals for **drugs/metabolites**, not glutamate. Useful so “E-AB can be fast” is not silently attached to glutamate glu1 sensors whose published Glu assays use **minutes of incubation** (C03-02, C03-03, C03-04).
- **full_text_inspected:** yes (PMC author manuscript)
- **access_route:** pmc
- **limitation:** No glutamate aptamer, no glutamate `sensor_LOD`. Time-resolution examples are other targets. `transferable`: no.

**Review-supported (non-glutamate E-AB platform):** interrogation can be seconds (SWV) or sub-second (CA/IPA/EIS); measurements in undiluted serum/blood after drift correction. Not a glutamate result.

---

### C03-11

- **title:** Perspective—Assessing Electrochemical, Aptamer-Based Sensors for Dynamic Monitoring of Cellular Signaling
- **year:** 2023 (article issue date 2023 Dec 1; epub 2023 Dec 27)
- **journal:** ECS Sensors Plus
- **authors:** Rousseau CR; Kumakli H; White RJ
- **DOI:** 10.1149/2754-2726/ad15a1
- **PMID:** 38152504
- **PMCID:** PMC10750225
- **source_type:** review
- **why it matters for THIS assigned lane:** Makes the `response_time` vs `measurement_time` split explicit: Langmuir 10–90% occupancy spans an **81-fold** concentration window; electrochemical interrogation can be ≤2 ms while **equilibration** can be much slower; electrode size and distance set the sampled volume. Examples are ATP/cytokines/kanamycin, **not glutamate**. Needed to keep Hu/Wu **minute-scale ACV incubations** from being described as FSCV-like millisecond glutamate sensing.
- **full_text_inspected:** yes (PMC HTML)
- **access_route:** pmc
- **limitation:** Perspective; no glutamate aptamer data. 81-fold range is a Langmuir idealization, not a measured glutamate `analytical_working_range`.

---

### C03-12

- **title:** Aptamer based biosensor platforms for neurotransmitters analysis
- **year:** 2023 (Crossref issued 2023-05; OpenAlex publication_date 2023-03-13)
- **journal:** TrAC Trends in Analytical Chemistry
- **authors:** Hu Z; Li Y; Figueroa-Miranda G; Musall S; Li H; Martínez-Roque MA; Hu Q; Feng L; Mayer D; Offenhäusser A
- **DOI:** 10.1016/j.trac.2023.117021
- **PMID:** (empty — PubMed DOI search did not return this article)
- **PMCID:** (empty)
- **source_type:** review
- **why it matters for THIS assigned lane:** Same Jülich group’s survey of aptamer NT platforms immediately before the glutamate MEA/retina devices. Xiao 2025 cites it. Would map which transduction classes existed for glutamate vs DA/5-HT **if** an OA copy appears; currently closed.
- **full_text_inspected:** no
- **access_route:** abstract-only (Unpaywall `closed`; OpenAlex `is_oa=false`)
- **limitation:** No PMID verified. Cannot extract glutamate `sensor_LOD` tables without VoR. Do not use snippets from secondary sites as numbers.

---

### C03-13

- **title:** Capture-SELEX: Selection Strategy, Aptamer Identification, and Biosensing Application
- **year:** 2022 (2022-12-07)
- **journal:** Biosensors (Basel)
- **authors:** Lam SY; Lau HL; Kwok CK
- **DOI:** 10.3390/bios12121142
- **PMID:** 36551109
- **PMCID:** PMC9776347
- **source_type:** review
- **why it matters for THIS assigned lane:** Secondary source that **cites Wu 2022** (reference 73) in a Capture-SELEX review. Relevant only to identify that 1d04/glu1 entered the review literature as a glutamate Capture-SELEX → electrochemical sensor example. Not used here to copy numerical LODs.
- **full_text_inspected:** partial (PMC HTML scanned for glutamate/1d04/glu1 body text; Wu 2022 appears in the reference list)
- **access_route:** pmc
- **limitation:** Not an architecture paper. Any Kd quoted in reviews must be re-checked against Wu VoR (closed here). This scout did **not** extract a ± error bar for the 12 µM Kd because it is not in the Wu abstract.

---

## Near-misses (not counted in the 8–15; recorded for negative-search integrity)

| Item | IDs | Why examined | Why not a glutamate nucleic-acid aptasensor architecture candidate |
| --- | --- | --- | --- |
| Receptor-mediated RGO FET of hippocampal glutamate release | Li et al. 2019 *Anal. Chem.* DOI 10.1021/acs.analchem.9b00832 PMID 31142114 (Europe PMC + PubMed esearch; Unpaywall closed) | Tissue/neuron glutamate, FET | Biorecognition is **synthesized mGluR**, not an aptamer |
| Redox-labeled stimuli-responsive **polymer** for Glu/His | Ahmadian-Alam et al. 2024 *ACS Appl. Polym. Mater.* DOI 10.1021/acsapm.4c00121 PMID 39444408 PMC11498899 | Electrochemical glutamate, SPR Kd 2.40 μM polymer-Glu | Not an aptamer |
| Aptamer-FETs overcoming Debye length | Nakatsuka et al. 2018 *Science* DOI 10.1126/science.aao6750 PMID 30190311 PMC6663484 | FET architecture, small-molecule NTs | Europe PMC abstract: serotonin, dopamine, glucose, sphingosine-1-phosphate — **not glutamate** |
| Implantable aptamer-FET neuroprobes | Zhao et al. 2021 *Sci. Adv.* DOI 10.1126/sciadv.abj7422 PMID 34818033 PMC8612678 | in vivo NT FET | Europe PMC abstract: serotonin in brain tissue — **not glutamate** |
| Graphene microtransistor in vivo | Wu et al. 2022 *Nano Lett.* DOI 10.1021/acs.nanolett.2c00289 PMID 35439419 PMC9420334 | in vivo graphene FET | Europe PMC abstract: dopamine demonstration — **not glutamate** |
| Hu et al. 2023 truncated E-AB serotonin + PEG | DOI 10.3390/bios13090881 PMID 37754115 PMC10527390 | Immobilization/antifouling later used on Glu MEA | **Serotonin**, not glutamate; LOD not transferable |
| Enzymatic glutamate oxidase electrodes (many) | e.g. DOI 10.3390/s20102924 PMID 32455706 | Fast enzymatic glutamate | Enzyme, not aptamer |
| iGluSnFR / FSCV multiplexing | Shrestha et al. 2025 *J. Neurochem.* PMID 40621619 | Biological glutamate time scale | Protein indicator / carbon-fiber voltammetry |
| Capacitive malaria aptasensor | Singh et al. 2018 DOI 10.1016/j.bios.2018.06.022 PMID 29909195 | Title contains glutamate | Target is PfGDH antigen |
| Flexible parylene glutamate sensor (2011) | Kotake et al. IEEE NER DOI 10.1109/ner.2011.5910550 (Crossref: 2011; authors Kotake, Suzuki, Fukayama, Mabuchi; **no PMID** in Europe PMC) | Tissue-like flexible probe | Europe PMC hitCount=0 for this DOI; not identified here as a nucleic-acid aptamer paper. Not used for LOD transfer. |

**Optical glutamate DNA aptasensor:** no primary paper with extractable `sensor_LOD` found on the free routes above. SPR in Xiao is an **affinity** assay for aptamer screening, not the reported glutamate quantification architecture.

---

## Identifiers attempted but not verified

| String | Attempt | Result |
| --- | --- | --- |
| 10.18154/rwth-2025-07238 | Crossref `/works/{doi}`; Unpaywall `/v2/{doi}` | HTTP 404 both. Do not treat as a verified DOI. Thesis located by RWTH record 1017243. |
| PMID for 10.1016/j.trac.2023.117021 | PubMed esearch on the DOI | No hit (query parser split the DOI). PMID left empty. |
| Wu 2022 PMCID | PubMed esummary 34783880; Unpaywall; Europe PMC | none |
| Abrantes PMID | Europe PMC DOI search | preprint; PMID empty |
| JuSER “Fresenius' journal… 44, 1609–1622” for Wu 2022 | JuSER HTML snippet vs Crossref/PubMed | **Disagreement.** Bibliographic sources agree on *Anal. Bioanal. Chem.* 414:1609–1622. |
| Park glutamate FET LOD 16.7 / 48.6 pM as neurotransmitter glutamate | Park PMC vs Singh 2019 abstract | **Not glutamate.** Verified as PfGDH. |
| Lam 2022 body quotation of 1d04 Kd ± error | PMC9776347 grep | Wu 2022 is in the reference list; this scout did not verify a ±6 µM figure from Lam’s body. |

---

## Architecture map for extractors (not a thesis)

All rows are **candidates**. Empty cells were not inspected in a VoR.

| Candidate | Transduction | Construct (as stated) | Matrix actually used | `sensor_LOD` (that paper) | Time quantity (that paper) |
| --- | --- | --- | --- | --- | --- |
| C03-01 Wu 2022 | ACV, Fc-glu1 on Au/MCH | truncated DNA glu1; parent 1d04 | 10× diluted human serum (abstract) | 0.0013 pM (abstract) | not in abstract |
| C03-02 Hu 2025 MEA | ACV, Fc-Glu-apt on AuED-MEA/PEG | truncated DNA citing Wu | PBS; 50% serum; aCSF | 32 pM PBS; 51.5 pM 50% serum | ~15 min Glu incubation |
| C03-03 Hu thesis Ch. 6 | ACV on parylene retinal probe | Glu aptamer, PA + PEG | PBS-like cal; 50% serum; Ames; **mouse retina** | 0.3 pM (buffer cal) | ~10 min to plateau; ACV ~14 s; 1 min sampling in tissue |
| C03-04 Abrantes preprint | graphene FET, PBASE | 58-nt NG-Apt-Glu; also glu1 on same gFET | 1× aCSF; human CSF | 1 aM (NG-Apt-Glu, aCSF); 10 aM (glu1 on same gFET) | 1 h cal incubation; 10 min CSF; 20 transfer curves <1 s **after** incubation |
| C03-05 Xiao 2025 | CNT FET | pH-responsive DNA aptamer; SPR Kd 293 nM | 0.1× PBS; diluted PC12 medium | 10 fM practical (0.1× PBS) | 1 h static; ~200 s real-time stabilize; 40 s reset |
| C03-06 Maldonado 2025 | Si-nanoribbon bio-FET | glutamate **aptamer** (sequence not in abstract) | buffer and aCSF (abstract) | 58 fM (abstract) | within 10 min (abstract) |
| C03-07 Wang 2022 | amperometry, Fc-peptide | **peptide**, not DNA | PBS; 100× mouse serum | 1.00×10⁻¹⁰ M | optimum response within 200 s |

**Hypothesis (not a result):** published glutamate **nucleic-acid** aptasensors in this set are dominated by **minutes-scale incubation + sweep** or **highly diluted FET buffers**, whereas millisecond synaptic glutamate is a different `biological_concentration_range` / timescale problem. That hypothesis is for later contradiction-hunting; this scout does not adopt it as a thesis.

**Falsifier for a future “aptamer sensor already reports synaptic glutamate in vivo” claim:** a primary experiment that (i) uses a named nucleic-acid glutamate aptamer, (ii) reports `response_time` or `koff` on the same immobilized construct, (iii) in undiluted CSF, brain, or retina, and (iv) with `measurement_time` short enough to sample the claimed biological transient — none of the candidates above jointly satisfy (i)–(iv).

---

## Claim-tag summary (substantive statements in this record)

- Identifier/metadata facts from PubMed, Europe PMC, Crossref, Unpaywall, PMC: treated as bibliographic, not scientific claims.
- Numerical sensor metrics: tagged in each candidate as `primary-source-supported` only when read from that paper’s abstract or inspected OA full text for **that** architecture.
- Docking/MD in Abrantes: `computational illustration`.
- Park glutamate FET table row as neurotransmitter glutamate: **rejected** after checking Singh 2019; the mislabel is `primary-source-supported` as a review error.
- In vivo glutamate nucleic-acid aptasensor: `unresolved` (not found).
- Optical glutamate DNA aptasensor with LOD: `unresolved` (not found on the routes above).

**Promotion:** none to `core`. Orchestrator may ingest these as `candidate` rows only.
