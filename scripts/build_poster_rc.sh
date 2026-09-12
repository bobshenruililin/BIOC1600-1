#!/usr/bin/env bash
# Rebuild poster/rc/poster_rc.png from poster/rc/poster_rc.svg.
# Fail nonzero on missing input or renderer. Never silently reuse a committed PNG.
# No network. No PDF.
set -eu

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SVG="${ROOT}/poster/rc/poster_rc.svg"
OUT="${ROOT}/poster/rc/poster_rc.png"
FONTCONFIG_FILE="${ROOT}/scripts/poster_fontconfig.conf"
export FONTCONFIG_FILE
export PANGOCAIRO_BACKEND=fontconfig
# A1 landscape at 150 dpi: 841 mm × 594 mm → 4967 × 3508 px
WIDTH_PX=4967
HEIGHT_PX=3508

if [[ ! -f "${SVG}" ]]; then
  echo "build_poster_rc: missing input ${SVG}" >&2
  exit 1
fi
if [[ ! -f "${FONTCONFIG_FILE}" ]]; then
  echo "build_poster_rc: missing ${FONTCONFIG_FILE}" >&2
  exit 1
fi

TMP="$(mktemp "${OUT}.tmp.XXXXXX.png")"
cleanup() { rm -f "${TMP}"; }
trap cleanup EXIT

render_ok=0
if command -v rsvg-convert >/dev/null 2>&1; then
  # Unset proxies so a renderer cannot fetch remote hrefs.
  env -u http_proxy -u https_proxy -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY \
    rsvg-convert --keep-image-data -w "${WIDTH_PX}" -h "${HEIGHT_PX}" "${SVG}" -o "${TMP}"
  render_ok=1
elif command -v inkscape >/dev/null 2>&1; then
  env -u http_proxy -u https_proxy -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY \
    inkscape "${SVG}" \
      --export-type=png \
      --export-filename="${TMP}" \
      --export-width="${WIDTH_PX}" \
      --export-height="${HEIGHT_PX}"
  render_ok=1
else
  echo "build_poster_rc: no renderer (need rsvg-convert or inkscape on PATH)" >&2
  exit 1
fi

if [[ "${render_ok}" -ne 1 || ! -s "${TMP}" ]]; then
  echo "build_poster_rc: renderer produced no PNG" >&2
  exit 1
fi

# Refuse PDF output even if a renderer were misconfigured.
case "$(file -b --mime-type "${TMP}" 2>/dev/null || true)" in
  application/pdf)
    echo "build_poster_rc: refused PDF output" >&2
    exit 1
    ;;
esac

python3 - "${TMP}" "${WIDTH_PX}" "${HEIGHT_PX}" <<'PY'
import sys
from pathlib import Path

path = Path(sys.argv[1])
want_w, want_h = int(sys.argv[2]), int(sys.argv[3])
raw = path.read_bytes()
if raw.startswith(b"%PDF"):
    sys.exit("build_poster_rc: refused PDF bytes")
if not (raw.startswith(b"\x89PNG\r\n\x1a\n")):
    sys.exit("build_poster_rc: output is not a PNG")
# PNG IHDR: width/height at bytes 16-23
w = int.from_bytes(raw[16:20], "big")
h = int.from_bytes(raw[20:24], "big")
if w < 1 or h < 1:
    sys.exit("build_poster_rc: PNG has empty dimensions")
print(f"build_poster_rc: rendered {w}x{h} PNG ({path.stat().st_size} bytes)")
if (w, h) != (want_w, want_h):
    print(
        f"build_poster_rc: warning: requested {want_w}x{want_h}, got {w}x{h}",
        file=sys.stderr,
    )
PY

mv -f "${TMP}" "${OUT}"
trap - EXIT
echo "build_poster_rc: wrote ${OUT}"
