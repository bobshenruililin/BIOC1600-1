# Mission 1 evidence map

Mapper: independent inventory of what this checkout actually contains. Not a new extraction. Not a story recommendation. No source promoted to `core` in this file.

Checkout: branch `cursor/mission1-map-9264` from `main` at `9819f0a`. Ledgers read as files; identifiers and numbers below are copied from those files only. Empty fields in the ledgers stay empty here.

---

## 0. Scope

**In scope.** Mission 1 artifacts plus the ledgers and reviews those artifacts treat as evidence: `reports/`, `state/`, `rounds/` (including `rounds/mission1/`), `poster/`, `AGENTS.md`, `research/evidence/`, `research/reviews/`, and the accepted occupancy/atlas tables those reviews cite.

**Out of scope.** New literature search; re-inspection of OA PDFs; promotion of sources; scoring a winner; a polished poster; editing hash-locked files.

**Method.** For each load-bearing claim in `state/claims.csv`, record: evidential tag, source locator, quantity type, construct, conditions, `transferable`, and `full_text_inspected` as stored on the linked source/evidence row. Split **measured / inferred / unknown**. Numbers that appear in Mission 1 *narrative* but not in `claims.csv` or `core_evidence.csv` are listed as **not ledger-promoted** and are not treated as claims.

**Stale-file warning (inventory, not a science result).** Several round logs describe an earlier tree:

| File | What it still says | What the live ledgers say |
| --- | --- | --- |
| `rounds/01/scout_merge.md` | 65 sources, all `candidate`; no core | 66 sources; 17 `core` |
| `rounds/02/round2.md` | 16 core; 41 evidence rows; 26 claims | 17 core (S066 added later); 46 evidence rows; 32 claims |
| `poster/theses.md` / `state/scoreboard.json` | overnight T1 winner, T5 runner-up | Mission 1 gate recommends **revised D**, status **REVISE**; T1–T5 not this mission’s result |
| `reports/nightly_summary.md` §12 | canonical SHA `984af62…` | this checkout HEAD is `9819f0a` (later merge of swarm-scheduling) |

---

## 1. Repository inventory

### 1.1 `AGENTS.md`

Founding operating manual. Provisional question (to be tested, not assumed): whether an aptamer can keep up with neurochemical signaling, and what affinity, selectivity, kinetics, transduction, immobilization, and biological context jointly determine about a glutamate aptamer biosensor. Desired handoff is `reports/nightly_summary.md`, not a finished poster. Round 0–1: promote nothing to `core`. Poster freeze: no polished artwork. Mission 1 appears in the scheduling section as the observed async-cap failure (launch >~10 agents), not as a science result.

### 1.2 `reports/`

| File | What it is |
| --- | --- |
| `reports/nightly_summary.md` | 13-section overnight handoff. Still headlines **T1** as best current thesis (provisional, contested). Lists S066 retina as strongest Glu-apt neural-tissue experiment. Flagship analysis: occupancy + atlas. Canonical SHA in §12 does not match this HEAD. |
| `reports/mission1_story_tournament.md` | Mission 1 tournament. Gate **REVISE**. Recommended title: **revised D** (two-regime matching; occupancy-at-basal withdrawn as a finding). Runner-up C as a panel. Blind Opus scores A 68 / B 73 / C 77 / D 85. Adversarial Grok: as submitted, D not materially stronger than C. |

### 1.3 `state/`

| File | Content |
| --- | --- |
| `claims.csv` | 32 claims (C001–C032) |
| `sources.csv` | 66 sources; status `core` 17, `relevant` 25, `candidate` 23, `rejected` 1 (S013 peptide aptamer) |
| `gates/science_story.json` | `status: REVISE`, `group_final: false`, `recommended_thesis_id: D_revised`, `runner_up_id: C` |
| `scoreboard.json` | Overnight T1/T5; Round 2 notes 17 core / 46 evidence / 32 claims; analyses P2 atlas 76 and P1 occupancy 68 accepted |
| `decisions.md` | No group-final thesis. Last human-required line: Mission 1 gate REVISE (2026-09-11) |
| `open_questions.md` | Glu kon/koff; in vivo Glu aptamer; Wu VoR; 1.8 nM as occupancy Kd (**no** as 1:1 tissue occupancy of the PaC probe); Asp/Gln; Probe 3; PaC-probe apparent Kd empty; GCL vs photoreceptor narrative; diffusion kon on a poster; which scoring stack |
| `remaining_blockers.md` | Wu VoR; no Glu kon/koff; thesis not group-final; Ohsawa/MacDonald/Lam ±6 not re-verified; Abrantes ELONA unentered (`10.3`/`25.1` are funder IDs); InstructNA not trained; Park GDH; no in vivo Glu aptamer; course cannot run wet IPA |
| `model_config.json` | Parent `cursor-grok-4.6-xhigh`. Do not invent grok-4.7 |
| `LOCKED_FILES.sha256` | constitution, rubric, safety — not edited here |

