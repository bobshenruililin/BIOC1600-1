# Mission 1 — Scientific story tournament

Not a finished poster. Not group-final. Gate: **REVISE**.

Date: 2026-09-11. Branch: `cursor/story-tournament-634f`.  
Blind senior review: Opus 5 (`bc-35465731-9331-54fd-b508-ca3af59e84ec`), saved at `research/reviews/premium/opus_story_gate.md`.  
Prior overnight T1–T5 scores were **not** averaged into this ranking.

## Verdict

**Recommended title (revised D).** There is no generic glutamate-aptamer sensor. Neurochemistry is two regimes (Herman’s baseline plus superimposed transients). A 1:1 Langmuir site spans exactly 81-fold between 10% and 90% occupancy, while those literature concentrations span ~44,000-fold. The only neural-tissue Glu-apt experiment (Hu thesis S066) is already clock-limited to basal/slow sampling. Occupancy at that basal on the parylene-C probe in Ames or tissue is **unmeasured**, not shown saturated. Millisecond cleft reporting is **untested** — missing `koff` does not prove a millimolar rising edge is impossible.

**Runner-up (C, as a panel).** Ultrasensitive working-range ceilings miss Herman ~25 nM from above (Wu glu1 top 1 nM; Abrantes preprint 10 pM). Hu 32 pM is legitimate matrix-matched LOD and must not be binned with Wu 0.0013 pM or Abrantes 1 aM.

**B** survives as a construct×quantity key, not as the title. **A** fails as a title (IUPAC tautology); its same-oligo four-grade table survives as teaching. **W1** (Glu vs Asp/Gln) is a real gap (C032) and not a fifth thesis.

The science-story gate does **not** pass: the occupancy half of unrevised D is not primary, Probe 3 is gold-confounded, Herman/Clements are hippocampal transfers onto a retina experiment, and the 1:1 overlay of Hu’s Langmuir–Freundlich 1.8 nM is a double hop (isotherm type and device).

---

## 1. Four candidates (orchestrator dossiers)

| ID | Title as submitted | Trio verdicts | Opus score / title call |
|---|---|---|---|
| A | Fit for a named neurochemical task | Steelman KEEP sharpened; red REVISE slogan; independent: slogan too weak / field’s alibi | 68 FAIL as title |
| B | Construct non-identity (not a transformation mechanism) | Steelman/independent KEEP as non-identity; red FAIL as strongest story | 73 FAIL as title (KEEP as panel) |
| C | LOD is not usefulness; occupancy at ambient is the paradox | Steelman KEEP sharpened (saturation / range-in-matrix); red REVISE slogan; independent: occupancy at ambient | 77 REVISE |
| D | Two biological regimes, not a generic glutamate sensor | Steelman KEEP two regimes; red REVISE “three problems”; independent: occupancy at basal | 85 KEEP title **conditional on revisions** |

Dossiers: `rounds/mission1/candidates/{A,B,C,D}.md`. Lane notes: `rounds/mission1/sealed/`.

Abrantes millimolar ELONA Kd was **not** entered. Tokens `10.3` / `25.1` remain funder IDs. Some isolated agents re-claimed millimolar ELONA from preprint HTML; those rows were not promoted.

---

## 2. Opus 5 ranking (blind)

Full text: `research/reviews/premium/opus_story_gate.md`.

| Criterion (weight) | A | B | C | D |
|---|---:|---:|---:|---:|
| primary-evidence strength (25) | 17 | 19 | 19 | 20 |
| BIOC1600 biochemical depth (15) | 9 | 12 | 10 | 13 |
| critical insight (15) | 11 | 10 | 13 | 14 |
| reproducibility (15) | 11 | 14 | 13 | 12 |
| central-question relevance (10) | 8 | 5 | 7 | 10 |
| visual explanatory power (10) | 7 | 6 | 8 | 8 |
| Tanner intellectual alignment (5) | 3 | 5 | 4 | 4 |
| novelty without overclaiming (5) | 2 | 2 | 3 | 4 |
| **Total** | **68** | **73** | **77** | **85** |

Opus: D is materially stronger because it is a claim about the world, not a rule about numbers; 81-fold vs 44,000-fold is the computation that *is* the argument; three of four dossiers’ own red teams already point at occupancy and clocks. Gate **REVISE** because D’s occupancy half is a 1:1 overlay of an LF EC50 from a different device plus Probe 3, which the thesis attributes to detached gold.

