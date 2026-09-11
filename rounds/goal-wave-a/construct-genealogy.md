# Construct genealogy of the glutamate DNA aptamer that went into tissue

Lane: 39-mer / Wu `1d04`–`glu1d04` / `glu1` / Hu Fc-thiol / Xiao (lineage test only).  
Mission 1 question this file is allowed to answer: is the recorded next experiment still the highest-information follow-up?

Recorded next experiment (`state/gates/science_story.json`; not edited here):

> Paired solution and surface isotherm of Hu Fc-thiol 39-mer in one buffer; report Langmuir–Freundlich n

**Verdict.** Yes. Wu’s closed VoR no longer hides the truncation cut. Springer ESM (OA Word SI) shows Hu’s tissue oligo **is** Wu `glu1`. What remains empty is `Kd_molecular` of that exact 39-mer. The load-bearing illegal transfer is still the 98-nt isolate’s 12 µM written onto the 39-mer. That is why the paired isotherm is still the Mission 1 experiment, not a lower LOD and not “open Wu VoR” as a substitute.

Gate status stays **REVISE**. This file does not re-score theses or rewrite the nightly summary.

---

## 1. Access (this session)

| Source | Route | `full_text_inspected` | What was actually read |
| --- | --- | --- | --- |
| Wu 2022 S001 VoR `10.1007/s00216-021-03783-w` | Unpaywall `is_oa=false`; Europe PMC `inEPMC=N`; OpenAlex closed; JuSER abstract only | **no** | PubMed/Europe PMC **abstract only**. Do not fill VoR numbers from Lam, TrAC, or Abrantes. |
| Wu 2022 ESM `216_2021_3783_MOESM1_ESM.docx` | Springer static ESM CDN, HTTP 200 | **yes** | Table S1 sequences; Fig. S5 caption; immobilization/selectivity paragraphs. PDF of VoR **not** stored. |
| Hu 2025 journal S002 `10.1016/j.bios.2025.117992` | RWTH OA PDF; CC-BY | **yes** | Experimental sequences; §3.2 isotherm/LOD/wait; Fig. 5 PBS recipe. |
| Hu 2025 journal SI `S0956566325008681-mmc1.docx` | Elsevier ARS, HTTP 200 | **yes** | PBS / PB / aCSF recipes; Fig. S8 Glu wait. |
| Hu 2025 thesis S066 `10.18154/RWTH-2025-07238` | RWTH OA PDF text extract; PDF not in git | **yes** | Table 3.1; Ch. 5–6 Glu-apt on MEA and PaC probe. |
| Lam 2022 S011 PMC9776347 | PMC HTML | **yes** | Secondary table quoting a 98-nt sequence and `12 ± 6 µM` citing Wu. **Not** used as Wu’s error bar. |
| Abrantes 2025 S010 bioRxiv | HTML preprint | **yes** | Quotes `glu1d04` 98-nt and a 58-nt trim. Computational + ELONA on **NG-Apt-Glu**, not Hu’s oligo. |
| Xiao 2025 S021 PMC12376627 | Europe PMC XML | **partial** | Main text SPR `Kd` 293 nM and FET LOD 10 fM. **Table S1 sequence not retrieved** (SI docx 403/520). |
| Hu/Li 2023 TrAC Table 2 | JuSER OA PDF text | **yes** | Review table cites Wu as [35] and prints **32 ± 8 mM** next to the 39-mer. Does **not** match Wu’s abstract. Unused as a number. |

Claim tags below are for this file only. Ledgers were not edited.

---

## 2. Naming (the fact that was missing in Mission 1)

Wu’s **abstract** isolates “aptamer **1d04**” with “dissociation constant of **12 µM**,” then names a truncated electrode oligo “**glu1**.” `primary-source-supported` (abstract).

Wu **ESM Table S1** lists the 98-nt clone as **`glu1d04`**, not `1d04`. Fig. S5 caption then plots “oligonucleotides **1d04** and **2g04**.” `primary-source-supported` (ESM). So **1d04 = glu1d04**. **glu1 ≠ glu1d04**.

Abrantes’ name `glu1d04` for the 98-nt parent matches the ESM table. It is not a merge of `glu1` with `1d04`. `review-supported` only as Abrantes’ citation of Wu; the sequence itself is now also in Wu ESM (`primary-source-supported`).

