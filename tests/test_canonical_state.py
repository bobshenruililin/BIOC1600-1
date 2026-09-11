import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CanonicalStateTests(unittest.TestCase):
    def test_current_thesis_is_revised_d(self):
        scoreboard = json.loads((ROOT / "state/scoreboard.json").read_text(encoding="utf-8"))
        self.assertEqual(scoreboard["current_best_thesis"], "D_revised")
        self.assertEqual(scoreboard["historical_overnight_tournament"]["current_best_thesis"], "T1")
        thesis = (ROOT / "state/current_thesis.md").read_text(encoding="utf-8")
        self.assertIn("unmeasured", thesis.lower())
        self.assertIn("hippocampal", thesis.lower())
        self.assertIn("does not prove", thesis.lower())
        lead = thesis.split("## Full statement")[0]
        self.assertNotIn("fail the slow problem on occupancy", lead)
        storyboard = (ROOT / "poster/storyboards/revised_D.md").read_text(encoding="utf-8")
        for stamp in ("MEASURED", "MODELED", "UNKNOWN", "PROPOSED"):
            self.assertIn(stamp, storyboard)
        winner = (ROOT / "poster/storyboards/winner.md").read_text(encoding="utf-8")
        self.assertIn("HISTORICAL", winner)
        theses = (ROOT / "poster/theses.md").read_text(encoding="utf-8")
        self.assertIn("historical", theses.lower())
        self.assertIn("revised D", theses)

    def test_current_thesis_does_not_use_1p8nm_as_pac_kd(self):
        thesis = (ROOT / "state/current_thesis.md").read_text(encoding="utf-8").lower()
        self.assertIn("as the retinal probe", thesis)
        self.assertIn("langmuir–freundlich", thesis)
        self.assertIn("different device", thesis)
        self.assertIn("unmeasured", thesis)
