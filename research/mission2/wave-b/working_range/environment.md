# Environment

- Python 3.10+ standard library (`csv`, `math`, `re`, `xml.etree.ElementTree`, `unittest`, `pathlib`).
- No pip packages.
- No paid APIs, no GPUs, no network on rebuild.
- Canonical input: `research/evidence/core_evidence.csv` already in the git worktree.
- Candidate basal poles are **package-local** (`candidates.py`), tagged `candidate`. They are not `claims.csv` rows.
