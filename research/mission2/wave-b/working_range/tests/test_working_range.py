import csv
import math
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from candidates import CANDIDATE_POLES
from figures import (
    CAPTION,
    LF_CAPTION,
    basal_sensitivity_rows,
    classify_vs_canonical,
    glyph_note,
    lf_n_svg,
    n_sensitivity_identity_rows,
    range_table_rows,
    working_range_svg,
)
from ledger import find_repo, load_canonical_poles, load_ledger, load_range_bars, pole_by_id
from model import lf_occupancy, n_for_span, occupancy_c10_c90, occupancy_span_10_90, verdict
from units import contains, format_fold, parse_conc_token, parse_span

CSV = find_repo(Path(__file__).resolve()) / "research/evidence/core_evidence.csv"


class ParseTests(unittest.TestCase):
    def test_si_prefixes(self):
        self.assertAlmostEqual(parse_conc_token("1 aM"), 1e-18)
        self.assertAlmostEqual(parse_conc_token("10 fM"), 1e-14)
        self.assertAlmostEqual(parse_conc_token("0.01 pM"), 1e-14)
        self.assertAlmostEqual(parse_conc_token("0.3 pM"), 0.3e-12)
        self.assertAlmostEqual(parse_conc_token("1 nM"), 1e-9)
        self.assertAlmostEqual(parse_conc_token("25 nM"), 25e-9)
        self.assertAlmostEqual(parse_conc_token("10 µM"), 1e-5)
        self.assertAlmostEqual(parse_conc_token("1.8 µM"), 1.8e-6)
        self.assertAlmostEqual(parse_conc_token("1.1 mM"), 1.1e-3)
        self.assertAlmostEqual(parse_conc_token("1 mM"), 1e-3)
        self.assertAlmostEqual(parse_conc_token("9.4 µM"), 9.4e-6)
        self.assertAlmostEqual(parse_conc_token("34.7 µM"), 34.7e-6)

    def test_en_dash_and_hyphen_spans(self):
        lo, hi = parse_span("0.01 pM–1 nM")
        self.assertAlmostEqual(lo, 1e-14)
        self.assertAlmostEqual(hi, 1e-9)
        lo, hi = parse_span("PBS 1 nM-1 mM linear window")
        self.assertAlmostEqual(lo, 1e-9)
        self.assertAlmostEqual(hi, 1e-3)

    def test_empty_and_unparseable_omitted(self):
        self.assertIsNone(parse_span(""))
        self.assertIsNone(parse_conc_token(""))
        self.assertIsNone(parse_span("81-fold"))

    def test_format_fold(self):
        self.assertEqual(format_fold(25.0), "25")
        self.assertEqual(format_fold(1.1), "1.1")
        self.assertEqual(format_fold(34.7 / 10.0), "3.47")
        self.assertEqual(format_fold(1.1e-3 / 1e-7), "11000")


class LfAlgebraTests(unittest.TestCase):
    def test_span_is_81_to_the_1_over_n(self):
        self.assertAlmostEqual(occupancy_span_10_90(1.0), 81.0)
        self.assertAlmostEqual(occupancy_span_10_90(0.5), 6561.0)
        self.assertAlmostEqual(occupancy_span_10_90(2.0), 9.0)

    def test_c10_c90_occupancy_endpoints(self):
        for n in (0.5, 1.0, 2.0):
            for kd in (1.8e-9, 12e-6, 1.0):
                c10, c90 = occupancy_c10_c90(kd, n)
                self.assertAlmostEqual(lf_occupancy(c10, kd, n), 0.1, places=12)
                self.assertAlmostEqual(lf_occupancy(c90, kd, n), 0.9, places=12)
                self.assertAlmostEqual(c90 / c10, occupancy_span_10_90(n), places=10)

    def test_kd_cancels(self):
        self.assertAlmostEqual(
            occupancy_c10_c90(1.8e-9, 0.7)[1] / occupancy_c10_c90(1.8e-9, 0.7)[0],
            occupancy_c10_c90(12e-6, 0.7)[1] / occupancy_c10_c90(12e-6, 0.7)[0],
        )

    def test_n_star_of_withdrawn_ratio_is_below_one_but_not_a_flagship(self):
        ratio = 1.1e-3 / 25e-9
        self.assertAlmostEqual(ratio, 44000.0)
        n_star = n_for_span(ratio)
        self.assertAlmostEqual(n_star, math.log(81) / math.log(44000), places=12)
        self.assertLess(n_star, 1.0)
        # Inverse identity only. Not Hu's n.
        self.assertAlmostEqual(occupancy_span_10_90(n_star), ratio, delta=1e-6)

    def test_illegal_1p8nM_overlay_never_contains_clements_at_tested_n(self):
        for n in (0.5, 1.0, 2.0):
            c10, c90 = occupancy_c10_c90(1.8e-9, n)
            self.assertFalse(contains(c10, c90, 1.1e-3))

    def test_n1_overlay_misses_25nM_from_above(self):
        c10, c90 = occupancy_c10_c90(1.8e-9, 1.0)
        self.assertAlmostEqual(c90, 16.2e-9)
        self.assertFalse(contains(c10, c90, 25e-9))
        self.assertAlmostEqual(25e-9 / c90, 25 / 16.2, places=10)


