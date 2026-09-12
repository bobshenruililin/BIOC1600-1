# Provisional six-panel storyboard — revised D

Not a finished poster. Not group-final. Canonical thesis: `state/current_thesis.md`. QUANTITATIVE FLAGSHIP: **NONE** (unresolved as title). Do not reopen “Mission 2 must decide a replacement flagship” as an open action.

This file **supersedes** `poster/storyboards/winner.md` (overnight T1; kept as history).

Stamps must be readable at panel scale. A viewer who cannot read captions must still see four classes:

| Stamp | Meaning on this poster |
|---|---|
| **MEASURED** | Inspected primary result on the named construct, matrix, and device |
| **MODELED** | Algebra or simulation; not a tissue measurement |
| **UNKNOWN** | Empty cell; do not paint a number |
| **PROPOSED** | Experiment that does not yet exist in the ledger |

Do not use `occupancy.svg` as a flagship glyph. That plot is a 1:1 overlay of advertised Kd/EC50 values, including Hu’s 1.8 nM AuED-MEA Langmuir–Freundlich apparent Kd, onto Herman ~25 nM. Overlay math is MODELED. It is not PaC-probe tissue occupancy. Do not use the 81-fold-versus-44,000-fold comparison as the flagship either; PR #31’s basal-pole and Langmuir–Freundlich objections remain candidate inputs.

---

## 1. Two regimes, two hippocampal examples

- **Claim.** Neurochemistry is baseline plus superimposed transients, not a generic sensor spec. Herman ~25 nM is ambient glutamate in **acute hippocampal slice** (MEASURED in that preparation). Clements ~1.1 mM / 1.2 ms is a kinetic **inference** at **cultured hippocampal synapses**, abstract-only. Different preparations. Not a retinal concentration range. Clements’ quantal-cleft preparation is not evidence about photoreceptor release.
- **Stamps.** MEASURED (Herman framing and 25 nM in slice). MODELED/INFERENCE (Clements peak/τ). UNKNOWN (retinal [Glu]).
- **IDs.** C012, C011
- **Figure.** Two labeled wells. No third extrasynaptic Kd well.

## 2. Flagship placeholder — NONE

- **Claim.** QUANTITATIVE FLAGSHIP: **NONE**. A plot would re-center on conversions the freeze forbids (slope-as-occupancy; Appendix II molarity; C_eq as tissue [Glu]). The 1:1 81-fold identity remains valid supporting biochemistry (C027/C013), but the Herman-to-Clements comparison is not a settled device requirement. Sampling-clock, dual-pole working-range, and occupancy overlay stay rejected as titles. PR #24 is not accepted and should not be called “Nyquist” without defended signal assumptions.
- **Stamps.** MODELED (81-fold identity). UNKNOWN (representative surface-electrode concentration span; LF *n*; flagship remains NONE). PROPOSED (U2 pharmacology plus scrambled/binding-null on both ACV legs).
- **IDs.** C027, C013, C031, E045, E046; `state/mission2_input_queue.md`
- **Figure.** Placeholder only. `span_identity.svg` may appear as a supporting inset; do not label it flagship. Do not merge PR #24’s generated figure wholesale.

## 3. Hu retina: two ACV legs on a slow clock, identity UNKNOWN

- **Claim.** S066 in vitro mouse retina: two ACV signal-gain legs on 14 s scans and 1 min points (C033 / E046, Fig. 6.13) with **unequal IVs**. (A) post-insertion rise (time; light held on) from a dashed baseline; (B) later room-light on–off–on (illumination) (Probes 1–2 authors p < 0.05; Probes 3–4 ns). Authors interpret both as basal / sustained glutamate, not synaptic transients. Printed spiked-buffer PBS/Ames `%gain` maps cannot invert tissue ACV. Ames window 10 nM–10 µM with **41.6% blank noise** (C030 / E044) — no absolute [Glu]. Neither leg is MEASURED glutamate: **identity UNKNOWN at panel scale**. Ch. 7 “steady-state [Glu]” is not a licensed MEASURED reading of Fig. 6.13. Printed spiked-buffer `%gain` maps ≠ ephys spike-rate panels ≠ Leg A ≠ Leg B. It is not a failed hippocampal-cleft experiment. The aptamer ACV electrode is the large bottom electrode at the **GCL/IPL border** (C034 / E045); pool assignment UNKNOWN. The declared two-map central object (two named-IV tissue legs beside two spiked-buffer `%gain` maps) is **prose-only**: no new flagship plot; do not invent pixels.
- **Stamps.** MEASURED (clocks, both ACV legs as signal-gain referenced to a post-insertion baseline, unequal IVs, author disclaimer, Ames SNR, in vitro). UNKNOWN (analyte identity at panel scale, absolute [Glu], occupancy, pool, in vivo). INFERRED (that either tissue ACV signal-gain is glutamate). PROPOSED (U2: pharmacology plus scrambled/binding-null on both ACV legs).
- **IDs.** C031, C033, C034, C028, C030, C020, C006
- **Figure.** `analysis/accepted/figures/two_regime_clocks.svg`. Two columns only: slow ACV MEASURED as signal-gain versus rapid-transient UNKNOWN. Stamp identity UNKNOWN in the slow/retina column. PROPOSED on this panel is U2, not kon/koff. Do not paint the slow column as identified glutamate. Do not draw Fig. 6.13 pixels. Do not use omnibus `clocks.svg` unlabeled (it mixes biological τ, bound t_off, incubation, and interrogation). Supporting clocks figure only; QUANTITATIVE FLAGSHIP remains NONE.

