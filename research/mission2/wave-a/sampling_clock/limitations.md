# Limitations — interrogation/sampling-timescale mismatch

- **Not accepted flagship.** This is a Mission 2 analysis candidate. Reproducible arithmetic is not group-final science.
- **Literature waveform, not a recording.** The millisecond trace is Clements 1.1 mM decaying with τ = 1.2 ms (E032/E033/C011). Clements is a kinetic inference at cultured hippocampal synapses (PubMed abstract re-read this session; VoR closed; `full_text_inspected=no` in the ledger). Transferable to a GCL-positioned parylene-C electrode: unknown.
- **Herman 25 nM is not spliced.** PR #24 constructed a chimeric pulse (slice ambient + cleft peak). Amplitude is not required for T/τ. E034 remains a labeled hippocampal-slice ambient row and is off the plotted waveform.
- **Architecture clocks, not binding rates.** 14 s (E045) is interrogation. ~1 min (E046) is sampling. Protocol time ≠ koff. Glutamate `kon`/`koff` remain empty (C007). This figure does not fill that cell.
- **Nyquist is not used.** Shannon reconstruction requires a band-limited signal, a stated highest frequency, a regular point sampler, and a reconstruction claim. An exponential is not band-limited. An ACV voltage sweep is not a regular sampler of [Glu](t). No reconstruction operator is claimed. The load-bearing MODELED fact is coarser: 14 s and 60 s are 10⁴–10⁵ times 1.2 ms, and one scan yields one scalar.
- **Infinite-fast occupancy is a hypothetical measurement-operator argument**, not a glutamate rate and not a simulated θ(t).
- **No spatial dilution.** A GCL-positioned electrode is not a cleft. No volume, distance, or mean-equivalent nM is computed onto the figure. A rectangular-window mean is not computed in this package.
- **Electrode diameter is not used.** The OA thesis names Ø 25 µm for the large bottom electrode; that number is not a `claims.csv` / `core_evidence.csv` numerical_result and is not plotted.
- **Incubation/plateau are other protocol times.** Journal 15 min (C006/E008) and thesis 10 min plateau (C028/E042) are off-figure. They are not interrogation, not sampling, and not koff.
- **IPA 2 ms and GlutOx 500–800 ms are other-class.** Tobramycin interrogation (C009) and an enzyme comparator (C022) stay off-figure except as a caption footnote.
- **Authors already refuse the synaptic-transient claim.** C031 / S066 §6.3 states the retina ACV reports basal glutamate, not synaptic transients. The computation makes that refusal quantitative for a *named* 1.2 ms waveform; it is not a new wet-lab result and it does not convert Hu’s basal retina experiment into a failed cleft experiment.
- **If Layer 2 is the wrong biological spec, Layer 3 does not grade the retina experiment.** Light-on/off over minutes is the manipulation that was run.
