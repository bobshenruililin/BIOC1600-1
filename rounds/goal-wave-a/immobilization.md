# Immobilization and property transfer

Lane: immobilization / property transfer (Goal Wave A). Independent worker; no nested agents. Not a poster. Not group-final.

**Question.** Where did papers (and this repo) silently or illegally transfer Kd, kinetics, or LOD across parent→truncated, soluble→surface-bound, buffer A→buffer B, or architecture A→architecture B? What does the interface actually do to nucleic-acid recognition?

**Provisional answer.** Immobilization is not a null operation, and glutamate papers repeatedly label one construct with another construct’s number. That is not the same as proving that the electrode *caused* the 12 µM → 1.8 nM jump. The jump mixes at least four hops. A uniform “2D confinement tightens Kd” law already fails inside Hu 2025: dopamine’s surface apparent Kd stays near the cited solution value while glutamate’s does not.

---

## 1. Method, access, negative search

Free routes only (PubMed, PMC, Europe PMC, Crossref, Unpaywall/RWTH OA, HAL, bioRxiv HTML). No Sci-Hub. No copyrighted PDFs committed. Numbers not re-located are left empty.

| Query / chain | What was opened | Result |
| --- | --- | --- |
| Wu 2022 1d04 vs glu1 | PubMed PMID 34783880; JuSER abstract | Abstract only. VoR still closed. `full_text_inspected=no` |
| Hu 2025 multiplex MEA | RWTH OA PDF `publications.rwth-aachen.de/record/1019759/files/1019759.pdf` | VoR re-read this session. `full_text_inspected=yes` |
| Hu 2023 truncated ST E-AB | PMC10527390 | VoR. `full_text_inspected=yes` |
| Hu 2025 thesis Ch. 6 | not re-fetched; used ledger S066 / orchestrator extract | Prior OA extract. `full_text_inspected=no` this session |
| White 2008 packing/SAM | PMC2674396 | `full_text_inspected=yes` |
| Daniel 2013 KD_sol vs KD_surf | PLOS ONE HTML + PMC3775802 | thrombin. `full_text_inspected=yes` |
| MacDonald 2019 L-Tym crowding | HAL `hal-02180487` (ACS was previously 403 in this repo) | small-molecule surface. `full_text_inspected=yes` |
| Liu/Xiao 2021 immobilization | NSF PAR PDF `par.nsf.gov/servlets/purl/10210214` | cocaine/adenosine/MDPV. `full_text_inspected=yes` |
| Ricci 2016 Acc. Chem. Res. | PMC5660318 | Langmuir 81-fold; cocaine truncation. **Not** Langmuir–Freundlich. `full_text_inspected=yes` |
| Nakatsuka 2018 Debye FET | eScholarship OA PDF of *Science* 362:319 | DA/5-HT, not Glu. `full_text_inspected=yes` |
| Xiao 2025 CNT FET | PMC12376627 XML + publisher HTML | Glu SPR vs FET. `full_text_inspected=yes` |
| Xu/Tanner 2026 tetrahedron fiber | PMC13112887 XML | N-protein, not Glu. `full_text_inspected=yes` |
| Lam 2022 Capture-SELEX review | PMC9776347 | 98-nt 1d04 string; `12 ± 6 µM` is the review’s table, not Wu’s abstract. `full_text_inspected=yes` |
| Abrantes 2025 preprint | bioRxiv HTML 10.1101/2025.11.05.686731 | in silico truncation of 1d04; docking scores; 1 aM LOD. ELONA millimolar **Kd not entered**. `full_text_inspected=partial` |
| Glutamate aptamer kon/koff | S001 abstract, S002 VoR, S021 PMC, S010 HTML | none found. `unresolved` |

**Negative-search integrity.** No paired solution-phase `Kd_molecular` of Hu’s Fc-thiol 39-mer was found in inspected OA text. No packing-density series for that oligo. No glutamate surface kon/koff. Ohsawa 2008 conjugate Kd remains unentered (JSTAGE previously 500). Wu truncation cut-sites remain behind the closed VoR.

