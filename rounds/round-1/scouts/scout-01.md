# Round 1 literature scout 01

- Scout: 1 of 6
- Lane (search focus, not a conclusion): glutamate-binding DNA/RNA aptamers — selection, sequences/constructs, reported `Kd_molecular`, selectivity vs related amino acids
- Date of search: 2026-09-11
- Status: **candidates only**. Nothing promoted to `core`.
- Isolation: this record was written without reading other scout reports, theses, claims ledgers, or nightly summaries for conclusions.

Provisional central question (context only; not answered here): Can an aptamer actually keep up with neurochemical signaling? What do affinity, selectivity, binding kinetics, sensor transduction, immobilization and biological context jointly determine about the usefulness of a glutamate aptamer biosensor?

## Quantity and transfer rules used while reading

Every number below is tied to a named construct, phase, and assay when the source stated them. The following are kept separate: `Kd_molecular`, `kon`, `koff`, `EC50`, `sensor_LOD`, `analytical_working_range`, `signal_gain`, `response_time`, `measurement_time`, `biological_concentration_range`.

Do not transfer:

- parent aptamer `Kd_molecular` to a truncated oligo
- solution `Kd_molecular` to a surface-bound/electrochemical apparent Kd or FET `sensor_LOD`
- one buffer/matrix to another
- docking scores to wet-lab Kd

unless the cited experiment is on that same construct and condition.

Claim tags used: `primary-source-supported`, `review-supported`, `computational illustration`, `hypothesis`, `proposed experiment`, `unresolved`.

---

## Search strategy (negative-search integrity)

Free routes only: PubMed/eutils, Europe PMC, Crossref, OpenAlex, Unpaywall, PMC HTML, publisher OA HTML, J-STAGE, RWTH Publications, bioRxiv. No Sci-Hub, no paid APIs, no PDFs committed to git.

**Queries (representative):**

1. PubMed Title/Abstract: `(glutamate OR "glutamic acid") AND (aptamer OR SELEX)` → 58 hits (2026-09-11).
2. Europe PMC: `(TITLE:glutamate OR TITLE:"glutamic acid") AND (TITLE:aptamer OR ABSTRACT:aptamer)`.
3. PubMed: `"1d04" OR Capture-SELEX glutamate`; `RNA aptamer AND (glutamate OR "glutamic acid" OR "amino acid")`.
4. Europe PMC: `"1d04" OR glu1 AND glutamate AND aptamer`.
5. OpenAlex search: `glutamate DNA aptamer SELEX`.
6. Crossref works: `10.1007/s00216-021-03783-w` and related DOIs; Unpaywall OA flags.
7. Targeted follow-ups: `glutamine riboswitch` L-glutamate ITC; Yarus RNA–amino acid compilations; J-STAGE Ohsawa 2008; RWTH Hu thesis/paper; Xiao 2025 PMC; Abrantes bioRxiv.

**What the hit lists were actually full of (near-misses, not glutamate-oligo binders):**

- RNA aptamers to **glutamate receptors** (AMPA/kainate/NMDA; Niu, Huang, Jergova, Du, Park JS, Lee). These are receptor antagonists, not free-glutamate binders.
- Aptamers to **glutamate dehydrogenase** (PfGDH malaria; *C. difficile* GDH). A review table can mislabel these as neurotransmitter glutamate (Park 2023; see candidate 14).
- Dual-aptamer cancer sensors that happen to use **poly(glutamic acid)** films (Yazdanparast 2018).
- Peptide, not nucleic-acid, glutamate binders (Wang 2022).
- Generic small-molecule Capture-SELEX / FluMag-SELEX methods with non-glutamate targets.

**Negative-search result for unmodified RNA SELEX against free glutamate:**

- Yarus 2009 compiles 337 independent RNA sites to **8** amino acids; Yarus 2017 Figure 1 draws Val, Ile, Leu, Gln, Phe, Tyr, Trp, His, Arg. **Glutamate and aspartate are not in that drawn set.** `review-supported` for absence from those compilations; not a proof that no RNA glutamate aptamer exists anywhere.
- Ohsawa 2008, after 17 rounds of arginine-modified DNA SELEX against immobilised glutamic acid, states they could not obtain an aptamer bound to **free** glutamic acid. `primary-source-supported` for that authors’ conclusion.
- Natural *glnA* RNA binds **L-glutamine** and, on Ren 2015 ITC constructs, does not bind L-glutamate. That is Gln-RNA chemistry, not a glutamate biosensor aptamer.

**Identifiers attempted but not fully verified / not retrieved:**

