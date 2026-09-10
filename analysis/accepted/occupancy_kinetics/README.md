# Occupancy and diffusion-limited kinetic bound

**Question.** If published glutamate Kd/EC50 values are treated as occupancy parameters, which construct is empty at 25 nM, which is saturated, and which could unbind near 1.2 ms under a diffusion-limited kon **bound**?

**This analysis remains useful if it contradicts the preferred thesis.** A “too slow” slogan fails if the µM isolate’s bound is near 1.2 ms. A “tighter is better” slogan fails if 1.8 nM is saturated at tonic glutamate.

## Rebuild

```bash
python3 -m unittest discover -s tests -v
python3 figures.py
```

Outputs: `figures/occupancy.svg`, `figures/clocks.svg`, `figures/CAPTION.md`.

## Assumptions (must appear in captions)

- kon = 1×10^8 M⁻¹ s⁻¹ is a small-molecule diffusion-limit **upper bound**, not a glutamate measurement.
- Hu 1.8 nM is electrochemical apparent Kd (EC50), not proven molecular Kd.
- Cleft 1.1 mM / 1.2 ms is a kinetic inference (Clements abstract).
- 25 nM is slice ambient glutamate (Herman).

## Not in this analysis

- Tobramycin IPA rates (not transferred)
- Docking
- InstructNA training
- Filling empty glutamate kon/koff cells
