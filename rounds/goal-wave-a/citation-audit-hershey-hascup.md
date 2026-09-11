# Citation audit: Hershey 2025 and Hascup 2008/2010

Auditor role: independently re-fetch identifiers; check claim–paper fit. Do not trust scouts, extractors, or the opposing-case lane. Date: 2026-09-11.

Routes used: PubMed E-utilities (`esummary`, `esearch`, `efetch`, `elink`), Crossref REST, Unpaywall, PMC HTML, PMC OAI JATS (`metadataPrefix=pmc`), Europe PMC search JSON. No Sci-Hub. No paid APIs. No PDFs committed.

`full_text_inspected` rule: a load-bearing numerical claim is confirmed only when the number was read in article body or figure/table caption, not from another agent’s note. Publisher version-of-record PDFs (ACS, Wiley, ASPET) were **not** fetched. PMC deposits inspected here are NIHMS/author-manuscript HTML or JATS (`nihpa` collection). Scientific numbers below are from those PMC texts.

Identifier rule: `identifier_ok=yes` only if DOI and/or PMID resolve to the stated title/authors/year/journal.

---

## Source identifiers (re-fetched)

### SRC-HERSHEY-2025

| Field | Claimed | Re-fetched |
| --- | --- | --- |
| Authors | Hershey, Popov, Oliver, Dugan & Kennedy | Neil D. Hershey; Pavlo Popov; Nicholas M. Oliver; Colleen E. Dugan; Robert T. Kennedy |
| Title | (implied ACS Chem Neurosci 2025 glutamate/microdialysis) | Detection of Neuronal Glutamate in Brain Extracellular Space In Vivo Using Microdialysis and Metabolic Labeling with Glutamine |
| Journal | ACS Chem Neurosci | PubMed: `ACS Chem Neurosci`. Crossref container: `ACS Chemical Neuroscience` |
| Year | 2025 | Print 2025-09-03; online 2025-08-21 |
| Volume/issue/pages | not claimed | 16(17):3398–3409 |
| PMID | 40838767 | 40838767 |
| PMCID | PMC12418293 | PMC12418293 (elink; PubMed articleids) |
| DOI | not claimed | 10.1021/acschemneuro.5c00518 |
| Manuscript | — | NIHMS2108906 |

`identifier_ok`: **yes**. doi.org returns HTTP 302 for the DOI (resolver hit). PubMed, Crossref, and PMC JATS agree on title, authors, PMID, PMCID, and DOI. Print vs online dates differ by 13 days; year 2025 is correct.

`full_text_inspected`: **yes** (PMC HTML + OAI JATS NIHMS2108906). ACS VoR PDF not inspected.

Construct in the paper (not transferable to aptamer electrodes): male Sprague–Dawley rats; probe in cortex (AP +0.2 mm, ML ±2.3 mm, 3 mm from skull; authors later call the tail-pinch site **motor cortex**); homemade 250 µm o.d. cellulose probes or CMA12 Elite 0.5 mm o.d. / 2 mm membrane; 1 µL/min aCSF; 2.5 µM ¹³C₅-Gln retrodialysis; LC measurement of dialysate ¹³C₅-Glu vs endogenous ¹²C-Glu. Implant under ketamine/dexmedetomidine; “the day of the experiment” animals were briefly isoflurane-anesthetized then tethered to a Raturn (awake sampling). Two-minute fractions unless stated.

Quantity types in this paper are **not** Kd, LOD, kon, or sensor response time. They are: dialysate concentrations, extraction-fraction-corrected apparent extracellular concentrations (`Capp`), and percent of a normalized labeled or endogenous signal.

### SRC-HASCUP-2010

| Field | Claimed | Re-fetched |
| --- | --- | --- |
| Authors | Hascup et al. 2010 | Erin R. Hascup; Kevin N. Hascup; Michelle Stephens; Francois Pomerleau; Peter Huettl; Alain Gratton; Greg A. Gerhardt |
| Title | (not given) | Rapid microelectrode measurements and the origin and regulation of extracellular glutamate in rat prefrontal cortex |
| Journal | (not given) | *Journal of Neurochemistry* (`J Neurochem`) |
| Year | 2010 | Print 2010 Dec; epub 2010-11-19 |
| Volume/issue/pages | not claimed | 115(6):1608–1620 |
| PMID | 20969570 | 20969570 |
| PMCID | not claimed | PMC2996468 |
| DOI | not claimed | 10.1111/j.1471-4159.2010.07066.x |
| Manuscript | — | NIHMS247588 |

