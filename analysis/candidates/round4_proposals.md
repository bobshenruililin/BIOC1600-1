# Round 4 analysis proposals (drafted after Round 2 evidence; scored after Round 3)

Six required families. None is pre-selected. Docking is included only as a **rejected** foil. InstructNA training is out of scope.

Scoring (locked, 0–10 each): scientific relevance; required assumptions; public data; no paid resources; reproducibility; visual value; first-year explainability; low misleading-interpretation risk.

## P1. Equal-Kd / different-kinetics Langmuir ODE vs biological timescales

**Question.** If two aptamers share Kd but differ in kon/koff, which (if either) could follow a 1.2 ms cleft transient vs a 15 min assay wait?

**Method.** Mass-action 1:1 binding ODE; occupancy θ = [AL]/[L]tot. Drive with (a) Clements-like 1.1 mM decaying τ=1.2 ms pulse (labeled **literature-derived stimulus**, not a new measurement) and (b) a step to Hu calibration concentrations. Scan kon along Ding’s surveyed order of magnitude **as a sensitivity axis**, never as glutamate data. Label every curve SIMULATION.

**Data.** C011, C006, C007, C010, C008. No fabricated Glu kon.

**Risk.** Viewers may read simulated kon as measured glutamate kinetics. Caption must say the opposite.

## P2. Structured evidence atlas from core_evidence.csv

**Question.** Which quantity types actually exist for which glutamate constructs?

**Method.** Plot construct × quantity_type with empty cells left empty. No interpolation. Separate biological [Glu] from sensor LOD.

**Data.** `research/evidence/core_evidence.csv` only.

**Risk.** Low if empty cells stay empty. High if a heatmap invents colors for missing kon.

## P3. Construct-change audit 1d04 → glu1 → Hu Glu-apt → Xiao FET

**Question.** What was chemically changed at each step, and which number belongs to which molecule?

**Method.** Table/flowchart: sequence modifications (truncation, thiol, Fc), matrix, quantity type, locator. Include Hu methods citation of Wu 12 µM as a **citation edge**, not a measurement.

**Data.** C001, C002, C004, C005, C014, C021, C026.

**Risk.** Drawing a single “affinity improvement” arrow from 12 µM to 32 pM.

## P4. Kinetic sensitivity / time-resolution budget

**Question.** Where in a time budget (binding vs interrogation vs incubation vs biology) does each paper sit?

**Method.** Log-time axis: 1.2 ms; IPA 2 ms; GlutOx 0.5–0.8 s; Xiao 200 s; Hu 15 min; White thrombin 11–20 min. Group by molecule class.

**Data.** C006, C009, C011, C014, C022, C023, C024, C018.

**Risk.** Plotting tobramycin IPA on the same glyph as glutamate.

## P5. Lightweight CPU HT-SELEX count illustration

**Question.** What does a responsible computational contribution look like without claiming a glutamate aptamer was designed?

**Method.** FASTAptamer-style count/enrichment on a **tiny bundled public example or synthetic labeled counts**. Do not train InstructNA. Compare qualitatively to C016 (many generated sequences fail SPR).

**Data.** S043 methods; C016 as the wet-lab caution. If no licensed public FASTQ can be bundled, use a fully labeled toy count table and say so.

**Risk.** Implying we designed a glutamate aptamer.

## P6. Responsible AI-design demo tagged hypothesis generation

**Question.** What must a poster say if it shows InstructNA/Abrantes?

**Method.** One panel: InstructNA protein SPR hit/miss counts (C016) + Xie docking selectivity failure (C017) + Abrantes preprint 1 aM LOD (C025) as **unvalidated device claim**. No new docking.

**Data.** C016, C017, C025.

**Risk.** Decorative 3D pose. This proposal exists to **block** that failure mode.

## Foil (do not implement as flagship)

Molecular docking of a glutamate aptamer. Rejected: C017; no Glu crystal; constitution forbids docking-as-proof.
