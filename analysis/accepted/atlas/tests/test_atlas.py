import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from atlas import SELECTED, build_grid, load_ledger, svg, find_repo

CSV = find_repo(Path(__file__).resolve()) / "research/evidence/core_evidence.csv"


class AtlasTests(unittest.TestCase):
    def test_ledger_loads(self):
        ledger = load_ledger(CSV)
        self.assertIn("E001", ledger)
        self.assertIn("E004", ledger)

    def test_glutamate_kon_not_invented(self):
        grid = build_grid(load_ledger(CSV))
        for construct in [
            "1d04 isolate",
            "glu1 E-AB",
            "Hu Glu-apt surface",
            "Hu Glu-apt 50% serum",
            "Xiao SPR oligo",
            "Xiao CNT FET",
            "Hu retina probe thesis",
        ]:
            self.assertEqual(grid.get((construct, "kon"), ""), "")
            self.assertEqual(grid.get((construct, "koff"), ""), "")

    def test_selected_cells_nonempty(self):
        grid = build_grid(load_ledger(CSV))
        self.assertIn("12", grid[("1d04 isolate", "Kd_molecular")])
        self.assertIn("1.8", grid[("Hu Glu-apt surface", "EC50")])
        self.assertIn("15", grid[("Hu Glu-apt surface", "measurement_time")])
        self.assertIn("51.5", grid[("Hu Glu-apt 50% serum", "sensor_LOD")])
        self.assertIn("serum", grid[("Hu Glu-apt 50% serum", "sensor_LOD")].lower())
        self.assertIn("PBS", grid[("Hu Glu-apt surface", "sensor_LOD")])
        self.assertIn("0.3", grid[("Hu retina probe thesis", "sensor_LOD")])
        self.assertIn("PBS", grid[("Hu retina probe thesis", "sensor_LOD")])
        self.assertIn("10", grid[("Hu retina probe thesis", "measurement_time")])

    def test_svg_mentions_empty_kon(self):
        text = svg(build_grid(load_ledger(CSV)))
        self.assertIn("empty", text.lower())
        self.assertIn("MEASURED", text)
        self.assertIn("1.8 nM", text.replace("µ", "u"))


if __name__ == "__main__":
    unittest.main()
