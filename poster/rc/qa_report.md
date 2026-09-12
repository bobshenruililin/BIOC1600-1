# QA report

INTERNAL RELEASE CANDIDATE — NOT FINAL. Gate **REVISE**. Flagship **NONE**. Astra skipped. SVG remains authoritative.

## Pixel / PDF vision

Inspected rasters were from the A1 PDF, not from the SVG.

| Item | Value |
| --- | --- |
| Prior vision (audited PDF) | `/cursor/stores/bc-036c0435-1c1d-46ee-b329-3ec20161245a/docs/mission3-pdf-vision-review.md` |
| Prior PDF SHA-256 | `18d43961bce4545c38a8a78c265d9dc9251899b249a30827906d9aadd3e02dbf` |
| Prior MUST FIX | **none** |
| Changed-pixel vision | `/cursor/stores/bc-036c0435-1c1d-46ee-b329-3ec20161245a/docs/mission3-pdf-vision-changed-pixels.md` |
| Current PDF (off-repo) | `/cursor/stores/bc-036c0435-1c1d-46ee-b329-3ec20161245a/media/BIOC1600_poster_review.pdf` |
| Current PDF SHA-256 | `bbdac14785ef1ab06ed88638695b49bce2e1c515af61418f60aa828051afdd9a` |
| Current MUST FIX | **none** |
| New PDF after changed-pixel review | **no** |

Science gate stays **REVISE**. Pixel vision does not manufacture PASS or group-final. Do not transfer Astra’s verdict from PDF `18d43961` onto PDF `bbdac147`.

## CI checksum (preview PNG)

`9aabb85` proved the 5-byte file delta was a **real raster difference** (committed pixels `4e10acac…` vs Actions `9efb2e26…`). Preview PNG was re-rasterized with `scripts/poster_fontconfig.conf`. Current file SHA-256 `09f4ecc2d447222515676f78676a67715e9c3a538b09221046adee2184f51935`; decoded RGB `fa920782242d492b6f22b31c5f1c6a6870f556b7c60c2ce7ee7e2f3fd5167d94` at 4967×3508. SVG and off-repo PDF are unchanged. Do not transfer Astra’s verdict onto this PNG.

## Stylistic leftovers (not MUST FIX)

- Clocks-calfix C028 caption overflow inherited from the exported 420-px face; ~1 min not independently readable in `crop_04_clocks.png`
- Faint Panel 0 subtitle
- Cramped 3Q strip; **1.8 nM** and **12 µM** still visible

## Composition checks

| Check | Result |
| --- | --- |
| A1 841 × 594 mm SVG | `width="841mm" height="594mm"` `viewBox="0 0 841 594"` |
| Visible label | INTERNAL RELEASE CANDIDATE — NOT FINAL |
| Nested faces 0–9 | b0, eyefix, maps, spikes, clocks-calfix, 3Q, 3H, why-layers-fidfix, C032, U2 |
| Isolated mouse retina | on hero face |
| eye-cup | absent |
| 1.8 nM | visible on hero parked chip and 3Q card 1 |
| 12 µM | visible on 3Q card 4 |
| clocks face | `b2-clocks-calfix.svg` with C028 10 min plateau / 10 nM Glu step; not `protocol_clocks.svg` |
| C032 Asp/Gln/GABA | UNKNOWN empty cells, not MEASURED |
| U1 | red-X different question / not next |
| Fig. 6.13 data pixels | not drawn |
| Filename `final` | none |
| PDF in git | none |

## Forbidden-as-finding scan

Visible “not Thesis E” on the spikes face is a refusal copied from the exported card, not Thesis E as a finding. Source XML comments mention Nyquist / recognition-first / protocol_clocks as **not** those objects; they are not masthead findings.

Do not git-add the off-repo PDF or its PNG crops.
