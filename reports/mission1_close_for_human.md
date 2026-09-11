# Mission 1 close package (for human review)

Scribe, not a new scientific authority. This file copies already-tagged records. It does not promote a thesis to group-final, does not change gate status, does not merge research PRs, and does not start Mission 2.

Date: 2026-09-11.  
Checkout this package was written against: `main` at `9819f0a77d85665915e01069e667ce89e6b38576`.  
Not a finished poster.

**Gate remains REVISE. `group_final` remains false.**

Short coordinator snapshot (do not duplicate here): [`reports/mission1_close_status.md`](https://github.com/bobshenruililin/BIOC1600-1/pull/22) on PR #22. This file is the full close package, including the eight-question table for PRs **#6–#21**, Mission 2 analysis drafts **#23/#24**, and Wave C architecture-transfer critique **#25**.

---

## 1. Gate state (unchanged by this package)

From `state/gates/science_story.json` (already on `main` via PR #4):

| Field | Value |
| --- | --- |
| `gate` | `science_story` |
| `status` | **REVISE** |
| `date` | 2026-09-11 |
| `group_final` | **false** |
| `recommended_thesis_id` | `D_revised` |
| `runner_up_id` | `C` |
| `report` | `reports/mission1_story_tournament.md` |
| `opus_review` | `research/reviews/premium/opus_story_gate.md` |

Pass-criteria already recorded in that JSON (not re-scored here):

- `one_thesis_materially_stronger.as_submitted` = `disputed`
- `one_thesis_materially_stronger.after_revision` = `true`
- `load_bearing_primary_evidence` = `false`
- `survives_counterevidence` = `partial`
- `fits_one_poster` = `true`
- `computation_answers_thesis` = `qualified`

`state/decisions.md` already records: Mission 1 science-story gate = REVISE; revised D recommended as title, not group-final; occupancy-at-basal not primary; overnight T1 ranking not adopted as this mission’s result; human approval still required. **No group-final thesis has been approved.**

This close package does **not** edit `state/gates/science_story.json`, hash-locked files, `poster/theses.md`, `state/scoreboard.json`, or `reports/nightly_summary.md`.

---

## 2. What Mission 1 recommended vs what overnight T1 still occupies

This split is **unresolved for humans**. It is not fixed by rewriting T1 away in this package.

### Mission 1 recommendation (story tournament)

Source: `reports/mission1_story_tournament.md` Verdict; `state/gates/science_story.json`.

**Recommended title (revised D).** There is no generic glutamate-aptamer sensor. Neurochemistry is two regimes (Herman’s baseline plus superimposed transients). A 1:1 Langmuir site spans exactly 81-fold between 10% and 90% occupancy, while those literature concentrations span ~44,000-fold. The only neural-tissue Glu-apt experiment (Hu thesis S066) is already clock-limited to basal/slow sampling. Occupancy at that basal on the parylene-C probe in Ames or tissue is **unmeasured**, not shown saturated. Millisecond cleft reporting is **untested** — missing `koff` does not prove a millimolar rising edge is impossible.

Runner-up: Candidate C as a **panel** (working-range ceilings that miss Herman ~25 nM from above), not as the title.

Rejected as titles (already in the gate JSON `rejected_as_title`): A fit-for-purpose; B construct transformation; C’s strong LOD form; D’s three-regime form; D occupancy-saturation-as-measured; W1 amino-acid selectivity.

Overnight T1–T5 scores were **not** averaged into this ranking (`do_not_promote` includes “T1 overnight ranking as this mission's result”).

### What still occupies the poster-facing overnight files

`poster/theses.md` Winner (mean 87 / 100):

> Present glutamate DNA-aptamer sensors have not jointly demonstrated the molecular recognition, selectivity, kinetics, architecture, and validation needed to measure neurochemical dynamics: published Kd, apparent Kd, and LOD values attach to non-transferable constructs, glutamate kon/koff are unreported, and a 15 min electrochemical incubation cannot be identified with an inferred 1.2 ms cleft transient.

Source named there: isolated writer **T1**. Status: not group-final; scoring contested (Stack B inverts).

`state/scoreboard.json`: `current_best_thesis` = `"T1"`; `current_best_status` = `"provisional_contested"`; `runner_up_thesis` = `"T5"`. No `D_revised` key.

`reports/nightly_summary.md` §1 still prints that T1 sentence as **Best current poster thesis**, status provisional/contested (T1, Stack A). The nightly *header* already warns that overnight T1 is not Mission 1’s result; the §1 body still occupies T1.

`poster/storyboards/winner.md` is a **T1** six-panel outline with T5 occupancy inversion as the computational panel.

**How to read this without collapsing it.** Mission 1 did not delete the overnight tournament. It declined to adopt T1 as *this mission’s* result. Until a human chooses which file is poster-facing, both headlines are live in the repo.

---

## 3. Exact stale canonical files

“Stale” here means: the file still states an overnight occupancy that Mission 1 explicitly did not adopt, or it stamps a SHA that is no longer `HEAD`. Updating a file would change what a PI reads first; it would **not** by itself convert REVISE → PASS or `group_final` → true.

| File | What it still says | If updated to match Mission 1 (still REVISE, still not group-final) |
| --- | --- | --- |
| `poster/theses.md` | T1 is Winner (mean 87); T5 runner-up | Poster-facing headline would be **revised D**; T1/T5 would be labeled overnight occupancy, not this mission’s result |
| `poster/storyboards/winner.md` | Six panels for T1; T5 occupancy inversion as the computational panel | Computational panel would stop being θ-inversion / 1.8 nM overlay-as-finding; two-regime + 81-fold identity + S066 clocks would be the spine; occupancy-at-basal marked unmeasured |
| `state/scoreboard.json` | `current_best_thesis: T1`, status `provisional_contested` | Could *mention* `D_revised` as Mission 1 recommended title under REVISE. Must not set a PASS status. Human must decide the schema (see §7) |
| `reports/nightly_summary.md` §1 | Best current poster thesis = T1 sentence | §1 would headline revised D as Mission 1 recommendation and keep T1 as overnight occupancy, or would defer to `poster/theses.md` after a human choice |
| `reports/nightly_summary.md` §6 / §8 | Flagship = occupancy/kinetics + atlas; storyboard = T1 winner.md | Flagship pointer would match Mission 1: keep 81-fold identity (C027); demote 1.8 nM tissue-occupancy overlay. Storyboard pointer would no longer be T1-only |
| `reports/nightly_summary.md` §12 | Canonical SHA `984af62f25127b43e7d2be248ca1c8123921b8a8` | Checkout instruction would match live `main` (`9819f0a…` at this writing, after PRs #4 and #5). The old SHA is still in history (`0268887`); it is not current `HEAD` |

Historical census logs (not poster-facing, but stale if used as counts):

| File | What it still says | Live ledgers |
| --- | --- | --- |
| `rounds/01/scout_merge.md` | 65 sources, all `candidate`; no core | 66 sources; 17 `core` (inventory as of this checkout; not re-counted here as a new result) |
| `rounds/02/round2.md` | 16 core; older claim/evidence census | Later promotion of S066; 32 claims C001–C032 |

**Not stale as gate files:** `state/gates/science_story.json`, `reports/mission1_story_tournament.md`, `research/reviews/premium/opus_story_gate.md`, `state/decisions.md` last row. Those already say REVISE / not group-final.

This package does not update the stale files listed above.

---

## 4. Load-bearing primary vs withdrawn occupancy-at-basal vs computational illustration

Copied from existing tagged records (`state/claims.csv` and `reports/mission1_story_tournament.md` §4). No new numbers.

### 4.1 Load-bearing, `primary-source-supported` (revised-D spine that survives withdrawal)

| ID | Claim (ledger text or tournament restatement that the ledger already supports) | Quantity type | Construct / system | Transferable |
| --- | --- | --- | --- | --- |
| C012 | Ambient extracellular glutamate in hippocampal slice is about 25 nM by tonic NMDAR current. Tournament uses Herman’s two-component framing (baseline plus superimposed transients) from the same source (C012 / S050). | `biological_concentration_range` | not aptamer; acute hippocampal slice | no |
| C006 | Hu 2025 glutamate assay uses 15 min incubation before ACV. | `measurement_time` | Glu-apt; MEA ACV | no |
| C028 | Hu 2025 RWTH thesis: 10 nM glutamate signal on the Glu-apt intraretinal probe plateaus at approximately 10 min. | `measurement_time` | Glu-apt on PaC probe; probe calibration | no |
| C031 | Hu 2025 thesis records glutamate ACV in in vitro mouse retina at 14 s/scan then ~1 min sampling; the authors state this reports basal glutamate, not synaptic transients. | `measurement_time` | Glu-apt on PaC probe in retina; in vitro mouse retina | no |
| C005 | Hu 2025 glutamate electrochemical apparent Kd is 1.8 nM (Langmuir-Freundlich), distinct from cited 12 µM solution value. | `EC50` | surface Glu-apt; PBS ACV | no |
| C032 | Hu 2025 thesis selectivity panel compares 100 nM glutamate with 10 µM serotonin, dopamine, tyrosine, and lactate; aspartate and glutamine are not in that panel. | `signal_gain` (empty value: no ratio reported) | Glu-apt on PaC probe | no |

C031 notes already on the ledger: strongest Glu-apt neural-tissue experiment in this ledger; not in vivo; does not fill C007; Probe 3 near basal saturation; Probe 4 unstable. Value stored is the 1 min sampling interval.

### 4.2 Withdrawn as a finding (occupancy-at-basal)

Tournament §4 item 4 (not a new claim row): occupancy at basal on the **PaC probe in Ames/tissue is unmeasured**. The probe has no reported apparent Kd.

What was withdrawn: treating current devices as having **failed the slow problem on occupancy**, and treating Probe 3 as a clean occupancy ceiling.

Gate JSON already lists `D_occupancy_saturation_as_measured` under `rejected_as_title`. `load_bearing_primary_evidence` is already `false`.

Related primary that is **not** occupancy-at-basal of the tissue probe: C005 is an AuED-MEA Langmuir–Freundlich `EC50`, transferable = no. Using it as tissue θ is a hop the tournament already labels `computational illustration`.

Probe 3 occupancy reading: `unresolved` (gold-nanostructure detachment, thesis Fig. 6.16, already in tournament §6 and C031 notes). Probes 1–2 still change with light: remaining dynamic range at whatever the retinal basal is, not demonstrated saturation (`primary-source-supported` as S066 §6.3 in the tournament record).

### 4.3 `computational illustration` (and related tags) — do not promote to occupancy findings

| ID / object | Ledger / tournament tag | What it is | What it is not |
| --- | --- | --- | --- |
| C027 | `computational illustration` | For 1:1 Langmuir occupancy, c90/c10 = 81 exactly, independent of Kd | Not Hu’s fitted isotherm; Hu used Langmuir–Freundlich and **n is unknown** |
| C013 | `review-supported` | Rousseau states the same 81-fold identity for a generic E-AB Langmuir site | Tonic/cleft numbers in that claim text come from C012/C011, not measured in Rousseau |
| 25 nM → 1.1 mM ≈ 44,000-fold | tournament: `computational illustration` on C012 and C011 | Arithmetic on two literature concentrations | Not a measured span of one sensor |
| Overlay θ(25 nM)≈0.93 | tournament: `computational illustration`; C005 is a different device | 1:1 overlay of AuED-MEA LF 1.8 nM | Not PaC-probe tissue occupancy |
| τ_eq at 1.1 mM can still be short | tournament: `computational illustration` | Identity τ_eq = 1/(kon·c + koff) | Not a glutamate `koff`; do not quote koff ≈ 1/1.2 ms |
| C007 | `unresolved` | No glutamate aptamer kon/koff found in inspected glutamate sensor papers | Absence; C008/C010 are **not glutamate** (`transferable=no`); gate `do_not_promote` already lists “glutamate kon/koff from C008 or C010” |
| C011 | `primary-source-supported`, abstract-only | Inferred peak cleft glutamate 1.1 mM decaying with tau 1.2 ms at cultured hippocampal synapses | Kinetic inference, not chemical assay; VoR closed; hippocampal culture, not this retina experiment |
| C017 | `computational illustration` | Docking failed theophylline vs caffeine selectivity | Not a glutamate structure proof |

Hu 12 µM on the MEA paper is a **Wu citation**, not a Hu remeasurement (C021, `primary-source-supported`). Do not collapse with C005.

---

## 5. Premium Opus review (path only; no new consensus score)

**Read this file verbatim. Do not treat this section as a rewrite:**

`research/reviews/premium/opus_story_gate.md`

- Agent: `bc-35465731-9331-54fd-b508-ca3af59e84ec`
- Model recorded in that file: `claude-opus-5-thinking-xhigh`
- Blind: no Grok A–D ranking; T1–T5 / scoreboard / nightly files not opened
- Orchestrator note already in that file: reviewer reported `.cursor/rules/safety-and-integrity.mdc` missing; the file is present and hash-locked

Scores **already stored** in `state/gates/science_story.json` `opus_scores` (identical to the table in the Opus file):

| A | B | C | D |
| ---: | ---: | ---: | ---: |
| 68 | 73 | 77 | 85 |

Opus gate word in that file: **REVISE.** D is the story; the gate does not pass as submitted.

This close package:

- does not average Opus with Grok;
- does not enter a second Opus pass;
- does not treat synthesizer self-score 89 (`rounds/mission1/synthesis/d_revised.md`) as an Opus score;
- does not convert 85 KEEP-conditional into PASS.

---

## 6. Adversarial Grok disagreement (recorded, not adjudicated here)

Sources already on `main`: `reports/mission1_story_tournament.md` §3; `rounds/mission1/synthesis/opus_redteam.md` (agent `bc-3aa253b4-c60f-5313-8e51-d891b5f7fa49`); `rounds/mission1/synthesis/d_revised.md` (agent `bc-55b3484f-6d4d-5453-8b51-5c8bada88b45`).

**Agreement with Opus.** Gate stays REVISE. A fails as title. B is a panel. W1 is not a fifth title. C’s strong LOD form is false for Hu 32 pM. Missing `koff` does not prove a millimolar rising edge is impossible.

**Disagreement with Opus.** D **as submitted** was **not** materially stronger than C. The 85 KEEP scores occupancy-as-demonstrated and then withdraws it in the gate list. As submitted: C and D are a dead heat or C slightly ahead. **After named revisions:** D is the course title; C and B are supporting panels.

Gate JSON already encodes that split: `as_submitted: disputed`, `after_revision: true`. Stricter reading used for the gate: occupancy not primary (`load_bearing_primary_evidence: false`).

Revised-D synthesizer integer 89 is **not** a second Opus pass and does **not** convert REVISE into PASS.

**Status after named revisions: D is the recommended title. Status remains REVISE.**

---

## 7. Human decisions required

Agents may recommend. Humans record approval in `state/decisions.md`. None of the following is decided by this package.

1. **Which file is poster-facing?**  
   - Overnight occupancy: `poster/theses.md` (T1) + `poster/storyboards/winner.md`.  
   - Mission 1 recommendation: `reports/mission1_story_tournament.md` + `state/gates/science_story.json` (`D_revised`).  
   Until a human picks one headline, both remain live. Do not silently overwrite T1 in this close.

2. **May `state/scoreboard.json` mention `D_revised` without implying PASS?**  
   Recommended schema if a human later edits the scoreboard: keep overnight T1/T5 rows as historical Stack A; add a Mission 1 field such as `recommended_thesis_id: D_revised` with `science_story_status: REVISE` and `group_final: false`. Do **not** set `current_best_status` to anything that reads as PASS. Do **not** average Opus 85 with Stack A 87 or with synthesizer 89.

3. **Which scoring stack is authoritative for the overnight T1–T5 tournament?** Stack A (T1/T5 mean 87) vs Stack B (Task R1: T3; Task R2: T5/T4). Do not average. Independent of Mission 1 A–D.

4. **Re-gate to PASS?** Not available from this package. Tournament already says another slogan tournament without a PaC-probe isotherm (or an explicit poster that occupancy is unknown) is low value. Completion is not acceptance.

5. **Open research PRs #6–#25:** default **hold**. Do not merge from this close (see §9). Do not treat #21 sequences as ledger promotions. #19 follow-up does not change REVISE. [#23](https://github.com/bobshenruililin/BIOC1600-1/pull/23)/[#24](https://github.com/bobshenruililin/BIOC1600-1/pull/24) are Mission 2 analysis drafts. [#25](https://github.com/bobshenruililin/BIOC1600-1/pull/25) is a Wave C architecture-transfer critique, not close.

6. **Do not start Mission 2 from this package.** Wave A / analysis-implementation PRs (#11, #23, #24) and Wave C critique #25 are exploration parked for later, not Mission 1 acceptance criteria.

---

## 8. What must remain unresolved

Copied from tournament §6, `state/open_questions.md`, `state/remaining_blockers.md`, and the gate JSON. Not closed here.

- Occupancy at basal on the PaC probe in Ames/tissue (unmeasured; no probe apparent Kd).
- Probe 3: occupancy ceiling vs gold loss vs both.
- Whether to draw any 1:1 overlay of Hu 1.8 nM; n unpublished; 10–90% for LF is 81^(1/n), not 81.
- Non-transfer as a physical law vs hygiene (DA 49.6 µM ≈ cited 44 µM in the same LF panel).
- Middle extrasynaptic band as a design spec (Moussawi review span vs D’s tool-class/clock reading).
- H2 vs C031 on how hard to rank S066 (strongest Glu-apt neural-tissue experiment **and** device-level feasibility, not chemical identification).
- GCL/IPL-border electrode vs photoreceptor-terminal narrative.
- Opus 85 vs Grok “not materially stronger as submitted.”
- Ames L-glutamine vendor identity / interference (arithmetic on a public sheet is not an interference measurement).
- Glutamate aptamer `kon`/`koff` (C007).
- Chemical identity of the S066 ACV change (no TTX/CNQX/AP5/TBOA; no scrambled-aptamer probe in the Hu reconstruction).
- Wu 2022 VoR (abstract-only 1d04/glu1).
- Abrantes millimolar ELONA Kd: **not entered** on the ledger; tokens `10.3` / `25.1` recorded as funder IDs in Mission 1. Some Wave A text re-claims millimolar ELONA from preprint HTML (see PR #14). Do not promote from this close.
- No in vivo glutamate aptamer sensor (C020); S066 is in vitro retina.
- Overnight T1 vs Mission 1 `D_revised` as the poster-facing sentence.
- 39-mer / `glu1` / `glu1d04` sequence identity as parked in PR #21 — not a `claims.csv` row until extracted and audited.
- Whether A3 (#23) can later swap C vs D as title — the draft itself says **no automatic swap**.
- Whether A4 (#24) may reframe the highest-information next experiment as fast interrogation vs locking a basal/graded spec — the gate JSON still records the paired 39-mer isotherm; do not auto-update it.
- Whether Hershey 2025 “wrong quantity” (PR #18) survives the architecture-transfer critique in PR #25 — parked; not a title swap.
- Whether C008/C010 may appear on a poster as a labeled non-glutamate envelope (gate already: do not promote as glutamate rates).

Falsifiers already listed in the tournament (not performed): paired 39-mer solution/surface isotherm near 12 µM vs near 1.8 nM; pharmacological identity of the retina ACV change; measured Glu-apt `koff`; large Asp/Gln cross-reactivity at Ames-realistic concentrations.

Highest-information next experiment already in the gate JSON: paired solution and surface isotherm of Hu Fc-thiol 39-mer in one buffer; report Langmuir–Freundlich n. If the question is retinal glutamate rather than sensor fitness, substitute pharmacological identity. Do not do both and report neither.

---

## 9. Open research PRs — eight-question policy (default hold; do not merge)

Eight questions (parent):

1. Inference change if merged?  
2. New claims?  
3. Weakened claims?  
4. Numerical traceability?  
5. Construct / quantity / matrix / clock conflation?  
6. Science-gate alteration (`state/gates/science_story.json`)?  
7. Touches stale canonical files (`poster/theses.md`, `state/scoreboard.json`, nightly §1)?  
8. What stays unresolved?

**Recommendation vocabulary:** `hold` (default) | `human-review` (still do not merge) | `merge` (not used here).

None of PRs #6–#25 edits `state/gates/science_story.json` or hash-locked files. None should be merged as a Mission 1 close action. Default **hold**.

Round 1 scout PRs (#8, #10, #12, #13, #15, #16) re-run an already-completed Round 1 protocol into `rounds/round-1/scouts/` (that tree is **not** on current `main`). Treat as **Mission 2 exploration**, not Mission 1 close.

Wave A reports (#6, #7, #9, #11, #14, #17, #18, #19, #21) are **Mission 2 exploration**. #11 proposes analyses; it does not implement them. #19 reviews occupancy and calls REPLACE; a follow-up commit on that PR records that occupancy withdrawal keeps revised D as REVISE — **still not a gate decision**. #21 parks 39-mer sequence genealogy; **do not treat its sequence facts as ledger promotions**. #20 is coordinator hold-rationale for #19, not a science result.

[#23](https://github.com/bobshenruililin/BIOC1600-1/pull/23) implements A3 as an isolated draft under `analysis/working_range/` (not `analysis/accepted/`). [#24](https://github.com/bobshenruililin/BIOC1600-1/pull/24) implements A4 and **does** write under `analysis/accepted/interrogation_nyquist/` plus hooks in `analysis/accepted/rebuild.sh`. **Both are Mission 2 analysis drafts. Hold. Not Mission 1 close. Not a gate change.** Merging #24 would still change the accepted-analysis tree without flipping REVISE — that is a reason to hold, not a reason to treat it as close.

[#25](https://github.com/bobshenruililin/BIOC1600-1/pull/25) is a **Wave C architecture-transfer critique** of the “wrong quantity” inference (Hershey/Kennedy → aptamer electrode). The PR titles itself Goal Wave A; this close treats it as Wave C discrimination, not Mission 1 close. **Hold. Do not merge. Do not change the gate.**

PR #22 is the short status snapshot only; it is not re-tabulated here.

### Rec index (#6–#25)

| PR | One-line | Rec |
| --- | --- | --- |
| [#6](https://github.com/bobshenruililin/BIOC1600-1/pull/6) | GluOx comparator wildcard report | hold |
| [#7](https://github.com/bobshenruililin/BIOC1600-1/pull/7) | Mission 1 evidence map | hold |
| [#8](https://github.com/bobshenruililin/BIOC1600-1/pull/8) | Round 1 scout-04 immobilization | hold |
| [#9](https://github.com/bobshenruililin/BIOC1600-1/pull/9) | Immobilization / transfer audit | hold |
| [#10](https://github.com/bobshenruililin/BIOC1600-1/pull/10) | Round 1 scout-01 discovery | hold |
| [#11](https://github.com/bobshenruililin/BIOC1600-1/pull/11) | Analysis *proposals* (drafts are #23/#24, still hold) | hold |
| [#12](https://github.com/bobshenruililin/BIOC1600-1/pull/12) | Round 1 scout-06 wildcard | hold |
| [#13](https://github.com/bobshenruililin/BIOC1600-1/pull/13) | Round 1 scout-02 kinetics | hold |
| [#14](https://github.com/bobshenruililin/BIOC1600-1/pull/14) | Kinetics vs timescales; re-claims Abrantes 10.3/25.1 | hold + human-review |
| [#15](https://github.com/bobshenruililin/BIOC1600-1/pull/15) | Round 1 scout-03 architectures | hold |
| [#16](https://github.com/bobshenruililin/BIOC1600-1/pull/16) | Round 1 scout-05 biological Glu | hold |
| [#17](https://github.com/bobshenruililin/BIOC1600-1/pull/17) | New primary candidates (Hascup/Okubo/…) | hold |
| [#18](https://github.com/bobshenruililin/BIOC1600-1/pull/18) | Opposing-case (Hershey identity vs speed) | hold + human-review |
| [#19](https://github.com/bobshenruililin/BIOC1600-1/pull/19) | Occupancy-challenge; REPLACE is not a gate flip | hold |
| [#20](https://github.com/bobshenruililin/BIOC1600-1/pull/20) | Coordinator hold rationale for #19 | hold |
| [#21](https://github.com/bobshenruililin/BIOC1600-1/pull/21) | 39-mer genealogy; sequences ≠ ledger rows | hold |
| [#23](https://github.com/bobshenruililin/BIOC1600-1/pull/23) | A3 working-range draft (not `analysis/accepted/`) | hold |
| [#24](https://github.com/bobshenruililin/BIOC1600-1/pull/24) | A4 Nyquist draft (writes under `analysis/accepted/`) | hold |
| [#25](https://github.com/bobshenruililin/BIOC1600-1/pull/25) | Wave C identity-inference / architecture-transfer critique | hold |

PR #22 is status snapshot only (not in this index).

### #6 [Add enzyme comparator wildcard research report](https://github.com/bobshenruililin/BIOC1600-1/pull/6)

Branch `cursor/wildcard-matrix-effects-8459`. File: `rounds/goal-wave-a/wildcard.md`. Ready-for-review (not draft). +157 / 1 file.

| Q | Answer |
| --- | --- |
| Inference | Would park a GluOx-comparator organizing frame (`hypothesis` in the report). Does not displace revised D or T1 on canonical files. |
| New claims | Report-local W1–W16 (name collision with Mission 1 wildcard W1 = Asp/Gln). Not written to `state/claims.csv`. |
| Weakened | Challenges “cleft milliseconds” as the only pass/fail; does not weaken C006/C028/C031 clocks. |
| Traceability | Mix of already-ledger sources (Hu, Rutherford) and new GluOx papers. W15 tagged abstract-only. |
| Conflation | Report separates `response_time` vs `measurement_time`; still a comparator hop if read as aptamer rates. |
| Gate | No. |
| Stale canonical | No. |
| Unresolved | Matched Glu-apt vs GluOx experiment; aptamer in vivo still absent. |
| **Rec** | **hold** (Mission 2 exploration). |

### #7 [Map Mission 1 evidence (no story recommendation)](https://github.com/bobshenruililin/BIOC1600-1/pull/7)

Draft. `rounds/goal-wave-a/mission1-map.md`. Inventory of this checkout; no core promotion.

| Q | Answer |
| --- | --- |
| Inference | None intended; map explicitly refuses a story recommendation. |
| New claims | No ledger rows. |
| Weakened | None. |
| Traceability | Copies ledgers; useful as a stale-file inventory (matches §3). |
| Conflation | Flags existing collapses; does not add new ones as findings. |
| Gate | No. |
| Stale canonical | Documents them; does not edit them. |
| Unresolved | Same as Mission 1. |
| **Rec** | **hold** (harmless parking; still not a Mission 1 merge). |

### #8 [Round 1 scout-04: immobilization and interface candidates](https://github.com/bobshenruililin/BIOC1600-1/pull/8)

Draft. `rounds/round-1/scouts/scout-04.md`. Candidates only.

| Q | Answer |
| --- | --- |
| Inference | None if left as candidates. Duplicate Round 1 lane after Mission 1 already merged scouts. |
| New claims | Candidate records only; `state/claims.csv` untouched. |
| Weakened | None on the ledger. |
| Traceability | Identifiers claimed cross-checked; Wu/Abrantes remain abstract-level in the PR body. |
| Conflation | Lane is immobilization; risk is treating non-Glu interface papers as Glu Kd. |
| Gate | No. |
| Stale canonical | No. |
| Unresolved | Solution vs surface Kd of the 39-mer. |
| **Rec** | **hold** (Mission 2 / duplicate Round 1). |

### #9 [Immobilization and property-transfer audit](https://github.com/bobshenruililin/BIOC1600-1/pull/9)

Draft. `rounds/goal-wave-a/immobilization.md`.

| Q | Answer |
| --- | --- |
| Inference | 12 µM → 1.8 nM is not a measured confinement result; DA on the same chip is the internal counterexample. Aligns with Mission 1 B-as-panel, does not retitle. |
| New claims | None in `claims.csv`. |
| Weakened | Weakens B-as-mechanism if someone still wanted it as title (already rejected). |
| Traceability | Re-reads OA/PMC; MacDonald via HAL. Ohsawa still unentered. |
| Conflation | Explicitly lists hops (citation/truncation/LF/surface). |
| Gate | No. |
| Stale canonical | No. |
| Unresolved | Paired 39-mer isotherm; n. |
| **Rec** | **hold** (Mission 2 exploration). |

### #10 [Round 1 scout 01: glutamate DNA/RNA aptamer candidates](https://github.com/bobshenruililin/BIOC1600-1/pull/10)

Draft. `rounds/round-1/scouts/scout-01.md`.

| Q | Answer |
| --- | --- |
| Inference | None if candidates-only. Duplicate of completed Round 1 discovery lane. |
| New claims | No ledger writes. |
| Weakened | None. |
| Traceability | Construct split 1d04/glu1/Hu/Abrantes/Xiao/Ohsawa restated. |
| Conflation | PR body keeps Kd vs LOD vs docking separate. |
| Gate | No. |
| Stale canonical | No. |
| Unresolved | Wu VoR; glu1 Kd; Asp/Gln ratios; Glu kon/koff. |
| **Rec** | **hold** (Mission 2 / duplicate Round 1). |

### #11 [Goal Wave A: eight analysis-tournament proposals](https://github.com/bobshenruililin/BIOC1600-1/pull/11)

Draft. `rounds/goal-wave-a/analysis-proposals.md`. **Not an implementation.** Worker scores A3 75/80, A4 74/80; those integers are one pass, not a tournament, and must not enter `state/scoreboard.json` without independent red-team.

| Q | Answer |
| --- | --- |
| Inference | Would nominate working-range-vs-poles and interrogation-Nyquist as *next* flagships. Could later swap C vs D if implemented and scored. Not implemented here. |
| New claims | No `claims.csv` rows. Arithmetic labeled computational illustration on existing ledger numbers. |
| Weakened | Would demote occupancy/kinetics as *next* flagship; does not edit accepted analysis code. |
| Traceability | Uses C011/C012/C027/C030/C031; Ames Gln arithmetic flagged as not an interference measurement. |
| Conflation | Explicitly designed to avoid 1:1 overlay of 1.8 nM. |
| Gate | No. Does not edit `science_story.json`. |
| Stale canonical | No. |
| Unresolved | Whether A3 would actually swap C vs D; n unpublished. |
| **Rec** | **hold** (Mission 2 exploration — analysis *proposals*, not close). |

### #12 [Round 1 scout 06: wildcard literature candidates](https://github.com/bobshenruililin/BIOC1600-1/pull/12)

Draft. `rounds/round-1/scouts/scout-06.md`.

| Q | Answer |
| --- | --- |
| Inference | Enzyme/protein comparators and “is glutamate a hard SELEX target” as candidates, not a title. |
| New claims | Candidates only. |
| Weakened | None on the ledger. |
| Traceability | Candidate IDs S06-01–S06-15; not core. |
| Conflation | Risk of reading GluOx/iGluSnFR clocks as aptamer FoMs if promoted carelessly. |
| Gate | No. |
| Stale canonical | No. |
| Unresolved | Same comparator questions as #6. |
| **Rec** | **hold** (Mission 2 / duplicate Round 1 wildcard). |

### #13 [Round 1 scout 02: glutamate and small-molecule aptamer binding kinetics](https://github.com/bobshenruililin/BIOC1600-1/pull/13)

Draft. `rounds/round-1/scouts/scout-02.md`.

| Q | Answer |
| --- | --- |
| Inference | Negative search: no numerical kon/koff for 1d04/glu1/NG-Apt-Glu in inspected free-route set. Confirms C007; does not fill it. |
| New claims | No ledger writes. |
| Weakened | None. |
| Traceability | Tobramycin IPA called out as non-transferable (already C008). |
| Conflation | PR body forbids transferring tobramycin rates. |
| Gate | No. |
| Stale canonical | No. |
| Unresolved | C007. |
| **Rec** | **hold** (Mission 2 / duplicate Round 1). |

### #14 [Kinetics vs biological timescales Wave A report](https://github.com/bobshenruililin/BIOC1600-1/pull/14)

Draft. `rounds/goal-wave-a/kinetics.md`.

| Q | Answer |
| --- | --- |
| Inference | “Keeping up” is ill-posed until the compartment is named; no Glu kon/koff. Could challenge a single-basal-number poster. |
| New claims | Report-local K-rows, not in `claims.csv`. |
| Weakened | Would weaken any remaining “one ambient [Glu]” reading of Herman 25 nM if later promoted. |
| Traceability | **Fail against Mission 1 promotion rule:** re-states Abrantes inhibition ELONA `Kd_molecular` **10.3–25.1 mM** as `primary-source-supported` (preprint HTML Fig. 1D). Mission 1 / gate `do_not_promote` / tournament: millimolar ELONA Kd **not entered**; `10.3` / `25.1` recorded as funder IDs; HTML re-claims were not promoted. This close does not adjudicate which reading is correct. |
| Conflation | Vocabulary table is careful; ELONA vs FET LOD split is the intended exhibit — but only if the millimolar number is real. |
| Gate | No file edit. Promoting ELONA Kd would still be a ledger event, not a gate flip. |
| Stale canonical | No. |
| Unresolved | C007; which biological pole; Abrantes ELONA identity. |
| **Rec** | **hold** + **human-review** (citation audit of 10.3/25.1 before any promotion). Mission 2 exploration. |

### #15 [Round 1 scout 03: glutamate aptamer biosensor architectures](https://github.com/bobshenruililin/BIOC1600-1/pull/15)

Draft. `rounds/round-1/scouts/scout-03.md`.

| Q | Answer |
| --- | --- |
| Inference | None if candidates-only. Duplicate architecture lane. |
| New claims | No ledger writes. |
| Weakened | None. |
| Traceability | Mix of OA VoR (Hu) and abstract-only (Wu, Maldonado). Park GDH caution already C019. |
| Conflation | Lane is transduction metrics; PR body says no transfer across architectures. |
| Gate | No. |
| Stale canonical | No. |
| Unresolved | Same construct/matrix splits. |
| **Rec** | **hold** (Mission 2 / duplicate Round 1). |

### #16 [Round 1 scout 05: biological glutamate concentration ranges and timescales](https://github.com/bobshenruililin/BIOC1600-1/pull/16)

Draft. `rounds/round-1/scouts/scout-05.md`.

| Q | Answer |
| --- | --- |
| Inference | Would expand biological poles beyond Herman/Clements if later promoted (e.g. extrasynaptic imaging, CSF/plasma). Not promoted here. |
| New claims | 15 candidate sources; `claims.csv` untouched. |
| Weakened | Could weaken “Herman 25 nM is the ambient number” as a unique spec if promoted (already `unresolved` as a transfer onto retina). |
| Traceability | Clements still abstract-only; some CSF numbers abstract-only. |
| Conflation | Risk of packing cleft / extrasynaptic / CSF / plasma on one axis (the scout’s job is to keep them separate). |
| Gate | No. |
| Stale canonical | No. |
| Unresolved | Which compartment is Topic 1. |
| **Rec** | **hold** (Mission 2 exploration). |

### #17 [Wave A literature scout: new primary sources Mission 1 missed](https://github.com/bobshenruililin/BIOC1600-1/pull/17)

Draft. `rounds/goal-wave-a/literature-scout.md`. 14 sources absent from Mission 1 `state/sources.csv` (per PR body). Status **candidate**. Ledgers not edited.

| Q | Answer |
| --- | --- |
| Inference | If later promoted, Hascup resting ~µM vs Herman nM, Okubo extrasynaptic 1–8 µM / tens of ms, Yang (glutamate as hard SELEX amino acid), Latham folding-limited apparent kon (not Glu), Aggarwal iGluSnFR4 clocks could change which biological pole the poster uses. **Not promoted.** |
| New claims | None in `claims.csv`. |
| Weakened | Would weaken uniqueness of Herman 25 nM as “the” basal if Hascup were later treated as interchangeable (it is not: different method/compartment). |
| Traceability | Candidates with free-route locators; nothing core. |
| Conflation | Highest risk is treating Hascup MEA resting µM and Herman NMDAR nM as one `biological_concentration_range`. |
| Gate | No. |
| Stale canonical | No. |
| Unresolved | Whether any of the five “story-changing” candidates survive extraction/audit. |
| **Rec** | **hold** (Mission 2 exploration). |

### #18 [Opposing-case evidence for glutamate aptamer biosensors](https://github.com/bobshenruililin/BIOC1600-1/pull/18)

Draft. `rounds/goal-wave-a/opposing-case.md`. Proposed claim rows for orchestrator adjudication, **not auto-promoted**.

| Q | Answer |
| --- | --- |
| Inference | Strongest limiter may be **identity of extracellular glutamate** (neuronal vs total), not speed. Hershey 2025 (O1) is the load-bearing new primary the report nominates. Would be a framing challenger if later accepted — not a Mission 1 title swap in this close. |
| New claims | Proposed OC-rows in the report only. |
| Weakened | Would weaken “measure total free Glu at Herman’s 25 nM and you have the neurotransmitter.” Does not weaken S066 clocks. |
| Traceability | O1 full text claimed inspected (PMC12418293). Hascup 2008 (O9) `full_text_inspected=no` in the report table. Proposed numbers must not enter `claims.csv` without independent extraction. |
| Conflation | Microdialysis total/neuronal split is not an aptamer-electrode measurement (architecture transfer). |
| Gate | No. |
| Stale canonical | No. |
| Unresolved | Citation audit of Hershey/Hascup; whether identity-vs-speed displaces two-regime matching. |
| **Rec** | **hold** + **human-review** before any ledger promotion. Mission 2 exploration. |

### #19 [Replace occupancy/kinetics as flagship (Wave A adversarial review)](https://github.com/bobshenruililin/BIOC1600-1/pull/19)

Draft. `rounds/goal-wave-a/occupancy-challenge.md` only. Diff at this writing: +347 / 1 file (initial review `03799ea8`, follow-up `506d75ec` “Record that occupancy withdrawal keeps revised D as REVISE”). Does **not** edit `state/gates/science_story.json`, accepted analysis code, `poster/theses.md`, scoreboard, or nightly.

**Do not adopt its “REPLACE occupancy” call as a gate decision.** The follow-up commit still does **not** change the REVISE gate. Mission 1 already demoted the 1.8 nM tissue-occupancy overlay and kept the 81-fold 1:1 identity (C027) as flagship *computation*, with occupancy table remaining SIMULATION/BOUND. A Wave A critique cannot flip that JSON from this close.

| Q | Answer |
| --- | --- |
| Inference | If someone treated the PR title as a decision: occupancy/kinetics would stop being flagship; atlas-only interim; working-range-vs-poles nominated. **That is not a science-story gate change.** Follow-up text: occupancy withdrawal keeps revised D as a **REVISE** recommendation and is not enough for PASS. |
| New claims | None in `claims.csv`. Rebuild pass and 12/12 table recompute are code checks, not new wet-lab numbers. |
| Weakened | Weakens occupancy.svg θ(25 nM)=0.933 and `test_hu_saturated_at_tonic` as a scientific result; weakens C008/C010 sensitivity punchline as a glutamate bound; weakens 81-fold as a claim about **Hu’s** LF sensor until n is reported. Does not weaken C006/C028/C031. Aligns with already-withdrawn occupancy-at-basal. |
| Traceability | Re-reads Hu OA / Ricci PMC; n absence is a negative search, not a fitted n. |
| Conflation | The critique’s target *is* conflation (LF→1:1, chip→probe, foreign kon). Replacement analysis (working-range bars vs Herman/Clements ticks) is not implemented in this PR. |
| Gate | **No, including after the follow-up.** `science_story.json` unchanged. Do not read REPLACE as PASS, FAIL, or a new `recommended_thesis_id`. |
| Stale canonical | Not edited. Title/body must not be used to rewrite T1 or D into `poster/theses.md`. |
| Unresolved | n; whether 81 vs 44,000 remains licensed for this device; Probe 3; paired isotherm. |
| **Rec** | **hold**. Do not merge. Mission 2 exploration, not Mission 1 close. |

### #20 [Hold rationale for occupancy-challenge PR 19](https://github.com/bobshenruililin/BIOC1600-1/pull/20)

Draft. `reports/pr_policy/pr-19-occupancy-challenge.md`. Coordinator documentation of the eight questions for #19 only. Not a science lane.

| Q | Answer |
| --- | --- |
| Inference | None beyond parking a hold note. Explicitly: merging a `rounds/` critique is not a flagship swap. |
| New claims | None in `claims.csv`. |
| Weakened | None. |
| Traceability | No new numbers. |
| Conflation | None. |
| Gate | **No.** |
| Stale canonical | No. |
| Unresolved | Same as #19. |
| **Rec** | **hold**. Do not merge as a science close. |

### #21 [39-mer construct genealogy](https://github.com/bobshenruililin/BIOC1600-1/pull/21)

Draft. `rounds/goal-wave-a/construct-genealogy.md` only (+277). Gates, theses, ledgers, nightly, scoreboard **not** edited.

**Do not treat its sequence facts as ledger promotions.** Report-local H1–H4 cards stay in `rounds/` until independent extraction + citation audit write `state/claims.csv` / `state/sources.csv`.

PR body (already on the PR, not re-derived here): Wu 2022 ESM (OA Word SI) identifies the Hu tissue Fc-thiol oligo as truncated `glu1`; abstract `Kd` 12 µM stays on 98-nt `glu1d04`/`1d04`; the load-bearing illegal transfer is Hu’s methods line that writes that 12 µM onto the 39-mer; paired isotherm remains the recorded next experiment; Wu VoR remains closed.

| Q | Answer |
| --- | --- |
| Inference | If later promoted: construct panel can say tissue DNA **is** Wu `glu1`, and 12 µM attaches to the 98-nt isolate, not the 39-mer. Occupancy-at-basal stays unmeasured. Next experiment in the gate JSON stays the paired 39-mer isotherm (report argues it is still highest-information). **Not a title swap and not PASS.** |
| New claims | Report-local sequence/construct cards only. **Not** `claims.csv` rows. Do not copy sequences or packing arithmetic into the ledger from this PR. |
| Weakened | Weakens “open Wu VoR to learn the truncation cut” as a substitute experiment. Does not weaken C021 (12 µM is a citation). Does not fill 39-mer `Kd_molecular`. Xiao SI sequence still not retrieved — lineage vs Wu remains unknown. |
| Traceability | Sequences claimed from Wu ESM OA `.docx` + Hu VoR/thesis. VoR HTML still closed (`full_text_inspected=no` for S001 VoR). TrAC `32 ± 8 mM` inspected in the report and **rejected** as Wu’s Kd. Packing ~17× (thesis vs ESM densities) is report arithmetic, not a ledger quantity. |
| Conflation | File’s job is to un-collapse H1 (98-nt) / H2 (Wu glu1/MCH) / H3 (Hu MEA) / H4 (PaC probe). Risk if a later editor pastes H2 selectivity (Asp/GABA in 10 mM PBS) onto the retina probe (C032 already: Asp/Gln absent). |
| Gate | **No.** `science_story.json` not in the diff. REVISE unchanged. Do not auto-update `next_experiment` from this PR (the string is already the paired isotherm). |
| Stale canonical | No. |
| Unresolved | 39-mer solution `Kd_molecular`; LF n; PaC-probe isotherm; glu2/glu3 function; Xiao Table S1; C007; occupancy-at-basal. |
| **Rec** | **hold**. Do not merge. Mission 2 exploration. Sequence facts stay parked, not promoted. |

### #23 [A3 draft: working-range bars vs biological poles](https://github.com/bobshenruililin/BIOC1600-1/pull/23)

Draft. Branch `cursor/analysis-working-range-634f`. Isolated A3 implementation under `analysis/working_range/` (+1104 / 12 files, including a hook in `tests/test_analyses.py`). **Not** copied into `analysis/accepted/`. Gates, theses, nightly, scoreboard, claims, hash-locked files **not** edited.

**Mission 2 analysis draft. Hold. Do not merge. Do not treat as Mission 1 close or a gate change.**

PR body already states: no automatic C vs D swap; glu1 ceiling 25-fold below 25 nM and Abrantes (preprint) 2500-fold below 25 nM; Xiao 100 nM vs 1.1 mM is **11000-fold**, not the proposal’s 11-fold; Ames/Hu MEA 10 µM ceilings contain 25 nM and sit 110-fold below 1.1 mM; PaC PBS 1 nM–1 mM is E044 **comparator** text; no plotted bar contains both poles; 0.3 pM is PBS LOD not Ames. Occupancy θ is not plotted. Folds labeled SIMULATION / computational illustration.

| Q | Answer |
| --- | --- |
| Inference | If later *accepted* as flagship, nightly §6 would gain a working-range-vs-poles glyph. **This PR does not perform that swap.** Draft itself: A3 does **not** force C over revised D; Ames contains 25 nM, so the tissue-device title stays D’s two-regime/clocks frame unless a human reframes Topic 1 as the ultrasensitive-calibration contest. |
| New claims | None in `claims.csv`. Fold-below ratios are `computational illustration` on existing ledger spans (E003, E041, E026, E007, E044) vs C012/C011 ticks. Corrects PR #11 proposal arithmetic (Xiao 11-fold → 11000-fold). |
| Weakened | Weakens “A3 can swap C vs D” as an automatic result. Weakens the proposal’s “PBS contains 1.1 mM” (SI-strict: 1 mM does not contain 1.1 mM). Does not revive occupancy-at-basal (θ not computed). Does not weaken C006/C028/C031. |
| Traceability | Bars copied from `research/evidence/core_evidence.csv`. PaC PBS bar is comparator text, not a dedicated `analytical_working_range` `numerical_result` — labeled as such. Wu/Abrantes spans remain abstract/preprint. Herman/Clements still hippocampal literature. |
| Conflation | Quantity types are separated on-figure (`analytical_working_range` vs `biological_concentration_range` vs `EC50` vs `sensor_LOD`). Residual labeled hop: hippocampal poles drawn on Glu-apt calibrations (`transferable=no` in limitations). Ames LOD cell left empty (E043 is PBS). Does not plot Hu 1.8 nM. |
| Gate | **No.** `science_story.json` not in the diff. REVISE unchanged. Not Mission 1 close. |
| Stale canonical | Does not edit `poster/theses.md`, `state/scoreboard.json`, or nightly. Would make nightly §6 stale *only if* a human later promoted it into `analysis/accepted/` — that promotion is not this PR. |
| Unresolved | C vs D as title; whether Clements 1.1 mM is the right-hand pole for a retina electrode; Wu VoR spans; Ames LOD; occupancy-at-basal still unmeasured. |
| **Rec** | **hold**. Mission 2 analysis draft. Do not merge. Not a gate decision. |

### #24 [A4 interrogation Nyquist (draft analysis, not Mission 1 close)](https://github.com/bobshenruililin/BIOC1600-1/pull/24)

Draft. Branch `cursor/analysis-nyquist-634f`. Isolated A4 implementation (+1100 / 18 files). Package: `analysis/accepted/interrogation_nyquist/`. Also adds `analysis/accepted/figures/nyquist.svg` and **hooks `analysis/accepted/rebuild.sh`**. Gates, theses, nightly, scoreboard, claims, hash-locked files **not** edited.

**Mission 2 analysis draft. Hold. Do not merge. Do not treat as Mission 1 close or a gate change.**

Unlike #23, a merge would land inside the **accepted** analysis tree. That is still not a science-story PASS. It is an extra reason to hold until a human decides flagship packaging.

PR body already states: 14 s interrogation (E045) and ~1 min sampling (E046) cannot reconstruct a Clements-like 1.2 ms literature stimulus even if occupancy tracked it instantly; authors already refuse synaptic transients (C031); clock ratios 11,667 and 50,000 are dimensionless T/τ, **not** koff; C007 stays empty; caption does not say “the aptamer is too slow.” Highest-information experiment *from this figure* is fast interrogation on a known millisecond [Glu](t), **or** locking a basal/graded spec — that must not auto-replace the gate JSON’s paired-isotherm `next_experiment`.

| Q | Answer |
| --- | --- |
| Inference | If merged as accepted analysis: a Nyquist/two-clock glyph would sit beside atlas/occupancy. **Does not close Mission 1.** Could later reframe “too slow” as architecture/interrogation rather than missing koff — Mission 1 already refuses koff ≈ 1/τ_cleft. Do not treat merge as adopting A4’s next-experiment fork. |
| New claims | None in `claims.csv`. Ratios 14 s / 1.2 ms and 60 s / 1.2 ms are `computational illustration` on C031 vs C011. Nyquist τ/2 = 0.6 ms is labeled a sketch (exponential is not band-limited). |
| Weakened | Weakens “fill C007 and the cleft column opens on this ACV.” Does not weaken C031 authors’ basal/not-transients sentence. Does not revive occupancy-at-basal. |
| Traceability | Ledger pins E032–E034, E045–E046, E008, E042, C011/C012/C031/C006/C028/C007. No invented glutamate kon/koff. Rectangular-window mean kept in tests only (not SVG). 25 µm electrode diameter unused (not a ledger number). |
| Conflation | Quantity types separated: literature stimulus vs interrogation vs sampling vs incubation (15 min / 10 min off-figure). Residual labeled hop: hippocampal 1.2 ms waveform as a “literature stimulus” on a retina ACV (`transferable` unknown; Clements abstract-only). IPA/GlutOx off-figure except footnote. |
| Gate | **No.** `science_story.json` not in the diff. REVISE unchanged. Not Mission 1 close. Do not auto-edit `next_experiment`. |
| Stale canonical | Does not edit `poster/theses.md`, scoreboard, or nightly. **Would** change `analysis/accepted/README.md`, `figures/README.md`, and `rebuild.sh` if merged — accepted-tree staleness, not a gate flip. |
| Unresolved | Whether Topic 1’s right-hand spec is a 1.2 ms cleft waveform; C007; occupancy-at-basal; gate next experiment remains the paired 39-mer isotherm until a human says otherwise. |
| **Rec** | **hold**. Mission 2 analysis draft. Do not merge. Not a gate decision. |

### #25 [identity-inference / architecture-transfer critique](https://github.com/bobshenruililin/BIOC1600-1/pull/25)

Draft. Branch `cursor/identity-inference-critique-bb84`. One file: `rounds/goal-wave-a/identity-inference-critique.md`. No ledger writes, no hash-locked edits, no poster, no `science_story.json`.

**Wave C architecture-transfer critique (PR titles itself Goal Wave A). Not Mission 1 close. Hold. Do not merge. Do not change the gate.**

Assigned question already on that PR: does Hershey/Kennedy 2025 imply a glutamate DNA-aptamer reports the *wrong quantity*, so speed cannot fix usefulness? Report verdict **QUALIFY** (keep operational form; reject the strong form). Hascup 2010 is named as a total-glutamate GluOx counterexample. Replacement limiter (sampling volume vs release domain) and h\* depletion arithmetic stay parked — not `claims.csv` rows.

| Q | Answer |
| --- | --- |
| Inference | Would *qualify* #18’s “wrong quantity” challenger rather than install it. Does not retitle Mission 1. Does not flip REVISE. |
| New claims | None in `claims.csv`. |
| Weakened | Weakens #18’s strong form (any architecture reports the wrong quantity). Does not weaken C031 clocks or occupancy-withdrawal. |
| Traceability | Critique of a specified inference; proposed numbers stay in `rounds/`. h\* wildcard is computational illustration if later used. |
| Conflation | Load-bearing point is microdialysis ≠ aptamer electrode. Do not treat Hascup GluOx as proof an aptamer sees the neuronal pool. |
| Gate | **No.** |
| Stale canonical | No. |
| Unresolved | Whether identity-vs-speed displaces two-regime matching; citation audit of Hershey/Hascup/#18; gate `next_experiment` remains the paired 39-mer isotherm. |
| **Rec** | **hold**. Wave C critique. Do not merge. Not Mission 1 close. Not a gate decision. |

---

## 10. Mission 2 exploration vs Mission 1 close

| Bucket | PRs | Role in this close |
| --- | --- | --- |
| Mission 1 already on `main` | #4 (story tournament REVISE), #5 (scheduling) | Canonical science-story record |
| Overnight occupancy still on `main` | thesis files from earlier merges | T1 still poster-facing until a human chooses |
| Short snapshot (do not duplicate) | [#22](https://github.com/bobshenruililin/BIOC1600-1/pull/22) `reports/mission1_close_status.md` | Status only |
| This package | this file | Full close + eight-question table #6–#21, #23–#25; no gate edit |
| Mission 2 exploration (do not merge as close) | #6–#21 | Wave A reports, duplicate Round 1 scouts, analysis *proposals*, occupancy *critique*, 39-mer genealogy |
| Process note for #19 | #20 | Hold rationale; not a science result |
| Mission 2 analysis drafts | [#23](https://github.com/bobshenruililin/BIOC1600-1/pull/23), [#24](https://github.com/bobshenruililin/BIOC1600-1/pull/24) | A3 working-range (not accepted/); A4 Nyquist (writes under accepted/); not close |
| Wave C critique | [#25](https://github.com/bobshenruililin/BIOC1600-1/pull/25) | Architecture-transfer vs “wrong quantity”; not close |

Hash-locked files (`state/LOCKED_FILES.sha256`) were not edited. Hashes re-checked while writing this package; they match.

No polished poster.

---

## Scribe checklist (this package)

- [x] `science_story` = REVISE  
- [x] `group_final` = false  
- [x] T1 vs `D_revised` split left for humans  
- [x] Stale files listed, not silently rewritten  
- [x] Claims copied, not invented  
- [x] Opus path given; no new consensus score  
- [x] Grok as-submitted disagreement recorded; after revisions D is the title; still REVISE  
- [x] PRs #6–#25 held; #19 REPLACE is not a gate decision; #21 sequences are not ledger promotions; #23/#24 Mission 2 analysis drafts; #25 Wave C critique not close  
- [x] Mission 2 not started  
- [x] Snapshot left in PR #22; not duplicated here  

**Mission 1 cannot PASS from this package; it can only be closed as REVISE pending human choice.**
