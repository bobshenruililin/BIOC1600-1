# Round 1 literature scout 05 — biological glutamate context

**Scout ID:** 05 of 06  
**Lane (search focus, not a conclusion):** synaptic vs extrasynaptic vs CSF/plasma glutamate concentration ranges, and signaling timescales a sensor would need to resolve.  
**Central question (not answered here):** Can an aptamer actually keep up with neurochemical signaling? What do affinity, selectivity, binding kinetics, sensor transduction, immobilization and biological context jointly determine about the usefulness of a glutamate aptamer biosensor?  
**Round:** 1 — candidates only. Nothing promoted to `core`. Ledgers not written.  
**Isolation:** This scout did not read other scout reports, theses, `state/claims.csv`, `state/sources.csv` science rows, or `reports/nightly_summary.md` for conclusions.  
**Date of search:** 2026-09-11  
**Access used:** PubMed E-utilities, Europe PMC REST, Crossref REST, publisher/PMC OA HTML. Unpaywall REST returned HTTP 422 in this environment (see unverified identifiers). No Sci-Hub, no paid APIs, no PDFs committed.

Quantity types below are recorded separately. This record does **not** treat any `biological_concentration_range` as an aptamer `Kd_molecular`, `EC50`, `sensor_LOD`, or `analytical_working_range`, and does **not** treat any biological timescale as an aptamer `kon`/`koff`, sensor `response_time`, or `measurement_time`. No inference is made about whether an aptamer can or cannot keep up.

Every number below was read from the cited source (abstract and/or OA HTML). Missing values are left empty.

---

## Search strategy (negative-search integrity)

PubMed (`esearch` + `esummary` + `efetch` abstract XML) and Europe PMC title/OA searches, then PMC/publisher OA HTML for full-text inspection.

**Queries used (representative):**

- `time course of glutamate in the synaptic cleft`
- `extracellular glutamate concentration hippocampal slice`
- `extrasynaptic ambient glutamate concentration`
- `cerebrospinal fluid glutamate concentration human` / `healthy volunteers`
- `plasma serum glutamate concentration healthy`
- `glutamate transporter clearance timescale synapse`
- `iGluSnFR glutamate dynamics in vivo`
- `microdialysis extracellular glutamate brain basal`
- `synaptic cleft glutamate millimolar millisecond`
- Author/title searches: Clements; Diamond AND Jahr transporters buffer; Dzubay AND Jahr; Herman AND Jahr; Chiu AND Jahr nucleus accumbens; Le Meur tonic NMDA; Rusakov AND Kullmann extrasynaptic diffusion; Okubo imaging extrasynaptic; Armbruster glutamate clearance; Helassa ultrafast glutamate; Moussawi extracellular glutamate; Hawkins blood-brain barrier glutamate; Zhou AND Danbolt healthy brain; Hashimoto CSF glutamine glutamate; Alfredsson glutamate cerebrospinal serum; Trabado plasma metabolome; Timmerman Westerink microdialysis; Cavelier Attwell tonic glutamate; Featherstone intercellular glutamate; Scimemi Beato neurotransmitter concentration; Danbolt glutamate uptake; Madeira CSF glutamate Alzheimer; Ercan plasma-free amino acid.

**What the searches actually returned vs what was kept:**

- CSF/plasma keyword searches were dominated by disease cohorts, drug PK, and MRS (tissue glutamate+glutamine, not extracellular `biological_concentration_range`). Those were not treated as synaptic/extrasynaptic concentrations.
- “Ambient extrasynaptic glutamate” returns both nanomolar electrophysiological estimates and micromolar microdialysis/biosensor estimates. Both families were retained as candidates because they measure different compartments/methods; they were not averaged.
- iGluSnFR/EOS papers were retained only as **biological timescale / extrasynaptic transient** measurements. Indicator `Kd_molecular` is recorded as a sensor property of that protein, not as brain glutamate concentration.

---

## Candidate sources (n = 15)

Status for orchestrator merge: **`candidate` only**.

---

### C01 — Clements, Lester, Tong, Jahr, Westbrook 1992

- **title:** The time course of glutamate in the synaptic cleft.
- **year:** 1992
- **journal:** Science
- **authors (PubMed listing):** Clements JD; Lester RA; Tong G; Jahr CE; Westbrook GL  
  Crossref expands given names to John D. Clements; Robin A. J. Lester; Gang Tong; Craig E. Jahr; Gary L. Westbrook. Same article; no silent “best guess” between listings.
- **DOI:** 10.1126/science.1359647
- **PMID:** 1359647
- **PMCID:** (empty; Europe PMC `pmcid: None`)
- **source_type:** `primary`
- **why it matters for THIS lane:** Direct kinetic estimate of **free glutamate in the synaptic cleft** at cultured hippocampal synapses, i.e. the phasic synaptic `biological_concentration_range` and a clearance **timescale**, not an aptamer or electrode property. The abstract states glutamate peaked at 1.1 millimolar and decayed with a time constant of 1.2 milliseconds. The same abstract separates AMPA vs NMDA occupancy consequences of that time course; those receptor inferences are not transferred here to any sensor.
- **full_text_inspected:** `partial` (PubMed abstract). Science VoR HTML was not available on the free routes used (publisher 403; no PMCID).
- **access_route:** `abstract-only`
- **limitation:** Cultured hippocampal synapses, not in vivo neuropil. The 1.1 mM / 1.2 ms figures are a kinetic **estimate** from displacement of a rapidly dissociating NMDA antagonist, not a direct chemical assay in the cleft. Later modeling (C02, C07, C10) argues the true free-glutamate decay can be faster than the 1.2 ms antagonist-derived τ. Do not transfer these numbers to extrasynaptic space, CSF, or plasma.

**Extracted quantities (from inspected abstract):**

| quantity_type | value | units | claim_tag | transferable | locator |
| --- | --- | --- | --- | --- | --- |
| biological_concentration_range (synaptic cleft, peak, estimated) | 1.1 | millimolar | primary-source-supported | no (this construct/system only) | abstract |
| (clearance timescale; not sensor response_time) | 1.2 | milliseconds (decay time constant) | primary-source-supported | no | abstract |

---

### C02 — Diamond and Jahr 1997

