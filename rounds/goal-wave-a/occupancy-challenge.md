# Adversarial review: occupancy/kinetics as flagship

Lane: falsify or demote `analysis/accepted/occupancy_kinetics/` (with `analysis/accepted/atlas/` and captions). Isolated inspection of the accepted tree; no other Wave A reports or PRs were read.

**Verdict: REPLACE** the occupancy/kinetics package as flagship.

**Replace with:** a construct-locked **analytical working-range vs biological-concentration poles** plot (ledger `analytical_working_range` against Herman ~25 nM and Clements 1.1 mM). No 1:1 Langmuir θ, no Langmuir–Freundlich EC50 used as Kd, no C008/C010 kon. Until that panel exists, the only accepted analysis that should be called flagship is the atlas (`analysis/accepted/atlas/`), and even it needs a quantity-type caption on the green 1.2 ms cell.

**Highest-information next experiment from this critique:** paired solution-phase and surface isotherm of Hu’s exact Fc-thiol 39-mer in one buffer; fit Langmuir and Langmuir–Freundlich; **report n** with a confidence interval.

Computational illustration stays labeled. No glutamate kon/koff was invented. Hash-locked files were not edited.

---

## 0. What was actually inspected

| object | what I did | full_text_inspected |
| --- | --- | --- |
| Occupancy code, tests, CSV, SVGs, captions | read + `sh analysis/accepted/rebuild.sh` (pass) + independent Python recompute of all 12 table rows | n/a (repo) |
| Atlas code, tests, SVG | read; confirmed glutamate kon/koff cells empty; 1.2 ms stored as `response_time` | n/a (repo) |
| Hu 2025 journal S002 DOI 10.1016/j.bios.2025.117992 | OA text from RWTH Publications record 1019759 (CC-BY VoR). No PDF committed. | **yes** (OA HTML/text, 2026-09-11) |
| Hu 2025 thesis S066 DOI 10.18154/RWTH-2025-07238 | OA text from RWTH record 1017243; searched for fitted n and 1.8 nM | **partial** (methods/isotherm chapters) |
| Ricci 2016 PMC5660318 | OA HTML; 81-fold 1:1 Langmuir identity | **yes** |
| Ding 2024 PMID 38785220 | PubMed/publisher abstract only (VoR closed) | **partial** (abstract) |
| Abeykoon 2025 C008 | ledger + PMC Fig. 3 numbers already in C008; not re-used as glutamate rates | ledger; not re-opened as a Glu source |
| Herman / Clements | ledger C011/C012/E032–E034 only this pass | **no** new VoR this pass |

Independence rule: Mission 1 already recommended demoting the 1.8 nM overlay. This review does not treat that as verified. New load-bearing points below are from re-running the code and re-reading Hu/Ricci/Ding.

---

## 1. Rebuild and arithmetic (no new numbers)

Repo tests: 8 top-level + 4 atlas + 13 occupancy = pass. Rebuild: pass. Independent recompute of `occupancy_table.csv`: **12/12 match**.

Identities used (computational illustration unless a ledger claim is cited):

- 1:1 Langmuir 10–90 span = 81 exactly (`c10 = Kd/9`, `c90 = 9 Kd`). Matches C027.
- Herman 25 nM → Clements 1.1 mM = 44 000-fold. Matches C011/C012 arithmetic.
- Table θ(25 nM): 1d04 0.0021; Hu overlay 0.9328; Xiao 0.0786.
- Table 1d04 t_off at kon = 1×10^8 M⁻¹ s⁻¹ = 8.333×10⁻⁴ s.

These identities are correctly coded. The scientific failure is **what is plugged in**, not algebra.

---

## 2. Charge: 1:1 Langmuir overlay on a Langmuir–Freundlich EC50

### 2.1 What Hu measured

Hu §3.2 (OA text, locator: adsorption-isotherm paragraph after multiplex ACV): a Langmuir–Freundlich model was used “to take the inhomogeneity among the adsorption sites into account”; apparent Kd **1.8 nM** (Glu), 2.7 nM (ST), 49.6 µM (DA). Authors contrast these with solution-phase citations and invoke 2D confinement “among others.” `primary-source-supported` (C005, C026). Transferable: **no**.

