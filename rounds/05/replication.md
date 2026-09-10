# Round 5 replication and caption audit

Clean copy at `/tmp/bioc1600-replicate-*` containing only `research/evidence/core_evidence.csv` and `analysis/accepted/`. Figures deleted, then `sh rebuild.sh`.

Result: tests passed; `atlas.svg`, `occupancy.svg`, `clocks.svg` regenerated.

Caption audit: occupancy/clocks captions contain SIMULATION and BOUND; they do not claim a measured glutamate kon/koff. Atlas caption states empty cells are empty. Banned-phrase grep for “glutamate kon” / “measured koff” / “proves” on the occupancy caption was clean.

No analysis rejected. P5 FASTAptamer was never implemented (not a replication failure).
