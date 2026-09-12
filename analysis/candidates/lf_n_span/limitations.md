# Limitations

- Hu's Langmuir–Freundlich exponent *n* is unpublished. No value in this package is a measurement of n.
- Herman ~25 nM (acute hippocampal slice) and Clements ~1.1 mM / 1.2 ms (cultured hippocampal synapses, abstract kinetic inference) are different preparations. Their ratio is a labeled literature-example arithmetic, not a retinal range and not a surface-electrode specification. Transferable: **no**.
- 1.8 nM is C005 AuED-MEA PBS apparent electrochemical c50, not PaC-probe molecular Kd. Overlay θ(25 nM) is MODELED and is not tissue occupancy.
- Alternative LF parameterizations exist. This package uses θ = c^n / (Kd^n + c^n) so Kd is c50. A different (K, n) writing would need a restated inverse.
- Crowding, mixed SAMs, and MacDonald-style solution-to-surface Kd shifts (S038, not glutamate) are not fitted here.
- This package is an isolated Mission-2 candidate. It is not `analysis/accepted/`.