`identifier_ok`: **yes**. PMID 20969570 is this paper, not the 2008 mouse paper.

`full_text_inspected`: **yes** (PMC HTML + OAI JATS NIHMS247588). Wiley VoR PDF not inspected.

Construct: ceramic GluOx / Nafion microelectrode array (MEA), two GluOx sites plus sentinel self-reference, constant-potential amperometry (+0.7 V), FAST16, 1 Hz save; **awake Long Evans rats**; MEA in **right PFC** (AP +3.2 mm). Resting glutamate is the self-referenced GluOx–sentinel difference, calibrated in 37 °C PBS. Not microdialysis. Not an aptamer.

### SRC-HASCUP-2008

PubMed search `Hascup[Author] AND 2008[pdat] AND glutamate` returns **one** journal article.

| Field | Claimed | Re-fetched |
| --- | --- | --- |
| Citation | Hascup et al. 2008 (PMID unknown) | Kevin N. Hascup; Erin R. Hascup; Francois Pomerleau; Peter Huettl; Greg A. Gerhardt |
| Title | — | Second-by-second measures of L-glutamate in the prefrontal cortex and striatum of freely moving mice |
| Journal | — | *The Journal of Pharmacology and Experimental Therapeutics* (`J Pharmacol Exp Ther`) |
| Year | 2008 | Print 2008 Feb; epub 2007-11-16 |
| Volume/issue/pages | — | 324(2):725–731 |
| PMID | find it | **18024788** |
| PMCID | — | PMC3404456 |
| DOI | — | 10.1124/jpet.107.131698 |
| Manuscript | — | NIHMS390173 |

`identifier_ok`: **yes** for PMID 18024788 as the 2008 Hascup glutamate MEA paper. Do not use 20969570 for this claim.

`full_text_inspected`: **yes** (PMC HTML). PMC OAI JATS for PMC3404456 returned `cannotDisseminateFormat`. ASPET VoR PDF not inspected. Europe PMC HTML/PDF timed out in this session; the PMC.gov HTML was sufficient.

Construct: ceramic GluOx/Nafion MEA chronically implanted in **freely moving C57BL/6 mice**, PFC or striatum. TTX experiment is **striatum only**. Tip dimensions given as 333 × 200 × 125 µm. This is an enzyme MEA, not a carbon-fiber “small enzyme electrode” of the Kulagina 1999 type.

---

## Audited claims

### A-HERSHEY-INFUSION

**Claim:** ¹³C₅-glutamine infusion via rat cortical microdialysis.

- `identifier_ok`: **yes**
- `supports_claim`: **yes**
- Locator: Methods §2.5; Results §3.2 / **Figure 1**. Abstract: infusing 2.5 µM ¹³C₅-Gln through a microdialysis probe in rat cortex collected 144 ± 35 nM (n = 11) ¹³C₅-Glu in **dialysate**.
- Quantity type: retrodialysis metabolic labeling; dialysate ¹³C₅-Glu. Not Kd, LOD, or a neuronal concentration after Ed correction.
- Construct match: yes (rat cortex microdialysis, 2.5 µM ¹³C₅-Gln).
- Metadata discrepancies: none for this clause. Abstract writes “500 mM riluzole”; methods use **500 µM** riluzole. That typo is not part of the audited claim.
- Required correction: **none** for the infusion clause. If downstream text treats 144 ± 35 nM as Ed-corrected ECF neuronal glutamate, that is a quantity-type swap (`no`). It is uncorrected dialysate ¹³C₅-Glu (Figure 1B).

### A-HERSHEY-TAILPINCH

**Claim:** Tail pinch raised neuronally-derived glutamate 155 ± 14% and TTX abolished that increase while total endogenous extracellular glutamate did not move.