| Attempt | Outcome |
| --- | --- |
| Wu et al. VoR full text DOI `10.1007/s00216-021-03783-w` | Unpaywall `is_oa: false`; Europe PMC `isOpenAccess: N`; JuSER record 904340 HTML empty in this environment. **No PMCID.** Abstract only. |
| Wu `12 ± 6 μM` | Appears in Lam 2022 review table citing Wu; **not** in the PubMed/Europe PMC abstract (abstract says `12 µM` without ±). Not confirmed from Wu VoR. |
| Wu glu1 `Kd_molecular` and amino-acid competitor panel | Not in abstract. `unresolved` until VoR/supplement is OA-inspected. |
| Xiao 2025 Table S1 sequences | Main PMC HTML inspected; Wiley SI download returned HTTP 500. Sequence origin of the SPR glutamate aptamer is `unresolved`. |
| Ames & Breaker 2011 PMC3127080 full text | PMCID and DOI verified; PubMed abstract/figure captions inspected; PMC PDF/HTML timed out here. Glutamate-rejection experiments in Ames itself therefore `unresolved` from this scout (Ren 2015 ITC is independently inspected). |
| Kuwahara 2005 OA PDF (`academic.oup.com/nass/article-pdf/...`) | Unpaywall `is_oa: true`; fetch timed out. Abstract only. |
| Hu 2025 thesis Crossref DOI | No DOI found. Locator: `https://publications.rwth-aachen.de/record/1017243`. |
| PMID 41548790 (from a noisy “Xiao glutamate aptamer” PubMed query) | Verified as PSMA RNA aptamer A10-3.2 photothermal therapy — **not glutamate**. Discarded. |
| Unpaywall with `email=research@example.com` | HTTP 422. Succeeded with a real-form email. |

---

## Construct map observed in OA text (not a thesis)

These are **different oligos**. Do not collapse them.

| Nickname in sources | Length / chemistry | Where it appears | What was actually measured in the text I could inspect |
| --- | --- | --- | --- |
| Wu **1d04** | Parent Capture-SELEX DNA; Lam quotes 98 nt | Wu abstract; Lam table | Abstract: `Kd_molecular` **12 µM** (assay, buffer, n not in abstract). `unresolved` beyond abstract. |
| Wu **glu1** | Truncation of 1d04; Fc + thiol; gold/MCH; ACV | Wu abstract | `sensor_LOD` **0.0013 pM**; `analytical_working_range` **0.01 pM–1 nM**; serum selectivity claimed. **No glu1 Kd in abstract.** |
| Hu **Glu-apt** | 36 nt = 5′ of the Lam 98-nt string, thiol-Fc | Hu 2025 paper + thesis | Authors **cite** Wu `Kd = 12 μM` for this truncated oligo (`review-supported`/`unresolved` transfer). Electrochemical Langmuir–Freundlich **apparent Kd 1.8 nM** is **not** `Kd_molecular`. |
| Abrantes **NG-Apt-Glu** | 58 nt = 5′ 58 of the same 98-nt string | bioRxiv 2025 | ELONA apparent Kd **10.3–25.1 mM**; docking scores are `computational illustration`; gFET `sensor_LOD` **1 aM** in aCSF. |
| Xiao SPR glutamate aptamer | Sequence in Table S1 (not retrieved) | Xiao 2025 | SPR `Kd` printed **293 nm** for glutamate; FET work in **0.1× PBS**. Not shown to be 1d04/glu1. |
| Ohsawa clones 2/6/8 | Arginine-modified dU DNA | Ohsawa 2008 | SPR vs **avidin–biotin-glutamate conjugates**, not free Glu. Authors: no free-Glu aptamer. |
| Ames/Ren *glnA* RNA | Natural Gln riboswitch | Ames 2011; Ren 2015 | Gln binder; Ren ITC: **does not bind L-glutamate**. |

---

## Candidate sources (15)

### 1. Wu et al. 2022 — parent Capture-SELEX DNA and glu1 sensor

- **title:** Highly selective and sensitive detection of glutamate by an electrochemical aptasensor
- **year:** print 2022; epub 2021-11-16. Crossref `published-print` 2022-02; `published-online` 2021-11-16. Lam 2022 cites this as 2021. **Do not silently pick one year.**
- **journal:** Analytical and Bioanalytical Chemistry
- **authors:** Changtong Wu; Daria Barkova; Natalia Komarova; Andreas Offenhäusser; Mariia Andrianova; Ziheng Hu; Alexander Kuznetsov; Dirk Mayer
- **DOI:** `10.1007/s00216-021-03783-w`
- **PMID:** `34783880`
- **PMCID:** (empty; none on PubMed/Europe PMC)
- **source_type:** `primary`
- **why it matters for THIS lane:** This is the only PubMed-verified primary that names a Capture-SELEX DNA aptamer (**1d04**) isolated against glutamic acid and reports a parent `Kd_molecular`. The same abstract distinguishes a **truncated** construct (**glu1**) used as a thiol/Fc electrochemical sensor. That split is the load-bearing construct boundary for later Hu/Abrantes truncations.
- **full_text_inspected:** `no`
- **access_route:** `abstract-only`
- **limitation:** VoR is closed (Unpaywall `is_oa: false`). Abstract does not state the Kd assay, buffer, temperature, n, or whether 12 µM is 1d04 in solution. Abstract does not give the 1d04 or glu1 sequences. glu1 numbers in the abstract are `sensor_LOD` / `analytical_working_range`, not `Kd_molecular`. “Good selectivity … in tenfold diluted human serum” is a matrix claim, not a published Asp/Gln ratio in the abstract. `unresolved`: amino-acid selectivity panel; glu1 Kd; kon/koff.

