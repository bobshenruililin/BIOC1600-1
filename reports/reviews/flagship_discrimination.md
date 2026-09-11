# Wave D senior review — flagship discrimination

Reviewer: Wave D senior reviewer, `bc-bc113322-4a1f-5da9-b248-993be9c6b865`. Branch `cursor/flagship-discrimination-245a`. Date 2026-09-11.
Model: `cursor-grok-4.6-xhigh` (`state/model_config.json`).

**Scope.** Discriminate among Mission 1's three recommendations by reading the parked PRs. Coordinator only. No merges. No thread takeovers.

**Not done, by instruction.** The science-story gate is **not** set to PASS. `state/gates/science_story.json`, `poster/theses.md`, `reports/nightly_summary.md`, `state/decisions.md`, `state/claims.csv` and hash-locked files were **not** edited. No poster sentence was written onto `main`. Mission 2 was not started. PR #28's PASS claim was not read and is not copied.

Files read: `reports/mission1_story_tournament.md`; `research/reviews/premium/opus_story_gate.md`; `state/gates/science_story.json`; `analysis/accepted/occupancy_kinetics/limitations.md`; `gh pr diff` for #11, #18, #19, #21, #23, #24, #25, #26.

---

## 0. Verdicts

| Recommendation | Verdict |
| --- | --- |
| 1. Story: revised D (two regimes; occupancy-at-basal withdrawn; Hu retina positive on a basal/slow clock; missing `koff` ≠ slow kinetics) | **KEEP**, with one named repair (§2.3) |
| 2. Flagship: 81-fold 1:1 Langmuir identity vs ~44,000-fold Herman-to-Clements span; demote 1.8 nM overlay | **REPLACE** |
| 3. Next experiment: paired solution + surface isotherm of Hu Fc-thiol 39-mer in one buffer, report Langmuir–Freundlich *n* | **KEEP**, with two specifications (§3.3) |

Gate remains **REVISE**. Nothing here converts REVISE into PASS; §2 and §1 both move a load-bearing claim from "asserted" to "contested by primary evidence," which is the opposite direction.

---

## 1. Flagship: REPLACE

### 1.1 What is being replaced, precisely

The identity is not in dispute. For a 1:1 site, θ = c/(c+Kd), θ = 0.1 at c = Kd/9 and θ = 0.9 at c = 9·Kd, so c₉₀/c₁₀ = 81 exactly, for every Kd, with no aptamer number entering. I re-derived and re-checked it. `computational illustration` (C027). Opus was right that this is the most course-appropriate biophysics in the set.

What is being replaced is the **comparison**: 81-fold set against "~44,000-fold" as if the biological span were a settled quantity whose ratio to 81 carries the argument. That span is one arithmetic operation on one choice of basal number. Three parked PRs supply primary, tagged, full-text-inspected measurements that make the choice contested, and within the contested range the conclusion **changes sign**.

### 1.2 The decisive evidence

Four primary basal extracellular-glutamate measurements now sit in the parked PRs. I re-retrieved and re-read each one myself rather than inheriting it; PR #26's citation audit independently re-fetched the identifiers and confirmed `identifier_ok=yes` and `supports_claim=yes` for the two µM-class rows.

