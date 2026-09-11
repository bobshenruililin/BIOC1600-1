# Quantity ontology (Mission 1 O1/O2)

Closed ledger vocabulary (`scripts/validate_ledgers.py` QUANTITY_TYPES):
`Kd_molecular`, `kon`, `koff`, `EC50`, `sensor_LOD`, `analytical_working_range`, `signal_gain`, `response_time`, `measurement_time`, `biological_concentration_range`.

Live claims/evidence **notes** usually split objects. The ten-type schema and selected occupancy/sensitivity glyphs still collapse some of them.

## Objects that must not be treated as one number

| Object | What it is | Ledger example | Common collapse |
|---|---|---|---|
| molecular Kd | 1:1 oligo–ligand Kd in a named phase | 1d04 12 µM (C001); Xiao SPR 293 nM (C014) | Hu cited 12 µM typed `Kd_molecular` (C021) |
| cited Kd | literature label, not a remeasurement | Hu methods 12 µM Wu citation (C021) | Same type as 1d04 measurement |
| apparent / electrochemical Kd | half-maximal transduced signal; may be LF | Hu 1.8 nM (C005, stored as `EC50`) | 1:1 occupancy Kd |
| receptor EC50 | NMDAR dose–response | Herman 1.8 **µM** (E035) | Hu 1.8 **nM** (E004); same digits |
| sensor LOD | blank + 3SD or 3RSD of a signal | 32 pM 3SD PBS vs 0.3 pM 3RSD PBS | One improvement axis |
| working range | calibration span | Hu PBS 0.1 nM–10 µM; Ames 10 nM–10 µM | 81-fold occupancy identity (C013/C027) |
| incubation | wait after adding analyte | Hu 15 min (C006); thesis 10 min (C028) | `measurement_time` with IPA 2 ms |
| interrogation | duration of the electrical query | IPA 2 ms (C009); ACV 14 s (E045) | koff |
| sampling interval | time between quantitative points | retina ~1 min (C031/E046) | 14 s scan clock |
| biological τ | inferred free-Glu lifetime | Clements 1.2 ms (E033 stored as `response_time`) | sensor t90 |
| ambient [Glu] | baseline extracellular | Herman ~25 nM (C012) | extrasynaptic-only; cleft peak |
| peak [Glu] | inferred cleft peak | Clements 1.1 mM (C011) | packed with τ in C011 claim text |
| kon / koff | binding rates of a named oligo | **none for glutamate** (C007) | tobramycin IPA / Ding ITC (C008/C010) |
| τ_eq | 1/(kon c + koff) | occupancy table SIMULATION | t_off; 1/τ_cleft |
| t_off | 1/koff | BOUND from assumed kon × advertised Kd | measured glutamate koff |

## Glyphs that still perform collapses (O2)

- `occupancy.svg`: 1:1 Langmuir θ and 81-fold overlay on Hu LF 1.8 nM; tests assert θ(25 nM)>0.9.
- `clocks.svg`: biological τ, bound koff, protocol wait, enzyme t90, FET stabilize on one axis.
- Atlas thesis LOD cell `0.3 pM` unlabeled PBS (not Ames).
- Stale: `rounds/01/merge_sources.py` S050 notes still say tonic extrasynaptic.

Captions, empty glutamate kon/koff cells, C003/C005/C007/C009/C012/C021/C025 are already careful.

Occupancy table: SIMULATION/BOUND only.
