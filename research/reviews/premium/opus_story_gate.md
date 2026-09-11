# Opus 5 blind story-gate review

Agent: `bc-35465731-9331-54fd-b508-ca3af59e84ec`
Model: `claude-opus-5-thinking-xhigh`
Blind: no Grok A–D ranking; forbidden T1–T5 / scoreboard / nightly files not opened.

Saved verbatim from the reviewer output. Orchestrator note (not part of the review): `.cursor/rules/safety-and-integrity.mdc` is present in the repo; the reviewer reported it missing. Constitution and rubric were read.

---

## Method

Read: `rounds/mission1/candidates/{README,evidence_packet,A,B,C,D}.md`; `rounds/mission1/sealed/README.md`; `sealed/hu/{h1,h2,h3}.md`; `sealed/ontology/{O1,O2_confusion_hunt,orchestrator_draft}.md`; `sealed/wildcard/W1.md`; all twelve `sealed/programs/*` lane notes (treated as provenance only); `state/claims.csv`; `research/evidence/{core_evidence.csv,poster_numbers.md,quantity_ontology.md}`; `research/reviews/{contradictions,citation_audit,sensor_engineer,aptamer_biochemist,tanner_objections}.md`; `analysis/accepted/occupancy_kinetics/tables/occupancy_table.csv`; `analysis/accepted/occupancy_kinetics/limitations.md`; `analysis/accepted/figures/{occupancy,atlas}.CAPTION.md`; `.cursor/rules/{research-constitution,scoring-rubric}.mdc`. Primary extracts: `/tmp/hu_thesis_ch6.txt`, `/tmp/hu_thesis_ch7.txt`, `/tmp/hu_thesis_probe.txt`, `/tmp/hu_thesis_seq.txt`, `/tmp/hu_journal_snippets.txt`.

`.cursor/rules/safety-and-integrity.mdc` is not present in this repo; I proceeded on the constitution and rubric.

I did not read `reports/nightly_summary.md`, `state/scoreboard.json`, `analysis/candidates/theses/`, `poster/theses.md`, `poster/storyboards/`, `rounds/03/`, `rounds/04/`, `rounds/consolidation.md`, or `rounds/mission1/protocol.md` (not on the MAY list). Directory listings exposed some of these filenames; no contents were opened. I carry no prior T1–T5 ranking and no A/B/C/D ranking from any source; the scores below are mine.

## Per-candidate scores

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

### Candidate A — Fit for a named neurochemical task — 68 — FAIL as a title

The evidence A stands on is real and mostly inspected, but the title is true by definition. "Fit, or not, for a named task tuple" is the IUPAC fitness-for-purpose definition; it cannot be wrong, so it cannot be a finding. A's own independent section concedes the deeper problem: fit-to-task is the alibi the field uses when a figure of merit does not match its own introduction. The dossier's revised form — lock a biological concentration and a biological clock, then test θ(c) and the measured clock against them — is not a revision of A. It is Candidate D. A does two things better than anyone: it is the only candidate that explicitly lists "1.8 nM LF midpoint is the occupancy Kd of the PaC probe" under *inferred* (the chip-to-probe hop, which H1 also flags), and its same-oligo-four-grades table is the best single teaching panel in the set. Both survive inside another title.

Three hardest oral questions: (1) Fit for what — name the concentration, the clock, the matrix and the construct, now, with units. (2) Your table grades one oligo "capable" on LOD and "saturated" on occupancy; which of those two numbers was measured on the device that went into retina, and which was measured on a different chip? (3) If failing a broad task always licenses re-declaring fitness for a narrower one, what result could falsify your title?

Indefensible if: the poster prints "fit for purpose" with no locked (c, τ, matrix, construct); or prints 0.3 pM and 1 min/point as though they describe the same experiment's capability.

Occupancy/atlas: **decoration**. It supplies one cell of a grade table. A's argument survives intact on the clocks and the LODs alone, and A's own supporting lane calls the overlay fragile.

### Candidate B — Construct non-identity — 73 — FAIL as a title (KEEP as a panel)

