#!/usr/bin/env python3
"""Compare two PNG files by decoded pixels, not file bytes.

rsvg-convert can emit different zlib/filter encodings of the same raster.
CI therefore hashes the unfiltered RGB(A) samples, not sha256sum of the .png.
"""
from __future__ import annotations

import hashlib
import struct
import sys
import zlib
from pathlib import Path


PNG_SIG = b"\x89PNG\r\n\x1a\n"


def _paeth(a: int, b: int, c: int) -> int:
    p = a + b - c
    pa = abs(p - a)
    pb = abs(p - b)
    pc = abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    if pb <= pc:
        return b
    return c


def decode_png_pixels(path: Path) -> tuple[int, int, int, bytes]:
    data = path.read_bytes()
    if not data.startswith(PNG_SIG):
        raise ValueError(f"{path}: not a PNG")
    pos = 8
    width = height = bit_depth = color_type = None
    idat = bytearray()
    while pos + 8 <= len(data):
        length = struct.unpack(">I", data[pos : pos + 4])[0]
        ctype = data[pos + 4 : pos + 8]
        chunk = data[pos + 8 : pos + 8 + length]
        pos += 12 + length
        if ctype == b"IHDR":
            width, height, bit_depth, color_type, compression, filt, interlace = struct.unpack(
                ">IIBBBBB", chunk
            )
            if compression != 0 or filt != 0 or interlace != 0:
                raise ValueError(f"{path}: unsupported PNG compression/filter/interlace")
            if bit_depth != 8 or color_type not in (2, 6):
                raise ValueError(f"{path}: expected 8-bit RGB or RGBA, got depth={bit_depth} type={color_type}")
        elif ctype == b"IDAT":
            idat.extend(chunk)
        elif ctype == b"IEND":
            break
    if width is None or color_type is None:
        raise ValueError(f"{path}: missing IHDR")
    channels = 3 if color_type == 2 else 4
    raw = zlib.decompress(bytes(idat))
    stride = width * channels
    expected = height * (1 + stride)
    if len(raw) != expected:
        raise ValueError(f"{path}: inflated {len(raw)} bytes, expected {expected}")
    out = bytearray(height * stride)
    prev = bytearray(stride)
    for y in range(height):
        row_off = y * (1 + stride)
        ftype = raw[row_off]
        src = raw[row_off + 1 : row_off + 1 + stride]
        dst_off = y * stride
        if ftype == 0:
            recon = src
        elif ftype == 1:
            recon = bytearray(stride)
            for i, v in enumerate(src):
                left = recon[i - channels] if i >= channels else 0
                recon[i] = (v + left) & 255
        elif ftype == 2:
            recon = bytearray((src[i] + prev[i]) & 255 for i in range(stride))
        elif ftype == 3:
            recon = bytearray(stride)
            for i, v in enumerate(src):
                left = recon[i - channels] if i >= channels else 0
                recon[i] = (v + ((left + prev[i]) // 2)) & 255
        elif ftype == 4:
            recon = bytearray(stride)
            for i, v in enumerate(src):
                left = recon[i - channels] if i >= channels else 0
                up = prev[i]
                up_left = prev[i - channels] if i >= channels else 0
                recon[i] = (v + _paeth(left, up, up_left)) & 255
        else:
            raise ValueError(f"{path}: unknown PNG filter {ftype}")
        out[dst_off : dst_off + stride] = recon
        prev = bytearray(recon)
    return width, height, channels, bytes(out)


def pixel_sha256(path: Path) -> tuple[str, int, int, int]:
    width, height, channels, pixels = decode_png_pixels(path)
    digest = hashlib.sha256(pixels).hexdigest()
    return digest, width, height, channels


def _png_chunk(tag: bytes, payload: bytes) -> bytes:
    crc = zlib.crc32(tag + payload) & 0xFFFFFFFF
    return struct.pack(">I", len(payload)) + tag + payload + struct.pack(">I", crc)


def write_unfiltered_png(
    path: Path,
    width: int,
    height: int,
    channels: int,
    pixels: bytes,
    *,
    compresslevel: int = 9,
) -> None:
    """Write RGB/RGBA PNG using filter 0 only. compresslevel changes file bytes, not pixels."""
    if channels not in (3, 4):
        raise ValueError(f"channels must be 3 or 4, got {channels}")
    stride = width * channels
    if len(pixels) != height * stride:
        raise ValueError("pixel buffer length does not match geometry")
    color_type = 2 if channels == 3 else 6
    raw = bytearray()
    for y in range(height):
        raw.append(0)
        raw.extend(pixels[y * stride : (y + 1) * stride])
    ihdr = struct.pack(">IIBBBBB", width, height, 8, color_type, 0, 0, 0)
    idat = zlib.compress(bytes(raw), compresslevel)
    path.write_bytes(
        PNG_SIG
        + _png_chunk(b"IHDR", ihdr)
        + _png_chunk(b"IDAT", idat)
        + _png_chunk(b"IEND", b"")
    )


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("usage: compare_poster_png.py committed.png rebuilt.png", file=sys.stderr)
        return 2
    committed = Path(argv[1])
    rebuilt = Path(argv[2])
    h1, w1, ht1, c1 = pixel_sha256(committed)
    h2, w2, ht2, c2 = pixel_sha256(rebuilt)
    print(f"committed pixels {w1}x{ht1} ch={c1} sha256={h1}")
    print(f"rebuilt    pixels {w2}x{ht2} ch={c2} sha256={h2}")
    if (w1, ht1, c1) != (w2, ht2, c2):
        print("FAIL: geometry/channel mismatch", file=sys.stderr)
        return 1
    if (w1, ht1) != (4967, 3508):
        print(f"FAIL: expected 4967x3508, got {w1}x{ht1}", file=sys.stderr)
        return 1
    if h1 != h2:
        print("FAIL: decoded pixel SHA-256 mismatch", file=sys.stderr)
        return 1
    print("PASS: decoded pixels match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
