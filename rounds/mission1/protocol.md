# Mission 1 — launch inventory and wave schedule

Branch: `cursor/story-tournament-634f`

Do not treat launch errors as negative research results.

## Runtime constraint

Effective async ceiling: **10** delegated agents. Project policy going forward: **8** concurrent, including premium-model subagents (`AGENTS.md`).

## Intended lanes

| Lane | Role | First-launch outcome | Later outcome |
| --- | --- | --- | --- |
| A1 | Fit-for-purpose steelman | launched | awaiting return |
| A2 | Fit-for-purpose red team | launched | awaiting return |
| A3 | Fit-for-purpose independent | launched | awaiting return |
| B1 | Construct-transformation steelman | **cap miss** | relaunched `bc-f16d3b77` |
| B2 | Construct-transformation red team | **cap miss** | relaunched `bc-7cb3dc5d` |
| B3 | Construct-transformation independent | launched | **complete** `bc-2dd31e8c` |
| C1 | LOD-paradox steelman | **cap miss** | relaunched `bc-053dfcf9` |
| C2 | LOD-paradox red team | **cap miss** | relaunched `bc-2496c55a` |
| C3 | LOD-paradox independent | launched | awaiting return |
| D1 | Scale-matching steelman | launched | **complete** `bc-8c323354` |
| D2 | Scale-matching red team | launched | **complete** `bc-6ee36931` |
| D3 | Scale-matching independent | **cap miss** | relaunched `bc-602c145b` |
| H1 | Hu retina logic reconstruction | **cap miss** | orchestrator filled from OA Ch.6/7; **Grok H1 still queued** (do not shrink to notes-only) |
| H2 | Hu retina adversarial | launched | **complete** `bc-1a969e5f` |
| H3 | Hu retina independent | launched | **complete** `bc-e396c51e` |
| O1 | Quantity ontology | launched | **complete** `bc-382a2220` |
| O2 | Repo quantity-confusion hunt | **cap miss** | relaunched `bc-7ed99a48` |
| W1 | Wildcard Glu vs Asp/Gln | **cap miss** | **still missing — next wave** |

Opus 5 story gate: not started. Premium review waits until the four program reports, Hu reconstruction, ontology, and wildcard exist.

## Still missing after cap repair (Wave 2, max 8, isolation)

1. **H1** — full experimental-logic reconstruction by an isolated Grok researcher that does not see H2/H3 or program theses. Orchestrator `/tmp` notes are a backup, not a substitute.
2. **W1** — amino-acid selectivity wildcard, isolated from program theses.

Do not relaunch B1/B2/C1/C2/D3/O2 unless those relaunch IDs fail to return. Do not relaunch completed lanes.

## Isolation for Wave 2

Wave 2 prompts must not include, and must not be allowed to read:

- `rounds/mission1/programs/`
- `rounds/mission1/sealed/`
- `/tmp/mission1*`
- prior thesis tournament files (`analysis/candidates/theses/`, `poster/theses.md`, `rounds/03`, `state/scoreboard.json`, `reports/nightly_summary.md`)

H1 may read `/tmp/hu_thesis_*.txt` and ledger C028–C032 / E042–E046 only.

## Gate

`state/gates/science_story.json` stays unwritten until required lanes complete or are documented as genuinely blocked.