- **title:** Transporters buffer synaptically released glutamate on a submillisecond time scale.
- **year:** 1997
- **journal:** The Journal of Neuroscience (PubMed source: J Neurosci)
- **authors (PubMed):** Diamond JS; Jahr CE
- **DOI:** 10.1523/JNEUROSCI.17-12-04672.1997
- **PMID:** 9169528
- **PMCID:** PMC6573331
- **source_type:** `primary`
- **why it matters for THIS lane:** Tests whether glutamate transporters change the **cleft glutamate time course within the first few hundred microseconds** at cultured rat CA1 autapses, a timescale a synaptic-resolution sensor would have to resolve. OA HTML states most free glutamate is cleared very rapidly, perhaps within 1 msec (citing C01), and that transporter block further slows the mEPSC rise in kynurenate, indicating transporters affect cleft glutamate in the first few hundred microseconds. Buffering, not a full transport cycle, is the authors’ mechanistic conclusion.
- **full_text_inspected:** `yes` (PMC HTML)
- **access_route:** `pmc`
- **limitation:** Cultured microisland autapses, not adult in vivo cortex. The glutamate waveform used in the AMPA-receptor model is constrained to resemble C01/Clements 1996 estimates; it is not an independent millimolar assay. Transport-cycle time is stated to be too slow to explain the submillisecond effect — do not confuse cycling time with the buffering timescale. Not CSF/plasma.

**Extracted quantities (PMC HTML):**

| quantity_type | value | units | claim_tag | transferable | locator |
| --- | --- | --- | --- | --- | --- |
| (timescale: transporter effect on cleft glutamate) | first few hundred microseconds | — | primary-source-supported | no | Results/abstract via PMC HTML |
| (timescale: literature comparison in this paper) | perhaps within 1 msec | — | review-supported in this paper (cites Clements 1992) | no | Introduction, PMC HTML |

Patch solution-exchange 20–80% time ~100 μsec and recording rise 25 μsec are **instrument `measurement_time`**, not biological glutamate time course.

---

### C03 — Dzubay and Jahr 1999

- **title:** The concentration of synaptically released glutamate outside of the climbing fiber-Purkinje cell synaptic cleft.
- **year:** 1999
- **journal:** The Journal of Neuroscience
- **authors (PubMed):** Dzubay JA; Jahr CE
- **DOI:** 10.1523/JNEUROSCI.19-13-05265.1999
- **PMID:** 10377338
- **PMCID:** PMC6782308
- **source_type:** `primary`
- **why it matters for THIS lane:** Quantifies **extrasynaptic** glutamate at Bergmann glial membranes after climbing-fiber release, distinct from cleft millimolar estimates. PMC HTML: extrasynaptic transmitter concentration estimated to reach 160–190 μM (from 840 ± 240% potentiation, n = 8, and patch EC50 1810 μM control vs 304 μM in CTZ). Contrast stated in-paper: cleft thought to rise rapidly above 1 mM. Also states glial transporter activation lasts >10 msec in cerebellum and hippocampus (citing Bergles & Jahr 1997 and related).
- **full_text_inspected:** `yes` (PMC HTML)
- **access_route:** `pmc`
- **limitation:** P13–P15 rat cerebellum, climbing fiber–Purkinje/Bergmann glia geometry; not hippocampus, NAc, CSF, or plasma. The 160–190 μM figure is inferred from AMPA EC50 shift (cyclothiazide), not a calibrated chemical sensor. Do not transfer to tonic/ambient extrasynaptic glutamate (C04–C06). The paper’s “>10 msec” extrasynaptic elevation is cited from prior transporter-current work, not re-measured as a single τ here.

**Extracted quantities (PMC HTML):**

| quantity_type | value | units | claim_tag | transferable | locator |
| --- | --- | --- | --- | --- | --- |
| biological_concentration_range (extrasynaptic, peak at Bergmann glia, estimated) | 160–190 | μM | primary-source-supported | no | abstract + results, PMC HTML |
| EC50 (Bergmann glia AMPA in patches, control vs CTZ) | 1810 vs 304 | μM | primary-source-supported | no (receptor assay, not brain ECF) | abstract, PMC HTML |
| biological_concentration_range (cleft, cited contrast) | above 1 | mM | review-supported in this paper | no | abstract, PMC HTML |
| (timescale: extrasynaptic transporter activation, cited) | >10 | msec | review-supported in this paper | no | Introduction, PMC HTML |

---

### C04 — Herman and Jahr 2007

- **title:** Extracellular glutamate concentration in hippocampal slice.
- **year:** 2007
- **journal:** The Journal of Neuroscience
- **authors (PubMed):** Herman MA; Jahr CE
- **DOI:** 10.1523/JNEUROSCI.3009-07.2007
- **PMID:** 17804634
- **PMCID:** PMC2670936
- **source_type:** `primary`
- **why it matters for THIS lane:** Primary electrophysiological estimate of **tonic/ambient** extracellular glutamate in acute hippocampal slice, a different `biological_concentration_range` from phasic cleft millimolar transients. PMC HTML: standing NMDAR current corresponds to ~25 nM after scaling (unscaled conversion 37.9 ± 10.8 nM). Authors contrast this with microdialysis reports of 1–4 μM in vivo and NMDAR glutamate EC50 ~2 μM (Patneau and Mayer 1990; that EC50 is **receptor EC50**, not ambient concentration). Thermodynamic transporter lower limit 2 nM is cited (Zerangue and Kavanaugh 1996), not measured here.
- **full_text_inspected:** `yes` (PMC HTML)
- **access_route:** `pmc`
- **limitation:** P15–P19 rat acute slices at 32–35 °C, not in vivo. Ambient estimate is a spatial/temporal average reported by CA1 NMDARs, not a point sample of every extrasynaptic niche. Authors **suggest** in vivo ambient is also nanomolar; that in vivo leap is `hypothesis` relative to this experiment. Do not average with microdialysis micromolar values. Do not transfer 25 nM to CSF or plasma.

**Extracted quantities (PMC HTML):**

