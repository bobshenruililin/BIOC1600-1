# BIOC1600-1

Aptamer-based biosensor research swarm for HKU BIOC1600 Topic 1.

This repository is a verified-evidence workspace, not a finished poster.

- Swarm operating manual: [`AGENTS.md`](AGENTS.md)
- Saved plan: [`.cursor/plans/aptamer_research_swarm_2114d7d1.plan.md`](.cursor/plans/aptamer_research_swarm_2114d7d1.plan.md)
- Specialist agents: [`.cursor/agents/`](.cursor/agents/)
- Evidence ledgers: [`state/`](state/) and [`research/evidence/core_evidence.csv`](research/evidence/core_evidence.csv)

```bash
python3 scripts/check_structure.py
python3 scripts/validate_ledgers.py
python3 scripts/forbid_pdfs.py
python3 -m unittest discover -s tests -v
```