## 4. Occupancy on the retinal PaC probe is UNKNOWN

- **Claim.** The PaC probe has no reported apparent Kd in Ames or tissue. Hu 1.8 nM is MEASURED as an AuED-MEA Langmuir–Freundlich apparent electrochemical Kd in PBS — a different device. Do not draw θ(25 nM)≈0.93 as tissue occupancy. Do not recover θ from printed `%gain`. Probe 3/4: gold-nanostructure detachment (Fig. 6.16A) is MEASURED as failure analysis; occupancy-ceiling reading UNKNOWN. Do not collapse Fig. 6.12 (insertion peak drop) with Fig. 6.16B (1 kHz Z after cleaning). Probes 1–2 still change with light (MEASURED remaining dynamic range, not saturation). Ames is not a Glu-free ionic twin of PBS; Ames-loaded wording stays dropped.
- **Stamps.** UNKNOWN (PaC θ). MEASURED (1.8 nM on AuED-MEA; gold loss; Probes 1–2 modulation). MODELED (any 1:1 overlay of 1.8 nM; slope-ratio illustration).
- **IDs.** C005, C021, C026
- **Figure.** Empty occupancy well stamped UNKNOWN. Park 1.8 nM in a “different device / different isotherm” well. If `occupancy.svg` is shown at all, it is a supporting MODELED inset, not Panel 4’s claim.

## 5. Construct × quantity key (retired title B)

- **Claim.** 12 µM (1d04 Kd), 0.0013 pM (glu1 LOD), 1.8 nM (AuED-MEA LF apparent Kd), 32 pM (MEA PBS LOD), 51.5 pM (MEA 50% serum LOD), 0.3 pM (PaC PBS blank+3 RSD), 293 nM (Xiao SPR Kd), 10 fM (Xiao FET LOD in 0.1× PBS) are different objects on different constructs and matrices. Glutamate kon/koff cells stay empty (UNKNOWN). 0.3 pM is PBS, lowest calibrant 1 nM, not Ames. 32 pM is PBS blank+3SD, lowest calibrant 0.1 nM — not the serum number. 1.8 nM (electrochemical apparent Kd) versus 1.8 µM (Herman NMDAR EC50) share digits and must carry unit and quantity type in the axis label.
- **Stamps.** MEASURED (each ledger number on its row). UNKNOWN (empty kon/koff; PaC Kd).
- **IDs.** C001, C002, C004, C005, C007, C014, C021, C029, C030
- **Figure.** `analysis/accepted/figures/atlas.svg`.

## 6. What to measure next (PROPOSED)

- **Claim.** Highest-information experiment if the claim is tissue identity (U2): pharmacology plus scrambled/binding-null on **both** ACV legs, same shank and room-light protocol. Do not substitute rates for identity. Optional late-only Fig. 6.13 split does not name the analyte. If a human locks construct fitness (U1): paired solution `Kd_molecular` and surface ACV apparent Kd of the exact Fc-thiol 39-mer in one justified buffer; include a binding-null point mutant in both arms and L-glutamine/L-aspartate controls at biologically justified concentrations; fit Langmuir and Langmuir–Freundlich; report *n* with uncertainty, coverage, and interface chemistry. Do not do both and report neither.
- **Stamps.** PROPOSED (both experiments). UNKNOWN (until done).
- **IDs.** `state/high_value_unknowns.md`; C007, C032
- **Figure.** Protocol cartoon only. No invented Kd.

---

## Current figure status

| File | Role |
|---|---|
| replacement flagship | **UNRESOLVED — NONE as title.** |
| `span_identity.svg` | Supporting only. 81-fold identity is valid; the endpoint comparison is not accepted as representative. |
| `two_regime_clocks.svg` | Panel 3. Two clocks, four stamps. Identity UNKNOWN; PROPOSED is U2. Not a flagship plot. |
| `atlas.svg` | Panel 5. Empty cells stay empty. |
| `occupancy.svg` | DEMOTED MODELED overlay of advertised numbers. Not tissue occupancy. |
| `sensitivity.svg` | Supporting: empirical kon band is NOT glutamate; τ_eq ≠ t_off. |
| `clocks.svg` | Supporting omnibus axis. Do not use unlabeled. |
