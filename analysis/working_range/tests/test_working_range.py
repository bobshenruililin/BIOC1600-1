import csv
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ledger import (
    LOD_FOR_RANGE,
    ceiling_fold_below,
    classify_row,
    contains,
    find_repo,
    format_fold,
    glyph_note,
    load_ledger,
    load_poles,
    load_range_bars,
    parse_conc_token,
    parse_span,
    pole_by_id,
    table_rows,
)
from figures import CAPTION, working_range_svg

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

    def test_format_fold_integer_and_tenth(self):
        self.assertEqual(format_fold(25.0), "25")
        self.assertEqual(format_fold(1.1), "1.1")
        self.assertEqual(format_fold(1.1e-3 / 1e-11), "110000000")
        self.assertEqual(format_fold(1.1e-3 / 1e-9), "1100000")


class LedgerRowTests(unittest.TestCase):
    def setUp(self):
        self.ledger = load_ledger(CSV)
        self.bars = load_range_bars(self.ledger)
        self.poles = load_poles(self.ledger)
        self.by_id = {bar.row_id: bar for bar in self.bars}

    def test_required_range_rows_present(self):
        self.assertIn("E003:numerical_result", self.by_id)
        self.assertIn("E007:numerical_result", self.by_id)
        self.assertIn("E026:numerical_result", self.by_id)
        self.assertIn("E041:numerical_result", self.by_id)
        self.assertIn("E044:numerical_result", self.by_id)
        self.assertIn("E044:comparator", self.by_id)

    def test_empty_numerical_result_omits_row(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = CSV.read_text(encoding="utf-8")
            # Blank E003 span without inventing a replacement number.
            blanked = src.replace("0.01 pM–1 nM", "", 1)
            path = Path(tmp) / "core_evidence.csv"
            path.write_text(blanked, encoding="utf-8")
            bars = load_range_bars(load_ledger(path))
            ids = [bar.row_id for bar in bars]
            self.assertNotIn("E003:numerical_result", ids)

    def test_does_not_read_xiao_interferent_comparator_as_glu_range(self):
        self.assertNotIn("E026:comparator", self.by_id)

    def test_poles_from_ledger_only(self):
        tonic = pole_by_id(self.poles, "herman_tonic")
        cleft = pole_by_id(self.poles, "clements_cleft")
        nmdar = pole_by_id(self.poles, "herman_nmdar_ec50")
        self.assertIsNotNone(tonic)
        self.assertIsNotNone(cleft)
        self.assertIsNotNone(nmdar)
        self.assertAlmostEqual(tonic.value_M, 25e-9)
        self.assertAlmostEqual(cleft.value_M, 1.1e-3)
        self.assertAlmostEqual(nmdar.value_M, 1.8e-6)
        self.assertEqual(tonic.quantity_type, "biological_concentration_range")
        self.assertEqual(cleft.quantity_type, "biological_concentration_range")
        self.assertEqual(nmdar.quantity_type, "EC50")

    def test_glu1_and_abrantes_miss_25nM_from_above(self):
        glu1 = classify_row(self.by_id["E003:numerical_result"], self.poles)
        abr = classify_row(self.by_id["E041:numerical_result"], self.poles)
        self.assertEqual(glu1["contains_25nM"], "no")
        self.assertEqual(abr["contains_25nM"], "no")
        self.assertEqual(glu1["fold_below_25nM"], "25")
        self.assertEqual(abr["fold_below_25nM"], "2500")

    def test_ames_contains_25nM_misses_cleft(self):
        ames = classify_row(self.by_id["E044:numerical_result"], self.poles)
        self.assertEqual(ames["contains_25nM"], "yes")
        self.assertEqual(ames["contains_1.1mM"], "no")
        self.assertEqual(ames["fold_below_1.1mM"], "110")

    def test_pbs_pac_does_not_contain_1_1mM_on_si_strict(self):
        pbs = classify_row(self.by_id["E044:comparator"], self.poles)
        self.assertEqual(pbs["contains_25nM"], "yes")
        self.assertEqual(pbs["contains_1.1mM"], "no")
        self.assertEqual(pbs["fold_below_1.1mM"], "1.1")
        self.assertFalse(contains(self.by_id["E044:comparator"].lo_M, self.by_id["E044:comparator"].hi_M, 1.1e-3))

    def test_xiao_cleft_fold_is_11000_not_11(self):
        xiao = self.by_id["E026:numerical_result"]
        cleft = pole_by_id(self.poles, "clements_cleft")
        fold = ceiling_fold_below(xiao.hi_M, cleft.value_M)
        self.assertAlmostEqual(fold, 11000.0)
        self.assertNotAlmostEqual(fold, 11.0)
        self.assertEqual(format_fold(fold), "11000")
        verdict = classify_row(xiao, self.poles)
        self.assertEqual(verdict["contains_25nM"], "yes")
        self.assertEqual(verdict["fold_below_1.1mM"], "11000")

    def test_hu_mea_110_fold_below_cleft(self):
        mea = classify_row(self.by_id["E007:numerical_result"], self.poles)
        self.assertEqual(mea["contains_25nM"], "yes")
        self.assertEqual(mea["fold_below_1.1mM"], "110")

    def test_no_bar_contains_both_poles(self):
        for bar in self.bars:
            verdict = classify_row(bar, self.poles)
            both = verdict["contains_25nM"] == "yes" and verdict["contains_1.1mM"] == "yes"
            self.assertFalse(both, bar.row_id)

    def test_ames_has_no_lod_dot(self):
        ames = self.by_id["E044:numerical_result"]
        self.assertEqual(ames.lod_id, "")
        self.assertIsNone(ames.lod_M)
        self.assertEqual(LOD_FOR_RANGE[("E044", "numerical_result")], None)

    def test_pbs_lod_is_e043_not_ames(self):
        pbs = self.by_id["E044:comparator"]
        self.assertEqual(pbs.lod_id, "E043")
        self.assertIn("PBS", pbs.lod_matrix)
        self.assertAlmostEqual(pbs.lod_M, 0.3e-12)
        self.assertEqual(pbs.lod_quantity_type, "sensor_LOD")

    def test_serum_lod_not_paired(self):
        mea = self.by_id["E007:numerical_result"]
        self.assertEqual(mea.lod_id, "E005")
        self.assertNotEqual(mea.lod_id, "E006")

    def test_constructs_not_binned_as_one_row(self):
        labels = [bar.label for bar in self.bars]
        self.assertEqual(len(labels), len(set(labels)))
        self.assertEqual(len(self.bars), 6)


class FigureHygieneTests(unittest.TestCase):
    def setUp(self):
        ledger = load_ledger(CSV)
        self.bars = load_range_bars(ledger)
        self.poles = load_poles(ledger)
        self.svg = working_range_svg(self.bars, self.poles)
        self.cap = CAPTION.lower()

    def test_svg_labeled_simulation_ledger(self):
        text = self.svg.lower()
        self.assertIn("ledger", text)
        self.assertIn("simulation", text)
        self.assertIn("analytical_working_range", self.svg)
        self.assertIn("biological_concentration_range", self.svg)
        self.assertIn("sensor_LOD", self.svg)

    def test_svg_has_no_occupancy_overlay(self):
        self.assertIn("No occupancy θ", self.svg)
        self.assertNotIn("θ(25", self.svg)
        self.assertNotIn("langmuir", self.svg.lower())
        self.assertNotIn("1:1", self.svg)

    def test_svg_does_not_print_03pm_as_ames(self):
        self.assertIn("0.3 pM PBS LOD (not Ames)", self.svg)
        ames_bar = [b for b in self.bars if b.row_id == "E044:numerical_result"][0]
        self.assertIsNone(ames_bar.lod_M)

    def test_svg_omits_moussawi_band_not_in_core_ledger(self):
        self.assertNotIn("0.02", self.svg)
        self.assertNotIn("30 µM", self.svg)
        self.assertNotIn("Moussawi", self.svg)

    def test_svg_does_not_print_astronomical_cleft_folds(self):
        self.assertNotIn("110000000", self.svg)
        self.assertNotIn("1100000-fold", self.svg)
        abr = [b for b in self.bars if b.row_id == "E041:numerical_result"][0]
        self.assertIn("misses 1.1 mM", glyph_note(abr, self.poles))
        self.assertIn("2500-fold", glyph_note(abr, self.poles))

    def test_svg_does_not_plot_hu_1_8_nM(self):
        self.assertNotIn("1.8 nM", self.svg)
        self.assertIn("1.8 µM", self.svg)

    def test_caption_quantity_types_and_limits(self):
        self.assertIn("simulation", self.cap)
        self.assertIn("ledger", self.cap)
        self.assertIn("analytical_working_range", self.cap)
        self.assertIn("biological_concentration_range", self.cap)
        self.assertIn("sensor_lod", self.cap)
        self.assertIn("ec50", self.cap)
        self.assertIn("not an ames or tissue lod", self.cap)
        self.assertIn("occupancy", self.cap)
        self.assertIn("11000", self.cap)
        self.assertNotIn("proves", self.cap)

    def test_table_empty_ames_lod_cell(self):
        rows = table_rows(self.bars, self.poles)
        ames = next(r for r in rows if r["row_id"] == "E044:numerical_result")
        self.assertEqual(ames["lod_id"], "")
        self.assertEqual(ames["lod_display"], "")
        pbs = next(r for r in rows if r["row_id"] == "E044:comparator")
        self.assertEqual(pbs["lod_id"], "E043")


if __name__ == "__main__":
    unittest.main()