**Tagged claims from the inspected abstract only** (`primary-source-supported` as abstract wording; not VoR-confirmed):

- Glutamic acid-selective oligonucleotides were isolated from an ssDNA library by Capture-SELEX in complex medium.
- Aptamer **1d04** had a dissociation constant of **12 µM** (`Kd_molecular` as labeled by the authors; assay unspecified).
- Truncated **glu1**, Fc at 3′, Au–thiol, 6-mercapto-1-hexanol backfill, characterised by ACV.
- glu1 aptasensor `sensor_LOD` **0.0013 pM**; range **0.01 pM–1 nM**.

---

### 2. Lam, Lau, Kwok 2022 — Capture-SELEX review quoting 1d04 sequence and ±6 µM

- **title:** Capture-SELEX: Selection Strategy, Aptamer Identification, and Biosensing Application
- **year:** 2022
- **journal:** Biosensors
- **authors:** Sin Yu Lam; Hill Lam Lau; Chun Kit Kwok
- **DOI:** `10.3390/bios12121142`
- **PMID:** `36551109`
- **PMCID:** `PMC9776347`
- **source_type:** `review`
- **why it matters for THIS lane:** The OA table is the only inspected source that prints a **98-nt** glutamate DNA sequence and a **12 ± 6 μM** Kd, both citing Wu. Later truncations (Hu 36 nt; Abrantes 58 nt) are prefixes of this string.
- **full_text_inspected:** `yes`
- **access_route:** `pmc`
- **limitation:** Secondary. The table does not re-measure Kd, does not name the assay/buffer, and does not say whether 12 ± 6 μM belongs to 1d04, glu1, or “the” 98-nt oligo. Sequence and ±6 must not be treated as VoR-verified Wu numbers. `review-supported` only.

**Quoted from Lam Table (OA), citing Wu as [73]:**

- Target: Glutamate, CAS 56-86-0
- Sequence: `GCATCAGTCCACTCGTGAGGTCGACTGATGAGGCTCGATCAGGAGCGCCGCTCGATCGCACTTTCACAGGATAGTAGTTGGTAGCGACCTCTGCTAGA`
- Length 98; Kd **12 ± 6 μM**
- Sensor row: glutamate EIS/electrochemical `sensor_LOD` 0.0013 pM; range 0.01 pM–1 nM (same Wu citation)

---

### 3. Ohsawa et al. 2008 — arginine-modified DNA SELEX; no free-glutamate aptamer

- **title:** Arginine-modified DNA Aptamers That Show Enantioselective Recognition of the Dicarboxylic Acid Moiety of Glutamic Acid
- **year:** 2008
- **journal:** Analytical Sciences
- **authors:** Kazuomi Ohsawa; Toshiyuki Kasamatsu; Jun-ichi Nagashima; Kazuo Hanawa; Masayasu Kuwahara; Hiroaki Ozaki; Hiroaki Sawai
- **DOI:** `10.2116/analsci.24.167`
- **PMID:** `18187867`
- **PMCID:** (empty)
- **source_type:** `primary`
- **why it matters for THIS lane:** Independent, earlier attempt to select a glutamic-acid binder. Library is **not** natural DNA: TTP replaced by C5-arginyl dUTP. Selection used biotinylated glutamic acid on streptavidin-Sepharose. SPR Kd values are against **avidin–biotin-amino-acid conjugates**, not free Glu. Authors conclude they did not obtain an aptamer to free glutamic acid. Directly limits any claim that “glutamate DNA aptamers have been around since 2008.”
- **full_text_inspected:** `yes`
- **access_route:** `html` (J-STAGE publisher page/PDF converted to text; Unpaywall still listed `is_oa: false` — metadata disagreement, access was via J-STAGE)
- **limitation:** Modified nucleotides are required (natural-T replacements lost gel binding). SPR analytes are protein conjugates. Do not transfer conjugate Kd to free Glu, or modified DNA to unmodified DNA. Internal unit inconsistency: Methods inject **30–1000 μM** analyte; Figure 5 caption says “approximately 50–450 mM”. Reported here, not silently “corrected.”

**Tagged from inspected VoR** (`primary-source-supported` unless noted):