| quantity_type | value | units | claim_tag | transferable | locator |
| --- | --- | --- | --- | --- | --- |
| biological_concentration_range (ambient, hippocampal slice, NMDAR reporter) | ~25 | nM | primary-source-supported | no | abstract, Results, Discussion |
| biological_concentration_range (same method, unscaled conversion) | 37.9 ± 10.8 | nM | primary-source-supported | no | Results |
| EC50 (NMDAR, glutamate, nucleated patch in this paper) | 1.8 | μM | primary-source-supported | no (receptor, not ambient [glu]) | Results |
| EC50 (NMDAR, NMDA, nucleated patch) | 37.7 | μM | primary-source-supported | no | Results |
| biological_concentration_range (microdialysis in vivo, cited) | 1–4 | μM | review-supported in this paper | no | Introduction |

---

### C05 — Chiu and Jahr 2017

- **title:** Extracellular Glutamate in the Nucleus Accumbens Is Nanomolar in Both Synaptic and Non-synaptic Compartments.
- **year:** 2017
- **journal:** Cell Reports
- **authors (PubMed):** Chiu DN; Jahr CE
- **DOI:** 10.1016/j.celrep.2017.02.047
- **PMID:** 28297662
- **PMCID:** PMC5388241
- **source_type:** `primary`
- **why it matters for THIS lane:** Directly tests whether **synaptic vs non-synaptic** extracellular compartments in NAc hold different basal glutamate (the compartment model in C11). PMC HTML: standing NMDAR current equivalent to 25.6 ± 3.2 nM glutamate (n = 19) in juveniles and 31.7 ± 8.7 nM (n = 8) in 8–12 week adults; with 100 μM DL-TBOA, 123.2 ± 10.5 nM (n = 16) juveniles and 142.5 ± 21.1 nM (n = 4) adults. Spine Ca2+ still rare in TBOA (~3% of trials), arguing against a hidden micromolar non-synaptic reservoir feeding the cleft when EAATs are blocked.
- **full_text_inspected:** `yes` (PMC XML/HTML)
- **access_route:** `pmc`
- **limitation:** Rat NAc acute slices, not human CSF/plasma or hippocampal cleft transients. NMDAR affinity cited as ~2 μM (Hansen et al. 2014; Herman and Jahr 2007) is **receptor EC50/affinity**, not NAc glutamate concentration. In vivo microdialysis 5–6 μM in NAc core (Baker 2003; Miguéns 2008) is cited, not repeated. Do not treat TBOA-elevated nanomolar values as the intact-uptake basal range.

**Extracted quantities (PMC text):**

| quantity_type | value | units | claim_tag | transferable | locator |
| --- | --- | --- | --- | --- | --- |
| biological_concentration_range (NAc, basal, synaptic NMDAR reporter, juvenile) | 25.6 ± 3.2 | nM | primary-source-supported | no | Results (Figure 1C) |
| biological_concentration_range (NAc, basal, adult 8–12 wk) | 31.7 ± 8.7 | nM | primary-source-supported | no | Results |
| biological_concentration_range (NAc, TBOA 100 μM, juvenile) | 123.2 ± 10.5 | nM | primary-source-supported | no | Results (Figure 3B) |
| biological_concentration_range (NAc, TBOA, adult) | 142.5 ± 21.1 | nM | primary-source-supported | no | Results |
| biological_concentration_range (cited microdialysis NAc) | 5–6 | μM | review-supported in this paper | no | Results/Discussion |

---

### C06 — Le Meur, Galante, Angulo, Audinat 2007

- **title:** Tonic activation of NMDA receptors by ambient glutamate of non-synaptic origin in the rat hippocampus.
- **year:** 2007
- **journal:** The Journal of Physiology
- **authors (PubMed):** Le Meur K; Galante M; Angulo MC; Audinat E  
  Crossref parses the first author as Meur, Karim Le. Same four-author paper as PMID 17185337.
- **DOI:** 10.1113/jphysiol.2006.123570
- **PMID:** 17185337
- **PMCID:** PMC2075557
- **source_type:** `primary`
- **why it matters for THIS lane:** Characterizes **tonic** NMDAR current from ambient glutamate in CA1/subiculum slices and argues the glutamate is **glial / non-vesicular**, acting at probably extrasynaptic NMDARs (MK801 use-dependence). PMC HTML: tonic current 53.99 ± 6.48 pA at +40 mV. Vesicular-release inhibition did not affect the tonic current; glutamine-synthetase inhibition increased it; transporter inhibitors increased it. Distinguishes tonic ambient glutamate from fast millimolar cleft transients (citing Clements 1996).
- **full_text_inspected:** `yes` (PMC HTML)
- **access_route:** `pmc`
- **limitation:** Does not itself convert the 53.99 pA tonic current into a nanomolar concentration (Herman 2007 / Cavelier & Attwell do related conversions). P14–P29 rat slices. “Probably extrasynaptic” is an MK801 inference, not ultrastructural localization. Not CSF/plasma. Current amplitude is not `biological_concentration_range`.

**Extracted quantities (PMC HTML / abstract):**

| quantity_type | value | units | claim_tag | transferable | locator |
| --- | --- | --- | --- | --- | --- |
| (tonic NMDAR current amplitude, not concentration) | 53.99 ± 6.48 | pA at +40 mV | primary-source-supported | no | abstract |
| biological_concentration_range (cleft during fast transmission, cited) | millimolar range | — | review-supported in this paper (Clements 1996) | no | Introduction |

---

### C07 — Rusakov and Kullmann 1998

- **title:** Extrasynaptic glutamate diffusion in the hippocampus: ultrastructural constraints, uptake, and receptor activation.
- **year:** 1998
- **journal:** The Journal of Neuroscience
- **authors (PubMed):** Rusakov DA; Kullmann DM
- **DOI:** 10.1523/JNEUROSCI.18-09-03158.1998
- **PMID:** 9547224
- **PMCID:** PMC6792642
- **source_type:** `primary` (ultrastructure) plus **computational illustration** (extrasynaptic concentration field)
- **why it matters for THIS lane:** Adult rat CA1 neuropil geometry that constrains **how far and how long** glutamate can exist extrasynaptically after one vesicle. PMC HTML: typical nearest-neighbor synapse distance ~465 nm. Kinetic simulations: transporters rapidly reduce free transmitter; one vesicle is enough to bind high-affinity receptors in the immediate perisynaptic space; whether NMDARs at ~465 nm activate **depends critically on the extracellular diffusion coefficient**.
- **full_text_inspected:** `yes` (PMC HTML)
- **access_route:** `pmc`
- **limitation:** Concentration-vs-distance/time profiles are simulations parameterized by EM, not measured millimolar fields. Crosstalk at 465 nm remains conditional on D\*. Adult rat CA1 basal dendrites only. Do not treat simulated extrasynaptic waveforms as aptamer `response_time` requirements without stating they are simulations.

