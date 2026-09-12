import math
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from model import (
    C_CLEFT_M,
    C_TONIC_M,
    KD_1D04_M,
    KD_HU_APPARENT_M,
    KD_XIAO_SPR_M,
    KON_DIFFUSION_M_S,
    KON_ITC_HIGH_M_S,
    KON_ITC_LOW_M_S,
    KON_TOBRAMYCIN_IPA_M_S,
    cleft_pulse,
    euler_occupancy,
    koff_diffusion_bound,
    langmuir_span_10_90,
    occupancy,
    tau_eq,
    toff_diffusion_bound,
)


class OccupancyTests(unittest.TestCase):
    def test_81_fold_identity(self):
        _, _, ratio = langmuir_span_10_90(1.8e-9)
        self.assertAlmostEqual(ratio, 81.0, places=12)

    def test_1d04_nearly_empty_at_tonic(self):
        th = occupancy(C_TONIC_M, KD_1D04_M)
        self.assertLess(th, 0.01)

    def test_overlay_theta_at_herman_ambient_if_1p8nm_treated_as_1to1_kd(self):
        """Overlay math if 1.8 nM is treated as a 1:1 occupancy Kd. Not tissue occupancy."""
        th = occupancy(C_TONIC_M, KD_HU_APPARENT_M)
        self.assertGreater(th, 0.9)

    def test_herman_clements_span_is_44000_fold(self):
        self.assertAlmostEqual(C_CLEFT_M / C_TONIC_M, 44000.0, places=6)

    def test_cleft_occupies_1d04(self):
        th = occupancy(C_CLEFT_M, KD_1D04_M)
        self.assertGreater(th, 0.95)

    def test_xiao_partial_at_tonic(self):
        th = occupancy(C_TONIC_M, KD_XIAO_SPR_M)
        self.assertGreater(th, 0.05)
        self.assertLess(th, 0.15)

    def test_diffusion_bound_1d04_near_cleft_tau(self):
        t_off = toff_diffusion_bound(KD_1D04_M)
        self.assertLess(t_off, 2e-3)
        self.assertGreater(t_off, 5e-4)

    def test_diffusion_bound_hu_much_slower_than_cleft(self):
        t_off = toff_diffusion_bound(KD_HU_APPARENT_M)
        self.assertGreater(t_off, 1.0)

    def test_koff_is_kon_times_kd(self):
        self.assertAlmostEqual(koff_diffusion_bound(KD_XIAO_SPR_M), KON_DIFFUSION_M_S * KD_XIAO_SPR_M)

    def test_euler_equilibrium(self):
        kd = 1e-6
        kon = 1e7
        koff = kon * kd
        c = 1e-6

        def conc(_t):
            return c

        _, theta = euler_occupancy(conc, t_end=0.5, dt=1e-4, kon=kon, koff=koff, theta0=0.0)
        self.assertAlmostEqual(theta[-1], occupancy(c, kd), delta=0.02)

    def test_cleft_pulse_starts_near_peak(self):
        self.assertAlmostEqual(cleft_pulse(0.0), C_TONIC_M + C_CLEFT_M)
        self.assertLess(cleft_pulse(0.01), C_TONIC_M + 1e-5)

    def test_empirical_kon_makes_1d04_toff_seconds(self):
        t_high = toff_diffusion_bound(KD_1D04_M, KON_ITC_HIGH_M_S)
        t_tobra = toff_diffusion_bound(KD_1D04_M, KON_TOBRAMYCIN_IPA_M_S)
        t_low = toff_diffusion_bound(KD_1D04_M, KON_ITC_LOW_M_S)
        self.assertGreater(t_high, 0.4)
        self.assertGreater(t_tobra, 2.0)
        self.assertGreater(t_low, 100.0)

    def test_tau_eq_at_cleft_faster_than_toff(self):
        kon = KON_ITC_HIGH_M_S
        t_off = toff_diffusion_bound(KD_1D04_M, kon)
        t_rise = tau_eq(C_CLEFT_M, KD_1D04_M, kon)
        self.assertLess(t_rise, t_off / 10.0)
        self.assertLess(t_rise, 0.02)

    def test_tau_eq_at_tonic_near_toff_when_empty(self):
        kon = KON_ITC_HIGH_M_S
        t_off = toff_diffusion_bound(KD_1D04_M, kon)
        t_tonic = tau_eq(C_TONIC_M, KD_1D04_M, kon)
        self.assertAlmostEqual(t_tonic / t_off, 1.0, delta=0.05)


if __name__ == "__main__":
    unittest.main()