B has the highest density of directly inspected primary rows and is the most reproducible thing here: a construct×quantity table with the empty cells honestly empty. It is also the most chemically dense candidate — truncation, Au–thiol SAM, backfill, packing density, Langmuir–Freundlich heterogeneity — and the most Tanner-aligned on interface seriousness and recognition honesty. Two problems cap it. First, the exhibit is Hu's own caveat: §3.2 already attributes the 12 µM/1.8 nM gap to 2D confinement, and a student who re-reads that paragraph has not produced a result. Second, within Hu's own Langmuir–Freundlich panel, the dopamine apparent Kd of 49.6 µM sits essentially on top of the cited 44 µM. Serotonin and glutamate "transform"; dopamine does not. A uniform interface-physics law fails inside the one table that is supposed to demonstrate it, and the more economical reading of the glutamate jump is wrong quantity plus wrong parent construct. Structurally, B answers "which numbers may not be averaged," not "can this measure neurochemical dynamics" — which is why central-question relevance is 5 and cannot be repaired without B becoming a different thesis.

Three hardest oral questions: (1) Hu wrote the confinement caveat; what did you add? (2) Why did glutamate's apparent Kd move ~10⁴-fold and dopamine's not at all, in the same fit, on the same chip? (3) Show the paired solution and surface Kd of the same 39-mer — it does not exist, so what is the measured content of your title?

Indefensible if: 12 µM → 1.8 nM is drawn as a measured truncation or confinement result; Ricci 2016 is cited as the Langmuir–Freundlich source (it is a 1:1 Langmuir/81-fold Account); Lam's "12 ± 6 µM" is printed as Wu.

Occupancy/atlas: the atlas is B's evidence and is load-bearing. The occupancy curves are **decoration** — B's own independent section calls them a warning illustration of promoting the wrong number to Kd.

### Candidate C — LOD is not usefulness; occupancy at ambient is the paradox — 77 — REVISE

C contains the sharpest previously-unstated observation in the set, and it is pure ledger arithmetic: the ultrasensitive calibrations miss the ambient number *from above*. Wu's glu1 working range tops out at 1 nM, twenty-five-fold below Herman's ~25 nM; the Abrantes preprint's stated ceiling of 10 pM is 2500-fold below it. The LOD contest is selecting windows that do not contain the concentration the same papers cite as biology. C is also the only candidate that names the confound in its own best exhibit: Hu's Fig. 6.16 attributes the Probe 3/4 failures to detached gold nanostructure, which the thesis says "could result in early saturation even at relatively low basal Glu levels," so Probe 3 is not a clean occupancy ceiling. That is exactly the kind of self-policing the rubric should reward.

The title still fails in its strong form, and C knows it. Hu's 32 pM already sits ~780-fold below 25 nM, so "you cannot see tonic glutamate" is false for that sensor, and Hu's 32/51.5 pM is legitimate matrix-matched blank+3SD antifouling chemistry that must not be binned with Wu's 0.0013 pM or Abrantes' 1 aM. What remains after the strong form is deleted is saturation-at-basal and working-range-in-matrix — which is D's content, arrived at from the LOD side.

Three hardest oral questions: (1) Hu's 32 pM is already ~780-fold below Herman's ambient; so which LOD is "too good to be useful," and what is the actual failure? (2) Fig. 6.16 shows gold detachment after insertion; how do you know Probe 3 is an occupancy ceiling and not lost binding sites? (3) Your Ames window is 10 nM–10 µM with 41.6% blank noise while the fitted signal step per decade is ~57%; what is the smallest glutamate change you could resolve in tissue?

Indefensible if: Hu's 32/51.5 pM is labelled vanity; 0.3 pM is printed as the retina-in-Ames LOD; Probe 3 is asserted as a measured saturation.

Occupancy/atlas: **partially load-bearing, but not the part that is computed**. C's load is carried by working-range arithmetic and by the authors' own saturation sentence. The θ(25 nM)≈0.93 curve is a caveat C must print in order to disown.

