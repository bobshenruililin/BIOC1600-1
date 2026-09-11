# Hu retina reconstruction (orchestrator H1, from OA Chapter 6/7 extract)

Source: Hu Z (2025) RWTH dissertation, DOI 10.18154/RWTH-2025-07238, OA PDF text extract. PDF not stored in git. Companion journal: Hu et al. Biosens. Bioelectron. 2025, 117992 (CC BY).

## Biological preparation
- In vitro mouse retina, not in vivo.
- Intraretinal probe: parylene-C, four shanks 50 µm wide × 225 µm long (matched to ~200–225 µm healthy mouse retina thickness), spaced 100 µm; each shank three electrodes: two Ø 15 µm (ephys) and bottom Ø 25 µm (Glu ACV).
- Insertion under ambient room light with micromanipulator; depth titrated by spike appearance on the large bottom electrode (NFL/GCL), then +20 µm steps; Z3 puts upper small electrode in GCL (~70 µm NFL+GCL+IPL).
- Probe fabricated by another doctoral researcher (Flores Cáceres); retina experiments acknowledged with Rincón Montes, Flores Cáceres, Kasavetov.
- Medium for tissue-relevant calibration: oxygenated Ames (carbogen ≥30 min, pH 7.4).

## What glutamate signal was interrogated
- Intended: light-dependent extracellular Glu in retina (photoreceptors depolarized/dark → Glu release; hyperpolarized/light → suppress Glu).
- Actually sampled: ACV current on the large bottom electrode after GCL positioning, consecutive scans until “steady state,” then light on–off–on.
- Authors’ own interpretation: **sustained basal Glu**, not synaptic transients.
- Optical pulses: 500 ms, used for **ephys vitality**, not for electrochemical Glu transients.

## Aptamer construct
- Glu-apt: 5′-HO-(CH2)6-S-S-(CH2)6- GCATCAGTCCACTCGTGAGGTCGACTGATGAGGCTCGAT -Fc-3′
- Probe oligos from Sangon. Same truncated Fc-thiol family as journal S002.
- Mixed monolayer with thiol-PEG. PA immobilization +0.5/+0.1 V, 1 s pulses, 5 min total; coverage 0.80±0.26×10^13 cm^-2.
- Journal methods label Kd = 12 µM citing Wu — citation, not a remeasurement of this surface construct.

## Sensor architecture
- Flexible PaC probe, Au electrodeposited nanostructures (large 60 s / small 40 s at 0.6 V).
- ESA increase 16-fold (large) and 7-fold (small). Z(1 kHz) after AuED: 20.2±3.8 kΩ large, 65.9±12.4 kΩ small.
- After aptamer: 76.5±5.5 kΩ; after PEG: 109.6±26.5 kΩ (large electrode).
- Dual-modal: Glu ACV on large bottom electrode; spikes on small upper electrode of the same probe.
- Different AuED/pzc than AuED-MEA chips; authors say immobilization must be re-optimized per layout.

## Matrix
- PBS calibration (1 nM–1 mM linear claimed; ACV shown 1 nM–2 mM).
- 50% human serum recovery 117.6%, 107%, 108.3% (n=3, standard addition).
- Ames: linear 10 nM–10 µM; blank noise 41.6% (3×RSD blank); adjacent-concentration signal change ~57%; authors: poor quantitative SNR vs PBS, but justified for relative changes.
- After insertion: ACV peak current drops vs pre-insertion (higher tissue impedance than Ames).

## Calibration / clocks
- 10 nM Glu wait-to-plateau ~10 min (Fig. 6.6); authors call this association/dissociation steady state and “time required to quantitatively determine Glu.” Not a fitted koff.
- PBS LOD 0.3 pM = mean blank + 3×RSD. Authors contrast >100× lower LOD and wider high-end range vs AuED-MEA (journal 32 pM).
- ACV 0–0.7 V, 0.05 V^-1 → **one point every 14 s**.
- In tissue: consecutive ACV at **1 min intervals** until steady, then light protocol.
- Regeneration: 3 min Ames wash, ~90% signal over three 100 nM cycles.

## Electrophysiology comparison
- Two sorted units on Probe 1 upper electrode. Light-off firing 6.34 Hz and 1.46 Hz; light-on 8.36 Hz and 2.8 Hz — interpreted as ON-pathway RGCs.
- 500 ms optical pulses time-lock spikes (tissue viability).
- Explicit: ephys has millisecond AP resolution; electrochemistry averages ~one minute per point. These are **not the same glutamate events**.

## Pharmacological manipulation
- Negative search in Chapter 6/7 extract: no TTX, CNQX, APV, NBQX, TBOA, or other Glu-receptor/transporter pharmacology. Light is the only intervention. Bibliography hits only.

## Selectivity
- Fig. 6.8A: 100 nM Glu vs 10 µM ST, DA, Tyr, Lac. Not aspartate, not glutamine, not GABA.

## Saturation / failure
- Four independent probes in Fig. 6.13.
- Probes 1–2: light-off increases signal vs light-on (p<0.05).
- Probe 3: no significant light-on vs off; authors: **near saturation at basal Glu**.
- Probe 4: unstable; ns light effect; broad IQR.
- Post-experiment: gold nanostructure detached; impedance up after insertion; authors link this to lost aptamer sites, early saturation, fouling.

## What authors claim
- Dual recording of ephys + electrochemical Glu in in vitro mouse retina.
- Light-dependent shifts in average extracellular Glu consistent with photoreceptor physiology.
- Probe 1/2 statistically distinguish light-on vs off.
- Platform for retinal physiology / neurochemical interactions.

## What authors decline / limit
- Ch. 6: “aptasensor captures sustained changes in basal Glu concentration, rather than the fast, transient release events associated with individual synaptic activity.”
- Ch. 7: “time resolution of the electrochemical aptasensor limits the detection of rapid, transient Glu release events, which typically occur on the millisecond to second scale in vitro.” “Current aptasensors lack the temporal resolution required to monitor NTs dynamics occurring on the sub-second scale.” Future needs fast kon/koff already at selection.
- Ames: not fine absolute quantification.
- Nanostructure stability under physiological conditions remains a major challenge; in vivo is outlook, not this experiment.

## Caption inconsistency
- Body §6.1: signal gain vs PA time tested at **10 nM Glu** (Fig. 6.5A narrative).
- Fig. 6.5 caption: signal gain to **100 nM Glu**.
- Record both; do not silently pick.

## Successful scientific question
Whether a Glu-apt E-AB on a flexible PaC intraretinal probe can report **light-dependent, minute-scale changes in sustained (basal) extracellular glutamate in an isolated mouse retina**, alongside RGC spiking, after PBS/Ames/serum calibration.

## Open questions
- Absolute [Glu] in tissue (Ames SNR; no in-tissue calibration; saturation).
- Causal identity of the ACV signal (no pharmacology; possible impedance/mechanical confounds).
- Glu vs Asp/Gln.
- kon/koff of this construct.
- Synaptic transients (authors decline).
- Why Probe 3 saturates if PBS LOD is 0.3 pM / Ames window includes 10 nM–10 µM.
- In vivo, nuclease stability, multiplex on this probe.

## Falsifier for over-reading
If the light-off ACV increase survives Glu-receptor/transporter block but dies with electrode impedance-only controls, the neurochemical claim fails. If a sub-second interrogation with measured koff tracks 500 ms optical-evoked Glu, the “basal-only” limitation would need revision.