Method note: Opus reported `.cursor/rules/safety-and-integrity.mdc` missing; the file is present and hash-locked. Constitution and rubric were read. Forbidden T1–T5 / scoreboard files were not opened.

---

## 3. Grok post-review (adversarial synthesis)

Agents: `bc-3aa253b4` (attack Opus), `bc-55b3484f` (steelman revised D). No vote. Notes: `rounds/mission1/synthesis/`.

**Agreement with Opus.** Gate stays REVISE. A fails as title. B is a panel, not the title. W1 is not a fifth title. C’s strong form (“you cannot see 25 nM without aM LOD”) is false for Hu 32 pM. Missing `koff` does not prove a millimolar rising edge is impossible. Do not score Hu retina as a failed hippocampal-cleft sensor.

**Disagreement with Opus.** The submitted D dossier is **not** materially stronger than C. The 85 KEEP scores occupancy-as-demonstrated and then withdraws it in the gate list — internally inconsistent. Probes 1–2 still change with light (`primary-source-supported`, S066 §6.3): remaining dynamic range at whatever the retinal basal is, not saturation. 81-fold is a 1:1 identity; Hu fitted Langmuir–Freundlich and **n is unknown**, so 10–90% is 81^(1/n), not 81, for this sensor. Herman 25 nM and Clements 1.1 mM / 1.2 ms are hippocampal literature, not this retina experiment’s spec. A already names Herman’s 1.8 µM NMDAR EC50 (E035); uniqueness of that trap is false. B was under-scored on primary-evidence density, still correctly killed as title.

**As submitted:** C and D are a dead heat or C slightly ahead (C’s distinctive exhibit does not need Probe 3).  
**After named revisions:** D is the course title; C and B are supporting panels.

Revised D self-score 89 is a synthesizer’s integer on the locked rubric. It is **not** a second Opus pass and does **not** convert REVISE into PASS.

---

## 4. Recommended thesis (revised D)

One sentence in the Verdict. Load-bearing, tagged:

1. Herman: transients superimposed on a low baseline — two components, not three (`primary-source-supported`, C012 / S050).
2. 1:1 Langmuir 10–90% span is exactly 81-fold (`computational illustration` / `review-supported`, C027). 25 nM → 1.1 mM is ~44,000-fold (`computational illustration` on C012 and C011).
3. S066 clocks are basal/slow by the authors: 14 s/scan, ~1 min/point, 10 min plateau after 10 nM, journal 15 min wait (`primary-source-supported`, C006, C028, C031).
4. Occupancy at basal on the **PaC probe in Ames/tissue is unmeasured**. The probe has no reported apparent Kd. Overlay θ(25 nM)≈0.93 is a 1:1 overlay of an AuED-MEA Langmuir–Freundlich 1.8 nM (`computational illustration`; C005 is a different device).
5. Probe 3 is author-flagged failure with gold-nanostructure detachment (Fig. 6.16) that can mimic early saturation (`primary-source-supported` as failure analysis; occupancy reading `unresolved`).
6. No glutamate aptamer `kon`/`koff` (C007, `unresolved`). τ_eq at 1.1 mM can still be short (`computational illustration`). Do not quote koff ≈ 1/1.2 ms.
7. Glu vs Asp/Gln is a named open FoM, not a title (C032, W1 REJECT).

**Must print on-panel, not only in captions:** quantity type and device; GCL/IPL-border electrode vs photoreceptor-terminal narrative; Herman = hippocampal slice; Clements = cultured hippocampal inference, abstract-only; 0.3 pM = PBS blank+3 RSD, not Ames, lowest calibrant 1 nM.

---

## 5. Runner-up and why it is not the title

**C.** Ceiling-from-above is the sharpest previously unstated ledger observation and belongs on the poster. After C’s strong LOD form is deleted, what remains is occupancy/working-range/clocks — D’s content, arrived at from the LOD side. Hu 32/51.5 pM is real antifouling chemistry.

**B** loses as title because Hu already wrote the 2D-confinement caveat, DA 49.6 µM ≈ cited 44 µM in the same LF panel, and the truncated 39-mer has no solution Kd. It wins as the empty-cell construct×quantity table.

**A** loses because “fit for purpose” cannot be wrong. Its repaired form is revised D.

---

## 6. Unresolved disagreements

