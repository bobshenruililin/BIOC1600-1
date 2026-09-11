#!/usr/bin/env python3
"""A4 measurement-operator identities. No glutamate kon/koff.

Every time-domain trace is a LITERATURE STIMULUS or a labeled averaging
window applied to that stimulus. None of this is a PaC-probe recording.
"""

from __future__ import annotations

import math

from ledger import LedgerClocks


def literature_stimulus_m(t_s: float, clocks: LedgerClocks) -> float:
    """Basal + peak * exp(-t/τ) for t >= 0.

    LITERATURE STIMULUS constructed from E034 + E032 decaying with E033.
    Not a new measurement. Not [Glu] at a GCL-positioned electrode.
    """
    if t_s < 0:
        return clocks.basal_m
    return clocks.basal_m + clocks.peak_m * math.exp(-t_s / clocks.tau_s)


def clock_ratio(clock_s: float, tau_s: float) -> float:
    """Dimensionless T/τ. A clock ratio, not a koff."""
    if tau_s <= 0 or clock_s < 0:
        raise ValueError("tau must be positive and clock non-negative")
    return clock_s / tau_s


def nyquist_interval_s(tau_s: float) -> float:
    """COMPUTATIONAL ILLUSTRATION: τ/2 as a Nyquist-style sketch.

    An exponential is not band-limited, so this is not a Shannon reconstruction
    theorem. It is a first-year inequality: sampling much slower than τ cannot
    recover a τ-scale waveform. Not a sensor spec.
    """
    if tau_s <= 0:
        raise ValueError("tau must be positive")
    return 0.5 * tau_s


def interrogation_allows_shape(interrogation_s: float, tau_s: float) -> bool:
    return interrogation_s <= nyquist_interval_s(tau_s)


def sampling_allows_shape(sampling_s: float, tau_s: float) -> bool:
    return sampling_s <= nyquist_interval_s(tau_s)


def shape_reconstructable(interrogation_s: float, sampling_s: float, tau_s: float) -> bool:
    """False unless both architecture clocks sit at or below the Nyquist sketch."""
    return interrogation_allows_shape(interrogation_s, tau_s) and sampling_allows_shape(
        sampling_s, tau_s
    )


def axis_occupancy_fraction(event_s: float, window_s: float) -> float:
    """Fraction of a linear axis occupied by an event of duration event_s."""
    if window_s <= 0:
        raise ValueError("window must be positive")
    return event_s / window_s


def rectangular_window_mean_m(window_s: float, clocks: LedgerClocks) -> float:
    """Exact mean of the literature stimulus over [0, window_s].

    COMPUTATIONAL ILLUSTRATION of temporal averaging only.
    Do not write this mean onto a figure as nM at the electrode.
    Spatial dilution is unmeasured and is not modeled.
    """
    if window_s <= 0:
        raise ValueError("window must be positive")
    peak_integral = clocks.peak_m * clocks.tau_s * (1.0 - math.exp(-window_s / clocks.tau_s))
    return clocks.basal_m + peak_integral / window_s


def pulse_width_to_one_percent_s(clocks: LedgerClocks) -> float:
    """Time for the exponential peak term to fall to 1% (ln(100)*τ)."""
    return math.log(100.0) * clocks.tau_s
