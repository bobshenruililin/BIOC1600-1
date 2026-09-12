import hashlib
import json
import struct
import tempfile
import unittest
import zlib
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from compare_poster_png import (  # noqa: E402
    decode_png_pixels,
    pixel_sha256,
    write_unfiltered_png,
)


PNG_SIG = b"\x89PNG\r\n\x1a\n"


def _chunk(tag: bytes, payload: bytes) -> bytes:
    crc = zlib.crc32(tag + payload) & 0xFFFFFFFF
    return struct.pack(">I", len(payload)) + tag + payload + struct.pack(">I", crc)


def _write_filtered_png(path: Path, width: int, height: int, pixels: bytes, filters: list[int]) -> None:
    channels = 3
    stride = width * channels
    raw = bytearray()
    prev = bytes(stride)
    for y, ftype in enumerate(filters):
        row = pixels[y * stride : (y + 1) * stride]
        encoded = bytearray(stride)
        if ftype == 0:
            encoded[:] = row
        elif ftype == 1:
            for i, v in enumerate(row):
                left = row[i - channels] if i >= channels else 0
                encoded[i] = (v - left) & 255
        elif ftype == 2:
            for i, v in enumerate(row):
                encoded[i] = (v - prev[i]) & 255
        elif ftype == 3:
            for i, v in enumerate(row):
                left = row[i - channels] if i >= channels else 0
                encoded[i] = (v - ((left + prev[i]) // 2)) & 255
        elif ftype == 4:
            def paeth(a: int, b: int, c: int) -> int:
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                if pa <= pb and pa <= pc:
                    return a
                if pb <= pc:
                    return b
                return c

            for i, v in enumerate(row):
                left = row[i - channels] if i >= channels else 0
                up = prev[i]
                up_left = prev[i - channels] if i >= channels else 0
                encoded[i] = (v - paeth(left, up, up_left)) & 255
        else:
            raise ValueError(ftype)
        raw.append(ftype)
        raw.extend(encoded)
        prev = row
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    path.write_bytes(
        PNG_SIG
        + _chunk(b"IHDR", ihdr)
        + _chunk(b"IDAT", zlib.compress(bytes(raw), 9))
        + _chunk(b"IEND", b"")
    )


class PosterPngPixelTests(unittest.TestCase):
    def test_file_bytes_may_differ_when_pixels_match(self):
        width, height, channels = 8, 4, 3
        pixels = bytes((i * 17) % 256 for i in range(height * width * channels))
        with tempfile.TemporaryDirectory() as tmp:
            a = Path(tmp) / "a.png"
            b = Path(tmp) / "b.png"
            write_unfiltered_png(a, width, height, channels, pixels, compresslevel=1)
            write_unfiltered_png(b, width, height, channels, pixels, compresslevel=9)
            self.assertNotEqual(hashlib.sha256(a.read_bytes()).hexdigest(), hashlib.sha256(b.read_bytes()).hexdigest())
            ha, wa, ha_h, ca = pixel_sha256(a)
            hb, wb, hb_h, cb = pixel_sha256(b)
            self.assertEqual((ha, wa, ha_h, ca), (hb, wb, hb_h, cb))
            self.assertEqual((wa, ha_h, ca), (width, height, channels))
            self.assertEqual(hashlib.sha256(pixels).hexdigest(), ha)

    def test_unfilters_all_png_filter_types(self):
        width, height = 5, 5
        pixels = bytes((x * 3 + y * 19 + c) % 256 for y in range(height) for x in range(width) for c in range(3))
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "filt.png"
            _write_filtered_png(path, width, height, pixels, [0, 1, 2, 3, 4])
            w, h, ch, decoded = decode_png_pixels(path)
            self.assertEqual((w, h, ch), (width, height, 3))
            self.assertEqual(decoded, pixels)

    def test_committed_poster_pixel_sha_if_present(self):
        png = ROOT / "poster/rc/poster_rc.png"
        manifest_path = ROOT / "poster/rc/manifest.json"
        if not png.is_file() or not manifest_path.is_file():
            self.skipTest("poster RC PNG not in this tree")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        expected = manifest["png"]["pixel_sha256"]
        digest, width, height, channels = pixel_sha256(png)
        self.assertEqual((width, height), (4967, 3508))
        self.assertEqual(channels, 3)
        self.assertEqual(digest, expected)
        self.assertEqual(manifest["png"]["ci_gate"], "decoded_pixels")
