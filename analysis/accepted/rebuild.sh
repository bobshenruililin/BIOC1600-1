#!/bin/sh
set -e
cd "$(dirname "$0")/atlas"
python3 -m unittest discover -s tests -v
python3 atlas.py
cd ../occupancy_kinetics
python3 -m unittest discover -s tests -v
python3 figures.py
cd ..
mkdir -p figures
cp atlas/figures/atlas.svg figures/atlas.svg
cp atlas/figures/CAPTION.md figures/atlas.CAPTION.md
cp occupancy_kinetics/figures/occupancy.svg figures/occupancy.svg
cp occupancy_kinetics/figures/clocks.svg figures/clocks.svg
cp occupancy_kinetics/figures/sensitivity.svg figures/sensitivity.svg
cp occupancy_kinetics/figures/span_identity.svg figures/span_identity.svg
cp occupancy_kinetics/figures/protocol_clocks.svg figures/protocol_clocks.svg
cp occupancy_kinetics/figures/two_regime_clocks.svg figures/two_regime_clocks.svg
cp occupancy_kinetics/figures/CAPTION.md figures/occupancy.CAPTION.md
echo "rebuild ok"
