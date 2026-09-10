# Citation audit (Round 2)

Auditor role: re-fetch identifiers; check claim–paper fit. Date: 2026-09-10. Europe PMC/Crossref/PubMed/PMC HTML/OA PDF. No Sci-Hub.

Identifier rule: a source is `identifier_ok=yes` only if DOI and/or PMID resolve to the stated title/authors.

## Starting leads

| source | PMID / DOI | identifier_ok | notes |
| --- | --- | --- | --- |
| S001 Wu 2022 | 34783880 / 10.1007/s00216-021-03783-w | yes | Europe PMC title match. VoR closed. Abstract only. |
| S002 Hu 2025 | 40992279 / 10.1016/j.bios.2025.117992 | yes | PubMed, Crossref, Europe PMC agree. CC BY VoR re-read 2026-09-10 (RWTH OA PDF). Europe PMC `isOpenAccess=N` is a metadata mismatch, not an identifier failure. |
| S003 Ding 2024 | 38785220 / 10.1002/cbic.202400225 | yes | Abstract only. Not glutamate. |
| S004 Abeykoon 2025 | 41231675 / 10.1021/acs.analchem.5c01604 | yes | PMC13101946 HTML. Tobramycin, not glutamate. |
| S006 Xu/Tanner 2026 | 41851736 / 10.1186/s12951-026-04194-8 | yes | PMC13112887 XML. N-protein fiber, not glutamate. |
| S007 InstructNA 2026 | 41813969 / 10.1038/s43588-026-00965-3 | yes | PMC13121014 XML. LOX1/CXCL5 proteins, not glutamate. |
| S021 Xiao 2025 | 40433802 / 10.1002/advs.202504497 | yes | PMC12376627 XML. Glutamate SPR + FET in 0.1× PBS. |
| S049 Clements 1992 | 1359647 / 10.1126/science.1359647 | yes | Abstract: 1.1 mM, 1.2 ms. VoR closed. |
| S050 Herman 2007 | 17804634 / 10.1523/JNEUROSCI.3009-07.2007 | yes | PMC2670936 HTML. Ambient ~25 nM. |
| S030 Rousseau 2023 | 38152504 / 10.1149/2754-2726/ad15a1 | yes | PMC10750225 XML. 81-fold Langmuir 10–90%. |
| S054 Rutherford 2007 | 17630982 | yes | PMC3482110 HTML. GlutOx 500–800 ms. |
| S055 Clay 2018 | 29076724 | yes | PMC5881573 HTML. Simulated 0.73 s; experimental 0.8 ± 0.2 s. |
| S062 Armbruster 2020 | 32352378 | yes | PMC7255799 XML. iGluSnFR 10–100× longer waveform. |
| S023 Park 2023 | 37185488 | yes | PMC10136356. Table “Glutamate FET” is PfGDH. |
| S010 Abrantes 2025 preprint | 10.1101/2025.11.05.686731 | yes | bioRxiv/Europe PMC abstract. Not peer-reviewed. |
| S066 Hu 2025 thesis | 10.18154/RWTH-2025-07238 | yes | RWTH publications record + OA PDF text extract. Same Glu-apt family as S002. PDF not stored in git. |
| S008 Ohsawa 2008 | 18187867 | yes | Abstract only this session. JSTAGE PDF 500. Do not enter 580–810 µM. |
| S038 MacDonald 2019 | 10.1021/acs.jpcc.9b00845 | yes (DOI in ledger) | Full text not re-fetched (ACS 403 / HAL challenge). Surface-crowding numbers not entered as claims. |

## Claim–source fit (adversarial)

