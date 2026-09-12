---
cursor:
  subagentId: "bc-1f60a187-c646-584f-9fe4-96c66e30d190"
---

# B2 2C clocks calfix (I2 string only)

Base (read, not edited): `internal/mission3/prototypes/b2-clocks.svg` (SURVIVE parent; do not overwrite).
Output: `internal/mission3/prototypes/b2-clocks-calfix.svg` (this note's companion). Freeze: `main` @ `3fa11240c85df9ebac58dcc6879494911968f75c`. Communication only. Mission 2 not reopened. No numbers invented. No PR. No Astra.

Opus I2: parent prints three equal-weight tokens `14 s scan · ~1 min/point · 10 min plateau`. E045/E046 are tissue. C028 is probe calibration after a 10 nM Glu step (Fig. 6.6), not a tissue clock.

## Delta (10 min token only)

| # | Location | parent | calfix |
|---|---|---|---|
| 1 | Third token `<text>` (14 bold, same x/y as parent) | `10 min plateau` | `10 min plateau (buffer calibration, 10 nM Glu step)` |
| 2 | `aria-label` (same token, scored face) | `10 min plateau` | `10 min plateau (buffer calibration, 10 nM Glu step)` |

Sibling identity only: header comment `clocks.` → `clocks calfix. Copy of b2-clocks.svg. Parent not overwritten.` No geometry, bars, clocks, or type-weight change.

## Kept (verbatim from parent)

- Tabs `NOT LEG A` · `NOT LEG B` · `2C`
- Title `Clocks of the scan, not a Glu assay`
- Stamp `MEASURED: protocol times · not a current ID`
- Caption `MEASURED clocks · not Leg A · not Leg B · identity still UNKNOWN`
- Tokens 1–2: `14 s scan` · `~1 min/point` (14 bold; equal type weight with token 3)
- UNKNOWN / UNMEASURED wells; ID rail `C031 · E045 · E046 · C028 · C007`
- No bar lengths. No new clocks. No 1.2 ms. Not `protocol_clocks.svg`. No untraced Hz.

## Forbidden (none violated)

- Parent `b2-clocks.svg` not overwritten.
- No 1.2 ms / Nyquist / Clements / Hz / duration bars / extra clocks.
