# Quantity confusion hunt (O2)
Agent: bc-7ed99a48-eeba-5141-8dde-888bfbc11f8f

Sealed until remaining isolated Stage 1/Wave 2 agents return. Full table also at `/tmp/mission1_confusion.md`.

**Net:** live claims/evidence notes usually split the objects; the closed ten-type schema and the selected occupancy/sensitivity glyphs still perform the collapses the notes warn about.

## Severity split

**Fatal live identity errors:** none identified (Abrantes millimolar ELONA Kd not treated as a ledger number).

**Misleading (glyphs / stale scout / mixed clocks):**
- `rounds/01/merge_sources.py` S050 still says Herman extrasynaptic; live S050/E034/C012 already reject that as Herman’s own label.
- Occupancy.svg + tests + occupancy_table: 1:1 Langmuir θ(25 nM)=0.933 and 81-fold overlay on Hu L–F 1.8 nM; caption already warns, glyph still reports molecular occupancy.
- `model.py` cleft_pulse mixes Herman 25 nM tonic floor with Clements 1.1 mM / 1.2 ms pulse.
- clocks.svg mixes biological τ, bound koff, protocol wait, enzyme, FET stabilize on one axis.
- sensitivity.svg C008 label weaker than C010 “NOT Glu”.
- Atlas thesis LOD cell `0.3 pM` unlabeled PBS (not Ames); E043 comparator invites 32 pM vs 0.3 pM.
- C011 packs 1.1 mM and τ 1.2 ms in one claim; C014 packs SPR Kd and FET LOD; C008 packs kon/koff/Kd.

**Schema-limitation (forced into the ten QUANTITY_TYPES):**
- E033 Clements 1.2 ms stored as `response_time`.
- Incubation / interrogation / sampling all `measurement_time` (E008, E016, E042, E045, E046).
- C021/E036 Hu cited 12 µM typed `Kd_molecular`.
- C005 Hu L–F 1.8 nM typed `EC50`; E004 vs E035 both EC50, 1.8 nM vs 1.8 µM.
- C013/C027 81-fold typed `analytical_working_range`.
- LOD estimator (3SD vs 3RSD) dropped from atlas cells.
- C024 iGluSnFR fold typed `response_time`.
- E014 vs E015 both `Kd_molecular` (kinetic vs equilibrium, tobramycin).

**Already careful:** occupancy/atlas captions; empty glutamate kon/koff cells; C003, C005 vs C021, C007, C009, C012, C025; poster_numbers.md; tests forbidding “measured koff”.

**Suggested later (not gate-blocking while Wave 2 isolation holds):** extend quantity vocabulary; stop selecting 1:1 Hu overlay as canonical occupancy; stamp C008 NOT Glu; label atlas LOD method+matrix; split packed claims.
