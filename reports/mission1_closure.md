# Mission 1.5 — Canonicalize and close the science-story gate

Not a finished poster. Not group-final. Criteria were **not** weakened.

Date: 2026-09-11. Branch: `cursor/story-gate-closure-634f`.  
Prior gate: **REVISE** (`reports/mission1_story_tournament.md`; `research/reviews/premium/opus_story_gate.md`).  
Closure review: Opus 5 (`bc-7da27ff4-88b3-5acc-b4cc-ad86a0beaa66`), saved verbatim at `research/reviews/premium/opus_story_closure.md`.  
No new literature search.

## Verdict

Named revisions resolve the reasons the gate previously failed. Occupancy-at-basal is withdrawn as a finding. Remaining load-bearing claims are inspected primary evidence, correctly graded algebra, or honestly empty cells. Biological-context transfers are explicit. Counterevidence (gold loss, layer tension, Ames SNR) is displayed rather than hidden. The flagship computation is the 81-fold 1:1 Langmuir identity, not a 1.8 nM tissue-occupancy overlay. Opus identified **no fatal defect** and graded all five original criteria **PASS**.

**SCIENCE STORY GATE: PASS** on the existing criteria. Thesis is not group-final.

---

## 1. Canonical state

Created:

- `state/current_thesis.md` — canonical revised D
- `state/high_value_unknowns.md` — five Mission 1 unknowns, still open
- `state/model_disagreements.md` — live science disagreements plus historical ranking splits

Marked **historical / superseded as current consensus** (history kept):

| Artifact | What a later reader could mistake | How it is marked |
|---|---|---|
| `poster/theses.md` | Overnight T1 as the winner | Current revised D first; T1/T5 table labeled historical |
| `poster/storyboards/winner.md` | T1 six-panel + T5 occupancy inversion as flagship | HISTORICAL banner; points to `revised_D.md` |
| `state/scoreboard.json` | `"current_best_thesis": "T1"` | Now `D_revised`; T1 nested under `historical_overnight_tournament` |
| `reports/nightly_summary.md` §1 | T1 as best current thesis | Rewritten to revised D; overnight SHA demoted |
| `rounds/01/scout_merge.md` | 65 candidates / no core as live census | HISTORICAL CENSUS banner |
| `rounds/02/round2.md` | 16 core / 26 claims as live census | HISTORICAL CENSUS banner |
| `rounds/03/` | Stack A T1 winner as current | HISTORICAL OVERNIGHT banners |
| `analysis/candidates/theses/` | T1–T5 as current dossiers | README: historical |
| `rounds/mission1/candidates/D.md` | Occupancy-at-basal as a finding | AS SUBMITTED / superseded as a claim |

`state/scoreboard.json` `current_best_thesis` is `D_revised`. Overnight T1 remains in the historical block so the inversion of Stack A vs Stack B is still auditable.

---

## 2. Canonical revised D

Full text: `state/current_thesis.md`.

One sentence: there is no generic glutamate-aptamer sensor: neurochemistry is two measurement regimes (slow/basal versus rapid transients); a 1:1 Langmuir site spans exactly 81-fold while two commonly cited hippocampal literature concentrations span ~44,000-fold; the only glutamate-aptamer experiment in nervous tissue in this ledger is positive evidence inside a basal/slow clock; occupancy on that retinal probe is unmeasured; missing `koff` does not prove slow kinetics.

Constraints honored:

- Slow/basal measurement is distinguished from rapid transient measurement.
- Herman ~25 nM and Clements ~1.1 mM / 1.2 ms are literature examples from **different hippocampal preparations**, not a retinal concentration range.
- Occupancy on the retinal PaC probe is **unmeasured**.
- Hu’s 1.8 nM Langmuir–Freundlich apparent fit is an **AuED-MEA PBS** number, not the retinal probe’s molecular Kd.
- Missing glutamate `koff` is not treated as proof of slow kinetics.
- Hu retinal work is **positive** neural-tissue evidence within its demonstrated temporal regime (C033 / E046; authors: basal, not synaptic transients).
- Construct, matrix, device, and quantity types remain distinct (32 pM = PBS LOD; 51.5 pM = 50% serum LOD; 0.3 pM = PaC PBS blank+3 RSD, not Ames).