**Extracted quantities (PMC HTML):**

| quantity_type | value | units | claim_tag | transferable | locator |
| --- | --- | --- | --- | --- | --- |
| (anatomical spacing, not concentration) | ~465 | nm (nearest synapse) | primary-source-supported | no (this neuropil sample) | abstract |
| biological_concentration_range (extrasynaptic after 1 vesicle) | (not a single number; D\*-dependent) | — | computational illustration | no | abstract/discussion |

---

### C08 — Okubo et al. 2010

- **title:** Imaging extrasynaptic glutamate dynamics in the brain.
- **year:** 2010
- **journal:** Proceedings of the National Academy of Sciences
- **authors (PubMed):** Okubo Y; Sekiya H; Namiki S; Sakamoto H; Iinuma S; Yamasaki M; Watanabe M; Hirose K; Iino M
- **DOI:** 10.1073/pnas.0913154107
- **PMID:** 20308566
- **PMCID:** PMC2851965
- **source_type:** `primary`
- **why it matters for THIS lane:** Imaging of **extrasynaptic** glutamate transients in cerebellar and other slices, plus in vivo somatosensory cortex after tactile input. Distinguishes sensor `Kd_molecular` from estimated extrasynaptic `biological_concentration_range`. PMC HTML: L401C-EOS Kd = 1.57 μM; K716A-EOS Kd = 174 nM; five PF pulses at 100 Hz gave peak L401C-EOS signal corresponding to ≈2 μM glutamate; average extrasynaptic glutamate in a 50-ms window 1–8 μM depending on pulse number; FWHM of K716A-EOS signal ≈7 μm; in vivo 200-ms hind-paw stimulation produced extrasynaptic EOS signal in the corresponding cortex. Indicator >97% extrasynaptic by EM (not a cleft reporter).
- **full_text_inspected:** `yes` (PMC HTML)
- **access_route:** `pmc`
- **limitation:** EOS fluorescence-to-concentration conversion assumes in vitro calibration transfers to tissue (`transferable: unknown`). 100 Hz trains and 200 ms tactile stimuli are the imposed protocols, not the elementary single-vesicle cleft waveform. Kd values are **indicator** properties. Do not transfer ≈2 μM extrasynaptic train peaks to basal ambient (C04–C05) or to CSF/plasma.

**Extracted quantities (PMC HTML):**

| quantity_type | value | units | claim_tag | transferable | locator |
| --- | --- | --- | --- | --- | --- |
| Kd_molecular (K716A-EOS) | 174 | nM | primary-source-supported | no (indicator, not brain [glu]) | Results |
| Kd_molecular (L401C-EOS) | 1.57 | μM | primary-source-supported | no (indicator) | Results |
| biological_concentration_range (extrasynaptic peak, 5×100 Hz PF, L401C-EOS) | ≈2 | μM | primary-source-supported | unknown (calibration transfer) | Results |
| biological_concentration_range (extrasynaptic mean, 50-ms window, 1–5 pulses) | 1–8 | μM | primary-source-supported | unknown | Results |
| (stimulus timescale in vivo) | 200 | ms tactile pulse | primary-source-supported | no (protocol, not endogenous τ) | Results |
| EC50 (NMDAR, cited for interpretation) | ≈2 | μM | review-supported in this paper | no | Results |
| EC50 (mGluR, cited) | ≈10 | μM | review-supported in this paper | no | Results |
| EC50 (AMPAR, cited) | ≈500 | μM | review-supported in this paper | no | Discussion |

---

### C09 — Armbruster, Hanson, Dulla 2016

- **title:** Glutamate Clearance Is Locally Modulated by Presynaptic Neuronal Activity in the Cerebral Cortex.
- **year:** 2016
- **journal:** The Journal of Neuroscience
- **authors (PubMed):** Armbruster M; Hanson E; Dulla CG
- **DOI:** 10.1523/JNEUROSCI.2066-16.2016
- **PMID:** 27707974
- **PMCID:** PMC5050332
- **source_type:** `primary`
- **why it matters for THIS lane:** Shows that **clearance timescale is not a single number**: in adult mouse cortex, astrocytic glutamate uptake slows up to threefold after bursts ≥30 Hz, recovers within 50 ms, is independent of the amount released, and is synapse/input-specific even inside one astrocyte. That is a biological clearance timescale a sensor in neuropil would encounter, recorded with iGluSnFR imaging plus transporter currents. Prolonged NR2A NMDA decay is the neuronal readout of increased extracellular persistence — not an aptamer kinetic constant.
- **full_text_inspected:** `yes` (PMC HTML)
- **access_route:** `pmc`
- **limitation:** iGluSnFR kinetics filter the true free-glutamate waveform (see C10). Cortex slice after viral expression, not human CSF. “Up to threefold” and “<50 ms” are clearance-modulation descriptors, not aptamer `response_time`. Frequency threshold ≥30 Hz is for this preparation.

**Extracted quantities (PMC HTML / abstract):**

| quantity_type | value | units | claim_tag | transferable | locator |
| --- | --- | --- | --- | --- | --- |
| (clearance slowing after bursts) | up to 3-fold slower | — | primary-source-supported | no | abstract |
| (recovery of clearance after stimulation ceases) | within 50 | ms | primary-source-supported | no | abstract |
| (activity threshold for slowing) | ≥30 | Hz | primary-source-supported | no | abstract |

iGluSnFR here is the **measurement tool**; its `Kd_molecular` is not this paper’s reported brain concentration.

---

### C10 — Helassa et al. 2018

