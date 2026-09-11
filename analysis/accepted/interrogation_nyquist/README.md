# A4 interrogation Nyquist (isolated analysis)

**Question.** Can Hu’s parylene-C retina ACV cadence report the **shape** of a 1.2 ms Clements-like literature stimulus *even if* occupancy tracked that stimulus instantly?

**Answer this figure is allowed to give.** No. Interrogation (14 s/scan, E045) and sampling (~1 min/point, E046) both sit far above a Nyquist-style τ/2 sketch. Authors already refuse synaptic transients (C031). Missing glutamate koff (C007) is not what this figure tests.

**Not Mission 1 close.** This package implements proposed analysis A4 only. It does not rewrite the science-story gate, scoreboard, theses, or nightly summary.

## Rebuild

From this directory:

```bash
sh rebuild.sh
```

One-command from `analysis/accepted/`:

```bash
sh rebuild.sh
```

Requires Python 3.10+ standard library only (`requirements.txt`). No network.

Outputs: `figures/nyquist.svg`, `figures/CAPTION.md`, `tables/clocks.csv`.

## Quantity types (kept separate)

| glyph | object | ledger | on figure |
| --- | --- | --- | --- |
| teal curve | literature stimulus / biological τ | E032, E033, E034 / C011, C012 | yes |
| orange | interrogation (ACV scan) | E045 / C031 | yes |
| purple | sampling interval | E046 / C031 | yes |
| — | journal 15 min Glu wait | E008 / C006 | no (caption/table) |
| — | thesis 10 min 10 nM plateau | E042 / C028 | no (caption/table) |
| — | IPA 2 ms; GlutOx 500–800 ms | C009; C022 | no (other-class footnote) |

Clock ratios 14 s / 1.2 ms and 60 s / 1.2 ms are dimensionless T/τ, **not** koff.

## Highest-information next experiment *from this figure*

A glutamate-aptamer recording whose **interrogation and sampling** are sub-millisecond to few-millisecond on a known millisecond [Glu](t) pulse (IPA-class cadence on the same oligo), **or** a locked decision that the biological spec is basal/graded photoreceptor glutamate rather than a 1.2 ms hippocampal cleft waveform.

A glutamate `kon`/`koff` on 14 s ACV, and another PBS LOD, cannot reopen cleft-waveform reporting on **this** architecture.

## Falsifier

A glutamate-aptamer recording whose sampling interval is sub-millisecond to few-millisecond **and** whose authors claim synaptic transients.

See `limitations.md` and `provenance.md`.
