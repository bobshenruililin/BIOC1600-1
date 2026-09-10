# Occupancy, diffusion-limited bound, and empirical-kon sensitivity

**Question.** If published glutamate Kd/EC50 values are treated as occupancy parameters, which construct is empty at 25 nM, which is saturated, and how does t_off move when kon is a diffusion ceiling versus the small-molecule aptamer kon values already in the ledger?

**This analysis remains useful if it contradicts the preferred thesis.** T5’s “12 µM is near 1.2 ms” fails inside the C008/C010 kon envelope. T1’s “too slow” slogan still fails as a measured koff (C007 is an absence). Occupancy at 25 nM is independent of kon.

## Rebuild

```bash
python3 -m unittest discover -s tests -v
python3 figures.py
```

Outputs: `figures/occupancy.svg`, `figures/clocks.svg`, `figures/sensitivity.svg`, `figures/CAPTION.md`, `tables/occupancy_table.csv`.

## Assumptions (must appear in captions)

- kon = 1×10^8 M⁻¹ s⁻¹ is a small-molecule diffusion-limit **upper bound**, not a glutamate measurement.
- 96–2×10^5 M⁻¹ s⁻¹ (C010) and 3.5×10^4 M⁻¹ s⁻¹ (C008) are **not glutamate**.
- Hu 1.8 nM is electrochemical apparent Kd (EC50), not proven molecular Kd.
- Cleft 1.1 mM / 1.2 ms is a kinetic inference (Clements abstract).
- 25 nM is slice ambient glutamate (Herman).

## Not in this analysis

- Transferring tobramycin or ITC rates onto glutamate
- Docking
- InstructNA training
- Filling empty glutamate kon/koff cells