---

## 3. Sequences (OA only; not invented)

Capture-SELEX library `B2_bank` (ESM Table S1):

`GCATCAGTCCACTCGTGA` + N10 + `TGAGGCTCGAT` + N42 + `AGCGACCTCTGCTAGA`

Constants 18 + 11 + 16 plus N10 + N42 sum to **97 nt**. Every listed “98 nt” clone in Table S1 is **98 letters**. For `glu1d04` the post-dock stretch before the 3′ primer is 43 nt, not 42. Recorded as written; no reconstruction of the extra base.

**H1 — isolate `glu1d04` / `1d04` (98 nt), unmodified in Table S1:**

`GCATCAGTCCACTCGTGAGGTCGACTGATGAGGCTCGATCAGGAGCGCCGCTCGATCGCACTTTCACAGGATAGTAGTTGGTAGCGACCTCTGCTAGA`

Parse against the library (this file, not Wu’s):

| Piece | Sequence | nt |
| --- | --- | ---: |
| 5′ constant = B2-for | `GCATCAGTCCACTCGTGA` | 18 |
| N10 | `GGTCGACTGA` | 10 |
| docking (capture complement) | `TGAGGCTCGAT` | 11 |
| remaining random-like | `CAGGAGCGCCGCTCGATCGCACTTTCACAGGATAGTAGTTGG` + 1 extra T into the 3′ junction | 43 |
| 3′ constant | `AGCGACCTCTGCTAGA` | 16 |

Capture oligo `B2_cap`: `bio-TAC-HEGL-GATCGAGCCTC` (complement of the docking 11-mer).

**H2 — truncated electrode oligos** (ESM: “Truncated aptamer for modifying the electrodes”; coloured underlines on `glu1d04`: blue=`glu1`, red=`glu2`, green=`glu3`):

| Name | Core DNA (5′→3′) | nt | 5′ / 3′ |
| --- | --- | ---: | --- |
| **glu1** | `GCATCAGTCCACTCGTGAGGTCGACTGATGAGGCTCGAT` | 39 | `5′-SH-(CH2)6-` … `-(CH2)6-ferrocene-3′` |
| glu2 | `GTGAGGTCGACTGATGAGGCTCGAT` | 25 | same chemistry |
| glu3 | `GTGAGGTCGACTGATGAGGCTCGATCAGGAGCGCCG` | 36 | same chemistry |

`glu1` = 5′ constant + N10 + docking. It **drops the entire N42 and 3′ constant**. `glu2` is a further 5′ trim of `glu1` (starts at the last four bases of the 5′ primer). `glu3` = `glu2` + first 11 nt of the N42-like stretch.

Wu **abstract** attributes the E-AB LOD/range to **glu1**, not glu2/glu3. ESM QCM, chronocoulometry, and the 10 min ACV calibration paragraph are written for **glu1**. Sensor numbers for glu2/glu3: **empty** (`unresolved`; VoR closed).

**H3 — Hu Glu-apt (journal + thesis), DNA identity with glu1:**

`5′-HO-(CH2)6-S-S-(CH2)6-GCATCAGTCCACTCGTGAGGTCGACTGATGAGGCTCGAT-Fc-3′`

39 DNA letters **identical** to Wu `glu1`. `primary-source-supported` (Hu VoR experimental section; thesis Table 3.1; Wu ESM Table S1). 5′ disulfide vs ESM’s `5′-SH` is the usual TCEP-reduced precursor (`transferable=unknown` as a chemical hop; both are intended Au–S).

Thesis footnote: PaC-probe Glu-apt from **Sangon**; journal MEA oligos from **FRIZ**. Same letters; vendor hop `transferable=unknown`.

---

## 4. Construct cards and which quantities attach

### H0 — library, not a binder

Capture-SELEX on magnetic beads in “complex medium” (abstract). ESM Fig. S1–S4: elution vs glutamic acid in “transparent buffer” and “NB buffer.” Buffer recipes: **empty** (VoR closed). No Kd.

### H1 — `glu1d04` / `1d04` in solution-like assays