- Selection buffer: 20 mM Tris–HCl, pH 7.6, 300 mM NaCl, 5 mM MgCl2. SPR running buffer: 20 mM Tris–HCl, pH 7.6, 150 mM KCl, 5 mM MgCl2.
- 17 rounds; clones 2, 6, 8 sequenced (variable regions in Table 2; `t` = arginine-modified dU).
- SPR `Kd_molecular` vs conjugates: aptamer 2–AvD **720 ± 28 μM**; aptamer 6–AvD **810 ± 30 μM**; aptamer 6–AvG **580 ± 25 μM**. Association/dissociation too fast for kinetic fits (box sensorgrams).
- PEGylated free amino acids TL/TD gave no useful SPR signal.
- Conclusion sentence: “Unfortunately, at this time, we could not obtain an aptamer bound to the glutamic acid.”

---

### 4. Kuwahara et al. 2005 — symposium note preceding Ohsawa

- **title:** Screening of a glutamic acid-binding aptamer from arginine-modified DNA library
- **year:** 2005
- **journal:** Nucleic Acids Symposium Series
- **authors:** Masayasu Kuwahara; Kazuomi Ohsawa; Toshiyuki Kasamatsu; Atsushi Shoji; Hiroaki Sawai; Hiroaki Ozaki
- **DOI:** `10.1093/nass/49.1.81`
- **PMID:** `17150643`
- **PMCID:** (empty)
- **source_type:** `primary`
- **why it matters for THIS lane:** Documents that the 2008 modified-DNA campaign started as a glutamic-acid SELEX from an arginyl-dU library. No Kd in the inspected abstract.
- **full_text_inspected:** `no`
- **access_route:** `abstract-only` (Unpaywall flags publisher OA PDF; fetch timed out)
- **limitation:** Two-page symposium note. Do not treat it as an independent Kd source. Likely superseded by Ohsawa 2008.

---

### 5. Hu et al. 2025 — truncated Glu-apt on MEAs (sequence + cited vs apparent Kd)

- **title:** Potential-pulse-assisted co-immobilization of multiple aptamers on microelectrode arrays for multiplexed neurotransmitter detection
- **year:** 2025 (PubMed epub 2025-09-13; Crossref print 2025-12)
- **journal:** Biosensors and Bioelectronics
- **authors:** Ziheng Hu; Ruifeng Zhu; Gabriela Figueroa-Miranda; Lingyan Feng; Andreas Offenhäusser; Dirk Mayer
- **DOI:** `10.1016/j.bios.2025.117992`
- **PMID:** `40992279`
- **PMCID:** (empty)
- **source_type:** `primary`
- **why it matters for THIS lane:** Prints the **truncated glutamate oligo actually used** on gold MEAs and explicitly cites Wu for `Kd = 12 μM`. Also reports an electrochemical Langmuir–Freundlich **apparent Kd 1.8 nM** for that surface construct and states that it differs from solution-phase values. That is a documented solution→surface non-transfer.
- **full_text_inspected:** `yes`
- **access_route:** `other` (RWTH Publications OA PDF, record 1019759; Unpaywall `is_oa: true` / publisher; Crossref first license URL is Elsevier TDM — license-metadata disagreement)
- **limitation:** This paper does **not** re-select the aptamer. Selectivity shown is multiplex crosstalk among ST/Glu/DA, not Asp/Gln. 12 μM on the 36-nt probe is a Wu citation, not a new molecular Kd. Apparent 1.8 nM is surface electrochemical, not `Kd_molecular`.

**Sequence (HPLC, FRIZ Biochem), as printed:**

`5′-OH-(CH2)6-S-S-(CH2)6-GCA TCA GTC CAC TCG TGA GGT CGA CTG ATG AGG CTC GAT-Fc-3′`

Ungapped DNA: `GCATCAGTCCACTCGTGAGGTCGACTGATGAGGCTCGAT` (36 nt; 5′ of Lam’s 98-nt string).

**Tagged:**

- `Glu-apt, Kd = 12 μM (Wu et al., 2022)` — **citation of parent**, not a truncation remeasurement. Tag: `unresolved` as `Kd_molecular` of this 36-nt oligo.
- Electrochemical apparent Kd **1.8 nM** (Langmuir–Freundlich fit of ACV). Quantity type: **not** `Kd_molecular`; closest ledger types `EC50` / surface apparent affinity. Authors attribute the gap to 2D interface vs 3D solution. `primary-source-supported` for the fit on **this** electrode architecture.

---

### 6. Hu 2025 RWTH dissertation — OA construct/selectivity detail for the same Glu-apt

