# Mission 3 RC checkpoint

Phase **D** (clean-checkout rebuild). Not FINAL. Not group-final. Do not merge PR #33. Do not regenerate the review PDF. Astra not invoked.

## Restart identity

| Item | Value |
| --- | --- |
| Phase | D (clean-checkout rebuild) |
| Worker | sole git writer on PR #33 |
| Repository | `bobshenruililin/BIOC1600-1` |
| Branch | `cursor/m3-int-eyefix-245a` |
| Integration PR | [#33](https://github.com/bobshenruililin/BIOC1600-1/pull/33) (draft; do not merge) |
| Science freeze | `3fa11240c85df9ebac58dcc6879494911968f75c` |
| Gate | REVISE |
| Thesis | `D_revised` |
| QUANTITATIVE FLAGSHIP | NONE |
| Highest-information experiment | U2 |
| `group_final` | false |
| Astra this turn | **not invoked** · PRE-COMPOSITION ASTRA: SKIPPED — PACKET INCOMPLETE |

## PDF vision (no new PDF)

| Item | Value |
| --- | --- |
| Review | `docs/mission3-pdf-vision-review.md` (store) |
| Off-repo PDF | `/cursor/stores/bc-036c0435-1c1d-46ee-b329-3ec20161245a/media/BIOC1600_poster_review.pdf` |
| SHA-256 | `18d43961bce4545c38a8a78c265d9dc9251899b249a30827906d9aadd3e02dbf` |
| MUST FIX | **none** |
| New PDF | **no** |

Stylistic leftovers only: clocks C028 caption overflow inherited; faint Panel 0 subtitle; cramped 3Q. **1.8 nM still visible.**

## Clean-checkout rebuild provenance

Detached worktree from `b8b64fa70b23c92adddb8fc0c81e66c26bfeec16`. Deleted `poster/rc/poster_rc.png`, then `bash scripts/build_poster_rc.sh` (rsvg-convert 2.58.0; no network; no PDF). Rebuild matched the committed bytes.

| Artifact | SHA-256 | Notes |
| --- | --- | --- |
| `poster/rc/poster_rc.svg` | `dd487bff52cbbd3a343bfcf0d9fea9181463cfe569c3046cc52b8944038f3eaa` | 72646 bytes; A1 841 × 594 mm; authoritative |
| `poster/rc/poster_rc.png` | `7b0fd5a69df9917a6dd9fcf4411d8ce58b2e0a0f2149532ea34cdc9b65cc0b74` | 2337595 bytes; 4967 × 3508 |

Validators in that tree: `check_structure.py` PASS; `validate_ledgers.py` PASS; `forbid_pdfs.py` PASS; `python3 -m unittest discover -s tests -v` 23 tests OK. `git ls-files '*.pdf'` empty.

## PRE-COMPOSITION ASTRA

`PRE-COMPOSITION ASTRA: SKIPPED — PACKET INCOMPLETE`

Missing (do not invent): verbatim Hu 2025 S002 methods/Experimental paragraph (C021); S002 §3.2 paragraph (C005); S066 Fig. 6.13 caption/pixels; Fig. 6.6 caption/pixels (C028); Fig. 6.8A caption/pixels (C032).

## Next executable action

Keep PR #33 draft. Do not merge. Do not reopen Mission 2. Do not invoke Astra. Do not regenerate the review PDF.
