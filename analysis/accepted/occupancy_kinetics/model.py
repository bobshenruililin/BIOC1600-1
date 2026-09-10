#!/usr/bin/env python3
"""1:1 occupancy identities and a diffusion-limited koff bound.

Every kinetic output is a BOUND or SIMULATION. Glutamate kon/koff were not measured.
"""

from __future__ import annotations

import math

# Physical-chemistry upper bound for small-molecule bimolecular association
# in water (order-of-magnitude). Not a glutamate aptamer measurement.
KON_DIFFUSION_M_S = 1.0e8
# Empirical small-molecule aptamer kon envelope already in the ledger.
# NOT glutamate. C010 Ding ITC abstract endpoints; C008 tobramycin IPA.
KON_ITC_LOW_M_S = 96.0
KON_ITC_HIGH_M_S = 2.0e5
KON_TOBRAMYCIN_IPA_M_S = 3.5e4

KD_1D04_M = 12e-6
KD_HU_APPARENT_M = 1.8e-9
KD_XIAO_SPR_M = 293e-9
C_TONIC_M = 25e-9
C_CLEFT_M = 1.1e-3
TAU_CLEFT_S = 1.2e-3
HU_WAIT_S = 15 * 60
XIAO_STABILIZE_S = 200.0


def occupancy(conc_m: float, kd_m: float) -> float:
    if kd_m <= 0:
        raise ValueError("Kd must be positive")
    return conc_m / (conc_m + kd_m)


def langmuir_span_10_90(kd_m: float) -> tuple[float, float, float]:
    """Concentrations at 10% and 90% occupancy and their ratio (exactly 81)."""
    c10 = kd_m / 9.0
    c90 = 9.0 * kd_m
    return c10, c90, c90 / c10


def koff_diffusion_bound(kd_m: float, kon: float = KON_DIFFUSION_M_S) -> float:
    return kon * kd_m


def toff_diffusion_bound(kd_m: float, kon: float = KON_DIFFUSION_M_S) -> float:
    koff = koff_diffusion_bound(kd_m, kon)
    return 1.0 / koff


def tau_eq(conc_m: float, kd_m: float, kon: float) -> float:
    """Equilibration time 1/(kon c + koff) with koff = kon Kd. SIMULATION.

    At c << Kd this collapses to t_off. At cleft-scale c it can be much faster
    than t_off. Do not quote koff ≈ 1/τ_cleft as the FoM.
    """
    if kon <= 0 or kd_m <= 0:
        raise ValueError("kon and Kd must be positive")
    koff = kon * kd_m
    return 1.0 / (kon * conc_m + koff)


def euler_occupancy(
    conc_fn,
    t_end: float,
    dt: float,
    kon: float,
    koff: float,
    theta0: float = 0.0,
) -> tuple[list[float], list[float]]:
    """Forward Euler for dθ/dt = kon c (1-θ) - koff θ. SIMULATION."""
    n = int(t_end / dt)
    times = [0.0]
    theta = [theta0]
    th = theta0
    t = 0.0
    for _ in range(n):
        c = conc_fn(t)
        th = th + dt * (kon * c * (1.0 - th) - koff * th)
        th = min(1.0, max(0.0, th))
        t += dt
        times.append(t)
        theta.append(th)
    return times, theta


def cleft_pulse(t: float) -> float:
    """Literature-derived stimulus: 25 nM + 1.1 mM decaying with τ=1.2 ms. Not a new measurement."""
    if t < 0:
        return C_TONIC_M
    return C_TONIC_M + C_CLEFT_M * math.exp(-t / TAU_CLEFT_S)


CONSTRUCTS = {
    "1d04_Kd_12uM": KD_1D04_M,
    "Hu_apparent_1.8nM": KD_HU_APPARENT_M,
    "Xiao_SPR_293nM": KD_XIAO_SPR_M,
}
