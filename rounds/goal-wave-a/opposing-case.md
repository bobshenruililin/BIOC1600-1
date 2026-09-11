# Goal Wave A — Lane: BEST OPPOSING CASE

Worker: opposing-case lane, `bc-1fdbede0-…-c406`. Branch `cursor/opposing-case-wave-a-c406`.
Search window: 2026-09-11. Access routes used: Europe PMC REST (search + `fullTextXML`), NCBI `efetch` (PMC OA + author manuscripts), Crossref, bioRxiv, publisher OA HTML. No paid APIs. No PDFs committed.

Lane rule followed: this worker did not read `rounds/mission1/candidates/*`, `rounds/mission1/sealed/*`, `analysis/candidates/theses/*`, `poster/theses.md`, or any other Wave A lane output. It did read the orchestrator ledgers (`state/sources.csv`, `state/claims.csv`) to avoid re-deriving settled records and to know what was already contested. Every number below that is load-bearing was pulled from the source by this worker, including re-verification of ledger-inherited anchors.

---

## 0. One-paragraph summary of the opposing case

The strongest argument against a glutamate aptamer biosensor is **not** that aptamers are too slow. It is that the published glutamate aptasensors have been optimised into a concentration decade where brain glutamate does not live, and that the quantity they would measure there — total free extracellular glutamate — has been shown in a 2025 primary experiment to be dominated by a non-neuronal pool that does not move when neurons release glutamate. Speed is the third bottleneck, not the first. Separately, the molecular-recognition foundation of the entire glutamate story rests on a single unreplicated 12 µM number from one laboratory, in a target class where an independent group has demonstrated that three published nanomolar small-molecule aptamers bind nothing at all. There is also a genuinely surprising result inside the opposing case: the **one** reported glutamate affinity that *is* biologically well matched is the 12 µM parent aptamer the field treats as the weak, superseded version.

---

## 1. Search strategy and negative-search record

### 1.1 Queries run (Europe PMC unless noted)

| # | Query | Hits | Yield |
| --- | --- | ---: | --- |
| Q1 | `TITLE:"glutamate" AND TITLE:"aptamer" AND (selectivity OR aspartate OR glutamine)` | 3 | 0 relevant — see §1.2 |
| Q2 | `"glutamate aptamer" AND (glutamine OR aspartate)` | 1 | Abrantes preprint only |
| Q3 | `"1d04" OR "glu1 aptamer"` | 13 | only Wu 2022 itself |
| Q4 | `(glutamate OR glutamic) AND aptamer AND ("k_on" OR "association rate" OR koff OR "dissociation rate constant")` | 96 | 0 glutamate kon/koff |
| Q5 | `CITES:34783880_MED` (everything citing Wu 2022) | 23 | 1 independent expert comment (O4); 0 replications |
| Q6 | `TITLE:"Do Aptamers Always Bind"` | 1 | O3 |
| Q7 | `AUTH:"McKeague" AND TITLE:"Comprehensive Analytical Comparison"` | 1 | O8 |
| Q8 | `AUTH:"Kennedy RT" AND glutamate basal extracellular neuronal origin` + `brain extracellular glutamine concentration microdialysis rat` | 4 / 1097 | O1 |
| Q9 | `aptamer binding kinetics slow association rate conformational change induced fit small molecule SPR` | 116 | O2 |
| Q10 | `AUTH:"Arroyo-Curras" AND (stability OR drift OR degradation) AND aptamer`; `TITLE:"electrochemical aptamer" AND (drift OR fouling OR stability) AND in vivo` | 38 / 46 | O5 |
| Q11 | `AUTH:"Jaquins-Gerstl" AND (penetration injury OR microdialysis)` | 13 | O6 |
| Q12 | `TITLE:"Going Beyond the Debye Length"`; `Debye length screening limitation FET biosensor physiological ionic strength` | 1 / 75 | O7 |
| Q13 | `AUTH:"Alam MA" AND TITLE:"Screening-limited response"`; `TITLE:"Making it stick" AND AUTH:"Squires"` | 1 / 1 | O11, O12 (abstract only) |
| Q14 | `AUTH:"Slavkovic" AND cocaine aptamer quinine affinity`; `TITLE:"cocaine-binding aptamer" AND (selectivity OR quinine OR ligand)` | 11 / 13 | near-miss, §1.3 |
| Q15 | `aptamer folding magnesium divalent cation dependence structure-switching DNA` | 55 | O10 (wildcard) |
| Q16 | `TITLE:(extracellular calcium) AND (activity OR stimulation) AND (decrease OR depletion) AND (cortex OR hippocampus OR brain)` | 114 | **nothing usable** — §1.4 |
| Q17 | `AUTH:"Hascup" AND glutamate second-by-second behaving` | 2 | O9 |
| Q18 | `AUTH:"Danbolt" …`, `AUTH:"Diamond JS" AND glutamate transporter uptake time course` | 16 / 12 | no new primary numbers beyond ledger S062 |

### 1.2 Negative-search integrity — what genuinely is not there

These are searches that returned an informative *absence*, with enough detail to show what was actually looked for.

- **There is no title-level nucleic-acid glutamate aptamer literature.** Q1 (`TITLE:glutamate AND TITLE:aptamer` plus a selectivity term) returns exactly three records: a *peptide* aptamer amperometric sensor (PMID 35623273), and two papers on *Plasmodium falciparum* glutamate dehydrogenase — a protein target, not the neurotransmitter (PMIDs 30308419, 29722521). This independently reproduces the Round-2 citation-auditor finding recorded as `C019`, by a different route.
- **No independent replication of the 1d04/glu1 aptamer exists.** Q3 finds `1d04` only in Wu 2022. Q5 enumerated all 23 Europe PMC records citing Wu 2022: they are reviews, the same Jülich group's follow-ups (Hu 2025), and unrelated sensor papers. Not one re-measures the aptamer. The single substantive independent engagement is a one-sentence chemical judgement (O4, §3.1).
- **No glutamate aptamer kon or koff has been published.** Q4 over 96 records; none reports an association or dissociation rate constant for any glutamate-binding nucleic acid. This confirms ledger claim `C007` by independent search rather than by inheritance.
- **No peer-reviewed study reports glutamate-aptamer cross-reactivity against glutamine or aspartate.** Q2 returns a single record and it is the unrefereed Abrantes bioRxiv preprint. `C032` already notes that the Hu thesis panel omits both.

### 1.3 Near-misses recorded and why they were not used

