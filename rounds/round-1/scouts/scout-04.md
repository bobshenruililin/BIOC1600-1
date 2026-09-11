# Round 1 literature scout 4 of 6

- scout_id: scout-04
- lane: immobilization and interface effects (surface attachment chemistry, orientation, crowding, fouling, solution Kd versus surface)
- status of all sources: candidate (promote nothing to core)
- search_date: 2026-09-11
- model: cursor-grok-4.6-xhigh
- isolation: did not read other Round 1 scout reports, theses, `state/claims.csv`, or nightly summaries for conclusions; did not spawn nested agents

## Assigned question (search focus only)

Can an aptamer actually keep up with neurochemical signaling? This lane searches immobilization and interface effects for aptamer glutamate sensors and closely related small-molecule sensors: surface attachment chemistry, orientation, crowding, fouling, and whether solution `Kd_molecular` transfers to the surface.

Do not treat this lane as a conclusion.

## Search strategy

Free routes only: Europe PMC REST, PubMed E-utilities, Crossref works API, OpenAlex, Unpaywall, PMC HTML, publisher OA HTML, HAL author manuscript, RWTH institutional OA HTML/PDF text (not committed). No Sci-Hub, no paid APIs, no copyrighted PDFs written into git.

Queries (representative):

- Europe PMC: glutamate AND (aptamer OR aptasensor) AND (immobiliz* OR thiol OR packing OR MCH OR fouling)
- Europe PMC title searches for packing density, solution-phase vs surface-phase affinity, DNA tetrahedron probe platform, potential-pulse co-immobilization, truncated antifouling serotonin aptasensor, Debye-length aptamer FETs, codeposition EAB, Au–C anchoring EAB
- Starting leads verified, not trusted: PMID 41851736 / DOI 10.1186/s12951-026-04194-8 (Tanner tetrahedron as interface evidence); White/Plaxco packing-density literature (DOI 10.1021/la800801v)
- Wildcard not specified by the parent prompt: replace Au–S with Au–C≡C anchoring for E-AB stability (Zhang 2026 *Chem. Sci.*)
- Negative / near-miss terms: glutamate aptamer packing density titration; glutamate aptamer DNA tetrahedron; glutamate solution Kd versus surface Kd on the same construct; Herne/Tarlov thiol-DNA SAM (hybridization, not aptamer)

Identifier cross-check: every nominated DOI was retrieved from Crossref; PMIDs from PubMed esummary and Europe PMC; PMCIDs from PubMed articleids where present; Unpaywall OA status independently.

## Candidate sources (n = 15)

All `status: candidate`. Quantity types below are those the cited experiment actually reports. `transferable` is from that experiment only.

---

### C04-01

- title: Highly selective and sensitive detection of glutamate by an electrochemical aptasensor
- year: print 2022 / electronic 2021 (disagreement recorded below)
- journal: Analytical and Bioanalytical Chemistry
- authors: Wu Changtong; Barkova Daria; Komarova Natalia; Offenhäusser Andreas; Andrianova Mariia; Hu Ziheng; Kuznetsov Alexander; Mayer Dirk
- DOI: 10.1007/s00216-021-03783-w
- PMID: 34783880
- PMCID: empty
- source_type: primary
- why it matters for THIS assigned lane: This is a glutamate nucleic-acid aptamer sensor that names the immobilization chemistry. PubMed/JuSER abstract: parent Capture-SELEX clone 1d04; truncated glu1 with 3′-ferrocene immobilized on gold via Au–thiol bonds; 6-mercapto-1-hexanol backfill; ACV readout. That is the glutamate-specific thiol/MCH architecture later reused by Hu 2025.
- full_text_inspected: partial
- access_route: abstract-only
- limitation: VoR is closed (Unpaywall `is_oa: False`). Packing density, orientation, and a same-construct solution-versus-surface Kd were not inspectable here. Abstract `Kd_molecular` is for 1d04; abstract `sensor_LOD` and `analytical_working_range` are for truncated surface-bound glu1. Those quantities must not be collapsed. `transferable`: unknown (truncation and surface attachment not supported by an inspected same-construct experiment in this scout).
- tagged observations from inspected abstract:
  - 1d04 `Kd_molecular` 12 µM (`primary-source-supported` at abstract level only; locator: PubMed abstract PMID 34783880).
  - glu1 `sensor_LOD` 0.0013 pM and `analytical_working_range` 0.01 pM–1 nM in the abstract (`primary-source-supported` at abstract level; not a molecular Kd).
  - Selectivity claimed in tenfold-diluted human serum (`primary-source-supported` at abstract level; matrix not undiluted CSF/brain).
- metadata disagreement: PubMed `pubdate` 2022 Feb, `epub` 2021 Nov 16; Crossref `issued` 2021-11-16; Unpaywall/OpenAlex year 2021. Do not silently pick one year.

---

### C04-02