| Item | Positions | Status |
|---|---|---|
| Probe 3 | Occupancy ceiling (unrevised D, H2) vs gold loss (thesis Fig. 6.16, C, Opus) vs both | `unresolved`. Probes 1–2 still modulate. |
| 1:1 overlay of 1.8 nM | Ontology: stop selecting as canonical occupancy. A/C/D dossiers still draw it with captions. | Draw only as a sensitivity band across 1.8 nM–12 µM, or drop. |
| Non-transfer as a law | B steelman near-universal; B red team: sequence and Au–thiol can transfer; DA near-match | Hygiene, not a physical law. |
| Middle extrasynaptic band | D: tool-class/clock artifact; A would allow it as a task; Moussawi 0.02–30 µM review span | `unresolved` as a design spec. |
| H2 vs C031 | H2: Ch.7 sub-second sentence load-bearing; C031 over-ranks S066 | S066 is the strongest Glu-apt neural-tissue experiment **and** a device-level feasibility result, not a chemical identification. |
| Layer (GCL/IPL vs photoreceptors) | H2/H3 flag; A–D originally silent | Must be an on-panel bracket. |
| Opus 85 vs Grok “not materially stronger as submitted” | Structural vs scorekeeping | **Both recorded.** Gate uses the stricter reading: occupancy not primary. |
| Ames L-glutamine | Public A1420 0.073 g/L ≈ 0.5 mM arithmetic; Hu Appendix II not re-read as A1420 | `unresolved` vendor identity; no interference measurement. Fold at Ames top (10 µM) is 50×, not 10⁵. |

---

## 7. Reversing evidence

- Paired solution and surface isotherm of the exact Fc-thiol 39-mer near **12 µM** → θ(25 nM) tiny, “saturated at basal” arithmetically dead, **C rises**.
- Same pair near **1.8 nM** → confinement becomes a result, **B rises** relative to its ceiling.
- Pharmacology + scrambled aptamer identifies the retina ACV change as glutamate → “device already works at basal” becomes primary; A gains a positive case; title stays D’s two-regime frame.
- Measured Glu-apt `koff` fast at a µM-scale Kd → cleft column flips from untested toward architecture/interrogation-clock story.
- Large Asp/Gln cross-reactivity at Ames-realistic concentrations → W1 content becomes load-bearing inside every title.

---

## 8. Five highest-value unknowns

1. Is 1.8 nM affinity or interface/transduction? Paired solution + surface Kd of the 39-mer, Langmuir and LF, exponent *n*, coverage. `proposed experiment`
2. Is the retina ACV chemically glutamate? TTX, CNQX/AP5, TBOA, scrambled-aptamer probe. `proposed experiment`
3. Glutamate aptamer `kon`/`koff` on the 39-mer (IPA/SPR, controlled mass transport). `unresolved` / `proposed experiment`
4. Glu vs Asp/Gln/GABA signal-gain on that oligo in PBS and Ames. `unresolved`
5. Probe 3: occupancy vs lost gold (ESA, 1 kHz Z, coverage before/after insertion). `unresolved`

---

## 9. Flagship analysis

**Keep:** 81-fold 1:1 identity (C027) as a fixed-width band against labeled Herman 25 nM and Clements 1.1 mM. No aptamer number enters.

**Demote:** θ curves anchored on Hu 1.8 nM as tissue occupancy. Honest redraw: sensitivity band θ(25 nM) from 1.8 nM to 12 µM showing the occupancy verdict is undetermined by four orders of magnitude.

**Clocks:** two-clock retina panel (millisecond spikes vs ~1 min ACV), not one log axis mixing biological τ, bound t_off, incubation, interrogation, and sampling.

**Atlas:** supporting Panel B. Empty glutamate kon/koff cells stay empty.

Occupancy table remains SIMULATION/BOUND.

---

## 10. Next experiment

`proposed experiment`: measure Hu’s exact Fc/thiol 39-mer twice, one buffer, one construct — solution `Kd_molecular` (ITC or fluorescence) and surface ACV apparent Kd (Langmuir and Langmuir–Freundlich, report *n*), with achieved coverage.

Not a lower LOD. If the biological question is retinal glutamate rather than sensor fitness, substitute pharmacological identity (unknown 2). Do not do both and report neither.

---

## 11. Hu retina (H1–H3 consensus)

Thesis S066, **in vitro** isolated mouse retina, not journal MEA S002, not in vivo.

**Answered:** Can a PaC-shank Fc-Glu-apt E-AB at the GCL/IPL border report a reversible, light-dependent, minutes-scale extracellular-Glu occupancy *proxy* on the same implant that records light-responsive RGC-like spikes? Yes for Probes 1–2.