**Core sources already in the ledger (this map does not add any):** S001, S002, S003, S004, S006, S007, S021, S023, S030, S033, S046, S049, S050, S054, S055, S062, S066.

**Core sources with no row in `core_evidence.csv`:** S023 (Park mislabel), S030 (Rousseau 81-fold; also C013/C027), S046 (docking; C017). Claims exist; extraction rows do not.

### 1.4 `rounds/`

| Path | Role |
| --- | --- |
| `00/bootstrap.md` | Structure only; no claims; no core |
| `01/scout_merge.md` | Six scouts; **stale** “all candidate” census |
| `02/round2.md` | Double extraction + audit; **stale** 16-core / 26-claim census |
| `03/` | Overnight T1–T5 tournament + two scoring stacks that invert |
| `04/tournament.md` | Analysis scores; P2 76 implemented; P1 68 implemented because it can contradict T5 |
| `05/replication.md` | Clean rebuild passed; BOUND/SIMULATION captions present |
| `consolidation.md` | Branch/PR hygiene (overnight) |
| `meta/` | Failure taxonomy; framing-challenger patch |
| `mission1/protocol.md` | 18 lanes complete (A1–D3, H1–H3, O1–O2, W1) |
| `mission1/candidates/{A,B,C,D}.md` | Isolated story dossiers |
| `mission1/candidates/evidence_packet.md` | Allowed reading list for blind review |
| `mission1/sealed/` | Lane notes (programs, Hu, ontology, W1) |
| `mission1/synthesis/` | `d_revised.md` (gate still REVISE); Opus red-team |
| `mission1/hu/orchestrator_backup.md` | Extra Hu-retina reconstruction notes |

### 1.5 `poster/`

`poster/theses.md`: overnight **T1** as winner (mean 87), **T5** runner-up. Explicitly not group-final; Stack B inverts. Storyboard `poster/storyboards/winner.md` is a T1 six-panel outline that still uses occupancy inversion as the computational panel. **This is not the Mission 1 recommended title.** No polished poster files.

### 1.6 Evidence tables Mission 1 treated as canonical

- `research/evidence/core_evidence.csv` — 46 rows (E001–E046)
- `research/evidence/poster_numbers.md` — poster-worthy numbers with verification route
- `research/evidence/quantity_ontology.md` — objects the ten-type schema still collapses
- `analysis/accepted/occupancy_kinetics/tables/occupancy_table.csv` — all rows labeled `SIMULATION/BOUND`
- Reviews: `citation_audit.md`, `contradictions.md`, `aptamer_biochemist.md`, `sensor_engineer.md`, `tanner_objections.md`, `premium/opus_story_gate.md`

---

## 2. Quantity vocabulary (as the repo uses it)

Closed types in `scripts/validate_ledgers.py` / `quantity_ontology.md`:

`Kd_molecular`, `kon`, `koff`, `EC50`, `sensor_LOD`, `analytical_working_range`, `signal_gain`, `response_time`, `measurement_time`, `biological_concentration_range`.

**Collapses the ledgers themselves flag:**

| Stored type | Object that is actually meant | Example |
| --- | --- | --- |
| `Kd_molecular` | measured 1:1 oligo–ligand Kd | C001 1d04 12 µM (abstract) |
| `Kd_molecular` | **citation**, not a remeasurement | C021 Hu methods 12 µM |
| `EC50` | Langmuir–Freundlich apparent electrochemical Kd | C005 Hu 1.8 nM |
| `EC50` | receptor dose–response | E035 Herman NMDAR 1.8 **µM** (no claim row) |
| `sensor_LOD` | blank+3SD vs blank+3RSD | C004 32 pM (3SD) vs C029 0.3 pM (3RSD) |
| `measurement_time` | incubation / interrogation / sampling | C006 15 min; C009 2 ms; C031 1 min; E045 14 s |
| `response_time` | biological τ packed here | E033 Clements 1.2 ms |
| `response_time` | enzyme or indicator waveform | C022, C023, C024 |
| `analytical_working_range` | calibration span **and** 81-fold identity | C030 vs C027 |
| `kon` | glutamate rates (empty) **and** foreign-aptamer rates | C007 vs C008/C010 |

Transferable = `yes` only for C013 and C027 (Langmuir algebra / community statement of the same identity). C011 transferable = `unknown` (kinetic inference). All other claims = `no`.

---

## 3. Load-bearing claim map

`full_text_inspected` is taken from `state/sources.csv` for the claim’s `source_id`, with the matching `core_evidence.csv` row noted when it differs. Auditor `supports_claim` is from `research/reviews/citation_audit.md`.

### 3.1 Glutamate aptamer recognition numbers

