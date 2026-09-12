#!/usr/bin/env bash
# CI helper: delete committed PNG, rebuild, require decoded-pixel match.
# PNG file SHA-256 is renderer-local (zlib/filter encoding) and is printed
# for diagnosis only. The gate is unfiltered RGB(A) samples.
set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "${ROOT}"
PNG="${ROOT}/poster/rc/poster_rc.png"
SVG="${ROOT}/poster/rc/poster_rc.svg"
COMPARE="${ROOT}/scripts/compare_poster_png.py"
if [[ ! -f "${SVG}" ]]; then
  echo "ci_rebuild_poster_rc: no ${SVG}; skip"
  exit 0
fi
if [[ ! -f "${PNG}" ]]; then
  echo "ci_rebuild_poster_rc: missing committed PNG" >&2
  exit 1
fi
if [[ ! -f "${COMPARE}" ]]; then
  echo "ci_rebuild_poster_rc: missing ${COMPARE}" >&2
  exit 1
fi
WORKDIR="$(mktemp -d)"
cleanup() { rm -rf "${WORKDIR}"; }
trap cleanup EXIT
cp -f "${PNG}" "${WORKDIR}/committed.png"
echo "ci_rebuild_poster_rc: committed file sha256=$(sha256sum "${PNG}" | awk '{print $1}') size=$(stat -c%s "${PNG}")"
rm -f "${PNG}"
bash "${ROOT}/scripts/build_poster_rc.sh"
echo "ci_rebuild_poster_rc: rebuilt file sha256=$(sha256sum "${PNG}" | awk '{print $1}') size=$(stat -c%s "${PNG}")"
python3 "${COMPARE}" "${WORKDIR}/committed.png" "${PNG}"
