# T5 — framing challenger (forced diversity)

This candidate is required by the overnight brief: at least one thesis must **challenge the current framing**, not refine “aptamers cannot keep up with synapses.”

## one-sentence thesis

The distinctive BIOC1600 story is not that aptamers are too slow for neurotransmission—that treats a missing glutamate kon/koff as a negative result—but that after truncation, labeling, and immobilization the literature’s “improved” nM apparent Kd and pM–fM LODs describe different molecules and, if treated as occupancy Kd, are the numbers that saturate tonic glutamate and cannot unbind on a 1.2 ms cleft clock under a diffusion-limited kon bound, whereas the µM SELEX isolate could be kinetically competent and still empty at 25 nM (C001, C005, C007, C011, C012; computational illustration of the bound).

## central biochemical mechanism

The leading theses ask whether a glutamate aptamer sensor can jointly match recognition, kinetics, and architecture to neurochemical dynamics, then answer no. That answer is mostly a **gap**: inspected glutamate aptamer papers do not report kon/koff (C007, unresolved). Small-molecule E-AB architecture is already capable of millisecond interrogation (C009, tobramycin IPA 2 ms) and, for cocaine, equilibration faster than a ~4 s scan (C018/White). Importing those clocks as glutamate rates would be illegal transfer; ignoring them as architecture lessons would overclaim that “aptamers cannot keep up.”

The distinctive biochemical claim is an **inversion of the sales metric**. Occupancy θ = [Glu]/([Glu]+Kd). A diffusion-limited small-molecule kon (~10^8 M⁻¹ s⁻¹, physical-chemistry upper bound, not a glutamate measurement) implies koff ≈ kon·Kd:

- 1d04 Kd 12 µM (C001, abstract): koff bound ~1.2×10^3 s⁻¹, t_off ~0.8 ms — **fast enough to sit near Clements τ 1.2 ms (C011)** — but θ(25 nM) ≈ 0.2% (empty at Herman ambient, C012).
- Hu surface apparent Kd 1.8 nM (C005): koff bound ~0.18 s⁻¹, t_off ~6 s — **too slow for 1.2 ms** — and θ(25 nM) ≈ 93% (already occupied at tonic; cleft 1.1 mM cannot be a dynamic increment).
- Xiao SPR Kd 293 nM (C014): intermediate occupancy and a ~30 ms unbinding bound, still slower than 1.2 ms.

So “tighter” and “lower LOD” are not automatically better for dual-compartment dynamics. LOD (C002, C004, C014) is not occupancy. Hu’s 12 µM is a Wu citation, not a surface remeasurement (C021, C026). The 81-fold 10–90% Langmuir window is an occupancy identity (derived; C013 states it) and does not need a review as sole evidence.

This thesis **rejects** the slogan that aptamer quality is not a single number as the poster headline: the headline is that **the number the field advertises (LOD / nM apparent Kd) is the wrong number for the biological job**, and that we do not yet have glutamate kon/koff to replace the diffusion bound (C007).

## three decisive experiments

1. Measure kon/koff on Hu’s truncated Fc-thiol Glu-apt (method: IPA as in C008, numbers not transferred). If measured koff is ≫ 0.18 s⁻¹, the diffusion-limited bound using 1.8 nM as molecular Kd is false (the 1.8 nM figure is an electrochemical EC50, C005).
2. Solution Kd of that same truncated oligo (not 1d04). If it remains ~12 µM, Hu’s 1.8 nM is interface-dominated (C026); if it is nM, the SELEX isolate and the sensor oligo are different receptors (C001 vs C021).
3. Occupancy at 25 nM and 1.1 mM on one construct in 1× buffer (C012, C011), not 0.1× PBS (C014).

## one critical limitation

The inversion uses a **diffusion-limited kon bound** and treats electrochemical apparent Kd / SPR Kd as if they were molecular Kd. Both are labeled assumptions. C001 is abstract-only. Clements 1.1 mM / 1.2 ms is inference (C011). If kon is much slower than 10^8 M⁻¹ s⁻¹, even 12 µM is not fast. This thesis is stronger as a consistency check than as a kinetic measurement.

## one computational contribution

CPU occupancy + diffusion-limited koff bound, fully labeled SIMULATION / BOUND, empty cells for missing glutamate kon. Same atlas as other theses. No docking (C017). No InstructNA training (C016).

## six-panel storyboard

1. Wrong headline | “Too slow” is an unmeasured glutamate koff, not a result | C007, C009, C018 | Empty koff box beside a tobramycin/cocaine “architecture can be fast” card stamped NOT GLUTAMATE.
2. Construct split | 12 µM, 1.8 nM, 32 pM, 10 fM are different objects | C001, C002, C004, C005, C014, C021 | Identity cards; no average.
3. Occupancy inversion | µM Kd empty at 25 nM but potentially fast; nM apparent Kd full at 25 nM and slow under a diffusion bound | C001, C005, C012, C011 | Two Langmuir curves; caption SIMULATION/BOUND.
4. LOD is not occupancy | 32 pM / 10 fM / 0.0013 pM do not place θ at the synapse | C002, C004, C014 | LOD strip below the occupancy plot.
5. Interface rewrite | Truncation + Fc + thiol + 2D confinement | C026, C018, C015 | Hu sequence vs 1d04; Tanner tetrahedron as N-protein interface lesson only.
6. The experiment that would kill this thesis | IPA kon/koff on Glu-apt | C007, C008 | If measured t_off ≪ 6 s at nM Kd, the bound fails.

## three likely assessor attacks

1. “You invented glutamate kon from a diffusion limit.” Yes: it is a bound, not a measurement (C007). The poster must say BOUND.
2. “1.8 nM is not molecular Kd.” Agreed (C005 EC50). That is why experiment 1–2 exist; the inversion is a what-if on advertised numbers.
3. “Then the poster is just kinetics homework, not glutamate.” The inversion is glutamate-specific only because these particular published numbers (12 µM vs 1.8 nM vs 25 nM vs 1.1 mM) sit on opposite sides of tonic occupancy. That is the BIOC1600 point.