- **title:** Electrochemical Aptamer-Based Biosensing Platforms for Multiple Neurotransmitters Analysis
- **year:** 2025 (oral exam 14.08.2025; title-page date 18.08.2025)
- **journal:** RWTH Aachen University dissertation (Fakultät für Mathematik, Informatik und Naturwissenschaften)
- **authors:** Ziheng Hu
- **DOI:** (empty; not found on Crossref)
- **PMID:** (empty)
- **PMCID:** (empty)
- **source_type:** `primary` (thesis; chapters overlap Hu 2023/2025 papers)
- **why it matters for THIS lane:** OA full text of the same Glu-apt sequence; cites group Capture-SELEX Kd 12 μM then truncation (Wu). Intraretinal-probe selectivity panel is printed and **does not include aspartate or glutamine**.
- **full_text_inspected:** `yes`
- **access_route:** `other` (RWTH Publications `https://publications.rwth-aachen.de/record/1017243`)
- **limitation:** Not peer-reviewed as a single article. 12 μM remains a Wu citation. Selectivity vs 100 nM Glu compared with 10 μM ST, DA, tyrosine, L-lactate — **not** Asp/Gln. Probe LOD 0.3 pM (3×RSD of blank) and MEA LOD 32 pM are `sensor_LOD`, architecture-specific.

**Tagged from inspected thesis:**

- “Our group introduced a capture-SELEX protocol and successfully selected a Glu aptamer with a KD value of 12 μM. Afterwards, the aptamer sequence was truncated…” citing Wu. `review-supported`/`unresolved` as molecular Kd of the truncated probe.
- Selectivity (in vitro probe): 100 nM Glu vs 10 μM ST, DA, Tyr, Lac — small interferent responses. `primary-source-supported` for **that** panel only. Asp/Gln ratios: **not reported** (`unresolved`).

---

### 7. Xiao et al. 2025 — independent SPR Kd on a glutamate DNA aptamer (sequence in SI)

- **title:** In Situ Electrically Resettable Field-Effect Transistor Biosensors for Continuous and Multiplexed Neurotransmitter Detection
- **year:** 2025
- **journal:** Advanced Science
- **authors:** Bo Xiao; Tingxian Li; Xianmao Cao; Yang Zhang; Jianping He; Mengmeng Xiao; Zhiyong Zhang
- **DOI:** `10.1002/advs.202504497`
- **PMID:** `40433802`
- **PMCID:** `PMC12376627`
- **source_type:** `primary`
- **why it matters for THIS lane:** Reports an SPR dissociation constant for a glutamate aptamer that is **not** the Wu 12 µM figure: **293 nm** as printed next to dopamine 20 nm, serotonin 10.5 nm, histamine 15 nm. If this is a different oligo, it is an independent molecular-affinity datapoint. FET calibrations are in **0.1× PBS** (`sensor_LOD` / device response), not transferable to 1× PBS or tissue.
- **full_text_inspected:** `partial` (PMC HTML/XML yes; Supporting Information Table S1/Figure S6 not retrieved — Wiley SI HTTP 500)
- **access_route:** `pmc`
- **limitation:** Sequence not in the main text. Unclear whether SPR used the pH-triplex-modified oligo or the parent. Printed unit is `nm` in PMC HTML; in context it is a Kd, almost certainly nanomolar, but the SI sensorgram/fit was not inspected. Do not identify this oligo as 1d04/glu1 without Table S1. Do not transfer 293 nM to Wu or Hu constructs. Amino-acid selectivity of the **aptamer** (Asp/Gln) not given in the main text; FET specificity is vs other neurotransmitters in 0.1× PBS.

**Tagged:** SPR Kd glutamate **293 nm** (as printed), Figure S6. `primary-source-supported` for the main-text statement; fit details `unresolved` pending SI.

---

### 8. Abrantes et al. 2025 bioRxiv — 58-nt truncation, ELONA Kd vs docking vs FET LOD

- **title:** Ultrasensitive graphene FET aptasensor for direct attomolar detection of glutamate in human clinical samples
- **year:** 2025
- **journal:** bioRxiv
- **authors:** Mafalda Abrantes; Yolanda Blanco; Rafael P. Giacomazzi; Isabel P. Moreira; Patricia Monteiro; Jérôme Borme; Maria Vieira-Coelho; Sérgio F. Sousa; Carlos Briones; Luis Jacinto; Pedro Alpuim
- **DOI:** `10.1101/2025.11.05.686731`
- **PMID:** (empty)
- **PMCID:** (empty)
- **source_type:** `preprint`
- **why it matters for THIS lane:** Names parent **glu1d04** and prints the same 98-nt string as Lam, then a **58-nt** 3′-trim (`NG-Apt-Glu`) designed in silico. Reports **wet-lab ELONA Kd in the millimolar range** on that truncation **and** a gFET `sensor_LOD` of 1 aM — a documented truncation + assay-class split. Selectivity includes **glutamine and GABA** at the device level (not Asp).
- **full_text_inspected:** `yes` (bioRxiv HTML via DOI)
- **access_route:** `html`
- **limitation:** Not peer-reviewed. Docking/MD are `computational illustration`. ELONA uses hybridised capturer oligos; Kd is capturer-orientation-dependent. FET selectivity used 10 aM glutamate vs 1 pM interferents (unequal concentrations). Aspartate not in the panel. Do not transfer ELONA mM Kd to Wu 1d04 or to FET LOD.