**Wildcard (not in the parent prompt).** (i) Hu’s **dopamine** channel as an internal falsifier of “confinement always tightens Kd.” (ii) MacDonald L-tyrosinamide as a **small-molecule** crowding experiment (Daniel is protein). (iii) Abrantes MFold/docking truncation of 1d04 as a computational property transfer.

---

## 2. First-year objects (do not collapse)

| Object | What it is | Glutamate example |
| --- | --- | --- |
| `Kd_molecular` | 1:1 oligo–ligand Kd in a named phase | 1d04 12 µM in Wu abstract; Xiao SPR 293 nM |
| cited Kd | literature label, not a remeasurement | Hu methods “Glu-apt, Kd = 12 µM (Wu et al., 2022)” |
| `EC50` / apparent electrochemical Kd | half-maximal transduced signal; may be Langmuir–Freundlich | Hu Glu 1.8 nM |
| `sensor_LOD` | blank + 3SD (or 3RSD) of a transduced signal | Wu glu1 0.0013 pM; Hu MEA 32 pM PBS |
| `signal_gain` | fractional current change | White cocaine 60–200% |
| `response_time` | time to a new occupancy/signal plateau | Xiao multiplex ~200 s after 10 nM |
| `measurement_time` | wait or interrogation clock | Hu Glu 15 min ACV; Xiao static 1 h incubation |
| packing density | probes per area | Hu PA 1.43 ± 0.37 × 10¹³ cm⁻² (ST-optimized) |

Docking scores are not Kd. `computational illustration`.

---

## 3. The glutamate construct chain (what was actually measured)

```
Capture-SELEX isolate 1d04  --Kd 12 µM, abstract-->  truncated glu1 Fc-thiol-MCH E-AB  --LOD 0.0013 pM-->
         |                                                    |
         |  (sequence 5' 39 nt maps onto Hu oligo;            |  VoR truncation table not inspected
         |   Kd does not travel with the string)              |
         v                                                    v
Hu 2025 methods label the 39-mer "Kd = 12 µM"  ----citation, not a titration----
Hu 2025 surface ACV Langmuir–Freundlich apparent Kd 1.8 nM; LOD 32 pM PBS / 51.5 pM 50% serum
Hu 2025 thesis: same family on PaC probe; PBS LOD 0.3 pM; Ames window 10 nM–10 µM; retina 1 min sampling
Xiao 2025: different glutamate aptamer; SPR Kd 293 nM; CNT FET LOD 10 fM in 0.1× PBS
Abrantes 2025 preprint: NG-Apt-Glu = 3'-trim of a 98-nt "glu1d04" string; 1 aM FET LOD in aCSF
```

**Sequence identity can transfer; Kd cannot.** Hu’s Glu-apt is `GCATCAGTCCACTCGTGAGGTCGACTGATGAGGCTCGAT` (39 nt, 5′-thiol, 3′-Fc). Lam 2022 quotes a 98-nt Wu-attributed string that **begins with those 39 nt** (`review-supported` for the map; Wu VoR not inspected). `transferable=yes` for the nucleotide string; `transferable=no` for Kd.

---

## 4. Transfer ledger

Each row is one hop. “Illegal” = the paper or this repo treats the destination as if it inherited the source number. “Silent” = the hop is not measured and not flagged. “Honest” = the authors split the objects.

### 4.1 Parent → truncated

