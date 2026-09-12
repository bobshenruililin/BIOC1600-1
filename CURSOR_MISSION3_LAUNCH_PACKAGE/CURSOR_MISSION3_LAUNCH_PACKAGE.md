# Cursor Mission 3 launch package

## Give Cursor now

Use the existing Cursor Project that contains the selected `eyefix-package` sources.

1. Paste `MISSION3_MATERIALIZATION_GOAL_FINAL.md` as the sole active `/goal`.
2. Attach `ASTRA_MISSION3_DESIGN_CONTRACT_AUDIT.md` as the gated pre-composition audit contract.
3. Attach `ASTRA_MISSION3_COLD_AUDIT.md` as the gated finished-pixel audit contract.
4. Keep the existing Mission 3 constitution and the selected Project Context objects available.

Do not attach the superseded original goal as a competing instruction. Keep the long workflow transcript as historical provenance only; Cursor should not load it unless resolving a named provenance gap.

## Live repository anchor verified 2026-09-12

- Repository: `bobshenruililin/BIOC1600-1`
- Canonical main: `3fa11240c85df9ebac58dcc6879494911968f75c`
- Integration PR: `#33`, branch `cursor/m3-int-eyefix-245a`
- Observed PR head: `c519197d1d1b2a3bb3a1f90fa5bf4061bca12edd`
- Observed exact-head validation: workflow run `34696427958`, success
- PR #33 remains open, draft, mergeable, and unmerged.
- Current PR contains only three pointer/status files; it does not yet contain the poster package.

Cursor must reverify these anchors at launch and again before audit and PI handoff.

## Operating model

Cursor is the long-horizon owner: context recovery, durable source export, planning, worker coordination, integration, rendering, tests, CI, finding disposition, and recovery after interruption.

GPT-6 Astra is used exactly twice:

1. After source export, to audit the semantic design contract before composition—only if the required packet is complete.
2. After a committed, reproducible, pixel-inspected candidate passes exact-head production CI, to audit the finished visual object.

No general Astra swarm and no automatic rerun. Cursor/Sol implements bounded findings. The PI retains merge and final-release authority.

## Expected checkpoints

- A — selected Context sources exported, opened, inventoried, and hashed.
- B — design contract audited or explicitly skipped because its packet was incomplete; findings dispositioned.
- C — complete poster rendered and both talks aligned.
- D — separate-clean-checkout rebuild, full crop-covered pixel QA, provenance, repository validation, fresh-clone delivery check, and exact-head production CI pass.
- E — finished candidate receives the single cold Astra audit.
- F — findings repaired within scope or stopped at a concrete PI boundary; handoff package complete.

Cursor should continue automatically between checkpoints and stop only for an exact missing prerequisite or a PI decision that would change frozen science.