| Quantity | Value | Locator | Tag | Attach |
| --- | --- | --- | --- | --- |
| `Kd_molecular` | **12 µM** | Wu abstract | `primary-source-supported` | **This clone.** Method (ITC vs fluorescence vs elution fit) is in the closed VoR. ESM Fig. S5 is Cy5 fluorescence vs glutamic acid for **1d04 and 2g04**, plus `B2_bank` and no-aptamer controls — **no fitted Kd in the ESM text**. |
| `12 ± 6 µM` | — | Lam Table 1 citing Wu | `review-supported` only as Lam’s quotation | **Do not enter as Wu.** Abstract has 12 µM without ±. |
| `kon` / `koff` | empty | glutamate search + this ESM | `unresolved` | |

`transferable` onto glu1/Hu 39-mer: **no**.

### H2 — Wu `glu1` Fc-thiol + **MCH** on gold (not tissue)

ESM, not VoR:

- Immobilization [aptamer] tested 0.1 / 0.25 / 0.5 µM; QCM example **0.25 µM glu1** then **1 mM MCH**.
- Chronocoulometric density at 0.25 µM: **4.74 × 10¹¹ molecules cm⁻²**. `primary-source-supported` (ESM). MCH literature density in the same paragraph is quoted, not remeasured here.
- ACV wait: **10 min** after glutamate. `measurement_time`. `primary-source-supported` (ESM).
- Selectivity (qualitative in ESM): **1 µM glutamate** vs **10 µM** dopamine, uric acid, L-lactate, **GABA**, **aspartic acid** in **10 mM PBS**. Ratios: **empty**. Matrix is 10 mM PBS, not Hu’s Mg-PBS and not Ames.
- Regeneration: ~90 °C PBS, 15 min.
- Real-sample matrices named: aCSF (recipe in ESM), 100× and 10× diluted human serum.
- Abstract LOD **0.0013 pM**; range **0.01 pM–1 nM**; “good selectivity … tenfold diluted human serum.” `sensor_LOD` / `analytical_working_range` on **surface glu1**, not H1. `primary-source-supported` (abstract). LOD matrix vs serum matrix not separable from the abstract. `transferable=no` onto Hu MEA or PaC.

No solution `Kd_molecular` of truncated glu1 in abstract or ESM. `unresolved`.

### H3 — Hu journal Glu-apt on **AuED-MEA**, thiol-PEG, potential-pulse

Same 39-nt DNA. Differences from H2 that Mission 1 already treated as non-null, now sequence-locked:

| Axis | Wu glu1 (ESM) | Hu journal Glu-apt |
| --- | --- | --- |
| Backfill | MCH | thiol-PEG 2 kDa |
| Immobilization | drop/QCM 0.25 µM (ESM) | PA 1 µM in 10 mM PB + 450 mM K₂SO₄; ST-optimized packing **1.43 ± 0.37 × 10¹³ cm⁻²** (ST as model, not a Glu-only density) |
| Electrode | gold (macro / QCM) | AuED microelectrodes, 0.6 V / 7 min |
| ACV wait | 10 min | **15 min** Glu (journal §3.2 + Fig. S8); DA 10 min |
| Assay buffer | selectivity in 10 mM PBS | **low-salt PBS: 137 mM NaCl, 2.7 mM KCl, 10 mM Na₂HPO₄, 1.8 mM NaH₂PO₄, 2 mM MgCl₂, pH 7.4** |
| Signal | — | Glu **signal-on**; ST/DA signal-off |

Quantities that attach to **H3 only**:

| Quantity | Value | Locator | Tag |
| --- | --- | --- | --- |
| `Kd_molecular` label **12 µM** | citation of Wu next to the 39-mer | Experimental section | `primary-source-supported` as a **citation**, not a remeasurement (Mission 1 C021). **Illegal transfer if used as this oligo’s Kd.** |
| apparent electrochemical Kd / `EC50` | **1.8 nM** Langmuir–Freundlich | §3.2 | `primary-source-supported`. Authors’ 2D-confinement sentence is **their interpretation**, not a solution remeasurement. |
| `sensor_LOD` | **32 pM** PBS; **51.5 pM** 50% serum | Fig. 4h; §3.4 / Fig. S11 | `primary-source-supported` |
| `analytical_working_range` | **0.1 nM–10 µM** semi-log | Fig. 4e | `primary-source-supported` |
| `measurement_time` | **15 min** Glu incubation | §3.2; Fig. S8 | `primary-source-supported` |
| LF exponent n | empty | — | `unresolved` |

