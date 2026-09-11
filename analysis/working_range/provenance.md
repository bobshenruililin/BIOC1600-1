# Provenance — A3 working range

Rebuild does not download literature. Every plotted number is copied from `research/evidence/core_evidence.csv` or is a ratio of two such numbers (labeled SIMULATION / computational illustration).

| object | value | ledger locator | quantity_type |
| --- | --- | --- | --- |
| glu1 range | 0.01 pM–1 nM | E003 `numerical_result` | analytical_working_range |
| glu1 LOD | 0.0013 pM | E002 | sensor_LOD |
| Abrantes range | 1 aM–10 pM | E041 `numerical_result` | analytical_working_range |
| Abrantes LOD | 1 aM | E040 | sensor_LOD |
| Xiao FET range | 10 fM–100 nM | E026 `numerical_result` | analytical_working_range |
| Xiao FET LOD | 10 fM | E025 | sensor_LOD |
| Hu AuED-MEA range | 0.1 nM–10 µM | E007 `numerical_result` | analytical_working_range |
| Hu AuED-MEA LOD | 32 pM | E005 | sensor_LOD |
| Hu PaC Ames range | 10 nM–10 µM | E044 `numerical_result` | analytical_working_range |
| Hu PaC PBS window | 1 nM–1 mM | E044 `comparator` (not a dedicated range cell) | treated as analytical_working_range text already in the ledger |
| Hu PaC PBS LOD | 0.3 pM | E043 | sensor_LOD (PBS; not Ames) |
| Herman tonic | 25 nM | E034 (claim C012) | biological_concentration_range |
| Clements cleft | 1.1 mM | E032 (claim C011) | biological_concentration_range |
| Herman NMDAR EC50 | 1.8 µM | E035 | EC50 (receptor, not aptamer) |

Fold columns in `tables/range_table.csv` are computed as `pole_M / hi_M` when `hi_M < pole_M`. They are not experimental results.

Not used (absent from this package's inputs, or present but unpaired):

- E006 51.5 pM serum LOD — no serum working-range row
- E004 / C005 Hu 1.8 nM electrochemical EC50 — occupancy overlay forbidden
- C027 81-fold Langmuir identity — occupancy, not a calibration span
- Moussawi 0.02–30 µM — not in `core_evidence.csv`
- Mission 1 backup note of PBS ACV shown to 2 mM — not a ledger `numerical_result`; omitted
