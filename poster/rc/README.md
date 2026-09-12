# Mission 3 internal release candidate (eyefix-package)

**INTERNAL RELEASE CANDIDATE — NOT FINAL.** Not group-final. Do not merge PR #33.

| Lock | Value |
| --- | --- |
| Science freeze | `origin/main` @ `3fa11240c85df9ebac58dcc6879494911968f75c` |
| Thesis | `D_revised` |
| Gate | **REVISE** |
| QUANTITATIVE FLAGSHIP | **NONE** |
| Highest-information experiment | **U2** |
| `group_final` | false |
| Pre-composition Astra | **SKIPPED — PACKET INCOMPLETE** |

Canonical poster: `poster/rc/poster_rc.svg` (A1 landscape 841 × 594 mm). Preview: `poster/rc/poster_rc.png`. SVG is authoritative.

## Rebuild PNG (no PDF, no network)

```bash
bash scripts/build_poster_rc.sh
```

Fails nonzero if the SVG or renderer (`rsvg-convert` or `inkscape`) is missing. Does not silently reuse a committed PNG. Does not write PDF.

## Reading order (nested exported faces)

0. `sources/b0-question.svg` — question, not a finding
1. `sources/hybrid-hero-v3-eyefix.svg` — dominant finding (in vitro isolated mouse retina)
2. `sources/b2-maps.svg` — buffer ≠ tissue
3. `sources/b2-spikes.svg` — physiology, not ID
4. `sources/b2-clocks-calfix.svg` — 14 s / ~1 min / 10 min C028 buffer calibration
5. `sources/b3-3q-traps.svg` — four traps including 12 µM and 1.8 nM
6. `sources/b3-3h-regimes.svg` — two hippocampal examples, not a retinal spec
7. `sources/b3-why-layers-fidfix.svg` — three objects differ
8. `sources/b3-c032-selectivity.svg` — four interferents run; Asp/Gln/GABA UNKNOWN
9. `sources/u2-close.svg` — PROPOSED naming test

Chain: **MEASURED ACV signal-gain → INFERRED glutamate → UNKNOWN identity → PROPOSED U2**

## Package files

`copy.md`, `captions.md`, `talk_90s.md`, `talk_3min.md`, `oral_defense.md`, `provenance.csv`, `decision_record.md`, `review_index.md`, `qa_report.md`, `manifest.json`, `checkpoint.md`, `astra_design_contract_report.md`, `astra_design_contract_disposition.md`, `astra_report.md`, `astra_disposition.md`, `astra_bundle/index.md`, `sources/`.

No filename contains `final`. No PDF in this repository.