| ID | Tag | Quantity | Value | Construct | Conditions | Locator | transferable | FTI (source / evidence) | Measured / inferred / unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C001 | primary-source-supported | Kd_molecular | 12 µM | 1d04 (not glu1) | Capture-SELEX / complex medium (unspecified in abstract) | PubMed abstract (S001) | no | partial / no | **Measured** in the indexed abstract only. VoR closed. Auditor: yes. |
| C005 | primary-source-supported | EC50 | 1.8 nM | surface Glu-apt on AuED-MEA | PBS ACV; Langmuir–Freundlich | S002 §3.2 | no | yes / yes | **Measured** as apparent electrochemical Kd, not solution Kd. Authors contrast with cited solution values. |
| C014 (Kd half) | primary-source-supported | Kd_molecular | 293 nM | glutamate aptamer (SI sequence) | SPR (buffer not specified as 0.1× PBS in the SPR sentence) | S021 Fig. 3; SPR paragraph / Fig. S6 | no | yes / yes | **Measured** SPR Kd. Do not transfer onto FET LOD. |
| C021 | primary-source-supported | Kd_molecular | 12 µM | Hu Glu-apt sequence; **label from Wu citation** | AuED-MEA methods | S002 Experimental section sequences | no | yes / yes | **Not measured by Hu.** Citation of Wu. Auditor: yes. |
| C026 | primary-source-supported | *(empty)* | *(empty)* | truncated Fc- and thiol-modified Glu-apt vs cited solution Kd | PBS ACV | S002 §3.2 | no | yes / yes | **Measured:** sequence/modification as used. **Inferred (authors):** 2D confinement explains 12 µM vs 1.8 nM. Mapper: confinement remains author interpretation. |

E036 records the Hu oligo as `5'-HS-C6-GCATCAGTCCACTCGTGAGGTCGACTGATGAGGCTCGAT-Fc-3'`. Truncation was **not** shown in inspected texts as a separate solution-phase Kd of that 39-mer (`aptamer_biochemist.md`).

### 3.2 Glutamate aptamer sensor LOD / range / gain

| ID | Tag | Quantity | Value | Construct | Conditions | Locator | transferable | FTI | Measured / inferred / unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C002 | primary-source-supported | sensor_LOD | 0.0013 pM | truncated glu1 Fc-thiol-MCH | gold E-AB ACV; LOD matrix **unspecified in abstract**; selectivity mentioned in 10-fold diluted human serum | S001 PubMed abstract | no | partial / no | **Measured** in abstract only. Different construct from 1d04. |
| C004 | primary-source-supported | sensor_LOD | 32 pM PBS; 51.5 pM 50% serum | Glu-apt on AuED-MEA | ACV multiplex MEA | S002 Fig. 4h; §3.4 | no | yes / yes | **Measured** blank+3SD (PBS) and serum LOD. Not Wu 0.0013 pM. |
| C014 (LOD half) | primary-source-supported | sensor_LOD | 10 fM | same family on AuNP/CNT FET | 0.1× PBS | S021 Fig. 3 | no | yes / yes | **Measured** practical LOD in 0.1× PBS. Not 1× aCSF, not in vivo. |
| C025 | primary-source-supported | sensor_LOD | 1 aM | NG-Apt-Glu (in silico) | graphene FET; aCSF | S010 bioRxiv abstract | no | partial / partial | **Claimed** in a preprint abstract. Not peer-reviewed. ELONA millimolar Kd **not entered**. |
| C029 | primary-source-supported | sensor_LOD | 0.3 pM | Glu-apt on PaC probe | PBS calibration, 1 nM–1 mM; blank+3 RSD | S066 Fig. 6.7; §6.2 | no | yes / yes | **Measured** on PBS calibration. Not Ames. Not tissue. Not C004’s 32 pM. |
| C030 | primary-source-supported | analytical_working_range | 10 nM–10 µM | Glu-apt on PaC probe | Ames medium | S066 Fig. 6.9A; §6.2 | no | yes / yes | **Measured** linear window. Authors: poor quantitative SNR vs PBS. E044 notes 41.6% blank noise. |
| C032 | primary-source-supported | signal_gain | *(empty — intentional)* | Glu-apt on PaC probe | 100 nM Glu vs 10 µM ST, DA, Tyr, Lac | S066 Fig. 6.8A | no | yes / yes | **Measured:** those interferents were tested. **Unknown:** Asp/Gln/GABA ratios (absent from panel). |

**Evidence rows with ranges that have no dedicated claim:**

| Evidence | Quantity | Value | Construct | Matrix | FTI |
| --- | --- | --- | --- | --- | --- |
| E003 | analytical_working_range | 0.01 pM–1 nM | glu1 Fc-thiol | unspecified in abstract | no |
| E007 | analytical_working_range | 0.1 nM–10 µM | Hu Glu-apt AuED-MEA | PBS semi-log; r=0.99 | yes |
| E026 | analytical_working_range | 10 fM–100 nM | Xiao Glu FET | 0.1× PBS | yes |
| E041 | analytical_working_range | 1 aM–10 pM | NG-Apt-Glu | aCSF; preprint abstract | partial |

Mission 1 Candidate C uses E003’s **1 nM ceiling** and E041’s **10 pM ceiling** as sitting below Herman 25 nM. Those ceilings are in the evidence table; they are not separate claim IDs.