- **Cocaine/quinine aptamer (Q14).** I pursued the canonical "aptamer binds a non-target better than its target" precedent (Slavkovic, Churcher, Johnson, *Bioorg Med Chem* 2018, DOI 10.1016/j.bmc.2018.09.017, PMID 30266453; Neves et al., *ACS Sens* 2017, PMID 28929744). Both are paywalled; I could reach titles and partial abstracts only, and the title-level claim ("nanomolar binding affinity of quinine-based antimalarial compounds by the cocaine-binding aptamer") is not sufficient to state a selectivity ratio without inventing one. **Dropped rather than approximated.** Bottari 2020 (O3) covers the same logical ground with an abstract I could read in full.
- **Squires 2008 / Nair & Alam 2008 (Q13).** Both are the right physics for attacking attomolar LOD claims (mass-transport collection limits; screening-limited response). Both paywalled, abstract-only. Squires' abstract does explicitly "highlight unexplained discrepancies between reported values and theoretical limits" — useful as framing, not as a number. I did **not** compute a Squires-style flux bound, because doing so requires the geometry and flow conditions of the Abrantes device, which I could not obtain (§1.4).
- **Berg & Purcell 1977 (*Biophys J*, PMID 911982, PMC1473391).** Europe PMC and NCBI return metadata only (scanned article, 1.8 kB of text). I did **not** build a Berg–Purcell counting-noise argument, because I could not read the source. Recorded as an unexplored direction, not as a finding.

### 1.4 Access blocks (these are blocks, not results)

- **Abrantes 2025 preprint full text is unreachable from this environment.** `biorxiv.org/content/…v1.full` returned a 17-byte body (bot block); `api.biorxiv.org` returned no JSON; Europe PMC holds it as `PPR1115530` with `inEPMC=N`, `hasPDF=N`. I therefore have the abstract only, and the tension I raise in §3.2 is tagged `unresolved`, not asserted as an error.
- **Ding & Liu 2024 kinetic ITC (ledger S003) VoR remains closed.** No OA route found. The ledger's abstract-level entry stands; I added nothing.
- **Physiological activity-evoked extracellular Ca²⁺ dips (Q16).** I could not retrieve, by free routes, a primary quantification of activity-evoked \[Ca²⁺\]ₒ decreases under normal (non-seizure) conditions. The closest hit was pathophysiological (Sawant-Pokam et al., *J Neurophysiol* 2025, PMID 40924686). My wildcard (§6) is therefore explicitly left as `hypothesis` with the missing link named.

---

## 2. New sources this lane verified

`full_text_inspected` is reported honestly: `yes` = I read the article body; `partial` = I read specific sections; `no` = abstract only.

| ID | Citation | DOI | PMID | PMCID | Full text |
| --- | --- | --- | --- | --- | --- |
| O1 | Hershey ND, Popov P, Oliver N, Dugan CE, Kennedy RT. Detection of Neuronal Glutamate in Brain Extracellular Space In Vivo Using Microdialysis and Metabolic Labeling with Glutamine. *ACS Chem Neurosci* 2025 | 10.1021/acschemneuro.5c00518 | 40838767 | PMC12418293 | yes |
| O2 | Sulliger M, Peters M, Sottini A, Stuber A, Yang K, Nakatsuka N, Ortega Arroyo J, Quidant R. Scalable Multiparametric Characterization of Aptamer–Target Interactions. *ACS Nano* 2026 | 10.1021/acsnano.5c19596 | 41504417 | PMC12825375 | yes |
| O3 | Bottari F, Daems E, de Vries AM, Van Wielendaele P, Trashin S, Blust R, Sobott F, Madder A, Martins JC, De Wael K. Do Aptamers Always Bind? … *JACS* 2020 | 10.1021/jacs.0c08691 | 33166132 | — | no |
| O4 | Xie Y, Chen Y, Liu J. Capture-SELEX of DNA Aptamers for Highly Selective Binding of Folate. *ChemBioChem* 2026 | 10.1002/cbic.70393 | 42179008 | PMC13206267 | yes |
| O5 | Leung KK, Gerson J, Emmons N, Heemstra JM, Kippin TE, Plaxco KW. The Use of Xenonucleic Acids Significantly Reduces the In Vivo Drift of Electrochemical Aptamer-Based Sensors. *Angew Chem Int Ed* 2024 | 10.1002/anie.202316678 | 38500260 | PMC11821280 | yes |
| O6 | Jaquins-Gerstl A, Michael AC. Comparison of the brain penetration injury associated with microdialysis and voltammetry. *J Neurosci Methods* 2009 | 10.1016/j.jneumeth.2009.06.023 | 19559724 | PMC2743756 | yes |
| O7 | Kesler V, Murmann B, Soh HT. Going beyond the Debye Length… *ACS Nano* 2020 | 10.1021/acsnano.0c08622 | 33226776 | PMC7761593 | partial |
| O8 | McKeague M, De Girolamo A, Valenzano S, et al. Comprehensive analytical comparison of strategies used for small molecule aptamer evaluation. *Anal Chem* 2015 | 10.1021/acs.analchem.5b02102 | 26192270 | — | no |
| O9 | Hascup KN, Hascup ER, Pomerleau F, Huettl P, Gerhardt GA. Second-by-second measures of L-glutamate in the prefrontal cortex and striatum of freely moving mice. *JPET* 2008 | 10.1124/jpet.107.131698 | 18024788 | PMC3404456 | no |
| O10 | McCluskey K, Boudreault J, St-Pierre P, et al. Unprecedented tunability of riboswitch structure and regulatory function by sub-millimolar variations in physiological Mg²⁺. *Nucleic Acids Res* 2019 | 10.1093/nar/gkz316 | 31045204 | PMC6614840 | partial |
| O11 | Squires TM, Messinger RJ, Manalis SR. Making it stick: convection, reaction and diffusion in surface-based biosensors. *Nat Biotechnol* 2008 | 10.1038/nbt1388 | 18392027 | — | no |
| O12 | Nair PR, Alam MA. Screening-limited response of nanobiosensors. *Nano Lett* 2008 | 10.1021/nl072593i | 18386914 | — | no |
| O13 | Yu H, Alkhamis O, Canoura J, Liu Y, Xiao Y. Advances and Challenges in Small-Molecule DNA Aptamer Isolation, Characterization, and Sensor Development. *Angew Chem Int Ed* 2021 | 10.1002/anie.202008663 | 33559947 | PMC8292151 | partial |