- `identifier_ok`: **yes**
- `supports_claim`: **partial**
- Locators:
  - Results §3.6 body: tail pinch increased ¹³C₅-Glu following ¹³C₅-Gln infusion by **155 ± 14%** (p ≤ 0.05 for all data; 4 time points p ≤ 0.05; **n = 4**). “This increase was abolished by TTX infusion (p ≤ 0.05, **n = 3**; **Figure 7**).” Endogenous ¹²C-Glu and ¹²C-Gln: “had no effect” / Figure 7C–D “no overall change.”
  - **Figure 7** caption: “Tail pinch (gray solid bar, n = 4) evoked a 155 ± 14% increase (p < 0.05) in dialysate concentration of ¹³C₅-Glu … This increase was blocked in the presence of TTX (open circles, n = 3). … no overall change in … [¹²C-Glu]out.”
- What was measured: percent of **pre-pinch ¹³C₅-Glu** (caption: normalized to the average of each analyte prior to tail pinch). Endogenous ¹²C-Glu in the **same** tail-pinch sessions.
- What was inferred: that ¹³C₅-Glu is “neuronally derived.” Authors argue this from TTX/mGluR/Gln-transport pharmacology (§3.4, §4). Basal TTX suppression of ¹³C₅-Glu is **62 ± 7%**, not 100% (**Figure 3**, n = 3). Authors state a caveat that ¹³C₅-Glu could come from a source only *dependent on* neuronal activity. Infusing **50 µM** ¹³C₅-Gln (not 2.5 µM) yields ¹³C₅-Glu that is **not** TTX-sensitive (Figure SI 4C).
- Quantity-type check: 155 ± 14% is **not** a change in total extracellular glutamate, **not** Kd, **not** LOD. It is a normalized labeled-dialysate signal. Do not add it to, or replace, the 9.4 µM Capp.
- Construct match: motor cortex (authors contrast this with prior mPFC work), not a generic “brain.” Sprague–Dawley, microdialysis, 2-min fractions.
- Metadata discrepancies: none on identifiers. “155 ± 14% increase” is the paper’s own wording; y-axis is percent of pre-pinch, so 155% of basal (1.55×), not necessarily “increased by 155 percentage points above 100%” in the additive English sense. Copy the paper’s phrase and the normalization, do not rewrite as 2.55-fold unless the VoR figure axis is inspected.
- Required correction: Restate as **dialysate ¹³C₅-Glu (2.5 µM ¹³C₅-Gln labeling), Figure 7, 155 ± 14% of pre-pinch, n = 4; TTX block n = 3; endogenous ¹²C-Glu no overall change (Figure 7C)**. Do not write “neuronally-derived glutamate” as if cell type were measured. Do not attach n = 11 from the Ed section. Do not transfer to an aptamer electrode or to mPFC.

### A-HERSHEY-KPLUS

**Claim:** 75 mM K⁺ raised total glutamate ~160% with no neuronal component.

- `identifier_ok`: **yes**
- `supports_claim`: **partial**
- Locators: Results §3.6; **Figure 6**. “Addition of 75 mM K⁺ to the dialysis perfusion fluid (**n = 4**) while ¹³C₅-Gln was also infused increased only ¹²C-Glu (**160 ± 20%**, p < 0.05) with **no increase in ¹³C₅-Glu** relative to physiological K⁺.” GABA +2270 ± 400%; ¹²C-Gln fell to 48 ± 0.6% of basal. Figure 6A caption: high K⁺ “had no effect on the dialysate concentration of ¹³C₅-Glu.”
- Discussion §4.3 uses the phrase “lack of a ¹³C₅-Glu or **neuronal component**.” That is author interpretation of the labeled pool, not a separate neuronal assay.
- Quantity-type check: 160 ± 20% is percent of the ¹²C-Glu signal during the same ¹³C₅-Gln infusion (normalized to aCSF + ¹³C₅-Gln steady state). It is **not** Ed-corrected ECF glutamate and **not** a 160% increase of the 9.4 µM Capp.
- Construct match: same microdialysis / motor-cortex preparation. K⁺ and TTX/tail-pinch are **separate** sessions (K⁺ n = 4; tail pinch n = 4). Do not claim the two stimuli were in the same animals unless the paper says so (it does not).
- Metadata discrepancies: “~160%” rounds **160 ± 20%**. Keep the SEM.
- Required correction: **75 mM K⁺ aCSF, Figure 6, ¹²C-Glu 160 ± 20% (n = 4); ¹³C₅-Glu no increase.** Replace “neuronal component” with “¹³C₅-Glu (putative neuronal-enriched labeled pool).” Same 2.5 µM ¹³C₅-Gln constraint as above.