- **title:** Ultrafast glutamate sensors resolve high-frequency release at Schaffer collateral synapses.
- **year:** 2018
- **journal:** Proceedings of the National Academy of Sciences
- **authors (PubMed):** Helassa N; Dürst CD; Coates C; Kerruth S; Arif U; Schulze C; Wiegert JS; Geeves M; Oertner TG; Török K
- **DOI:** 10.1073/pnas.1720648115
- **PMID:** 29735711
- **PMCID:** PMC6003469
- **source_type:** `primary`
- **why it matters for THIS lane:** Places a **100 Hz** constraint on synaptic glutamate imaging: in rat hippocampal slice culture, iGlu_u resolves individual release events during 100 Hz trains and reports rapid cleft clearance between events. Also documents that even this ultrafast indicator **cannot** resolve the true free-cleft waveform (authors compare Clements τ = 1.2 ms vs later estimates closer to 100 μs). Indicator Kd values are **not** biological concentrations.
- **full_text_inspected:** `yes` (PMC HTML)
- **access_route:** `pmc`
- **limitation:** Slice culture Schaffer collaterals; iGlu_u `Kd_molecular` 600 μM and iGlu_f 137 μM are protein affinities in vitro. τ_off (9 ms iGluSnFR, 4 ms iGlu_f, 2 ms iGlu_u at 20 °C in vitro) is indicator `response_time`/`koff`-related, **not** biological cleft decay. Authors explicitly say iGlu_u still cannot resolve true cleft dynamics.

**Extracted quantities (PMC HTML):**

| quantity_type | value | units | claim_tag | transferable | locator |
| --- | --- | --- | --- | --- | --- |
| Kd_molecular (iGlu_f) | 137 | μM | primary-source-supported | no (indicator) | abstract |
| Kd_molecular (iGlu_u) | 600 | μM | primary-source-supported | no (indicator) | abstract |
| (in vitro τ_off iGluSnFR / iGlu_f / iGlu_u at 20 °C) | 9 / 4 / 2 | ms | primary-source-supported | no (indicator kinetics) | Results |
| (stimulus frequency resolved at boutons) | 100 | Hz | primary-source-supported | no (this synapse/sensor) | abstract |
| (biological interpretation: cleft cleared between 100 Hz events) | qualitative | — | primary-source-supported | no | abstract |
| (cleft decay, cited Clements 1992) | τ = 1.2 | ms | review-supported in this paper | no | Discussion |
| (cleft decay, cited modeling/anisotropy) | closer to 100 | μs | review-supported in this paper | no | Discussion |

Parent iGluSnFR usable up to ~10 Hz is this paper’s statement about **that indicator**, not about biology.

---

### C11 — Moussawi, Riegel, Nair, Kalivas 2011

- **title:** Extracellular glutamate: functional compartments operate in different concentration ranges.
- **year:** 2011
- **journal:** Frontiers in Systems Neuroscience
- **authors (PubMed):** Moussawi K; Riegel A; Nair S; Kalivas PW
- **DOI:** 10.3389/fnsys.2011.00094
- **PMID:** 22275885
- **PMCID:** PMC3254064
- **source_type:** `review`
- **why it matters for THIS lane:** Maps why **one glutamate number cannot serve all compartments**: OA HTML states plasma ~150 μM, CSF ~10 μM, intracellular ~10 mM (citing Danbolt 2001; Featherstone and Shippy 2008 — **not measured here**); cleft after AP >1 mM for <10 ms returning to <20 nM (citing Dzubay and Jahr 1999 — see limitation); tonic extrasynaptic estimates 0.02–30 μM depending on method. Microdialysis no-net-flux mostly 1–5 μM (range 1–30 μM); measurement interval >1 min. Speculative compartment cartoon (synaptic nM vs nonsynaptic low μM).
- **full_text_inspected:** `yes` (Europe PMC fullTextXML / OA HTML)
- **access_route:** `pmc`
- **limitation:** Review/speculation, not a new concentration assay. **Citation mismatch to flag for audit:** this review attributes “returns to <20 nM” to Dzubay and Jahr 1999; the Dzubay OA text inspected here estimates **extrasynaptic peaks 160–190 μM**, not a <20 nM basal. Nanomolar basal estimates belong to Herman/Chiu-type NMDAR work. Plasma 150 μM and CSF 10 μM are transferred from other reviews (`transferable: unknown`). Do not use this paper as primary `biological_concentration_range`.

**Extracted quantities (OA HTML; all review-level unless noted):**

| quantity_type | value | units | claim_tag | transferable | locator |
| --- | --- | --- | --- | --- | --- |
| biological_concentration_range (plasma, cited) | ~150 | μM | review-supported | unknown | opening paragraph |
| biological_concentration_range (CSF, cited) | ~10 | μM | review-supported | unknown | opening paragraph |
| biological_concentration_range (intracellular brain, cited) | ~10 | mM | review-supported | unknown | opening paragraph |
| biological_concentration_range (cleft after AP, cited) | >1 mM for <10 ms; <20 nM between events | mixed | review-supported; cleft <20 nM attribution to Dzubay 1999 is **unresolved** vs Dzubay OA text | no | opening paragraph |
| biological_concentration_range (tonic extrasynaptic, span of methods) | 0.02–30 | μM | review-supported | no (span, not a measurement) | opening paragraph |
| biological_concentration_range (microdialysis no-net-flux, majority) | 1–5 (reported span 1–30) | μM | review-supported | no | dialysis section |
| measurement_time (microdialysis, as stated here) | >1 | min | review-supported | no | dialysis section |

Abstract also gives tonic basal 0.02–20 μM (three orders of magnitude). Record both spans as the review’s own wording; do not collapse them.

---

### C12 — Hawkins 2009

- **title:** The blood-brain barrier and glutamate.
- **year:** 2009
- **journal:** The American Journal of Clinical Nutrition (PubMed: Am J Clin Nutr)
- **authors (PubMed):** Hawkins RA
- **DOI:** 10.3945/ajcn.2009.27462BB
- **PMID:** 19571220
- **PMCID:** PMC3136011
- **source_type:** `review`
- **why it matters for THIS lane:** Separates **plasma** vs **whole-brain tissue** vs **brain ECF** glutamate, and explains why plasma glutamate is not the brain interstitial `biological_concentration_range` (BBB tight junctions; abluminal EAATs). Abstract/PMC HTML: plasma 50–100 μmol/L; whole brain 10,000–12,000 μmol/L; ECF 0.5–2 μmol/L. Net glutamate entry to brain is not allowed; ECF is kept low. Circumventricular organs are exceptions (fenestrated capillaries).
- **full_text_inspected:** `yes` (PMC HTML; review, not a new HPLC table)
- **access_route:** `pmc`
- **limitation:** ECF 0.5–2 μmol/L **conflicts** with Herman/Chiu ~25 nM slice estimates and with Hashimoto/Madeira CSF micromolar HPLC values. Hawkins does not resolve method (dialysis vs NMDAR reporter vs lumbar CSF). Plasma 50–100 μmol/L is a review range, not this paper’s volunteer cohort. Umami symposium context; IGTC funding noted in PMC HTML. Do not transfer plasma or whole-brain tissue concentrations into the synaptic cleft.