| Hop | What moved | Status | Tag | Locator | Transferable |
| --- | --- | --- | --- | --- | --- |
| Wu 2022 abstract: 1d04 Kd 12 µM, then glu1 sensor LOD 0.0013 pM / 0.01 pM–1 nM | Kd is **not** restated as glu1’s Kd; LOD is glu1’s. The abstract still narrates one “aptamer sequence… further used” pipeline | **honest split of quantities; silent on truncated Kd** | `primary-source-supported` for the two numbers; `unresolved` for glu1 `Kd_molecular` | PubMed/JuSER abstract | no |
| Hu 2025 methods: truncated Fc-thiol 39-mer labeled “Kd = 12 µM (Wu et al., 2022)” | parent isolate Kd pasted onto truncated, labeled, surface oligo | **illegal citation transfer** | `primary-source-supported` that the citation exists; `unresolved` that 12 µM is the 39-mer’s Kd | Hu Experimental section sequences | no |
| Hu 2023 ST: Nakatsuka parent Kd = 30 nM cited; S1 (44 nt) vs truncated S2 (32 nt) vs S3 (26 nt) compared **only** by SWV signal suppression at 10 nM ST: S2 27.2 ± 4.6%, S1 19.8 ± 3.5%, S3 9.5 ± 5.2% | truncation changes **gain**, not a remeasured Kd | **silent Kd transfer** of 30 nM onto S2 | `primary-source-supported` for SS%; `unresolved` for truncated `Kd_molecular` | PMC10527390 §3.1 Fig. 1A; intro cites Nakatsuka 30 nM | no |
| Hu 2025 ST-apt line: “Truncated serotonin aptamer (ST-apt, Kd = 30 nM) (Hu et al., 2023b; Nakatsuka et al., 2018)” then the S2 sequence | 30 nM parent/solution label on the truncated multiplex oligo | **illegal citation transfer** (same pattern as Glu) | `primary-source-supported` | Hu 2025 sequences | no |
| Ricci 2016: cocaine truncations/circular permutations shift affinity **up to 2800-fold**; point mutations <2-fold; extent **not predictable** | method lesson: truncation can rewrite Kd | **honest; not glutamate** | `primary-source-supported` | PMC5660318 | no |
| Abrantes preprint: trim 40 nt from 3′ of 98-nt “glu1d04” because MFold hairpins “could be involved in the glutamate-binding site(s)” | parent secondary structure treated as transferable to a 58-nt child | **computational property transfer** | `computational illustration` | bioRxiv HTML, in silico design section | no |

Ricci 2016 is the paper that shows truncation *can* move affinity by thousands-fold. It does **not** license writing 12 µM on Hu’s 39-mer, and it does **not** develop Langmuir–Freundlich (Hu cites Ricci 2016 in the LF sentence; that citation does not support the isotherm choice). `supports_claim=no` for “Ricci 2016 = LF.” `primary-source-supported` for 2800-fold cocaine truncation.

### 4.2 Soluble → surface-bound

