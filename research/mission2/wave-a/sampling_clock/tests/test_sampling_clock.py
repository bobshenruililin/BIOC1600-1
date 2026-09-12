import ast
import csv
import math
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from figures import caption_text, sampling_clock_svg, write_clock_table
from ledger import PINNED, load_clocks
from model import (
    axis_occupancy_fraction,
    clock_ratio,
    inferred_clements_waveform_m,
    pulse_width_to_one_percent_s,
    shape_reporting_excluded,
    timescale_mismatch,
)

PKG = Path(__file__).resolve().parents[1]


class LedgerPinTests(unittest.TestCase):
    def test_pins_match_core_evidence(self):
        clocks = load_clocks()
        self.assertAlmostEqual(clocks.tau_s, 1.2e-3)
        self.assertAlmostEqual(clocks.peak_m, 1.1e-3)
        self.assertAlmostEqual(clocks.basal_m, 25e-9)
        self.assertAlmostEqual(clocks.interrogation_s, 14.0)
        self.assertAlmostEqual(clocks.sampling_s, 60.0)
        self.assertAlmostEqual(clocks.incubation_s, 15 * 60)
        self.assertAlmostEqual(clocks.plateau_s, 10 * 60)
        self.assertEqual(clocks.tau_id, "E033")
        self.assertEqual(clocks.interrogation_id, "E045")
        self.assertEqual(clocks.sampling_id, "E046")

    def test_c031_refuses_synaptic_transients(self):
        clocks = load_clocks()
        self.assertIn("not synaptic transients", clocks.c031_text.lower())

    def test_c007_names_empty_rates(self):
        clocks = load_clocks()
        self.assertIn("kon", clocks.c007_text.lower())
        self.assertIn("koff", clocks.c007_text.lower())

    def test_pin_table_covers_required_rows(self):
        self.assertEqual(
            set(PINNED),
            {"E033", "E032", "E034", "E045", "E046", "E008", "E042"},
        )


class StimulusTests(unittest.TestCase):
    def setUp(self):
        self.clocks = load_clocks()

    def test_t0_is_peak_without_herman_basal(self):
        c0 = inferred_clements_waveform_m(0.0, self.clocks)
        self.assertAlmostEqual(c0, self.clocks.peak_m)
        self.assertEqual(c0, self.clocks.peak_m)
        self.assertNotEqual(c0, self.clocks.basal_m + self.clocks.peak_m)

    def test_negative_time_is_zero_not_herman(self):
        self.assertAlmostEqual(inferred_clements_waveform_m(-1.0, self.clocks), 0.0)

    def test_one_tau_is_peak_over_e(self):
        c = inferred_clements_waveform_m(self.clocks.tau_s, self.clocks)
        self.assertAlmostEqual(c, self.clocks.peak_m / math.e)

    def test_late_time_near_zero(self):
        c = inferred_clements_waveform_m(0.05, self.clocks)
        self.assertLess(c, 1e-12)

    def test_no_spatial_dilution_parameters(self):
        tree = ast.parse((PKG / "model.py").read_text(encoding="utf-8"))
        names = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
        args = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                args.update(a.arg for a in node.args.args)
        self.assertNotIn("dilution", names | args)
        self.assertNotIn("volume", names | args)
        self.assertNotIn("radius", names | args)


class ClockIdentityTests(unittest.TestCase):
    def setUp(self):
        self.clocks = load_clocks()

    def test_scan_ratio(self):
        self.assertAlmostEqual(
            clock_ratio(self.clocks.interrogation_s, self.clocks.tau_s), 14.0 / 1.2e-3
        )
        self.assertAlmostEqual(clock_ratio(14.0, 1.2e-3), 11666.666666, places=4)

    def test_sample_ratio_is_50000(self):
        self.assertAlmostEqual(clock_ratio(self.clocks.sampling_s, self.clocks.tau_s), 50000.0)

    def test_both_architecture_clocks_mismatch_independently(self):
        tau = self.clocks.tau_s
        self.assertTrue(timescale_mismatch(self.clocks.interrogation_s, tau))
        self.assertTrue(timescale_mismatch(self.clocks.sampling_s, tau))
        self.assertTrue(
            shape_reporting_excluded(self.clocks.interrogation_s, self.clocks.sampling_s, tau)
        )

    def test_each_clock_fails_independently(self):
        tau = self.clocks.tau_s
        self.assertTrue(shape_reporting_excluded(1e-9, self.clocks.sampling_s, tau))
        self.assertTrue(shape_reporting_excluded(self.clocks.interrogation_s, 1e-9, tau))

    def test_hypothetical_fast_cadence_would_not_mismatch(self):
        tau = self.clocks.tau_s
        self.assertFalse(shape_reporting_excluded(tau, tau, tau))

    def test_pulse_is_a_tiny_fraction_of_the_scan(self):
        frac = axis_occupancy_fraction(self.clocks.tau_s, self.clocks.interrogation_s)
        self.assertLess(frac, 1e-4)
        self.assertAlmostEqual(frac, 1.2e-3 / 14.0)

    def test_one_percent_width_still_much_shorter_than_scan(self):
        width = pulse_width_to_one_percent_s(self.clocks)
        self.assertLess(width, 0.01)
        self.assertLess(width / self.clocks.interrogation_s, 0.001)


