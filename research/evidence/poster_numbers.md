# Poster-worthy numbers

Every row is a number that could appear on a storyboard. Reviews are not used as the sole source when a primary row exists. `independently_verified` means this session re-located the number in the cited text (OA/PMC/abstract).

| construct | format | matrix | quantity | value | source | verified |
| --- | --- | --- | --- | --- | --- | --- |
| 1d04 SELEX isolate | Capture-SELEX / affinity (abstract) | complex medium (unspecified in abstract) | Kd_molecular | 12 µM | Wu 2022 S001 PMID 34783880 abstract | yes, abstract only |
| truncated glu1 Fc-thiol-MCH | gold E-AB ACV | LOD matrix unspecified in abstract | sensor_LOD | 0.0013 pM | Wu 2022 S001 abstract | yes, abstract only |
| truncated glu1 Fc-thiol-MCH | gold E-AB ACV | unspecified in abstract | analytical_working_range | 0.01 pM–1 nM | Wu 2022 S001 abstract | yes, abstract only |
| Hu Glu-apt Fc-thiol truncated oligo | methods citation of Wu, not a measurement | cited solution-phase | Kd_molecular (citation) | 12 µM | Hu 2025 S002 methods | yes, VoR |
| Hu Glu-apt Fc-thiol on AuED-MEA | ACV Langmuir–Freundlich | PBS | EC50 / apparent electrochemical Kd | 1.8 nM | Hu 2025 S002 §3.2 | yes, VoR |
| Hu Glu-apt Fc-thiol on AuED-MEA | ACV blank+3SD | PBS | sensor_LOD | 32 pM | Hu 2025 S002 Fig. 4h | yes, VoR |
| Hu Glu-apt Fc-thiol on AuED-MEA | ACV | 50% human serum | sensor_LOD | 51.5 pM | Hu 2025 S002 §3.4 / Fig. S11 | yes, VoR |
| Hu Glu-apt Fc-thiol on AuED-MEA | ACV semi-log | PBS | analytical_working_range | 0.1 nM–10 µM | Hu 2025 S002 Fig. 4e | yes, VoR |
| Hu Glu-apt Fc-thiol on AuED-MEA | incubation before ACV | PBS | measurement_time | 15 min | Hu 2025 S002 §3.2 Fig. S8 | yes, VoR |
| Xiao glutamate aptamer | SPR | not specified as 0.1× PBS in SPR sentence | Kd_molecular | 293 nM | Xiao 2025 S021 Fig. S6 | yes, PMC XML |
| Xiao glutamate aptamer on AuNP/CNT FET | FET | 0.1× PBS | sensor_LOD | 10 fM | Xiao 2025 S021 | yes, PMC XML |
| Xiao glutamate aptamer FET | FET Ids | 0.1× PBS | analytical_working_range | 10 fM–100 nM | Xiao 2025 S021 Fig. 3f | yes, PMC XML |
| Xiao multiplex FET | real-time after 10 nM target | 0.1× PBS | response_time | 200 s | Xiao 2025 S021 Fig. 5e | yes, PMC XML |
| NG-Apt-Glu (in silico, preprint) | graphene FET | aCSF | sensor_LOD | 1 aM | Abrantes 2025 S010 abstract | yes, abstract; not peer-reviewed |
| not aptamer; cultured synapses | kinetic inference | synaptic cleft (culture) | biological_concentration_range | 1.1 mM | Clements 1992 S049 abstract | yes, abstract only |
| not aptamer; cultured synapses | kinetic inference | synaptic cleft (culture) | decay tau (stored as response_time) | 1.2 ms | Clements 1992 S049 abstract | yes, abstract only |
| not aptamer; NMDAR reporter | tonic current | acute hippocampal slice | biological_concentration_range | ~25 nM | Herman 2007 S050 | yes, PMC HTML |
| not aptamer; GlutOx MEA | enzyme electrode | freely moving rat CNS | response_time | 500–800 ms | Rutherford 2007 S054 | yes, PMC HTML |
| not aptamer; GlutOx model | continuum simulation | model of enzyme stack | response_time | 0.73 s simulated | Clay 2018 S055 | yes, PMC HTML; simulation |
| not aptamer; GlutOx experiment | cited experimental match | enzyme stack | response_time | 0.8 ± 0.2 s | Clay 2018 S055 | yes, PMC HTML |
| 1:1 Langmuir (derived) | occupancy identity | none | 10–90% concentration span | 81-fold | derived; Rousseau 2023 states the same | computational; Rousseau is not sole evidence |
| tobramycin parent aptamer E-AB | IPA flow | tris buffer | kon | 3.5×10^4 M⁻¹ s⁻¹ | Abeykoon 2025 S004 | yes, PMC HTML; **not glutamate** |
| tobramycin parent aptamer E-AB | IPA flow | tris buffer | koff | 1.39 s⁻¹ | Abeykoon 2025 S004 | yes; **not glutamate** |
| tobramycin parent aptamer E-AB | IPA | — | measurement_time | 2 ms | Abeykoon 2025 S004 | yes; interrogation clock |
| cocaine E-AB | ACV/DPV | 1× SSC | response_time | faster than ~4 s scan | White 2008 S033 | yes, PMC HTML; **not glutamate** |
| glutamate DNA aptamer (any inspected) | E-AB / SPR / FET | — | kon / koff | not reported | Round 2 search plus overnight hunter | absence; unresolved |
| Hu Glu-apt on parylene-C intraretinal probe | ACV wait after 10 nM Glu | probe calibration | measurement_time | 10 min plateau | Hu 2025 thesis S066 Fig. 6.6 | yes, OA extract |
| Hu Glu-apt on parylene-C probe | ACV blank+3 RSD | PBS calibration | sensor_LOD | 0.3 pM | Hu 2025 thesis S066 Fig. 6.7 | yes, OA extract |
| Hu Glu-apt on parylene-C probe | ACV semi-log | Ames medium | analytical_working_range | 10 nM–10 µM | Hu 2025 thesis S066 Fig. 6.9A | yes, OA extract |
| Hu Glu-apt on parylene-C probe in mouse retina | ACV scan clock | in vitro retina | measurement_time | 14 s / scan | Hu 2025 thesis S066 §6.3 | yes, OA extract |
| Hu Glu-apt on parylene-C probe in mouse retina | consecutive ACV sampling | in vitro retina | measurement_time | 1 min / point | Hu 2025 thesis S066 §6.3 | yes, OA extract |

Do not plot the not-glutamate kinetic rows as glutamate rates.
Do not treat the thesis 10 min plateau or 1 min sampling as a measured glutamate koff.
