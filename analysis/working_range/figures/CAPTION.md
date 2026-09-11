Figure (A3): Horizontal bars are reported `analytical_working_range` copied from `research/evidence/core_evidence.csv`. This is a LEDGER plot of calibration windows, not an occupancy figure and not a Kd figure. Fold-below annotations are SIMULATION / computational illustration (ratio of a literature pole to a reported ceiling). No interpolation. Empty cells stay empty.

Quantity types on this figure:
- `analytical_working_range` — bars (E003 glu1 0.01 pM–1 nM; E041 Abrantes preprint 1 aM–10 pM; E026 Xiao 10 fM–100 nM in 0.1× PBS; E007 Hu AuED-MEA 0.1 nM–10 µM in PBS; E044 Ames 10 nM–10 µM; E044 comparator PBS 1 nM–1 mM linear window).
- `biological_concentration_range` — solid vertical ticks: Herman ~25 nM tonic (C012/E034, hippocampal slice); Clements 1.1 mM cleft inference (C011/E032, cultured synapses). These are not retina measurements.
- `EC50` — dashed tick: Herman NMDAR EC50 1.8 µM (E035). Receptor EC50, not an aptamer Kd, not Hu 1.8 nM.
- `sensor_LOD` — unconnected open dots, paired only to the same construct/matrix. E043 0.3 pM is PBS calibration LOD (C029), not an Ames or tissue LOD. Ames has no sensor_LOD in the ledger, so that cell stays empty. Do not bin Hu 32 pM (E005) with Wu 0.0013 pM (E002) or Abrantes 1 aM (E040).

SI-strict containment (do not round 1.1 mM to 1 mM): no plotted bar contains both 25 nM and 1.1 mM. The PBS PaC ceiling is 1 mM, which is 1.1-fold below 1.1 mM. Ames and Hu MEA ceilings (10 µM) are 110-fold below 1.1 mM. Xiao's 100 nM ceiling is 11000-fold below 1.1 mM (not 11-fold). glu1's 1 nM ceiling is 25-fold below 25 nM; Abrantes' 10 pM ceiling is 2500-fold below 25 nM.

Hu electrochemical apparent Kd 1.8 nM is not plotted. Occupancy θ is not plotted. Moussawi 0.02–30 µM is not in `core_evidence.csv` and is not drawn.

Not Mission 1 close. Not group-final. Not a polished poster.