Ledger anchors **re-verified by this lane from the primary abstract**, not inherited: Herman & Jahr 2007 (PMID 17804634 — "baseline concentration is much lower, near 25 nM"); Clements et al. 1992 (PMID 1359647 — "Glutamate peaked at 1.1 millimolar and decayed with a time constant of 1.2 milliseconds"); Wu et al. 2022 (PMID 34783880 — Kd 12 µM for 1d04; glu1 LOD 0.0013 pM; **detection range 0.01 pM–1 nM**); Hu et al. 2025 (PMID 40992279); Abrantes et al. 2025 (bioRxiv 10.1101/2025.11.05.686731 — LOD 1 aM, **linear range 1 aM–10 pM**, 24 mV/decade, aCSF).

---

## 3. The opposing case, by domain

### 3.1 Affinity and molecular recognition — the foundation is one unreplicated number in a target class with a demonstrated false-positive rate

**OC-1.** *Three published small-molecule DNA aptamers with reported nanomolar affinity were shown to bind their target not at all.* Bottari et al. selected three ampicillin aptamers "with a reported affinity in the nanomolar range," reproduced the original AuNP colorimetric assay (getting "conflicting results with respect to the original report"), then tested binding in solution by ITC, native nESI-MS, and ¹H NMR, and concluded that "none of the ampicillin aptamers show any specific binding with their intended target." They validated their own pipeline against two well-characterised aptamers (MN4, 1OLD).
Tag: `primary-source-supported` (from the published abstract; VoR paywalled). Source: O3. Quantity type: `Kd_molecular`. Transferable to glutamate: **no** — this is ampicillin. What it *does* establish is a base rate: a reported nanomolar small-molecule DNA aptamer affinity, reproduced in reviews, can be an artefact of the assay used to measure it.

**OC-2.** *Assay-to-assay disagreement in small-molecule aptamer affinity is documented, not anecdotal.* McKeague et al. ran a head-to-head panel of conventional affinity assays on a suite of ochratoxin A aptamers and report "inconsistency between conventional affinity assays and the need for multiple characterization strategies."
Tag: `primary-source-supported` (abstract only). Source: O8. Transferable: **no** (OTA), but it is the methodological reason OC-1 happens.

**OC-3.** *An independent expert group states, in print, that a glutamate moiety is a poor aptamer epitope — and names the 12 µM number as the evidence.* Xie, Chen and Liu (Juewen Liu lab) selected a folate DNA aptamer by Capture-SELEX and, explaining why only one aptamer family emerged, write: the pteridine ring supports binding, whereas "the other end of the molecule, containing a glutamate moiety, is unlikely to support such nanomolar binding affinity, as a previously reported DNA aptamer for glutamate exhibited a Kd of only ~12 µM, nearly 30-fold weaker than the affinity observed here."
Tag: `primary-source-supported` for the fact that the statement was made and for the folate Kd = 0.64 µM by ITC; the glutamate inference itself is `hypothesis`. Source: O4, §3.3 of that paper. This is the only substantive independent engagement with the glutamate aptamer among all 23 Europe PMC records citing Wu 2022 (Q5).

**OC-4 (methodological contrast, and the sharpest version of OC-1 for our case).** The same folate paper is a worked example of what an adequately validated small-molecule Capture-SELEX aptamer looks like: label-free solution ITC (Kd 0.64 µM); a two-base point mutant (FA1m) that abolishes binding, establishing that a defined sequence element is required; a structurally-related interferent panel (guanine, adenine, theophylline, xanthine, caffeine); and — the honest part — an apparent cross-reactivity to tetrahydrofolate that the authors chased down with ITC and attributed to *in situ* oxidation rather than binding.
None of these four controls exists in the glutamate aptamer literature. There is no solution ITC on 1d04 or glu1, no binding-null mutant control, and no amino-acid interferent panel (Q2). Tag: `unresolved` — this is an absence of controls, not evidence of failure.

### 3.2 Dynamic range — the reported sensors are tuned to a decade that brain glutamate does not occupy

This is the quantitative core of the opposing case. It uses only numbers taken from primary sources, plus 1:1 Langmuir algebra.

Biological anchors (all re-verified, §2):

| Compartment | Value | Source |
| --- | --- | --- |
| Ambient, acute hippocampal slice (tonic NMDAR current) | **25 nM** | Herman & Jahr 2007 |
| Rat cortex ECF, microdialysis with stable-isotope extraction-fraction correction, n = 11 | **9.4 ± 0.6 µM** | O1, §3.1 |
| Awake mouse PFC / striatum, chronic enzyme MEA | **3.3 µM / 5.0 µM** | O9 |
| Inferred peak synaptic cleft | **1.1 mM**, τ = 1.2 ms | Clements 1992 |

Reported sensor affinities / ranges:

| Construct | Reported quantity | Value |
| --- | --- | --- |
| Wu 2022 `glu1` E-AB | `analytical_working_range` | 0.01 pM – **1 nM** |
| Hu 2025 MEA surface Glu-apt | `EC50` (electrochemical apparent Kd, Langmuir–Freundlich) | **1.8 nM** |
| Xiao 2025 glutamate aptamer | `Kd_molecular` by SPR, 0.1× PBS | **293 nM** |
| Wu 2022 `1d04` parent | `Kd_molecular`, solution | **12 µM** |
| Abrantes 2025 (preprint) NG-Apt-Glu | `analytical_working_range` | 1 aM – **10 pM** |

**OC-5.** *Fractional occupancy, θ = C/(K + C), computed for each affinity against each biological anchor.*
Tag: `computational illustration`. Implementation: `/tmp/oc/occupancy.py` (reproduced in §8 so it can be re-run).

| K used | θ at 25 nM | θ at 9.4 µM | θ at 1.1 mM |
| --- | ---: | ---: | ---: |
| Hu 2025 surface 1.8 nM | 0.9328 | 0.99981 | 0.999998 |
| Xiao 2025 SPR 293 nM | 0.0786 | 0.9698 | 0.99973 |
| Wu 2022 solution 12 µM | 0.0021 | 0.4393 | 0.9892 |

Signal available for a **doubling** of glutamate from each baseline, as a fraction of full scale:

| K used | from 25 nM | from 9.4 µM | from 1.1 mM |
| --- | ---: | ---: | ---: |
| Hu 2025 surface 1.8 nM | 3.24 % | **0.0096 %** | 0.0001 % |
| Xiao 2025 SPR 293 nM | 6.72 % | 1.49 % | 0.013 % |
| Wu 2022 solution 12 µM | 0.21 % | **17.1 %** | 0.54 % |

