# Canonical figure copies

These files are produced by `sh analysis/accepted/rebuild.sh`. Do not edit them by hand.

**Handoff selection (best 3):** `atlas.svg`, `occupancy.svg`, `sensitivity.svg`.

| file | selected | source package | kind |
| --- | --- | --- | --- |
| `atlas.svg` | yes | `analysis/accepted/atlas/` | ledger plot; empty cells stay empty |
| `occupancy.svg` | yes | `analysis/accepted/occupancy_kinetics/` | SIMULATION Langmuir occupancy |
| `sensitivity.svg` | yes | `analysis/accepted/occupancy_kinetics/` | t_off vs kon; empirical band is NOT glutamate |
| `clocks.svg` | supporting | `analysis/accepted/occupancy_kinetics/` | BOUND vs MEASURED vs INFERENCE clocks |
| `nyquist.svg` | A4 draft | `analysis/accepted/interrogation_nyquist/` | literature stimulus vs 14 s interrogation / 1 min sampling; not koff |

Captions: `atlas.CAPTION.md`, `occupancy.CAPTION.md`, `nyquist.CAPTION.md`.
Tables: `analysis/accepted/occupancy_kinetics/tables/occupancy_table.csv`, `analysis/accepted/interrogation_nyquist/tables/clocks.csv`.

`nyquist.svg` is not Mission 1 close. It does not replace the occupancy/atlas flagship. It replaces the *use* of omnibus `clocks.svg` for the cleft-column interrogation question.
