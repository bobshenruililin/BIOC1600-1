import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_RC_FILES = [
    "poster/rc/checkpoint.md",
    "poster/rc/poster_rc.svg",
    "poster/rc/poster_rc.png",
    "poster/rc/README.md",
    "poster/rc/copy.md",
    "poster/rc/captions.md",
    "poster/rc/talk_90s.md",
    "poster/rc/talk_3min.md",
    "poster/rc/oral_defense.md",
    "poster/rc/provenance.csv",
    "poster/rc/decision_record.md",
    "poster/rc/review_index.md",
    "poster/rc/qa_report.md",
    "poster/rc/manifest.json",
    "poster/rc/astra_bundle/index.md",
    "poster/rc/astra_design_contract_report.md",
    "poster/rc/astra_design_contract_disposition.md",
    "poster/rc/astra_report.md",
    "poster/rc/astra_disposition.md",
    "scripts/build_poster_rc.sh",
    "scripts/poster_fontconfig.conf",
    "poster/rc/fonts/NotoSans-Regular.ttf",
    "poster/rc/fonts/DejaVuSans.ttf",
]


class PosterRcPackageTests(unittest.TestCase):
    def test_required_rc_files_exist(self):
        missing = [rel for rel in REQUIRED_RC_FILES if not (ROOT / rel).is_file()]
        self.assertEqual(missing, [])

    def test_svg_is_a1_landscape_with_rc_label(self):
        svg = (ROOT / "poster/rc/poster_rc.svg").read_text(encoding="utf-8")
        self.assertIn('width="841mm"', svg)
        self.assertIn('height="594mm"', svg)
        self.assertIn('viewBox="0 0 841 594"', svg)
        self.assertIn("INTERNAL RELEASE CANDIDATE — NOT FINAL", svg)
        self.assertNotIn("eye-cup", svg.lower())
        self.assertIn("1.8 nM", svg)
        self.assertIn("12 µM", svg)
        self.assertRegex(svg, r"isolated mouse retina")

    def test_svg_has_no_network_hrefs_or_duplicate_ids(self):
        svg = (ROOT / "poster/rc/poster_rc.svg").read_text(encoding="utf-8")
        hrefs = re.findall(r"""(?:href|xlink:href)\s*=\s*["']([^"']+)["']""", svg)
        remote = [h for h in hrefs if h.startswith("http://") or h.startswith("https://") or h.startswith("//")]
        self.assertEqual(remote, [])
        ids = re.findall(r'\bid="([^"]+)"', svg)
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        self.assertEqual(dupes, [])

    def test_manifest_pins_decoded_pixels_and_fonts(self):
        manifest = json.loads((ROOT / "poster/rc/manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["png"]["ci_gate"], "decoded_pixels")
        self.assertEqual(manifest["png"]["width_px"], 4967)
        self.assertEqual(manifest["png"]["height_px"], 3508)
        self.assertEqual(manifest["svg"]["sha256"], "c8e3d19035fbe5f8315e87b8969f154f023187fbcdfa014999e0c6b66b5a1782")
        self.assertIn("fonts", manifest)
        self.assertGreaterEqual(len(manifest["fonts"]), 8)
