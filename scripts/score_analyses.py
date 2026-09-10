#!/usr/bin/env python3
"""Apply the locked analysis-tournament rubric. Weights are equal 0–10 scales; do not change criteria."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CRITERIA = [
    "scientific relevance",
    "required assumptions",
    "availability of public data",
    "ability to run without paid resources",
    "reproducibility",
    "visual value",
    "ability of first-year students to explain it",
    "risk of misleading interpretation (higher score = lower risk)",
]


def score_one(scores: dict[str, float]) -> dict:
    missing = [k for k in CRITERIA if k not in scores]
    extra = [k for k in scores if k not in CRITERIA]
    if missing or extra:
        raise ValueError(f"score keys mismatch; missing={missing} extra={extra}")
    total = 0.0
    for key in CRITERIA:
        value = float(scores[key])
        if value < 0 or value > 10:
            raise ValueError(f"{key}={value} outside 0–10")
        total += value
    return {"total": total, "max": 80, "scores": scores}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", help="JSON object or list of {id, scores}")
    args = parser.parse_args()
    if not args.path:
        print(json.dumps({"criteria": CRITERIA, "each": "0-10", "max_total": 80}))
        return 0
    payload = json.loads(Path(args.path).read_text(encoding="utf-8"))
    if isinstance(payload, dict) and "scores" in payload:
        payload = [payload]
    print(json.dumps([{"id": item.get("id"), **score_one(item["scores"])} for item in payload], indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"score_analyses: FAIL {exc}", file=sys.stderr)
        raise SystemExit(1)