**Sequences as printed:**

- Parent glu1d04 (citing Wu): `5'-GCATCAGTCCACTCGTGAGGTCGACTGATGAGGCTCGATCAGGAGCGCCGCTCGATCGCACTTTCAC AGGATAGTAGTTGGTAGCGACCTCTGCTAGA-3'` (space in HTML as retrieved)
- NG-Apt-Glu (58 nt): `5'-GCATCAGTCCACTCGTGAGGTCGACTGATGAGGCTCGATCAGGAGCGCCGCTCGATCG-3'`

**Tagged:**

- MFold / 3dRNA / MD / docking scores 33.86 (site B) and 30.15 (site A): `computational illustration`
- Inhibition ELONA Kd **10.3 to 25.1 mM**; %LOS 15.4 to 61.8: `primary-source-supported` for **NG-Apt-Glu + those capturers** (quantity is an assay Kd, not necessarily 1:1 `Kd_molecular` in free solution)
- gFET `sensor_LOD` **1 aM**; linear range **1 aM–10 pM**; 24 mV/decade in 1× aCSF
- Device response to 10 aM Glu **−81 ± 7 mV** vs 1 pM GABA, glutamine, dopamine, serotonin (small mV shifts): sensor-level selectivity, unequal doses; **not** molecular Kd ratios; **aspartate not tested**

---

### 9. Ames and Breaker 2011 — natural RNA aptamer for glutamine (related amino acid)

- **title:** Bacterial aptamers that selectively bind glutamine
- **year:** 2011
- **journal:** RNA Biology
- **authors:** Tyler D. Ames; Ronald R. Breaker
- **DOI:** `10.4161/rna.8.1.13864`
- **PMID:** `21282981`
- **PMCID:** `PMC3127080`
- **source_type:** `primary`
- **why it matters for THIS lane:** The best-characterised **natural RNA amino-acid aptamer** in the glutamate/glutamine chemical neighbourhood. PubMed figure captions give in-line-probing `Kd_molecular` **575 µM** for L-glutamine on 67 *glnA* RNA and **5 mM** for 83 DP RNA. This is a Gln binder. Useful as a selectivity contrast, not as a glutamate biosensor sequence.
- **full_text_inspected:** `partial` (PubMed abstract + figure captions; PMC full text timed out)
- **access_route:** `abstract-only`
- **limitation:** This scout did not inspect Ames VoR analog gels for L-glutamate. PubMed Figure 3 analog list (Ala-Gln, esters, theanine, homoglutamine, asparagine, …) **does not name glutamate** in the caption. Do not claim Ames measured glutamate rejection from this inspection. Do not transfer Gln Kd to glutamate.

**Tagged from PubMed figures:** 67 *glnA* in-line probing curve drawn for 1:1 binding with KD **575 µM** L-glutamine. `primary-source-supported` as caption; full-text gel not re-read here.

---

### 10. Ren et al. 2015 — ITC: *glnA* constructs bind Gln, do not bind L-glutamate

- **title:** Structural and Dynamic Basis for Low-Affinity, High-Selectivity Binding of L-Glutamine by the Glutamine Riboswitch
- **year:** 2015
- **journal:** Cell Reports
- **authors:** Aiming Ren; Yi Xue; Alla Peselis; Alexander Serganov; Hashim M. Al-Hashimi; Dinshaw J. Patel
- **DOI:** `10.1016/j.celrep.2015.10.062`
- **PMID:** `26655897`
- **PMCID:** `PMC4690532`
- **source_type:** `primary`
- **why it matters for THIS lane:** Wet-lab **selectivity vs L-glutamate** on a named RNA construct. ITC: GU glutamine riboswitch binds L-glutamine with `Kd_molecular` **117 μM** (no U1A) and **154 μM** (with U1A); NMR titration ~**280–590 μM**. ITC: **does not bind** D-glutamine, **L-glutamate**, L-asparagine (Fig. S1E / Table S1). Structural rationale: carboxamide vs charged carboxylate.
- **full_text_inspected:** `yes` (PMC HTML; Table S1 numeric “no binding” cells not independently re-tabulated beyond the sentence)
- **access_route:** `pmc`
- **limitation:** Crystallisation constructs replace loops with GAAA/U1A-binding loops. Not a SELEX glutamate aptamer. NMR/MD of conformational penalty are mixed experiment/simulation — simulations remain labelled as such. Do not use 117 μM as a glutamate Kd.

**Tagged:** ITC non-binding of L-glutamate on these *glnA* sensing-domain constructs. `primary-source-supported`. Ames citation that *glnA* motifs “strongly discriminate against … L-glutamate” is `review-supported` from this paper’s introduction, not a substitute for Ames VoR.

---

### 11. Yarus 2017 — OA map of RNA–amino-acid SELEX sites (Glu not drawn)

