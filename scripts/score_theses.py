#!/usr/bin/env python3
"""Apply the locked thesis scoring weights. Do not change weights here."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

WEIGHTS = {
    "primary-evidence strength": 25,
    "BIOC1600 biochemical depth": 15,
    "critical insight": 15,
    "reproducibility": 15,
    "central-question relevance": 10,
    "visual explanatory power": 10,
    "Tanner intellectual alignment": 5,
    "novelty without overclaiming": 5,
}

DISCARD_BELOW = 75
FINALIST_AT = 85


def decision(total: float) -> str:
    if total >= FINALIST_AT:
        return "finalist"
    if total < DISCARD_BELOW:
        return "discard"
    return "hold"


def score_one(scores: dict[str, float]) -> dict:
    missing = [k for k in WEIGHTS if k not in scores]
    extra = [k for k in scores if k not in WEIGHTS]
    if missing or extra:
        raise ValueError(f"score keys mismatch; missing={missing} extra={extra}")
    total = 0.0
    for key, weight in WEIGHTS.items():
        value = float(scores[key])
        if value < 0 or value > weight:
            raise ValueError(f"{key}={value} outside 0–{weight}")
        total += value
    if abs(sum(WEIGHTS.values()) - 100) > 1e-9:
        raise RuntimeError("locked weights no longer sum to 100")
    return {"total": total, "decision": decision(total), "scores": scores}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path",
        nargs="?",
        help="JSON object or list of {id, scores} objects",
    )
    args = parser.parse_args()
    if not args.path:
        print(json.dumps({"weights": WEIGHTS, "discard_below": DISCARD_BELOW, "finalist_at": FINALIST_AT}))
        return 0
    payload = json.loads(Path(args.path).read_text(encoding="utf-8"))
    if isinstance(payload, dict) and "scores" in payload:
        payload = [payload]
    results = []
    for item in payload:
        results.append({"id": item.get("id"), **score_one(item["scores"])})
    print(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"score_theses: FAIL {exc}", file=sys.stderr)
        raise SystemExit(1)
