# Candidate A — Fit for a named neurochemical task

**One-sentence thesis.** A glutamate aptamer sensor is not “good” or “bad” as a scalar. It is fit, or not, for a named task tuple: concentration window × clock × matrix, on a named construct.

**Program label.** Fit-for-purpose (Mission 1 Program A).

**Trio.** Steelman `bc-ca1e1f55`; red team `bc-9de418cc`; independent `bc-5594d47d`.

**Trio verdict on this program (not a ranking of A–D).** Steelman: sharpened KEEP. Red team: REVISE the slogan (IUPAC tautology as written). Independent: the slogan is too weak and false as a sufficiency claim; “fit to task” is also the field’s alibi.

---

## Why this could be the BIOC1600 story

The course question is whether an aptamer can keep up with neurochemical signaling, jointly determined by affinity, selectivity, kinetics, transduction, immobilization, and biological context. Candidate A’s claim is that those axes are not averaged into one LOD rank. The same Glu-apt family (Wu truncated oligo / Hu Fc-thiol Glu-apt) receives opposite grades depending on which FoM is asked:

| Named task | Same-family number | Grade if that task is the question |
|---|---|---|
| Detect glutamate above blank in PBS | Hu MEA LOD 32 pM blank+3SD (C004); thesis probe 0.3 pM blank+3 RSD (C029) | Capable at nM calibrants |
| Sit in the linear occupancy window at Herman ambient ~25 nM | 1:1 overlay of Hu LF 1.8 nM → θ(25 nM) ≈ 0.93 (SIMULATION; occupancy table) | Saturated if 1.8 nM is used as occupancy Kd |
| Follow synaptic milliseconds | Journal 15 min Glu wait (C006); thesis ~10 min plateau after 10 nM (C028); retina ~1 min/point, authors: basal not synaptic (C031) | Protocol-slow; no Glu `kon`/`koff` (C007) |
| Quantify in Ames / tissue | Ames window 10 nM–10 µM, authors: poor SNR, 41.6% blank noise (C030); tissue ACV is signal-gain, not µM maps | Qualitative |

The strongest primary spine is **within-paper quantity splits** plus the **only neural-tissue Glu-apt experiment** (Hu thesis S066): dual-mode PaC probe, 2/4 probes light-correlated, authors disclaim synaptic transients.

---

## Load-bearing claims

1. **Kd ≠ LOD ≠ EC50 ≠ wait time ≠ biological [Glu].** `hypothesis` as a joint slogan; each split is `primary-source-supported` (C001 vs C002; C021 vs C005; C006; C012).
2. **Herman ~25 nM is ambient/baseline slice glutamate, not extrasynaptic-only.** `primary-source-supported` (C012; S050). Receptor EC50 1.8 µM on patches is not an aptamer Kd (E035).
3. **Clements 1.1 mM / 1.2 ms is kinetic inference at cultured hippocampal synapses.** `primary-source-supported` as inference; not a chemical assay; `full_text_inspected=no` (C011).
4. **Hu 1.8 nM is Langmuir–Freundlich apparent electrochemical Kd / EC50, not 1:1 molecular Kd.** `primary-source-supported` (C005). Occupancy θ from plugging 1.8 nM into 1:1 Langmuir is `computational illustration`.
5. **Hu methods 12 µM is a Wu citation, not a remeasurement of the surface 39-mer.** `primary-source-supported` (C021).
6. **S066 reports basal glutamate, not synaptic transients; Probe 3 near saturation at basal.** `primary-source-supported` (C031). In vitro retina ≠ in vivo (C020).
7. **Asp/Gln are not in the thesis selectivity panel.** `primary-source-supported` (C032). Selectivity is a FoM inside this thesis, not a replacement thesis (wildcard W1: REJECT as fifth story).

---

## What the red team breaks

The unsharpened slogan “the sensor must be fit for purpose” is an IUPAC tautology. A first-year assessor can ask “fit for *what*?” and the poster has not named [Glu] and τ. LOD rank does not predict S066: a 0.3 pM PBS LOD coexists with Probe 3 saturation and 1 min sampling of basal Glu.

Helassa/Marvin protein indicators are **comparators** (affinity variants; buffering, C024), not aptamer transfer.

**Revised A (the version that can survive):** lock a biological concentration and a biological clock; test whether θ(c) on a named construct is in a useful occupancy band and whether the **measured** clock (incubation, scan, sampling) is shorter than that biological clock. Do not claim fitness from LOD.

---

## Independent cut

Fit-to-task is also how papers excuse a FoM that does not match the introduction’s biology. Hu bills physiologically relevant / brain glutamate and then uses 15 min ACV waits and a retina protocol the authors themselves call basal. Candidate A is only honest if the poster **fails** the synaptic task rather than hiding that failure under “different purpose.”

---

## Inference boundary

**Measured:** construct-tagged LODs, Hu LF 1.8 nM, wait/scan/sampling times, S066 light-on/off signal-gain on Probes 1–2, author basal-not-transient sentences.

**Inferred:** that 1.8 nM LF midpoint is the occupancy Kd of the PaC probe in Ames/tissue; that Herman 25 nM is retinal [Glu]; that “fitness” is the right course title rather than a methods heading.

**Unknown:** glu1/Hu 39-mer solution `Kd_molecular`; glutamate `kon`/`koff`; chemical identity of the retina ACV change (no TTX/CNQX/TBOA).

---

## Falsifier

A is weakened if (i) a paired solution+surface Kd of the 39-mer shows 1.8 nM is molecular affinity and the overlay is no longer an overlay; (ii) a Glu-apt reports a pharmacologically identified, sub-second extracellular Glu transient in tissue; (iii) the poster names no [Glu] and no τ and still claims “fit for purpose.”

---

## One-poster form

Panel 1: task tuple (c, t, matrix, construct). Panel 2: same oligo, four FoMs, four grades. Panel 3: S066 dual clocks (spikes ms vs ACV ~1 min) and Probe 3. Do not print 81-fold as Hu’s calibration window. Do not print θ(25 nM)=0.93 without “1:1 overlay of an LF number.”

**Must not claim:** in vivo Glu-apt; synaptic transients in S066; Abrantes millimolar ELONA Kd; Park 2023 “Glutamate FET” as neurotransmitter glutamate; tobramycin IPA as Glu koff.

**Highest-value next step.** Pharmacological identity of the S066 ACV change, or a solution Kd of the exact 39-mer — not a lower LOD.
