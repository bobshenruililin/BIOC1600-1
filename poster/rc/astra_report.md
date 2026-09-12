---
cursor:
  subagentId: "bc-eb853b44-ddee-5704-9900-c0ef163874ff"
---

# Mission 3 cold Astra audit

Audited commit: `6c2d7f67b0d36f46d686f7f76fd8720267d24f20`  
Poster render SHA-256: `18d43961bce4545c38a8a78c265d9dc9251899b249a30827906d9aadd3e02dbf`  
Inspected: PDF-derived `poster_review_page.png` and crops `crop_masthead` through `crop_09_u2` (not SVG). Talks/provenance/checkpoint/copy/captions/QA/Astra-skip record at that SHA only. Prior pixel vision opened last.

Frozen state (unchanged by this audit): `D_revised`; science gate `REVISE`; Mission 2 `FREEZE`; quantitative flagship `NONE`; next experiment `U2`; `group_final=false`. Do not merge.

## Initial visual interpretation (before freeze/talks)

**Measured.** ACV current as `%gain` vs post-insertion baseline on a Ø 25 µm Fc-thiol 39-mer PaC shank in vitro isolated mouse retina. Two protocols: Leg A = time after insertion with room light held ON; Leg B = later room-light ON/OFF/ON (not 500 ms LED). Printed PBS/Ames `%gain` maps (11.86 and 57.11 %/decade). Placement (large ACV disk vs small ephys). Protocol clocks. Four buffer interferents (serotonin, dopamine, tyrosine, lactate).

**Glutamate / identity.** Authors’ Glu reading is stamped INFERRED. Tissue chemical ID is UNKNOWN / unnamed. The board refuses “not glutamate” and “sensor failed.” Maps cannot invert tissue ACV. Spikes do not name the faradaic current. Parked 1.8 nM is another device’s PBS EC50, not this probe’s Kd.

**Next.** Panel 9: proposed U2 on both legs (working 39-mer / scrambled / pharmacology). Empty cells. Not U1. Gate REVISE.

## Decision

**ADVANCE AFTER SPECIFIED FIXES**

**Strongest reason.** PDF pixels, talks, and freeze chips keep ACV `%gain` MEASURED and tissue Glu INFERRED/UNKNOWN, with U2 proposed and flagship NONE on-face. One on-board phrase plus the 90 s gist treat the two unequal-IV legs as one shared unnamed species. That is a freeze-internal wording defect, not a science-gate contradiction.

Science fatals: **none.**

## Locator INCOMPLETE (audit limitation, not a fatal)

Original Hu excerpts were not in the candidate packet; none were invented.

| Locator | Needed for | Status |
| --- | --- | --- |
| S002 methods/Experimental paragraph | C021 12 µM citation | INCOMPLETE |
| S002 §3.2 paragraph | C005 1.8 nM | INCOMPLETE |
| S066 Fig. 6.13 caption/pixels | Leg A/B tissue ACV | INCOMPLETE |
| S066 Fig. 6.6 caption/pixels | C028 10 min / 10 nM step | INCOMPLETE |
| S066 Fig. 6.8A caption/pixels | C032 four interferents | INCOMPLETE |

Qualifications on the poster match freeze ledgers quoted in the skip record; they were not re-checked against original Hu text or figure pixels.

## MUST FIX (1)

**Shared-identity wording on two unequal IVs**

- **Where.** Hero: “different IVs same unnamed analyte”; “Two different experiments — same unnamed analyte.” 90 s gist: “They measured a current twice … did not name the molecule.” 3 min: “Two currents. The molecule is unnamed.”
- **Wrong inference.** One unnamed chemical species is shared across Leg A (time, light held ON) and Leg B (illumination). Freeze: identity UNKNOWN on each leg; U2 tests both because shared identity is untested. Not an identification of Glu, and not a claim that the signal is not Glu.
- **Smallest repair.** Hero/copy: “analyte unnamed on each leg (shared identity untested).” 90 s: “two currents, unlike conditions; neither named.” 3 min: “Two currents. Neither molecule is named.” Keep MEASURED/INFERRED/UNKNOWN stamps.
- **Acceptance test.** A reader pointing at the two white wells cannot quote a sentence that the two legs are the same species. U2’s 2×3 empty grid still treats legs separately.

## U2

**Coherent as proposed.** Panel 9 and talks lock pharmacology + scrambled/binding-null on both legs, same shank and room-light protocol, including Leg A. Empty = not in hand. Survive both legs falsifies a Glu-occupancy reading; die on both strengthens the inference and still is not inverted tissue [Glu]. U1 / C007 / late rebin refused. Does not claim definitive chemical ID.

## Flagship NONE

**Defensible.** Masthead and footers print Flagship NONE / Gate REVISE / not group-final. Maps: no flagship plot, no θ from `%gain`. 3Q parks 1.8 nM, 0.3 pM, 25 nM, 12 µM as wrong objects. Measured buffer slopes, clocks, placement, and four interferents remain as positive findings, not a title conversion to occupancy or tissue [Glu].

## Optional (2)

1. Clocks-calfix C028 collision (`crop_04_clocks.png`: “pltateau”; `~1 min` not independently readable). 10 min / buffer calibration / 10 nM Glu step still present; talks state C028 correctly. Widen the caption; do not regenerate science.
2. Panel 0 subtitle is faint; the locked question is readable. Darken subtitle or drop it.

## Release vs this render

Checkpoint, QA, and `BIOC1600_poster_review.json` pin this PDF hash. SVG `dd487bff…838e3eaa` / PNG `7b0fd5a6…65cc0b74` match the bundle. Talks point at `poster/rc/poster_rc.svg`. Astra standing record: SKIPPED — PACKET INCOMPLETE; not invoked. INTERNAL RELEASE CANDIDATE — NOT FINAL on masthead. Prior vision (`MUST FIX none` on this hash) is historical, not a vote.

## Unchecked limitations

No original S002/S066 captions or figure pixels. No git hash of the off-repo PDF bytes in this audit (JSON/checkpoint asserted). No rebuild. No merge. Poster freeze forbids a polished final.