| Hop | What moved | Status | Tag | Locator | Transferable |
| --- | --- | --- | --- | --- | --- |
| Hu 2025: cited solution Kd vs electrochemical apparent Kd 2.7 nM (ST), 1.8 nM (Glu), 49.6 µM (DA) | authors **contrast** the numbers and invoke “confined 2D space… among others” | **honest that they differ; illegal if 1.8 nM is used as molecular Kd of 1d04 or of the soluble 39-mer** | `primary-source-supported` for the three apparent values; confinement is **author interpretation** | Hu §3.2 | no |
| **Same table, DA: 49.6 µM apparent vs cited 44 µM** | surface EC50 ≈ cited solution Kd | **internal counterexample** to a uniform confinement-tightening law | `primary-source-supported` | Hu §3.2 | no |
| White 2008 cocaine: hyperbolic “Kd” 327 ± 64, 101 ± 8, 127 ± 35 µM at 25 / 60 / 500 nM fabrication; authors say comparable to solution ~100 µM | packing moves apparent Kd; low/mid density can **match** solution | **honest; not glutamate** | `primary-source-supported` | PMC2674396 Fig. 3 caption | no |
| White 2008 SAM thickness: C6 / C3 / C2 apparent Kd 95 ± 15, 86 ± 5, 18 ± 5 µM at equal 1.6 × 10¹² cm⁻² | backfill chemistry moves apparent Kd ~5-fold | **honest; not glutamate** | `primary-source-supported` | PMC2674396 Fig. 7 | no |
| Daniel 2013 thrombin: KD_sol = 3.16 ± 1.16 nM; KD_surf depends on grafting density and **linearly extrapolates toward KD_sol at low σ** | surface ≠ solution except in the dilute-probe limit | **honest; protein target; not glutamate** | `primary-source-supported` | PLOS ONE Fig. 5, Table 2 | no |
| MacDonald 2019 L-Tym: solution Kd cited 1–3 µM; crowded QCM-D KDapp 160 → 13 µM as coverage falls; SPR KD 120 → 20 µM; below ~2.5 pmol cm⁻², KDapp plateaus at 26 ± 8 µM | **small-molecule** crowding; still not back to solution 1–3 µM | **honest; not glutamate** | `primary-source-supported` | HAL PDF Figs. 2, S10 | no |
| Liu 2021: cocaine aptamer ITC KD = 70.4 ± 0.8 µM **in the high-salt PBS used for immobilization**; occupancy ~78% at 250 µM cocaine vs ~96% at 2 mM | they measured affinity **in the immobilization buffer**, then folded-state tethering improved LOD (1 vs 2 µM cocaine) | **honest non-transfer; not glutamate** | `primary-source-supported` | NSF PAR PDF | no |

**What the interface actually does (mechanism, first-year).** A DNA aptamer on gold is a polyanion standing in a packed monolayer, often with a redox tag and a backfill (MCH or PEG). Neighbors can block folding (White, Hu ST density curve, MacDonald). The SAM thickness and electrode field can shift the folded/unfolded equilibrium (White C2 vs C6). A tetrahedron can reorient the same aptamer and change apparent fiber Kd (Xu/Tanner; N-protein). None of those experiments is a glutamate titration of Hu’s 39-mer.

### 4.3 Buffer A → buffer B

| Hop | What moved | Status | Tag | Locator | Transferable |
| --- | --- | --- | --- | --- | --- |
| Xiao 2025: SPR Kd 293 nM (buffer not specified as 0.1× PBS in the SPR sentence) vs FET practical LOD 10 fM and range 10 fM–100 nM **in 0.1× PBS**; static FET incubation 1 h in 0.1× PBS | ionic strength / Debye architecture | **honest split of SPR vs FET; illegal if 10 fM is used as 1× aCSF or as Kd** | `primary-source-supported` | PMC XML §2.3, Fig. 3, Methods | no |
| Nakatsuka 2018: new DA aptamer FET works 10⁻¹⁴–10⁻⁹ M in **undiluted 1× PBS and 1× aCSF**; prior DA aptamer (Kd 1 µM) required **0.1× PBS** and was >1000-fold weaker in that comparison | Debye length is why people dilute PBS | **honest; not glutamate** | `primary-source-supported` | eScholarship PDF Fig. 2A | no |
| Hu 2025: PBS calibration; aCSF recoveries 101.1–111.0%; 50% serum LOD Glu 51.5 pM vs PBS 32 pM | matrix hop **measured** as recovery/LOD, not as Kd | **honest LOD hop; silent on apparent Kd in serum/aCSF** | `primary-source-supported` | Hu §3.4; Fig. 6 | no |
| Hu thesis: Ames linear window 10 nM–10 µM with poor SNR vs PBS 1 nM–1 mM / LOD 0.3 pM | same oligo family, different buffer, different analytical window | **primary demonstration that buffer rewrites the sensor after selection** | `primary-source-supported` (S066 ledger) | thesis Fig. 6.7 vs 6.9A | no |
| Liu 2021: cocaine weak in high-salt immobilization PBS (ITC 70.4 ± 0.8 µM) | immobilization-buffer Kd ≠ sensing-buffer Kd | **honest; not glutamate** | `primary-source-supported` | NSF PAR | no |

