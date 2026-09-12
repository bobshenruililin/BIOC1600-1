# Limitations — occupancy/kinetics

- Diffusion-limited kon is an upper bound. Slower real kon makes every t_off longer.
- Empirical C008/C010 kon values are **not glutamate**. They are used only as a labeled envelope that can **contradict** T5’s 0.8 ms 1d04 story.
- Hu 1.8 nM is Langmuir–Freundlich electrochemical apparent Kd on AuED-MEA in PBS, not solution molecular Kd and not the PaC retinal probe’s Kd. The occupancy curves are 1:1 Langmuir overlays of advertised numbers. Overlay θ(25 nM)>0.9 is locked as math in `test_overlay_theta_at_herman_ambient_if_1p8nm_treated_as_1to1_kd`; it is not tissue occupancy.
- 1d04 12 µM is from a closed-VoR abstract.
- Clements peak/tau is not a chemical assay.
- No glutamate aptamer kon/koff is used, because none was found.
- τ_eq = 1/(kon c + koff) at 1.1 mM is not t_off. Do not quote koff ≈ 1/1.2 ms.
- Enzyme GlutOx times are comparators, not aptamer data.
- Hu thesis 10 min plateau / 1 min retina sampling are protocol times (E042, E046), not fitted koff.
