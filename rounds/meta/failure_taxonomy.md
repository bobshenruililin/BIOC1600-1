# Failure taxonomy (observed this cycle only)

1. **Kd collapsed into LOD** — extractor A/B disagreed on Hu 1.8 nM quantity type; consensus EC50.
2. **Review-table mislabel** — Park 2023 “Glutamate FET” is PfGDH.
3. **Compartment overclaim** — Herman 25 nM called extrasynaptic; paper’s language is ambient/baseline.
4. **Hunter miss** — Clay 2018 0.73/0.8 s was present in PMC HTML after a first pass said absent.
5. **Thesis-frame collapse** — four isolated thesis writers all refined “cannot claim neurodynamics”; zero framing challengers until T5 was forced.
6. **Citation-as-measurement** — Hu methods “Kd = 12 µM (Wu 2022)” is a citation edge.

## Meta A/B (one round)

Frozen observation: 4/4 isolated theses shared the same frame (diversity = 0).

Candidate patch: `AGENTS.md` Round 3 paragraph requiring at least one thesis that challenges the current framing.

Benchmark: after the patch instruction, T5 exists (diversity = 1/5). Rubric novelty mean rises (4.0 → includes a 5). No citation regression.

Stop: one adopted patch addressing the observed collapse. No further prompt churn. Constitution/rubric/safety untouched.