### Candidate D — Two biological regimes, not a generic glutamate sensor — 85 — KEEP as the title, conditional on named revisions

D is the only candidate whose title is a claim about the world rather than a rule about numbers, and it is the only one whose computation is the argument rather than an illustration attached to it. Herman's own framing is baseline plus superimposed transients — two components, not three pools, and "extrasynaptic" is not Herman's label. A 1:1 Langmuir site spans exactly 81-fold between 10% and 90% occupancy, derivable in two lines from θ = c/(c+Kd) with no aptamer number at all. Ambient 25 nM to inferred cleft 1.1 mM is 44,000-fold. That comparison is the most course-appropriate piece of biophysics in the set: a first-year can derive it, draw it, and defend it, and it does not depend on any contested affinity.

D also refuses the cheap kill that would have made it easier to write. "No koff, therefore too slow" is wrong, because τ_eq = 1/(kon·c + koff) can be short at millimolar glutamate even when t_off is long; D says so and keeps the cleft column tagged untested rather than failed. It names the 1.8 nM versus 1.8 µM digit collision (Hu's electrochemical apparent Kd against Herman's NMDAR EC₅₀ on nucleated patches), which is the single most likely oral trap on this topic. It refuses to score Hu's retina work as a failed hippocampal-cleft sensor, correctly noting photoreceptor glutamate is graded rather than quantal. It fences GlutOx and iGluSnFR as comparators.

The defect is specific and fixable. D's basal column asserts that current devices "fail the slow problem on occupancy," and the only support for the occupancy half is (i) a 1:1 overlay of a Langmuir–Freundlich EC₅₀ that D itself says must not be treated as a 1:1 Kd, measured on an AuED-MEA chip and not on the parylene-C probe, and (ii) Probe 3, which the thesis attributes to detached gold. The clocks half is airtight and entirely primary; the occupancy half is not. D must either restate that half as "occupancy at basal is unmeasured on this construct in this matrix" or carry C's honesty about the gold confound. D also does not engage the layer tension H2 and H3 raise — the aptamer electrode is the 25 µm bottom electrode reported at the GCL/IPL border while the light-dependence mechanism sentence is about photoreceptor terminals.

Three hardest oral questions: (1) Your basal column says the device fails on occupancy; the support is an overlay of a number you say is not an affinity, measured on a different device, plus one probe the authors explain by gold loss — what is left? (2) 1.1 mM and 1.2 ms are a 1992 kinetic inference from cultured hippocampal neurons, abstract-only; why is that the right-hand column of a retina poster? (3) If missing koff does not prove the sensor cannot do synapses, what exactly does your poster claim is wrong at the cleft, and what single measurement settles it?

Indefensible if: "1.8" appears anywhere near an occupancy axis without unit and quantity type; koff ≈ 1/1.2 ms is printed; a third extrasynaptic Kd is drawn; or Hu is said to have failed as a synaptic sensor when the retina chapter never claimed one.

Occupancy/atlas: **load-bearing** — and this is the only candidate for which that is true. The 81-fold identity *is* the thesis in quantitative form. Precisely because it is load-bearing, D inherits the overlay's illegitimacy, which is the revision.

## Comparative judgment

**Yes, one candidate is materially stronger: D, by eight points over the runner-up and seventeen over the weakest.** The margin is not cosmetic because it is structural rather than accumulated. D wins central-question relevance outright (10 vs 5–8) because it is the only title that states a testable match-or-mismatch between a biological quantity and a chemical one; the other three state rules about numbers (A: a definition, B: a vocabulary constraint, C: a negated proxy). It wins biochemical depth because its argument requires deriving an isotherm identity and distinguishing τ_eq from t_off, while A's and C's titles can be defended without writing a binding equation. It wins critical insight because it declines two available cheap wins — the koff kill and the "Hu failed at synapses" kill — and is still left with a claim.