### 3.3 Clocks (protocol vs binding vs biology)

| ID | Tag | Quantity | Value | Construct | Conditions | Locator | transferable | FTI | Measured / inferred / unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C006 | primary-source-supported | measurement_time | 15 min | Glu-apt AuED-MEA | incubation before ACV; PBS | S002 §3.2; Fig. S8 | no | yes / yes | **Measured protocol wait.** Auditor: Fig. 3f 15 min is **ST**, not Glu; Glu wait is §3.2 / Fig. S8. Not koff. |
| C009 | primary-source-supported | measurement_time | 2 ms | tobramycin E-AB IPA | IPA interrogation | S004 Methods | no | yes / yes | **Measured interrogation clock.** Not glutamate. Not koff. |
| C028 | primary-source-supported | measurement_time | 10 min | Glu-apt on PaC probe | wait after 10 nM Glu until plateau | S066 Fig. 6.6; §6.2 | no | yes / yes | **Measured wait-to-plateau.** Not a fitted koff. Distinct from C006. |
| C031 | primary-source-supported | measurement_time | 1 min (sampling); 14 s is the scan (E045) | Glu-apt on PaC probe in retina | in vitro mouse retina | S066 §6.3 | no | yes / yes | **Measured clocks** plus **author statement** that this reports basal Glu, not synaptic transients. |
| C011 (tau half) | primary-source-supported | stored as biological_concentration_range on the claim; **1.2 ms lives on E033 as `response_time`** | 1.2 ms | not aptamer | cultured hippocampal synapses | S049 PubMed abstract | unknown | no / no | **Inferred** kinetic decay tau. Not a sensor spec. VoR closed. |
| C022 | primary-source-supported | response_time | 500–800 ms | GlutOx MEA, not aptamer | freely moving rat CNS | S054 PMC3482110 HTML | no | yes / yes | **Measured** enzyme-electrode response. Comparator only. |
| C023 | primary-source-supported | response_time | 0.73 s simulated; experimental 0.8 ± 0.2 s cited in-paper | not aptamer | enzyme-electrode model | S055 PMC5881573 HTML | no | yes / yes | **Simulation + cited experiment.** Not aptamer. |
| C024 | primary-source-supported | response_time | 10–100 fold longer than free Glu lifetime | iGluSnFR, not aptamer | brain / simulations as in paper | S062 PMC7255799 XML | no | yes / yes | **Measured/modeled indicator waveform ≠ free [Glu].** |
| E027 | *(no claim; in C014 notes)* | response_time | 200 s | Xiao multiplex FET | 0.1× PBS after 10 nM target | S021 Fig. 5e | no | yes | **Measured** stabilize time. |

### 3.4 Biological concentration set-points

| ID | Tag | Quantity | Value | System | Locator | transferable | FTI | Measured / inferred / unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C011 (peak half) | primary-source-supported | biological_concentration_range | 1.1 mM | cultured hippocampal synapses; not aptamer | S049 abstract | unknown | no / no | **Inferred** peak free glutamate, not a chemical assay. Auditor: yes as inference. |
| C012 | primary-source-supported | biological_concentration_range | 25 nM | acute hippocampal slice; NMDAR tonic current; intact transport | S050 abstract; discussion | no | yes / yes | **Estimated** ambient extracellular glutamate. Auditor: paper does **not** use *extrasynaptic* as its own compartment label. Contrasts cited dialysis 1–4 µM. |
| E035 | *(no claim row)* | EC50 | 1.8 µM | NMDAR nucleated patches (CA1 somata) | S050 Fig. 2C | — | yes | **Measured receptor EC50.** Digit-collision risk with Hu 1.8 **nM** (C005). Mission 1 Candidate A names this trap. |

Herman 25 nM and Clements 1.1 mM / 1.2 ms are **hippocampal literature**, not measurements inside Hu’s retina experiment. Mission 1 tournament records that hop as a gate defect if occupancy-at-basal is asserted.

### 3.5 Occupancy identities (not sensor measurements)

| ID | Tag | Quantity | Value | Object | Locator | transferable | FTI | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C013 | review-supported | analytical_working_range | 81-fold (10–90%) | generic 1:1 Langmuir | S030 Rousseau PMC10750225 | yes | yes | Community statement of the identity. Tonic/cleft numbers are from C012/C011, **not** measured in Rousseau. |
| C027 | computational illustration | analytical_working_range | 81-fold | 1:1 Langmuir algebra (c10=Kd/9, c90=9 Kd) | algebra; Rousseau states the same | yes | yes (review) | **Derived.** Independent of Kd. Implemented in `occupancy_kinetics`. For Langmuir–Freundlich, Mission 1 notes 10–90% is 81^(1/n); Hu’s *n* is **unknown**. |
| C003 | hypothesis | *(empty)* | *(empty)* | 1d04 vs glu1 in one abstract | S001 construct split | no | partial | **Interpretation:** Kd and LOD in Wu 2022 are not interchangeable. Auditor: construct split is in the abstract; transferring 1d04 Kd onto glu1 LOD is **not** supported. |

