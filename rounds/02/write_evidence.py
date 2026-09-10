#!/usr/bin/env python3
"""Write Round 2 core evidence and claims from double extraction + audit.

Only rows where extractors A and B agree on source, construct, quantity type
family, and numerical result. Quantity-type label conflicts are recorded in notes.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

EVIDENCE_FIELDS = [
    "evidence_id",
    "source_id",
    "extractor_id",
    "system",
    "aptamer_construct",
    "experimental_manipulation",
    "comparator",
    "quantity_type",
    "numerical_result",
    "units",
    "matrix",
    "limitation",
    "locator",
    "full_text_inspected",
]

CLAIMS_FIELDS = [
    "claim_id",
    "claim_text",
    "evidential_status",
    "source_id",
    "locator",
    "quantity_type",
    "value",
    "units",
    "construct",
    "system",
    "transferable",
    "notes",
]

# Consensus rows: extractor_id records A+B agreement.
EVIDENCE = [
    ["E001", "S001", "A+B", "Capture-SELEX of glutamic-acid-selective ssDNA", "aptamer 1d04", "Capture-SELEX in complex medium", "", "Kd_molecular", "12", "µM", "complex medium (unspecified in abstract)", "Abstract only; VoR closed. Not glu1. Not a sensor LOD.", "PubMed/Europe PMC abstract", "no"],
    ["E002", "S001", "A+B", "Gold E-AB; ACV; MCH backfill", "truncated glu1; 3'-ferrocene; Au-thiol", "ACV characterization", "1d04 is a different construct", "sensor_LOD", "0.0013", "pM", "LOD matrix not specified in abstract; selectivity mentioned in 10-fold diluted human serum", "Abstract only. glu1 sensor LOD not 1d04 Kd.", "PubMed/Europe PMC abstract", "no"],
    ["E003", "S001", "A+B", "Gold E-AB; ACV; MCH backfill", "truncated glu1; 3'-ferrocene; Au-thiol", "ACV characterization", "", "analytical_working_range", "0.01 pM–1 nM", "span", "range matrix not specified in abstract", "Abstract only. glu1 range not 1d04 Kd. Units field records that the span mixes pM and nM.", "PubMed/Europe PMC abstract", "no"],
    ["E004", "S002", "A+B", "AuED-MEA E-AB; ACV; Langmuir-Freundlich fit", "Glu-apt Fc-tagged truncated sequence on electrode", "electrochemical isotherm", "cited solution Kd 12 µM from Wu 2022 not remeasured", "EC50", "1.8", "nM", "PBS electrochemical assay", "Apparent electrochemical Kd. Extractor B labeled Kd_molecular; A labeled EC50. Consensus: not solution molecular Kd. 2D confinement noted by authors.", "Hu 2025 section 3.2", "yes"],
    ["E005", "S002", "A+B", "AuED-MEA E-AB; ACV", "Glu-apt Fc-tagged", "LOD = blank mean + 3 SD", "ST 8 pM; DA 0.41 µM", "sensor_LOD", "32", "pM", "PBS", "Glutamate channel buffer LOD. Not Wu 0.0013 pM.", "Fig. 4h; section 3.2", "yes"],
    ["E006", "S002", "A+B", "AuED-MEA E-AB; ACV", "Glu-apt Fc-tagged", "standard addition", "PBS LOD 32 pM", "sensor_LOD", "51.5", "pM", "50% human serum", "Main-text report of Fig. S11.", "section 3.4", "yes"],
    ["E007", "S002", "A+B", "AuED-MEA E-AB; ACV", "Glu-apt Fc-tagged", "semi-log calibration", "", "analytical_working_range", "0.1 nM–10 µM", "span", "PBS", "Semi-log window; r=0.99. Mixed nM/µM span recorded in numerical_result.", "Fig. 4e; section 3.2", "yes"],
    ["E008", "S002", "A+B", "AuED-MEA E-AB; ACV", "Glu-apt Fc-tagged", "incubation before ACV", "DA 10 min; ST 15 min (Fig. 3f is ST, not Glu)", "measurement_time", "15", "min", "PBS", "Assay wait after adding Glu, not synaptic response time. Orchestrator re-verified OA PDF 2026-09-10: Glu 15 min / DA 10 min (section 3.2; Fig. S8).", "section 3.2; Fig. S8", "yes"],
    ["E009", "S003", "A+B", "Kinetic ITC of DNA aptamers vs small molecules", "various DNA aptamers (not glutamate in abstract)", "kon/koff vs Kd survey", "", "Kd_molecular", "28 nM–864 µM", "span", "", "Abstract range across aptamers. Not glutamate. VoR closed. Mixed nM/µM span.", "PubMed/Europe PMC abstract", "no"],
    ["E010", "S003", "A+B", "Kinetic ITC of DNA aptamers vs small molecules", "various DNA aptamers", "kon vs Kd trend", "", "kon", "2e5 to 96", "M^-1 s^-1", "", "Abstract endpoints. Not a single construct. Not glutamate.", "abstract", "no"],
    ["E011", "S003", "A+B", "Kinetic ITC of DNA aptamers vs small molecules", "various DNA aptamers", "koff vs Kd trend", "", "koff", "1.03e-3 to 0.012", "s^-1", "", "Abstract endpoints. Not glutamate.", "abstract", "no"],
    ["E012", "S004", "A+B", "E-AB IPA flow injection; 8e12 probes/cm2; 12 mL/min", "parent tobramycin aptamer HS-C6-...-MB", "kobs vs [T] slope", "SPR (nonspecific)", "kon", "3.5e4", "M^-1 s^-1", "tris buffer", "Tobramycin not glutamate. Surface-bound.", "Fig. 3; PMC13101946", "yes"],
    ["E013", "S004", "A+B", "E-AB IPA flow injection", "parent tobramycin aptamer", "dissociation-phase fit", "", "koff", "1.39", "s^-1", "tris buffer", "Tobramycin not glutamate.", "Fig. 3", "yes"],
    ["E014", "S004", "A+B", "E-AB IPA flow injection", "parent tobramycin aptamer", "Kd,kinetic = koff/kon", "equilibrium 46±6 µM", "Kd_molecular", "41±11", "µM", "tris buffer", "Surface kinetic Kd. Tobramycin.", "Abstract; Fig. 3", "yes"],
    ["E015", "S004", "A+B", "E-AB IPA flow injection", "parent tobramycin aptamer", "Langmuir Ieq isotherm", "kinetic 41±11 µM", "Kd_molecular", "46±6", "µM", "tris buffer", "Surface equilibrium Kd. Tobramycin.", "Abstract; Fig. 3", "yes"],
    ["E016", "S004", "A+B", "IPA 1 ms pulses 0 to -0.4 V", "MB-labeled tobramycin aptamer", "IPA waveform", "SWV seconds-scale", "measurement_time", "2", "ms", "", "Interrogation time not binding equilibration.", "Introduction; Methods", "yes"],
    ["E017", "S006", "A+B", "Gold TFBG-SPR fiber; SARS-CoV-2 N protein", "thiolated Apt48", "fiber concentration-response 0.05-2.5 µM", "DNT-Apt48", "EC50", "0.3981", "µM", "", "Apparent fiber Kd. N-protein not glutamate. B labeled Kd_molecular.", "Fig. 4D", "yes"],
    ["E018", "S006", "A+B", "Gold TFBG-SPR fiber; N protein", "DNT-Apt48 DNA tetrahedron + Apt48", "fiber concentration-response", "Apt48 alone", "EC50", "0.1996", "µM", "", "Apparent fiber Kd. Interface evidence only.", "Fig. 4D", "yes"],
    ["E019", "S006", "A+B", "TFBG-SPR", "Apt48 vs DNT-Apt48", "N-protein 0.4-2.5 µM", "Apt48 alone", "signal_gain", "2 to 2.5", "fold", "", "Abstract ~2.5 times; body 2-2.5 fold.", "Abstract; Fig. 4C-D", "yes"],
    ["E020", "S006", "A+B", "TFBG-SPR real-time", "10 µM Apt48 or DNT-Apt48", "2.5 µM N protein until plateau", "", "response_time", "25", "min", "", "N-protein fiber plateau. Not glutamate neurotransmission.", "Fig. 4B", "yes"],
    ["E021", "S007", "A+B", "SPR; LOX1 on chip", "InstructNA G1L", "SPR n=3", "HT-SELEX T1L 23.1 nM", "Kd_molecular", "12.9", "nM", "DPBS + 5 mM MgCl2 (B)", "LOX1 protein not glutamate. Generated sequences also include non-binders.", "Fig. 2b", "yes"],
    ["E022", "S007", "A+B", "SPR; CXCL5", "InstructNA G1C", "SPR n=3", "HT-SELEX T1C 18.3 nM", "Kd_molecular", "6.6", "nM", "DPBS + 5 mM MgCl2 (B)", "CXCL5 not glutamate.", "Fig. 2c", "yes"],
    ["E023", "S007", "A+B", "HT-SELEX then SPR", "top-frequency vs InstructNA-generated sets", "fraction strong binders KD<=100 nM", "", "", "", "", "", "Qualitative SPR counts, not a listed quantity type. HT-SELEX top-frequency: 2 (LOX1) and 1 (CXCL5) strong. InstructNA generated 10 sequences/target: 4 strong LOX1 (G1L-G4L) and 3 strong CXCL5 (G1C-G3C). Remaining weak or no binding.", "Fig. 2; Supplementary Tables 3-6", "yes"],
    ["E024", "S021", "A+B", "SPR of screened aptamers", "glutamate aptamer (Table S1 SI)", "SPR", "DA 20 nM; 5-HT 10.5 nM; HIS 15 nM", "Kd_molecular", "293", "nM", "", "SPR Kd not FET LOD. Sequence in SI.", "main text; Fig. S6", "yes"],
    ["E025", "S021", "A+B", "CNT FET; 0.1x PBS", "glutamate aptamer on AuNP/CNT FET", "practical LOD for four NTs", "SPR Kd 293 nM", "sensor_LOD", "10", "fM", "0.1x PBS", "Not 1x aCSF. Not in vivo. Do not transfer SPR Kd onto LOD.", "Fig. 3; abstract", "yes"],
    ["E026", "S021", "A+B", "CNT FET glutamate channel", "glutamate aptamer FET", "Ids vs concentration", "DA/ST/HIS 10 fM-100 µM", "analytical_working_range", "10 fM–100 nM", "span", "0.1x PBS", "Glutamate-specific figure span. Mixed fM/nM recorded in numerical_result.", "Fig. 3f caption", "yes"],
    ["E027", "S021", "A+B", "CNT FET real-time multiplex", "four NT aptamers", "stabilize after 10 nM target", "", "response_time", "200", "s", "0.1x PBS pH 7.4", "Not millisecond. Reset is a separate pH step.", "Fig. 5e", "yes"],
    ["E028", "S033", "A+B", "Cocaine E-AB ACV", "cocaine aptamer HS-C6-...-MB", "signal gain vs packing density", "", "signal_gain", "60 to 200", "%", "1x SSC", "Cocaine not glutamate. Max ~200% at 1.6e12 /cm2.", "Abstract; Fig. 4", "yes"],
    ["E029", "S033", "A+B", "Cocaine E-AB hyperbolic fits", "cocaine aptamer; 25/60/500 nM fabrication", "apparent sensor Kd vs density", "cited solution Kd ~100 µM", "EC50", "327±64; 101±8; 127±35", "µM", "1x SSC", "Surface apparent Kd. B labeled Kd_molecular.", "Fig. 3 caption", "yes"],
    ["E030", "S033", "A+B", "Cocaine E-AB DPV stirred", "high-density cocaine aptamer ~4e12 /cm2", "100 µM cocaine injection", "thrombin 11-20 min", "response_time", "4", "s", "1x SSC", "Upper bound: faster than 4 s scan dead time.", "Fig. 6 left", "yes"],
    ["E031", "S033", "A+B", "Thrombin E-AB", "thrombin aptamer; 5.8e11 vs 1.3e13 /cm2", "750 nM thrombin equilibration", "", "response_time", "11 to 20", "min", "thrombin Tris buffer", "Density slows protein-target equilibration. Fig. 6 caption rates conflict with minute-scale text; used body 11-20 min.", "Sensor Equilibrium Time; Fig. 6", "yes"],
    ["E032", "S049", "A+B", "Cultured hippocampal synapses; NMDA antagonist displacement", "not an aptamer", "kinetic inference of cleft free glutamate", "", "biological_concentration_range", "1.1", "mM", "synaptic cleft (culture)", "Abstract only. Inference not chemical assay.", "PubMed abstract", "no"],
    ["E033", "S049", "A+B", "same cleft inference", "not an aptamer", "decay time constant", "", "response_time", "1.2", "ms", "synaptic cleft (culture)", "Biological clearance tau NOT sensor response_time. Quantity type is the closest allowed field.", "PubMed abstract", "no"],
    ["E034", "S050", "A+B", "Tonic NMDAR current; acute hippocampal slice", "not an aptamer; NMDARs as reporters", "efficacy-scaled ambient glutamate", "cited dialysis 1-4 µM", "biological_concentration_range", "25", "nM", "acute hippocampal slice; intact transport", "Ambient extracellular estimate. Auditor: paper does not use the word extrasynaptic. Not cleft peak.", "Abstract; Discussion", "yes"],
    ["E035", "S050", "A+B", "Nucleated-patch glutamate dose-response", "NMDARs on CA1 somata", "Hill fit", "NMDA EC50 37.7 µM", "EC50", "1.8", "µM", "nucleated patches", "Receptor EC50 not aptamer Kd. Orchestrator re-verified PMC2670936 HTML.", "Fig. 2C", "yes"],
    ["E036", "S002", "orchestrator-reverify", "AuED-MEA E-AB sequence table", "Glu-apt Fc 5'-HS-C6-GCATCAGTCCACTCGTGAGGTCGACTGATGAGGCTCGAT-Fc-3'", "authors cite Wu 2022 Kd", "Hu electrochemical apparent Kd 1.8 nM", "Kd_molecular", "12", "µM", "cited solution-phase (not remeasured here)", "Citation of Wu, not a Hu measurement of the truncated Fc-thiol surface construct.", "Experimental section sequences", "yes"],
    ["E037", "S054", "orchestrator-reverify", "GlutOx ceramic MEA in freely moving rat CNS", "not an aptamer; glutamate oxidase enzyme stack", "chronic second-by-second Glu", "", "response_time", "500–800", "ms", "freely moving rat CNS", "Enzyme electrode, not aptamer. PMC3482110 HTML 2026-09-10.", "Introduction / abstract phrasing on PMC HTML", "yes"],
    ["E038", "S055", "orchestrator-reverify", "Modeled GlutOx Pt electrode stack", "not an aptamer", "continuum model vs cited experiment", "experimental 0.8 ± 0.2 s (their ref 24)", "response_time", "0.73", "s", "model of enzyme biosensor", "Simulated response time 0.73 s matching experimental 0.8 ± 0.2 s. Prior hunter missed this sentence. Not t90 labeled in the inspected sentence. Not an aptamer.", "PMC5881573 HTML; model results paragraph", "yes"],
    ["E039", "S062", "orchestrator-reverify", "iGluSnFR vs transporter/synaptic current", "not an aptamer; fluorescent indicator", "waveform vs free glutamate lifetime", "", "response_time", "10–100", "fold longer than free Glu lifetime", "brain tissue / simulations as stated", "Indicator waveform is not free [Glu]. Buffering by iGluSnFR delays uptake. PMC7255799 XML.", "Results/abstract phrasing in Europe PMC XML", "yes"],
    ["E040", "S010", "orchestrator-reverify", "Graphene FET; NG-Apt-Glu", "in silico designed DNA aptamer NG-Apt-Glu", "aCSF calibration claimed in abstract", "", "sensor_LOD", "1", "aM", "artificial cerebrospinal fluid", "Preprint abstract only this session. ELONA millimolar Kd was not in the abstract and is not entered. Not peer-reviewed.", "bioRxiv/Europe PMC abstract", "partial"],
    ["E041", "S010", "orchestrator-reverify", "Graphene FET; NG-Apt-Glu", "NG-Apt-Glu", "claimed linear range in abstract", "", "analytical_working_range", "1 aM–10 pM", "span", "artificial cerebrospinal fluid", "Preprint abstract. Do not treat as validated molecular Kd.", "bioRxiv/Europe PMC abstract", "partial"],
]

CLAIMS = [
    ["C001", "Capture-SELEX isolate 1d04 binds glutamate with Kd 12 µM in the indexed abstract.", "primary-source-supported", "S001", "PubMed abstract", "Kd_molecular", "12", "µM", "1d04 (not glu1)", "Capture-SELEX / complex medium", "no", "VoR closed. Do not transfer onto glu1 or Hu Glu-apt."],
    ["C002", "Truncated surface-bound glu1 E-AB reports LOD 0.0013 pM by ACV in the indexed abstract.", "primary-source-supported", "S001", "PubMed abstract", "sensor_LOD", "0.0013", "pM", "glu1 Fc-thiol-MCH", "gold E-AB", "no", "Different construct from 1d04. Matrix of LOD vs serum selectivity not separable from abstract."],
    ["C003", "Kd and LOD in Wu 2022 are not interchangeable affinity numbers.", "hypothesis", "S001", "abstract construct split", "", "", "", "1d04 vs glu1", "glutamate aptasensor paper", "no", "Load-bearing interpretation. Confirmed as construct split by citation auditor."],
    ["C004", "Hu 2025 glutamate MEA channel LOD is 32 pM in PBS and 51.5 pM in 50% serum.", "primary-source-supported", "S002", "Fig. 4h; section 3.4", "sensor_LOD", "32 (PBS); 51.5 (50% serum)", "pM", "Glu-apt on AuED-MEA", "ACV multiplex MEA", "no", "Double-extracted from OA PDF. Not Wu 0.0013 pM."],
    ["C005", "Hu 2025 glutamate electrochemical apparent Kd is 1.8 nM (Langmuir-Freundlich), distinct from cited 12 µM solution value.", "primary-source-supported", "S002", "section 3.2", "EC50", "1.8", "nM", "surface Glu-apt", "PBS ACV", "no", "Authors note 2D confinement. Not solution Kd."],
    ["C006", "Hu 2025 glutamate assay uses 15 min incubation before ACV.", "primary-source-supported", "S002", "section 3.2", "measurement_time", "15", "min", "Glu-apt", "MEA ACV", "no", "Cannot support millisecond neurotransmission."],
    ["C007", "No glutamate aptamer kon/koff were found in inspected glutamate sensor papers.", "unresolved", "S001", "Round 2 search of glutamate sensor sources", "kon", "", "", "glutamate DNA aptamers", "E-AB / SPR / ITC", "no", "Absence of evidence across S001/S002/S010/S021. Tobramycin IPA and mixed-aptamer ITC must not be substituted. source_id S001 is the primary glutamate aptamer paper searched, not a kon measurement."],
    ["C008", "Surface-bound tobramycin aptamer IPA: kon 3.5e4 M^-1 s^-1, koff 1.39 s^-1, Kd,kinetic 41±11 µM.", "primary-source-supported", "S004", "Fig. 3 PMC13101946", "kon", "3.5e4", "M^-1 s^-1", "tobramycin parent aptamer", "E-AB IPA tris buffer", "no", "Not glutamate. Shows IPA can measure surface kon/koff when mass transport is controlled."],
    ["C009", "IPA interrogation can be 2 ms; that clock is measurement_time not binding koff.", "primary-source-supported", "S004", "Methods", "measurement_time", "2", "ms", "tobramycin E-AB", "IPA", "no", "Do not equate 2 ms interrogation with synaptic 1.2 ms cleft clearance."],
    ["C010", "Small-molecule aptamer ITC survey: both kon and koff change with Kd (kon 2e5 to 96 M^-1 s^-1; koff 1.03e-3 to 0.012 s^-1 over Kd 28 nM to 864 µM).", "primary-source-supported", "S003", "Europe PMC abstract", "kon", "2e5 to 96", "M^-1 s^-1", "various DNA aptamers", "solution ITC", "no", "Abstract only; VoR closed. Not glutamate. Per-construct tables not inspected."],
    ["C011", "Inferred peak cleft glutamate 1.1 mM decaying with tau 1.2 ms at cultured hippocampal synapses.", "primary-source-supported", "S049", "PubMed abstract", "biological_concentration_range", "1.1", "mM", "not aptamer", "cultured hippocampal synapses", "unknown", "Kinetic inference not chemical assay. VoR closed."],
    ["C012", "Ambient extracellular glutamate in hippocampal slice is about 25 nM by tonic NMDAR current.", "primary-source-supported", "S050", "abstract; discussion", "biological_concentration_range", "25", "nM", "not aptamer", "acute hippocampal slice", "no", "Auditor: not an extrasynaptic-only measurement. Contrasts cited dialysis 1-4 µM."],
    ["C013", "A 1:1 Langmuir isotherm spans 81-fold between 10% and 90% occupancy, so one Kd cannot cover both 25 nM tonic and 1.1 mM cleft glutamate.", "review-supported", "S030", "Rousseau 2023 PMC10750225", "analytical_working_range", "81", "fold (10-90% occupancy)", "generic E-AB Langmuir", "perspective", "yes", "Theoretical Langmuir property. Tonic/cleft numbers are from C012/C011, not measured in Rousseau."],
    ["C014", "Xiao 2025 glutamate SPR Kd is 293 nM while FET practical LOD is 10 fM in 0.1x PBS.", "primary-source-supported", "S021", "Fig. 3; SPR paragraph", "Kd_molecular", "293", "nM", "glutamate aptamer (SI sequence)", "SPR vs CNT FET", "no", "Buffer is 0.1x PBS. Response stabilize 200 s. Not in vivo."],
    ["C015", "DNA tetrahedron display of Apt48 increased N-protein fiber signal 2-2.5 fold and halved apparent fiber Kd vs Apt48 alone.", "primary-source-supported", "S006", "Fig. 4", "signal_gain", "2 to 2.5", "fold", "DNT-Apt48 vs Apt48", "TFBG-SPR N-protein", "no", "Interface evidence. Not glutamate."],
    ["C016", "InstructNA generated some stronger SPR binders than top-frequency HT-SELEX clones for LOX1/CXCL5, but most generated sequences were not strong binders.", "primary-source-supported", "S007", "Fig. 2", "Kd_molecular", "12.9 (best G1L)", "nM", "InstructNA G1L", "SPR protein targets", "no", "Hypothesis-generating for glutamate. Not a glutamate aptamer."],
    ["C017", "Predicted aptamer structures and docking scores failed to recover experimental theophylline vs caffeine selectivity.", "computational illustration", "S046", "full text", "", "", "", "theophylline DNA aptamer models", "docking benchmark", "no", "Primary computational benchmark vs crystals; experimental selectivity is cited not remeasured."],
    ["C018", "E-AB packing density and SAM chemistry change signal gain and apparent Kd (cocaine/thrombin).", "primary-source-supported", "S033", "Figs. 3-4, 7", "signal_gain", "60 to 200", "%", "cocaine E-AB", "ACV 1x SSC", "no", "Not glutamate. Immobilization is not a null operation."],
    ["C019", "Park 2023 table row labeled Glutamate FET is Plasmodium falciparum GDH (Singh 2019 PMID 30308419), not neurotransmitter glutamate.", "primary-source-supported", "S023", "Table 1 vs ref 59", "", "", "", "review table error", "Biosensors 2023 review", "no", "Citation auditor: supports_claim=no for using Park as Glu NT sensor evidence."],
    ["C020", "No verified in vivo glutamate aptamer sensor among Round 1-2 sources; in vivo aptamer FETs demonstrated for serotonin and dopamine.", "unresolved", "S018", "Zhao 2021; Wu Nano Lett 2022", "", "", "", "serotonin/dopamine FETs", "in vivo", "no", "Scope limit not a measured glutamate negative result."],
    ["C021", "Hu 2025 lists Glu-apt Kd = 12 µM citing Wu 2022; that value is a citation, not a Hu remeasurement of the Fc-thiol truncated surface construct.", "primary-source-supported", "S002", "Experimental section sequences", "Kd_molecular", "12", "µM", "Glu-apt sequence as used by Hu, Kd label from Wu citation", "AuED-MEA methods", "no", "Do not collapse this 12 µM with Hu electrochemical apparent Kd 1.8 nM."],
    ["C022", "Rutherford 2007 GlutOx MEA reports subsecond 500-800 ms response time in freely moving rats.", "primary-source-supported", "S054", "PMC3482110 HTML", "response_time", "500–800", "ms", "not aptamer; glutamate oxidase", "freely moving rat CNS", "no", "Enzyme comparator. Still ~1000-fold slower than 1.2 ms cleft tau."],
    ["C023", "Clay 2018 reports a simulated GlutOx response time of 0.73 s matching experimental 0.8 ± 0.2 s.", "primary-source-supported", "S055", "PMC5881573 HTML model paragraph", "response_time", "0.73", "s", "not aptamer", "enzyme-electrode model", "no", "Simulation plus cited experiment. Not synaptic milliseconds. Round-2 hunter had incorrectly said 0.73-0.8 s was absent."],
    ["C024", "iGluSnFR fluorescence time courses often last 10-100 times longer than the extracellular lifetime of synaptically released glutamate, in part because the indicator buffers glutamate.", "primary-source-supported", "S062", "Europe PMC full text XML PMC7255799", "response_time", "10–100", "fold", "not aptamer; iGluSnFR", "brain / simulations as in paper", "no", "Shows even protein glutamate sensors can report a filtered waveform. Not an aptamer kinetic."],
    ["C025", "Abrantes 2025 preprint abstract claims 1 aM glutamate LOD in aCSF on a graphene FET with computationally designed NG-Apt-Glu.", "primary-source-supported", "S010", "bioRxiv abstract", "sensor_LOD", "1", "aM", "NG-Apt-Glu", "graphene FET; aCSF", "no", "Preprint. In silico design. Do not enter unverified ELONA millimolar Kd. Not a substitute for kon/koff."],
    ["C026", "Hu 2025 Glu-apt sequence is a truncated Fc- and thiol-modified oligo; authors themselves contrast electrochemical apparent Kd with cited solution-phase values because of 2D confinement.", "primary-source-supported", "S002", "section 3.2", "", "", "", "surface Glu-apt vs cited solution Kd", "PBS ACV", "no", "Supports construct/interface non-transfer. The confinement explanation is the authors' interpretation."],
]


CORE = {
    "S001",
    "S002",
    "S003",
    "S004",
    "S006",
    "S007",
    "S021",
    "S023",
    "S030",
    "S033",
    "S046",
    "S049",
    "S050",
    "S054",
    "S055",
    "S062",
}

RELEVANT = {
    "S005",
    "S008",
    "S010",
    "S011",
    "S014",
    "S017",
    "S018",
    "S019",
    "S022",
    "S024",
    "S025",
    "S028",
    "S029",
    "S034",
    "S036",
    "S038",
    "S041",
    "S043",
    "S045",
    "S051",
    "S058",
    "S060",
    "S061",
    "S063",
    "S064",
}

REJECTED = {
    "S013": "Peptide aptamer, not a nucleic-acid aptamer; out of BIOC1600 nucleic-acid scope for this thesis.",
}


def promote_sources() -> None:
    path = ROOT / "state/sources.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    for row in rows:
        sid = row["source_id"]
        if sid in CORE:
            row["status"] = "core"
            row["rejection_reason"] = ""
        elif sid in RELEVANT:
            row["status"] = "relevant"
            row["rejection_reason"] = ""
        elif sid in REJECTED:
            row["status"] = "rejected"
            row["rejection_reason"] = REJECTED[sid]
        # else leave candidate
        if sid == "S002":
            row["full_text_inspected"] = "yes"
            row["access_route"] = "oa-pdf-rwth"
            row["notes"] = (
                "PMID 40992279 confirmed. Orchestrator re-read CC-BY VoR 2026-09-10. "
                "Glu electrochemical apparent Kd 1.8 nM; PBS LOD 32 pM; 50% serum LOD 51.5 pM; "
                "Glu incubation 15 min. Cited Wu 12 µM is not a Hu remeasurement."
            )
        if sid == "S050":
            row["notes"] = (
                "Tonic/ambient extracellular glutamate near 25 nM in acute hippocampal slice. "
                "Paper uses ambient/baseline, not extrasynaptic as its own claim. Contrasts dialysis 1-4 µM."
            )
        if sid == "S055":
            row["full_text_inspected"] = "yes"
            row["access_route"] = "pmc"
            row["notes"] = (
                "GlutOx model. Simulated response 0.73 s matches experimental 0.8 ± 0.2 s. "
                "Not an aptamer. Clay 2021 is a separate simulation paper."
            )
        if sid == "S010":
            row["full_text_inspected"] = "partial"
            row["notes"] = (
                "Preprint. Abstract claims 1 aM LOD in aCSF. ELONA millimolar Kd not in abstract; not entered."
            )
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(
        "sources core={0} relevant={1} rejected={2}".format(
            sum(1 for r in rows if r["status"] == "core"),
            sum(1 for r in rows if r["status"] == "relevant"),
            sum(1 for r in rows if r["status"] == "rejected"),
        )
    )


def main() -> None:
    ev_path = ROOT / "research/evidence/core_evidence.csv"
    with ev_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=EVIDENCE_FIELDS)
        writer.writeheader()
        for row in EVIDENCE:
            writer.writerow(dict(zip(EVIDENCE_FIELDS, row)))
    cl_path = ROOT / "state/claims.csv"
    with cl_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CLAIMS_FIELDS)
        writer.writeheader()
        for row in CLAIMS:
            writer.writerow(dict(zip(CLAIMS_FIELDS, row)))
    promote_sources()
    print(f"evidence={len(EVIDENCE)} claims={len(CLAIMS)}")


if __name__ == "__main__":
    main()