- title: Potential-pulse-assisted co-immobilization of multiple aptamers on microelectrode arrays for multiplexed neurotransmitter detection
- year: 2025
- journal: Biosensors and Bioelectronics
- authors: Hu Ziheng; Zhu Ruifeng; Figueroa-Miranda Gabriela; Feng Lingyan; Offenhäusser Andreas; Mayer Dirk
- DOI: 10.1016/j.bios.2025.117992
- PMID: 40992279
- PMCID: empty
- source_type: primary
- why it matters for THIS assigned lane: Glutamate-containing multiplex E-AB on gold nanostructured MEAs. Inspected OA text: potential-pulse-assisted (PA) co-immobilization of thiolated aptamers with thiol-PEG; site-selective electrodesorption to place ST, Glu, and DA aptamers on different channels; packing/orientation compared with drop-casting; authors themselves attribute electrochemical apparent Kd versus cited solution values to 2D confinement.
- full_text_inspected: yes
- access_route: unpaywall
- limitation: Elsevier HTML was blocked in this environment; inspected the CC BY published version via RWTH OA (`https://publications.rwth-aachen.de/record/1019759/files/1019759.pdf`). Text was not committed. Glu sequence is the truncated Wu glu1 construct; cited solution `Kd` 12 µM is from Wu 2022 (parent 1d04 in Wu’s abstract), not a new solution titration of this immobilized oligo. ACV recorded after 15 min Glu incubation (`measurement_time`), not synaptic `response_time`. `transferable`: no for Wu 1d04 `Kd_molecular` → glu1 surface apparent Kd; unknown for this MEA architecture → other electrodes or in vivo brain.
- tagged observations from inspected OA text:
  - Glu-apt sequence given as 5′-HO-(CH2)6-S-S-(CH2)6-GCATCAGTCCACTCGTGAGGTCGACTGATGAGGCTCGAT-Fc-3′, cited `Kd = 12 μM` from Wu et al. 2022 (`primary-source-supported` as a citation in Hu; not a new molecular measurement here).
  - Optimal PA pulse +0.6/+0.1 V, 1 s; surface coverage 1.43 ± 0.37 × 10^13 molecules/cm² versus drop-casting 1.22 ± 0.44 × 10^13 molecules/cm²; PA in 5 min versus overnight drop-casting (`primary-source-supported`; locator: Hu 2025 results, immobilization section).
  - Authors state PA gives higher `signal_gain` and they attribute that to improved orientation versus drop-casting (`primary-source-supported` as the authors’ interpretation of their comparison).
  - Electrochemical apparent Kd (Langmuir–Freundlich fit to ACV): 1.8 nM Glu, 2.7 nM ST, 49.6 µM DA. Authors explicitly say these differ from solution-phase reports because of confined 2D folding/binding (`primary-source-supported` for the electrochemical apparent Kd on this sensor; not `Kd_molecular`).
  - Glu `sensor_LOD` 32 pM in buffer; 51.5 pM in 50% serum; `analytical_working_range` 0.1 nM–10 µM (semi-log); ACV after 15 min Glu incubation (`measurement_time`) (`primary-source-supported`).
  - Thiol-PEG backfill: recoveries in 50% serum; authors attribute antifouling to hydrophilic PEG (`primary-source-supported` for this PEG-blocked MEA, not for MCH-only glutamate sensors).

---

### C04-03

- title: In Situ Electrically Resettable Field-Effect Transistor Biosensors for Continuous and Multiplexed Neurotransmitter Detection
- year: 2025
- journal: Advanced Science
- authors: Xiao Bo; Li Tingxian; Cao Xianmao; Zhang Yang; He Jianping; Xiao Mengmeng; Zhang Zhiyong
- DOI: 10.1002/advs.202504497
- PMID: 40433802
- PMCID: PMC12376627
- source_type: primary
- why it matters for THIS assigned lane: Glutamate is one of four FET channels. Inspected PMC HTML: aptamers attached through Au–S on Au nanoparticles on HfO2-gated CNT FETs; excess Au–S sites passivated with MCH; SPR affinities reported separately from FET calibration in 0.1× PBS.
- full_text_inspected: yes
- access_route: pmc
- limitation: FET calibration is in 0.1× PBS, not physiological ionic strength. SPR `Kd` and FET `sensor_LOD` are different quantity types on different interfaces. PMC HTML dropped the first given name; Crossref lists Xiao Bo. Sequence table is in Supporting Information (not fully extracted here). Not in vivo brain. `transferable`: no for SPR `Kd_molecular` → FET `sensor_LOD`; unknown for 0.1× PBS → CSF/brain; unknown for this CNT/AuNP stack → gold E-AB.
- tagged observations from inspected PMC HTML:
  - Immobilization: Au NPs capture sulfhydryl probes by Au–S; excess sites passivated with MCH (`primary-source-supported`; locator: Xiao 2025, sensor configuration / Figure 3b).
  - SPR affinities: dopamine 20 nM, serotonin 10.5 nM, histamine 15 nM, glutamate 293 nM (`primary-source-supported` as SPR `Kd` on that SPR chip; locator: Figure S6 cited in main text). Quantity type: `Kd_molecular` only if the SPR experiment is accepted as molecular; it is still a surface SPR measurement, so treat as surface SPR Kd, not a solution ITC Kd.
  - Practical FET detection claimed at 10 fM; dopamine/histamine/serotonin traces described as 10 fM–100 µM in 0.1× PBS (`primary-source-supported` as FET `sensor_LOD` / working range in 0.1× PBS).
  - Reset uses a pH-sensitive triplex extension, i.e. a different construct than the parent aptamer (`primary-source-supported`; do not transfer affinity from the unextended aptamer).