There is a second, independent signal inside the dossiers themselves: each candidate's own adversarial section points at the same place. A's revised form is "lock a biological concentration and a biological clock, test θ(c) and the measured clock." C's red team says C may be rejected as the title in favour of an occupancy/timescale story. B's red team says the load-bearing story is occupancy and clocks, not a transformation flowchart. Three of four dossiers converge on D's content while writing about themselves. That is not a ranking handed to me; it is what the four independent trios each concluded when trying hardest to defend something else.

**Runner-up: C (77).** Its ceiling-from-above observation is genuinely additive and belongs in the winning poster whether or not C is the title.

**Unresolved disagreements.** (1) Probe 3: occupancy ceiling (D, H2) versus gold-detachment artifact (thesis §6.3/Fig. 6.16, flagged by C). Unresolved, and it matters because it is the only in-tissue evidence for "saturated at basal." (2) Whether the 1:1 overlay on Hu's 1.8 nM should be drawn at all: the ontology lane recommends no longer selecting it as canonical occupancy, while A, C and D all draw it with captions. (3) Whether non-transfer is a law: B's red team says no — sequence string and Au–thiol chemistry transfer, and dopamine's apparent Kd nearly matches its cited solution value — while A and B's steelman treat non-transfer as near-universal. (4) Whether a middle "extrasynaptic" regime exists as a design spec: D says it is a tool-class and clock artifact; A's named-task frame would permit it as a task; the Moussawi span 0.02–30 µM is review-supported and unresolved. (5) H2 versus C031: H2 holds that the Chapter 7 sub-second sentence is load-bearing and that C031 over-ranks S066 as "the strongest neural-tissue experiment"; H2 and H3 both read it as device-level feasibility. (6) The layer tension — aptamer electrode at the GCL/IPL border, photoreceptor narrative — is raised by H2 and H3 and addressed by none of A, B, C, D. That is a shared blind spot and an oral-ending one for any poster that prints "photoreceptor glutamate" next to this electrode. (7) W1 is rejected by all four as a fifth title; its rank among the open unknowns is not agreed.

**Reversing evidence that would swap the ranking.** If a paired solution-and-surface isotherm of the same 39-mer lands near 12 µM in both phases, then 1.8 nM is a transduction artifact, θ(25 nM) falls to ~0.2%, "saturated at basal" collapses, and C's working-range story becomes the stronger title. If it lands near 1.8 nM in both phases, confinement becomes a measured result and B rises furthest relative to its ceiling. If pharmacology identifies the retina signal as glutamate, "the device already works at basal" becomes primary, and A's framing gains a positive case (though the title stays tautological). If a glutamate aptamer koff is measured and is fast at a µM-scale Kd, the cleft column flips from untested to plausibly adequate and the poster becomes an architecture-and-interrogation-clock story — closest to A's task tuple and B's interface content. If Asp/Gln cross-reactivity at Ames-realistic concentrations proves large, W1's content becomes load-bearing inside every title and the tissue result's chemical identity is in doubt.

## Hu retina

S066 answered a device-and-physiology feasibility question and answered it honestly: whether a ferrocene/thiol glutamate aptamer on a gold-electrodeposited parylene-C intraretinal shank can, inside isolated mouse retina, produce a reversible ACV signal-gain change that tracks room-light on/off in the direction expected for basal extracellular glutamate, while a neighbouring electrode on the same shank records light-modulated ganglion-cell spikes — yes, for Probes 1 and 2 at p < 0.05, on a probe characterized by a PBS calibration linear from 1 nM to 1 mM with a 0.3 pM blank+3RSD LOD (C029), an Ames window of 10 nM–10 µM with 41.6% blank noise that the authors themselves call poor resolution for quantitative analysis (C030), a ~10 min signal plateau after 10 nM glutamate (C028), 14 s per ACV scan and ~1 min per point after insertion (C031), and a selectivity panel of 100 nM Glu versus 10 µM serotonin, dopamine, tyrosine and lactate (C032). It did not answer how much glutamate — there is no absolute in-tissue concentration and the authors say the Ames SNR forbids one; nor how fast — Chapter 7 states the time resolution limits detection of transient release, and §6.3 states the sensor captures sustained basal glutamate "rather than the fast, transient release events associated with individual synaptic activity"; nor whether the signal is chemically glutamate — there is no TTX, CNQX/AP5 or TBOA and no scrambled-aptamer probe (H1–H3); nor from which pool — the aptamer-modified 25 µm bottom electrode is reported at the GCL/IPL border while the light-dependence mechanism invoked is photoreceptor terminal release, the layer tension H2 and H3 flag; nor with what selectivity against the relevant chemical neighbours, since aspartate, glutamine and GABA are absent from Fig. 6.8A. Probes 3 and 4 failed, and Fig. 6.16 attributes this to detached gold nanostructure reducing available binding sites and possibly causing "early saturation even at relatively low basal Glu levels," so Probe 3 is a confounded, not a clean, occupancy observation. No journal MEA number belongs on this probe: 1.8 nM is an AuED-MEA Langmuir–Freundlich fit and 32/51.5 pM are MEA LODs; the intraretinal probe has no reported apparent Kd at all. The internal 10 nM (body) versus 100 nM (Fig. 6.5A caption) discrepancy should be recorded as found, not resolved by choosing one.

