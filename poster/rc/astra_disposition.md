# Astra disposition (specified-fix)

INTERNAL RELEASE CANDIDATE — NOT FINAL. Gate **REVISE**. Flagship **NONE**. `group_final` false. Do not merge PR #33.

**Astra findings were addressed by Cursor/Sol.** Do not transfer Astra’s verdict onto any commit it did not inspect.

## Audited object (not this repair)

| Item | Value |
| --- | --- |
| Verdict (verbatim) | `poster/rc/astra_report.md` = store `mission3-cold-astra-audit.md` |
| Decision | ADVANCE AFTER SPECIFIED FIXES |
| Science fatals | none |
| Audited commit | `6c2d7f67b0d36f46d686f7f76fd8720267d24f20` |
| Audited PDF SHA-256 | `18d43961bce4545c38a8a78c265d9dc9251899b249a30827906d9aadd3e02dbf` |

The post-repair commit is **not** the Astra-audited SHA.

## MUST FIX applied (shared-identity wording)

Between-cards glyph: `different IVs` kept; `same unnamed` → `unnamed each`; `analyte` → `leg (untested)`.

Hero footer: `Analyte unnamed on each leg (shared identity untested).`

Source `aria-label` no longer says “same unnamed analyte”.

Copy, hero companion note, 90 s gist, 3 min opening sentence: same repair. MEASURED / INFERRED / UNKNOWN stamps kept. U2 2×3 grid still per-leg.

**Acceptance test.** A reader pointing at the two white wells cannot quote a sentence that the two legs are the same species.

## Optional leftovers — not applied

Clocks-calfix C028 collision / Panel 0 subtitle restyle: **not changed**.

## Rebuild (post-repair)

| Artifact | SHA-256 |
| --- | --- |
| `poster/rc/poster_rc.svg` | `c8e3d19035fbe5f8315e87b8969f154f023187fbcdfa014999e0c6b66b5a1782` |
| `poster/rc/poster_rc.png` | `f905ba9378dd0b24d9ad73072682210d9fd13689641d4ac475c0d481043761c9` |

PNG regenerated with `bash scripts/build_poster_rc.sh` (4967 × 3508). No PDF in git. Astra not re-invoked.
