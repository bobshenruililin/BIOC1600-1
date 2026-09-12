#!/usr/bin/env python3
"""Measurement-operator identities. No glutamate kon/koff. No sampling-theorem claim.

Every time-domain trace is an INFERRED literature waveform or a labeled MODELED
window applied to that waveform. None of this is a PaC-probe recording.
"""

from __future__ import annotations

import math

from ledger import LedgerClocks


def inferred_clements_waveform_m(t_s: float, clocks: LedgerClocks) -> float:
    """peak * exp(-t/τ) for t >= 0; 0 for t < 0.

    INFERRED Clements-like decay from E032/E033. Not spliced with Herman 25 nM
    (E034). Not [Glu] at a GCL-positioned electrode.
    """
    if t_s < 0:
        return 0.0
    return clocks.peak_m * math.exp(-t_s / clocks.tau_s)


def clock_ratio(clock_s: float, tau_s: float) -> float:
    """Dimensionless T/τ. A clock ratio, not a koff."""
    if tau_s <= 0 or clock_s < 0:
        raise ValueError("tau must be positive and clock non-negative")
    return clock_s / tau_s


def timescale_mismatch(clock_s: float, tau_s: float) -> bool:
    """True when the architecture clock is longer than the literature τ.

    This is a coarse first-year inequality, not a reconstruction theorem.
    An exponential is not band-limited, the ACV scan is not a regular point
    sampler of [Glu](t), and no reconstruction operator is claimed.
    """
    if tau_s <= 0 or clock_s < 0:
        raise ValueError("tau must be positive and clock non-negative")
    return clock_s > tau_s


def shape_reporting_excluded(interrogation_s: float, sampling_s: float, tau_s: float) -> bool:
    """True unless both architecture clocks are at or below τ.

    Each clock is sufficient to exclude shape reporting of a τ-scale waveform.
    Instantaneous occupancy is a hypothetical measurement-operator assumption,
    not a glutamate rate.
    """
    return timescale_mismatch(interrogation_s, tau_s) or timescale_mismatch(sampling_s, tau_s)


def axis_occupancy_fraction(event_s: float, window_s: float) -> float:
    """Fraction of a linear axis occupied by an event of duration event_s."""
    if window_s <= 0:
        raise ValueError("window must be positive")
    return event_s / window_s


def pulse_width_to_one_percent_s(clocks: LedgerClocks) -> float:
    """Time for the exponential peak term to fall to 1% (ln(100)*τ). MODELED."""
    return math.log(100.0) * clocks.tau_s