The occupancy model sets `KD_HU_APPARENT_M = 1.8e-9` and plots θ = c/(c+Kd). Captions say it is not a 1:1 molecular Kd. The **glyph** still reports θ(25 nM)=0.933 in the legend of `occupancy.svg`. Tests require it:

```37:39:analysis/accepted/occupancy_kinetics/tests/test_model.py
    def test_hu_saturated_at_tonic(self):
        th = occupancy(C_TONIC_M, KD_HU_APPARENT_M)
        self.assertGreater(th, 0.9)
```

A unit test that 1:1 Langmuir of an LF EC50 exceeds 0.9 is not a test of code correctness. It hard-codes the illegal overlay as a pass/fail scientific result. `computational illustration` mislabeled as an occupancy finding.

### 2.2 n is missing, so the overlay is not even a bound

Hu journal OA text: **no numerical heterogeneity exponent n**. Negative search: “Langmuir-Freundlich” appears as the model name and as the fit to Fig. 4; no “n = …” for Glu.

Hu thesis eq. (2.14) defines LF as S = Smax a C^n / (1 + a C^n) with n “the surface heterogeneity index, ranging between 0 and 1” (Chapter 2). Chapter 5 says Glu signal-gain vs log concentration “can be fitted by a Langmuir-Freundlich equilibrium model, Figure 5.8E” and then quotes a **log-linear** calibration, not n. Negative search in the thesis extract: no “1.8 nM” string in that file; Glu LOD 32 pM is stated; fitted n is not quoted next to the Glu fit. `unresolved`.

For LF occupancy θ = c^n / (c^n + Kd^n), the 10–90 concentration ratio is **81^(1/n)**, not 81. `computational illustration` (algebra). If n < 1 (Hu’s stated range), the window is **wider** than 81-fold. The n at which 10–90 equals 44 000-fold is n = ln(81)/ln(44000) ≈ 0.41. That is **not** Hu’s n; it is the reason n must be measured before anyone uses C027 against this sensor.

Occupancy.svg’s footnote, “10–90% span is 81-fold for **each** curve,” applies the n = 1 identity to the LF curve. That is a mechanism error, not a caption nit. Tanner objection 10 is correct.

### 2.3 Ricci 2016 does not license Langmuir–Freundlich

Hu cites Ricci et al., 2016 for the LF inhomogeneity sentence. Ricci 2016 *Acc. Chem. Res.* (PMC5660318, inspected) is the **1:1 Langmuir / 81-fold** Account. It does not develop Langmuir–Freundlich. `primary-source-supported` for what Ricci states; `supports_claim=no` for “Ricci = LF.” Hu’s citation is the 81-fold paper used to justify the non-81-fold model. Overlaying 81-fold on Hu’s 1.8 nM then citing C027/Rousseau/Ricci is circular with Hu’s own mis-citation.

### 2.4 Hu’s own calibration contradicts the 1:1 Hu curve

Hu Glu semi-log working range **0.1 nM–10 µM** (C005 neighborhood; poster_numbers; thesis Ch. 5: Signal gain (%) = 25.24 log C + 62.42, 0.1 nM to 10 µM). Fold = 1×10^5. `primary-source-supported`.

A 1:1 10–90 window around 1.8 nM is 0.20 nM–16.2 nM (81-fold). `computational illustration`. That window is not Hu’s published calibration. Occupancy.svg draws a site that is already ~90% occupied near 16 nM, while Hu reports a log-linear calibration continuing to 10 µM. Either (i) signal is not occupancy, (ii) n ≪ 1, or (iii) 1.8 nM is a fit midpoint of a heterogeneous isotherm, not a 1:1 Kd. The occupancy plot assumes (none of these) and still prints θ=0.933 at 25 nM.

### 2.5 Dopamine on the same chip is the counterexample to “confinement rewrites Kd”

Same paragraph, same LF procedure: DA apparent Kd **49.6 µM** vs cited solution **44 µM**. Glu jumps ~10^4-fold (cited 12 µM → 1.8 nM). `primary-source-supported` (Hu OA). A uniform 2D-confinement occupancy story fails inside the table that occupancy.svg treats as three comparable Langmuir sites. Transferable: **no**.