Read the first row: a sensor with the Hu surface apparent Kd sits at 99.98 % occupancy in rat cortical ECF, and doubling the glutamate concentration there moves it by one part in ten thousand of full scale. It is not slow; it is **pinned**. The conclusion survives the unresolved ambient-glutamate controversy: even at Herman & Jahr's much lower 25 nM, that sensor is already 93 % occupied and a doubling yields 3 % of full scale.

**OC-6 (the surprising result).** *The one glutamate affinity in the literature that is well matched to brain extracellular glutamate is the 12 µM parent aptamer the field treats as superseded.* At 9.4 µM, a Kd = 12 µM receptor sits at θ = 0.44 — near the steepest point of its response curve — and a doubling of glutamate yields **17 % of full scale**, the largest value anywhere in the table. Truncation plus surface immobilisation moved the reported apparent affinity roughly 6,700-fold tighter (12 µM → 1.8 nM) and, in doing so, moved the sensor's responsive window *out of* the biological range. Every reported improvement in limit of detection in this literature is, on this analysis, a movement away from usability.
Tag: `computational illustration` built on `primary-source-supported` inputs. **Non-transfer warning:** 12 µM is a solution measurement on 1d04 and 1.8 nM is a surface electrochemical apparent Kd on a different, truncated, Fc- and thiol-modified construct (ledger `C021`, `C026`). I am **not** claiming the truncation caused an affinity shift — that comparison is forbidden. I am claiming something weaker and safe: *as reported*, these two numbers place their respective constructs in non-overlapping concentration decades, and only one of those decades contains brain glutamate.

**OC-7.** *The reported analytical working ranges terminate below the biological range.* Wu 2022's stated range tops out at 1 nM: that is 25× below ambient slice glutamate, 9,400× below O1's cortical ECF value, and 1.1 × 10⁶× below the inferred cleft peak. The Abrantes preprint's stated linear range tops out at 10 pM, i.e. 2,500× / 9.4 × 10⁵× / 1.1 × 10⁸× below the same three anchors — yet the same abstract reports measuring glutamate in human CSF, a matrix conventionally quoted in the low micromolar range.
Tag: `unresolved`. I could not obtain the preprint's full text (§1.4), so I cannot see whether samples were diluted by ~10⁶ or whether a separate calibration was used. This is flagged as a tension requiring full-text inspection, **not** asserted as an error.

### 3.3 Kinetics — the limiting step may be a conformational isomerisation, and for glutamate it has never been measured

**OC-8.** *In a structure-switching neurotransmitter aptamer, most of the signal can come from a slow, concentration-independent step.* Sulliger et al. used droplet single-molecule FRET to resolve serotonin aptamer binding across ms-to-hour timescales for three stem-length variants. All three show a common two-step mechanism: a fast, serotonin-concentration-dependent step (apparent k_on,obs = 5.0 × 10⁶ M⁻¹ s⁻¹ for L5, 9.8 × 10⁶ M⁻¹ s⁻¹ for L4) completing in < 1 s, followed by "a slower structural rearrangement of the complex (over approximately 60 min)" that is **independent of serotonin concentration** for all three aptamers. For the long-stem L5, only "roughly 25 % of the total decay" occurs within the first 600 ms; for L4 it is ~65 %. The authors conclude that L4 gives a readout "in under 1 s, representing an ~1000-fold reduction in assay time compared to the longer stem aptamer, which requires over 20 min."
Tag: `primary-source-supported`. Source: O2, Figure 4 and associated text. Quantity types: `kon`, `response_time`. Construct: serotonin DNA aptamer, stem variants L3/L4/L5, solution FRET, PBS. Transferable to glutamate: **no**.

Why this is the strongest kinetic opposing argument available, and why it is more interesting than "aptamers are slow":
1. The conventional worry is that koff or kon[L] limits sensor speed. This experiment shows a third possibility — the **reporting conformational change** can be the slow step, and because it is concentration-independent it cannot be outrun by raising analyte concentration.
2. The effect is set by a trivial construct parameter (stem length) and spans ~1000× in assay time. Wu 2022 truncated 1d04 into glu1 precisely to create structure-switching behaviour. **Nobody has measured where glu1 or Hu's Glu-apt land on that 1000-fold spectrum.**
3. It supplies a mechanism, not previously in our ledger, for the observed glutamate measurement clocks — Hu's 15 min incubation (`C006`) and the ~10 min plateau of the intraretinal probe (`C028`). That mechanistic link is `hypothesis`, not measured for glutamate.

**OC-9.** *Matrix slows the association step.* For aptamer L4, moving from PBS to human serum halved the concentration-dependent apparent association rate (9.8 × 10⁶ → 5.9 × 10⁶ M⁻¹ s⁻¹) and roughly doubled K_D (60 ± 15 nM → 137 ± 25 nM); the authors attribute this to non-specific species interfering with association rather than with complex stability.
Tag: `primary-source-supported`. Source: O2. Transferable: **no** (serotonin, serum, solution) — but it is a measured, not assumed, matrix penalty on `kon`, which is the quantity a fast glutamate sensor would most need protected.

**Honest counterweight (this cuts against my own lane).** OC-8 does *not* show aptamers are intrinsically slow. 5–10 × 10⁶ M⁻¹ s⁻¹ is a respectable association rate, and the fast step completes in under a second. The defensible opposing statement is narrower and stronger: *the slow step is construct-dependent and engineerable, and for glutamate it has been neither engineered nor measured.*

### 3.4 Transduction — drift, screening, and the attomolar problem

**OC-10.** *A DNA-aptamer electrochemical sensor lost 48 % of signal in 5 h in a live rat; the nuclease-resistant analogue lost 7 %.* Leung et al. placed a DNA-aptamer E-AB sensor and its 2′-O-methyl-RNA equivalent in the left and right jugular veins of the same anaesthetised rat. "While the signal of the DNA-employing device fell by 48 % after 5 h under these conditions, the signal of the equivalent OMe RNA device fell by just 7 %." Frequency-resolved charge-transfer analysis showed the DNA device's in vivo behaviour matches its behaviour in DNase-containing buffer (loss of reporters at constant transfer rate), whereas the OMe RNA device's matches fouling-dominated in vitro blood behaviour. The authors note drift is *correctable* for accuracy by kinetic differential measurement, but that the signal loss irreducibly degrades signal-to-noise (their example: signal SD rising from 0.008 to 0.020 over 4 h in vivo).
Tag: `primary-source-supported`. Source: O5, Figure 3B and §Conclusions. Quantity type: `signal_gain` (loss). Construct: tobramycin-binding DNA vs 2′-OMe-RNA aptamer, rat jugular vein. Transferable to a brain glutamate DNA aptamer: **no** — different target, different construct, blood not brain ECF. The *mechanism* (DNase attack on a DNA aptamer in living tissue) is generic to DNA, but the rate in brain parenchyma is unmeasured.