Nakatsuka is the reason Xiao’s 0.1× PBS LOD cannot be walked into cerebrospinal fluid. `hypothesis` if someone claims Xiao would work in 1× aCSF; `unresolved` experimentally for that glutamate FET.

### 4.4 Architecture A → architecture B

| Hop | What moved | Status | Tag | Locator | Transferable |
| --- | --- | --- | --- | --- | --- |
| Wu glu1 gold E-AB LOD 0.0013 pM vs Hu AuED-MEA LOD 32 pM vs Hu thesis PaC probe LOD 0.3 pM | three LODs, three formats, same aptamer family | **illegal if averaged into “the” glutamate LOD** | `primary-source-supported` for each number in its paper | Wu abstract; Hu Fig. 4h; S066 Fig. 6.7 | no |
| Hu journal 15 min Glu wait vs thesis 10 min plateau at 10 nM vs retina 14 s scan / 1 min sampling | clocks are protocol, not koff | **illegal if identified with 1.2 ms cleft τ** | `primary-source-supported` | Hu §3.2 Fig. S8; S066 Fig. 6.6, §6.3 | no |
| Xiao SPR Kd vs FET LOD; multiplex response “stabilized after 200 s” after 10 nM target (Fig. 5e) | SPR occupancy vs FET charge gating | **honest numbers; illegal if 10 fM = 293 nM** | `primary-source-supported` | Xiao Fig. 5e paragraph | no |
| Xu/Tanner: Apt48 fiber apparent Kd 0.3981 µM vs DNT-Apt48 0.1996 µM; signal 2–2.5 fold; plateau ~25 min; LOD 46 nM vs 34 nM | **display architecture** changes apparent Kd of the **same** aptamer | **honest interface evidence; not glutamate** | `primary-source-supported` | PMC13112887 Fig. 4D–E | no |
| Hu 2025 intro: “each aptamer requires a unique packing density”; then PA time/density optimized on **ST** (Fig. 3c, 10 nM ST, 5 min) and reused for Glu and DA | packing optimum transferred as a **fabrication method** | **silent method transfer** | `primary-source-supported` | Hu intro; §3.1; “Similarly, E-AB sensors for… Glu and DA were fabricated using the PA deposition method” | no |
| Hu thesis: authors say immobilization must be re-optimized per AuED/pzc layout; probe coverage 0.80 ± 0.26 × 10¹³ cm⁻² vs journal 1.43 ± 0.37 × 10¹³ | chip → probe is a new interface | **illegal if journal 1.8 nM / 32 pM are inherited by the retina probe** | `primary-source-supported` (S066 extract) | orchestrator H1 | no |
| Abrantes graphene FET 1 aM in aCSF vs Wu E-AB 0.0013 pM vs Hu 32 pM | LOD rank is architecture, not aptamer quality | **illegal if used as affinity** | `primary-source-supported` as preprint abstract/HTML | bioRxiv | no |
| Park 2023 “Glutamate FET” = *P. falciparum* GDH | wrong molecule | **illegal harvest** | `primary-source-supported` as refutation (C019) | PMC10136356 Table 1 | no |

**Hu packing numbers (ST-optimized, then reused).** PA: 1.43 ± 0.37 × 10¹³ molecules cm⁻² in 5 min vs drop-cast 1.22 ± 0.44 × 10¹³ overnight. Not statistically different in density; PA claimed higher gain via orientation. `primary-source-supported`. Hu 2023 S2 optimum was 1.05 × 10¹² cm⁻² — an order of magnitude lower, on a different electrode (macro AuE, drop-cast, PEG 4 h). Reusing 2025 PA density for Glu is not licensed by the 2023 ST chronocoulometry.

### 4.5 Repo-internal transfers

