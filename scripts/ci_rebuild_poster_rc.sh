#!/usr/bin/env bash
# CI helper: delete committed PNG, rebuild, require SHA-256 match.
# Fail if poster RC source is present but renderer/rebuild/checksum fails.
set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "${ROOT}"
PNG="${ROOT}/poster/rc/poster_rc.png"
SVG="${ROOT}/poster/rc/poster_rc.svg"
if [[ ! -f "${SVG}" ]]; then
  echo "ci_rebuild_poster_rc: no ${SVG}; skip"
  exit 0
fi
if [[ ! -f "${PNG}" ]]; then
  echo "ci_rebuild_poster_rc: missing committed PNG" >&2
  exit 1
fi
committed="$(sha256sum "${PNG}" | awk '{print $1}')"
rm -f "${PNG}"
bash "${ROOT}/scripts/build_poster_rc.sh"
rebuilt="$(sha256sum "${PNG}" | awk '{print $1}')"
if [[ "${rebuilt}" != "${committed}" ]]; then
  echo "ci_rebuild_poster_rc: PNG checksum mismatch rebuilt=${rebuilt} committed=${committed}" >&2
  exit 1
fi
echo "ci_rebuild_poster_rc: OK ${committed}"