**OC-11.** *Charge screening is a first-principles constraint on the FET route, and the glutamate FET papers operate around it rather than through it.* Kesler, Murmann and Soh: "The Debye length under physiological conditions is less than 1 nm; in contrast, the length of an antibody is on the order of 10–15 nm, and a 30-base aptamer is up to ~10 nm. This intrinsic mismatch in dimensions … poses a fundamental challenge." Note their overall position is *optimistic* — they argue Poisson–Boltzmann has "merely reached the limits of [its] utility" and propose Debye-volume and non-equilibrium strategies.
Tag: `review-supported` (perspective article). Source: O7. Relevance: ledger `C014` records that the Xiao 2025 glutamate FET calibration was performed in **0.1× PBS**, i.e. at reduced ionic strength, which lengthens the Debye length. That is a legitimate characterisation condition and an illegitimate basis for inferring brain-ECF performance.

**OC-12.** *The attomolar claim has a known theoretical failure mode I could not close.* Squires, Messinger and Manalis derive collection-rate limits for micro- and nanoscale sensors and "highlight unexplained discrepancies between reported values and theoretical limits"; Nair and Alam show that electrostatic screening limits nanobiosensor response logarithmically in target concentration and in salt concentration.
Tag: `review-supported` / `primary-source-supported` respectively, **abstract-only**. Sources: O11, O12. I deliberately did **not** compute a transport bound for the Abrantes device, because its geometry and sample handling are behind the access block in §1.4. Recorded as the highest-value open check, not as a refutation.

### 3.5 Immobilisation and the probe–tissue interface

**OC-13.** *A probe of the wrong size does not measure the tissue it displaced.* Jaquins-Gerstl and Michael implanted 280 µm o.d. microdialysis probes and 7 µm carbon fibres in rat striatum for 1, 4 and 24 h. Microdialysis tracks showed PECAM-positive vessels devoid of perfused nanobeads (ischaemia) at all three time points, a PECAM-immunoreactive debris halo, and by 24 h hyperplastic/hypertrophic glia encircling ~75 % of the track circumference. Carbon fibres produced none of these. The authors summarise their prior voltammetry-near-probe work: at 1 mm from a dialysis probe, evoked dopamine release looks normal; at ~200 µm it is **decreased by 90 %**; in contact with the probe it is **abolished**. Carbon-fibre penetration injury is confined to ~3 µm by EM.
Tag: `primary-source-supported`. Source: O6, §Results and §Discussion. Construct: not an aptamer; analyte is dopamine. Transferable to glutamate: **no** — but the geometric argument is analyte-independent, and it is directly aimed at the formats this project's glutamate aptasensors actually use. Hu's gold-nanostructured microelectrode arrays and Parylene-C intraretinal probes are in the hundreds-of-microns class, i.e. the microdialysis class, not the carbon-fibre class.

**OC-14 (ledger-inherited; re-stated because it belongs in the opposing case, and flagged as not re-verified by this lane).** Surface immobilisation is not a null operation. `state/sources.csv` S038 (MacDonald et al. 2019, *J Phys Chem C*, DOI 10.1021/acs.jpcc.9b00845) records an L-tyrosinamide aptamer with solution Kd 1–3 µM behaving as ~100 µM on a crowded surface; ledger claim `C018` (White et al. 2008, S033) records packing density and SAM chemistry changing E-AB gain and apparent Kd. **This lane did not retrieve either source**; these are inherited records and should not be treated as independently confirmed here. What they bound is how much of the Wu solution measurement can survive onto the Hu surface construct: the honest answer is *unknown*, and both of the possible answers (§4) are bad for the sensor.

### 3.6 Biological context — the decisive limiter

**OC-15.** *Glutamine stands at ~19× the glutamate concentration in the same tissue, measured in the same animals with the same probe.* Hershey et al., infusing stable-isotope-labelled standards through a rat cortical microdialysis probe and correcting for extraction fraction, report extracellular **Gln = 179 ± 20 µM** and **Glu = 9.4 ± 0.6 µM** (n = 11).
Tag: `primary-source-supported`. Source: O1, §3.1. Quantity type: `biological_concentration_range`. Construct: not an aptamer.
This sets a hard, quantitative selectivity bar that the glutamate aptamer literature has never been tested against: glutamine is glutamate's γ-amide, differing by one substitution, and it is present at roughly nineteen times the concentration. Q2 establishes that no peer-reviewed glutamate-aptamer study reports a glutamine cross-reactivity measurement; `C032` records that the Hu thesis panel compares 100 nM glutamate against 10 µM serotonin, dopamine, tyrosine and lactate — chemically unrelated compounds — with glutamine and aspartate absent. A 1 % cross-reactivity to glutamine would contribute ~1.8 µM glutamate-equivalent signal, roughly 19 % of the true glutamate concentration.

**OC-16 — the strongest single result in this lane.** *Total extracellular glutamate is the wrong observable: a genuine, TTX-sensitive, stimulus-evoked neuronal glutamate release event produced no change in it.* In the same study, Hershey et al. infused 2.5 µM ¹³C₅-glutamine through the probe so that neurons near the probe would convert it to ¹³C₅-glutamate via the glutamate–glutamine shuttle, letting neuronal and non-neuronal glutamate be measured separately in the same dialysate. They recovered 144 ± 35 nM ¹³C₅-Glu (n = 11). That labelled pool behaved like a neurotransmitter and the unlabelled bulk pool did not:

| Manipulation | ¹³C₅-Glu (neuronal-enriched) | endogenous ¹²C-Glu (total) |
| --- | --- | --- |
| TTX 2 µM | **−62 ± 7 %** (p ≤ 0.001, n = 3) | unchanged |
| ACPD (mGluR agonist) | **−59 ± 9 %** (p ≤ 0.001, n = 4); blocked by MCPG | unchanged |
| Riluzole 500 µM (Gln transport) | −58 ± 3 % (n = 8) | −33 ± 4 % |
| MeAIB 20 mM (SNAT1/2) | −33 ± 8 % (n = 11) | unchanged |
| Tail pinch (stressor) | **+155 ± 14 %** (p ≤ 0.05, n = 4); abolished by TTX | **unchanged** |
| 75 mM K⁺ | no increase | **+160 ± 20 %** |
| PDC (uptake block) | +173 ± 8 % | +342 ± 76 % |

