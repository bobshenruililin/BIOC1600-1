import math
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from model import (
    C_CLEMENTS_CULTURE_M,
    C_HERMAN_SLICE_M,
    HERMAN_CLEMENTS_RATIO,
    KD_HU_AUED_MEA_APPARENT_M,
    LANGMUIR_SPAN,
    lf_occupancy,
    lf_span_10_90,
    lf_span_ratio,
    n_for_herman_clements_span,
    n_for_span_ratio,
)


class LangmuirFreundlichSpanTests(unittest.TestCase):
    def test_n1_is_langmuir_81(self):
        _, _, ratio = lf_span_10_90(1.8e-9, 1.0)
        self.assertAlmostEqual(ratio, LANGMUIR_SPAN, places=12)
        self.assertAlmostEqual(lf_span_ratio(1.0), 81.0, places=12)

    def test_span_independent_of_kd(self):
        r1 = lf_span_ratio(0.7)
        _, _, r2 = lf_span_10_90(12e-6, 0.7)
        _, _, r3 = lf_span_10_90(1.8e-9, 0.7)
        self.assertAlmostEqual(r1, r2, places=12)
        self.assertAlmostEqual(r2, r3, places=12)

    def test_endpoints_are_10_and_90(self):
        kd = 1e-6
        n = 0.6
        c10, c90, _ = lf_span_10_90(kd, n)
        self.assertAlmostEqual(lf_occupancy(c10, kd, n), 0.10, places=12)
        self.assertAlmostEqual(lf_occupancy(c90, kd, n), 0.90, places=12)
        self.assertAlmostEqual(lf_occupancy(kd, kd, n), 0.50, places=12)

    def test_n_half_span_is_6561(self):
        self.assertAlmostEqual(lf_span_ratio(0.5), 81.0**2, places=9)

    def test_n_two_span_is_9(self):
        self.assertAlmostEqual(lf_span_ratio(2.0), 9.0, places=12)

    def test_herman_clements_ratio_is_44000(self):
        self.assertAlmostEqual(HERMAN_CLEMENTS_RATIO, 44000.0, places=6)
        self.assertAlmostEqual(C_CLEMENTS_CULTURE_M / C_HERMAN_SLICE_M, 44000.0, places=6)

    def test_n_needed_for_44000_fold_is_below_one(self):
        n_star = n_for_herman_clements_span()
        self.assertAlmostEqual(n_star, math.log(81.0) / math.log(44000.0), places=12)
        self.assertLess(n_star, 0.42)
        self.assertGreater(n_star, 0.40)
        self.assertAlmostEqual(lf_span_ratio(n_star), 44000.0, places=6)

    def test_inverse_roundtrip(self):
        n = 0.8
        self.assertAlmostEqual(n_for_span_ratio(lf_span_ratio(n)), n, places=12)

    def test_withdrawn_overlay_is_n_sensitive(self):
        """MODELED overlay if 1.8 nM were c50. Not tissue occupancy."""
        th_n1 = lf_occupancy(C_HERMAN_SLICE_M, KD_HU_AUED_MEA_APPARENT_M, 1.0)
        th_lo = lf_occupancy(C_HERMAN_SLICE_M, KD_HU_AUED_MEA_APPARENT_M, 0.5)
        th_hi = lf_occupancy(C_HERMAN_SLICE_M, KD_HU_AUED_MEA_APPARENT_M, 2.0)
        self.assertGreater(th_n1, 0.9)
        self.assertLess(th_lo, th_n1)
        self.assertGreater(th_hi, th_n1)
        self.assertLess(th_lo, 0.85)

    def test_rejects_nonpositive_n(self):
        with self.assertRaises(ValueError):
            lf_span_ratio(0.0)
        with self.assertRaises(ValueError):
            lf_occupancy(1e-9, 1e-9, -1.0)


if __name__ == "__main__":
    unittest.main()
