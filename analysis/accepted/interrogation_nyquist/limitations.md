# Limitations — A4 interrogation Nyquist

- **Literature stimulus, not a recording.** The millisecond trace is constructed from Herman 25 nM (E034/C012) plus Clements 1.1 mM decaying with τ = 1.2 ms (E032/E033/C011). Clements is a kinetic inference at cultured hippocampal synapses (abstract; VoR closed; transferable unknown). Herman is acute-slice ambient glutamate, not an extrasynaptic-only measurement. Neither number was measured at a GCL-positioned parylene-C electrode.
- **Architecture clocks, not binding rates.** 14 s (E045) is interrogation. ~1 min (E046) is sampling. Protocol time ≠ koff. Glutamate `kon`/`koff` remain empty (C007). This figure does not fill that cell.
- **Nyquist is a sketch.** τ/2 = 0.6 ms treats 1/τ as a characteristic frequency. An exponential is not band-limited, so this is not a Shannon reconstruction theorem. The load-bearing fact is coarser: 14 s and 60 s are 10⁴–10⁵ times τ, so waveform shape is not a degree of freedom of the measurement.
- **Infinite-fast occupancy is a hypothetical measurement-operator argument**, not a glutamate rate and not a simulated θ(t).
- **No spatial dilution.** A GCL-positioned electrode is not a cleft. No volume, distance, or “mean-equivalent nM” is computed onto the figure. The rectangular-window mean exists only in tests, as a check that peak identity is lost, and is not written to SVG, caption, or `clocks.csv`.
- **Electrode diameter is not used.** A 25 µm figure appears in sealed Hu notes, not as a `claims.csv` / `core_evidence.csv` numerical_result. It is not a plotted number here.
- **Incubation/plateau are other protocol times.** Journal 15 min (C006/E008) and thesis 10 min plateau (C028/E042) are off-figure. They are not interrogation, not sampling, and not koff.
- **IPA 2 ms and GlutOx 500–800 ms are other-class.** Tobramycin interrogation (C009) and an enzyme comparator (C022) stay off-figure except as a caption footnote. They are not glutamate-aptamer rates.
- **Authors already refuse the claim.** C031 states the retina ACV reports basal glutamate, not synaptic transients. The computation makes that refusal the cleft-column limiter; it is not a new wet-lab result.
- **Not Mission 1 close.** Implementing A4 does not approve a thesis, does not change `state/gates`, and does not enter the scoreboard.