## Quantity honesty

Where the four still collapse quantities:

- **The 1:1 overlay on Hu's 1.8 nM (A, C, D).** All three print θ(25 nM) ≈ 0.93 and all three caption it. A caption is not protection at 90×120 cm. Worse, this is a *double* transfer: Langmuir–Freundlich to 1:1, and AuED-MEA chip to parylene-C probe. A and B name the chip-to-probe hop explicitly; C and D only gesture at it. Whoever wins must print the quantity type and the device inside the axis label, not the caption.
- **1.8 nM versus 1.8 µM.** Hu's electrochemical apparent Kd and Herman's NMDAR EC₅₀ on nucleated patches share digits across a thousand-fold and mean different things. Only D names the collision. A, B and C are exposed.
- **1.8 nM versus Herman's ambient.** Neither is a molecular affinity of a glutamate aptamer in the matrix that matters; putting them on one concentration axis is the trap the whole atlas was built to prevent.
- **LOD estimators and their calibration floors.** 32 pM is blank+3SD on a semi-log fit whose lowest calibrant is 0.1 nM — about 3-fold of extrapolation. 0.3 pM is blank mean + 3×relative SD on a fit whose lowest calibrant is 1 nM — roughly 3,300-fold below anything actually measured. The thesis nonetheless compares them directly ("more than 100-times smaller than the classical MEA sensor"). No candidate makes this explicit; C comes closest by planning to caption the 3SD/3RSD split. Any poster printing 0.3 pM must print the estimator, the matrix (PBS, not Ames), and the fact that it is extrapolated three decades below the lowest calibration point.
- **Clocks.** Five distinct objects are in play — biological decay τ (1.2 ms, inferred), interrogation (14 s scan; IPA 2 ms), incubation (15 min journal, 10 min thesis), sampling interval (~1 min), and equilibration/stabilization (200 s FET, 11–20 min thrombin) — plus one enzyme comparator (500–800 ms) and one simulation (0.73 s). A single log-time axis merges them; A's and D's two-clock retina panel (millisecond spikes versus ~1 min ACV points) is the honest form and should replace the omnibus axis.
- **Herman's 25 nM as "the" ambient number (A, C, D).** It is efficacy-scaled from tonic NMDAR current in acute hippocampal slice with intact transport — not retina, not a chemical assay, not extrasynaptic-only. A and D flag the retinal transfer as inferred; C does not.
- **The parent Kd's matrix.** Wu's 12 µM is from "complex medium (unspecified in abstract)." No candidate says the parent affinity has no defined buffer, which matters for anyone arguing about what confinement changed it from.
- **Clements as a chemical measurement.** All four label it correctly. Keep it that way: it is an abstract-only kinetic inference in cultured hippocampal neurons, `full_text_inspected=no`.
- **Abrantes.** 1 aM is a preprint abstract claim (C025). The millimolar ELONA Kd is not a ledger number and must not be promoted; the 10.3/25.1 tokens were identified as funder award IDs. Two lane notes and one candidate lane (A's independent, B's independent, D's steelman) touched this; none of the four candidate dossiers promote it. Correct.

## Wildcard

I agree W1 should not be a fifth title, and the reasoning holds: a title needs a load-bearing exhibit, and W1's exhibit is an empty cell. Fig. 6.8A compares 100 nM glutamate against 10 µM serotonin, dopamine, tyrosine and lactate — the wrong chemical class, with no ratio reported for aspartate, glutamine or GABA. The Abrantes selectivity row is a preprint's secondary citation of a closed version of record. Xiao's panel is neurotransmitters in 0.1× PBS. Docking cannot rescue it (C017). Selectivity here is organized by missing panels, not by a measured number.

**Dissent, on rank rather than verdict.** W1 is under-weighted as an unknown. Ames' published formulation lists L-glutamine at 0.073 g/L, which is about 0.5 mM by arithmetic on the vendor sheet — a structurally adjacent amino acid present at roughly 10²–10⁵-fold above the analyte across the entire 10 nM–10 µM window used for the tissue experiment, never challenged. That does not make a title, but it is not a footnote either: it belongs as a named open box in the winning poster and, in my ranking below, as the fourth of five highest-value unknowns. Tag it `unresolved`; the concentration is arithmetic on a public product sheet, not a ledger claim, and no interference has been measured.

## Gate recommendation

**REVISE.** D is the story; the gate does not pass as submitted.

1. *One thesis materially stronger than the other three* — **yes.** D at 85 versus 77/73/68, with the margin in relevance, insight and depth rather than in rounding.
2. *Load-bearing claims have primary evidence* — **no (partial).** D's clock half is fully primary and inspected. D's occupancy half is not: it rests on a 1:1 overlay of a Langmuir–Freundlich EC₅₀ measured on a different device, plus a probe failure the authors attribute to detached gold. The cleft column rests on an abstract-only 1992 kinetic inference.
3. *Survives the counterevidence in its own dossier and contradictions.md* — **no.** Unaddressed: the Fig. 6.16 gold-detachment explanation for Probe 3, and the H2/H3 GCL-IPL layer tension against the photoreceptor narrative.
4. *Fits one poster a first-year can draw without collapsing Kd/LOD/EC50/clocks* — **yes, conditionally.** Two columns, two clocks, one empty kon/koff cell is drawable. The condition is that quantity type and device move from captions into axis labels.
5. *Computation answers the thesis rather than decorating it* — **yes, qualified.** The 81-fold identity versus 44,000-fold span is the thesis in quantitative form and requires no aptamer number. The θ curves anchored on 1.8 nM are the decorative part and should be demoted.

Required revisions before re-gating: restate the basal column as unmeasured occupancy rather than demonstrated saturation; adopt C's gold-detachment caveat and A's chip-to-probe wording; address or explicitly bracket the electrode-layer question; move the θ-overlay curves to a captioned inset or drop them; import B's construct×quantity key and C's ceiling-from-above panel as supporting panels with their own titles retired.

## Five highest-value unknowns

1. **Is 1.8 nM an affinity or an interface artifact?** A paired solution-phase and surface Kd of Hu's exact Fc-thiol 39-mer, same buffer, with the Langmuir–Freundlich exponent reported. Everything downstream — whether the device is saturated at ambient, whether confinement is a result, whether the 81-fold window is even applicable — turns on this one answer.
2. **Is the retina signal chemically glutamate?** Pharmacological identity (TTX, CNQX/AP5, TBOA) plus a scrambled-aptamer probe on the same shank. Without it, the only neural-tissue glutamate-aptamer result in the ledger is a correlation with room light, and every candidate's "the device already works at basal" leg is soft.
3. **Glutamate aptamer kon and koff on the 39-mer** (IPA or SPR under controlled mass transport). This is the empty cell the cleft column is built around; it converts "untested" into "tested" and is the only route to a real τ_eq.
4. **Glu versus Asp/Gln/GABA signal-gain ratios on the same oligo, in PBS and in Ames**, at the glutamine concentration the medium actually contains. Decides whether the tissue signal is the analyte.
5. **Is Probe 3 occupancy or lost gold?** Paired electroactive surface area, 1 kHz impedance and aptamer surface coverage on the same probe before and after insertion, alongside the light test. Hu has half of this already in Fig. 6.16B.

## Flagship analysis

The 81-fold Langmuir identity (C027, implemented in `analysis/accepted/occupancy_kinetics`) is the flagship, and its strength is that it needs no aptamer number: c₉₀/c₁₀ = 81 for any 1:1 Kd, derivable in two lines and drawable as a fixed-width band slid along a concentration axis against 25 nM and 1.1 mM. Set against a 44,000-fold biological span, that is the entire argument, and no contested value enters it.

The θ curves in the same analysis — the ones anchored on 1.8 nM, 12 µM and 293 nM — do not answer the recommended story; they illustrate what happens if you believe one of three advertised numbers, and the one the poster would lean on is the one D disowns. The clocks figure answers the clock half but is the figure the ontology lane flags for merging five clock types onto one axis. The atlas answers B, not D. So: one existing computation is flagship-grade, and the honest redraw of the other is a sensitivity band — θ(25 nM) across candidate Kd from 1.8 nM to 12 µM — showing that the occupancy verdict is currently undetermined by four orders of magnitude, rather than a single curve asserting 0.93.

## Next experiment

`proposed experiment` — **Measure the isotherm of Hu's exact Fc/thiol-modified 39-mer twice, in two phases, in one buffer, on one construct.** In solution by ITC or fluorescence titration for a 1:1 `Kd_molecular`; on the same gold-electrodeposited surface by ACV under the published PBS conditions for the apparent electrochemical Kd, fitting both Langmuir and Langmuir–Freundlich and reporting the heterogeneity exponent n with its confidence interval. Pair each with the surface coverage actually achieved.

This is the highest-information single experiment because it resolves five things at once: whether 1.8 nM is an affinity or a transduction number; whether the 1:1 81-fold window may legitimately be drawn on this sensor at all (n tells you); whether construct non-identity is a measured result or an assertion; what θ at 25 nM honestly is; and whether "saturated at basal" in retina is even arithmetically available. It is not a lower LOD, and it does not require tissue. If the poster's biological question is retinal glutamate rather than sensor fitness, substitute the pharmacological-identity control from unknown 2 — but do not do both and report neither completely.

## Before-closure answers

**After reading the four titles**, I expected B to win. Construct non-identity had the most directly inspected primary numbers, the cleanest exhibit, and the best claim to being a chemistry result rather than a slogan.

**After the ledger, that reversed.** B's exhibit turned out to be Hu's own §3.2 caveat restated, and Hu's own Langmuir–Freundlich panel contains its counterexample: dopamine's apparent Kd of 49.6 µM sits on the cited 44 µM while glutamate's moves by four orders. Meanwhile the clocks — 15 min, 10 min, 14 s, 1 min, 200 s — are all primary, all inspected, and decide the biological question without needing any affinity number, and the 81-fold identity is derivable without one either. Weight moved to D, whose thesis is the only one those two facts jointly support.

**Tested and rejected:** that "LOD is not usefulness" could be a title — Hu's 32 pM already sits ~780-fold below Herman's ambient, so the strong form is false; that "fit for purpose" is a thesis — it is a definition, and its repaired form is D; that Probe 3 is a clean occupancy-ceiling demonstration — §6.3 and Fig. 6.16 attribute it to detached gold; that W1 could be a fifth title — it has no measured ratio; and that three neurochemical regimes exist as design specs — Herman's own sentence is two components, and the middle band is a tool-class and clock problem with [Glu] unspecified across three orders of magnitude.

**Remaining uncertainty:** whether 1.8 nM is an affinity at all; whether the retina ACV change is glutamate; whether an electrode at the GCL/IPL border is compatible with a photoreceptor-release narrative; and whether any glutamate aptamer's koff is within three orders of magnitude of what the cleft would require. All four are unknown, and the poster should say so in those words.