**~44,000-fold** (25 nM → 1.1 mM) is Mission 1 arithmetic on C012 and C011. Tag in the tournament: `computational illustration`. Not a measured biological span in one preparation.

**θ overlays** (`occupancy_table.csv`, all `SIMULATION/BOUND`):

| Advertised number used as occupancy Kd | θ(25 nM) | θ(1.1 mM) |
| --- | --- | --- |
| 1d04 12 µM | 0.0021 | 0.9892 |
| Hu apparent 1.8 nM | 0.9328 | 1.0000 |
| Xiao SPR 293 nM | 0.0786 | 0.9997 |

Mission 1 **withdrew** “Hu device is ~93% occupied at basal” as a finding: 1.8 nM is an AuED-MEA Langmuir–Freundlich EC50, not a 1:1 Kd of the PaC probe in Ames/tissue. PaC-probe apparent Kd is **empty**.

### 3.6 Glutamate kon/koff (absent)

| ID | Tag | Quantity | Value | Notes |
| --- | --- | --- | --- | --- |
| C007 | unresolved | kon *(empty)* | *(empty)* | No glutamate aptamer kon/koff in inspected glutamate sensor papers (S001/S002/S010/S021; later S066 clocks are not koff). Absence of evidence, not a negative kinetic experiment. `source_id` S001 is the primary glutamate paper searched, not a kon measurement. transferable = no. FTI of S001: partial. |

Foreign-aptamer rates **in the ledger but not transferable to glutamate:**

| ID | Tag | Quantity | Value | Construct | Conditions | FTI |
| --- | --- | --- | --- | --- | --- | --- |
| C008 | primary-source-supported | kon | 3.5e4 M^-1 s^-1 | tobramycin parent aptamer E-AB | IPA tris buffer; also koff 1.39 s^-1, kinetic Kd 41±11 µM (E012–E015) | yes |
| C010 | primary-source-supported | kon | 2e5 to 96 M^-1 s^-1 | various DNA aptamers, **not glutamate** | solution ITC abstract; koff 1.03e-3 to 0.012 s^-1 over Kd 28 nM–864 µM | no (S003) |

Overnight sensitivity figure uses C008/C010 as a **labeled NOT-glutamate envelope**. Under C010 high-end kon, occupancy-table `t_off` for 12 µM is 0.41667 s (seconds, not 0.8 ms). That row is SIMULATION/BOUND, not a glutamate measurement.

### 3.7 Interface / AI / mislabel / in-vivo scope

| ID | Tag | Quantity | Value | What it is | transferable | FTI |
| --- | --- | --- | --- | --- | --- | --- |
| C015 | primary-source-supported | signal_gain | 2–2.5 fold | DNT-Apt48 vs Apt48; N-protein TFBG-SPR; not glutamate | no | yes |
| C016 | primary-source-supported | Kd_molecular | 12.9 nM best G1L | InstructNA vs HT-SELEX on LOX1/CXCL5 proteins; many non-binders | no | yes |
| C017 | computational illustration | *(empty)* | *(empty)* | Docking fails theophylline vs caffeine selectivity | no | yes |
| C018 | primary-source-supported | signal_gain | 60–200% | Cocaine E-AB packing density / SAM; apparent Kd also moves (E029). Not glutamate | no | yes |
| C019 | primary-source-supported | *(empty)* | *(empty)* | Park 2023 “Glutamate FET” = *P. falciparum* GDH, Singh 2019 PMID 30308419. Auditor: **supports_claim=no** if used as neurotransmitter-Glu sensor evidence | no | yes |
| C020 | unresolved | *(empty)* | *(empty)* | No verified **in vivo** glutamate aptamer sensor. S018/S019 are serotonin/dopamine FETs. S066 is **in vitro** retina, not in vivo. Scope limit, not a measured glutamate negative | no | S018 yes |

### 3.8 Claim-status census

| evidential_status | n | IDs |
| --- | --- | --- |
| primary-source-supported | 26 | C001–C002, C004–C006, C008–C012, C014–C016, C018–C019, C021–C026, C028–C032 |
| unresolved | 2 | C007, C020 |
| computational illustration | 2 | C017, C027 |
| hypothesis | 1 | C003 |
| review-supported | 1 | C013 |

Among the 26 `primary-source-supported` rows, several are **not glutamate-aptamer measurements** (C008–C011, C015–C016, C018, C022–C024) or are **citations / author interpretation** (C021, C026 confinement). Tag ≠ “usable as a glutamate Kd.”

---

## 4. Measured vs inferred vs unknown

### 4.1 Measured (construct- and matrix-tagged)

Glutamate DNA aptamer, as named in the ledger:

- 1d04 Kd 12 µM — abstract only (C001 / E001).
- glu1 LOD 0.0013 pM and range 0.01 pM–1 nM — abstract only (C002 / E002–E003).
- Hu AuED-MEA: apparent electrochemical Kd 1.8 nM; PBS LOD 32 pM; 50% serum LOD 51.5 pM; PBS semi-log 0.1 nM–10 µM; Glu ACV wait 15 min (C004–C006, E004–E008). Sequence as used, with Wu 12 µM as a **citation** (C021 / E036).
- Xiao: SPR Kd 293 nM; FET LOD 10 fM and range 10 fM–100 nM in 0.1× PBS; stabilize 200 s (C014, E024–E027).
- Hu PaC probe: 10 min plateau after 10 nM Glu; PBS LOD 0.3 pM; Ames 10 nM–10 µM; ACV 14 s/scan then ~1 min sampling in isolated mouse retina; authors: basal, not synaptic transients; selectivity panel as C032 (C028–C032, E042–E046).
- Abrantes 1 aM / 1 aM–10 pM — preprint abstract claims only (C025, E040–E041).

Non-aptamer comparators that **were** measured or modeled in their own systems: Herman ambient ~25 nM and NMDAR EC50 1.8 µM (C012, E034–E035); Rutherford 500–800 ms; Clay 0.73 / 0.8 ± 0.2 s; Armbruster 10–100×; White cocaine gain/Kd/times; Abeykoon tobramycin IPA rates and 2 ms clock; Ding ITC survey endpoints (abstract); Xu/Tanner N-protein fiber; InstructNA protein SPR; Xie/Liu docking failure.

### 4.2 Inferred (do not promote to measured glutamate-aptamer facts)

- Clements 1.1 mM peak and 1.2 ms tau (C011 / E032–E033): kinetic inference, abstract-only, cultured synapses.
- Hu 2D-confinement explanation of 12 µM vs 1.8 nM (C026): authors’ interpretation.
- 1:1 θ(25 nM) overlays of 12 µM / 1.8 nM / 293 nM: SIMULATION using advertised numbers as occupancy Kd (`occupancy_table.csv`).
- Diffusion-limit `t_off` and `τ_eq` rows: BOUND, and C008/C010 kon values are **not glutamate**.
- 81-fold 10–90% window: algebra / review identity (C027 / C013), not a calibration of Hu’s LF sensor.
- ~44,000-fold tonic-to-cleft span: arithmetic on two different hippocampal literatures.
- “Too slow for synapses” as a **measured koff**: not licensed (C007).
- Occupancy of the PaC probe at basal Glu in Ames/tissue: **not measured**. Probe 3 “near saturation” is author-reported and gold-confounded (Fig. 6.16 in Mission 1 notes).
- Chemical identity of the retina ACV change as glutamate: **not** shown (no TTX/CNQX/AP5/TBOA/scrambled aptamer in the mapped Hu reconstruction).
- In vivo glutamate aptamer sensing: **not** in this ledger (C020). S066 is in vitro.

### 4.3 Unknown (empty on purpose)

- Glutamate aptamer `kon` and `koff` on any inspected construct (C007).
- Solution `Kd_molecular` of Hu’s Fc-thiol 39-mer (not 1d04).
- Langmuir–Freundlich exponent *n* for Hu Glu.
- PaC-probe apparent Kd in PBS, Ames, or tissue.
- Glu vs Asp/Gln/GABA signal-gain ratios on Hu/Xiao constructs (C032; W1 REJECT as a fifth title).
- Wu VoR truncation table; Lam “12 ± 6 µM” **not found** in inspected Lam PMC this session (`citation_audit.md`) and **not** in claims.
- Ohsawa conjugate Kd; MacDonald surface-crowding Kd — identifiers ok, numbers **not entered**.
- Abrantes ELONA millimolar Kd — **not entered**. API tokens `10.3` / `25.1` are funder IDs.
- Absolute [Glu] in the retina experiment; which Glu pool (GCL/IPL-border electrode vs photoreceptor-terminal narrative).
- Probe 3 mechanism: occupancy ceiling vs lost gold (`unresolved` in the tournament).

---

## 5. Numbers used in Mission 1 *narrative* that are not in `claims.csv`

These appear in `reports/mission1_story_tournament.md` and/or candidate/Hu notes. This map **does not promote them**.

| Number | Where it is used | Ledger status |
| --- | --- | --- |
| DA apparent Kd 49.6 µM ≈ cited 44 µM | B red team / Opus / tournament “what surprised us” | **Not** in `claims.csv` or `core_evidence.csv`. Do not treat as a mapped claim. |
| Ames blank noise 41.6% | E044 limitation text; H1/H3; Candidate C | In evidence **limitation** field, not a claim value. |
| Ames L-glutamine 0.073 g/L ≈ 0.5 mM | W1 / tournament; public A1420 arithmetic | Tagged `unresolved` vendor identity; **no interference measurement**. |
| Fig. 6.5 body 10 nM vs caption 100 nM | H1/H3 | Inconsistency recorded; both values; not a claim row. |
| Probe 3/4 gold detachment (Fig. 6.16) | Mission 1 gate / C / Opus | Primary as **failure analysis** in tournament text; no dedicated claim ID. |
| θ(25 nM)≈0.93 | occupancy table / unrevised D | SIMULATION overlay of C005; withdrawn as tissue finding. |
| 44,000-fold | C011/C012 arithmetic | computational illustration |
| Ricci 2016 as LF neighborhood citation | B / Opus | Tournament says Ricci is a **1:1 Langmuir Account**, not an LF paper. Not a ledger source. |