---

### C04-04

- title: Ultrasensitive graphene FET aptasensor for direct attomolar detection of glutamate in human clinical samples
- year: 2025
- journal: bioRxiv (preprint; Crossref `posted-content`)
- authors: Abrantes Mafalda; Blanco Yolanda; Giacomazzi Rafael P.; Moreira Isabel P.; Monteiro Patricia; Borme Jérôme; Vieira-Coelho Maria; Sousa Sérgio F.; Briones Carlos; Jacinto Luis; Alpuim Pedro
- DOI: 10.1101/2025.11.05.686731
- PMID: empty
- PMCID: empty
- source_type: preprint
- why it matters for THIS assigned lane: Glutamate-specific graphene FET. Europe PMC abstract: graphene FET arrays functionalized with DNA aptamer NG-Apt-Glu; in silico design plus biochemical characterization; aCSF and clinical CSF. Interface architecture is the immobilization question for a glutamate FET, even though the inspected abstract does not name thiol chemistry or packing density.
- full_text_inspected: partial
- access_route: abstract-only
- limitation: Not peer-reviewed. bioRxiv HTML returned HTTP 429 in this session; Unpaywall lists green OA at the DOI. Immobilization chemistry, crowding, and a solution-versus-device Kd pair were not inspectable from the abstract. Computational binding-site claims in the abstract are `computational illustration` until a wet-lab same-construct measurement is inspected. `transferable`: unknown.
- tagged observations from inspected Europe PMC abstract:
  - `sensor_LOD` 1 aM in aCSF; `analytical_working_range` 1 aM–10 pM; 24 mV/decade (`primary-source-supported` at abstract level only).
  - Aptamer designed/characterized computationally and biochemically; two putative binding sites (`computational illustration` for the in silico part; biochemical details not in the inspected abstract).

---

### C04-05

- title: Optimization of Electrochemical Aptamer-Based Sensors via Optimization of Probe Packing Density and Surface Chemistry
- year: 2008
- journal: Langmuir
- authors: White Ryan J.; Phares Noelle; Lubin Arica A.; Xiao Yi; Plaxco Kevin W.
- DOI: 10.1021/la800801v
- PMID: 18690727
- PMCID: PMC2674396
- source_type: primary
- why it matters for THIS assigned lane: Founding packing-density / SAM-thickness experiment for E-AB. Inspected PMC HTML: cocaine (small molecule) and thrombin (protein) thiolated MB-aptamers on gold; RuHex chronocoulometry packing; MCH versus shorter hydroxythiols; gain, apparent Kd, and equilibration time all change with density and SAM.
- full_text_inspected: yes
- access_route: pmc
- limitation: Not glutamate. Europe PMC flags `isOpenAccess: N`; Unpaywall green / PMC author manuscript. Cocaine apparent Kd versus a cited solution Kd of 100 µM is the authors’ comparison, not a glutamate transfer. `transferable`: unknown to glutamate glu1/MCH sensors; no to thrombin protein crowding → small-molecule glutamate.
- tagged observations from inspected PMC HTML:
  - Cocaine packing 1.2 × 10^11 to 4.4 × 10^12 molecules/cm²; thrombin 5.7 × 10^11 to 1.3 × 10^13 molecules/cm² (`primary-source-supported`).
  - Cocaine `signal_gain` 60% at high density to ~200% at 1.6 × 10^12 molecules/cm² (`primary-source-supported`).
  - Hyperbolic apparent Kd for cocaine sensors fabricated at 25, 60, 500 nM probe: 327 ± 64, 101 ± 8, 127 ± 35 µM; authors call these comparable to a cited solution Kd of 100 µM (`primary-source-supported` for the surface fits; the solution 100 µM is a citation, not re-measured here).
  - Cocaine high-density sensors equilibrate within ~4 s `response_time`; thrombin equilibration time constant doubles from 11 to 20 min as density increases 40-fold (`primary-source-supported`; protein vs small molecule).
  - C2 vs C6 SAM at 1.6 × 10^12 molecules/cm²: C2 gain reduced ~10-fold; apparent Kd 18 ± 5 µM (C2) vs 95 ± 15 µM (C6) (`primary-source-supported`). Thinner SAM is not a free lunch.

---

### C04-06