**Extracted quantities (abstract + PMC HTML):**

| quantity_type | value | units | claim_tag | transferable | locator |
| --- | --- | --- | --- | --- | --- |
| biological_concentration_range (plasma) | 50–100 | μmol/L | review-supported | unknown | abstract |
| biological_concentration_range (whole brain tissue) | 10,000–12,000 | μmol/L | review-supported | no (tissue ≠ ECF) | abstract |
| biological_concentration_range (brain ECF, as stated here) | 0.5–2 | μmol/L | review-supported | no (conflicts with C04/C05) | abstract |

---

### C13 — Hashimoto et al. 2005

- **title:** Elevated glutamine/glutamate ratio in cerebrospinal fluid of first episode and drug naive schizophrenic patients.
- **year:** 2005
- **journal:** BMC Psychiatry
- **authors (PubMed):** Hashimoto K; Engberg G; Shimizu E; Nordin C; Lindström LH; Iyo M
- **DOI:** 10.1186/1471-244X-5-6
- **PMID:** 15683541
- **PMCID:** PMC548680
- **source_type:** `primary`
- **why it matters for THIS lane:** HPLC of **human lumbar CSF** glutamate and glutamine in first-episode drug-naive men vs age-matched healthy men. Control CSF glutamate: median 5.26 μM, mean 4.73 ± 1.29 μM, range 2.54–6.51 μM (n = 17). Patient glutamate was not significantly different; the glutamine/glutamate **ratio** was. This is CSF `biological_concentration_range`, not synaptic cleft or plasma.
- **full_text_inspected:** `yes` (Europe PMC full text)
- **access_route:** `pmc`
- **limitation:** Lumbar CSF ≠ cortical ECF ≠ cleft. Morning lumbar puncture, 12–18 mL, frozen; HPLC-fluorescence. Glutamine hydrolysis during handling can inflate glutamate (see C15 analytical contrast). Male-only, n = 17 controls. Authors cite ~10% CSF vs blood for neutral amino acids (not a glutamate measurement in this table). Do not use the schizophrenia ratio as a healthy reference.

**Extracted quantities (OA full text):**

| quantity_type | value | units | claim_tag | transferable | locator |
| --- | --- | --- | --- | --- | --- |
| biological_concentration_range (CSF glutamate, healthy men) | 4.73 ± 1.29 (median 5.26; range 2.54–6.51) | μM | primary-source-supported | no (lumbar CSF, this assay) | Results |
| biological_concentration_range (CSF glutamate, patients) | 4.25 ± 1.77 (median 4.17; range 2.22–8.88) | μM | primary-source-supported | no | Results |
| biological_concentration_range (CSF glutamine, healthy) | 405.6 ± 108.6 (median 410.5) | μM | primary-source-supported | no | Results |
| (glutamine/glutamate ratio, healthy vs patients) | 89.1 ± 22.5 vs 117.7 ± 27.4 | dimensionless | primary-source-supported | no | Results |

---

### C14 — Trabado et al. 2017

- **title:** The human plasma-metabolome: Reference values in 800 French healthy volunteers; impact of cholesterol, gender and age.
- **year:** 2017
- **journal:** PLoS One
- **authors (PubMed):** Trabado S; Al-Salameh A; Croixmarie V; Masson P; Corruble E; Fève B; Colle R; Ripoll L; Walther B; Boursier-Neyret C; Werner E; Becquemont L; Chanson P
- **DOI:** 10.1371/journal.pone.0173615
- **PMID:** 28278231
- **PMCID:** PMC5344496
- **source_type:** `primary`
- **why it matters for THIS lane:** Fasting **plasma** amino-acid reference values in 800 medication-free healthy French adults (Biocrates AbsoluteIDQ p180, LC-MS/MS). OA S1 table: L-glutamic acid mean ± SD **46.2 ± 21.4 μmol/L**, median 42.2, IQR [30.8; 58.7], extremes (9.12; 192.3), LLOQ 10.0 μmol/L, 0% not detected. L-glutamine 657.9 ± 106.2 μmol/L. This is plasma `biological_concentration_range`, not brain ECF.
- **full_text_inspected:** `yes` (PMC HTML of main text + OA S1 docx amino-acid table)
- **access_route:** `pmc`
- **limitation:** Targeted kit metabolomics, overnight-fasted venous EDTA plasma, not CSF or neuropil. Extreme plasma glutamate to 192.3 μmol/L is the table’s min/max, not a clinical reference interval. Do not transfer 46.2 μmol/L into the synaptic cleft or extrasynaptic space (BBB; C12). Glutamine ≫ glutamate in plasma; mixing them (MRS Glx) would mis-state this range.

**Extracted quantities (S1 table, inspected):**

| quantity_type | value | units | claim_tag | transferable | locator |
| --- | --- | --- | --- | --- | --- |
| biological_concentration_range (plasma L-glutamic acid, 800 HV) | 46.2 ± 21.4 (median 42.2) | μmol/L | primary-source-supported | no (plasma, this kit) | S1 Table |
| biological_concentration_range (plasma L-glutamine, 800 HV) | 657.9 ± 106.2 (median 652.9) | μmol/L | primary-source-supported | no | S1 Table |

Main text also states L-glutamine 0.66 mmol/L as most abundant amino acid and L-aspartic acid 6.7 μmol/L as least abundant — consistent with S1 (657.9 μmol/L glutamine; 6.26 ± 2.34 μmol/L aspartate).

---

### C15 — Alfredsson, Wiesel, Tylec 1988

- **title:** Relationships between glutamate and monoamine metabolites in cerebrospinal fluid and serum in healthy volunteers.
- **year:** 1988
- **journal:** Biological Psychiatry
- **authors (PubMed):** Alfredsson G; Wiesel FA; Tylec A  
  Crossref: Alfredsson, G.; Wiesel, F-A.; Tylec, A.