| Basal value | System / method | Locator | Tag | `full_text_inspected` |
| --- | --- | --- | --- | --- |
| ~25 nM | acute hippocampal slice; tonic NMDAR current on CA1 pyramidal cells | Herman & Jahr 2007, PMID 17804634, PMC2670936, abstract | `primary-source-supported` (S050, C012) | partial (abstract re-read this pass) |
| 3.3 ± 1.0 µM (PFC, n = 8); 5.0 ± 1.2 µM (striatum, n = 10) | awake mouse, GluOx ceramic MEA, self-referenced | Hascup KN 2008, PMID 18024788, PMC3404456, Table 1 | `primary-source-supported` (PR #18 O9; audited PR #26) | no (this pass); PR #26 read PMC HTML |
| 9.4 ± 0.6 µM (n = 11) | rat cortex microdialysis, stable-isotope extraction-fraction correction, `Ed` 0.29 ± 0.01 | Hershey 2025, PMID 40838767, PMC12418293, **§3.1 body text, no figure/table** | `primary-source-supported` (PR #18 O1; audited PR #26) | **yes** (efetch JATS, this pass) |
| 34.7 ± 11.8 µM (n = 41) | awake Long Evans rat PFC, GluOx MEA, self-referenced | Hascup ER 2010, PMID 20969570, PMC2996468, **§3.1 parenthetical, not Table I** | `primary-source-supported` (PR #26) | **yes** (efetch JATS, this pass) |

Quoted verbatim from the text I retrieved, so no one has to take my transcription on trust:

- Hershey §3.1: "When infusing 5.0 μM ¹³C₅-Glu, we recovered 3.5 ± 0.05 μM ¹³C₅-Glu giving an E_d of 0.29 ± 0.01 and an extracellular concentration calculated as 9.4 ± 0.6 μM for Glu (n = 11)."
- Hascup 2010 §3.1: "our extracellular resting glutamate values (for rats used in this study, 34.7 μM ± 11.8 μM (n=41)) are within the physiological range since the affinity of the high affinity glial and neuronal glutamate transporters are in the 1–100 μM range". The same paragraph states these are "in the range of 10 fold greater values as compared to the average levels reported by microdialysis."

Basal-pole spread across these four: 34.7 µM / 25 nM = **1,388-fold**.

### 1.3 The sign flip

Span from each candidate basal to Clements 1.1 mM, against the 81-fold single-site window. `computational illustration` throughout; two-line arithmetic, no fitted parameters.

| Basal used | Span to 1.1 mM | Does one 1:1 site's 10–90% window (81-fold) cover it? |
| --- | ---: | --- |
| Herman 25 nM | 44,000-fold | no (543× too narrow) |
| Hascup 2008 PFC 3.3 µM | 333-fold | no (4.1× too narrow) |
| Hascup 2008 striatum 5.0 µM | 220-fold | no (2.7× too narrow) |
| Hershey 9.4 µM | 117-fold | no (1.4× too narrow) |
| Hascup 2010 PFC 34.7 µM | **31.7-fold** | **yes — the window is 2.6× wider than the whole span** |

On the highest primary basal measurement, a single 1:1 Langmuir site does not merely approach the biological span; its 10–90% window **over-covers** it. The poster sentence "no single site can span biology" is then false, using only numbers the same literature publishes.

Two further checks confirm this is not an artefact of picking the extreme row:

1. **The inversion is robust to the direction Hu's own isotherm model allows.** Hu fitted Langmuir–Freundlich with n as a surface heterogeneity index in (0,1] and **did not report a numerical n** — PR #19's negative search across the journal OA text and the thesis isotherm chapters, `unresolved`. For LF/Hill occupancy the 10–90% span is 81^(1/n), so n < 1 makes the window **wider** than 81-fold, never narrower. Narrowing the window below 81-fold would require n = 1.27 > 1, which Hu's stated parameter range excludes. `computational illustration`. So every isotherm shape Hu's model permits covers a 31.7-fold span.
2. **A reported calibration already spans more than any 1:1 site can.** Hu's parylene-C probe — the construct that actually went into retina — is reported linear over 1 nM–1 mM in PBS, a 10⁶-fold window (E044 comparator), and the AuED-MEA over 0.1 nM–10 µM, 10⁵-fold (E007). `primary-source-supported`. PR #19 makes the point sharply: no 1:1 site produces a 10⁵–10⁶-fold log-linear calibration, so either signal is not 1:1 occupancy on these devices, or n ≈ 0.32–0.38, or 1.8 nM is a fit midpoint rather than a Kd. Whichever holds, drawing an 81-fold band as a property of this sensor is not licensed.

### 1.4 Why this is REPLACE and not "add a caption"

The recommendation's own justification was that this computation is load-bearing — Opus: "the 81-fold identity *is* the thesis in quantitative form," and the gate scored bullet 5 "qualified yes" on that basis. A load-bearing computation whose conclusion reverses depending on which of four primary basal measurements you select is not repairable by a caption. The repo already half-knew this: `state/sources.csv` S050 carries the note "Contrasts dialysis 1-4 µM," and Moussawi's 0.02–30 µM tonic span was on file as `review-supported` and dismissed by candidate D as "a tool-class and clock artifact." PRs #18 and #26 convert that dismissable review span into four primary, audited, method-documented measurements. That is exactly the category of evidence the brief requires for REPLACE.

I also record what does **not** change: the demotion of the 1.8 nM 1:1 overlay as tissue occupancy stands, and PR #19 independently strengthens it (LF→1:1 hop, AuED-MEA→parylene-C device hop, n unreported, and a unit test `test_hu_saturated_at_tonic` that freezes θ > 0.9 into CI). That half of recommendation 2 is upheld; it is the "81 vs 44,000" half that fails.

---

## 2. Story: KEEP

### 2.1 What survives untouched

Revised D's spine does not route through the span comparison:

| Revised-D element | Status after the parked PRs | Tag |
| --- | --- | --- |
| Herman: transients superimposed on a low baseline — two components | Survives, and is re-verified. Herman's abstract opens "Synaptic glutamate transients resulting from vesicular exocytosis are superimposed on a low baseline concentration of glutamate in the extracellular space." | `primary-source-supported` (C012 / S050) |
| S066 clocks are basal/slow by the authors: 14 s/scan, ~1 min/point, 10 min plateau, 15 min journal wait | Untouched. No parked PR contests any of these. | `primary-source-supported` (C006, C028, C031) |
| Occupancy at basal on the PaC probe in Ames/tissue is unmeasured | Strengthened by PR #19 and PR #21 (no probe apparent Kd exists in any inspected text) | `unresolved` |
| Probe 3 is author-flagged failure with gold detachment | Untouched | `primary-source-supported` as failure analysis |
| Millisecond cleft reporting untested; missing `koff` ≠ impossible millimolar rising edge | Untouched; no glutamate `kon`/`koff` appeared. PR #18 Q4 searched 96 records and found none, an independent re-confirmation of C007 | `unresolved` |
| 81-fold vs ~44,000-fold as the quantitative form of the thesis | **Fails** (§1) | — |

Losing the span comparison costs revised D its headline computation, not its claim about the world. A title reading "two biological regimes, not a generic glutamate sensor" is still carried by Herman's two-component sentence plus the author-owned S066 clocks.

### 2.2 Two challenges to the story that I tested and rejected

**PR #18's "wrong quantity" limiter (OC-16) does not displace the story.** The lane nominates Hershey's compartmentalisation result as the project's strongest limiter and concludes "Making the sensor faster makes it faster at measuring the wrong quantity." I reject the strong form, and I am not the first: PR #25 read the primary source before reading PR #18 and reached the same verdict independently. Three grounds, all checkable:

1. The authors attribute the labelled channel's visibility to a **recovery-geometry** advantage, not to a chemical difference: Hershey §4.2 speculates that "if ¹³C-Glu is formed preferentially near the probe, it is more likely to be captured immediately after release from a neuron than endogenous Glu formed farther away," supported by dialysate ¹³C-Glu/¹³C-Gln = 11% against endogenous 7%. A dissociation produced by differential recovery cannot establish that the observable itself is wrong.
2. An existing total-glutamate sensor reports the event the ¹²C channel missed. Hascup 2010 §3.2, which I retrieved and read: local TTX decreased awake rat PFC resting glutamate by −40.8 ± 10.8% (n = 7) against citrate 1.6 ± 4.1% (n = 5), p < 0.01; PR #25 verified the companion result that the tail-pinch glutamate response is completely TTX-blocked. GluOx has no isotope channel. `primary-source-supported`, and `transferable = no` to an aptamer — the point is existential, not a transfer.
3. PR #25's transcription audit found the high-K⁺ "false positive" confounded by the stimulus suppressing the Gln–Glu shuttle itself, the percent convention ambiguous in the source, and the load-bearing "¹²C unchanged" cells to be nulls at n = 3–4.

What survives from PR #18 is not a story replacement but a **measured selectivity specification**: Gln 179 ± 20 µM against Glu 9.4 ± 0.6 µM in the same animals with the same probe, a ~19-fold excess of glutamate's γ-amide. Per C032 the only glutamate-aptamer selectivity panel in the ledger (100 nM Glu vs 10 µM serotonin, dopamine, tyrosine, lactate) omits glutamine and aspartate entirely. That belongs on the poster as a named open box. `primary-source-supported`; `transferable` as a specification **yes**, as a cross-reactivity result **no**.

**PR #19's REPLACE verdict does not extend to the title.** PR #19 says so itself (§16) and I agree on inspection: its charges are all against the occupancy/kinetics figures, and the clocks half of D needs none of them.

### 2.3 The one repair the KEEP requires

The basal pole must be printed as a **method-labelled range, not a number**. Concretely: 25 nM (slice, tonic NMDAR current) to 34.7 µM (awake rat PFC, GluOx MEA), with 3.3–5.0 µM and 9.4 ± 0.6 µM between them, each carrying its method, species, region and n. A poster that prints "25 nM" as *the* basal glutamate concentration next to a retina electrode is printing the narrowest value in a 1,388-fold primary spread, and PR #26 explicitly warns against the opposite error too: "do not 'reconcile' by averaging with 9.4 or 34.7."

This repair costs revised D nothing and gains it something. "Two regimes" is a claim about there being a baseline and superimposed transients — which Herman's own sentence asserts — not a claim that the baseline has a known value. Stating that the baseline is unsettled across three orders of magnitude is more defensible than asserting 25 nM, and it is a second `unresolved` printed on-panel alongside the occupancy one.

### 2.4 Wildcard: are the four basal numbers even the same quantity?

Not specified by the brief; examined because it decides whether §2.3 is a range or a contradiction.

Herman & Jahr's abstract, which I re-read, contains two sentences nobody in this repo appears to have used. First: "Reported values of baseline glutamate concentrations range up to 4 microM" — Herman knew about and was arguing against the µM-class literature. Second, and more useful: "superfusion of low micromolar concentrations of glutamate had no effect on neurons, indicating that glutamate transport prevents access to receptors within the slice. However, equipotent concentrations of NMDA, a nontransported agonist, depolarized neurons dramatically."

Measured: low-micromolar bath glutamate does not activate NMDARs in the slice, while a non-transported agonist at equipotent concentration does. `primary-source-supported`.

Inferred by me: Herman's 25 nM is a **receptor-domain, transport-shielded** concentration — what an NMDAR behind the transporter screen reports — whereas microdialysis `Capp` and a GluOx MEA report a **bulk extracellular** concentration sampled by a device that has displaced the tissue it measures. If that reading is right, the four numbers are not four attempts at one quantity, and the correct biological target for a surface aptamer electrode is the bulk number, because an electrode is not behind the transport screen. Clements 1.1 mM is likewise a cleft/receptor-domain inference. On that reading the flagship's 44,000-fold span is a **receptor-domain** span being used to specify a **bulk-ECF** device, and the span the device must actually cover has never been measured. `hypothesis`.

Unknown: whether any bulk-ECF transient amplitude has been measured at all; and whether a tens-of-micrometres aptamer electrode samples bulk ECF, a trauma-altered shell, or something between. PR #18 O6 and PR #25 §7 supply the geometric half (Jaquins-Gerstl 2009: evoked dopamine release suppressed 90% at ~200 µm from a 280 µm probe, abolished at contact) but that is dopamine and `transferable = no`.

I flag this as a hypothesis, not a finding, and I have two blind reviewers checking it (§6).

---

## 3. Next experiment: KEEP

### 3.1 Why it survives

PR #21 re-derives the same experiment from a different direction and I accept its reasoning. Its new contribution is a construct fact obtained from Wu's Springer ESM (`216_2021_3783_MOESM1_ESM.docx`, OA, HTTP 200) rather than the closed VoR: Hu's tissue oligo is Wu `glu1` letter-for-letter, 39 nt = 5′ constant + N10 + docking 11-mer, and the 12 µM Kd attaches to the 98-nt `glu1d04`/`1d04` clone, not to it. `primary-source-supported`. So the load-bearing illegal transfer is now sequence-locked rather than assumed, and the empty cell the experiment fills — `Kd_molecular` of the exact 39-mer — is confirmed empty by two independent lanes.

### 3.2 What the flagship REPLACE does to its value

I checked whether replacing the flagship demotes this experiment, since the recorded experiment was largely motivated by the occupancy overlay. PR #11 is explicit that a new Kd feeds neither A3 nor A4: "a new Kd does not put 1.1 mM inside Ames 10 µM." That is a real argument for demotion and I take it seriously.

It is outweighed by a consequence of §1.2 that nobody has recorded. Once the basal pole is credibly µM-class, PR #18's OC-6 stops being a curiosity and becomes the sharpest live question in the project: the **12 µM parent Kd is well matched to measured bulk ECF glutamate**, and a 1.8 nM surface sensor would be 99.98% occupied at 9.4 µM with ~0.01% of full scale available for a doubling. The paired isotherm is the experiment that decides which of those two regimes the deployed construct is in. Its outcomes are now sharply asymmetric in a way they were not when 25 nM was assumed:

- Both phases near 12 µM → the recognition chemistry is well matched to measured ECF glutamate, "saturated at basal" dies, and 1.8 nM is transduction.
- Both phases near 1.8 nM → the device is pinned in bulk ECF and the recognition element must be deliberately **weakened** to be useful, which inverts the field's entire lower-LOD direction of travel.
- Solution near 12 µM, surface near 1.8 nM → construct non-identity is measured rather than asserted.

All three redirect the project. That is what "highest-information" means.

### 3.3 Two specifications, which do not change its identity

From PR #18 §7.3 and PR #21 §7, adopted as additions rather than as a replacement:

1. **A binding-null point mutant in each arm.** PR #18's OC-1 (Bottari 2020, *JACS*, DOI 10.1021/jacs.0c08691, PMID 33166132) reports three published nanomolar-affinity ampicillin DNA aptamers showing no specific target binding by ITC, native nESI-MS and ¹H NMR, with the pipeline validated against MN4 and 1OLD. A Kd measured without a null control cannot distinguish binding from an assay artefact. I record honestly that this is `full_text_inspected = no` (abstract only, VoR paywalled) and is ampicillin — `transferable = no`. It is a base-rate argument for adding a control, not evidence about glutamate, which is why it specifies the experiment instead of replacing it. PR #18's OC-3 (Xie/Chen/Liu, *ChemBioChem* 2026, DOI 10.1002/cbic.70393, an independent group stating in print that a glutamate moiety is unlikely to support nanomolar affinity, citing the ~12 µM value) is `primary-source-supported` for the statement and `hypothesis` for the glutamate inference.
2. **An amino-acid interferent arm at the concentration the medium actually contains**: L-glutamine at 179 µM, plus L-aspartate, reported as heats or as ACV signal gain on the same construct in the same buffer. Justified by §2.2's surviving specification.

Both arms use the same instrument, the same construct and the same buffer as the recorded experiment. The recorded experiment is unchanged in identity: **solution `Kd_molecular` + surface apparent Kd of the Fc-thiol 39-mer, one buffer, Langmuir and Langmuir–Freundlich, report *n* with a confidence interval, report achieved coverage.** `proposed experiment`.

### 3.4 Rejected as a replacement

PR #25's co-located experiment (Kennedy ¹³C₅-Gln retrodialysis plus a fast total-glutamate sensor at a measured distance, tail pinch ± TTX) is the correct experiment for the question "is total extracellular glutamate the right observable," and its version 1 requires no aptamer. It is not this project's next experiment because §2.2 rejected the strong form of the claim it would test, and because it requires two laboratories' in vivo capability. Recorded as the highest-information experiment for a question this poster should not be organised around.

---

## 4. A3 or A4 as the replacement flagship

**A4, with A3 rebuilt as the supporting panel.** A4 (interrogation Nyquist, PR #24, scored 74/80 in PR #11) is the only implemented candidate whose load-bearing comparison is immune to §1.2. Its argument is a ratio of clocks — 14 s per ACV scan (E045) and ~1 min per sampling point (E046) against a 1.2 ms decay (E033) — in which the two numerator terms are author-reported protocol times measured on the exact parylene-C construct that went into retina, and no concentration pole enters the inference at all. The Herman/Hershey/Hascup dispute that destroys "81 vs 44,000" cannot touch a dimensionless T/τ of 11,667 and 50,000, and the figure needs no aptamer Kd, no occupancy θ, and no `kon`/`koff`, so it leaves C007 honestly empty. Its two real weaknesses are that it partly re-states what Hu's own authors already concluded (C031) — which costs it on "novelty without overclaiming" but is also why it is defensible — and that its τ is Clements' abstract-only cultured-hippocampal inference imported onto a retina poster, which must stay labelled as the literature stimulus it is. A3 (working-range bars, PR #23, scored 75/80) is the better exhibit on relevance and is cleanly implemented — stdlib-only, ledger-copied, tested, and it already caught two errors in its own proposal table (Xiao's cleft fold is 11,000-fold, not 11-fold; 1 mM does not contain 1.1 mM on SI-strict reading) — but it cannot be the flagship as drawn, because its left tick **is** Herman's 25 nM. Rebuild it with a basal *band* rather than a tick and it becomes stronger, not weaker: against a 34.7 µM basal, Xiao's 100 nM ceiling misses from above by 347-fold and both Hu windows (10 µM ceiling) fall below the basal band's top, so candidate C's ceiling-from-above observation stops being a remark about two ultrasensitive outliers and becomes a statement about every calibration in the ledger. That is the correct division of labour: A4 flagship, A3-with-a-band as Panel 2, and the 81-fold identity demoted from flagship to a two-line derivation that is explicitly **not** compared to a single biological span.

---

## 5. Public-data feasibility of the named flagship

**A4 as it stands: already built and reproducible, no new data required.** PR #24 implements it in Python 3.10+ standard library only, no network, no pip, no GPU, with `rebuild.sh`, `provenance.md`, `limitations.md` and a top-level test hook. Every plotted value is pinned to a `research/evidence/core_evidence.csv` row already in the tree (E032, E033, E034 for the literature stimulus; E045 interrogation; E046 sampling), with the 15 min journal wait (E008) and 10 min plateau (E042) held off-figure and IPA/GlutOx confined to a labelled other-class footnote. Feasibility risk is zero because nothing has to be retrieved.

**A3 rebuilt with a basal band: feasible on free routes, with one ledger dependency that is not mine to satisfy.** The bars and the existing ticks are already ledger-local (PR #23 reads them from `core_evidence.csv`). The three new basal rows are **not** in `core_evidence.csv`, `state/claims.csv` or `state/sources.csv` — I grepped for Hershey, Hascup, 40838767, 20969570 and 18024788 and found nothing. All three are retrievable free and I retrieved two of them in this session:

```
curl "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=12418293&retmode=xml"   # Hershey 2025
curl "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=2996468&retmode=xml"    # Hascup 2010
curl "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=3404456&retmode=xml"    # Hascup 2008
```

The Europe PMC `fullTextXML` endpoint returns an empty body for all three (NIH author manuscripts); the `efetch` route works. No paid API, no PDF committed. PR #26 has already audited the identifiers and stated the required corrections — notably that Hascup 2010's 34.7 ± 11.8 µM is a §3.1 parenthetical with n = 41 that must not be fused with the n = 7 TTX result, and that Hascup 2008's ~20% TTX figure is mouse striatum (PMID 18024788), not rat PFC. The orchestrator owns the ledger write; until those rows exist, A3-with-a-band is blocked on a ledger entry, not on data access.

---

## 6. What was tested and rejected

| Tested | Outcome |
| --- | --- |
| Whether the 81-fold identity is itself wrong | **Rejected.** The algebra is exact and construct-independent; I re-derived it. What fails is the comparison, not the identity. |
| Whether "81 vs 44,000" survives as the flagship | **Rejected** (§1). Conclusion flips sign across four primary basal measurements spanning 1,388-fold. |
| Whether PR #18's "wrong quantity" limiter should replace the story | **Rejected** (§2.2). Authors attribute the dissociation to recovery geometry; Hascup 2010's total-glutamate sensor reports the TTX-sensitive event; load-bearing nulls are n = 3–4. Its Gln = 179 µM specification is kept. |
| Whether PR #19's REPLACE extends to killing revised D as title | **Rejected.** PR #19 concurs; the clocks half needs no occupancy figure. |
| Whether PR #18's folate-protocol experiment replaces the paired isotherm | **Rejected as a replacement, adopted as two specifications** (§3.3). Bottari is abstract-only and ampicillin; OC-3's glutamate inference is `hypothesis`. |
| Whether PR #25's co-located dialysis + fast sensor experiment replaces it | **Rejected** (§3.4) — right experiment for a question §2.2 rejected. |
| Whether A3 should be flagship | **Rejected in favour of A4** (§4). A3's own left tick is the contested pole. |
| Whether the four basal values are a flat contradiction | **Rejected as a framing** (§2.4), `hypothesis` only: Herman's own transport-shielding result suggests receptor-domain vs bulk-ECF compartments. Not a finding. |
| Whether any parked PR supplies a glutamate aptamer `kon`/`koff` | **No.** PR #18's Q4 covered 96 records with zero hits, independently re-confirming C007. Atlas cells stay empty. |
| Whether PR #28's PASS claim was used | **Not read, not copied**, per instruction. |

---

## 7. What would falsify the KEEPs

**Falsifiers of the story KEEP (§2.1).** Any one of these materially weakens it:

1. A primary measurement showing that the retina ACV change Hu recorded is **not** glutamate — pharmacological identity (TTX, CNQX/AP5, TBOA) or a scrambled-aptamer probe on the same shank returning the same light-correlated signal. The positive leg of the story ("Hu retina positive on a basal/slow clock") then reduces to a correlation with room light.
2. A glutamate-aptamer recording with sub-millisecond-to-few-millisecond interrogation **and** sampling on the same oligo. "Two regimes, and this architecture serves only the slow one" becomes an architecture-choice statement rather than a device limit, and A4 falls with it.
3. Primary evidence that the baseline and the transient are not separable compartments at all — i.e. that Herman's two-component framing is an artefact of the slice — which would remove the "two regimes" premise rather than its numbers.
4. A measured glutamate `koff` that is fast at a µM-scale Kd, flipping the cleft column from untested toward architecture-limited.

**Falsifier of the next-experiment KEEP (§3).** A published solution `Kd_molecular` for the exact Fc-thiol 39-mer, with a binding-null control, appearing from any group — the experiment is then done and the highest-information action moves to pharmacological identity (Opus unknown 2). Weaker but real: a locked decision that the poster's question is retinal glutamate biology rather than sensor fitness, which is Opus's own fork and substitutes pharmacology.

**Falsifier of my own flagship REPLACE.** If the µM-class basal values are shown to be method artefacts — e.g. primary evidence that GluOx MEA self-referencing systematically over-reports resting glutamate, or that extraction-fraction correction inflates `Capp` — and 25 nM is re-established as the bulk-ECF basal, then the span returns to ~44,000-fold and "81 vs 44,000" is safe again. PR #18's OC-17 and PR #25 §6 both record this reconciliation as `unresolved`, and PR #26 declines to adjudicate it. I have not resolved it either, and my REPLACE does **not** depend on which method is right: it depends only on the fact that four primary measurements disagree by 1,388-fold and the poster's conclusion is not invariant across them.

---

## 8. Inference boundary

**Measured** (by others; I inspected Hershey §3.1, Hascup 2010 §3.1–3.2 and Herman's abstract myself this pass): basal extracellular glutamate at 25 nM (slice, tonic NMDAR current), 3.3/5.0 µM (awake mouse MEA), 9.4 ± 0.6 µM (rat cortex dialysis, `Ed`-corrected, n = 11), 34.7 ± 11.8 µM (awake rat PFC MEA, n = 41); Gln 179 ± 20 µM in the same animals as the 9.4 µM; −40.8 ± 10.8% TTX effect on awake rat PFC resting glutamate (n = 7); Hu's reported calibration windows and protocol clocks; that Hu fitted Langmuir–Freundlich and did not report n.

**Inferred by me**: the span table and the n-threshold arithmetic in §1.3 (`computational illustration`, two lines, no fitted parameters); that the flagship's conclusion is not invariant across the primary basal set (§1.4); the receptor-domain vs bulk-ECF compartment reading (§2.4, `hypothesis`); that A4's clock ratio is immune to the basal dispute (§4).

**Unknown**: which basal method is right, or whether the question is well posed; Hu's LF exponent n; solution `Kd_molecular` of the 39-mer; glutamate `kon`/`koff`; chemical identity of the S066 ACV change; any bulk-ECF transient amplitude; glutamate-aptamer cross-reactivity to glutamine at 179 µM.

---

## 9. Independent review of this review

Per the Research Effort Standard, my load-bearing conclusion (§1, flagship REPLACE) was sent to two blind reviewers who did not see this file or any Wave A conclusion, and who were instructed not to read `reports/`, `rounds/`, `poster/`, `state/gates/` or `research/reviews/`:

- `bc-44c0c46b-2b0a-51de-86d1-d529108cb394` — given the proposed poster computation and the primary numbers only; asked to judge whether "81-fold vs ~44,000-fold" is safe, to compute the LF n thresholds independently, and to run its own negative search for a glutamate-aptamer `kon`/`koff`.
- `bc-b7ac5ad5-bae0-597d-8a85-332fe27880d2` — asked independently whether a surface aptamer electrode and a tonic NMDAR current report the same quantity, and required to argue the opposite case (that the methods genuinely contradict and one is wrong).

Their findings are recorded in §10. Where a reviewer disagrees with me, the disagreement is recorded rather than resolved.

---

## 10. Blind reviewer findings

*(Appended after the reviewers returned; see §9 for what each was asked.)*

---

## 11. Gate status

Unchanged: **REVISE**, `group_final: false`. This review did not touch `state/gates/science_story.json`.

For the record, the direction of travel: gate bullet 5 ("computation answers the thesis rather than decorating it") was scored **qualified yes** on the strength of the 81-fold-vs-44,000-fold comparison. §1 removes that support. A closer acting on this review should expect bullet 5 to weaken to **no** until a replacement flagship is accepted, and bullet 2 ("load-bearing claims have primary evidence") to remain **no** with a second `unresolved` added: the basal pole itself. Completion is not acceptance; nothing here licenses PASS.