| Location | What happened | Status |
| --- | --- | --- |
| `occupancy.svg` / occupancy table | 1:1 Langmuir θ overlay on Hu **Langmuir–Freundlich** 1.8 nM and on 1d04 12 µM | captioned SIMULATION; still an **illegal occupancy reading** if treated as measured tissue occupancy. Ledger already flags this (C027 vs C005). |
| Hu methods 12 µM typed as `Kd_molecular` in C021 | correctly tagged as a **citation**, not a Hu measurement | honest ledger row |
| C008/C010 kon used in `sensitivity.svg` | not glutamate; labeled NOT Glu / BOUND | honest **if** the caption stays larger than the number |
| Citing Xu/Tanner as glutamate immobilization | N-protein optical fiber | **illegal**; Tanner objection 5 |

This repo’s constitution already forbids the hops. The remaining risk is **oral**: a first-year pointing at 1.8 nM as “the aptamer’s Kd after immobilization.”

---

## 5. Hu 2025 as the load-bearing immobilization paper

**What was measured.** Potential-pulse-assisted (PA) co-immobilization of three thiolated, redox-tagged aptamers on Au-electrodeposited MEAs; thiol-PEG backfill; ACV.

**Sequence labels (citation Kd, not remeasured here):**

- ST-apt truncated, “Kd = 30 nM” (Nakatsuka 2018 / Hu 2023)
- Glu-apt truncated 39-mer, “Kd = 12 µM” (Wu 2022)
- DA-apt, “Kd = 44 µM” (Liu 2021)

**Surface Langmuir–Freundlich apparent Kd:** ST 2.7 nM; Glu 1.8 nM; DA 49.6 µM. `primary-source-supported`. Authors: differences vs solution-phase “can be attributed among others to… confined 2D space.” That sentence is interpretation.

**Scale factors (cited → apparent), for display only, not as a mechanism:**

| Channel | Cited label | Apparent EC50 | Ratio (cited/apparent) |
| --- | --- | --- | --- |
| ST | 30 nM | 2.7 nM | ~11 |
| Glu | 12 µM | 1.8 nM | ~6700 |
| DA | 44 µM | 49.6 µM | ~0.9 |

A BIOC1600 assessor who hears “immobilization tightened glutamate 6700-fold by 2D confinement” should be shown the dopamine row. Same chip family, same PA method, same LF fit. DA did not tighten. `hypothesis` that the Glu jump is mostly **wrong parent construct + wrong quantity** (1d04 Kd vs truncated-surface EC50), not a universal interface physics law.

**Clocks.** Glu ACV after 15 min; DA after 10 min; ST 15 min chosen as signal/time compromise (Fig. 3f is ST). `measurement_time`, not koff. `primary-source-supported`.

**LOD vs apparent Kd vs calibration span.** Glu LOD 32 pM PBS / 51.5 pM 50% serum; semi-log 0.1 nM–10 µM. LOD is not occupancy. The 10 µM top of the Glu calibration is not 1.1 mM cleft glutamate.

---

## 6. Inference boundary

**Measured**

- Wu abstract: 1d04 Kd 12 µM; glu1 LOD 0.0013 pM; glu1 range 0.01 pM–1 nM; MCH backfill; 10-fold diluted serum selectivity.
- Hu 2025: packing optimized on ST; PA vs drop-cast densities; LF apparent Kd ST/Glu/DA; Glu 15 min; LODs; aCSF recoveries 101.1–111.0%; serum LODs.
- Hu 2023: truncation changes ST **signal suppression** at 10 nM; S2 density 1.05 × 10¹² cm⁻²; 40 min to SS plateau; LOD 0.14 nM; Nakatsuka 30 nM is cited, not remeasured on S2.
- Xiao: SPR Kd Glu 293 nM; FET LOD 10 fM in 0.1× PBS; 1 h static incubation; ~200 s multiplex stabilize; pH-reset architecture.
- White, Daniel, MacDonald, Liu, Xu/Tanner, Nakatsuka: interface rewrites gain, apparent Kd, and/or Debye response **on non-glutamate (or non-Glu-aptamer) systems**.
- MacDonald HAL: small-molecule crowded-surface KDapp can be ~100 µM vs solution 1–3 µM.