`transferable` H2 LOD 0.0013 pM → H3 32 pM: **no**.  
`transferable` H3 1.8 nM → H1 12 µM or vice versa: **no**.  
`transferable` H3 1.8 nM → PaC probe (H4): **no** (different electrode, pulse, packing, wait, vendor).

### H4 — the oligo that actually went into tissue (thesis Ch. 6)

Same 39-nt Glu-apt\* (Sangon), 3′ Fc, 5′ disulfide, thiol-PEG, **PA on AuED parylene-C shank**. Bottom Ø 25 µm electrode for ACV; upper Ø 15 µm for spikes. **In vitro mouse retina in Ames**, not in vivo.

| Axis | vs H3 |
| --- | --- |
| PA pulse | **+0.5 / +0.1 V**, 1 s (MEA was +0.6 / +0.1 V) |
| Glu packing (this electrode) | **0.80 ± 0.26 × 10¹³ molecules cm⁻²** PA vs 0.75 ± 0.17 × 10¹³ dipping (Fig. 6.5B). ~17× Wu glu1’s 4.74 × 10¹¹. |
| Wait after 10 nM Glu | plateau **~10 min** (Fig. 6.6). Body vs caption 10 nM / 100 nM disagreement: record both; do not pick. |
| PBS calibration | linear **1 nM–1 mM**; LOD **0.3 pM** blank+3 RSD (Fig. 6.7). Not Ames, not tissue. |
| Ames | linear **10 nM–10 µM**; authors: 41.6% blank noise, poor quantitative SNR (Fig. 6.9A). |
| Selectivity panel | **100 nM Glu** vs **10 µM** ST, DA, Tyr, Lac (Fig. 6.8A). **Aspartate and glutamine absent.** Wu ESM named Asp/GABA on **H2**, not on this probe. `transferable=no`. |
| Tissue clock | ACV **14 s/scan**, then **~1 min** sampling; authors: **basal Glu, not synaptic transients**. |
| Apparent Kd on probe / Ames / tissue | **empty** |

EIS on the probe used a different PBS (**10 mM PBS, 200 mM NaCl, 15 mM KCl, pH 7.4**) than the journal ACV PBS. Do not merge those buffers.

### Out of this tissue lineage (keep off the 39-mer card)

- **Ohsawa 2008**: arginine-modified DNA vs avidin–glutamate conjugates; authors conclude no aptamer to **free** glutamic acid. Different chemistry. Not H1–H4.
- **Xiao 2025**: SPR `Kd_molecular` **293 nM**; FET `sensor_LOD` **10 fM** in **0.1× PBS**; stabilize **200 s**. Sequence is in Table S1 SI, **not inspected this session**. Lineage vs Wu **unknown**. Do not put 293 nM on the 39-mer.
- **Abrantes NG-Apt-Glu**: 58-nt 5′ prefix of `glu1d04` (`glu1d04[:58]`), in silico trim, 5′-amino on graphene FET. Docking scores are `computational illustration`. ELONA used 0–50 mM glutamate; fitted Kd **not entered** (Mission 1: do not promote). Not the tissue oligo.

---

## 5. Transfer table (each hop)

| Hop | What changes | `transferable` | Why |
| --- | --- | --- | --- |
| library → `glu1d04` | isolate vs pool | n/a | selection, not a property transfer |
| `glu1d04` → `glu1` | drop N42 + 3′ constant; add SH + Fc | **no** | truncation + labels; no solution Kd of glu1 |
| `glu1` → `glu2` / `glu3` | further cuts | **unknown** | sequences exist; quantities empty |
| Wu glu1 / MCH / gold → Hu Glu-apt / PEG / AuED-MEA | backfill, packing (~10²), pulse, Mg-PBS, 10→15 min | **no** | LOD 0.0013 pM vs 32 pM already shows the devices disagree |
| Hu methods 12 µM citation → Hu 1.8 nM LF | citation vs surface fit | **no** | different quantity types |
| H3 MEA → H4 PaC probe | electrode, pulse, packing measured on Glu, vendor, 15→10 min, Ames | **no** | 32 pM vs 0.3 pM; no probe Kd |
| H4 PBS → Ames → retina | matrix | **no** | authors report Ames SNR collapse |
| H1 12 µM or H3 1.8 nM → θ at Herman 25 nM | occupancy arithmetic | **no** as tissue occupancy | 1:1 overlay of an LF surface number or of the parent Kd |

