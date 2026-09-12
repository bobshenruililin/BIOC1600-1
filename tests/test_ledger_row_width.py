import csv
import io
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_ledgers import check_csv_row_widths  # noqa: E402


class LedgerRowWidthTests(unittest.TestCase):
    def test_canonical_ledgers_match_header_width(self):
        errors: list[str] = []
        for rel in (
            "state/sources.csv",
            "state/claims.csv",
            "research/evidence/core_evidence.csv",
        ):
            check_csv_row_widths(ROOT / rel, errors)
        self.assertEqual(errors, [])

    def test_c031_and_c033_keep_caveats_in_notes(self):
        with (ROOT / "state/claims.csv").open(newline="", encoding="utf-8") as handle:
            rows = {row["claim_id"]: row for row in csv.DictReader(handle)}
        for claim_id in ("C031", "C033"):
            notes = rows[claim_id]["notes"]
            self.assertIn("gold-nanostructure detachment confounds", notes)
            self.assertIn("PaC occupancy is unmeasured", notes)
            self.assertNotIn(None, rows[claim_id])

    def test_regression_fails_on_unquoted_comma_in_notes(self):
        malformed = (
            "claim_id,claim_text,notes\n"
            "C031,quoted claim,interpretation, not a pharmacological identification\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "claims.csv"
            path.write_text(malformed, encoding="utf-8")
            errors: list[str] = []
            check_csv_row_widths(path, errors)
            self.assertTrue(errors)
            self.assertIn("parsed width 4 != header width 3", errors[0])

    def test_quoted_notes_with_commas_are_one_field(self):
        text = (
            "claim_id,claim_text,notes\n"
            'C031,quoted claim,"interpretation, not a pharmacological identification"\n'
        )
        reader = csv.reader(io.StringIO(text))
        header = next(reader)
        row = next(reader)
        self.assertEqual(len(header), len(row))
        self.assertEqual(row[2], "interpretation, not a pharmacological identification")