**Not answered:** how much glutamate; how fast; chemical identity (no TTX/CNQX/TBOA); which pool (electrode vs photoreceptor narrative); Asp/Gln selectivity; why Probe 3/4 fail (saturation vs gold loss). Fig. 6.5 body 10 nM vs caption 100 nM: record both.

---

## 12. Quantity ontology (O1/O2)

Closed ten-type schema forces Clements τ into `response_time`, incubation/interrogation/sampling into `measurement_time`, Hu cited 12 µM into `Kd_molecular`, 81-fold into `analytical_working_range`. Live notes usually split objects; selected occupancy/sensitivity glyphs still collapse them. See `research/evidence/quantity_ontology.md`. Schema extension is **not** this gate; it is a later hygiene pass.

---

## 13. Science-story gate (five bullets)

| Bullet | Result |
|---|---|
| One thesis materially stronger | **Partial.** After revision, D is the title. As submitted, Grok adversarial: not materially stronger than C. |
| Load-bearing claims have primary evidence | **No.** Clocks yes. Occupancy-at-basal as a result no. Cleft concentrations are hippocampal inference. |
| Survives counterevidence | **Partial after revision** (gold loss and layer tension now explicit). Unrevised D: no. |
| Fits one poster | **Yes, conditionally** — quantity type and device in axis labels; θ=0.93 not the main glyph. |
| Computation answers the thesis | **Qualified yes** — 81-fold identity does. 1.8 nM overlay does not. |

**Status: REVISE.** File: `state/gates/science_story.json`.

---

## 14. Before closing a major mission

**What did we believe before?** Overnight T1 (cannot jointly claim neurodynamics) vs T5 (µM isolate empty at 25 nM; Hu 1.8 nM saturated / slow) were both provisional and inverted across scoring stacks. Provisional user thesis: analytical sensitivity is not biological fitness.

**What changed?** Four isolated programs plus Hu reconstruction plus ontology plus wildcard. Blind Opus and Grok adversarial agree the **gate is REVISE**. The teachable story is two regimes + 81-fold identity + measured S066 clocks, with occupancy-at-basal **withdrawn as a finding**. Fit-for-purpose and “LOD distracts” fail as titles. Construct transformation fails as a mechanism (Hu already wrote it; DA does not move). Asp/Gln is a hole, not a fifth thesis.

**What surprised us?** (1) DA 49.6 vs 44 µM in the same LF panel as Glu 1.8 nM vs cited 12 µM. (2) Probes 1–2 still modulate — the occupancy-failure sentence fights the successful probes. (3) Wu/Abrantes working-range ceilings sit **below** Herman 25 nM. (4) Ricci 2016, Hu’s LF neighborhood citation, is a 1:1 Langmuir Account, not an LF paper. (5) Some agents re-harvested Abrantes 10.3–25.1 mM; those remain funder IDs.

**Tested and rejected.** A as title; B as title/mechanism; C’s strong LOD form; D’s three-regime form; D’s occupancy-saturation-as-measured; W1 as fifth title; koff ≈ 1/τ_cleft; T1 as group-final (human still chooses; this mission does not close that).

**Important uncertainty.** 39-mer solution vs surface Kd; chemical identity of S066 ACV; Glu `kon`/`koff`; Probe 3 mechanism; electrode layer vs photoreceptor pool; Ames Gln interference.

**What most threatens the preferred thesis?** A paired 39-mer isotherm near 12 µM, or pharmacology that the light-off ACV increase is not glutamate.

**What most strengthens it?** Author-owned S066 clocks; Herman’s two-component sentence; 81-fold identity needing no aptamer number; empty Glu kon/koff cell.

**Highest-information next action.** Paired 39-mer solution/surface isotherm (or, if the question is retina biology, pharmacological identity).

**Work not done, judged low value.** Docking/InstructNA; MacDonald/Ohsawa archaeology; another LOD contest; polished poster; schema migration of `validate_ledgers.py` this round.

**Would another round change a decision?** Yes for gate PASS: it requires either a PaC-probe isotherm or an explicit poster that occupancy is unknown. Another isolated slogan tournament without those measurements is low value.

---

## Isolation and concurrency record

Eighteen intended lanes. Runtime async cap 10 caused first-wave misses; those were relaunched. Policy: max 8 concurrent delegated agents (`AGENTS.md`). Launch errors were not treated as empty searches. Wave 2 (H1, W1) did not see program theses. Opus did not see Grok A–D ranking or T1–T5 scoreboard.

No polished poster. Hash-locked constitution, rubric, and safety files were not modified.