---

## 6. Load-bearing illegal transfer

**The hop that carries the poster if untreated:** Wu abstract `Kd_molecular` **12 µM** on **`1d04` / `glu1d04` (98 nt)** written beside Hu’s **39-mer** as “Glu-apt, Kd = 12 µM (Wu et al., 2022).”

That single methods line is what lets a storyboard treat 12 µM and 1.8 nM as two measurements of one receptor. They are not. ESM now makes the DNA cut explicit: the 12 µM clone still has the N42-like 3′ body; the tissue oligo is only primer + N10 + docking.

Secondary poison, not a replacement number: Hu/Li 2023 TrAC Table 2 prints **32 ± 8 mM** on the 39-mer letters citing Wu [35]. Wu’s abstract is 12 µM. `review-supported` as “this table exists”; **not** `primary-source-supported` as affinity.

Lesser illegal merges (already Mission 1, still true): glu1 LOD as affinity; 1.8 nM as 1:1 tissue occupancy Kd; 0.3 pM as Ames/tissue LOD; Wu Asp/GABA panel as the retina probe’s selectivity.

---

## 7. Is the recorded paired isotherm still the highest-information Mission 1 experiment?

**Yes**, with one specification and one honest fork.

Mission 1 REVISE hangs on occupancy-at-basal being **unmeasured** on the PaC probe, and on 1.8 nM being an LF surface number that cannot be used as a 1:1 `Kd_molecular` of the 39-mer. Opus unknown 1 and the gate `next_experiment` string are the same experiment: **solution `Kd_molecular` + surface isotherm of Hu’s exact Fc-thiol 39-mer in one buffer, report LF n and coverage.**

What this genealogy changed:

- **No longer unknown:** truncation cut sites. `glu1` = 39-mer = Hu tissue DNA. Mission 1 candidate B’s “Wu truncation cut sites from VoR” is answered from **ESM**, not VoR. Opening the paywalled HTML is now low value for sequence identity.
- **Still empty:** solution `Kd_molecular` of unlabeled 39-mer; of Fc-thiol 39-mer; LF n; probe-in-Ames isotherm.
- **Still empty and not this experiment:** glutamate `kon`/`koff`; retina pharmacology; glu2/glu3 function.

Why not replace it:

| Competitor | Why it is not the Mission 1 occupancy experiment |
| --- | --- |
| Open Wu VoR | Would likely show *how* 12 µM was fitted on **H1**. Would not measure the 39-mer. ESM already gave sequences. |
| IPA `kon`/`koff` on the 39-mer | Highest-info for the **cleft-clock** column. Mission 1 preferred story after revision is occupancy/basal, with milliseconds **untested**. Do not swap the experiment to fill a different empty cell. |
| TTX/CNQX/TBOA + scramble on the shank | Highest-info if the poster question is **“is the retina ACV glutamate?”** Opus already forked this: *if* biology-of-retina, substitute pharmacology; do not run both and finish neither. That fork is unchanged. |
| glu2 vs glu3 vs glu1 solution Kd | Useful biochemistry; not the oligo in tissue. |
| Lower LOD / Abrantes FET | Explicitly out of Mission 1 `do_not_promote`. |

**Specification the ESM now forces** (still the same experiment, not a new one):

1. Solution arm: unlabeled 39-mer **and** the Fc-thiol 39-mer, same buffer as the surface arm. If they disagree, the label is part of the construct.
2. Surface arm: gold-electrodeposited + thiol-PEG, coverage reported. Do not use Wu’s MCH 4.74 × 10¹¹ cm⁻² surface as the pair to Hu’s 1.8 nM. Optionally a second surface at PaC-probe coverage (~0.8 × 10¹³ cm⁻²) — valuable, not required to close the 12 µM-vs-1.8 nM methods line.
3. Buffer: Hu low-salt Mg-PBS (the 1.8 nM fit). Ames is a **later** hop; mixing Ames into the first pair would confound construct with matrix.
4. Fit Langmuir **and** Langmuir–Freundlich; report n. That is the gate’s “report n,” still required, still missing.