The authors' own conclusion: "the basal endogenous ¹²C-Glu must have a primarily non-neuronal source … it is a small fraction of what is detected," and, for the stressor, "in the motor cortex, the neuronal response is much more muted and **would not be detectable by recording only endogenous Glu**."
Tag: `primary-source-supported`. Source: O1, §3.4, §3.6, §4.1, §4.3. Construct: not an aptamer; rat motor cortex, microdialysis + LC-MS/MS. Transferable: **no** for the specific percentages; the structural point — that total \[Glu\]ₑₓ and neuronal Glu release are differently regulated pools — is what carries.

Why this outranks every kinetic argument: an aptamer sensor, of any speed, any LOD and any architecture, reports **total free glutamate**. Here is a real experiment in which a real, action-potential-dependent, physiologically evoked glutamate release event occurred and total free glutamate did not move — while, separately, a manipulation that raised total glutamate by 160 % (high K⁺) evoked **no** neuronal component at all. Both error directions are demonstrated in the same animals: false negatives for real neuronal signals, and false positives from astrocytic release. Making the sensor faster makes it faster at measuring the wrong quantity.

**OC-17 — method-dependent context, stated because the opposing case must not overreach.** The claim "basal extracellular glutamate is not neuronal" is method-dependent. O1 reports endogenous glutamate unchanged by TTX; O9 reports that in awake freely moving mice a chronically implanted enzyme MEA measures tonic Glu of 3.3 µM (PFC) and 5.0 µM (striatum), and that TTX **decreased** resting glutamate by 20 % (p < 0.05). O1's own introduction addresses this directly, attributing the discrepancy to "the ability of these different size probes to access different spatial concentration domains," while also noting "methodological issues with sensor electrodes, such as effects of enzyme immobilization on selectivity."
Tag: `primary-source-supported` for both measurements, `unresolved` for the reconciliation. This is a genuine disagreement between a large sampling probe and a small enzyme electrode, and it is the same axis as OC-13. It weakens the absolute form of OC-16 ("no neuronal glutamate escapes") but not the operational form ("total \[Glu\]ₑₓ can move independently of neuronal release, in both directions").

---

## 4. The dilemma this lane wants on the record

Take the two reported glutamate affinities at face value and ask which applies to a deployed surface sensor. Both branches fail, for different reasons:

