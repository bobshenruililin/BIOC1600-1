# Provenance — Mission 2 Wave B working range

Rebuild does not download literature. Canonical plotted numbers are copied from `research/evidence/core_evidence.csv` or are ratios of two such numbers (MODELED). Candidate basal poles are package-local (`candidates.py`), OA-rechecked this session, tagged `candidate`.

Closed-unmerged provenance reproduced: PR #23 / `cursor/analysis-working-range-634f` @ `924f794f5c2258d80394e34681248f470ceaabbc`. Canonical git used as input: `origin/main` @ `65971ae19714a783013e22a150cc474d26e9295c`.

| object | value | locator | quantity_type | stamp this package |
| --- | --- | --- | --- | --- |
| glu1 range | 0.01 pM–1 nM | E003; Wu PMID 34783880 abstract (re-read) | analytical_working_range | MEASURED as advertised; VoR closed |
| glu1 LOD | 0.0013 pM | E002; same abstract | sensor_LOD | MEASURED as advertised |
| Abrantes range | 1 aM–10 pM | E041; bioRxiv 10.1101/2025.11.05.686731 abstract + HTML this session | analytical_working_range | MEASURED as advertised in abstract/ledger; preprint. Body also writes linearized to 1 pM / saturating at 1 pM — not used as a bar |
| Abrantes LOD | 1 aM | E040; same abstract | sensor_LOD | MEASURED as advertised; preprint |
| Xiao FET range | 10 fM–100 nM | E026; Fig. 3f PMC12376627 (re-read) | analytical_working_range | MEASURED |
| Xiao FET LOD | 10 fM | E025; body “practical detection limit of 10 fM” | sensor_LOD | MEASURED; 0.1× PBS |
| Hu AuED-MEA range | 0.1 nM–10 µM | E007; S002 §3.2 / Fig. 4e OA PDF extract (re-read) | analytical_working_range | MEASURED |
| Hu AuED-MEA LOD | 32 pM | E005; Fig. 4h | sensor_LOD | MEASURED |
| Hu LF apparent Kd | 1.8 nM | E004 / C005; §3.2 OA extract | EC50 | MEASURED electrochemical fit; **n unpublished** |
| Hu PaC Ames range | 10 nM–10 µM | E044 `numerical_result`; C030 | analytical_working_range | ledger pin; S066 PDF **not** re-opened this session |
| Hu PaC PBS window | 1 nM–1 mM | E044 `comparator` | treated as range text already in the ledger | ledger pin; not a dedicated range cell |
| Hu PaC PBS LOD | 0.3 pM | E043 / C029 | sensor_LOD | ledger pin; PBS, not Ames |
| Herman tonic | 25 nM | E034 / C012; PMC2670936 HTML (re-read) | biological_concentration_range | **INFERRED** (currents MEASURED) |
| Clements cleft | 1.1 mM | E032 / C011; PMID 1359647 abstract (re-read) | biological_concentration_range | **INFERRED**; VoR closed |
| Herman NMDAR Glu EC50 | 1.8 µM | E035; OA this session: NMDA EC50 37.7 µM MEASURED × conversion 0.048 ≈ 1.81 µM | EC50 | **INFERRED** converted Glu EC50; NMDA 37.7 µM is the Hill-fit MEASURED number |
| Hershey Capp | 9.4 ± 0.6 µM | PMC12418293 §3.1 (re-read) | biological_concentration_range | INFERRED; **candidate** |
| Hershey 13C5 dialysate | 144 ± 35 nM | Abstract; Fig. 1B | biological_concentration_range | MEASURED dialysate; **candidate** |
| Hascup 2010 PFC | 34.7 µM ± 11.8 µM n=41 | PMC2996468 §3.1 parenthetical (re-read) | biological_concentration_range | MEASURED MEA; **candidate**; SEM vs SD UNKNOWN |
| Hascup 2008 PFC / Str | 3.3 / 5.0 µM | PMC3404456 / Europe PMC abstract this session; Table 1 HTML timed out | biological_concentration_range | MEASURED point estimates from abstract; **candidate**; ± and n from Table 1 not re-inspected this session |

Fold columns are `pole_M / hi_M` when `hi_M < pole_M`. Occupancy span is `81^(1/n)`.

Not used as bars or occupancy overlays: E006 51.5 pM serum LOD; E004 1.8 nM as occupancy Kd; C027 81-fold as a calibration span; Moussawi review band; Mission 1 backup note of PBS ACV to 2 mM (not a ledger `numerical_result`).