- **DOI:** 10.1016/0006-3223(88)90052-2
- **PMID:** 2453224
- **PMCID:** (empty)
- **source_type:** `primary`
- **why it matters for THIS lane:** Healthy-volunteer **CSF and serum** glutamate in the same 10 subjects, with HPLC glutamate and a stated low CSF value. Abstract: CSF glutamate 0.34 ± 0.14 nmol/ml (= 0.34 μM if 1 nmol/ml = 1 μM), n = 10; serum vs CSF glutamate r = 0.67, p < 0.05. The CSF number is an order of magnitude below Hashimoto 2005 / Madeira 2018 HPLC means — a method/handling discrepancy that must remain visible, not averaged.
- **full_text_inspected:** `partial` (PubMed abstract only; no PMC; publisher closed on free routes used)
- **access_route:** `abstract-only`
- **limitation:** n = 10. Absolute **serum** glutamate concentration is **not** in the inspected abstract (only the correlation). Do not fill serum from Hawkins or Trabado. The companion analytical paper PMID 3372631 (J Chromatogr 1988; no abstract in PubMed) was not OA-inspectable. Low CSF glutamate vs later HPLC studies is classically sensitive to glutamine-to-glutamate conversion in vitro — **unresolved** without the VoR methods. Not synaptic.

**Extracted quantities (abstract only):**

| quantity_type | value | units | claim_tag | transferable | locator |
| --- | --- | --- | --- | --- | --- |
| biological_concentration_range (CSF glutamate, healthy volunteers) | 0.34 ± 0.14 | nmol/ml | primary-source-supported | no | abstract |
| biological_concentration_range (serum glutamate, absolute) | (not stated in inspected abstract) | — | unresolved | — | — |
| (CSF–serum glutamate correlation) | r = 0.67, p < 0.05 | — | primary-source-supported | no | abstract |

---

## Inspected numbers that must not be collapsed

These are **not** one “affinity” or one “performance” number. They are different quantity types and compartments.

| Compartment / process | Order of inspected values | Quantity type | Must not be treated as |
| --- | --- | --- | --- |
| Synaptic cleft, phasic peak (C01) | 1.1 mM; decay τ 1.2 ms | biological_concentration_range + biological timescale | aptamer Kd, sensor LOD, response_time |
| Cleft buffering (C02) | hundreds of μs | biological timescale | transport-cycle time; aptamer koff |
| Extrasynaptic peak at Bergmann glia (C03) | 160–190 μM; cited >10 ms elevation | biological_concentration_range + timescale | ambient basal; CSF |
| Ambient slice / NAc (C04, C05) | ~25 nM (Herman); 25.6 nM (Chiu) | biological_concentration_range | microdialysis μM; plasma |
| Extrasynaptic imaged transients (C08) | ≈2 μM peak; 1–8 μM in 50 ms window; 100 Hz trains | biological_concentration_range + protocol timescale | indicator Kd; basal ambient |
| Clearance plasticity (C09) | ≤3× slower after ≥30 Hz; recover <50 ms | biological timescale | aptamer response_time |
| High-frequency cleft imaging (C10) | 100 Hz events resolved; indicator τ_off 2–9 ms | mixed biology vs indicator | free-cleft 100 μs estimates |
| Plasma (C12 review; C14 primary) | 50–100 μmol/L (review); 46.2 ± 21.4 μmol/L (800 HV) | biological_concentration_range | brain ECF |
| Lumbar CSF (C13 vs C15) | ~4.7 μM (Hashimoto controls) vs 0.34 μM (Alfredsson) | biological_concentration_range | cortical ECF; cleft |
| Hawkins ECF (C12) | 0.5–2 μmol/L | biological_concentration_range (review) | Herman 25 nM; do not average |
| Whole-brain tissue (C12) | 10–12 mmol/L | tissue content | extracellular range |
| Indicator Kd (C08, C10) | 174 nM–600 μM depending on construct | Kd_molecular of reporter | brain [glu] |

---

## Method disagreement to keep open (not a thesis)

- **Nanomolar ambient (NMDAR reporters in slices: C04, C05, related C06)** vs **micromolar microdialysis/biosensor (reviewed in C11; 1–4 μM cited in C04)** vs **Hawkins review ECF 0.5–2 μM (C12)**. Chiu 2017 tested and did not find a micromolar non-synaptic reservoir in NAc slices when EAATs were blocked. Moussawi 2011 offers a compartment hypothesis. These remain **unresolved** as a single extracellular number.
- **CSF HPLC:** Alfredsson 0.34 μM vs Hashimoto ~5 μM vs Madeira 2018 healthy-control mean 6.16 ± 3.19 μmol/L (OA Table 1 inspected; paper not in the 15 because it is a disease-elevation study — listed under near-misses). Do not average.
- **Cleft time course:** C01 1.2 ms τ vs C10’s citation of later ~100 μs estimates vs C02 submillisecond buffering vs C03/Bergles extrasynaptic elevation for many milliseconds. Different synapses and different inferred vs simulated quantities.

No statement is made here about aptamer adequacy for any of these clocks.

---

## Identifiers attempted but not verified, or not usable as OA full text