### 2.6 Chip ≠ probe

1.8 nM is AuED-MEA / PBS ACV (S002). The strongest tissue experiment is a parylene-C probe (S066). Occupancy-at-basal on the probe is **unmeasured** as 1:1 θ. Probe 3 “near saturation” is author language plus a gold-detachment confound (C031 notes). Using the MEA EC50 as tissue occupancy is a second hop (device + isotherm). `unresolved` as tissue occupancy; overlay is `computational illustration`.

---

## 3. Charge: non-glutamate kon used as if it constrained glutamate t_off

### 3.1 README vs figure

`occupancy_kinetics/README.md` “Not in this analysis”: “Transferring tobramycin or ITC rates onto glutamate.”

`sensitivity.svg` punchline (generated caption): at C010 high-end kon = 2×10^5 (NOT Glu), 1d04 t_off = 0.42 s. The overnight handoff treats this as a **tested contradiction of T5**.

Labeling “NOT Glu” does not make the operation a bound. A bound requires a monotone inequality that applies to this oligo. An envelope of **other** aptamers is a survey, not a constraint, unless glutamate is assumed typical — which is property transfer. C008 and C010 are tagged `transferable=no`. `do_not_promote` in `state/gates/science_story.json` already lists “glutamate kon/koff from C008 or C010.” The flagship figure does the promotion with a caption disclaimer.

### 3.2 Ding’s actual abstract trend is the opposite pairing

Ding 2024 abstract (PMID 38785220, `partial`): across Kd 28 nM → 864 µM, kon **decreased** 2×10^5 → 96 M⁻¹ s⁻¹ and koff **increased** 1.03×10⁻³ → 0.012 s⁻¹; “both kon and koff contributed… in the same direction.” Not glutamate. Per-construct tables not inspected (VoR closed). `primary-source-supported` as abstract endpoints (C010).

The occupancy model does `koff = kon × Kd_Glu` with a **foreign** kon. That assumes the diffusion-limit factorization Ding’s survey is evidence against (kon is not constant across Kd). Using Ding’s **tight-binder** kon endpoint (2×10^5, paired in the abstract with the 28 nM end of the Kd range) together with 1d04’s **12 µM** Kd is the wrong end of Ding’s stated trend. I do not interpolate a 12 µM kon; interpolation would invent a number. The scientific point: the sensitivity panel’s “even 12 µM is 0.42 s” is a chimeric rate, not an ITC result. `computational illustration`; transferable: **no**.

If one illegally used Ding’s **koff** envelope instead of kon×Kd (still not Glu), t_off would be ~80–970 s, not 0.42 s. I record that only to show the figure chose the pairing that still produces a short-ish “seconds” story. It is not a glutamate measurement.

### 3.3 Tobramycin chimeric koff

Abeykoon: kon 3.5×10^4 M⁻¹ s⁻¹, koff 1.39 s⁻¹, Kd,kinetic 41±11 µM (C008). Internally consistent: koff/kon ≈ 40 µM.

The table’s 1d04 row at C008 kon is t_off = 1/(3.5×10^4 × 12×10⁻⁶) = 2.38 s. Tobramycin’s own t_off = 1/1.39 ≈ 0.72 s. The analysis does not plot the measured tobramycin koff; it multiplies tobramycin kon by a glutamate Kd. Chimeric. `computational illustration`.

### 3.4 Diffusion ceiling is T5’s slogan, protected by tests

`test_diffusion_bound_1d04_near_cleft_tau` requires 0.5 ms < t_off < 2 ms at kon = 1×10^8. That is the T5 “~0.8 ms sits near 1.2 ms” picture, encoded as CI. Clocks.svg then places “1d04 t_off BOUND @ kon=1e8” next to “cleft τ 1.2 ms.” Captions say BOUND. The **geometry** is the slogan.

A diffusion-limited small-molecule kon is an optimistic **upper** speed on association; slower real kon lengthens every t_off (limitations.md is honest here). Clocks.svg shows only the optimistic end. Sensitivity.svg is supposed to be the honest version, but it uses non-Glu kon to do it.