class NoKineticsInventionTests(unittest.TestCase):
    def test_model_has_no_kon_koff_names(self):
        tree = ast.parse((PKG / "model.py").read_text(encoding="utf-8"))
        names = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
        self.assertNotIn("kon", names)
        self.assertNotIn("koff", names)

    def test_ledger_loader_has_no_kon_koff_names(self):
        tree = ast.parse((PKG / "ledger.py").read_text(encoding="utf-8"))
        names = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
        self.assertNotIn("kon", names)
        self.assertNotIn("koff", names)

    def test_model_has_no_nyquist_names(self):
        text = (PKG / "model.py").read_text(encoding="utf-8").lower()
        self.assertNotIn("nyquist", text)
        self.assertNotIn("shannon", text)


class FigureHygieneTests(unittest.TestCase):
    def setUp(self):
        self.clocks = load_clocks()
        self.svg = sampling_clock_svg(self.clocks)
        self.caption = caption_text(self.clocks)
        self.low = (self.svg + "\n" + self.caption).lower()

    def test_quantity_types_labeled(self):
        for needle in ("literature waveform", "interrogation", "sampling"):
            self.assertIn(needle, self.low)

    def test_computational_illustration(self):
        self.assertIn("computational illustration", self.low)

    def test_three_layers_stamped(self):
        for stamp in ("measured", "inferred", "modeled", "unknown", "proposed"):
            self.assertIn(stamp, self.low)
        self.assertIn("layer 1", self.low)
        self.assertIn("layer 2", self.low)
        self.assertIn("layer 3", self.low)

    def test_not_flagship(self):
        self.assertIn("not flagship", self.low)
        self.assertIn("candidate", self.low)

    def test_forbids_too_slow_slogan(self):
        self.assertNotIn("too slow", self.low)
        self.assertNotIn("the aptamer is", self.low)

    def test_forbids_nyquist_label(self):
        self.assertNotIn("nyquist", self.low)

    def test_protocol_time_is_not_koff(self):
        self.assertIn("not koff", self.low)
        self.assertIn("c007", self.low)

    def test_authors_refuse_synaptic(self):
        self.assertIn("c031", self.low)
        self.assertTrue("not synaptic" in self.low or "basal" in self.low)

    def test_herman_not_spliced_in_caption(self):
        self.assertIn("not spliced", self.low)

    def test_ipa_and_glutox_off_figure(self):
        self.assertNotIn("ipa", self.svg.lower())
        self.assertNotIn("glutox", self.svg.lower())
        self.assertNotIn("tobramycin", self.svg.lower())
        self.assertNotIn("500-800", self.svg)
        self.assertNotIn("500–800", self.svg)

    def test_caption_may_footnote_other_class(self):
        cap = self.caption.lower()
        self.assertIn("other-class", cap)
        self.assertIn("ipa", cap)
        self.assertIn("glutox", cap)

    def test_no_overclaim(self):
        self.assertNotIn("proves", self.low)
        self.assertNotIn("measured koff", self.low)

    def test_spatial_dilution_not_invented(self):
        self.assertIn("spatial dilution", self.low)
        self.assertIn("unmeasured", self.low)
        self.assertNotIn("dilution factor", self.low)

    def test_outputs_do_not_print_mean_equivalent_nM(self):
        excess_nM = self.clocks.peak_m * self.clocks.tau_s / self.clocks.interrogation_s * 1e9
        self.assertGreater(excess_nM, 90.0)
        self.assertLess(excess_nM, 100.0)
        with tempfile.TemporaryDirectory() as tmp:
            write_clock_table(Path(tmp) / "clocks.csv", self.clocks)
            table = (Path(tmp) / "clocks.csv").read_text(encoding="utf-8")
        joined_text = self.caption + "\n" + table
        for snippet in (
            "94 nM",
            "94 nm",
            f"{excess_nM:.0f} nM",
            f"{excess_nM:.1f} nM",
            "mean-equivalent",
            "mean equivalent",
        ):
            self.assertNotIn(snippet, joined_text)
            self.assertNotIn(snippet.lower(), joined_text.lower())
        self.assertNotIn("94 nM", self.svg)
        self.assertNotIn("mean-equivalent", self.svg.lower())

    def test_clock_table_marks_incubation_off_figure(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "clocks.csv"
            write_clock_table(path, self.clocks)
            with path.open(newline="", encoding="utf-8") as handle:
                rows = {row["quantity_class"]: row for row in csv.DictReader(handle)}
        self.assertEqual(rows["incubation"]["on_figure"], "no")
        self.assertEqual(rows["plateau"]["on_figure"], "no")
        self.assertEqual(rows["interrogation"]["on_figure"], "yes")
        self.assertEqual(rows["sampling"]["on_figure"], "yes")
        self.assertEqual(rows["slice_ambient"]["on_figure"], "no")
        self.assertEqual(rows["interrogation"]["stamp"], "MEASURED")
        self.assertEqual(rows["biological_tau"]["stamp"], "INFERRED")
        self.assertEqual(rows["clock_ratio_scan"]["stamp"], "MODELED")
        self.assertNotIn("15 min", self.svg)
        self.assertNotIn("10 min", self.svg)

    def test_svg_is_xml(self):
        self.assertIn("<svg", self.svg)
        self.assertIn("layer 1", self.low)
        self.assertIn("layer 3", self.low)


class RebuildTests(unittest.TestCase):
    def test_rebuild_script_exists(self):
        self.assertTrue((PKG / "rebuild.sh").is_file())
        self.assertTrue((PKG / "README.md").is_file())
        self.assertTrue((PKG / "limitations.md").is_file())
        self.assertTrue((PKG / "provenance.md").is_file())


if __name__ == "__main__":
    unittest.main()