class LedgerRowTests(unittest.TestCase):
    def setUp(self):
        self.ledger = load_ledger(CSV)
        self.bars = load_range_bars(self.ledger)
        self.poles = load_canonical_poles(self.ledger)
        self.by_id = {bar.row_id: bar for bar in self.bars}

    def test_required_range_rows_present(self):
        for key in (
            "E003:numerical_result",
            "E007:numerical_result",
            "E026:numerical_result",
            "E041:numerical_result",
            "E044:numerical_result",
            "E044:comparator",
        ):
            self.assertIn(key, self.by_id)

    def test_empty_numerical_result_omits_row(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = CSV.read_text(encoding="utf-8")
            blanked = src.replace("0.01 pM–1 nM", "", 1)
            path = Path(tmp) / "core_evidence.csv"
            path.write_text(blanked, encoding="utf-8")
            bars = load_range_bars(load_ledger(path))
            ids = [bar.row_id for bar in bars]
            self.assertNotIn("E003:numerical_result", ids)

    def test_does_not_read_xiao_interferent_comparator_as_glu_range(self):
        self.assertNotIn("E026:comparator", self.by_id)

    def test_canonical_poles_from_ledger_only(self):
        tonic = pole_by_id(self.poles, "herman_tonic")
        cleft = pole_by_id(self.poles, "clements_cleft")
        nmdar = pole_by_id(self.poles, "herman_nmdar_ec50")
        self.assertIsNotNone(tonic)
        self.assertIsNotNone(cleft)
        self.assertIsNotNone(nmdar)
        self.assertAlmostEqual(tonic.value_M, 25e-9)
        self.assertAlmostEqual(cleft.value_M, 1.1e-3)
        self.assertAlmostEqual(nmdar.value_M, 1.8e-6)
        self.assertEqual(tonic.stamp, "INFERRED")
        self.assertEqual(cleft.stamp, "INFERRED")
        self.assertEqual(nmdar.stamp, "INFERRED")
        self.assertEqual(nmdar.quantity_type, "EC50")
        self.assertEqual(tonic.role, "canonical_basal_example")
        self.assertEqual(cleft.role, "canonical_cleft_example_not_basal")

    def test_glu1_and_abrantes_miss_25nM_from_above(self):
        glu1 = classify_vs_canonical(self.by_id["E003:numerical_result"], self.poles)
        abr = classify_vs_canonical(self.by_id["E041:numerical_result"], self.poles)
        self.assertEqual(glu1["contains_25nM"], "no")
        self.assertEqual(abr["contains_25nM"], "no")
        self.assertEqual(glu1["fold_below_25nM"], "25")
        self.assertEqual(abr["fold_below_25nM"], "2500")

    def test_ames_contains_c012_misses_clements(self):
        ames = classify_vs_canonical(self.by_id["E044:numerical_result"], self.poles)
        self.assertEqual(ames["contains_25nM"], "yes")
        self.assertEqual(ames["contains_1.1mM"], "no")
        self.assertEqual(ames["fold_below_1.1mM"], "110")

    def test_pbs_pac_does_not_contain_1_1mM_on_si_strict(self):
        pbs = classify_vs_canonical(self.by_id["E044:comparator"], self.poles)
        self.assertEqual(pbs["contains_25nM"], "yes")
        self.assertEqual(pbs["contains_1.1mM"], "no")
        self.assertEqual(pbs["fold_below_1.1mM"], "1.1")
        bar = self.by_id["E044:comparator"]
        self.assertFalse(contains(bar.lo_M, bar.hi_M, 1.1e-3))

    def test_xiao_cleft_fold_is_11000_not_11(self):
        xiao = self.by_id["E026:numerical_result"]
        cleft = pole_by_id(self.poles, "clements_cleft")
        fold = cleft.value_M / xiao.hi_M
        self.assertAlmostEqual(fold, 11000.0)
        self.assertNotAlmostEqual(fold, 11.0)
        v = classify_vs_canonical(xiao, self.poles)
        self.assertEqual(v["contains_25nM"], "yes")
        self.assertEqual(v["fold_below_1.1mM"], "11000")

    def test_no_bar_contains_both_c012_and_c011(self):
        for bar in self.bars:
            v = classify_vs_canonical(bar, self.poles)
            both = v["contains_25nM"] == "yes" and v["contains_1.1mM"] == "yes"
            self.assertFalse(both, bar.row_id)

    def test_ames_has_no_lod_dot(self):
        ames = self.by_id["E044:numerical_result"]
        self.assertEqual(ames.lod_id, "")
        self.assertIsNone(ames.lod_M)

    def test_pbs_lod_is_e043_not_ames(self):
        pbs = self.by_id["E044:comparator"]
        self.assertEqual(pbs.lod_id, "E043")
        self.assertIn("PBS", pbs.lod_matrix)
        self.assertAlmostEqual(pbs.lod_M, 0.3e-12)

    def test_serum_lod_not_paired(self):
        mea = self.by_id["E007:numerical_result"]
        self.assertEqual(mea.lod_id, "E005")
        self.assertNotEqual(mea.lod_id, "E006")

    def test_six_construct_rows(self):
        self.assertEqual(len(self.bars), 6)
        self.assertEqual(len({b.label for b in self.bars}), 6)


class BasalPoleRobustnessTests(unittest.TestCase):
    def setUp(self):
        ledger = load_ledger(CSV)
        self.bars = load_range_bars(ledger)
        self.poles = load_canonical_poles(ledger)
        self.ames = next(b for b in self.bars if b.row_id == "E044:numerical_result")
        self.glu1 = next(b for b in self.bars if b.row_id == "E003:numerical_result")
        self.by_cand = {c.pole_id: c for c in CANDIDATE_POLES}

    def test_candidates_are_tagged(self):
        self.assertEqual(len(CANDIDATE_POLES), 5)
        for cand in CANDIDATE_POLES:
            self.assertEqual(cand.status, "candidate")
            self.assertEqual(cand.transferable, "no")

    def test_ames_contains_hershey_capp_and_hascup2008_not_2010(self):
        ames = self.ames
        self.assertTrue(contains(ames.lo_M, ames.hi_M, self.by_cand["hershey_capp_9p4uM"].value_M))
        self.assertTrue(contains(ames.lo_M, ames.hi_M, self.by_cand["hascup2008_pfc_3p3uM"].value_M))
        self.assertTrue(contains(ames.lo_M, ames.hi_M, self.by_cand["hascup2008_str_5p0uM"].value_M))
        self.assertTrue(contains(ames.lo_M, ames.hi_M, self.by_cand["hershey_dialysate_144nM"].value_M))
        self.assertFalse(contains(ames.lo_M, ames.hi_M, self.by_cand["hascup2010_pfc_34p7uM"].value_M))
        fold = self.by_cand["hascup2010_pfc_34p7uM"].value_M / ames.hi_M
        self.assertAlmostEqual(fold, 3.47, places=6)
        self.assertEqual(format_fold(fold), "3.47")

    def test_glu1_misses_all_candidate_basals(self):
        for cand in CANDIDATE_POLES:
            self.assertFalse(contains(self.glu1.lo_M, self.glu1.hi_M, cand.value_M), cand.pole_id)

    def test_lf_n_does_not_change_device_bar_containment(self):
        ames = self.ames
        tonic = pole_by_id(self.poles, "herman_tonic")
        for n in (0.4, 1.0, 2.0):
            # n is occupancy-window geometry, not a calibration endpoint.
            self.assertEqual(verdict(ames.lo_M, ames.hi_M, tonic.value_M)["contains"], "yes")
            self.assertEqual(occupancy_span_10_90(n) > 0, True)

    def test_sensitivity_table_marks_candidate_status(self):
        rows = basal_sensitivity_rows(self.bars, self.poles)
        cand_rows = [r for r in rows if r["pole_status"] == "candidate"]
        self.assertGreater(len(cand_rows), 0)
        self.assertTrue(all(r["pole_status"] == "candidate" for r in cand_rows))
        ames_347 = next(
            r
            for r in rows
            if r["bar_id"] == "E044:numerical_result" and r["pole_id"] == "hascup2010_pfc_34p7uM"
        )
        self.assertEqual(ames_347["contains"], "no")
        self.assertEqual(ames_347["ceiling_fold_below"], "3.47")


class FigureHygieneTests(unittest.TestCase):
    def setUp(self):
        ledger = load_ledger(CSV)
        self.bars = load_range_bars(ledger)
        self.poles = load_canonical_poles(ledger)
        self.svg = working_range_svg(self.bars, self.poles)
        self.lf = lf_n_svg()
        self.cap = (CAPTION + LF_CAPTION).lower()

    def test_svg_labeled_ledger_modeled_stamps(self):
        for stamp in ("LEDGER", "MODELED", "INFERRED", "MEASURED", "UNKNOWN", "PROPOSED", "CANDIDATE"):
            self.assertIn(stamp, self.svg)
        self.assertIn("analytical_working_range", self.svg)
        self.assertIn("biological_concentration_range", self.svg)

    def test_svg_has_no_occupancy_overlay_and_no_18nM(self):
        self.assertIn("No occupancy θ", self.svg)
        self.assertNotIn("θ(25", self.svg)
        self.assertNotIn("1.8 nM", self.svg)
        self.assertIn("1.8 µM", self.svg)

    def test_svg_does_not_splice_herman_and_clements_as_device_spec(self):
        lowered = self.svg.lower()
        self.assertIn("Not one device spec", self.svg)
        self.assertIn("No 81-versus-44000 flagship", self.svg)

    def test_svg_does_not_print_astronomical_cleft_folds(self):
        self.assertNotIn("110000000", self.svg)
        self.assertNotIn("1100000-fold", self.svg)
        abr = [b for b in self.bars if b.row_id == "E041:numerical_result"][0]
        self.assertIn("2500-fold", glyph_note(abr, self.poles))
        self.assertIn("misses C011 1.1 mM", glyph_note(abr, self.poles))

    def test_lf_svg_has_no_44000_flagship_line(self):
        self.assertNotIn("44000", self.lf)
        self.assertIn("81^(1/n)", self.lf)
        self.assertIn("UNKNOWN", self.lf)
        self.assertIn("n=1 → 81-fold", self.lf)

    def test_caption_quantity_types_and_limits(self):
        self.assertIn("modeled", self.cap)
        self.assertIn("ledger", self.cap)
        self.assertIn("analytical_working_range", self.cap)
        self.assertIn("biological_concentration_range", self.cap)
        self.assertIn("sensor_lod", self.cap)
        self.assertIn("candidate", self.cap)
        self.assertIn("81^(1/n)", self.cap)
        self.assertIn("not occupancy kd", self.cap)
        self.assertNotIn("proves", self.cap)

    def test_n_star_table_labels_withdrawn_pairing(self):
        rows = n_sensitivity_identity_rows()
        withdrawn = next(r for r in rows if "withdrawn" in r["pairing_name"].lower())
        self.assertEqual(withdrawn["concentration_ratio"], "44000")
        self.assertIn("WITHDRAWN_PAIRING", withdrawn["note"])
        self.assertIn("not a device spec", withdrawn["note"].lower())

    def test_range_table_ames_lod_empty(self):
        rows = range_table_rows(self.bars, self.poles)
        ames = next(r for r in rows if r["row_id"] == "E044:numerical_result")
        self.assertEqual(ames["lod_id"], "")
        pbs = next(r for r in rows if r["row_id"] == "E044:comparator")
        self.assertEqual(pbs["lod_id"], "E043")


if __name__ == "__main__":
    unittest.main()
