import json
import unittest
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


class AnalysisRebuildTests(unittest.TestCase):
    def test_accepted_rebuild(self):
        proc = subprocess.run(
            ["sh", "analysis/accepted/rebuild.sh"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertTrue((ROOT / "analysis/accepted/atlas/figures/atlas.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/occupancy_kinetics/figures/occupancy.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/occupancy_kinetics/figures/clocks.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/occupancy_kinetics/figures/sensitivity.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/occupancy_kinetics/figures/span_identity.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/occupancy_kinetics/figures/protocol_clocks.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/occupancy_kinetics/figures/two_regime_clocks.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/figures/atlas.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/figures/occupancy.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/figures/clocks.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/figures/sensitivity.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/figures/span_identity.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/figures/protocol_clocks.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/figures/two_regime_clocks.svg").is_file())

    def test_captions_forbid_overclaim(self):
        cap = (ROOT / "analysis/accepted/occupancy_kinetics/figures/CAPTION.md").read_text(encoding="utf-8").lower()
        self.assertIn("simulation", cap)
        self.assertIn("bound", cap)
        self.assertIn("not glutamate", cap)
        self.assertIn("unknown", cap)
        self.assertIn("hippocampal", cap)
        self.assertNotIn("proves", cap)
        self.assertNotIn("measured koff", cap)
        atlas = (ROOT / "analysis/accepted/atlas/figures/CAPTION.md").read_text(encoding="utf-8").lower()
        self.assertIn("empty", atlas)

    def test_supporting_span_identity_stamps_are_visible(self):
        span = (ROOT / "analysis/accepted/occupancy_kinetics/figures/span_identity.svg").read_text(encoding="utf-8")
        for stamp in ("MEASURED", "MODELED", "UNKNOWN", "PROPOSED"):
            self.assertIn(stamp, span)
        self.assertIn("81-fold", span)
        self.assertIn("hippocampal", span)
        self.assertIn("PaC probe", span)
        self.assertNotIn("θ(25 nM)=0.93", span)
        self.assertNotIn("~44,000-fold", span)
        occupancy = (ROOT / "analysis/accepted/occupancy_kinetics/figures/occupancy.svg").read_text(encoding="utf-8")
        self.assertIn("DEMOTED", occupancy)
        self.assertIn("not tissue occupancy", occupancy)
        self.assertNotIn("θ(25 nM)=", occupancy)

    def test_span_identity_is_not_declared_flagship(self):
        paths = (
            ROOT / "analysis/accepted/README.md",
            ROOT / "analysis/accepted/figures/README.md",
            ROOT / "analysis/accepted/figures/occupancy.CAPTION.md",
            ROOT / "analysis/accepted/occupancy_kinetics/README.md",
            ROOT / "analysis/accepted/occupancy_kinetics/figures/CAPTION.md",
        )
        for path in paths:
            text = path.read_text(encoding="utf-8").lower()
            self.assertNotIn("span_identity (flagship)", text, str(path))
            self.assertNotIn("span_identity.svg` | yes (flagship)", text, str(path))
            self.assertNotIn("flagship figure (mission 1.5)", text, str(path))

    def test_two_regime_figure_separates_calibration_from_retina(self):
        svg = (ROOT / "analysis/accepted/occupancy_kinetics/figures/two_regime_clocks.svg").read_text(encoding="utf-8")
        caption = (ROOT / "analysis/accepted/occupancy_kinetics/figures/CAPTION.md").read_text(encoding="utf-8")
        for label in ("PROBE CALIBRATION", "AMES CALIBRATION", "RETINA RECORDING"):
            self.assertIn(label, svg)
        self.assertIn("Calibration clocks are not tissue-recording clocks", caption)

    def test_protocol_clocks_picture_is_ledgered_not_nyquist(self):
        svg = (ROOT / "analysis/accepted/occupancy_kinetics/figures/protocol_clocks.svg").read_text(encoding="utf-8")
        for token in ("15 min", "1.2 ms", "INFERENCE", "MEASURED", "E008", "E033", "C022"):
            self.assertIn(token, svg)
        self.assertNotIn("Nyquist", svg)
        self.assertNotIn("t_off", svg)


if __name__ == "__main__":
    unittest.main()
