# Sensor engineer review (Round 2)

Role checklist applied by the orchestrator to verified claims. Not a ledger write.

## What is actually timed

| clock | example | quantity type |
| --- | --- | --- |
| Binding / occupancy equilibration | White thrombin 11–20 min; Xu/Tanner N-protein plateau ~25 min; Xiao 200 s stabilize | response_time |
| Assay incubation before a scan | Hu Glu 15 min, DA 10 min, ST 15 min | measurement_time |
| Electrochemical interrogation | Abeykoon IPA 2 ms; White cocaine dead time ~4 s | measurement_time |
| Enzyme-stack response | Rutherford 500–800 ms; Clay 0.73 / 0.8 s | response_time of **GlutOx**, not aptamer |
| Biological glutamate lifetime | Clements τ 1.2 ms; Armbruster free Glu vs iGluSnFR waveform | biology, not a sensor spec |

Hu’s 15 min is not a claim that the aptamer association is 15 min; it is the wait chosen as a signal/time compromise (Fig. 3f analog for ST; Fig. S8 for Glu/DA). It still cannot support millisecond neurotransmission as an achieved specification.

## Matrix and calibration

- Hu: PBS calibrations; aCSF recoveries 101.1–111.0%; 50% serum recoveries and serum LODs. Not undiluted brain ECF, not in vivo.
- Xiao: **0.1× PBS**. Debye-length and ionic-strength effects on FET small-molecule sensing are the whole point of the Nakatsuka 2018 literature (S017); transferring 10 fM in 0.1× PBS to cerebrospinal fluid is an architecture leap.
- Abrantes: aCSF in the abstract; clinical CSF claimed; preprint.

## Packing density and backfill

- Hu: PA immobilization 1.43 ± 0.37 × 10¹³ /cm² vs drop-cast 1.22 ± 0.44 × 10¹³ /cm²; thiol-PEG backfill; 5 min PA vs overnight drop-cast. Density was optimized for **ST** signal gain, then reused as a fabrication method for Glu/DA.
- White 2008: cocaine gain 60–200% and apparent Kd move with density; thrombin equilibration slows at high density.
- Xu/Tanner: DNA tetrahedron orientation changes apparent fiber Kd and gain for **N-protein**.

Immobilization is not a null operation. Do not quote a solution Kd as the sensor’s operating point.

## Fouling, drift, in-vivo leap

Hu PEG antifouling in 50% serum is real electrochemical evidence. “Substantial potential for in vivo monitoring” in the Hu abstract is a future-tense leap. Implantable aptamer FETs exist for 5-HT and DA (S018, S019), not glutamate in this ledger.

## Time-resolution budget (supported pieces only)

1. Biology: 1.2 ms cleft inference; ~25 nM ambient.
2. Enzyme glutamate sensors: 0.5–0.8 s.
3. Glutamate aptamer E-AB/FET: minutes (Hu) to hundreds of seconds (Xiao) in the inspected experiments.
4. Small-molecule E-AB **can** be interrogated in milliseconds (IPA) and, for some **non-glutamate** targets, equilibrate in seconds (White cocaine). That architecture lesson is transferable as a **method**, not as a glutamate kon.

A BIOC1600 assessor should not let the group say the glutamate aptamer is fast because tobramycin IPA is 2 ms.