### A-HERSHEY-CAPP

**Claim:** Extraction-fraction-corrected rat cortical glutamate 9.4 ± 0.6 µM and glutamine 179 ± 20 µM.

- `identifier_ok`: **yes**
- `supports_claim`: **yes**
- Locator: Results **§3.1** body text. **No figure and no table** carry these two numbers. Method: retrodialysis loss of a stable-isotope-labeled analyte to compute extraction fraction \(E_d\), then \(C_\mathrm{app} = C_\mathrm{out}^\mathrm{endogenous} / E_d^\mathrm{SIL}\). Errors are **SEM** (Methods §2.6). n = 11.
  - 2.5 µM ¹³C₅-Gln in → 1.73 ± 0.06 µM out → \(E_d\) 0.30 ± 0.03 → **Gln 179 ± 20 µM**.
  - 5.0 µM ¹³C₅-Glu in → 3.5 ± 0.05 µM out → \(E_d\) 0.29 ± 0.01 → **Glu 9.4 ± 0.6 µM**.
- Quantity type: `biological_concentration_range` as **apparent extracellular concentration from microdialysis Ed correction**. Not molecular Kd. Not sensor LOD. Not the ¹³C₅-Glu neuronal-enriched pool (that recovered concentration is 144 ± 35 nM in dialysate, Figure 1B). Not Hascup MEA resting glutamate.
- Construct match: rat cortex, this probe/flow/Ed method. §3.2 then uses **different probes with higher \(E_d\)** for the conversion time course (outlet ¹³C₅-Gln 1.25 ± 0.1 µM). Do not mix those recoveries into the 9.4 / 179 calculation.
- Transferable: **no** to surface aptamer sensors, enzyme MEAs, other brain regions, or other buffers.
- Metadata discrepancies: none.
- Required correction: **none** on the numbers. Cite **§3.1 (not a figure)**. Label as `Capp` / Ed-corrected microdialysis, n = 11, SEM, Sprague–Dawley cortex.

---

### A-HASCUP2010-RESTING-TTX

**Claim:** Awake-rat GlutOx MEA resting glutamate 34.7 ± 11.8 µM (n = 41), ~40% TTX-sensitive.

- `identifier_ok`: **yes** (PMID 20969570)
- `supports_claim`: **yes** (both quantities are in this paper; they are **not** the same experiment)
- Locators:
  - Resting value: Results **§3.1**, parenthetical, not Table I: “for rats used in this study, **34.7 μM ± 11.8 μM (n=41)**.” Table I only gives PFC MEA as a **range 9–45.5 µM** (Rutherford 2007 + current study).
  - TTX: Results **§3.2**; **Figure 2**. Local TTX (3 µL, 100 µM) decreased PFC resting glutamate by **~40% (−40.8 ± 10.8%, n=7)** vs citrate (1.6 ± 4.1%, n=5), p<0.01. Abstract: “Local application of tetrodotoxin (TTX …) produced a significant (~40%) decline in resting glutamate levels.” Decrease is described as **transient**, peaking after **~1 minute** (Figure 2a).