---

## 4. Charge: empty kon/koff cells are painted over

Atlas is the alibi: “so empty kon cells cannot be painted over” (`analysis/accepted/README.md`; nightly §6).

What the occupancy package actually draws:

| cell in atlas | occupancy figure |
| --- | --- |
| 1d04 kon/koff empty | clocks: t_off BOUND; table: four koff-like times |
| Hu Glu-apt kon/koff empty | clocks: Hu t_off BOUND @ 1e8; table: t_off from 5.6 s to 5.8×10^6 s |
| Xiao SPR kon/koff empty | clocks: Xiao t_off BOUND |
| cleft 1.2 ms as `response_time` (green) | clocks: same τ as if it were a kinetic FoM for aptamers |

Empty cells stay empty **on the atlas**. The flagship **clocks** and **sensitivity** figures are the paint. Combined “P1+P2 so we cannot paint” is false as a poster system: storyboard panel 1 is clocks.svg.

Atlas is not clean either:

- E033 1.2 ms is a cleft-clearance **inference**, stored as `response_time` because that is an allowed field. Green cell looks like a sensor spec. Caption discloses; the fill color does not.
- Thesis LOD 0.3 pM is unlabeled PBS (not Ames).
- `measurement_time` mixes 15 min Glu wait (C006) with 10 min 10 nM plateau (C028).

Atlas still correctly **omits** C008/C010 from glutamate rows. That is the one occupancy-adjacent thing it does better than occupancy_kinetics.

---

## 5. Charge: the figures decorate a slogan more than they answer a biochemical question

P1 as **proposed** (`analysis/candidates/round4_proposals.md`): mass-action ODE, Clements-like pulse, kon as a **sensitivity axis**, every curve SIMULATION.

P1 as **implemented**: equilibrium Langmuir of three advertised numbers; t_off = 1/(kon Kd); optional ODE is in `model.py` (`euler_occupancy`, `cleft_pulse`) and **tested**, but `figures.py` does not import or plot them. The biochemical question “can θ(t) follow a 1.2 ms decaying pulse?” is not in the flagship figures.

What occupancy.svg actually answers: “if three non-commensurable published numbers are treated as 1:1 occupancy Kd, who is empty at Herman 25 nM?” That is T5’s inversion, which T5 itself labeled assumption-laden. The 81-fold identity is **stated in a footnote** and **not drawn** as a 10–90 band against a 44 000-fold bar. The one construct-independent biochemical identity (C027) is the part Mission 1 wanted; the accepted flagship figure does not show it.

What clocks.svg answers: a log-time collage of inference τ, optimistic bounds, enzyme t90, FET stabilize, ACV wait. Quantity ontology already flags this collapse. It teaches “timescales differ” — true, and already available from primary protocol clocks (C006, C028, C031, E027) **without** inventing t_off.

What sensitivity.svg answers: t_off vs assumed kon. Useful as a teaching identity τ_eq ≠ t_off at millimolar c (`computational illustration`; limitations.md is right that koff ≈ 1/τ_cleft is the wrong FoM). Independent SVG inspection: Hu polyline (`#d62728`) has **38/81** vertices with y < plot top (ymin = −92.4); Xiao has **16/81** off-canvas. The “three-construct” sensitivity panel is visually a **1d04** panel plus an orange non-Glu band. It cannot carry a Hu occupancy-kinetic story.

Round 4 scores: P1 68/80 (assumptions 6, low-misleading 6); P2 atlas 76/80. P1 was implemented as flagship **because it can contradict T5**. That is circular: T5 exists to challenge “too slow”; occupancy was built to illustrate T5; sensitivity was added to kill T5 with the transfer T5 said was illegal. A figure that exists to defeat a simulation it also draws is not a glutamate result.

Nightly insight 4 still recites θ(25 nM) ≈ 0.93 and 0.8 ms as if they were the computational contribution. They are the slogan.

---

## 6. What survives (do not discard with the package)

Keep, but not as flagship occupancy curves:

