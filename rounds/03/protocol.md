# Round 3 protocol

Four isolated thesis writers (T1–T4) receive the same verified claims and do not see one another’s proposals.

Two independent `poster-red-team` scorers then score all four with locked weights in `.cursor/rules/scoring-rubric.mdc`. Record both scores and the mean in `state/scoreboard.json`.

- Discard total < 75
- Finalist ≥ 85
- If none reach 75, keep the highest as `provisional`

Orchestrator writes `poster/theses.md` and `poster/storyboards/*.md` (markdown outlines only). No group-final without `state/decisions.md`.