- Quantity type: enzyme-MEA **resting / tonic extracellular glutamate** (self-referenced amperometry) and **percent decrease after local TTX**. Not Kd, LOD, kon, or microdialysis Capp. Not Hershey 9.4 µM.
- Construct match: **yes** for awake-rat GlutOx MEA, with required region/strain: Long Evans, **PFC**, not motor cortex, not mouse, not dialysis.
- n mismatch: 34.7 µM uses **n = 41** (pooled rats in the study). TTX uses **n = 7**. Do not write “34.7 ± 11.8 µM, ~40% TTX-sensitive, n = 41.”
- Error-bar honesty: Figure 8 (tail pinch) explicitly says shade is SEM. The 34.7 ± 11.8 parenthetical does **not** state SEM vs SD. Methods give group sizes of 4–7 for pharmacology. Do not invent SEM/SD for 34.7.
- Metadata discrepancies: none on identifiers.
- Required correction: Split the claim. **§3.1: 34.7 ± 11.8 µM, n = 41, Long Evans PFC, GluOx MEA resting (self-reference).** **Figure 2 / §3.2: −40.8 ± 10.8%, n = 7, transient ~1 min peak after 100 µM TTX microinjection.** Keep `~40%` only as the authors’ rounding of −40.8 ± 10.8%. Do not transfer to Hershey dialysis or to Hascup 2008 mice.

---

### A-HASCUP2008-TTX20

**Claim:** Small enzyme electrode sees a ~20% TTX-sensitive tonic component. (Find the correct PMID.)

- `identifier_ok`: **yes** for PMID **18024788** as the 2008 paper. **no** if anyone attached this sentence to PMID 20969570.
- `supports_claim`: **partial**
- Locators (PMC HTML of PMC3404456):
  - Abstract: resting (tonic) Glu 3.3 µM PFC and 5.0 µM Str; “TTX significantly (p < 0.05) decreased resting Glu by **20%**.”
  - **Table 1**: PFC (n = 8) average **3.3 ± 1.0 µM**; Str (n = 10) average **5.0 ± 1.2 µM** (S.E.M.; all data are S.E.M.).
  - Results “Decrease in Resting Glu Levels after Local Application of TTX”; **Figure 5**: 1 µM TTX, 1.0 µL, **striatum**, day 4 post-implant. Change **−1.0 ± 0.2 µM, n = 6** vs citrate **−0.3 ± 0.1 µM, n = 6**. “This was approximately a **20%** decrease in resting Glu in the Str compared with our study in **Table 1**.” Discussion repeats: ~20% vs Table 1 Str average.
- What was measured: micromolar drop in MEA resting glutamate after local TTX in **mouse striatum**, then ratioed to the study-wide Str mean (5.0 µM), not a per-animal percent and not vehicle-subtracted (−1.0 vs −0.3 would be a smaller net).
- Quantity type: tonic MEA glutamate and TTX percent of that tonic level. Not response time (paper also reports 500–800 ms electrode response elsewhere; that is a different quantity). Not Kd.
- Construct mismatches vs a careless “small enzyme electrode / rat / tonic” slogan:
  - Species: **mouse**, not rat. (Discussion cites Rutherford for a similar ~20% in freely moving **rats**; that is a different paper.)
  - Region for the 20%: **striatum**, not PFC. Abstract does not say Str.
  - Device: ceramic **GluOx MEA** (four Pt sites, Nafion, self-reference), not a carbon-fiber enzyme electrode.
  - TTX: 1 µM, 1.0 µL local, not bath; not 100% block. Authors note incomplete attenuation vs anesthetized-rat microelectrode studies.
- Metadata discrepancies: print year 2008 vs epub 2007-11-16. Citing 2008 is correct for the VoR.
- Opposing-case lane flag (adversarial, not a ledger edit): that lane listed this paper as `full_text_inspected: no` (abstract only) while scoring the 20% TTX result as `primary-source-supported`. The **abstract does contain 20%**, so the number is not invented; the region, n, µM drop, and device details were not inspectable from the abstract. This audit inspected PMC HTML.
- Required correction: PMID **18024788**. Restate: **awake C57BL/6 mouse striatum, GluOx ceramic MEA, Figure 5 / Table 1, TTX −1.0 ± 0.2 µM (n = 6) ≈ 20% of Str resting 5.0 ± 1.2 µM.** Do not use this 20% for Hascup 2010 rat PFC (~40%). Do not call the device a carbon-fiber microelectrode.

---

## Quantity-type and construct traps (do not silently swap)