| claim | supports_claim | reason |
| --- | --- | --- |
| C001 1d04 Kd 12 µM | yes | Wu abstract: isolation of aptamer 1d04 with dissociation constant 12 µM. |
| C002 glu1 LOD 0.0013 pM | yes | Wu abstract: truncated glu1 sensor LOD 0.0013 pM, range 0.01 pM–1 nM. |
| C003 Kd ≠ LOD | interpretive | Construct split is in the abstract. Transfer of 1d04 Kd onto glu1 LOD is **not** supported. |
| C004 Hu Glu LOD 32 / 51.5 pM | yes | Hu §3.2 Fig. 4h PBS 32 pM; §3.4 / Fig. S11 serum 51.5 pM. |
| C005 Hu apparent Kd 1.8 nM | yes as **EC50/apparent electrochemical Kd** | Langmuir–Freundlich fit of ACV. Authors contrast with cited solution values. Not solution molecular Kd. |
| C006 Glu 15 min incubation | yes | Hu §3.2: ACV after 15 min for Glu, 10 min for DA. Fig. 3f 15 min is **ST**, not Glu. |
| C007 no Glu kon/koff | absence | No kon/koff in inspected Glu sensor papers. Not a negative experimental result. |
| C008–C009 tobramycin IPA | yes, not transferable | PMC13101946. |
| C011 cleft 1.1 mM / 1.2 ms | yes, inference | Clements abstract. Not a chemical assay. |
| C012 ambient 25 nM | yes | Herman abstract and body: “near 25 nM”; “estimated value of 25 nM”. Word *extrasynaptic* appears in a **citation**, not as Herman’s own compartment label. |
| C013 81-fold | yes as theory | Rousseau: “Langmuir isotherm, which predicts an 81-fold target concentration difference between 10% and 90% of aptamers bound.” |
| C014 Xiao 293 nM vs 10 fM | yes | SPR Kd glutamate 293 nM; practical LOD 10 fM; Glu range 10 fM–100 nM in 0.1× PBS; stabilize after 200 s. |
| C015 Tanner tetrahedron | yes, not Glu | Apparent fiber Kd 0.3981 vs 0.1996 µM; ~2–2.5×; plateau ~25 min. |
| C016 InstructNA | yes, not Glu | G1L 12.9 nM; G1C 6.6 nM; many sequences weak/non-binders. |
| C017 docking failure | yes as computation | Xie/Liu: docking scores fail to distinguish theophylline from caffeine despite cited 250,000-fold affinity difference. |
| C018 White packing density | yes, not Glu | Cocaine gain 60–200%; apparent Kd 327±64, 101±8, 127±35 µM; cocaine faster than ~4 s scan; thrombin 11–20 min. |
| C019 Park GDH | yes as **refutation** | Table 1 “Au Glutamate FET … [59]” and body: *Plasmodium falciparum* glutamate dehydrogenase, Singh 2019. |
| C021 Hu cites Wu 12 µM | yes | Experimental section: “Glutamate aptamer (Glu-apt, Kd = 12 μM) (Wu et al., 2022)” then the truncated Fc-thiol sequence. |
| C022–C024 comparators | yes | Enzyme / indicator papers, not aptamers. |
| C025 Abrantes 1 aM | yes as preprint abstract | ELONA millimolar Kd **not** in abstract; `supports_claim=no` for millimolar Kd. |
| C028–C032 Hu thesis retina | yes | OA dissertation text extract 2026-09-10. DOI 10.18154/RWTH-2025-07238. In vitro retina, not in vivo. 10 min plateau, 0.3 pM PBS LOD, Ames 10 nM–10 µM, 14 s ACV / 1 min sampling, basal-not-synaptic author sentence. |

## Secondary-source failures

- Lam 2022 (S011) table quotes Wu glu1 **LOD 0.0013 pM** and range 0.01 pM–1 nM. A 12 ± 6 µM Kd was **not** found in the inspected Lam PMC XML/HTML this session. Do not use ±6.
- Hu’s “physiologically relevant … brain” sentence is author interpretation, not a measured brain [Glu].

## Integrity notes

- Do not treat Europe PMC `isOpenAccess=N` as proof that Hu is closed; VoR is CC BY.
- Do not invent Ohsawa conjugate Kd or MacDonald surface Kd this round; identifiers ok, numbers not re-verified.