- title: Immobilization Strategies for Enhancing Sensitivity of Electrochemical Aptamer-Based Sensors
- year: 2021
- journal: ACS Applied Materials & Interfaces
- authors: Liu Yingzhu; Canoura Juan; Alkhamis Obtin; Xiao Yi
- DOI: 10.1021/acsami.0c20707
- PMID: 33448791
- PMCID: PMC7933091
- source_type: primary
- why it matters for THIS assigned lane: Direct test that conventional high-salt thiol/MCH immobilization can crowd/bundle aptamers. Inspected PMC HTML: target-assisted immobilization of folded aptamer–target complexes; ITC `Kd_molecular` / `K1/2` measured in the actual immobilization buffers; same average packing can give different `signal_gain` and `sensor_LOD` if local spacing differs.
- full_text_inspected: yes
- access_route: pmc
- limitation: Adenosine, cocaine, MDPV — not glutamate. Unpaywall green / submittedVersion PMC. `transferable`: unknown to glutamate glu1; no across targets. Demonstrates that immobilization-buffer affinity is not optional metadata.
- tagged observations from inspected PMC HTML:
  - ADE-25 ITC `K1/2` 27.6 ± 0.2 µM in low-salt Tris vs 23.1 ± 0.8 µM in high-salt PBS (`primary-source-supported`; quantity `Kd_molecular` / ITC K1/2; locator: Figure S1).
  - COC-32 ITC `KD` 70.4 ± 0.8 µM in high-salt PBS immobilization buffer (`primary-source-supported`).
  - Target-bound vs aptamer-alone immobilization at matched surface density improves cocaine `sensor_LOD` 1 vs 2 µM in buffer (`primary-source-supported`).
  - Low-salt vs high-salt immobilization at matched density improves cocaine gain; 50% saliva `sensor_LOD` 2 vs 4 µM (`primary-source-supported`).
  - SC-34 MDPV ITC `KD` 300 nM in low-salt Tris (`primary-source-supported`); increasing target during immobilization slightly lowers coverage, consistent with a bulkier complex.

---

### C04-07

- title: Influence of Aptamer Surface Coverage on Small Target Recognition: A SPR and QCM-D Comparative Study
- year: 2019
- journal: The Journal of Physical Chemistry C
- authors: MacDonald Hannah (Crossref); OpenAlex: Hannah E. Bruce Macdonald; HAL PDF byline: Hannah Macdonald; Bonnet Hugues; Van der Heyden Angéline; Defrancq Eric; Spinelli Nicolas; Coche-Guérente Liliane; Dejeu Jérôme
- DOI: 10.1021/acs.jpcc.9b00845
- PMID: empty
- PMCID: empty
- source_type: primary
- why it matters for THIS assigned lane: Small-molecule (L-tyrosinamide, 180 Da) oriented monolayer. Inspected HAL author manuscript: biotin/streptavidin immobilization with mixed EG thiols; coverage 0.7–5.5 pmol cm−2; apparent Kd, `kon`, and `koff` versus spacing; comparison to cited solution Kd 1–3 µM.
- full_text_inspected: yes
- access_route: unpaywall
- limitation: HAL is `submittedVersion`, not ACS VoR. No PMID (Europe PMC DOI query returned 0). L-Tym, not glutamate. Streptavidin capture is not Au–thiol E-AB. Author-name strings disagree across Crossref/OpenAlex/HAL. `transferable`: unknown to glutamate; no to a different immobilization chemistry.
- tagged observations from inspected HAL manuscript:
  - Cited solution Kd 1–3 µM (`review-supported` / citation in this paper, not re-measured as ITC in the inspected text).
  - QCM-D `KDapp` 160 µM at smallest spacing (highest coverage) to 13 µM at largest spacing (lowest coverage); threshold near 2.5 pmol cm−2 / ~9 nm spacing (`primary-source-supported` for this L-Tym monolayer).
  - SPR: `koff` ~0.04 s−1 independent of density; `kon` ~1500 M−1 s−1 at low coverage, ~3.5-fold lower at high coverage (`primary-source-supported`; quantities `koff`, `kon`, not `Kd_molecular`).
  - Authors state crowded-surface `KDapp` is about two orders of magnitude weaker than homogeneous-solution values, and about one order at low coverage (`primary-source-supported` as their comparison). `transferable`: no for crowded L-Tym `KDapp` → solution Kd.

---

### C04-08

- title: Solution-Phase vs Surface-Phase Aptamer-Protein Affinity from a Label-Free Kinetic Biosensor
- year: 2013
- journal: PLoS ONE
- authors: Daniel Camille; Roupioz Yoann; Gasparutto Didier; Livache Thierry; Buhot Arnaud
- DOI: 10.1371/journal.pone.0075419
- PMID: 24069412
- PMCID: PMC3775802
- source_type: primary
- why it matters for THIS assigned lane: Explicit same-paper measurement of `KD Sol` versus `KD Surf` as a function of grafting density, with PEG mixed SAM and T10 spacer. This is the cleanest inspected experiment on whether solution affinity transfers to a surface.
- full_text_inspected: yes
- access_route: pmc
- limitation: Thrombin protein, not a small-molecule glutamate aptamer. `KD Surf` numerical table is in figures; main text gives `KD Sol` = 3.16 ± 1.16 nM and states `KD Surf` is density-dependent and extrapolates to `KD Sol` at low σ, without a single headline `KD Surf` number in the inspected prose. `transferable`: no to glutamate.
- tagged observations from inspected PMC HTML:
  - Probe density 5.3 ± 0.4 to 7.9 ± 0.7 pmol/cm² depending on 10 or 20 µM thiol-aptamer in the droplet, with 10 µM MeO-PEG-SH (`primary-source-supported`).
  - Competition-assay `KD Sol` averaged 3.16 ± 1.16 nM, independent of grafting density (`primary-source-supported`; quantity `Kd_molecular` from solution competition read out on the chip).
  - `KD Surf` from Langmuir isotherms at 2, 4, 6, 6.8, 8 pmol/cm² differs from `KD Sol` and extrapolates linearly toward `KD Sol` at low density (`primary-source-supported`; quantity is surface apparent Kd). Authors credit PEG passivation and T10 spacer for low residual surface interactions.
  - `sensor_LOD` 100 pM thrombin; linear 0.2–20 nM (`primary-source-supported`; protein SPR, not glutamate).

