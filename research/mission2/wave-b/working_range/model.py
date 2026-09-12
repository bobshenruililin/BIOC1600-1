#!/usr/bin/env python3
"""Occupancy-window algebra and bar-vs-pole arithmetic.

Langmuir–Freundlich form used here (Kd is c50 for any n):

    θ = c^n / (Kd^n + c^n),  n > 0, Kd > 0

Then θ/(1−θ) = (c/Kd)^n, so the 10–90% occupancy span is 81^(1/n).

This is MODELED occupancy geometry. It is not a device calibration bar.
Hu 1.8 nM (C005) is an electrochemical EC50, not occupancy Kd.
Hu fitted n is UNKNOWN. Do not restore 81-versus-44000 as flagship.
"""

from __future__ import annotations

import math

from units import ceiling_fold_below, contains, format_fold


def lf_occupancy(conc_M: float, kd_M: float, n: float) -> float:
    if kd_M <= 0 or n <= 0 or conc_M < 0:
        raise ValueError("kd_M and n must be positive; conc_M must be >= 0")
    cn = conc_M**n
    kn = kd_M**n
    return cn / (cn + kn)


def occupancy_c10_c90(kd_M: float, n: float) -> tuple[float, float]:
    """Concentrations at θ=0.1 and θ=0.9 when Kd is c50."""
    if kd_M <= 0 or n <= 0:
        raise ValueError("kd_M and n must be positive")
    factor = 9.0 ** (1.0 / n)
    return kd_M / factor, kd_M * factor


def occupancy_span_10_90(n: float) -> float:
    """c90/c10 = 81^(1/n). Kd cancels."""
    if n <= 0:
        raise ValueError("n must be positive")
    return 81.0 ** (1.0 / n)


def n_for_span(ratio: float) -> float:
    """n such that 81^(1/n) equals ratio. Inverse algebra, not a fitted n."""
    if ratio <= 1:
        raise ValueError("ratio must be > 1")
    return math.log(81.0) / math.log(ratio)


def verdict(lo_M: float, hi_M: float, pole_M: float) -> dict[str, str]:
    out = {"contains": "", "ceiling_fold_below": "", "note": ""}
    if contains(lo_M, hi_M, pole_M):
        out["contains"] = "yes"
        return out
    out["contains"] = "no"
    fold = ceiling_fold_below(hi_M, pole_M)
    if fold is not None:
        out["ceiling_fold_below"] = format_fold(fold)
        out["note"] = f"ceiling {out['ceiling_fold_below']}-fold below pole"
    elif lo_M > pole_M:
        out["note"] = "floor above pole"
    return out