- **title:** The Genetic Code and RNA-Amino Acid Affinities
- **year:** 2017
- **journal:** Life
- **authors:** Michael Yarus
- **DOI:** `10.3390/life7020013`
- **PMID:** `28333103`
- **PMCID:** `PMC5492135`
- **source_type:** `review`
- **why it matters for THIS lane:** Figure 1 lists amino acids “studied by selection”: Val, Ile, Leu, Gln, Phe, Tyr, Trp, His, Arg. **Glutamate is not in that figure.** Negative-search documentation for free-amino-acid RNA SELEX compilations.
- **full_text_inspected:** `yes`
- **access_route:** `html` (MDPI OA)
- **limitation:** Compilation of origin-of-code SELEX, not a biosensor review. Absence from the figure is not a proof of non-existence. Ames 2011 is cited as a glutamine (riboswitch) reference.

---

### 12. Yarus, Widmann, Knight 2009 — 337 RNA sites / 8 amino acids compilation

- **title:** RNA-Amino Acid Binding: A Stereochemical Era for the Genetic Code
- **year:** 2009
- **journal:** Journal of Molecular Evolution
- **authors:** Michael Yarus; Jeremy Joseph Widmann; Rob Knight
- **DOI:** `10.1007/s00239-009-9270-1`
- **PMID:** `19795157`
- **PMCID:** (empty)
- **source_type:** `review`
- **why it matters for THIS lane:** Abstract: 337 independent RNA binding sites directed to **8 amino acids**. Glutamine is discussed as **hard to select** (low-affinity unpublished Scerch/Tocchini-Valentini sites; many Gln selections fail). Glutamate is not presented as one of the compiled free-aa RNA site classes in the inspected OA HTML.
- **full_text_inspected:** `yes`
- **access_route:** `html` (Springer OA)
- **limitation:** Same as candidate 11. 2009 says 8 amino acids; 2017 Figure 1 draws nine names — **do not silently reconcile**. Unpublished Gln Kd ≈ 2×10⁻² M is third-party unpublished and not a glutamate number.

---

### 13. Wang et al. 2022 — peptide aptamer (near-miss: not DNA/RNA)

- **title:** A peptide aptamer based electrochemical amperometric sensor for sensitive L-glutamate detection
- **year:** 2022
- **journal:** Bioelectrochemistry
- **authors:** Wenjing Wang; Yumin He; Yunling Gao; Hongrui Gao; Lei Deng; Qingwen Gui; Zhong Cao; Yulong Yin; Zemeng Feng
- **DOI:** `10.1016/j.bioelechem.2022.108165`
- **PMID:** `35623273`
- **PMCID:** (empty)
- **source_type:** `primary`
- **why it matters for THIS lane:** Shows that “glutamate aptamer sensor” in PubMed is **not always nucleic acid**. Sequence is a ferrocene-peptide SAM, not DNA/RNA. Keep it in the lane as a **negative inclusion control**.
- **full_text_inspected:** `no`
- **access_route:** `abstract-only`
- **limitation:** Closed VoR. Abstract `sensor_LOD` 1.00×10⁻¹⁰ M; `response_time` “optimum response within 200 s at 0.10 V”; two linear segments. No nucleic-acid Kd. Unpaywall `is_oa: false`.

---

### 14. Park, Eom, Kim 2023 — review that labels PfGDH as “glutamate”

- **title:** Recent Advances in Aptamer-Based Sensors for Sensitive Detection of Neurotransmitters
- **year:** 2023
- **journal:** Biosensors
- **authors:** Joon-Ha Park; Yun-Sik Eom; Tae-Hyung Kim
- **DOI:** `10.3390/bios13040413`
- **PMID:** `37185488`
- **PMCID:** `PMC10136356`
- **source_type:** `review`
- **why it matters for THIS lane:** Table 1 row “Au | Glutamate | FET | 100 fM–10 nM | 16.7, 48.6 pM”. Body text for that row describes an aptamer FET for ***Plasmodium falciparum* glutamate dehydrogenase**, not neurotransmitter glutamate. Documents a literature trap for this lane.
- **full_text_inspected:** `yes`
- **access_route:** `pmc`
- **limitation:** Do not harvest the table row as a glutamate-aptamer LOD. Underlying paper (body text): Singh et al. 2019, PMID `30308419`, DOI `10.1016/j.bios.2018.09.085` (PfGDH; not extracted as a glutamate-oligo candidate).

---

### 15. Stoltenburg, Nikolaus, Strehlitz 2012 — Capture-SELEX method (not glutamate)

