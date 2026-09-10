#!/bin/sh
set -e
cd "$(dirname "$0")/atlas"
python3 -m unittest discover -s tests -v
python3 atlas.py
cd ../occupancy_kinetics
python3 -m unittest discover -s tests -v
python3 figures.py
echo "rebuild ok"
