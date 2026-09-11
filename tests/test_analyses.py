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

    def test_captions_forbid_overclaim(self):
        cap = (ROOT / "analysis/accepted/occupancy_kinetics/figures/CAPTION.md").read_text(encoding="utf-8").lower()
        self.assertIn("simulation", cap)
        self.assertIn("bound", cap)
        self.assertIn("not glutamate", cap)
        self.assertNotIn("proves", cap)
        self.assertNotIn("measured koff", cap)
        atlas = (ROOT / "analysis/accepted/atlas/figures/CAPTION.md").read_text(encoding="utf-8").lower()
        self.assertIn("empty", atlas)

    def test_working_range_rebuild(self):
        proc = subprocess.run(
            ["sh", "analysis/working_range/rebuild.sh"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertTrue((ROOT / "analysis/working_range/figures/working_range.svg").is_file())
        self.assertTrue((ROOT / "analysis/working_range/tables/range_table.csv").is_file())

    def test_working_range_caption_quantity_types(self):
        cap = (ROOT / "analysis/working_range/figures/CAPTION.md").read_text(encoding="utf-8").lower()
        self.assertIn("simulation", cap)
        self.assertIn("ledger", cap)
        self.assertIn("analytical_working_range", cap)
        self.assertIn("biological_concentration_range", cap)
        self.assertIn("sensor_lod", cap)
        self.assertIn("not an ames or tissue lod", cap)
        self.assertNotIn("proves", cap)
        svg = (ROOT / "analysis/working_range/figures/working_range.svg").read_text(encoding="utf-8")
        self.assertIn("LEDGER", svg)
        self.assertIn("SIMULATION", svg)
        self.assertNotIn("θ(25", svg)
        self.assertNotIn("1.8 nM", svg)


if __name__ == "__main__":
    unittest.main()