- **If the surface construct really has apparent Kd ≈ 1.8 nM** (Hu's own electrochemical measurement, `C005`), then in brain extracellular fluid it is 93–99.98 % occupied depending on which ambient value is right, and it has essentially no output swing left (OC-5). It would be a fast, exquisitely sensitive sensor that is saturated everywhere it matters.
- **If the recognition chemistry is really the 12 µM solution binding** of the parent aptamer, then the reported picomolar and attomolar limits of detection cannot arise from equilibrium 1:1 occupancy of that site, and the burden shifts to identifying what the low-concentration signal actually is — which is precisely the situation Bottari et al. dissected for ampicillin (OC-1).

I cannot resolve this branch, and the constitution forbids me from transferring properties between the solution parent and the surface truncate to close it. Recording it as a dilemma is the honest output. It is also the most efficient experimental target in the whole project (§7).

---

## 5. Inference boundary

**What was measured** (by others, in the cited sources): Gln 179 ± 20 µM and Glu 9.4 ± 0.6 µM in rat cortical ECF; 144 ± 35 nM neuronally-derived ¹³C₅-Glu; TTX −62 %, ACPD −59 %, tail-pinch +155 % on the labelled pool with endogenous glutamate unchanged; serotonin aptamer k_on,obs 5.0–9.8 × 10⁶ M⁻¹ s⁻¹ with a ~60 min concentration-independent second step; 48 % vs 7 % 5 h in vivo E-AB signal loss for DNA vs 2′-OMe-RNA; 90 % suppression of evoked dopamine release 200 µm from a 280 µm probe; Kd 0.64 µM by ITC for a folate aptamer with a binding-null mutant control; no specific binding for three published ampicillin aptamers; ambient hippocampal glutamate ~25 nM; cleft peak 1.1 mM, τ 1.2 ms.

**What was inferred** (by me): the occupancy and marginal-sensitivity tables in OC-5 and OC-6 (algebra on a 1:1 Langmuir site applied to published K values and published concentrations — no new measurement); the claim that a glutamate aptasensor's working range fails to overlap the biological range (arithmetic on published ranges); the suggestion that a slow concentration-independent conformational step could explain Hu's minutes-scale clocks (`hypothesis`, untested for glutamate); the proposition that ionic confounds could masquerade as glutamate signals (§6, `hypothesis`).

**What remains unknown**: every kinetic constant for every glutamate aptamer; the cross-reactivity of any glutamate aptamer to glutamine or aspartate; the solution affinity of the truncated surface construct by any orthogonal method; whether Abrantes' attomolar range is reconcilable with micromolar CSF glutamate; the drift rate of a DNA aptamer sensor in brain parenchyma as opposed to blood; whether ambient extracellular glutamate is nanomolar or micromolar.

---

## 6. Wildcard — an ionic confound nobody in this project has checked

Direction investigated: *could a nucleic-acid glutamate sensor in brain tissue report ionic transients as glutamate transients?*

Rationale: a DNA aptamer's fold, and therefore its ligand response, depends on divalent cations, and brain extracellular Ca²⁺ and Mg²⁺ are in the sub-millimolar-to-millimolar range where that dependence is steepest.

**OC-18.** McCluskey et al. quantified intracellular Mg²⁺ in *B. subtilis* (0.8–3.7 mM across growth) and used single-molecule FRET on the lysine-sensing lysC riboswitch aptamer domain — a natural, folded nucleic-acid receptor for a **free amino acid**, the closest structural analogue available to a glutamate aptamer. Raising Mg²⁺ from 1 to 2 mM halved the lysine concentration needed for 50 % transcription termination (T50 129 ± 15 µM → 61 ± 7 µM); the Mg²⁺ binding isotherm gave K_D 1.8 ± 0.3 mM with Hill coefficient 2.6 ± 0.4; and overall, sub-millimolar Mg²⁺ variation "change\[s\] the ligand-binding affinity by two orders of magnitude."
Tag: `primary-source-supported` for the riboswitch. Source: O10. Transferable to a DNA glutamate aptamer in brain ECF: **no**.

**Status of the wildcard: not established.** The chain needs a second link — a primary quantification of activity-evoked extracellular Ca²⁺/Mg²⁺ changes under physiological (not seizure) conditions — and Q16 did not find one through free routes; the closest hit was pathophysiological (PMID 40924686). I am recording the direction, the one solid link, and the missing link, rather than manufacturing the conclusion. If the second link exists, this becomes a cheap and high-value control experiment (a no-glutamate ionic-swing challenge on a finished sensor); if it does not, the direction should be closed. Tag for the overall proposition: `hypothesis`.

---

## 7. Required outputs

### 7.1 Single strongest counterexample or limiter

**Hershey, Popov, Oliver, Dugan & Kennedy 2025 (O1): a tail pinch evoked a real, TTX-abolished, 155 % increase in neuronally-derived glutamate in rat motor cortex while total endogenous extracellular glutamate did not change — and, in the same animals, 75 mM K⁺ raised total glutamate by 160 % while producing no neuronal component at all.**

This is the strongest limiter because it is the only result I found that is indifferent to every parameter the project is trying to optimise. It does not care about the aptamer's Kd, its kon, the electrode chemistry, the probe geometry, the interrogation waveform, or the limit of detection. A glutamate aptamer biosensor measures total free glutamate; this experiment demonstrates, with both error directions in the same preparation, that total free glutamate can fail to report genuine neuronal release and can report large changes that contain none. The project's framing question — "can an aptamer keep up with neurochemical signalling?" — presupposes that keeping up with \[Glu\]ₑₓ is the same thing as keeping up with glutamatergic signalling. O1 is a direct experimental attack on that presupposition.

It beats the runner-up (the dynamic-range collapse of OC-5/OC-6, where a 1.8 nM apparent Kd leaves 0.0096 % of full scale for a doubling of cortical glutamate) because dynamic-range mismatch is a *fixable engineering error* — re-select or detune the aptamer and it goes away — whereas the observable mismatch is a property of the analyte, not of the instrument.

It is weakened, honestly, by OC-17: the enzyme-MEA literature (O9) does see a 20 % TTX-sensitive component of tonic glutamate in awake mice, and the discrepancy plausibly turns on probe size and spatial sampling domain (the same axis as OC-13). The operational form of the claim survives that objection; the absolute form does not.

### 7.2 Falsifier

The opposing case above would be materially weakened by this single result:

> A glutamate aptamer sensor with an independently validated solution affinity in the **1–100 µM** range (ITC or another label-free solution method, with a binding-null mutant control), immobilised on a carbon-fibre-class probe (≤ 10 µm), showing in living brain tissue (a) a graded, monotonic response across 1–50 µM glutamate, (b) < 5 % cross-response to 200 µM glutamine and to aspartate at its ECF concentration, and (c) a response to local electrical or optogenetic stimulation that is abolished by TTX and by a glutamate uptake blocker in the pharmacologically expected directions.

Each clause targets one pillar: (a) falsifies OC-5/OC-6 (dynamic-range mismatch); (b) falsifies OC-15 (glutamine interference); (c) falsifies OC-16 (wrong observable) by demonstrating that the sensor's signal tracks the neuronal pool and not the astrocytic background. Sub-second resolution is deliberately **not** in the falsifier. From this lane's viewpoint, a slow sensor measuring the right quantity at the right concentration would displace the opposing case; a fast sensor failing (a)–(c) would not.

A cheaper partial falsifier for OC-1/OC-3/OC-4: solution ITC on 1d04 and on glu1 under the published selection buffer, with a two-base binding-null mutant, reproducing Kd = 12 µM in an independent laboratory.

### 7.3 Highest-information next experiment from this lane's view

**Run the Xie/Chen/Liu folate validation protocol (O4) on the glutamate aptamer, with an amino-acid interferent panel — in a single laboratory, on both constructs, in solution.**

Concretely: solution ITC on 1d04 and on truncated glu1 in the published selection buffer and in an ECF-mimicking buffer; a two-base point mutant in the conserved region of each, to show that binding is sequence-specific and can be abolished; and a titration panel of **L-glutamine at 179 µM, L-aspartate, and L-glutamate**, reported as heats, not as sensor responses.

Why this and not something more ambitious:

1. **It is the only experiment that can resolve §4's dilemma.** A measured solution Kd for the *truncated* construct either lands near 12 µM — in which case the pM/aM limits of detection require a non-equilibrium explanation, and the sensor's biological window is µM after all (the OC-6 surprise becomes the project's central result) — or it lands in the nM decade, in which case the surface sensor is confirmed as saturated in brain and the recognition element must be deliberately *weakened* to be useful. Both outcomes redirect the project.
2. **It is the cheapest test of the highest-probability failure mode.** OC-1 shows that three published nanomolar small-molecule aptamers bound nothing when checked this way, and OC-3 shows an independent expert group already doubts on chemical grounds that a glutamate moiety supports tight binding. Our entire molecular-recognition base is one unreplicated number (Q3, Q5).
3. **It closes the selectivity gap that no one has touched.** Q2 establishes the absence; OC-15 supplies the concentration that makes it matter. Glutamine at 19× glutamate is a bigger threat than any of the interferents actually tested to date.
4. **It requires no animals, no fabrication, and no in vivo access,** and it is the precondition for interpreting any subsequent kinetic or in vivo measurement. Measuring kon for a receptor whose binding has not been independently confirmed would be measuring the rate of an unverified event.

The second-highest-information action is not an experiment but a retrieval: obtain the Abrantes et al. full text (interlibrary or author request) and check the CSF measurement against the stated 1 aM–10 pM linear range (OC-7). That is a one-hour task that could remove or promote a whole source.

---

## 8. Reproducibility

Occupancy arithmetic (OC-5, OC-6) — pure algebra, no fitted parameters, no data files:

```python
def theta(c, kd):      # 1:1 Langmuir fractional occupancy
    return c / (kd + c)

KD   = {"Hu 2025 surface apparent": 1.8e-9,
        "Xiao 2025 SPR (0.1x PBS)": 293e-9,
        "Wu 2022 1d04 solution":    12e-6}
CONC = {"Herman & Jahr 2007 ambient":  25e-9,
        "Hershey 2025 rat cortex ECF": 9.4e-6,
        "Clements 1992 cleft peak":    1.1e-3}

for kn, kd in KD.items():
    for cn, c in CONC.items():
        print(kn, cn, theta(c, kd), theta(2*c, kd) - theta(c, kd))
```

Every K and every C above is a published value with the source given in §2–§3; the script introduces no new numbers. The 81-fold 10 %–90 % Langmuir window used implicitly here is already implemented and tested in `analysis/accepted/occupancy_kinetics` (ledger `C027`).

Retrieval commands used for full texts (both free, both reproducible):

```bash
curl "https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML"
curl "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=<numeric>&retmode=xml"
```

The second route is required for NIH author manuscripts (O1, O2, O5, O6, O13), which return HTTP 404 from the Europe PMC `fullTextXML` endpoint.

---

## 9. Claims proposed to the orchestrator

The orchestrator owns `state/claims.csv`; this lane writes no ledger rows. Proposed entries, with the non-transfer flags that must travel with them:

| # | Claim | Tag | Source | Quantity | Value | Construct / system | Transferable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P1 | Rat cortical ECF glutamine is 179 ± 20 µM against glutamate 9.4 ± 0.6 µM (n = 11), same probe, same animals | primary-source-supported | O1 §3.1 | biological_concentration_range | 179 / 9.4 | µM; rat cortex microdialysis, Ed-corrected | no |
| P2 | Tail pinch raised neuronally-derived ¹³C₅-Glu by 155 ± 14 % (TTX-abolished) while endogenous ¹²C-Glu was unchanged | primary-source-supported | O1 §3.6 | biological_concentration_range | +155 | %; rat motor cortex | no |
| P3 | 75 mM K⁺ raised endogenous ¹²C-Glu 160 ± 20 % with no ¹³C₅-Glu increase | primary-source-supported | O1 §3.6 | biological_concentration_range | +160 | %; rat motor cortex | no |
| P4 | A serotonin DNA aptamer binds in two steps: fast concentration-dependent (k_on,obs 5.0–9.8 × 10⁶ M⁻¹ s⁻¹, < 1 s) then a ~60 min concentration-independent rearrangement | primary-source-supported | O2 Fig. 4 | kon / response_time | 5.0e6–9.8e6 / ~60 | M⁻¹ s⁻¹ / min; solution FRET, PBS | no |
| P5 | Stem length alone spans ~1000× in assay time for the same serotonin aptamer family (< 1 s vs > 20 min) | primary-source-supported | O2 | measurement_time | ~1000 | fold; solution FRET | no |
| P6 | Human serum halved k_on,obs (9.8e6 → 5.9e6 M⁻¹ s⁻¹) and doubled K_D (60 → 137 nM) for serotonin aptamer L4 | primary-source-supported | O2 | kon / Kd_molecular | see value | M⁻¹ s⁻¹ / nM | no |
| P7 | Three published nanomolar-affinity ampicillin DNA aptamers showed no specific target binding by ITC, native nESI-MS and ¹H NMR | primary-source-supported | O3 (abstract) | Kd_molecular | — | ampicillin aptamers, solution | no |
| P8 | An independent group (Liu lab) states the glutamate moiety is unlikely to support nanomolar aptamer affinity, citing the reported ~12 µM glutamate DNA aptamer as ~30× weaker than their folate aptamer (ITC K_d 0.64 µM) | primary-source-supported (statement + folate K_d); hypothesis (glutamate inference) | O4 §3.3 | Kd_molecular | 0.64 | µM; folate DNA aptamer, solution ITC | no |
| P9 | A DNA-aptamer E-AB sensor lost 48 % of signal in 5 h in a live rat jugular; the 2′-OMe-RNA equivalent lost 7 % | primary-source-supported | O5 Fig. 3B | signal_gain | 48 vs 7 | %; tobramycin aptamer, rat jugular | no |
| P10 | Evoked dopamine release is suppressed 90 % at ~200 µm from a 280 µm microdialysis probe and abolished at contact; carbon-fibre injury is confined to ~3 µm | primary-source-supported | O6 §Discussion | — | 90 | %; rat striatum | no |
| P11 | Reported glutamate aptasensor affinities place their 10–90 % response windows at 0.2–16 nM (Hu) and 33 nM–2.6 µM (Xiao); only the 12 µM solution value overlaps the reported ECF range | computational illustration | OC-5/OC-6 on O1 + ledger C005/C014/C001 | analytical_working_range | see §3.2 | derived Langmuir identity | yes (algebra only) |
| P12 | Wu 2022's stated analytical working range (0.01 pM–1 nM) terminates 25× below ambient slice glutamate and ~9,400× below measured rat cortical ECF glutamate | primary-source-supported inputs; computational illustration for the ratios | S001 abstract + O1 | analytical_working_range | 25 / 9400 | fold | no |
| P13 | Abrantes 2025 preprint states a 1 aM–10 pM linear range while reporting CSF glutamate measurements; full text unreachable, reconciliation unknown | unresolved | S010 abstract | analytical_working_range | 1e-18–1e-11 | M; aCSF, graphene FET | no |
| P14 | Sub-millimolar Mg²⁺ variation retunes a lysine-sensing riboswitch aptamer's ligand affinity by two orders of magnitude (T50 129 → 61 µM from 1 → 2 mM Mg²⁺) | primary-source-supported | O10 | EC50 | 129 → 61 | µM; lysC aptamer, smFRET | no |
| P15 | No glutamate-aptamer kon/koff, no independent 1d04 replication, and no glutamate-aptamer glutamine/aspartate selectivity measurement exist in Europe PMC as of 2026-09-11 (queries Q1–Q5 recorded) | unresolved | Q1–Q5, §1.2 | — | — | negative-search record | n/a |

---

## 10. Answers to the Research Effort Standard items applicable to this lane

- **Best opposing case:** §3, culminating in OC-16.
- **Best supporting case within the opposing lane** (deliberate self-attack): OC-8's fast step is genuinely fast (5–10 × 10⁶ M⁻¹ s⁻¹) and stem engineering achieved a sub-second readout, so "aptamers are inherently too slow" is false; Kesler et al. (O7) argue the Debye limit is not a dead end; O9 does detect a TTX-sensitive tonic glutamate component with a small enzyme electrode; and Xiao 2025's 293 nM SPR affinity is far better matched to brain glutamate than Hu's 1.8 nM apparent value.
- **Context for conflicting studies:** OC-17 (probe size and spatial sampling domain, plus enzyme-immobilisation selectivity, as the candidate explanation for the microdialysis/enzyme-electrode disagreement about whether basal glutamate is neuronal); §3.2 (solution vs surface, and diluted vs physiological ionic strength, as the reason reported affinities cannot be pooled).
- **Inference boundary:** §5.
- **Falsifier:** §7.2.
- **High-information next step:** §7.3.
- **Wildcard:** §6, including its unresolved status and the missing link.
- **Negative-search integrity:** §1.2–§1.4, with queries, hit counts, near-misses and access blocks recorded.
- **Not optimising for agreement:** OC-6 contradicts the direction of travel of the entire glutamate aptasensor literature (lower LOD = better) and is reported even though it also undercuts the simpler pessimistic story that the aptamer is too weak.