---

## 6. Construct isolation (no property transfer)

Ledger `transferable=no` unless noted. Mission 1 and Round 2 reviews treat these as **different objects**:

| Construct | What was actually attached to it |
| --- | --- |
| 1d04 SELEX isolate | abstract Kd 12 µM (C001) |
| truncated glu1 Fc-thiol-MCH gold E-AB | abstract LOD 0.0013 pM; range 0.01 pM–1 nM (C002, E003) |
| Hu Glu-apt on **AuED-MEA** (journal S002) | cited 12 µM; LF apparent Kd 1.8 nM; LOD 32 / 51.5 pM; PBS range 0.1 nM–10 µM; 15 min wait |
| Hu Glu-apt on **PaC intraretinal probe** (thesis S066) | 10 min plateau; PBS LOD 0.3 pM; Ames 10 nM–10 µM; 14 s / 1 min in vitro retina. **No reported apparent Kd** |
| Xiao glutamate aptamer SPR | Kd 293 nM |
| Xiao same family CNT FET | LOD 10 fM; range 10 fM–100 nM; 200 s; **0.1× PBS** |
| NG-Apt-Glu (in silico, preprint) | claimed 1 aM in aCSF |
| tobramycin / cocaine / N-protein / LOX1 / theophylline models | architecture or AI lessons only |

Do not merge S002 multiplex MEA numbers onto S066 PaC probes (`evidence_packet.md`).

---

## 7. Mission 1 process outcomes (inventory, not a vote)

Eighteen lanes completed (protocol table). Blind Opus 5 scored A–D without T1–T5 files. Gate JSON:

- **REVISE**, not group-final.
- Load-bearing primary evidence for the occupancy-at-basal half: **false**.
- Recommended thesis id in JSON: `D_revised`. Runner-up: `C`. Rejected as title: fit-for-purpose; construct-transformation; strong-form “LOD distracts”; three-regimes D; occupancy-saturation-as-measured; W1 amino-acid selectivity.
- Flagship analysis in JSON: 81-fold 1:1 identity vs ~44000-fold Herman-to-Clements span; **demote** 1.8 nM 1:1 overlay as tissue occupancy.
- Next experiment in JSON: paired solution and surface isotherm of Hu Fc-thiol 39-mer in one buffer; report Langmuir–Freundlich *n*.

Overnight T1 vs T5 remain in `poster/theses.md` and `state/scoreboard.json` with **inverted stacks**. Mission 1 explicitly does not adopt that ranking as its result. This map does not choose among T1, T5, C, or D.

Hu retina H1–H3 consensus (as the tournament records it): the experiment answered a **device-level** question (light-dependent, minutes-scale, basal-Glu-correlated ACV on Probes 1–2, same shank as spikes) in **in vitro** mouse retina. It did not answer how much glutamate, how fast, from which pool, or with pharmacological identity.

W1: amino-acid selectivity is a real gap (C032), **REJECT** as a fifth organizing story.

---

## 8. Negative-search integrity (what was looked for and not entered)

From `citation_audit.md`, `contradictions.md`, `remaining_blockers.md`, Round 2, and Mission 1 packet:

- Glutamate kon/koff: searched in S001 abstract, S002 VoR, S021 VoR, S010 abstract, S066 OA extract. **None entered.**
- Abrantes millimolar ELONA Kd: not in abstract; bioRxiv HTML/JATS HTTP 429 this cycle; `10.3`/`25.1` are funder IDs. **Unentered.**
- Lam ±6 µM: not found in inspected Lam PMC XML/HTML. **Unentered.**
- Ohsawa 580–810 µM: JSTAGE PDF 500; **unentered.**
- MacDonald surface crowding: ACS 403; **unentered.**
- In vivo glutamate aptamer: Zhao 2021 / Wu Nano Lett 2022 are 5-HT / DA. Hu journal future-tense in vivo. S066 in vitro. **C020 unresolved.**
- Park as Glu NT FET: **refuted** (C019).

This is a search-and-ledger record, not proof that no such numbers exist outside the inspected set.

---

## 9. Strongest supported Mission 1 conclusion

From the **tagged primary rows**, without choosing a poster slogan:

1. **Published glutamate-aptamer figures are different physical objects on different constructs and in different matrices.** 1d04 Kd 12 µM (abstract) is not glu1 LOD 0.0013 pM (abstract) is not Hu’s cited 12 µM is not Hu’s 1.8 nM Langmuir–Freundlich apparent electrochemical Kd is not Hu MEA LOD 32 pM / 51.5 pM is not PaC-probe PBS LOD 0.3 pM is not Xiao SPR 293 nM is not Xiao FET 10 fM in 0.1× PBS. Transferable = no on all of those claim rows.