Ledger promotions from already-inspected S066 rows (not a new search): **C033** (light-on/off ACV, E046) and **C034** (GCL bottom electrode, E045). C030 notes now carry the authors’ 41.6% Ames blank noise from E044.

---

## 3. Flagship storyboard and figures

Current: `poster/storyboards/revised_D.md`. Stamps **MEASURED / MODELED / UNKNOWN / PROPOSED** are panel-scale, not caption-only.

Flagship figures:

1. `analysis/accepted/figures/span_identity.svg` — 81-fold identity as a sliding design-principle ruler at a generic 1 µM Kd (so it cannot be read as the 1.8 nM overlay). Herman and Clements ticks labeled by preparation. PaC occupancy UNKNOWN. 1.8 nM is not drawn as tissue occupancy.
2. `analysis/accepted/figures/two_regime_clocks.svg` — basal/slow MEASURED versus rapid-transient UNKNOWN, including Ames 41.6% blank noise and GCL placement.

**Demoted:** `occupancy.svg`. Title is DEMOTED overlay SIMULATION. Legend no longer prints θ(25 nM)=0.93. Overlay math remains locked under `test_overlay_theta_at_herman_ambient_if_1p8nm_treated_as_1to1_kd` (renamed so the test name cannot reassert tissue saturation).

---

## 4. Blind Opus 5 closure review

Packet: `rounds/mission1_closure/packet.md`. Question asked, and only that question: *Do the named revisions resolve the reasons this gate previously failed?* No desired PASS was given. Safety file was present and read.

Verbatim: `research/reviews/premium/opus_story_closure.md`.

| Original criterion | Opus 5 |
|---|---|
| One thesis materially stronger | **PASS** |
| Load-bearing claims have primary evidence | **PASS** |
| Survives counterevidence | **PASS** |
| Fits one poster without collapsing quantities | **PASS** |
| Computation answers the thesis | **PASS** |
| Fatal defect | **none** |
| Overall | **PASS** |

Direct answer: **Yes.** Occupancy-as-finding is withdrawn in the thesis, storyboard, and flagship figure rather than only in commentary.

Cheap residuals named by Opus and closed in this same mission: C033/C034 promotion; C030 41.6% note; photoreceptor sentence restated conservatively; 32 pM labeled PBS not “matrix-matched”; Panel 5 10 fM duplication fixed and 0.0013 pM restored; occupancy tick labels un-overlapped; Ames SNR printed on Panel 3; overlay test renamed; axis label added to `span_identity.svg`. Dopamine 49.6 vs 44 µM was **dropped from the canonical thesis** (it is not a `claims.csv` row; it remains in Mission 1 dossiers and `model_disagreements.md`).

---

## 5. Gate decision

PASS only if all of the following hold. They do:

| Requirement | Result |
|---|---|
| Revised thesis has load-bearing support | Yes. Herman two-component sentence; S066 clocks and light-on/off ACV; 81-fold identity; empty kon/koff cell. |
| Unsupported occupancy claims absent | Yes. PaC θ UNKNOWN. 1.8 nM not used as PaC Kd. Overlay demoted. |
| Biological-context transfers explicit | Yes. Different hippocampal preparations; not a retinal range; Clements not evidence about photoreceptor release. |
| Counterevidence survived rather than hidden | Yes. Gold loss, GCL vs photoreceptor pool, Ames 41.6% SNR, Probe 3 unresolved. |
| Computation supports the thesis | Yes. Flagship is the 81-fold identity vs ~44,000-fold literature span. |
| Opus identifies no fatal defect | Yes. |

Criteria were not rewritten. Completion is not acceptance. Human approval still required for group-final.

---

## 6. Open PR review

### PR #7 — evidence/state audit (`cursor/mission1-map-9264`, draft)