---

### C04-09

- title: A DNA Nanostructure-based Biomolecular Probe Carrier Platform for Electrochemical Biosensing
- year: 2010
- journal: Advanced Materials
- authors: Pei Hao; Lu Na; Wen Yanli; Song Shiping; Liu Yan; Yan Hao; Fan Chunhai
- DOI: 10.1002/adma.201002767
- PMID: 20839255
- PMCID: PMC3071359
- source_type: primary
- why it matters for THIS assigned lane: Founding DNA-tetrahedron immobilization: three basal thiols, pendant probe, defined spacing/orientation on gold. Inspected PMC HTML: TSP vs linear ssDNA/MCH; MCH optional for TSP; lower BSA adsorption than MCH; extension to a thrombin aptamer tetrahedron.
- full_text_inspected: yes
- access_route: pmc
- limitation: Primary payload is DNA hybridization, not glutamate. Thrombin aptamer extension is protein. Unpaywall green / PMC manuscript. `transferable`: unknown to glutamate aptamers; no for hybridization LOD → glutamate sensor LOD.
- tagged observations from inspected PMC HTML:
  - SPR surface density 4.8 × 10^12 TSP cm−2 (8.0 pmol cm−2); estimated inter-probe spacing ~4.0 nm (`primary-source-supported`).
  - Hybridization `sensor_LOD` 1 pM vs 250 pM for ssDNA/MCH with similar HRP transduction (authors: 250-fold) (`primary-source-supported` for that sandwich DNA assay).
  - TSP electrodes without MCH produced amperometric signals comparable to MCH-treated TSP (`primary-source-supported`).
  - BSA adsorption on TSP ~1/4 of MCH; still more than OEG (`primary-source-supported`; fouling comparison on those SAMs).
  - Thrombin aTSP `sensor_LOD` 100 pM, stated as three orders of magnitude lower than a cited ssDNA aptamer sensor (`primary-source-supported` for aTSP; the comparison is a citation).

---

### C04-10

- title: Nanoplasmonic optical fiber sensing of SARS-CoV-2 nucleocapsid protein using an aptamer-DNA tetrahedron interface
- year: 2026
- journal: Journal of Nanobiotechnology
- authors: Xu Pin; Cui Jingyu; Cheng Zhi; Shiu Simon Chi-Chin; Cui Jingxian; Li Yujian; Liu Yifan; Wang Lin; Siu Ryan Ho Ping; Tanner Julian A.; Yu Changyuan
- DOI: 10.1186/s12951-026-04194-8
- PMID: 41851736
- PMCID: PMC13112887
- source_type: primary
- why it matters for THIS assigned lane: Starting lead. Same-device comparison of linear thiol-aptamer/MCH versus aptamer–DNA tetrahedron on gold-coated fiber. Inspected PMC HTML: three thiols on the tetrahedron base, Apt48 displayed on top, MCH passivation, AFM height 5.65 nm, LOD comparison.
- full_text_inspected: yes
- access_route: pmc
- limitation: SARS-CoV-2 N protein, not glutamate. Use as interface evidence only. PubMed/Crossref invert Chinese given/family names (Pin X …); OpenAlex and PMC affiliations support Xu Pin as first author. OpenAlex lists “Weiyin Lin”; PMC/Crossref list Wang Lin — recorded, not guessed. `transferable`: unknown to glutamate.
- tagged observations from inspected PMC HTML:
  - Linear Apt48: 5 µM thiol-aptamer 60 min, then 2 mM MCH 45 min (`primary-source-supported`).
  - DNT-Apt48: 17-base edges; three thiolated strands plus Apt48 extension; AFM height increase 5.65 nm vs bare gold, matching expected tetrahedron-plus-aptamer height (`primary-source-supported`).
  - Signal intensity ~2.5× versus aptamer alone (abstract); LOD = 3σ/slope: Apt48 46 nM, DNT-Apt48 34 nM (`primary-source-supported`; quantity `sensor_LOD` for N protein on this fiber).
  - Detection of 0.6 µM N protein in artificial saliva (`primary-source-supported`; matrix ≠ brain).

---

### C04-11