1. **C027 1:1 81-fold identity** — algebra, tested, construct-independent. Teaching sentence, not a Hu overlay. `computational illustration`.
2. **Atlas empty glutamate kon/koff** — C007 as a visible hole. `unresolved` absence, honestly drawn on those cells.
3. **τ_eq = 1/(kon c + koff) vs t_off** — first-year identity; forbids koff ≈ 1/1.2 ms at 1.1 mM. Keep as a caption, not as C008-colored curves. `computational illustration`.
4. **Protocol clocks that are measurements** — Hu 15 min (C006), thesis 10 min / 14 s / 1 min (C028, C031), Xiao 200 s (E027). These already kill synaptic-millisecond identification without occupancy θ.

Do not keep as findings:

- θ(25 nM) = 0.93 for Hu Glu-apt
- 1d04 t_off ≈ 0.8 ms as a kinetic near-miss of 1.2 ms
- “C008/C010 put even 12 µM in seconds” as a glutamate constraint
- 81-fold as a property of Hu’s fitted isotherm

---

## 7. Best supporting case for keeping occupancy as flagship (steelman)

If advertised occupancy parameters are treated as Kd, 1d04 is empty at 25 nM and Hu is not; tighter advertised affinity is worse for basal dynamic range; LOD is not occupancy. Captions say SIMULATION. Sensitivity can show that a diffusion ceiling is optimistic. First-year algebra is cheap and reproducible. Course cannot run IPA.

That steelman is why P1 was accepted. It is also why the package is a slogan engine: every load-bearing visual (0.933, 0.8 ms, 0.42 s) is either an illegal overlay or a non-Glu chimeric rate. Unavailability of the right wet experiment does not license a misleading computation as the oral figure.

---

## 8. Best opposing case (this review)

Hu fitted LF for inhomogeneity and did not report n; Ricci 2016 is 1:1 not LF; Hu’s 10^5-fold log-linear calibration is incompatible with a 1:1 site at 1.8 nM; DA on the same chip did not “confine” to nM; 1.8 nM is not the PaC probe; C008/C010 are not glutamate and Ding’s trend is mis-paired; clocks paint empty koff; P1 never plotted the pulse ODE it proposed; tests freeze T5 into CI.

---

## 9. Context: why the plots look like a finding

Apparently conflicting “12 µM vs 1.8 nM vs 293 nM” numbers are **different quantity types on different constructs** (C001, C005, C014, C021). Herman 25 nM is slice ambient by tonic NMDAR current, not [Glu] at an aptamer SAM (C012). Clements 1.1 mM / 1.2 ms is a cultured-synapse kinetic inference, abstract-only (C011). Putting them on one θ([Glu]) axis is the collapse the atlas was built to prevent.

---

## 10. Inference boundary

**Measured:** Hu LF apparent Kd 1.8 nM (MEA, PBS ACV); Hu Glu wait 15 min; thesis 10 min plateau / 1 min sampling / authors refuse synaptic transients; Xiao SPR 293 nM and FET 200 s; 1d04 Kd 12 µM in an abstract; no glutamate kon/koff in inspected sensor papers; Ding/Abeykoon kinetics on other molecules.

**Inferred (not licensed):** occupancy at 25 nM of any glutamate aptamer sensor; t_off of 1d04, Hu Glu-apt, or Xiao oligo; that C008/C010 constrain glutamate; that 81-fold is Hu’s isotherm.

**Unknown:** LF n; solution Kd of the truncated Fc-thiol 39-mer; surface kon/koff of that oligo; PaC-probe isotherm in Ames/tissue.

---

## 11. Falsifier of this critique

If a paired solution + surface isotherm of the **same** 39-mer, one buffer, returns n ≈ 1 and Kd_molecular near 1.8 nM in both phases, then occupancy.svg’s Hu curve becomes a legitimate 1:1 overlay and θ(25 nM) ≈ 0.93 is a finding (still not a koff). Occupancy could then return as a **restricted** flagship: 1:1 curves only, no C008/C010, no 0.8 ms clocks tick.

If n ≈ 1 and solution Kd stays ~12 µM, the overlay dies and this REPLACE stands.

If glutamate surface IPA yields a measured koff, clocks.svg’s bound ticks must be replaced by that number; C008/C010 bands come off.

---

## 12. Wildcard (not in the parent prompt)

