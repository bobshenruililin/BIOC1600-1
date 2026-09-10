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

    def test_captions_forbid_overclaim(self):
        cap = (ROOT / "analysis/accepted/occupancy_kinetics/figures/CAPTION.md").read_text(encoding="utf-8").lower()
        self.assertIn("simulation", cap)
        self.assertIn("bound", cap)
        atlas = (ROOT / "analysis/accepted/atlas/figures/CAPTION.md").read_text(encoding="utf-8").lower()
        self.assertIn("empty", atlas)


if __name__ == "__main__":
    unittest.main()
