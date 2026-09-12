Figure (Mission 2 Wave B candidate, not accepted): Horizontal bars are reported `analytical_working_range` copied from `research/evidence/core_evidence.csv`. LEDGER calibration windows, not occupancy and not Kd. Fold-below numbers are MODELED ratios (pole / ceiling) when the ceiling is below the pole. Empty LOD cells stay empty. No interpolation.

Quantity types:
- `analytical_working_range` — bars (E003 glu1 0.01 pM–1 nM abstract; E041 Abrantes preprint 1 aM–10 pM aCSF; E026 Xiao 10 fM–100 nM in 0.1× PBS; E007 Hu AuED-MEA 0.1 nM–10 µM PBS; E044 Ames 10 nM–10 µM; E044 comparator PBS 1 nM–1 mM). Ames/PBS PaC spans are ledger pins (S066 OA PDF not re-opened this session).
- `biological_concentration_range` — solid ticks: Herman ~25 nM (C012/E034, INFERRED ambient in acute hippocampal slice; standing currents are MEASURED). Clements 1.1 mM (C011/E032, INFERRED cleft peak at cultured synapses, abstract). These are different hippocampal preparations. They are not one device spec and not a retinal range.
- `EC50` — dashed tick: Herman converted Glu NMDAR EC50 ~1.8 µM (E035). OA this session: NMDA EC50 37.7 µM is MEASURED (nucleated patch Hill fit); × 0.048 conversion ≈ 1.81 µM is INFERRED. Receptor EC50, not Hu electrochemical EC50, not a basal pole.
- `sensor_LOD` — unconnected open dots, same construct/matrix only. E043 0.3 pM is PBS, not Ames. Ames LOD cell empty. Do not bin Hu 32 pM with Wu 0.0013 pM or Abrantes 1 aM.
- CANDIDATE ticks (open): Hershey Capp 9.4 µM (INFERRED), Hershey 144 nM dialysate (MEASURED), Hascup 2010 34.7 µM (MEASURED), Hascup 2008 3.3 / 5.0 µM (MEASURED). Not `claims.csv`. Not averaged with 25 nM.

SI-strict containment: no plotted bar contains both C012 25 nM and C011 1.1 mM. Xiao 100 nM vs 1.1 mM is 11000-fold, not 11-fold. PBS PaC 1 mM is 1.1-fold below 1.1 mM. Ames contains 25 nM and the candidate 3.3 / 5.0 / 9.4 µM poles and misses Hascup 2010 34.7 µM (3.47-fold below). Containment is geometric on the reported span, not SNR-qualified quantification (Ames 41.6% blank noise).

Hu 1.8 nM Langmuir–Freundlich electrochemical EC50 (C005) is not plotted. Occupancy θ is not plotted. Hu fitted n is UNKNOWN. Occupancy 10–90% width is MODELED as 81^(1/n); that algebra does not change device-bar arithmetic and does not restore 81-versus-44000 as flagship.

Not Mission 1 close. Not group-final. Not a polished poster. Not `analysis/accepted/`.

Figure (MODELED occupancy-window width, not a device bar): For θ = c^n/(Kd^n + c^n) with Kd as c50, the 10–90% occupancy span is exactly 81^(1/n). n=1 → 81; n=0.5 → 6561; n=2 → 9. Hu fitted n is UNKNOWN. 1.8 nM is C005 EC50, not occupancy Kd, so this panel is not PaC tissue occupancy. The withdrawn 81-versus-44000 comparison is not plotted. Pairing Herman 25 nM with Clements 1.1 mM as one device spec is refused even if n were later measured.
