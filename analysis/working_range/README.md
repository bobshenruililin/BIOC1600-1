# A3 — working-range bars versus biological poles

**Not Mission 1 close. Not group-final. Not copied into `analysis/accepted/`.**

Isolated implementation of analysis **A3** from Goal Wave A (`rounds/goal-wave-a/analysis-proposals.md`, PR #11). Occupancy-at-basal is not used. Docking is not used.

**Question.** After occupancy-at-basal is withdrawn, does the remaining ledger mismatch live in **calibration windows** (`analytical_working_range`) versus literature glutamate poles (`biological_concentration_range`), rather than in occupancy θ?

## Rebuild

Python 3 standard library only. No network. No pip.

```bash
sh analysis/working_range/rebuild.sh
```

From this directory:

```bash
python3 -m unittest discover -s tests -v
python3 figures.py
```

Outputs: `figures/working_range.svg`, `figures/CAPTION.md`, `tables/range_table.csv`.

## What is plotted

| row | span | field | vs Herman 25 nM (E034) | vs Clements 1.1 mM (E032) |
| --- | --- | --- | --- | --- |
| Abrantes NG-Apt-Glu FET, aCSF (preprint) | 1 aM–10 pM | E041 `numerical_result` | ceiling 2500-fold below | misses |
| glu1 E-AB (abstract) | 0.01 pM–1 nM | E003 `numerical_result` | ceiling 25-fold below | misses |
| Xiao CNT FET, 0.1× PBS | 10 fM–100 nM | E026 `numerical_result` | contains | ceiling **11000-fold** below |
| Hu AuED-MEA, PBS | 0.1 nM–10 µM | E007 `numerical_result` | contains | ceiling 110-fold below |
| Hu PaC probe, PBS | 1 nM–1 mM | E044 **comparator** | contains | ceiling **1.1-fold** below (SI-strict: 1 mM < 1.1 mM) |
| Hu PaC probe, Ames | 10 nM–10 µM | E044 `numerical_result` | contains | ceiling 110-fold below |

Folds are `pole / ceiling` when the ceiling is below the pole. They are computational illustration, not measurements.

Proposal table “Xiao ceiling 11-fold below 1.1 mM” is **not used**: 1.1 mM / 100 nM = 11000. That was a unit mix (nM vs µM). Proposal “PBS contains 1.1 mM” is **not used** on SI-strict containment.

## LOD dots

Unconnected `sensor_LOD` dots, same construct/matrix only. Ames LOD cell is empty (E043 0.3 pM is PBS, not Ames/tissue). Serum 51.5 pM (E006) is not plotted: no serum working-range row.

## C vs revised D (this figure does not close Mission 1)

A3 **does not force a title swap**. It makes both panels true on different rows:

- **Candidate C (supporting panel):** glu1 and Abrantes miss Herman 25 nM **from above**. That is occupancy-free ledger arithmetic.
- **Revised D (still the stronger title for the retina experiment):** the tissue-bathing Ames bar **contains 25 nM** and is 110-fold below 1.1 mM. No plotted bar contains both poles on SI-strict reading, including PBS 1 nM–1 mM.

Swap C over D only if the poster question is the field's ultrasensitive-calibration contest rather than the Hu retina device. That is a framing choice, not a numerical necessity. A3 is not a Mission 1 gate result.

## What would falsify the figure

1. A glutamate-aptamer calibration **in Ames or tissue on the same construct** whose `analytical_working_range` contains both a locked basal number and 1.1 mM.
2. A locked decision that Clements 1.1 mM is the wrong right-hand pole for a retina electrode (framing change, not a new span).
3. Full-text correction of Wu/Abrantes spans so those ceilings contain 25 nM (kills C's ceiling-from-above rows only).
4. A dedicated PaC PBS `analytical_working_range` numerical_result that differs from the E044 comparator string (the PBS bar would be omitted or replaced; it is not invented).

A new Kd/EC50 does not put 1.1 mM inside Ames 10 µM.
