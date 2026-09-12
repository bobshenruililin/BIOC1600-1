# Mission 2 Wave B — working-range bars (analysis candidate)

**Not accepted. Not `analysis/accepted/`. Not a GitHub PR. Not Mission 1 close.**

Isolated rebuild of closed-unmerged PR #23 (`cursor/analysis-working-range-634f` @ `924f794f5c2258d80394e34681248f470ceaabbc`) from public ledger rows plus OA. Adds the two robustness tests PR #23 did not run: (a) basal-pole choice, C012 only vs candidate Hershey/Hascup; (b) Langmuir–Freundlich *n* via `81^(1/n)`.

**Question.** After occupancy-at-basal is withdrawn, do reported `analytical_working_range` bars versus *named* glutamate poles still mismatch — and does that mismatch survive changing the left-hand pole or the unpublished LF exponent?

## Rebuild

Python 3 standard library only. No network. No pip.

```bash
sh research/mission2/wave-b/working_range/rebuild.sh
```

From this directory:

```bash
python3 -m unittest discover -s tests -v
python3 figures.py
```

Outputs: `figures/working_range.svg`, `figures/lf_n_span.svg`, `figures/CAPTION.md`, `tables/range_table.csv`, `tables/basal_pole_sensitivity.csv`, `tables/lf_n_span.csv`, `tables/n_star_named_ratios.csv`.

## Canonical bars vs C012 / C011 (SI-strict)

| row | span | field | vs C012 25 nM (INFERRED) | vs C011 1.1 mM (INFERRED) |
| --- | --- | --- | --- | --- |
| Abrantes NG-Apt-Glu FET, aCSF (preprint) | 1 aM–10 pM | E041 | ceiling 2500-fold below | misses |
| glu1 E-AB (abstract) | 0.01 pM–1 nM | E003 | ceiling 25-fold below | misses |
| Xiao CNT FET, 0.1× PBS | 10 fM–100 nM | E026 | contains | ceiling **11000-fold** below |
| Hu AuED-MEA, PBS | 0.1 nM–10 µM | E007 | contains | ceiling 110-fold below |
| Hu PaC probe, PBS | 1 nM–1 mM | E044 **comparator** | contains | ceiling **1.1-fold** below |
| Hu PaC probe, Ames | 10 nM–10 µM | E044 `numerical_result` | contains | ceiling 110-fold below |

Folds are `pole / ceiling` when the ceiling is below the pole. MODELED, not measurements. C012 and C011 are **separate named examples**. They are not spliced into one device specification.

Proposal-table “Xiao ceiling 11-fold below 1.1 mM” is **not used** (nM/µM mix). “PBS contains 1.1 mM” is **not used** on SI-strict containment.

## Robustness (a) basal-pole choice

Canonical left tick remains C012 only. Candidate Hershey/Hascup poles are package-local, tagged `candidate`, not written to `claims.csv`.

Ames 10 nM–10 µM **contains** C012 25 nM, Hershey 144 nM dialysate, Hascup 2008 3.3 / 5.0 µM, and Hershey Capp 9.4 µM, and **misses** Hascup 2010 34.7 µM (3.47-fold below). So “Ames covers basal” is **not invariant** to method class. No bar contains C011 1.1 mM under any of these left poles. Do not average unlike method classes.

## Robustness (b) Langmuir–Freundlich *n*

Occupancy 10–90% width = `81^(1/n)` for θ = c^n/(Kd^n + c^n) with Kd as c50. n=1 → 81; n=0.5 → 6561; n=2 → 9. Hu fitted **n is UNKNOWN**. 1.8 nM is C005 electrochemical **EC50**, not occupancy Kd. Device-bar endpoints do not move with *n*. Measuring *n* does **not** restore 81-versus-44000 as flagship and does not make Herman+Clements a device spec.

E035 1.8 µM tick is **INFERRED** (NMDA 37.7 µM MEASURED × 0.048). Herman 25 nM remains **INFERRED**.

## C vs revised D

This figure does **not** force a title swap. Candidate C’s ceiling-from-above punch is true on Wu/Abrantes vs C012. Revised D remains the stronger title for the retina experiment **if** the left pole is C012: Ames contains 25 nM and sits 110-fold below 1.1 mM. Swap C over D only if the question is the field’s ultrasensitive-calibration contest. If the left pole is Hascup 2010 34.7 µM, Ames no longer “contains basal” — that is a method-class change, not a new aptamer measurement.

## Falsifier

1. A same-construct Ames or tissue calibration whose working range contains both a **locked, quantity-class-matched** basal and 1.1 mM — or a locked decision that Clements 1.1 mM is the wrong right-hand pole for a retina electrode.
2. Publication of Hu’s LF *n* (with uncertainty) on an occupancy isotherm of the exact oligo. That would set the occupancy-window width. It would still not license Herman+Clements as one spec.
3. A chemical [Glu] at the Hu GCL electrode. None of the basal poles here is that number.
