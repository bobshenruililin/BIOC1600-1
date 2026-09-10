# Aptamer biochemist review (Round 2)

Role checklist applied by the orchestrator to verified claims. Not a ledger write.

## Construct that was actually measured

- **1d04** (S001): Capture-SELEX isolate in complex medium; Kd 12 µM in the abstract. Sequence and truncation details are behind a closed VoR.
- **glu1** (S001): truncated, 3′-ferrocene, Au-thiol, MCH backfill. Sensor LOD/range, not a reported Kd in the abstract.
- **Hu Glu-apt** (S002): truncated Fc-thiol oligo `GCATCAGTCCACTCGTGAGGTCGACTGATGAGGCTCGAT`, labeled in the methods as Kd = 12 µM **citing Wu**. Hu then measures a Langmuir–Freundlich **apparent electrochemical Kd of 1.8 nM**. Authors attribute the gap in part to 2D confinement. That explanation is theirs; the numerical split is experimental vs citation.
- **Xiao glutamate aptamer** (S021): SPR Kd 293 nM (Table S1 sequence in SI, not copied here). FET uses the same family of probes on AuNP/CNT in 0.1× PBS.
- **NG-Apt-Glu** (S010 preprint): in silico designed; two putative binding sites claimed; not a SELEX lineage in the abstract.

Truncation was **not** shown in inspected Hu/Wu texts as a separate solution-phase Kd of the truncated oligo. Treating 12 µM as the surface construct’s molecular Kd is a biochemical oversimplification.

## SELEX vs assay conditions

Wu: selection in complex medium; sensor in unspecified LOD matrix plus 10-fold diluted serum selectivity (abstract). Hu: PBS calibration, then 50% serum and aCSF recovery. Xiao: 0.1× PBS. None of these is a synaptic cleft.

## Specificity vs related metabolites

Hu shows analog-molecule selectivity with targets two orders of magnitude lower than interferents (Fig. 5d) and multiplex crosstalk tests (ST/Glu/DA). That is electrochemical selectivity of the **sensor**, not a full metabolomic screen. Xiao reports paired interferent tests at 1 pM target vs 1 nM interferents. Abrantes abstract claims selectivity vs GABA, glutamine, dopamine, serotonin — preprint, not re-read beyond abstract.

Glutamine/aspartate/GABA discrimination at cleft-relevant millimolar glutamate is **not** established in the core Glu E-AB papers.

## Kd vs EC50 vs apparent affinity

Keep three buckets:

1. Solution/SPR molecular Kd (1d04 12 µM; Xiao 293 nM).
2. Surface electrochemical apparent Kd / Langmuir–Freundlich (Hu 1.8 nM; White cocaine apparent Kd vs density).
3. Device LOD (pM–aM), which can be a blank+3SD of a transduced signal, not occupancy.

Mixing (1) and (3) is the error a BIOC1600 assessor should punish.

## Predicted structures

InstructNA and Abrantes in silico sites are hypothesis. Xie/Liu show docking can invert selectivity. Do not draw a glutamate-aptamer binding pose as fact.
