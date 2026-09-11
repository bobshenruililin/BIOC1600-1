# Provenance — A4 interrogation Nyquist

Rebuild does not download literature. Values are read from `research/evidence/core_evidence.csv` with pins in `ledger.py`. Claims C031/C007 are read from `state/claims.csv` for the author sentence and the empty kinetics cell.

| symbol | value | ledger | quantity class |
| --- | --- | --- | --- |
| inferred cleft peak | 1.1 mM | E032 / C011 | biological_concentration_range |
| inferred cleft τ | 1.2 ms | E033 / C011 | stored as `response_time`; caption says biological τ |
| slice ambient (pulse floor) | 25 nM | E034 / C012 | biological_concentration_range |
| ACV scan | 14 s | E045 / C031 | interrogation (`measurement_time`) |
| retina sampling | 1 min | E046 / C031 | sampling (`measurement_time`) |
| journal Glu wait | 15 min | E008 / C006 | incubation; **off-figure** |
| thesis 10 nM plateau | 10 min | E042 / C028 | plateau; **off-figure** |
| Nyquist sketch | τ/2 = 0.6 ms | derived from E033 | COMPUTATIONAL ILLUSTRATION |
| 14 s / 1.2 ms | 11,667 | derived | clock ratio, not koff |
| 60 s / 1.2 ms | 50,000 | derived | clock ratio, not koff |
| glutamate kon/koff | empty | C007 | not used |

C011 packs peak and τ in one claim text; this analysis uses the split evidence rows E032 and E033 (ontology note in `research/evidence/quantity_ontology.md`).

A4 data list in the proposal named C031, E045, E046, C011, C006, C028. E034/C012 is included because the specified literature stimulus is 25 nM + 1.1 mM decaying with τ = 1.2 ms.

Not used: any glutamate `kon`/`koff`; tobramycin IPA rates (C008); Ding ITC (C010); White packing densities; Hu 1.8 nM EC50; spatial-dilution geometry.