**Inferred (not licensed)**

- 12 µM is the Kd of glu1 or of Hu’s 39-mer.
- 1.8 nM is molecular Kd, or a 1:1 occupancy Kd in tissue, or the result of truncation, or the result of 2D confinement.
- Wu 0.0013 pM, Hu 32 pM, thesis 0.3 pM, Xiao 10 fM, Abrantes 1 aM are comparable affinity numbers.
- Tanner tetrahedron numbers apply to glutamate.
- Docking scores 33.86 / 30.15 (Abrantes site B / A) are affinities.

**Unknown**

- Solution `Kd_molecular` of the Fc-thiol 39-mer in Hu’s ACV PBS.
- Langmuir–Freundlich heterogeneity exponent *n* for the Glu channel (not extracted from inspected main text).
- Packing-density series for Glu-apt (only ST series in Fig. 3c).
- Glutamate kon/koff on any construct (C007).
- Wu VoR truncation table.
- Abrantes ELONA Kd (assay used 0, 10, 30, 50 mM glutamate; **fitted Kd not entered** this session).

---

## 7. Falsifier

The confinement-as-cause story dies if a paired solution vs surface isotherm of the **same** Hu 39-mer in **one** buffer either:

- agrees near 1.8 nM (then 1.8 nM is molecular, and the 12 µM label was the wrong parent), or
- agrees near 12 µM (then 1.8 nM is transduction/heterogeneous-surface EC50, not tighter recognition).

Hygiene (construct non-identity) dies only if those objects are shown to be the same measurement.

Oral kill: treating 12 µM → 1.8 nM as a measured truncation or confinement result, or plotting Tanner tetrahedron as a glutamate interface.

---

## 8. Is immobilization the bottleneck versus molecular affinity?

**Both, and they are not interchangeable.**

Molecular affinity of the SELEX isolate is already a tonic-occupancy problem independent of gold. If 12 µM were a 1:1 Kd, θ(25 nM) ≈ 25 nM / (25 nM + 12 µM) < 0.01 (`computational illustration` of Langmuir occupancy; Clements/Herman biology is separate). Tightening the advertised number into the nM range would saturate basal glutamate instead. That is an occupancy story, not an electrode story.

Immobilization is the bottleneck for **everything the poster can actually hold in a hand**: orientation, packing, backfill, Debye/ionic strength, matrix (Ames vs PBS), chip vs flexible probe, and the clock you choose to scan. White, MacDonald, Daniel, Liu, Nakatsuka, and Xu/Tanner show the interface rewrites gain and apparent Kd when those experiments are done. For glutamate they were **not** done as a paired solution/surface series on the 39-mer.

So: immobilization is the **operational** bottleneck of the sensor; unmeasured truncated-oligo Kd is the **biochemical** hole; silent citation of 12 µM is the **scholarship** failure. Ranking one as “the” bottleneck overclaims. The glutamate number scatter is not evidence that the electrode made a better receptor.

---

## 9. Flagship figure / analysis (not docking)

**One figure: “Illegal hops” construct×quantity matrix.**

Rows = constructs (1d04; glu1 E-AB; Hu 39-mer methods label; Hu 39-mer ACV on AuED-MEA; Hu 39-mer on PaC probe PBS; same probe Ames; Xiao SPR; Xiao FET 0.1× PBS; Abrantes NG-Apt-Glu preprint). Columns = `Kd_molecular`, cited Kd, `EC50`, `sensor_LOD`, `measurement_time`, packing density. Empty cells stay empty. Arrows that currently exist in papers are drawn in three colors: measured / citation / not allowed.

Inset (same poster panel, smaller): Hu’s three-channel **cited vs apparent** bars (ST ~11×, Glu ~6700×, DA ~1×) with caption “same PA method; dopamine did not tighten.” First-year explainable without a review.