Falsifiers (unchanged in kind, now DNA-locked):

- Solution and surface Kd of the 39-mer both near **1.8 nM** → confinement is a result; 12 µM parent is a different molecule; “saturated at 25 nM” becomes arithmetically available **on this oligo in this buffer**, still not a PaC-tissue occupancy.
- Both near **12 µM** → 1.8 nM is transduction/interface; θ(25 nM) tiny; occupancy-saturation story dies.
- Solution near 12 µM and surface near 1.8 nM → the methods citation is false as identity and true as “parent vs surface number”; construct non-identity is measured.

A BIOC1600 course cannot run IPA. It can, in principle, run ITC/fluorescence plus one ACV isotherm. That practical constraint still matches the recorded experiment.

---

## 8. Sequence/construct facts that would rewrite the poster story

**Already in hand (this session), and they do rewrite the construct panel:**

1. The tissue receptor **is Wu `glu1`**, letter-for-letter, not a vaguely “related 39-mer.” Secondary Lam/Abrantes quotes are no longer required for that identity.
2. `glu1` is not “the aptamer, shortened.” It is the Capture-SELEX **5′ primer + N10 + docking 11-mer**. Binding during selection had to compete with `B2_cap` on that docking sequence. Whether glutamate still uses that module after dropping N42 is **unmeasured**. Docking-as-binding-site is `hypothesis`.
3. Wu synthesized **three** electrode truncations. Hu used **glu1 only**. A poster that says “the truncated aptamer” as a singular biochemical object is underspecified.
4. Packing on the tissue electrode (Glu, Fig. 6.5) is **~17-fold** Wu glu1/MCH. Immobilization is not a null operation even inside one DNA sequence.

**Would rewrite occupancy arithmetic if measured:** a 39-mer solution Kd. That is the recorded experiment, not a new one.

**Would rewrite lineage if the Xiao SI sequence matched glu1.** SI not retrieved. Until then Xiao stays a parallel glutamate aptamer with SPR 293 nM, not this tree.

**Would rewrite the illegal-transfer story if Wu VoR showed 12 µM measured on glu1.** Abstract and ESM currently attach 12 µM / fluorescence traces to **1d04**, not to glu1. Do not anticipate the VoR.

---

## 9. Negative-search notes (enough to show what was opened)

- Unpaywall/OpenAlex/Europe PMC: Wu VoR closed; no author-accepted manuscript.
- Springer ESM filename `216_2021_3783_MOESM1_ESM.docx` **is** OA; `.pdf` ESM 403. Sequences taken from the docx.
- Exact 39-mer string: Europe PMC query hitCount 0 (sequence not indexed as text). Recovered from Hu OA + Wu ESM.
- Xiao SI `ADVS-12-e04497-s001.docx`: PMC/Europe PMC/Wiley paths failed (404/520/403). Sequence remains empty here.
- Changtong Wu dissertation: not found as an OA substitute for the VoR.
- TrAC 32 ± 8 mM: inspected, rejected as Wu’s Kd.

---

## 10. Mission 1 close (this lane only)

| Before | After this genealogy |
| --- | --- |
| glu1 vs Hu 39-mer identity inferred | **Identical DNA**; Hu disulfide/Fc/PEG/PA/AuED/PaC are later hops |
| Truncation cuts behind VoR | **Cuts in ESM Table S1** |
| 12 µM on “the Glu aptamer” | 12 µM on **98-nt `glu1d04`**; empty on 39-mer |
| Next experiment: paired 39-mer isotherm | **Still the highest-information Mission 1 follow-up** |
| Gate | Unchanged: **REVISE**; occupancy-at-basal unmeasured |

Highest-information next experiment remains: **paired solution and surface isotherm of the Hu Fc-thiol 39-mer (`glu1` DNA) in the published Mg-PBS, report Langmuir–Freundlich n and coverage.** If the poster question is switched to “is the retina ACV glutamate?”, replace it with pharmacology — that is a different question, not a better measurement of the 39-mer’s Kd.
