# BIOC1600-1

Verified-evidence workspace for HKU BIOC1600 Topic 1 (glutamate aptamer biosensors). **Not a finished poster.**

**Start here:** [`reports/mission3_entry.md`](reports/mission3_entry.md)

## Current thesis (one sentence)

Hu’s Ø 25 µm Fc-thiol 39-mer MEASURES ACV signal-gain referenced to a post-insertion baseline on two tissue legs with unequal IVs—post-insertion rise (time; light on) and later on–off–on (illumination)—both INFERRED as glutamate. Printed spiked-buffer `%gain` maps cannot invert tissue ACV; identity stays UNKNOWN until named U2. Rapid-transient readiness remains unmeasured.

Gate **REVISE**. QUANTITATIVE FLAGSHIP **NONE** as occupancy/Kd/LOD/tissue-[Glu] title. Selected picture: measured protocol clocks. `group_final` false. READY FOR MISSION 3: **NO** until a later readiness pair and a human row in `state/decisions.md`.

## Canonical vs historical

| Canonical now | Historical — do not treat as current |
| --- | --- |
| `state/current_thesis.md` | overnight T1/T5 in `poster/theses.md` |
| `poster/storyboards/mission3.md` (Mission-3-facing) | `poster/storyboards/winner.md` |
| `poster/storyboards/revised_D.md` (Mission-2 test-locked) | `rounds/03/`, `analysis/candidates/theses/` |
| `state/high_value_unknowns.md` | Wave C/D score politics in nightly §1 footnotes |

## Reproduce

```bash
python3 scripts/check_structure.py
python3 scripts/validate_ledgers.py
python3 scripts/forbid_pdfs.py
python3 -m unittest discover -s tests -v
sh analysis/accepted/rebuild.sh
```

Operating manual: [`AGENTS.md`](AGENTS.md). PI nightly (score-heavy): [`reports/nightly_summary.md`](reports/nightly_summary.md).

## Mission 3 may / must not

**May:** the freeze sentence; supporting figures `span_identity.svg`, `two_regime_clocks.svg`, `atlas.svg`; U2 as the next experiment if the claim is identity.

**Must not:** invert tissue ACV from printed `%gain`; fill C007 from other ligands; call either tissue leg MEASURED glutamate; restore occupancy-at-basal, 81-vs-44000, Nyquist, dual-pole bars, or scale-map as title; polish final poster artwork; set `group_final` without a human decision.
