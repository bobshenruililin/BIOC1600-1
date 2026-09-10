# Thesis scoring reconciliation

Two scoring stacks exist. They do **not** agree. The provisional winner remains T1 only as an orchestrator dual-pass result. Isolated Task red-teamers invert the ranking. This is a PI decision, not a bug to paper over.

## Stack A — orchestrator dual-pass (recorded in `scores_r1.json`, `scores_r2.json`)

Stances: R1 oral-defensibility; R2 primary-hawk.

| id | R1 | R2 | mean | Stack A decision |
| --- | ---: | ---: | ---: | --- |
| T1 | 89 | 85 | 87 | winner (tie-break vs T5: fewer extra assumptions) |
| T5 | 89 | 85 | 87 | runner-up |
| T4 | 88 | 84 | 86 | hold |
| T2 | 87 | 83 | 85 | hold |
| T3 | 83 | 78 | 80.5 | hold |

## Stack B — isolated Task red-teamers (verbatim JSON in `scores_r1_task.json`, `scores_r2_task.json`)

| id | Task R1 | Task R2 | mean | Stack B notes |
| --- | ---: | ---: | ---: | --- |
| T3 | 86 | 78 | 82.0 | Task R1 sole finalist / winner |
| T4 | 84 | 85 | 84.5 | Task R2 finalist |
| T5 | 80 | 85 | 82.5 | Task R2 co-finalist / winning-looking |
| T2 | 82 | 81 | 81.5 | hold both |
| T1 | 79 | 83 | 81.0 | Task R1 last; Task R2 not a finalist |

None discarded by either stack (all ≥75).

## What is not allowed

- Averaging Stack A and Stack B into a fake consensus winner.
- Silently keeping T1 while deleting Task JSON.
- Promoting T3 because one scorer liked the 81-fold slogan (C027 already derives it; T3’s load-bearing use of Rousseau was the original hawk objection).

## Scientific objections from Task scorers that **are** adopted into the science (independent of ranking)

1. Hu 1.8 nM is Langmuir–Freundlich EC50; 1:1 81-fold overlay needs a caption.
2. Empirical SM-aptamer kon (C008/C010) contradicts T5’s 0.8 ms 1d04 story. Sensitivity figure added.
3. τ_eq = 1/(kon c + koff) at 1.1 mM is not t_off.
4. Herman 25 nM and Clements 1.1 mM / 1.2 ms are not one biological specification.