- title: Truncated Electrochemical Aptasensor with Enhanced Antifouling Capability for Highly Sensitive Serotonin Detection
- year: 2023
- journal: Biosensors
- authors: Hu Ziheng; Zhu Ruifeng; Figueroa-Miranda Gabriela; Zhou Lei; Feng Lingyan; Offenhäusser Andreas; Mayer Dirk
- DOI: 10.3390/bios13090881
- PMID: 37754115
- PMCID: PMC10527390
- source_type: primary
- why it matters for THIS assigned lane: Same group as C04-02; precursor interface: truncated stem-loop thiol-aptamer plus 2 kDa MeO-PEG-thiol versus lying-down aptamers at short PEG times. AFM/QCM-D of orientation; aCSF + albumin challenge.
- full_text_inspected: yes
- access_route: pmc
- limitation: Serotonin, not glutamate. Truncation changes the construct; Nakatsuka solution `Kd` 30 nM is cited, not re-measured for S2 on the electrode. `transferable`: unknown to glutamate glu1; no from parent ST aptamer to truncated S2.
- tagged observations from inspected PMC HTML:
  - Overnight 0.5 µM thiol-aptamer in high-salt Tris, then 1 mg/mL PEG; AFM: aptamer-only roughness 0.96 ± 0.02 nm, unordered/lying; PEG yields more upright morphology (`primary-source-supported`).
  - QCM-D: aptamer Δf 5.05 Hz; PEG 7.05 Hz; ST 0.45 Hz (`primary-source-supported`).
  - `analytical_working_range` 0.1 nM–1 µM ST in PBS; `sensor_LOD` 0.14 nM (`primary-source-supported`).
  - Cited parent `Kd_molecular` 30 nM from Nakatsuka (`review-supported` / citation in this paper).
  - Selectivity vs 1 µM UA/DA/AA at 10 nM ST; aCSF with 45 mg dL−1 HSA used as a fouling mimic (`primary-source-supported` for those matrices).

---

### C04-12

- title: Week-Long Operation of Electrochemical Aptamer Sensors: New Insights into Self-Assembled Monolayer Degradation Mechanisms and Solutions for Stability in Serum at Body Temperature
- year: 2023
- journal: ACS Sensors
- authors: Watkins Zach; Karajic Aleksandar; Young Thomas; White Ryan; Heikenfeld Jason
- DOI: 10.1021/acssensors.2c02403
- PMID: 36884003
- PMCID: PMC10443649
- source_type: primary
- why it matters for THIS assigned lane: Fouling and SAM failure, not a new glutamate binder. Inspected PMC HTML: mixed alkylthiolate/aptamer monolayers in undiluted serum at 37 °C; chain length, scanning window, membranes, zwitterions; 30–50% rapid redox-tag current drop attributed to fouling.
- full_text_inspected: yes
- access_route: pmc
- limitation: Not glutamate. Unpaywall green / PMC manuscript. Week-long serum stability is not synaptic-timescale evidence. `transferable`: unknown to glutamate glu1/MCH MEAs; no from serum 37 °C → brain interstitial fluid without a glutamate experiment.
- tagged observations from inspected PMC HTML:
  - Conventional MCH mixed monolayers on polished gold: rapid initial 30–50% redox-tag current drop in protein-rich fluids (`primary-source-supported`; quantity is signal loss, not Kd).
  - Week-long operation in bovine serum at 37 °C claimed after longer alkylthiolates, optimized voltammetry, and membrane or zwitterion fouling control (`primary-source-supported` for those E-AB devices).
  - Fouling can preserve peak current while still constraining aptamer motion over days (`primary-source-supported` as the authors’ mechanistic claim from their multi-day data).

---

### C04-13

- title: Aptamer-field-effect transistors overcome Debye length limitations for small-molecule sensing
- year: 2018
- journal: Science
- authors: Nakatsuka Nako; Yang Kyung-Ae; Abendroth John M.; Cheung Kevin M.; Xu Xiaobin; Yang Hongyan; Zhao Chuanzhen; Zhu Bowen; Rim You Seung; Yang Yang; Weiss Paul S.; Stojanović Milan N.; Andrews Anne M.
- DOI: 10.1126/science.aao6750
- PMID: 30190311
- PMCID: PMC6663484
- source_type: primary
- why it matters for THIS assigned lane: Orientation / Debye-length interface for small-molecule aptamer FETs. Inspected PMC HTML: silane attachment of stem-loop aptamers to In2O3; physiological Debye length <1 nm; FET response in 1× PBS/aCSF; fluorescence solution Kd versus FET working range.
- full_text_inspected: yes
- access_route: pmc
- limitation: Dopamine, serotonin, glucose, S1P — not glutamate. Science VoR vs NIHMS/PMC manuscript. FET `sensor_LOD` in 10−14–10−9 M is not the fluorescence `Kd_molecular`. `transferable`: unknown to glutamate FETs; no for DA/5-HT Kd → glutamate.
- tagged observations from inspected PMC HTML:
  - Fluorescence `Kd_molecular`: dopamine 150 nM, serotonin 30 nM, glucose ~10 mM, S1P 180–190 nM (`primary-source-supported`; locator: Fig. 1 and fig. S2).
  - Aptamer-FETs respond 10−14 to 10−9 M in undiluted PBS or aCSF on the order of seconds (`primary-source-supported` as FET `response_time` / working range, not Kd).
  - Physiological Debye length <1 nm; authors argue stem-loop rearrangement of the charged backbone near the channel is required (`primary-source-supported` as their mechanistic interpretation plus FET/SERS/CD).
  - Changing the number of serotonin aptamers on the FET shifts the sensitive concentration window (Fig. 2F) (`primary-source-supported`; coverage/orientation control).

