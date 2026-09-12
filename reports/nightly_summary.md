# Nightly research handoff

Canonical file for PI review. Not a finished poster. Not group-final.

**Current thesis:** honesty-retitled revised D, spoken as the Mission 2 evidence-boundary freeze — `state/current_thesis.md`. Provisional storyboard: `poster/storyboards/revised_D.md`. Replacement flagship: **UNRESOLVED — NONE as title**.

**Mission 1 (2026-09-11):** science-story gate opened at **REVISE**. Occupancy-at-basal withdrawn as a finding; S066 clocks remain primary. Full record: [`reports/mission1_story_tournament.md`](mission1_story_tournament.md).
**Mission 1 closure:** completed with gate **REVISE** and `group_final=false`. Closure: [`reports/mission1_closure.md`](mission1_closure.md). Gate JSON: `state/gates/science_story.json`.

**Mission 2 (2026-09-12):** science freeze **FREEZE** at gate **REVISE**. Science-freeze test **PASS** (no flagship plot). Tournament **85+ HONEST: NO** (Wave D 83 NEITHER / 73 DISCARD unchanged; Wave C 67/67 unchanged). Score-blind freeze reviews: independent **80 REVISE**; Opus **74 REVISE**; fatals none. Do not mean 74 with 80, or 73 with 83. Do not manufacture 85. QUANTITATIVE FLAGSHIP: **NONE**. Ames-loaded wording stays dropped. Class B identity bounded, not looped. READY FOR MISSION 3: **NO**. GROUP FINAL: **NO**.

**PI 2026-09-12 (canonical now):** APPROVE AFTER SMALL FIXES. READY FOR MISSION 3: **YES**. Gate stays **REVISE**. Highest-information experiment: **U2**. QUANTITATIVE FLAGSHIP: **NONE**. `group_final` false. Do not reopen Mission 2. Do not manufacture PASS. The dated Mission 2 block above is the freeze-night record. Wave C/D and score-blind review-report files are not in this tree; those scores are coordinator-reported provenance (`research/reviews/premium/mission2_scores_provenance.md`).

