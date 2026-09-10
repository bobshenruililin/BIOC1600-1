import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BootstrapTests(unittest.TestCase):
    def test_structure_script_passes(self):
        proc = subprocess.run(
            ["python3", "scripts/check_structure.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_ledger_script_passes(self):
        proc = subprocess.run(
            ["python3", "scripts/validate_ledgers.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_forbid_pdfs_passes(self):
        proc = subprocess.run(
            ["python3", "scripts/forbid_pdfs.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_nine_agents_exist(self):
        names = [
            "literature-scout",
            "evidence-extractor",
            "contradiction-hunter",
            "citation-auditor",
            "aptamer-biochemist",
            "sensor-engineer",
            "quant-modeler",
            "poster-red-team",
            "meta-improver",
        ]
        for name in names:
            self.assertTrue((ROOT / ".cursor/agents" / f"{name}.md").is_file())

    def test_score_theses_weights_locked(self):
        proc = subprocess.run(
            ["python3", "scripts/score_theses.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        payload = json.loads(proc.stdout)
        self.assertEqual(sum(payload["weights"].values()), 100)
        self.assertEqual(payload["discard_below"], 75)
        self.assertEqual(payload["finalist_at"], 85)

    def test_score_theses_classifies_totals(self):
        sample = {
            "id": "demo",
            "scores": {
                "primary-evidence strength": 20,
                "BIOC1600 biochemical depth": 12,
                "critical insight": 12,
                "reproducibility": 12,
                "central-question relevance": 8,
                "visual explanatory power": 8,
                "Tanner intellectual alignment": 4,
                "novelty without overclaiming": 4,
            },
        }
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
            json.dump(sample, handle)
            path = handle.name
        proc = subprocess.run(
            ["python3", "scripts/score_theses.py", path],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        result = json.loads(proc.stdout)[0]
        self.assertEqual(result["total"], 80)
        self.assertEqual(result["decision"], "hold")


if __name__ == "__main__":
    unittest.main()