Asked only to attack occupancy. Extra direction: **does LF n < 1 let one heterogeneous surface span tonic-to-cleft?** Algebra: yes if n ≲ 0.41 for 10–90 occupancy. Hu’s published Glu calibration already spans 10^5-fold on a log plot, which would correspond to n ≈ 0.38 **if** that span were 10–90 occupancy — it may instead be transduction/log plotting, so I do not enter n. The wildcard is not a result. It is why “81-fold vs 44 000-fold” **cannot** be the replacement flagship for the Hu device until n is reported. That is a change relative to Mission 1’s recommended flagship analysis.

---

## 13. Negative-search record (n)

| search | result |
| --- | --- |
| Hu journal OA text “Langmuir-Freundlich” / “apparent Kd” / “1.8” | model named; 1.8 nM Glu apparent Kd; n not numeric |
| Hu thesis eq. 2.14 and Fig. 5.8E neighborhood | n defined in (0,1]; Glu fitted LF; n not quoted; 1.8 nM string not found in extract |
| Ricci 2016 PMC | 81-fold 1:1; no LF exponent |

“n unreported” is not a gap I failed to look up; it is absent from the OA texts that contain the 1.8 nM result.

---

## 14. Replacement analysis (one)

**Name.** Construct-locked working-range vs biological poles.

**Question.** Which published glutamate-aptamer **calibration windows** contain Herman ~25 nM, and which contain Clements 1.1 mM?

**Method.** One log-[Glu] axis. For each construct, a bar from that row’s `analytical_working_range` only (Wu glu1 0.01 pM–1 nM; Hu MEA PBS 0.1 nM–10 µM; Hu thesis Ames 10 nM–10 µM; Xiao FET 10 fM–100 nM). Ticks at 25 nM and 1.1 mM. No θ(c). No kon. Caption: calibration span is not occupancy; Ames ≠ PBS; 0.1× PBS ≠ aCSF.

**What it shows without transfer (ledger, `primary-source-supported` windows vs C011/C012 ticks):**

- Every listed Glu-apt calibration in this ledger that has a top end **misses 1.1 mM**.
- Hu PBS and Ames windows **contain 25 nM** as a calibration point, which is not occupancy-at-basal.
- Wu glu1 0.01 pM–1 nM contains **neither** pole.

That is a biochemical/analytical question (does the reported working range meet the biological concentrations?) answered with the construct’s own quantity type. It can change a mind that “0.1 nM–10 µM already covers tonic and a wide dynamic range”: 10 µM is not 1.1 mM, and the window is not 1:1 occupancy.

Atlas stays as the empty-kon companion, not as a substitute occupancy plot.

P3 construct audit remains useful as a table, not as the kinetic flagship.

---

## 15. Highest-information next experiment (from this critique)

**Measure the isotherm of Hu’s exact oligo twice, one buffer, one sequence.**

Construct (E036): `5'-HS-C6-GCATCAGTCCACTCGTGAGGTCGACTGATGAGGCTCGAT-Fc-3'`.

1. Solution: ITC or fluorescence titration → `Kd_molecular`, 1:1 model vs alternatives.
2. Surface: ACV on gold-electrodeposited gold under the published PBS conditions → apparent electrochemical Kd; **Langmuir and Langmuir–Freundlich**; report **n** and CI; report coverage.

This experiment decides whether occupancy.svg is a finding or a decoration, whether C027 may be drawn on this sensor, and whether “saturated at 25 nM” is arithmetic. It does not require tissue. It does not fill C007 (kon/koff); IPA on the same SAM is the follow-up if occupancy is rehabilitated.

Not this critique’s first experiment: a lower LOD; docking; transferring C008.

---

## 16. Decision line

**REPLACE** occupancy/kinetics (`occupancy.svg` + `clocks.svg` + `sensitivity.svg`) as flagship.

**With:** construct-locked working-range vs biological poles (above). Interim flagship among *implemented* analyses: **atlas only**, with the 1.2 ms cell captioned as cleft inference not `response_time`.

**Highest-information next experiment:** paired solution/surface isotherm of the Fc-thiol 39-mer; report Langmuir–Freundlich **n**.
