# Limitations — A3 working range

- Herman 25 nM and Clements 1.1 mM are hippocampal literature poles. Overlaying them on glutamate-aptamer calibrations is a labeled comparison. Transferable: **no**.
- Clements 1.1 mM / 1.2 ms is a kinetic inference (abstract), not a chemical assay at a retina electrode.
- Wu glu1 range and Abrantes range are abstract-only / preprint. Abrantes stays preprint.
- Xiao range is 0.1× PBS, not 1× aCSF and not tissue.
- Hu MEA range is PBS on AuED-MEA, not the parylene-C probe.
- PaC PBS 1 nM–1 mM is E044 **comparator** text (“PBS 1 nM-1 mM linear window”), not a dedicated `analytical_working_range` `numerical_result`. If that string is removed from the ledger, the row is omitted.
- SI-strict containment: 1 mM does **not** contain 1.1 mM. The proposal table's “PBS contains 1.1 mM” is not reproduced.
- Xiao 100 nM vs 1.1 mM is **11000-fold**, not the proposal table's 11-fold (unit mix).
- Ames authors report 41.6% blank noise and poor quantitative SNR (E044 limitation text). That is SNR, not occupancy, and is not drawn as a third pole.
- E043 0.3 pM is PBS `sensor_LOD`, not Ames/tissue LOD. Ames LOD cell is empty.
- Hu 1.8 nM Langmuir–Freundlich EC50 is not plotted. Occupancy θ is not computed.
- NMDAR EC50 1.8 µM (E035) is a receptor number. It is not Hu 1.8 nM and is not a biological concentration pole of the same type as 25 nM / 1.1 mM.
- Moussawi tonic band is not in `core_evidence.csv` and is not drawn.
- Constructs and matrices are separate rows. Do not bin Hu 32 pM with Wu 0.0013 pM or Abrantes 1 aM.
- This package is an isolated draft analysis. It is not Mission 1 close, not an accepted flagship, and not a poster.