---

### C04-14

- title: Codeposition Enhances the Performance of Electrochemical Aptamer-Based Sensors
- year: 2024
- journal: Langmuir
- authors: Wu Yuyang; Shi Jinyuan; Kippin Tod E.; Plaxco Kevin W.
- DOI: 10.1021/acs.langmuir.4c00585
- PMID: 38616608
- PMCID: PMC11821552
- source_type: primary
- why it matters for THIS assigned lane: Attachment-chemistry variant of thiol/MCH: simultaneous aptamer+MCH codeposition versus sequential overnight MCH. Inspected PMC/escholarship text: vancomycin, tryptophan, phenylalanine small-molecule E-AB; packing falls ~2 orders of magnitude as MCH rises from 10 µM to 1 mM; additive with target-assisted deposition.
- full_text_inspected: yes
- access_route: pmc
- limitation: Not glutamate. Effect depends on whether the aptamer is unfolded until target binds (CD). `transferable`: unknown to glu1.
- tagged observations from inspected PMC HTML:
  - Vancomycin sequential gain 91 ± 1%; codeposition at 500 nM aptamer + 10 µM MCH gain 121 ± 4% (`primary-source-supported`; quantity `signal_gain`).
  - Packing ~10−13 mol/cm² across 100 nM–1 µM aptamer at 10 µM MCH; packing falls ~100-fold as MCH goes 10 µM → 1 mM (`primary-source-supported`).
  - Incomplete MCH (1 µM) gives oxygen-reduction baselines; excess MCH suppresses MB peaks (`primary-source-supported`).
  - 1 h codeposition matches overnight codeposition for gain and binding midpoints (`primary-source-supported`).
  - Phenylalanine (folded without target by CD) does not gain from codeposition or target-assisted deposition (`primary-source-supported`; construct-specific).

---

### C04-15 (wildcard: non-thiol anchoring)

- title: A robust Au–C≡C anchoring group greatly improves the signal stability of electrochemical aptamer-based sensors for in vivo measurements
- year: 2026
- journal: Chemical Science
- authors: Zhang Wanxue; Alsuwayni Bandar; Liu Jiamei; Wu Qingqing; Mei Ziyin; Hou Songjun; Zhang Zishuo; Du Xuewei; Yi Suyan; Li Shaoguang; Lambert Colin; Li Hui; Xia Fan
- DOI: 10.1039/d6sc02701f
- PMID: 42094668
- PMCID: PMC13139930
- source_type: primary
- why it matters for THIS assigned lane: Parent prompt named tetrahedron and packing-density leads. This paper tests a different attachment bond. Inspected PMC HTML: alkyne/HYO versus thiol/MCH matched for OH terminus and chain length; vancomycin E-AB; XPS/confocal of probe retention; whole-blood and in-rat monitoring.
- full_text_inspected: yes
- access_route: pmc
- limitation: Vancomycin drug E-AB, not glutamate. In vivo is pharmacokinetics, not glutamate neurotransmission. `transferable`: unknown to glutamate aptamers and to Hu/Wu thiol-PEG glutamate MEAs.
- tagged observations from inspected PMC HTML:
  - Model MB–C≡CH vs MB–SH: <10% electrochemical fluctuation over 72 h (~1200 scans) vs ~60% peak-current loss; confocal remaining MB >90% vs ~50% (`primary-source-supported`).
  - HYO vs MCH protein coverage 40.2% vs 50.6%; EIS resistance 10701.3 Ω vs 1109.2 Ω (`primary-source-supported`).
  - VAN–C≡CH E-AB: <10% PBS attenuation over 72 h (>6000 cycles); thiol analogue complete signal loss after 55 h (`primary-source-supported`).
  - Authors report 92% signal integrity over 72 h (>6000 scans) in whole blood (`primary-source-supported` for this vancomycin Au–C sensor).

---

## Identifiers attempted but not verified / disagreements

| Attempt | Result |
| --- | --- |
| Europe PMC `DOI:10.1021/acs.jpcc.9b00845` | 0 hits; no PMID |
| Europe PMC `DOI:10.1021/ja9719586` (Herne/Tarlov 1997) | 0 hits; no PMID; Crossref/OpenAlex confirm the DOI |
| Europe PMC `TITLE:"Influence of Aptamer Surface Coverage"` | 0 hits |
| Wu 2022 year | PubMed print 2022 Feb / epub 2021-11-16; Crossref issued 2021-11-16; Unpaywall year 2021 |
| Tanner/Xu author strings | PubMed `Pin X; Jingyu C; …`; Crossref given/family inversion; OpenAlex `Xu Pin; … Wang Lin` vs one OpenAlex `Weiyin Lin`; PMC HTML dropped first given name |
| MacDonald given name | Crossref Hannah MacDonald; OpenAlex Hannah E. Bruce Macdonald; HAL PDF Hannah Macdonald |
| Pons 2022 OA flag | Unpaywall hybrid OA PDF; Europe PMC `isOpenAccess: N`; RSC HTML Cloudflare-blocked here |
| Abrantes 2025 full HTML | bioRxiv 429 in this session; Europe PMC abstract only |
| Hu 2025 Elsevier HTML | publisher page error; Unpaywall CC BY; RWTH OA PDF inspected, not committed |
| Wu 2022 VoR | Unpaywall closed; JuSER record is abstract-level |
| Xiao 2025 PMC HTML | first given name dropped; Crossref Xiao Bo used |