Inventory of Mission 1 evidence. Checkout was `9819f0a`. Confirmed stale T1 in `poster/theses.md` / `scoreboard.json`, stale Round 1/2 censuses, and numbers in narrative that are not ledger rows. **No story recommendation.** This closure treated it as an audit checklist and repaired those stale files on this branch. It is not a ranking and was not merged into the core ledger.

### PR #6 — enzyme GluOx comparator wildcard (`cursor/wildcard-matrix-effects-8459`, open, not draft)

Unpromoted Mission 2 wildcard. New sources (Wassum 2008/2012, Burmeister 2013, Robbins 2024, Kimble 2023, Wang 2019 abstract) are **not** in `claims.csv` / `core_evidence.csv`. Overlap with existing Rutherford **C022/S054** and Clay **C023/S055** is noted; those remain the enzyme comparators in the core ledger. Hypothesis that enzyme sensors should reframe the organizing question is **not** promoted. Do not run the audit pipeline by copying PR #6 numbers into the core tables.

---

## 7. Before closing a major mission

**What did we believe before?** Mission 1 recommended revised D but left the science-story gate REVISE, because occupancy-at-basal was not primary. Overnight T1 still sat in `poster/theses.md` and `scoreboard.json` as if it were current consensus.

**What changed?** Occupancy-as-finding was withdrawn in canonical files, not only in a synthesizer note. Herman/Clements are labeled as different hippocampal literature examples. Hu retina is scored as positive basal/slow evidence. Flagship glyph is the 81-fold identity. Stale T1 artifacts are historical. Opus 5 closure graded all five original bullets PASS with no fatal defect.

**What surprised us?** The occupancy overlay was still load-bearing in the *test name* `test_hu_saturated_at_tonic` after the thesis had withdrawn the finding. Renaming it was a one-line repair that would otherwise have re-taught the next agent the withdrawn claim. Also: 32 pM had been called “matrix-matched” in supporting prose; it is the PBS LOD.

**What was tested and rejected?** Using 1.8 nM as PaC tissue occupancy; treating missing koff as a kinetic proof; treating Herman+Clements as a retinal spec; leaving T1 as current consensus; promoting PR #6 into core.

**Important uncertainty.** Paired 39-mer solution/surface Kd; chemical identity of the S066 ACV; glutamate kon/koff; Ames Asp/Gln interference; Probe 3 mechanism.

**What most threatens the preferred thesis?** A paired 39-mer isotherm near 12 µM (occupancy-at-basal stays unmeasured, and Candidate C’s working-range story strengthens), or pharmacology that the light-off ACV increase is not glutamate.

**What most strengthens it?** Author-owned S066 clocks and light-on/off ACV; Herman’s two-component sentence; 81-fold identity with no aptamer number; explicit UNKNOWN occupancy.

**Highest-information next action.** Paired solution and surface isotherm of the Fc-thiol 39-mer, report Langmuir–Freundlich *n*. If the question is retina biology, substitute pharmacological identity. Do not do both and report neither.

**Work not done, judged low value.** Another literature search; polished poster; promoting PR #6; docking; averaging overnight scoring stacks.

**Would another round change a decision?** Another slogan tournament would not. A 39-mer isotherm or a pharmacological identity experiment would. Mission 2 should attack those unknowns, not re-rank titles.

---

SCIENCE STORY GATE: PASS
CURRENT THESIS: There is no generic glutamate-aptamer sensor: neurochemistry is two measurement regimes (slow/basal versus rapid transients); a 1:1 Langmuir site spans exactly 81-fold while two commonly cited hippocampal literature concentrations span ~44,000-fold; the only glutamate-aptamer experiment in nervous tissue in this ledger is positive evidence inside a basal/slow clock; occupancy on that retinal probe is unmeasured; missing koff does not prove slow kinetics.
MOST IMPORTANT REMAINING UNKNOWN: Paired solution and surface isotherm of Hu’s Fc-thiol 39-mer in one buffer, with Langmuir–Freundlich n reported (or pharmacological identity of the S066 ACV if the question is retina biology).
READY FOR MISSION 2: YES
