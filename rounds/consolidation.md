# Branch / PR / worktree consolidation

Generated: 2026-09-10

## Policy

The overnight cycle must end with one canonical branch containing all accepted work. Superseded PRs should be closed. Merging science onto `main` is a PI action.

## Inventory

| Artifact | Status |
| --- | --- |
| Canonical branch | `cursor/research-swarm-634f` |
| Base | `main` |
| Overnight science PR | https://github.com/bobshenruililin/BIOC1600-1/pull/2 |
| Plan branch / PR #1 | `cursor/save-research-plan-634f` — plan already in swarm history (`fa01d39`); superseded for science |
| Worktrees | none (`git worktree list` = this checkout only) |
| Extra analysis branches | none; analyses implemented on the canonical swarm branch |
| `main` | initial commit `bee2847` plus whatever GitHub has; science is not on `main` until PI merges |

## Actions

1. Confirm no accepted analysis exists only in a worktree.
2. Confirm nightly + ledgers + figures + scoreboard + audits are on `cursor/research-swarm-634f`.
3. Close PR #1 as superseded by PR #2 (plan is already in swarm history).
4. Keep PR #2 as the single overnight-cycle PR for PI review (mark ready after this handoff).
5. Do not merge swarm into `main` without PI. The PR tool cannot merge.

## Result

Canonical tree on `cursor/research-swarm-634f`. One open overnight science PR (#2) intended as the PI-review vehicle. PR #1 closed as superseded if the close action succeeds.

## Required artifact check

- `reports/nightly_summary.md`
- `research/evidence/core_evidence.csv`
- `state/claims.csv`
- `research/reviews/contradictions.md`
- figures under `analysis/accepted/figures/` with rebuildable source
- `state/scoreboard.json`
- `research/reviews/citation_audit.md`
- analysis READMEs