| Identifier / lead | What happened |
| --- | --- |
| Unpaywall `https://api.unpaywall.org/v2/{doi}` | HTTP 422 for every DOI tried with a placeholder email. OA status taken from PMCID / Europe PMC / live PMC HTML instead. |
| PMID 24728863 | Retrieved during a Zhou/Danbolt search; it is Calvey et al. 2014 *Curr Genet* (Lipomyces transformation) — **wrong paper**. Zhou & Danbolt 2014 is PMID **24578174** / PMC4133642 (inspected as wildcard review, not one of the 15). |
| “Moussawi … From the synaptic cleft to the extrasynaptic space” | 0 PubMed hits. Actual title is C11. |
| PMID 15695241 Cavelier & Attwell 2005 *J Physiol* “Tonic release of glutamate…” | Metadata verified (DOI 10.1113/jphysiol.2004.082131). Europe PMC `isOpenAccess: N`, no PMCID. Not inspected beyond metadata. Near-miss for ambient glutamate. |
| PMID 9329159 Timmerman & Westerink 1997 *Synapse* | Metadata verified. No PMCID. Abstract inspected: argues microdialysis GABA/glutamate is largely non-exocytotic and poorly represents synaptic leakage. Closed VoR. |
| PMID 11369436 Danbolt 2001 *Prog Neurobiol* “Glutamate uptake” | Metadata verified. Review, no PMCID. Heavily cited by C11/C12; VoR not inspected. |
| PMID 8723198 Clements 1996 *Trends Neurosci* | Metadata + abstract verified (peak 1–5 mM; biphasic ~100 μs and ~2 ms). No PMCID. Abstract-only. |
| PMID 10736372 Meldrum 2000 *J Nutr* | Metadata verified. Oxford HTML 403 in this environment. |
| PMID 3372631 Alfredsson et al. 1988 *J Chromatogr* | Metadata verified; PubMed has **no abstract**. No PMC. |
| PMID 23287559 Akiyama et al. 2014 *Brain Dev* CSF/plasma ratios in children | Metadata + abstract verified (glutamate CSF/plasma ratio higher in older children). No PMC. |
| PMID 40433056 Ercan et al. 2025 plasma FAA biological variation | OA HTML inspected; glutamic acid **means** not given in body text (CVs only). Not nominated. |
| PMID 22778802 Featherstone 2010 *ACS Chem Neurosci* | PMC3368625 HTML inspected (vesicular glutamate “100 mM or more”; cleft “several millimolar”; EAAT block “0.5–5 uM to several hundred micromolar” — those ranges are cited, not new assays). Not in the 15 (review overlapping C11/C12). |
| J Neurosci and PNAS **publisher** HTML | HTTP 403. PMC HTML used instead where PMCID exists. |
| Science 1992 C01 publisher HTML | Not obtained. Abstract only. |

DOI/PMID/PMCID triples above for C01–C15 were cross-checked PubMed esummary ↔ Crossref works. No unresolved title/year clash except the Le Meur / “Meur, Karim Le” author-order parsing already noted.

---

## Wildcard / near-miss sources examined (not in the 15)

| Paper | Why examined | Why not a 15th candidate (or how used) |
| --- | --- | --- |
| Zhou & Danbolt 2014 PMID 24578174 PMC4133642 | Healthy-brain glutamate review; serum 50–200 μM cited (Zlotnik); brain 5–15 mmol/kg | Overlaps C12; numbers are cited. Full text inspected (`yes`, pmc). |
| Madeira et al. 2018 PMID 30459657 PMC6232456 | Human CSF glutamate HPLC with healthy controls | Disease paper. **Inspected Table 1:** control glutamate 6.16 (3.19) μmol/L; AD 17.28 (1.99); MDD 16.31 (3.81); hydrocephalus 9.05 (2.06). Supports CSF micromolar HPLC cluster vs Alfredsson. |
| Bergles, Dzubay, Jahr 1997 PMID 9405697 PMC25121 | Extrasynaptic time course at Bergmann glia | Overlaps C03. PMC HTML: extrasynaptic glutamate persists >10 ms; peak much lower than 1–3 mM cleft. |
| Herman, Nahir, Jahr 2011 PMID 22069455 PMC3206024 | Tests privileged synaptic vs extrasynaptic ambient in CA1 | Complements C04/C05; ambient too low to activate significant NMDARs in spines **or** shafts. Kept out to avoid three Jahr-lab ambient papers in 15. |
| Otis, Wu, Trussell 1996 PMID 8774432 | Delayed clearance at a calyx-type synapse | Different architecture. Abstract: final 10–100 μM removed over tens of ms. PMC record thin. |
| Heit et al. 2023 PMID 36321247 PMC10107724 | Tonic glutamate / system x_c^− and ischemia | Wildcard source of **tonic** glutamate; pathology-leaning. Metadata verified; not extracted. |
| Aggarwal et al. 2023 PMID 37142767 PMC10250197 | iGluSnFR3 faster synaptic imaging | Indicator engineering; C10 already covers high-frequency optical timescales. |
| Scimemi & Beato 2009 PMID 19844813 PMC2777263 | How concentration profiles are inferred | Methods review; Europe PMC XML inspected. Not a concentration table. |

---

## Inference boundary (lane only; no poster thesis)

**Measured in the 15 (examples):** antagonist-displacement cleft waveform (C01); transporter effects in the first few hundred microseconds (C02); Bergmann-glia extrasynaptic peak estimate 160–190 μM (C03); NMDAR-reported ambient ~25 nM in hippocampus and NAc (C04, C05); tonic NMDAR current of glial origin (C06); CA1 synapse spacing ~465 nm (C07); EOS extrasynaptic ≈2 μM peaks and in vivo tactile responses (C08); activity-dependent clearance slowing (C09); 100 Hz optical events at Schaffer boutons (C10); HPLC CSF glutamate in healthy men (C13); LC-MS/MS plasma glutamic acid in 800 HV (C14); HPLC CSF glutamate 0.34 μM in 10 HV (C15).

**Inferred, not directly assayed:** in vivo ambient nanomolar (suggested in C04); micromolar extrasynaptic “nonsynaptic” compartments (C11 model); Hawkins ECF 0.5–2 μM; Rusakov neighbor-synapse occupancy (depends on D\*); EOS/iGluSnFR concentration calibrations in tissue.

**Unknown / unresolved:** a single extrasynaptic basal concentration; a single CSF glutamate reference; true free-cleft decay (1.2 ms vs ~100 μs vs many-ms extrasynaptic tails at glia); plasma-to-ECF mapping; any aptamer kinetic comparison (not in this lane).

**Falsifiers that would change this lane’s map (proposed, not claimed):** a primary in vivo method that reports both cleft-millimolar transients and NMDAR-defined ambient in the same preparation without probe trauma; CSF HPLC with documented glutamine-stability controls matching Alfredsson and Hashimoto on the same samples; extrasynaptic chemical (not receptor) calibration that is independent of indicator Kd.

**High-information next source for extractors (not done here):** double-extract C01 (if OA appears), C03, C04, C05, C08, C13, C14, C15; citation-audit C11’s Dzubay “<20 nM” sentence against C03 VoR.

---

## Orchestrator merge notes

- Promote **nothing** to `core`.
- Deduplicate by DOI then PMID.
- Do not write `state/claims.csv` from this file without an extractor.
- If Clements 1996 (PMID 8723198) is added later, it is a **review** of cleft timecourse (abstract: peak 1–5 mM; biphasic ~100 μs and ~2 ms) and must not overwrite C01’s primary 1.1 mM / 1.2 ms without tagging.

---

## End of scout-05 record