- **title:** Capture-SELEX: Selection of DNA Aptamers for Aminoglycoside Antibiotics
- **year:** 2012
- **journal:** Journal of Analytical Methods in Chemistry
- **authors:** Regina Stoltenburg; Nadia Nikolaus; Beate Strehlitz
- **DOI:** `10.1155/2012/415697`
- **PMID:** `23326761`
- **PMCID:** `PMC3544269`
- **source_type:** `primary`
- **why it matters for THIS lane:** Founding **library-immobilised Capture-SELEX** protocol that Wu’s abstract says was used for glutamate. Needed to interpret what “Capture-SELEX in complex medium” could mean; **target here is kanamycin-class antibiotics, not glutamate**.
- **full_text_inspected:** `no`
- **access_route:** `abstract-only`
- **limitation:** No glutamate sequence or Kd. Do not transfer aminoglycoside aptamer properties to 1d04.

---

## Additional incomplete / off-lane records (not in the 15)

| ID | Why noted | Status |
| --- | --- | --- |
| Maldonado et al. 2025, DOI `10.1021/acsami.5c15695`, PMID `41104714` | Abstract: aptamer bioreceptors for lactate **and glutamate** on Si-nanoribbon FETs; glutamate `sensor_LOD` 58 fM; quantification within 10 min. | Unpaywall closed. **Sequence and `Kd_molecular` not in abstract.** Candidate for a later sensor-lane scout, not extractable here. |
| Jergova et al. 2025, DOI `10.1038/s42003-025-08772-8`, PMID `41006757`, PMC12475499 | RNA aptamers targeting **glutamate receptors**, SCI pain model. | Off-lane (receptor, not free Glu). |
| Singh et al. 2019 PMID `30308419` | PfGDH FET; the Park-table false friend. | Off-lane. |
| Liu et al. 2018 PMID `28882627` | DNA aptamers to *C. difficile* **glutamate dehydrogenase**. | Off-lane. |
| Nakatsuka et al. 2018 Science (PMID `30190311`) | DA/5-HT aptamer-FETs; Hu cites ST/DA Kd from this family, **not glutamate**. | Off-lane for selection; immobilisation/FET context only. |

---

## Lane-specific observations (no poster thesis)

These are inventory notes for extractors, not a slogan.

1. **Verified nucleic-acid glutamate SELEX in this search is thin.** The only PubMed primary that both (a) selects vs glutamic acid and (b) reports a parent Kd is Wu 2021/2022, and that VoR was **not** OA-inspectable here. `unresolved`: assay, buffer, n, sequence in Wu VoR, glu1 Kd, Asp/Gln panel.

2. **Three truncations of the same 98-nt string are already in circulation**, with incompatible number types:
   - 98 nt / 12 µM (Wu abstract; Lam ±6 µM)
   - 36 nt Glu-apt / cited 12 µM + electrochemical apparent 1.8 nM (Hu)
   - 58 nt NG-Apt-Glu / ELONA 10.3–25.1 mM + FET LOD 1 aM + docking (Abrantes)
   Transfer across these rows is not supported by the inspected experiments.

3. **Selectivity vs related amino acids is mostly missing or off-target.**
   - Hu probe panel: ST, DA, Tyr, Lac — not Asp/Gln. `unresolved` for Asp/Gln on Glu-apt.
   - Abrantes device panel: GABA, glutamine, DA, serotonin at 1 pM vs Glu at 10 aM — not Asp; not equal-concentration Kd ratios.
   - Wu abstract: diluted serum, competitors unnamed.
   - Ohsawa: enantioselectivity of **conjugates**, and authors reject free-Glu binding.
   - Ren: **Gln RNA rejects Glu** (ITC) — inverse of the biosensor question.

4. **No `kon`/`koff` for a glutamate DNA/RNA aptamer** was found in inspected OA text. Ohsawa SPR was too fast to fit. Hu discusses interface folding qualitatively. `unresolved`.

5. **Modified DNA (Ohsawa) and peptide (Wang) and GDH reviews (Park) will contaminate naive “glutamate aptamer” searches.**

6. **Wildcard examined:** natural glutamine riboswitch (Ames/Ren) as an RNA that must ignore glutamate. Kept as a selectivity chemistry comparator. **Rejected as a glutamate biosensor sequence.**

---

## Suggested extractor priorities (orchestrator; still candidates)

Highest information if VoR/OA allows:

1. Wu VoR + supplement: 1d04 vs glu1 sequences, Kd method/buffer, competitor list, whether 12 ± 6 μM is in the paper.
2. Xiao SI Table S1 / Fig S6: glutamate oligo sequence vs Wu; SPR buffer; whether 293 nm is nM.
3. Ames VoR analog gels for L-glutamate (this scout timed out).
4. Do **not** promote any of the above to `core` in Round 1.

---

## Integrity checklist

- No core promotion.
- No invented DOI/PMID/PMCID/Kd.
- Wu year and Hu/Unpaywall license disagreements stated, not silently resolved.
- Computational docking (Abrantes) labelled `computational illustration`.
- Parent vs truncated vs surface vs FET LOD not collapsed.
- No poster, no ledger edits (`state/claims.csv` untouched).
