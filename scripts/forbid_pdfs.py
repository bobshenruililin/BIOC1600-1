#!/usr/bin/env python3
"""Fail if copyrighted PDF binaries are tracked or present in the worktree."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    errors: list[str] = []
    for pdf in ROOT.rglob("*.pdf"):
        if ".git" in pdf.parts:
            continue
        errors.append(f"PDF present in worktree: {pdf.relative_to(ROOT)}")

    tracked = subprocess.run(
        ["git", "ls-files", "*.pdf"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    for line in tracked.stdout.splitlines():
        if line.strip():
            errors.append(f"PDF tracked by git: {line.strip()}")

    if errors:
        print("forbid_pdfs: FAIL")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("forbid_pdfs: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
