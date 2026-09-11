# Mission 2 input queue

This is the bounded handoff from Mission 1. It is not a second claim ledger and it does not promote challenger PR text into canonical science. Mission 2 must re-read the source artifact, reproduce any analysis it selects, and use the normal evidence pipeline before changing `state/claims.csv` or `research/evidence/core_evidence.csv`.

Mission 2 must use one integration PR and may open at most one independently justified challenger PR. The replacement flagship remains undecided.

## Accepted facts and boundaries already canonical

- Revised D is the canonical working thesis, not group-final.
- Hu’s retinal result is positive evidence within its demonstrated slow/basal regime (C031, C033, C034, C028, C030).
- Occupancy on the PaC retinal probe is unmeasured. Hu 1.8 nM is an AuED-MEA Langmuir–Freundlich apparent fit in PBS, not the PaC probe’s molecular Kd (C005, C021, C026).
- The 1:1 Langmuir 10–90% span is exactly 81-fold (C027/C013). It is supporting biochemistry, not the accepted flagship and not Hu’s fitted working range.
- No glutamate-aptamer `kon`/`koff` is in the inspected canonical set (C007). Missing rates do not prove slow kinetics.
- The original 81-fold-versus-44,000-fold flagship is withdrawn. The two endpoint values remain valid in their own named hippocampal preparations; their comparison is not accepted as a representative device requirement.

## Audited candidate evidence — requires promotion before canonical use

1. **Basal-pole and compartment audit:** PRs #26 and #31. Recheck each primary source, method, region, species, sample size, and quantity class. Do not average unlike measurements. Decide whether any value specifies the concentration seen by a surface electrode.
2. **Construct and interface:** PRs #9 and #21. Confirm the 98-nt parent versus 39-mer sequence genealogy and all solution-to-surface/device/matrix hops before using any affinity value.
3. **Comparator evidence:** PR #6. Audit GluOx response-time, matrix, selectivity, and longevity rows before using the comparator in the poster.
4. **Kinetics:** PR #14 plus scout #13. Preserve the negative glutamate-rate search and the non-transfer boundary for other ligands.
5. **New-source backlog:** PR #17. Promote only source/claim pairs that survive identifier, locator, quantity-type, construct, matrix, and full-text checks.
6. **Raw candidate-source bundles:** PRs #8, #10, #12, #13, #15, and #16. Treat as search provenance, not merged evidence.

## Analysis candidates — reproduce before selection

1. **Interrogation/sampling-timescale mismatch (PR #24).** Candidate claim: the 14 s ACV interrogation and roughly 60 s sampling cadence cannot preserve the shape of a 1.2 ms literature waveform even if occupancy were instantaneous. Use the coarse clock-ratio result. Do not call the argument “Nyquist” in canonical text unless the signal model, bandwidth, sampling operator, and reconstruction claim are formally defended. Do not convert protocol time into `koff`.
2. **Working-range bars (PR #23).** Recheck every endpoint and unit, then test robustness to basal-pole choice and Langmuir–Freundlich *n* before considering it as a flagship.
3. **Analysis tournament (PR #11).** Retain proposal scores as provenance only; scores do not accept an analysis.
4. **81-fold identity figure (already reproducible in PR #28).** Retain as a supporting biochemical figure. It cannot by itself select a biological span or establish a device requirement.

## Unresolved hypotheses and adversarial tests

- PR #31: basal measurements span method- and compartment-dependent values, and an unknown Langmuir–Freundlich exponent can change the working-range conclusion. This is the reason the original flagship was withdrawn; the candidate rows still require canonical audit.
- PRs #18 and #25: a sampling-volume/release-domain concern survives, but the strong claim that faster sensors necessarily measure the “wrong quantity” is not accepted.
- PR #19: the LF-to-1:1 and AuED-MEA-to-PaC hops are invalid for tissue occupancy. Other occupancy arguments remain unresolved.
- PR #6: whether an enzyme comparator should reorganize the poster remains an open framing test, not a conclusion.
- Unknown bulk-ECF transient amplitude at the relevant electrode site; unknown PaC apparent Kd in Ames/tissue; unknown glutamate `kon`/`koff`; unknown chemical identity of the light-correlated retinal ACV change.

## Highest-information construct experiment

Paired solution and surface isotherms of the exact Hu Fc-thiol 39-mer in one justified buffer:

- include unlabeled and Fc-thiol forms where feasible so the label is not a hidden construct change;
- use a binding-null point mutant in both arms;
- use the same construct, buffer, and measurement conditions across arms;
- fit both Langmuir and Langmuir–Freundlich models and report *n* with uncertainty;
- report achieved surface coverage and the complete interface chemistry;
- include L-glutamine and L-aspartate at concentrations justified for the intended biological medium;
- keep the PaC/Ames transfer as a later, separately identified hop.

This experiment tests sensor fitness. If the project instead locks the question to retinal chemical identity, substitute pharmacology plus a scrambled/binding-null probe; do not blend both questions into one underpowered experiment.

## Mission 2 exit condition

Mission 2 may nominate a flagship only after the selected analysis has been rebuilt from a clean checkout, its inputs are canonical or explicitly candidate-tagged, its conclusion survives sensitivity analysis, and an independent reviewer is asked whether the evidence supports the claim rather than whether the story is attractive.

Full PR provenance and exact SHAs: `state/pr_disposition_register.md`.
