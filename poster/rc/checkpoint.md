# Mission 3 RC checkpoint

Phase **F** — PI handoff. INTERNAL RELEASE CANDIDATE — NOT FINAL. Not group-final. Do not merge PR #33. Astra not re-invoked.

## Restart identity

| Item | Value |
| --- | --- |
| Phase | F (PI handoff) |
| Worker | coordinator landing after specified-fix + changed-pixel vision |
| Repository | `bobshenruililin/BIOC1600-1` |
| Branch | `cursor/m3-int-eyefix-245a` |
| Integration PR | [#33](https://github.com/bobshenruililin/BIOC1600-1/pull/33) (draft; do not merge) |
| Science freeze | `3fa11240c85df9ebac58dcc6879494911968f75c` |
| Gate | REVISE |
| Thesis | `D_revised` |
| QUANTITATIVE FLAGSHIP | NONE |
| Highest-information experiment | U2 |
| `group_final` | false |
| Astra this turn | **not invoked** · findings addressed by Cursor/Sol |

## Record separately (do not collapse)

| Object | Value |
| --- | --- |
| Astra-audited SHA | `6c2d7f67b0d36f46d686f7f76fd8720267d24f20` |
| Astra-audited PDF | `18d43961bce4545c38a8a78c265d9dc9251899b249a30827906d9aadd3e02dbf` |
| Specified-fix visual git | `854a17a117f78b5a65bdf8f7964f7997d493467f` |
| Specified-fix SVG | `c8e3d19035fbe5f8315e87b8969f154f023187fbcdfa014999e0c6b66b5a1782` |
| Specified-fix PNG (file, this-tree encoding) | `f905ba9378dd0b24d9ad73072682210d9fd13689641d4ac475c0d481043761c9` |
| Specified-fix PNG (decoded pixels) | `4e10acace751c9f71cbca14ad803672121622eabad4e7a4cea267b4024d0d9a1` |
| PDF-hash git record | `44bd1997b54660940e26c31aa3a1527edc014b23` (docs only; visual target unchanged from `854a17a`) |
| Off-repo PDF (not git) | `bbdac14785ef1ab06ed88638695b49bce2e1c515af61418f60aa828051afdd9a` |
| Changed-pixel vision | MUST FIX **none** (`docs/mission3-pdf-vision-changed-pixels.md` in Project store) |

**Astra findings were addressed by Cursor/Sol.** Do not transfer Astra’s verdict onto `854a17a`, `44bd199`, PDF `bbdac147`, or later INT commits.

## CI poster gate

PNG **file** SHA-256 is renderer-local (zlib/filter encoding). After pinning Noto Sans, GitHub Actions still differed by 5 bytes from this VM (`c418d77` rebuilt `f54c81f6…` vs committed `f905ba93…`). CI now hashes **decoded RGB samples** via `scripts/compare_poster_png.py` (geometry 4967×3508). Exact-head green is recorded only after that step runs on GitHub.

## Next executable action

Wait for exact-head `validate` with the pixel-hash rebuild step, then PI visual review of the off-repo A1 PDF. Keep PR draft. Do not merge. Do not reopen Mission 2. Do not invoke Astra.
