# Evidence atlas

**Question.** Which quantity types actually exist for which glutamate-related constructs?

**Answer format.** A construct × quantity-type grid. Empty cells stay empty. No interpolation. Non-glutamate kinetic numbers are excluded from glutamate rows.

## Rebuild

```bash
python3 -m unittest discover -s tests -v
python3 atlas.py
```

Outputs: `figures/atlas.svg` and `figures/CAPTION.md`.

## Provenance

Reads `/workspace/research/evidence/core_evidence.csv` if present, else a path passed as `--csv`. Only rows listed in `atlas.py:SELECTED` are drawn. Values are copied as strings from the ledger.

## Limitations

- Wu rows are abstract-only.
- kon/koff glutamate cells are empty on purpose (C007).
- Biological tau is stored in the ledger as `response_time` because that is the allowed field; the caption says it is a cleft inference, not a sensor spec.