## Near-misses and negative-search notes

Inspected or identifier-checked but **not** nominated in the 15 (to avoid padding):

- Pons et al. 2022, *Analyst*, DOI 10.1039/d2an00824f, PMID 35983869. Same L-Tym group as C04-07; spacer length and immobilization mode can null or invert SPR signal even when QCM-D/ITC still report recognition (`KD` around 200 nM in the abstract). Full HTML not inspected (Cloudflare). Closely related; C04-07 already covers coverage.
- Herne TM; Tarlov MJ 1997, *JACS*, DOI 10.1021/ja9719586. Founding thiol-DNA then MCH. No PMID. Hybridization SAM, not aptamer folding. Abstract-only here.
- Steel AB; Herne TM; Tarlov MJ 1998, *Anal. Chem.*, DOI 10.1021/ac980037q, PMID 9844566. RuHex packing-density method used by White 2008. Not an aptamer-target paper.
- Gao et al. 2022, *Anal. Chem.*, DOI 10.1021/acs.analchem.1c05531, PMID 35678711, PMC9480490. Electrografting site-selective FET functionalization; DA/5-HT, no glutamate.
- Maldonado et al. 2025, *ACS AMI*, DOI 10.1021/acsami.5c15695, PMID 41104714. Si-nanoribbon FET brain chemistry including glutamate aptamer; VoR closed; sequence/Kd not inspectable.
- Petrek et al. 2025, *Langmuir*, DOI 10.1021/acs.langmuir.5c03116, PMID 40983868. AuNP crowding of thrombin aptamers; abstract-only; protein nanoparticle, not planar glutamate E-AB.
- Pham et al. 2025, *ACS Sens.*, DOI 10.1021/acssensors.5c01267, PMID 40591816. Blood components and E-AB drift; no PMCID; VoR not inspected.
- Shaver A; Arroyo-Currás N 2022, *Curr. Opin. Electrochem.*, PMID 36092288, PMC9455832. Review of long-term nucleic-acid E-AB stability, not a glutamate primary experiment.

**Negative search (glutamate-specific packing / same-construct solution-versus-surface Kd):** Europe PMC title/field searches did not return a paper that titrates glu1 packing density against `Kd_molecular` and surface apparent Kd on the same oligo in the same buffer. The closest glutamate-facing comparison in an inspected full text is Hu 2025 (C04-02), which reports electrochemical apparent Kd 1.8 nM for surface glu1 and cites Wu 12 µM — and Wu’s 12 µM is the parent 1d04 abstract value. That is not a same-construct transfer experiment. `unresolved` whether glu1 solution `Kd_molecular` equals glu1 surface apparent Kd.

**Negative search (glutamate DNA tetrahedron):** no glutamate aptamer–tetrahedron sensor was verified. C04-09 and C04-10 remain protein/hybridization interface analogues.

## Lane-level inventory (not a thesis)

What this scout can point an extractor at, without synthesizing a poster claim:

1. **Attachment chemistry (glutamate):** thiol-Au + MCH (C04-01 abstract); thiol-Au + thiol-PEG + potential pulses (C04-02 full text); AuNP Au–S + MCH on CNT FET (C04-03 full text).
2. **Crowding / packing:** cocaine/thrombin density–gain–time (C04-05); target-assisted unbundling (C04-06); L-Tym coverage vs `kon`/`KDapp` (C04-07); thrombin `KD Sol` vs `KD Surf` (C04-08); codeposition MCH ratio (C04-14). No glutamate packing series inspected.
3. **Orientation / spacer:** tetrahedron vs linear (C04-09, C04-10); PEG standing-up vs lying aptamer (C04-11); Debye-length stem-loop on FETs (C04-13); PA pulses claimed to improve orientation (C04-02).
4. **Fouling:** PEG on ST and Glu MEAs (C04-11, C04-02); serum SAM desorption (C04-12); HYO vs MCH protein pickup (C04-15).
5. **Solution versus surface:** C04-02 authors state electrochemical apparent Kd ≠ cited solution values because of 2D confinement; C04-07 crowded L-Tym `KDapp` weaker than cited solution Kd; C04-08 thrombin `KD Surf` ≠ `KD Sol` except in the low-density limit; C04-03 SPR glutamate 293 nM versus FET 10 fM-class response in 0.1× PBS. `transferable` is no or unknown in every glutamate-adjacent case inspected.

Wildcard retained: C04-15 (Au–C≡C vs Au–S). Direction examined because thiol desorption is a documented E-AB failure mode; not adopted as glutamate evidence.

No sources promoted to `core`. No claims written to `state/claims.csv`. No poster.
)
