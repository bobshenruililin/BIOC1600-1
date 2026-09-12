#!/usr/bin/env python3
"""SI concentration tokens. Empty or unparseable strings stay empty."""

from __future__ import annotations

import math
import re

PREFIX_TO_M = {
    "a": 1e-18,
    "f": 1e-15,
    "p": 1e-12,
    "n": 1e-9,
    "u": 1e-6,
    "µ": 1e-6,
    "μ": 1e-6,
    "m": 1e-3,
    "": 1.0,
}

CONC_TOKEN_RE = re.compile(r"([0-9]+(?:\.[0-9]+)?)\s*([aAfFpPnNuUµμ]|m)?M")
SPAN_RE = re.compile(
    r"([0-9]+(?:\.[0-9]+)?\s*[aAfFpPnNuUµμm]?M)"
    r"\s*[–—−-]\s*"
    r"([0-9]+(?:\.[0-9]+)?\s*[aAfFpPnNuUµμm]?M)"
)


def parse_conc_token(token: str) -> float | None:
    text = (token or "").strip()
    match = re.fullmatch(CONC_TOKEN_RE, text)
    if not match:
        return None
    coef = float(match.group(1))
    raw_prefix = match.group(2) or ""
    key = raw_prefix.replace("μ", "µ")
    if key == "µ":
        key = "u"
    else:
        key = key.lower()
    if key not in PREFIX_TO_M:
        return None
    return coef * PREFIX_TO_M[key]


def parse_conc_value_units(value: str, units: str) -> float | None:
    value = (value or "").strip()
    units = (units or "").strip()
    if not value:
        return None
    if units.lower() == "span":
        return None
    return parse_conc_token(f"{value} {units}".strip())


def extract_span_displays(text: str) -> tuple[str, str] | None:
    match = SPAN_RE.search(text or "")
    if not match:
        return None
    return match.group(1).strip(), match.group(2).strip()


def parse_span(text: str) -> tuple[float, float] | None:
    displays = extract_span_displays(text)
    if displays is None:
        return None
    lo = parse_conc_token(displays[0])
    hi = parse_conc_token(displays[1])
    if lo is None or hi is None or lo <= 0 or hi <= 0 or lo >= hi:
        return None
    return lo, hi


def format_fold(ratio: float) -> str:
    if ratio <= 0 or not math.isfinite(ratio):
        return ""
    nearest = round(ratio)
    if math.isclose(ratio, nearest, rel_tol=1e-8, abs_tol=1e-8):
        return str(int(nearest))
    nearest_tenth = round(ratio, 1)
    if math.isclose(ratio, nearest_tenth, rel_tol=1e-8, abs_tol=1e-8):
        return f"{nearest_tenth:.1f}"
    nearest_hundredth = round(ratio, 2)
    if math.isclose(ratio, nearest_hundredth, rel_tol=1e-6, abs_tol=1e-8):
        return f"{nearest_hundredth:.2f}"
    return f"{ratio:.3g}"


def contains(lo_M: float, hi_M: float, conc_M: float) -> bool:
    return lo_M <= conc_M <= hi_M


def ceiling_fold_below(hi_M: float, pole_M: float) -> float | None:
    if hi_M < pole_M:
        return pole_M / hi_M
    return None
