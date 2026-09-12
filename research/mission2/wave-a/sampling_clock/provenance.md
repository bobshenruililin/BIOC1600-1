# Provenance — interrogation/sampling-timescale mismatch

Rebuild does not download literature. Values are read from `research/evidence/core_evidence.csv` with pins in `ledger.py`. Claims C031/C007 are read from `state/claims.csv` for the author sentence and the empty kinetics cell.

This session independently re-read: PubMed abstract of Clements 1992 (PMID 1359647); OA HTML extract of Hu 2025 RWTH thesis (DOI 10.18154/RWTH-2025-07238, publications.rwth-aachen.de/record/1017243). PDF not stored in git.

| symbol | value | ledger | stamp | quantity class |
| --- | --- | --- | --- | --- |
| inferred cleft peak | 1.1 mM | E032 / C011 | INFERRED | biological_concentration_range |
| inferred cleft τ | 1.2 ms | E033 / C011 | INFERRED | stored as `response_time`; caption says biological τ |
| slice ambient | 25 nM | E034 / C012 | MEASURED elsewhere | biological_concentration_range; **not spliced** |
| ACV scan | 14 s | E045 / C034 | MEASURED | interrogation (`measurement_time`) |
| retina sampling | 1 min | E046 / C031 | MEASURED | sampling (`measurement_time`) |
| journal Glu wait | 15 min | E008 / C006 | MEASURED | incubation; **off-figure** |
| thesis 10 nM plateau | 10 min | E042 / C028 | MEASURED | plateau; **off-figure** |
| 14 s / 1.2 ms | 11666.7 | derived | MODELED | clock ratio, not koff |
| 60 s / 1.2 ms | 50000 | derived | MODELED | clock ratio, not koff |
| glutamate kon/koff | empty | C007 | UNKNOWN | not used |
| PaC occupancy in Ames/tissue | empty | — | UNKNOWN | not used |
| [Glu] at GCL electrode | empty | — | UNKNOWN | not used |

C011 packs peak and τ in one claim text; this analysis uses the split evidence rows E032 and E033.

Not used: any glutamate `kon`/`koff`; tobramycin IPA rates (C008); Ding ITC (C010); White packing densities; Hu 1.8 nM EC50; spatial-dilution geometry; Shannon/Nyquist τ/2 as a sensor spec.

Closed unmerged provenance: PR #24, branch `cursor/analysis-nyquist-634f` @ `4ac44f74d72a90cdb0b2ff13287ee1ca826d7a83`. This package is an independent rebuild, not a copy into `analysis/accepted/`.
