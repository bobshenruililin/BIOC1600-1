#!/bin/sh
set -e
cd "$(dirname "$0")"
python3 -m unittest discover -s tests -v
python3 figures.py
echo "working_range rebuild ok"
