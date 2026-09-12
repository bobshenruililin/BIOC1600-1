# Limitations — Mission 2 Wave B working range

- Herman 25 nM is an efficacy-scaled NMDAR **inference** in acute P15–19 hippocampal slice, not a chemical assay and not extrasynaptic-only. Overlaying it on aptamer calibrations is a labeled comparison. Transferable: **no**.
- Clements 1.1 mM is a kinetic inference at **cultured** hippocampal synapses (abstract). Different preparation from Herman. Not a retina-electrode spec. Do not splice with 25 nM into one device requirement.
- Wu glu1 range and Abrantes range are abstract-only / preprint. Abrantes stays preprint. Preprint body this session also writes linearized response to 1 pM and saturation at 1 pM while the abstract/ledger span is 1 aM–10 pM. Either ceiling still misses 25 nM from above. Package copies the ledger span.
- PaC PBS 1 nM–1 mM is E044 **comparator** text, not a dedicated `analytical_working_range` `numerical_result`. S066 dissertation PDF was **not** re-opened this session; Ames/PBS PaC numbers are ledger pins plus prior OA extract.
- SI-strict: 1 mM does **not** contain 1.1 mM. Xiao 100 nM vs 1.1 mM is **11000-fold**, not 11-fold.
- Ames authors report 41.6% blank noise. Geometric containment ≠ quantitative SNR.
- E043 0.3 pM is PBS `sensor_LOD`, not Ames/tissue. Ames LOD cell is empty.
- Hu 1.8 nM is Langmuir–Freundlich electrochemical EC50. Fitted **n unpublished** (OA §3.2 names the model and the 1.8 nM value; no exponent). Occupancy θ is not computed onto the bar figure.
- Candidate Hershey/Hascup poles are method-class-locked and **not** `claims.csv`. Do not average them with 25 nM. Hershey 9.4 µM is Capp, not the 144 nM labeled dialysate.
- Hascup 2010 34.7 µM error type (SEM vs SD) is UNKNOWN in the inspected parenthetical. Table I hippocampus 4.7–10.4 µM is unpublished data — not used.
- Occupancy `81^(1/n)` does not change device-bar endpoints. Inverse n* for 44000-fold is algebra on a **withdrawn pairing**, not Hu’s n and not a flagship.
- NMDAR Glu EC50 1.8 µM is a converted receptor number (INFERRED from NMDA 37.7 µM × 0.048). Digit collision with Hu 1.8 nM stays named.
- This package is an isolated analysis candidate. It is not Mission 1 close, not an accepted flagship, and not a poster.
