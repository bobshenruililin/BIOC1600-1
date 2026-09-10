# Round 1 scout merge

Six isolated `generalPurpose` scouts ran with the `literature-scout` contract (custom Task type `literature-scout` is not registered in this environment). Orchestrator merged and deduplicated by DOI then PMID.

## Identifier verification (Europe PMC 2026-09-10)

| Lead | Result |
| --- | --- |
| PMID 34783880 | Wu et al. 2022 *Anal Bioanal Chem* DOI 10.1007/s00216-021-03783-w. Closed VoR. |
| PMID 40992279 | Hu et al. 2025 *Biosens Bioelectron* 117992. PubMed/Crossref/Europe PMC agree. |
| PMID 38785220 | Ding and Liu 2024 *ChemBioChem* kinetic ITC. Closed VoR. Added by orchestrator after scouts missed it. |
| PMID 41231675 | Abeykoon et al. 2025 IPA tobramycin kinetics. PMC13101946. |
| PMID 41042013 | Wu and Plaxco 2025 E-AB design/fabrication review. PMC13005712. Added by orchestrator. |
| PMID 41851736 | Xu/Tanner 2026 tetrahedron optical fiber. N-protein, not glutamate. PMC13112887. |
| InstructNA DOI 10.1038/s43588-026-00965-3 | Zhang et al. 2026 *Nat Comput Sci*. PMID 41813969 PMC13121014. |

**No source promoted to `core`.** All 65 rows in `state/sources.csv` are `status=candidate`.

## Lane coverage after merge

- A: glutamate aptamer discovery (Wu 1d04/glu1; Ohsawa modified DNA; negative RNA-amino-acid SELEX maps)
- B: glutamate/neurotransmitter aptamer sensors (Hu multiplex MEA; Xiao CNT FET includes glutamate; Abrantes preprint; in vivo NT FETs are serotonin/dopamine not glutamate)
- C: E-AB kinetics vs interrogation time (no glutamate kon/koff found)
- D: immobilization/probe density/tetrahedron interface
- E: InstructNA/RaptGen/FASTAptamer plus docking/structure-prediction failure papers
- F: cleft/extrasynaptic/CSF biology vs GlutOx/FSCV/iGluSnFR

## Metadata disagreements recorded, not silently resolved

- Wu 2022 year: print 2022 vs epub 2021
- Wu Kd 12 µM (abstract, 1d04) vs glu1 sensor LOD 0.0013 pM (different construct)
- Lam 2022 quotes 12 ± 6 µM; the ±6 is not in the Wu abstract
- Abrantes ELONA Kd millimolar vs device attomolar LOD
- Park 2023 review table “glutamate FET” is *P. falciparum* GDH, not neurotransmitter glutamate

## Next

Select ~20–30 candidates as `relevant`. Double-extract the 10 most load-bearing papers. Still no core promotion until evidential status is clear.
