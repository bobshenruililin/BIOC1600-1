# QA report

INTERNAL RELEASE CANDIDATE — NOT FINAL. Gate **REVISE**. Flagship **NONE**. Astra skipped.

## Status: REVISE

`poster/rc/poster_rc.png` rebuilt at 4967×3508 via `scripts/build_poster_rc.sh`. Off-repo PDF crops may still be pending inspection. QA stays **REVISE** until those crops are inspected. SVG remains authoritative.

## Composition checks (this write)

| Check | Result |
| --- | --- |
| A1 841 × 594 mm SVG | `width="841mm" height="594mm"` `viewBox="0 0 841 594"` |
| Visible label | INTERNAL RELEASE CANDIDATE — NOT FINAL |
| Nested faces 0–9 | b0, eyefix, maps, spikes, clocks-calfix, 3Q, 3H, why-layers-fidfix, C032, U2 |
| Isolated mouse retina | on hero face |
| eye-cup | absent |
| 1.8 nM | visible on hero parked chip and 3Q card 1 |
| 12 µM | visible on 3Q card 4 |
| clocks face | `b2-clocks-calfix.svg` with C028 10 min plateau / 10 nM Glu step; not `protocol_clocks.svg` as the clocks face |
| C032 Asp/Gln/GABA | UNKNOWN empty cells, not MEASURED |
| U1 | red-X different question / not next |
| Fig. 6.13 data pixels | not drawn |
| Filename `final` | none |
| PDF in git | none (review PDF is off-repo only) |

## Forbidden-as-finding scan

Visible “not Thesis E” on the spikes face is a refusal copied from the exported card, not Thesis E as a finding. Source XML comments mention Nyquist / recognition-first / protocol_clocks as **not** those objects; they are not masthead findings.

## Off-repo review PDF

Path: `/cursor/stores/bc-036c0435-1c1d-46ee-b329-3ec20161245a/media/BIOC1600_poster_review.pdf`

Hash and page-size verification are filled after first complete SVG render. Do not git-add that PDF or its PNG crops.
