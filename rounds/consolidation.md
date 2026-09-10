# Branch / PR / worktree consolidation

Generated: 2026-09-10. Mandatory final handoff gate.

## Inventory (before merge)

| Artifact | Status |
| --- | --- |
| Swarm branch | `cursor/research-swarm-634f` — all accepted science |
| Plan branch | `cursor/save-research-plan-634f` at `fa01d39` — **ancestor of swarm**; not deleted |
| Worktrees | this checkout only |
| Extra analysis branches | none |
| PR #1 | closed (superseded); plan commit already in swarm |
| PR #2 | open overnight science PR targeting `main` |

No accepted analysis existed only in a worktree or on an unmerged branch.

## Figure selection (not “latest file”)

Selected **three** for the handoff (strongest, not a fourth dump):

1. `analysis/accepted/figures/atlas.svg` — ledger construct×quantity atlas; empty kon/koff stay empty.
2. `analysis/accepted/figures/occupancy.svg` — Langmuir occupancy SIMULATION; units on θ and [Glu].
3. `analysis/accepted/figures/sensitivity.svg` — t_off vs kon BOUND/SIMULATION; empirical band labeled NOT glutamate. This is the analysis that is not a literature recap.

Supporting, still rebuilt, not in the “best 3”: `clocks.svg` (15 min vs 1.2 ms category error).

## Merge required by this gate

The gate requires **no unresolved overnight-cycle PR**. ManagePullRequest cannot merge. Fast-forward `main` to the swarm tip (linear history from `bee2847`) so PR #2 can close as merged. The plan branch is kept because deleting it would only tidy optics; its commit is already in history.

## Result (filled after push)

See `reports/nightly_summary.md` section 12 for the canonical SHA.
