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
        self.assertTrue((ROOT / "analysis/accepted/occupancy_kinetics/figures/two_regime_clocks.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/figures/atlas.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/figures/occupancy.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/figures/clocks.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/figures/sensitivity.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/figures/span_identity.svg").is_file())
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

    def test_flagship_stamps_are_visible(self):
        span = (ROOT / "analysis/accepted/occupancy_kinetics/figures/span_identity.svg").read_text(encoding="utf-8")
        for stamp in ("MEASURED", "MODELED", "UNKNOWN", "PROPOSED"):
            self.assertIn(stamp, span)
        self.assertIn("81-fold", span)
        self.assertIn("hippocampal", span)
        self.assertIn("PaC probe", span)
        self.assertNotIn("θ(25 nM)=0.93", span)
        occupancy = (ROOT / "analysis/accepted/occupancy_kinetics/figures/occupancy.svg").read_text(encoding="utf-8")
        self.assertIn("DEMOTED", occupancy)
        self.assertIn("not tissue occupancy", occupancy)
        self.assertNotIn("θ(25 nM)=", occupancy)


if __name__ == "__main__":
    unittest.main()