**Mission 3 (communication RC, draft PR #33):** eyefix-package is materialized under `poster/rc/` on `cursor/m3-int-eyefix-245a`. Pre-composition Astra: **SKIPPED — PACKET INCOMPLETE**. Cold Astra on `6c2d7f67` / PDF `18d43961`: **ADVANCE AFTER SPECIFIED FIXES** (science fatals none). Specified-fix visual git `854a17a`; off-repo PDF `bbdac147`; changed-pixel vision **MUST FIX none**. Astra findings addressed by Cursor/Sol. Exact-head GitHub `validate` on `41e9acd` ran the poster rebuild step: **PASS: decoded pixels match**. Science story gate stays **REVISE**. `group_final` false. QUANTITATIVE FLAGSHIP **NONE**. U2 locked. Not FINAL. Do not merge PR #33. Do not reopen Mission 2.

Overnight T1/T5 are **not** current consensus and were never group-final.

## 1. Best current poster thesis

Hu’s Ø 25 µm Fc-thiol 39-mer MEASURES ACV signal-gain referenced to a post-insertion baseline on two tissue legs with unequal IVs—post-insertion rise (time; light on) and later on–off–on (illumination)—both INFERRED as glutamate. Printed spiked-buffer `%gain` maps cannot invert tissue ACV; identity stays UNKNOWN until named U2. Rapid-transient readiness remains unmeasured.

Status: **canonical working thesis, gate REVISE, Mission 2 science freeze FREEZE, not group-final** (`D_revised` id kept). Mission 2 discarded retitled D **as a 75+/85+ contribution** (Wave C 67/67). Original Thesis E (**83 NEITHER**) is recorded, not adopted as worded. Unnamed-measurement (**73 DISCARD**) remains recorded. Score-blind freeze reviews (**80 REVISE** independent; **74 REVISE** Opus) do not replace Wave C or Wave D. The frozen object is the bounded evidence-boundary restatement. Do not mean 73 with 83, Wave C 67 with 82, or 74 with 80. Tournament 85+ stays unreached.

Herman ~25 nM and Clements ~1.1 mM come from **different hippocampal preparations** and are not a retinal range or an accepted representative surface-device span. Hu 1.8 nM is an AuED-MEA Langmuir–Freundlich apparent Kd, not the PaC probe’s molecular Kd.

## 2. Runner-up thesis and why it lost

**Candidate C (working-range bars):** arithmetic reproduced (36/36 on isolated Mission 2 rebuild). **Not flagship.** Dual-pole “no bar contains Herman 25 nM and Clements 1.1 mM” is a category error. Ceiling-from-above may remain a supporting panel without enzyme-LOD overlays.

**Scale-map as title:** discarded. S066 leaves identity, occupancy, pool, and PaC Kd UNKNOWN as glutamate. An empty grid cannot carry the poster.

**Sampling clocks:** 36/36; **flagship rejected** (1.2 ms is the wrong spec for Hu’s GCL experiment; not Nyquist).

**Historical overnight T5** remains historical. Occupancy overlay stays demoted.

## 3. Top verified primary sources (smallest set)

1. Hu 2025 RWTH thesis S066 DOI 10.18154/RWTH-2025-07238 — in vitro mouse retina; 14 s / 1 min ACV; two ACV legs with unequal IVs; authors interpret as basal/sustained, not transients; not a pharmacological ID.
2. Hu 2025 journal S002 PMID 40992279 — AuED-MEA 1.8 nM LF apparent Kd in PBS; 12 µM is a Wu citation.
3. Wu 2022 S001 PMID 34783880 — 1d04 Kd 12 µM vs glu1 LOD (abstract); VoR still UNKNOWN.
4. Herman & Jahr 2007 S050 PMID 17804634 — ~25 nM ambient in **acute hippocampal slice**.
5. Clements 1992 S049 PMID 1359647 — inferred 1.1 mM, τ 1.2 ms at **cultured hippocampal synapses** (abstract).
6. Rutherford 2007 S054 — cites 500–800 ms (Burmeister); freely moving data recorded at **1 s**.
7. Clay 2018 S055 — modeled t90 0.73 s vs cited experimental 0.8 ± 0.2 s.
8. Xiao 2025 S021 PMID 40433802 — SPR Kd 293 nM; Table S1 sequence-locks oligo to Hu 39-mer; Fig. S6 is a Kd calibration, not kon/koff.

Full table: `research/evidence/poster_numbers.md`.

## 4. Five most important scientific insights

1. **Recognition ≠ architecture ≠ biological process** until a cited experiment connects them. Do not transfer 1.8 nM onto PaC/tissue occupancy. Do not recover θ from printed `%gain`.
2. **Hu 39-mer** is the exact 5′ of the Lam-quoted 98-nt Wu string. **12 µM is a citation hop**, not a 39-mer Kd.
3. **S066 is the only nervous-tissue Glu-apt experiment in the ledger, and its Glu identity is untested on both ACV legs**, including Hu’s baseline-rise “successful detection” sentence. Unequal IVs are what was varied, not two Hu-designed Glu assays.
4. **No THE basal spec.** Hascup 2008 Str 5.0 ± 1.2 µM is a real GluOx resting, not the Hu-class pole. Ames contains both 25 nM and 5 µM. Do not pair 5 µM with Clements. Ames is not a Glu-free ionic twin of PBS; Ames-loaded wording stays dropped.
5. **Missing `kon`/`koff` (C007) is not measured slowness.** Protocol time is not koff. Do not fill from tobramycin IPA or Ding.

## 5. Three important contradictions / limitations

1. Canonical Claim 5 / Panel 3 previously named identified glutamate while the same files listed identity as UNKNOWN. **This INT retitles both legs** as MEASURED ACV signal-gain referenced to a post-insertion baseline / INFERRED glutamate, with unequal IVs (time; light on vs later illumination). Identity stays UNKNOWN at panel scale. A later class-A stamp loop removed `SLOW / BASAL — MEASURED` from `two_regime_clocks.svg` and set Panel 3 PROPOSED to U2.
2. C022 previously stored 500–800 ms as Rutherford `response_time`; the paper **cites** that clock and **recorded at 1 s**. **This INT splits them.**
3. Isolated LF-*n* algebra `81^(1/n)` is correct, but that package still draws the withdrawn 44000-fold overlay. Measuring *n* does not restore the flagship. Accepted `occupancy_kinetics` on `main` is 1:1 Langmuir only. Ch. 7 “steady-state [Glu]” is not a licensed MEASURED reading of Fig. 6.13.

## 6. Flagship computational analysis — unresolved

Replacement flagship: **NONE as title**. Mission 2 reproductions (isolated branches, not merged):

| Package | Branch / SHA | Tests | Flagship? |
| --- | --- | --- | --- |
| Sampling clocks | `cursor/analysis-m2-sampling-634f` @ `5543ce7c6bc3c0b100e16f4ebeba85ddce218052` | 36/36 | **Rejected** (wrong spec; not Nyquist) |
| LF *n* span | `cursor/analysis-m2-lfn-634f` @ `93ddf2300edbaa7386c8baaadf4837592b7e7e27` | 10/10 | Algebra only; overlay **not restored** |
| Working-range | `cursor/analysis-m2-working-range-634f` @ `449ea4fd3aaa5916ae73f2fcdc0b44937f3b7e52` | 36/36 | **Not flagship** (dual-pole splice) |

Supporting on `main`: `span_identity.svg`, `two_regime_clocks.svg` (slow column MEASURED as ACV signal-gain; identity UNKNOWN; PROPOSED is U2), `atlas.svg`. Demoted: `occupancy.svg`.

A two-panel glyph of printed PBS vs Ames slopes is optional supporting analysis only. It is **not** a path to 85+ and cannot invert tissue ACV. Do not reopen “must decide a replacement flagship” as an open action.

## 7. Status of implemented analyses and tests

Accepted on `main`:

- Atlas tests + `atlas.svg` (glutamate kon/koff cells remain empty)
- Occupancy/kinetics tests (81-fold identity; advertised-number overlay arithmetic is supporting/demoted) + `span_identity.svg`

Repo command: `sh analysis/accepted/rebuild.sh` and `python3 -m unittest discover -s tests -v`.

Isolated Mission 2 packages are **not** merged. Open PR board should be this INT plus at most one challenger.

**Supporting figures for the handoff (verified, not an accepted flagship):**

| # | path | why it was kept | labels |
| --- | --- | --- | --- |
| 1 | `analysis/accepted/figures/span_identity.svg` | valid 81-fold identity; endpoint comparison not accepted as representative; PaC occupancy UNKNOWN | MEASURED / MODELED / UNKNOWN / PROPOSED |
| 2 | `analysis/accepted/figures/two_regime_clocks.svg` | S066 ACV signal-gain clocks vs untested transients; identity UNKNOWN; PROPOSED is U2 | MEASURED signal-gain vs UNKNOWN |
| 3 | `analysis/accepted/figures/atlas.svg` | Only plot that refuses to invent glutamate kon/koff | glutamate kon/koff stay empty; grey dashes may be curated omissions |

Demoted: `occupancy.svg` (overlay simulation, not tissue occupancy). Supporting: `sensitivity.svg`, `clocks.svg`.

## 8. Six-panel storyboard (text only)

See `poster/storyboards/revised_D.md`. Provisional panels: two regimes; Flagship placeholder — NONE; Hu retina two ACV legs on a slow clock, identity UNKNOWN (PROPOSED is U2; two-map central object is prose-only); PaC occupancy UNKNOWN; construct atlas; proposed next measurement (U2 on both legs, same shank and room-light protocol).

Historical overnight T1 storyboard: `poster/storyboards/winner.md` (superseded; occupancy inversion demoted).

No polished poster was generated. Mission 3 internal RC (not final) lives at `poster/rc/poster_rc.svg` on draft PR #33.

## 9. Hardest five assessor questions

1. What did Hu measure in the retina, and what would make you stop calling it glutamate — including the post-insertion baseline-rise sentence and the later on–off–on leg?
2. Why is 1.8 nM not the PaC Kd, and why is 12 µM not the 39-mer Kd? Why can printed `%gain` maps not invert tissue ACV?
3. Show 81-fold as biochemistry without using Herman-to-Clements as a device spec.
4. Why not treat empty koff, or 14 s vs 1.2 ms, as proof the aptamer is too slow?
5. Why doesn’t averaging 25 nM with 5 µM give “the” basal? Why is Ch. 7 “steady-state [Glu]” not a MEASURED reading of Fig. 6.13?

## 10. Swarm/prompt improvements that survived benchmarking

Observed failure: 4/4 isolated thesis writers refined the same frame. Adopted patch in `AGENTS.md`: at least one candidate must challenge the current framing.

Second observed failure: Wave C 4/4-style collapse to one slogan was already patched; Wave C still split on the 75-line (A none ≥75; B 8★ = 82 NEITHER). **Not patched by averaging.**

Constitution, rubric, and safety files were not edited.

## 11. Failures, unresolved uncertainties, blockers

- C007 empty. C032 empty on PaC for Asp/Gln/GABA. Wu VoR UNKNOWN. Clements VoR abstract-only. Burmeister VoR unopened (citation target of 500–800 ms).
- S066 analyte identity UNKNOWN on both ACV legs. PaC θ UNKNOWN. GCL/IPL-border vs photoreceptor pool UNKNOWN. In vivo Glu aptamer UNKNOWN (C020). Late-only rebin of Fig. 6.13 *p* UNKNOWN.
- Unknown 1 (paired 39-mer isotherm) and unknown 2 (tissue identity) are **not substitutes**.
- **85+ remains unreached on present public evidence.** U2 cannot be filled by scoring, caption, or a glyph of already-printed slopes. That is why the tournament bar is unmet; it is not why Mission 2 cannot freeze.
- Course cannot run wet IPA. Do not fill C007 computationally.
- Fatal objections: **NONE**. Ames-loaded wording stays dropped.
- Poster RC `validate` failed decoded-pixel match on `9aabb85`, then **passed** the rebuild step on `41e9acd` (`PASS: decoded pixels match`). Fonts are now shipped under `poster/rc/fonts/`; that commit’s GitHub run is not claimed until it finishes.

## 12. Exact Git commit SHA

Science freeze `origin/main`: `3fa11240c85df9ebac58dcc6879494911968f75c` (merge of PR 32). Astra-audited candidate: `6c2d7f67b0d36f46d686f7f76fd8720267d24f20`. Specified-fix visual: `854a17a117f78b5a65bdf8f7964f7997d493467f`. PDF-hash record: `44bd1997b54660940e26c31aa3a1527edc014b23`. Phase F INT `a60c0481b0d33b19ba5e51d034ffbfb47701e301`. First exact-head poster-rebuild CI green: `41e9acdef529524acc13f59cf5eecaafd7e95e38`. This fonts-shipping INT does not embed its own SHA. Isolated analysis SHAs in §6. Do not use overnight `984af62` or pre-reset `c87ebe4` as current science.

## 13. Exact paths

- Nightly: `reports/nightly_summary.md`
- Current thesis: `state/current_thesis.md`
- High-value unknowns: `state/high_value_unknowns.md`
- Model disagreements: `state/model_disagreements.md`
- Mission 1.5 closure: `reports/mission1_closure.md`
- Evidence table: `research/evidence/core_evidence.csv`
- Poster numbers: `research/evidence/poster_numbers.md`
- Claims: `state/claims.csv`
- Contradictions: `research/reviews/contradictions.md`
- Citation audit: `research/reviews/citation_audit.md`
- Tanner objections: `research/reviews/tanner_objections.md`
- Scoreboard: `state/scoreboard.json`
- Historical scoring reconciliation: `rounds/03/tournament_reconciliation.md`
- Current storyboard: `poster/storyboards/revised_D.md`
- Mission 3 entry: `reports/mission3_entry.md`
- Mission 3 communication RC: `poster/rc/` on draft PR #33 (`poster/rc/poster_rc.svg`, `poster/rc/checkpoint.md`, `poster/rc/astra_report.md`)
- Historical T1 storyboard: `poster/storyboards/winner.md`
- Supporting span identity: `analysis/accepted/figures/span_identity.svg`
- Figure 2 two-regime clocks: `analysis/accepted/figures/two_regime_clocks.svg`
- Figure 3 atlas: `analysis/accepted/figures/atlas.svg`
- Demoted occupancy overlay: `analysis/accepted/figures/occupancy.svg`
- Supporting sensitivity / clocks: `analysis/accepted/figures/sensitivity.svg`, `analysis/accepted/figures/clocks.svg`
- Source code: `analysis/accepted/atlas/atlas.py`, `analysis/accepted/occupancy_kinetics/model.py`, `analysis/accepted/occupancy_kinetics/figures.py`
- Captions: `analysis/accepted/figures/occupancy.CAPTION.md`, `analysis/accepted/figures/atlas.CAPTION.md`
- Table: `analysis/accepted/occupancy_kinetics/tables/occupancy_table.csv`
- Rebuild: `analysis/accepted/rebuild.sh`
- Consolidation log: `rounds/consolidation.md` (historical overnight merge)
- Mission-2 input queue: `state/mission2_input_queue.md`
- PR disposition register: `state/pr_disposition_register.md`

## Decisions for PI review

1. **Do not treat overnight T1 as current.** Canonical working thesis id is honesty-retitled revised D, spoken as the evidence-boundary freeze. It is **not** a 85+ Mission 2 tournament finalist.
2. **Replacement flagship stays NONE.** Sampling-clock and dual-pole working-range are rejected as titles. Do not reopen replacement selection.
3. **Lock unknown 2 vs unknown 1.** Recommendation: U2 — pharmacology plus scrambled/binding-null on both ACV legs, same shank and room-light protocol. Only a human may lock.
4. **Do not set PASS or group-final** without a measured identity or construct-locked quantity on this film.
5. **Do not treat this file as group-final** until a human initials `state/decisions.md`.

**Human / PI decision (2026-09-12):** APPROVE AFTER SMALL FIXES. Canonical `ready_for_mission3=true`. Gate stays REVISE. U2 locked. QUANTITATIVE FLAGSHIP NONE. group_final false. Do not reopen Mission 2. The boxed Mission-2 PI record below is historical.

```
MISSION 2 STATUS: REVISE
MISSION 2 SCIENCE FREEZE: FREEZE
RECOMMENDED THESIS: Evidence-boundary restatement (two unnamed ACV legs with unequal IVs; printed %gain maps cannot invert; identity UNKNOWN until U2). Git id remains D_revised. Not a 85+ tournament finalist.
RECOMMENDED FLAGSHIP: UNRESOLVED — NONE as title
MOST IMPORTANT REMAINING UNKNOWN: U2 tissue identity on both ACV legs (not a substitute for U1)
HIGHEST-INFORMATION NEXT EXPERIMENT: Pharmacology plus scrambled/binding-null on both ACV legs, same shank and room-light protocol. Do not substitute rates for identity if the claim is U2. Optional late-only Fig. 6.13 split does not name the analyte. Unknown 1 if a human locks construct fitness.
READY FOR MISSION 3: NO
GROUP FINAL: NO
HUMAN DECISION REQUIRED: Lock U2 vs U1; do not set PASS or group-final without a measured identity or construct-locked quantity on this film. 85+ HONEST: NO. Do not manufacture 85.
```
