#!/usr/bin/env python3
"""Langmuir–Freundlich 10–90% span identities.

MODELED. Hu's heterogeneity exponent n is unpublished. This package does not
fit n, does not restore occupancy-at-basal as a finding, and does not treat
Herman 25 nM and Clements 1.1 mM as a retinal or device specification.

Convention: θ = c^n / (Kd^n + c^n), so Kd is the concentration at θ = 0.5
for any n > 0. At n = 1 this is 1:1 Langmuir.
"""

from __future__ import annotations

import math

# Literature-example poles already in the canonical ledger. Different
# hippocampal preparations. Not a retinal range. Not a device spec.
C_HERMAN_SLICE_M = 25e-9
C_CLEMENTS_CULTURE_M = 1.1e-3
HERMAN_CLEMENTS_RATIO = C_CLEMENTS_CULTURE_M / C_HERMAN_SLICE_M  # 44000

# AuED-MEA Langmuir–Freundlich apparent electrochemical c50 in PBS (C005).
# Not PaC-probe molecular Kd. Used only to show n-sensitivity of a withdrawn overlay.
KD_HU_AUED_MEA_APPARENT_M = 1.8e-9

LANGMUIR_SPAN = 81.0


def lf_occupancy(conc_m: float, kd_m: float, n: float) -> float:
    if kd_m <= 0 or n <= 0:
        raise ValueError("Kd and n must be positive")
    if conc_m < 0:
        raise ValueError("concentration must be non-negative")
    cn = conc_m**n
    kdn = kd_m**n
    return cn / (cn + kdn)


def lf_span_10_90(kd_m: float, n: float) -> tuple[float, float, float]:
    """c10, c90, and c90/c10 = 81^(1/n), independent of Kd."""
    if kd_m <= 0 or n <= 0:
        raise ValueError("Kd and n must be positive")
    c10 = kd_m * (1.0 / 9.0) ** (1.0 / n)
    c90 = kd_m * 9.0 ** (1.0 / n)
    return c10, c90, c90 / c10


def lf_span_ratio(n: float) -> float:
    if n <= 0:
        raise ValueError("n must be positive")
    return LANGMUIR_SPAN ** (1.0 / n)


def n_for_span_ratio(ratio: float) -> float:
    """n such that 10–90% span equals `ratio`. MODELED inverse."""
    if ratio <= 1:
        raise ValueError("ratio must be > 1")
    return math.log(LANGMUIR_SPAN) / math.log(ratio)


def n_for_herman_clements_span() -> float:
    """n at which 10–90% span equals the labeled 44000-fold literature-example ratio."""
    return n_for_span_ratio(HERMAN_CLEMENTS_RATIO)
