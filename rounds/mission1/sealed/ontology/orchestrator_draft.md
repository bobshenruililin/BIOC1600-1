# Quantity ontology draft (orchestrator; to merge with O1/O2)

Ledger schema (`validate_ledgers.py` QUANTITY_TYPES) is too coarse. Allowed fields:
Kd_molecular, kon, koff, EC50, sensor_LOD, analytical_working_range, signal_gain, response_time, measurement_time, biological_concentration_range.

## Required quantities

### molecular Kd
- Def: equilibrium dissociation constant of a specified oligo–ligand pair in a specified phase; for 1:1, Kd = koff/kon = c(θ=0.5).
- Method: ITC, SPR, fluorescence titration, SELEX-follow-up binding assay — not blank+3SD.
- Constructs: 1d04 12 µM (S001 abstract); Xiao SPR 293 nM (S021). Hu 12 µM is a **citation of Wu**, not a molecular Kd of the Fc-thiol surface oligo.
- Units: concentration.
- Biology: sets occupancy θ=c/(c+Kd) only if the same construct, phase, and 1:1 mechanism apply.
- Confused with: LOD, apparent Kd, EC50.
- Cross-paper: illegitimate unless construct+method+matrix match.

### surface apparent Kd
- Def: concentration at half-maximal **transduced signal** on a surface ensemble; may include crowding, 2D confinement, heterogeneous sites.
- Method: isotherm of sensor signal (often hyperbolic or Langmuir–Freundlich).
- Example: White cocaine apparent Kd vs packing density (E029); Hu 1.8 nM authors call apparent Kd from Langmuir–Freundlich.
- Confused with molecular Kd.
- Cross-paper: no.

### EC50
- Def: concentration at 50% of fitted effect; mechanism-agnostic.
- Ledger stores Hu 1.8 nM as EC50 (C005) — correct bucket, still not 1:1 Kd.
- Receptor example: Herman NMDAR Glu EC50 1.8 µM in nucleated patches (E035) — **not** an aptamer number; coincidentally same 1.8 with different units/meaning.

### LOD
- Def: typically blank mean + 3 SD (or 3 RSD). Detection threshold of a **signal**, not occupancy.
- Examples: Wu glu1 0.0013 pM; Hu MEA 32 pM PBS / 51.5 pM 50% serum; thesis probe 0.3 pM PBS (3 RSD); Xiao 10 fM 0.1× PBS; Abrantes 1 aM preprint.
- Hu Probe 3 saturates at basal despite 0.3 pM LOD — LOD does not imply working occupancy window in tissue.
- Cross-paper: no.

### working range
- Def: concentrations where the calibration is used (linear/semi-log span). Not 10–90% occupancy unless that is what was fitted.
- Hu MEA 0.1 nM–10 µM PBS; thesis PBS 1 nM–1 mM; Ames 10 nM–10 µM.
- 1:1 Langmuir 10–90% span is exactly 81-fold, independent of Kd — a different object.

### kon, koff
- Def: kon bimolecular association (M^-1 s^-1); koff unimolecular dissociation (s^-1); Kd=koff/kon for 1:1.
- Method: kinetic ITC, SPR, IPA under controlled mass transport.
- Glutamate aptamer: **not reported** (C007). C008 tobramycin IPA; C010 Ding mixed aptamers. Do not transfer.
- t_off = 1/koff. Occupancy table t_off uses assumed kon × advertised Kd — SIMULATION/BOUND.

### tau_eq
- Def: 1/(kon c + koff). Rising-edge equilibration time at concentration c.
- Not in ledger schema. At c >> Kd, tau_eq << t_off. koff ≈ 1/τ_cleft is the wrong FoM at 1.1 mM.

### response time
- Ambiguous: sensor t90, biological decay tau, indicator waveform, enzyme stack t90.
- Ledger dumps all of these into response_time (E033 Clements 1.2 ms is biological tau; E027 Xiao 200 s stabilize; E037 GlutOx 500–800 ms).
- Schema limitation: fatal if plotted as one axis without labels.

### recovery time
- Time to return toward baseline after concentration drop (dissociation + wash + interrogation).
- Hu: 3 min Ames rinse regenerates ~90% over three cycles — wash protocol, not koff.

### incubation time
- Wait after adding analyte before recording. Hu journal Glu 15 min; thesis 10 min plateau after 10 nM.
- Stored as measurement_time (E008, E042). Not koff.

### measurement/interrogation time
- Duration of the electrical/optical query. IPA 2 ms (E016); ACV scan 14 s (E045).
- Can be << or >> binding equilibration.

### sampling interval
- Time between consecutive quantitative points. Thesis retina ~1 min (E046). Distinct from 14 s scan.
- Schema: both stored as measurement_time — confusion.

### biological transient duration
- Lifetime of free glutamate in a compartment (Clements inferred 1.2 ms cleft). Not a sensor spec.

### ambient concentration
- Steady extracellular [Glu] with intact transport. Herman ~25 nM ambient/baseline in acute hippocampal slice. NOT extrasynaptic-only (repo once said so in rounds/01/merge_sources.py notes).

### peak concentration
- Clements inferred 1.1 mM cleft peak. Inference, culture, abstract-only.

## Repo confusions already found (O2 preview)
1. **Schema:** Clements 1.2 ms as response_time (core_evidence E033; atlas plots it under response_time). Caption warns; field name does not.
2. **Schema:** 14 s scan and 1 min sampling both measurement_time (E045 vs E046).
3. **Schema:** incubation 15 min / 10 min as measurement_time, same field as IPA 2 ms interrogation.
4. **Stale note:** rounds/01/merge_sources.py S050 notes still say “Tonic extrasynaptic ~25 nM” — contradicted by later auditor.
5. **Model overlay:** occupancy.py uses Hu 1.8 nM as 1:1 Langmuir Kd; captions say Langmuir–Freundlich / not 1:1. Honest if read; misleading if figure is used without caption.
6. **Herman NMDAR EC50 1.8 µM vs Hu 1.8 nM** — same digits, different objects (E035 vs E004). Easy oral trap.
7. **Atlas** is careful: empty kon/koff stay empty.
8. **C031 notes** already split 14 s vs 1 min.

Severity: 1–3 schema-limitation; 4 stale/misleading; 5 caption-dependent; 6 coincidence trap.