2. **No glutamate aptamer kon/koff is in the inspected set (C007, unresolved).** Protocol clocks that *are* measured on Glu-apt devices are minutes-scale (15 min MEA wait; 10 min PaC plateau; 14 s ACV then ~1 min retina sampling). Those are `measurement_time`, not koff. A 2 ms IPA clock is tobramycin interrogation (C009).

3. **The strongest glutamate-aptamer experiment in nervous tissue in this ledger is Hu thesis S066, in vitro mouse retina, and the authors themselves locate it at basal / minutes, not synaptic transients (C031).** It is not in vivo (C020). Occupancy at that basal on the PaC probe in Ames/tissue was **not measured**.

4. **The biological numbers the swarm uses as set-points are not aptamer measurements:** Herman ~25 nM ambient in acute hippocampal slice (C012); Clements inferred 1.1 mM / 1.2 ms at cultured hippocampal synapses, abstract-only (C011). A 1:1 Langmuir 10–90% window is exactly 81-fold (C027, computational illustration; C013 review-supported). Overlaying that window, or θ≈0.93, onto Hu’s LF 1.8 nM as tissue occupancy is a double hop (isotherm type and device). Mission 1’s science-story gate is **REVISE** for that reason.

5. **Missing koff does not, by itself, prove a millimolar rising edge is impossible.** That caveat is already in the Mission 1 tournament (`τ_eq = 1/(kon c + koff)`). It is a limit on inference, not a glutamate rate.

Science-story gate remains **REVISE**. No group-final thesis (`state/decisions.md`).

---

## 10. Biggest evidential holes

1. **Glutamate `kon`/`koff` on the construct that went into tissue** (Hu Fc-thiol 39-mer), with controlled mass transport. C007 is the load-bearing empty cell.
2. **Paired solution `Kd_molecular` and surface apparent Kd of that same 39-mer**, Langmuir and Langmuir–Freundlich, with exponent *n* and coverage. Without this, 12 µM vs 1.8 nM cannot be read as a measured confinement result, and θ at 25 nM cannot be computed for the retina device.
3. **PaC-probe isotherm in Ames/tissue** — apparent Kd empty; 0.3 pM is PBS blank+3 RSD, not Ames, lowest calibrant 1 nM (C029 vs C030).
4. **Chemical identity of the retina ACV change** (pharmacology + scrambled aptamer). Light-locked signal-gain on Probes 1–2 is not a glutamate assay by itself.
5. **Wu 2022 VoR** — 1d04 vs glu1 biochemistry beyond the abstract is unverified (C001/C002 rest on abstracts).
6. **Clements VoR** — 1.1 mM / 1.2 ms remain abstract inference (C011).
7. **Amino-acid selectivity (Glu vs Asp/Gln/GABA)** at concentrations relevant to Ames or cleft (C032; W1).
8. **Probe 3:** occupancy vs gold-nanostructure loss (Fig. 6.16); GCL/IPL-border electrode vs photoreceptor narrative.
9. **In vivo glutamate aptamer sensor** — absent (C020).
10. **Overnight vs Mission 1 title split, plus two scoring stacks that invert T1/T5** — process hole, not a missing paper.

---

## 11. What would most change our mind

Copied from Mission 1’s own reversing-evidence list (`reports/mission1_story_tournament.md` §7), not invented here:

- Paired solution and surface isotherm of the exact Fc-thiol 39-mer **near 12 µM** → θ(25 nM) tiny; “saturated at basal” arithmetically dead; LOD/working-range story (C) strengthens relative to occupancy-saturation.
- Same pair **near 1.8 nM** → confinement becomes a measured result; construct/interface story (B) strengthens relative to its ceiling.
- Pharmacology + scrambled aptamer identifies the retina ACV change as glutamate → “device already works at basal” becomes primary; still does not fill C007 or Clements.
- Measured Glu-apt `koff` **fast at a µM-scale Kd** → cleft column moves from untested toward architecture/interrogation-clock.
- Large Asp/Gln cross-reactivity at Ames-realistic concentrations → W1 content becomes load-bearing inside every title.
- Conversely: a PaC-probe occupancy measurement at ambient glutamate, or an explicit poster that occupancy is unknown, is what Mission 1 says would be required to move the science-story gate off **REVISE**.

Highest-information next *experiment* already recorded in `state/gates/science_story.json` (not chosen by this mapper): paired solution and surface isotherm of Hu’s Fc-thiol 39-mer in one buffer, report Langmuir–Freundlich *n*. If the biological question is retinal glutamate rather than sensor fitness, the tournament substitutes pharmacological identity. It says: do not do both and report neither.

---

## 12. Explicit non-recommendation

This file maps Mission 1 evidence. It does **not** recommend T1, T5, A, B, C, revised D, or any other final scientific story, flagship-analysis packaging, or poster headline. Gate status, competing titles, and reversing experiments above are inventory of what the repo already recorded.