Do **not** make occupancy overlay the flagship of *this* lane (it is already the occupancy-kinetics analysis). Do **not** dock glutamate into a predicted 39-mer. Do **not** reuse Xu/Tanner N-protein structures as a glutamate cartoon.

Optional supporting strip (clearly NOT glutamate): White cocaine apparent Kd vs density; MacDonald L-Tym KDapp vs coverage. Caption: “the interface can move Kd; these are not glutamate numbers.”

---

## 10. Highest-information experiment on the interface

**Paired solution and surface isotherm of Hu’s exact Fc-thiol 39-mer in the PBS of the ACV assay, at ≥3 packing densities, with the Langmuir–Freundlich *n* reported.**

Protocol, in one buffer:

1. ITC or fluorescence/SPR competition `Kd_molecular` of the unlabeled 39-mer **and** of the Fc-thiol 39-mer (label can change switching).
2. ACV (or SWV) isotherms on AuED at low / Hu-like (~10¹³ cm⁻²) / deliberately crowded density; fit Langmuir **and** Langmuir–Freundlich; publish *n*.
3. If the surface construct equilibrates on a useful clock, IPA or flow-SPR kon/koff on **that** oligo (Abeykoon shows the method on tobramycin; `transferable=no` for the rates, `yes` for the method).

Pass: 12 µM vs 1.8 nM is resolved into parent-construct error vs interface rewrite vs isotherm-model error. Fail: we keep citing Wu on a different molecule.

Cheaper but weaker: open Wu VoR for the truncation table. That still would not be a surface Kd of Hu’s oligo.

Not this experiment: docking the 39-mer; transferring White cocaine density curves numerically; treating Xiao 0.1× PBS as aCSF.

---

## 11. Sources inspected this session (identifiers)

| ID in repo | Paper | Route | Inspected |
| --- | --- | --- | --- |
| S001 | Wu et al. 2022 *Anal. Bioanal. Chem.* PMID 34783880 DOI 10.1007/s00216-021-03783-w | abstract | no VoR |
| S002 | Hu et al. 2025 *Biosens. Bioelectron.* 117992 PMID 40992279 | RWTH OA PDF | yes |
| S011 | Lam et al. 2022 *Biosensors* PMC9776347 | PMC | yes |
| S017 | Nakatsuka et al. 2018 *Science* PMC6663484 / eScholarship | OA PDF | yes |
| S021 | Xiao et al. 2025 *Adv. Sci.* PMC12376627 | PMC XML | yes |
| S022 | Hu et al. 2023 *Biosensors* PMC10527390 | PMC | yes |
| S006 | Xu/Tanner et al. 2026 *J. Nanobiotechnol.* PMC13112887 | PMC XML | yes |
| S033 | White et al. 2008 *Langmuir* PMC2674396 | PMC | yes |
| S034 | Daniel et al. 2013 *PLOS ONE* PMC3775802 | OA HTML | yes |
| S037 | Liu et al. 2021 *ACS AMI* PMID 33448791 | NSF PAR PDF | yes |
| S038 | MacDonald et al. 2019 *J. Phys. Chem. C* DOI 10.1021/acs.jpcc.9b00845 | HAL PDF | yes (this session; previously ACS 403) |
| S010 | Abrantes et al. 2025 bioRxiv 10.1101/2025.11.05.686731 | HTML | partial |
| Ricci 2016 | *Acc. Chem. Res.* 49:1884 PMC5660318 DOI 10.1021/acs.accounts.6b00276 | PMC | yes (Hu’s LF citation target) |

---

## 12. Lane close

Immobilization is a real, first-year-explainable rewrite of nucleic-acid recognition (packing, SAM, crowding, Debye, display). Glutamate papers still mostly **cite** parent Kd onto truncated surface oligos and then report a different object (LOD or LF EC50). Until the 39-mer is titrated in solution and on the electrode in one buffer, the electrode is a suspect, not a convict. Docking is not that experiment.
