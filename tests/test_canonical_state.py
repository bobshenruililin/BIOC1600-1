import json
import re
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

    def test_mission1_is_complete_but_gate_is_revise(self):
        gate = json.loads((ROOT / "state/gates/science_story.json").read_text(encoding="utf-8"))
        scoreboard = json.loads((ROOT / "state/scoreboard.json").read_text(encoding="utf-8"))
        self.assertEqual(gate["status"], "REVISE")
        self.assertEqual(gate["mission1_status"], "COMPLETE")
        self.assertFalse(gate["group_final"])
        self.assertTrue(gate["ready_for_mission2"])
        self.assertIn("UNRESOLVED", gate["flagship_analysis"])
        self.assertFalse(gate["pass_criteria"]["computation_answers_thesis"])
        self.assertEqual(scoreboard["science_story_gate"], "REVISE")
        self.assertEqual(scoreboard["mission1_status"], "COMPLETE")
        self.assertEqual(scoreboard["flagship_analysis_status"], "unresolved_mission2_input")

    def test_canonical_handoffs_agree(self):
        closure = (ROOT / "reports/mission1_closure.md").read_text(encoding="utf-8")
        nightly = (ROOT / "reports/nightly_summary.md").read_text(encoding="utf-8")
        theses = (ROOT / "poster/theses.md").read_text(encoding="utf-8")
        storyboard = (ROOT / "poster/storyboards/revised_D.md").read_text(encoding="utf-8")
        for line in (
            "MISSION 1 STATUS: COMPLETE",
            "SCIENCE STORY GATE: REVISE",
            "CURRENT WORKING THESIS: REVISED D",
            "FLAGSHIP ANALYSIS: UNRESOLVED — MISSION 2 INPUT",
            "GROUP FINAL: NO",
            "READY FOR MISSION 2: YES",
        ):
            self.assertIn(line, closure)
        self.assertIn("gate **REVISE**", nightly)
        self.assertIn("Replacement flagship", nightly)
        self.assertIn("flagship analysis is unresolved", theses)
        self.assertIn("Flagship placeholder", storyboard)

    def test_pr_disposition_register_covers_every_open_pr_head(self):
        register = (ROOT / "state/pr_disposition_register.md").read_text(encoding="utf-8")
        for number in range(6, 32):
            self.assertRegex(register, rf"\| #{number} \|")
        full_shas = re.findall(r"`[0-9a-f]{40}`", register)
        self.assertEqual(len(full_shas), 26)

    def test_mission2_queue_separates_evidence_states(self):
        queue = (ROOT / "state/mission2_input_queue.md").read_text(encoding="utf-8")
        for heading in (
            "## Accepted facts",
            "## Audited candidate evidence",
            "## Analysis candidates",
            "## Unresolved hypotheses",
        ):
            self.assertIn(heading, queue)
        self.assertIn("not accepted", queue)
        self.assertIn("binding-null", queue)
