# Provenance — occupancy/kinetics

| symbol | value | origin |
| --- | --- | --- |
| 12 µM | 1d04 Kd | Wu 2022 abstract E001 |
| 1.8 nM | Hu apparent Kd | Hu 2025 §3.2 E004; AuED-MEA PBS Langmuir–Freundlich; not PaC-probe tissue occupancy |
| 293 nM | Xiao SPR Kd | Xiao 2025 E024 |
| 25 nM | slice ambient | Herman 2007 E034; acute hippocampal slice literature example, not retina |
| 1.1 mM, 1.2 ms | cleft inference | Clements 1992 E032/E033; cultured hippocampal synapses, different preparation |
| 15 min | Hu Glu ACV wait | Hu 2025 E008 |
| 200 s | Xiao FET stabilize | Xiao 2025 E027 |
| 500 ms | GlutOx lower end | Rutherford 2007 E037 |
| kon 1e8 M⁻¹ s⁻¹ | diffusion-limit bound | assumption, not a paper |
| kon 96–2e5 M⁻¹ s⁻¹ | ITC envelope | Ding 2024 C010; NOT glutamate |
| kon 3.5e4 M⁻¹ s⁻¹ | tobramycin IPA | Abeykoon 2025 C008; NOT glutamate |
| 10 min / 0.3 pM / 1 min | retina probe | Hu 2025 thesis E042–E046; not used as koff |

Rebuild does not download literature. Occupancy parameters are hardcoded from the ledger with tests. Atlas cells are copied from `core_evidence.csv`.
