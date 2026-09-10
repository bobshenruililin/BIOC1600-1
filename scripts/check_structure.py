#!/usr/bin/env python3
"""Assert the Round 0 swarm tree exists."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENTS.md",
    ".cursor/rules/research-constitution.mdc",
    ".cursor/rules/scoring-rubric.mdc",
    ".cursor/rules/safety-and-integrity.mdc",
    ".cursor/agents/literature-scout.md",
    ".cursor/agents/evidence-extractor.md",
    ".cursor/agents/contradiction-hunter.md",
    ".cursor/agents/citation-auditor.md",
    ".cursor/agents/aptamer-biochemist.md",
    ".cursor/agents/sensor-engineer.md",
    ".cursor/agents/quant-modeler.md",
    ".cursor/agents/poster-red-team.md",
    ".cursor/agents/meta-improver.md",
    "state/sources.csv",
    "state/claims.csv",
    "state/scoreboard.json",
    "state/open_questions.md",
    "state/decisions.md",
    "state/model_config.json",
    "state/LOCKED_FILES.sha256",
    "research/evidence/core_evidence.csv",
    "poster/theses.md",
    "scripts/validate_ledgers.py",
    "scripts/forbid_pdfs.py",
    "scripts/score_theses.py",
    "scripts/check_structure.py",
    ".github/workflows/validate.yml",
]

REQUIRED_DIRS = [
    "research/scouts",
    "research/reviews",
    "analysis/candidates",
    "analysis/accepted",
    "poster/storyboards",
    "rounds",
    "scripts",
    ".cursor/agents",
    ".cursor/rules",
]

AGENT_READONLY = {
    "literature-scout": True,
    "evidence-extractor": True,
    "contradiction-hunter": True,
    "citation-auditor": True,
    "aptamer-biochemist": True,
    "sensor-engineer": True,
    "quant-modeler": False,
    "poster-red-team": True,
    "meta-improver": False,
}

FORBIDDEN_POSTER_GLOBS = [
    "poster/**/*.pptx",
    "poster/**/*.ai",
    "poster/**/*.psd",
    "poster/**/*final*",
]


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"missing file: {rel}")
    for rel in REQUIRED_DIRS:
        if not (ROOT / rel).is_dir():
            errors.append(f"missing directory: {rel}")

    for name, readonly in AGENT_READONLY.items():
        path = ROOT / ".cursor/agents" / f"{name}.md"
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        needle = f"readonly: {'true' if readonly else 'false'}"
        if needle not in text:
            errors.append(f"{path.name} must contain `{needle}`")
        if "model: cursor-grok-4.6-xhigh" not in text:
            errors.append(f"{path.name} must pin model: cursor-grok-4.6-xhigh")
        if "grok-4.7" in text:
            errors.append(f"{path.name} invents grok-4.7")

    theses = (ROOT / "poster/theses.md").read_text(encoding="utf-8")
    if "Round 3 pending" not in theses:
        errors.append("poster/theses.md must remain a Round 3 stub during bootstrap")

    claims = (ROOT / "state/claims.csv").read_text(encoding="utf-8").strip().splitlines()
    if len(claims) > 1:
        errors.append("Round 0 must not add scientific claim rows")

    sources = (ROOT / "state/sources.csv").read_text(encoding="utf-8").strip().splitlines()
    if len(sources) > 1:
        errors.append("Round 0 must not add source rows")

    for pattern in FORBIDDEN_POSTER_GLOBS:
        matches = list(ROOT.glob(pattern))
        if matches:
            errors.append(f"poster freeze violated: {matches}")

    if errors:
        print("check_structure: FAIL")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("check_structure: PASS")
    print(f"  files={len(REQUIRED_FILES)} dirs={len(REQUIRED_DIRS)} agents={len(AGENT_READONLY)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
