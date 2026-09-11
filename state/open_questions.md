# Open questions

## Process

- Custom `.cursor/agents/` types are not registered in the Task tool; fallback remains `generalPurpose`.
- Two scoring stacks exist. Stack A: `rounds/03/scores_r1.json` + `scores_r2.json`. Stack B: `scores_r1_task.json` + `scores_r2_task.json`. They invert the ranking. Do not average them.
- Isolated analysis worktrees were not left unmerged: implementations live on the swarm branch so the handoff is reproducible from one tree.

## Science (unresolved)

- Glutamate aptamer kon/koff (C007)
- In vivo glutamate aptamer sensor (C020); S066 is in vitro retina
- Wu VoR truncation biochemistry beyond the abstract
- Whether Hu 1.8 nM EC50 may be used as an occupancy Kd even as a bound. Mission 1: **no** as a 1:1 tissue occupancy Kd of the PaC probe (chip→probe and LF→1:1 hops). Sensitivity band across 1.8 nM–12 µM remains a computational illustration.
- Amino-acid selectivity ratios (glutamate vs aspartate/glutamine) on the Hu/Xiao constructs (C032: those competitors were not in the thesis panel). W1 rejected as a fifth title; still a named FoM.
- Probe 3: occupancy ceiling vs gold-nanostructure loss (S066 Fig. 6.16)
- PaC-probe apparent Kd in Ames/tissue (empty)
- GCL/IPL-border electrode vs photoreceptor-terminal narrative (S066)
- Whether a diffusion-limited kon is an acceptable poster assumption given C008/C010
- Which scoring stack is the group’s
