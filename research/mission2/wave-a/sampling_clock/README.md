# Interrogation/sampling-timescale mismatch (Mission 2 candidate)

**Status.** Isolated reproduction of PR #24 / `cursor/analysis-nyquist-634f`. **Not** accepted flagship. **Not** under `analysis/accepted/`. Do not call this Nyquist.

**Question.** Can Hu’s parylene-C retina ACV cadence report the **shape** of a 1.2 ms Clements-like literature waveform *even if* occupancy tracked that waveform instantly?

**Answer this package is allowed to give.** No, as a coarse clock-ratio result. Interrogation (14 s/scan, E045) and sampling (~1 min/point, E046) each satisfy T ≫ τ independently. Authors already locate the retina recording at basal glutamate, not synaptic transients (C031). Missing glutamate koff (C007) is not what this figure tests.

Rebuild (Python 3.10+ standard library, no network):

```bash
sh rebuild.sh
```

Outputs: `figures/sampling_clock.svg`, `figures/CAPTION.md`, `tables/clocks.csv`.