| Do not treat as the same number | Distinct quantities |
| --- | --- |
| Hershey 9.4 ± 0.6 µM | Ed-corrected **total** apparent ECF Glu (`Capp`), dialysis, SD rat cortex, §3.1 |
| Hershey 144 ± 35 nM | **Uncorrected dialysate** ¹³C₅-Glu, Figure 1B |
| Hershey 155 ± 14% | Normalized **labeled** ¹³C₅-Glu after tail pinch, Figure 7 |
| Hershey 160 ± 20% | Normalized **endogenous ¹²C-Glu** after 75 mM K⁺, Figure 6 |
| Hascup 2010 34.7 ± 11.8 µM | GluOx MEA resting, Long Evans **PFC**, n = 41, §3.1 |
| Hascup 2010 −40.8 ± 10.8% | Local TTX, same MEA/PFC, **n = 7**, Figure 2, transient |
| Hascup 2008 3.3 / 5.0 µM | Mouse PFC / Str MEA tonic, Table 1 |
| Hascup 2008 ~20% | Mouse **Str** TTX, Figure 5, n = 6 |
| Herman ~25 nM (not audited here) | Different method/preparation; do not “reconcile” by averaging with 9.4 or 34.7 |

No Kd/LOD/kon/response-time swap was present **in the audited wording**; the failure mode is **identity of the glutamate pool** (labeled vs endogenous; MEA vs dialysis; rat vs mouse; PFC vs Str vs motor cortex).

---

## `full_text_inspected` honesty

| Source | Honest flag | What was actually read |
| --- | --- | --- |
| Hershey 2025 | **yes** (PMC NIHMS HTML/JATS) | Not ACS VoR PDF |
| Hascup 2010 | **yes** (PMC NIHMS HTML/JATS) | Not Wiley VoR PDF |
| Hascup 2008 | **yes** (PMC HTML) | Not ASPET VoR PDF; OAI JATS unavailable |

A later agent that cites only PubMed abstracts must not mark these numerical claims `full_text_inspected=yes`. The 2008 20% **is** in the abstract; the 2010 34.7 ± 11.8 (n=41) is **not** in the PubMed abstract (abstract has ~40% TTX, not 34.7 µM). Confirming 34.7 requires body text.

---

## Summary table

| ID | identifier_ok | supports_claim | Metadata discrepancies | Required correction |
| --- | --- | --- | --- | --- |
| SRC-HERSHEY-2025 | yes | — | Print 2025-09-03 vs online 2025-08-21; abstract 500 mM vs methods 500 µM riluzole | Record DOI 10.1021/acschemneuro.5c00518; PMC is NIHMS2108906 |
| A-HERSHEY-INFUSION | yes | yes | none | none; 144 nM is dialysate, not Capp |
| A-HERSHEY-TAILPINCH | yes | partial | “neuronally-derived” is interpretation of ¹³C₅-Glu | Figure 7; 155 ± 14% of pre-pinch ¹³C₅-Glu, n=4; TTX n=3; ¹²C-Glu unchanged |
| A-HERSHEY-KPLUS | yes | partial | “~160%” omits ±20%; “neuronal” = ¹³C₅-Glu | Figure 6; ¹²C-Glu 160 ± 20%, n=4; ¹³C₅-Glu no increase |
| A-HERSHEY-CAPP | yes | yes | numbers are in §3.1 text, not a figure/table | none on values; label Capp / Ed-corrected, n=11 SEM |
| SRC-HASCUP-2010 | yes | — | none | PMID 20969570 = this rat PFC MEA paper |
| A-HASCUP2010-RESTING-TTX | yes | yes | n=41 vs n=7 fused in the slogan | split §3.1 34.7 vs Figure 2 −40.8 ± 10.8% |
| SRC-HASCUP-2008 | yes | — | epub 2007 / print 2008 | **PMID 18024788** |
| A-HASCUP2008-TTX20 | yes | partial | “small enzyme electrode” and implied rat/PFC | mouse Str GluOx MEA, Figure 5, ~20% of Table 1 Str mean |

**Ledger files were not edited.**
