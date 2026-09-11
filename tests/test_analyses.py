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
        self.assertTrue((ROOT / "analysis/accepted/figures/atlas.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/figures/occupancy.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/figures/clocks.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/figures/sensitivity.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/interrogation_nyquist/figures/nyquist.svg").is_file())
        self.assertTrue((ROOT / "analysis/accepted/figures/nyquist.svg").is_file())

    def test_captions_forbid_overclaim(self):
        cap = (ROOT / "analysis/accepted/occupancy_kinetics/figures/CAPTION.md").read_text(encoding="utf-8").lower()
        self.assertIn("simulation", cap)
        self.assertIn("bound", cap)
        self.assertIn("not glutamate", cap)
        self.assertNotIn("proves", cap)
        self.assertNotIn("measured koff", cap)
        atlas = (ROOT / "analysis/accepted/atlas/figures/CAPTION.md").read_text(encoding="utf-8").lower()
        self.assertIn("empty", atlas)
        nyq = (ROOT / "analysis/accepted/interrogation_nyquist/figures/CAPTION.md").read_text(
            encoding="utf-8"
        )
        nyq_l = nyq.lower()
        self.assertIn("computational illustration", nyq_l)
        self.assertIn("literature stimulus", nyq_l)
        self.assertIn("interrogation", nyq_l)
        self.assertIn("sampling", nyq_l)
        self.assertNotIn("too slow", nyq_l)
        self.assertNotIn("proves", nyq_l)
        self.assertNotIn("94 nM", nyq)
        self.assertNotIn("mean-equivalent", nyq_l)


if __name__ == "__main__":
    unittest.main()
