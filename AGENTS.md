# BIOC1600 aptamer research swarm

Founding operating manual for the HKU BIOC1600 Topic 1 swarm on aptamer-based biosensors.

Provisional scientific question (must be tested, not assumed):

> Can an aptamer actually keep up with neurochemical signaling? What do affinity, selectivity, binding kinetics, sensor transduction, immobilization and biological context jointly determine about the usefulness of a glutamate aptamer biosensor?

Do not force the slogan “aptamer quality is not a single number.” If verified evidence supports a better thesis, return that thesis and the evidence that displaced the original.

This repository’s desired handoff is `reports/nightly_summary.md`, not a finished poster.

## Model configuration

Use only recorded Cursor Grok IDs in `state/model_config.json`.

- Parent / default worker: `cursor-grok-4.6-xhigh`
- Do not invent `grok-4.7` or any other identifier
- `-fast` variants are allowed only for high-volume extraction/merge

## What workers may not modify

Workers may propose prompt or workflow edits. They may not modify:

- scientific acceptance criteria
- source-verification standards
- scoring weights
- safety rules
- definitions of experimental versus computational evidence
- final human approval requirements

Those files are hash-locked in `state/LOCKED_FILES.sha256`. CI fails if they change without an explicit entry in `state/decisions.md`.

## Specialist agents

Project subagents live in `.cursor/agents/`. Research/review agents are `readonly: true` and return structured records. The orchestrator writes ledgers.

| Agent | File | Writes? |
| --- | --- | --- |
| literature-scout | `.cursor/agents/literature-scout.md` | no |
| evidence-extractor | `.cursor/agents/evidence-extractor.md` | no |
| contradiction-hunter | `.cursor/agents/contradiction-hunter.md` | no |
| citation-auditor | `.cursor/agents/citation-auditor.md` | no |
| aptamer-biochemist | `.cursor/agents/aptamer-biochemist.md` | no |
| sensor-engineer | `.cursor/agents/sensor-engineer.md` | no |
| quant-modeler | `.cursor/agents/quant-modeler.md` | isolated worktree only |
| poster-red-team | `.cursor/agents/poster-red-team.md` | no |
| meta-improver | `.cursor/agents/meta-improver.md` | `rounds/meta/` only |

If a custom agent type is not registered in the Task tool, run `generalPurpose` with that file’s prompt pasted verbatim and `model: cursor-grok-4.6-xhigh`.

## Isolation

- Swarm branch: `cursor/research-swarm-634f`
- Analysis implementations: separate branches and git worktrees (`cursor/analysis-<name>-634f`)
- Two writers never share a working tree
- Thesis-tournament agents must not see one another’s proposals during generation
- At least one thesis candidate must **challenge the current framing** rather than refine it (observed Round 3 failure: 4/4 isolated writers collapsed to the same “cannot claim neurodynamics” sentence). Adopted after one meta A/B on that observed collapse.

## Evidence rules (summary)

Full text: `.cursor/rules/research-constitution.mdc`

- Every substantive scientific claim is tagged as one of: `primary-source-supported`, `review-supported`, `computational illustration`, `hypothesis`, `proposed experiment`, `unresolved`
- Never invent citations, DOI/PMID, affinities, LODs, dynamic ranges, sample sizes, response times, or experimental validation
- Do not treat a source as verified merely because another agent cites it
- Never transfer properties across aptamer constructs, surface vs solution, buffers, or sensor architectures unless the cited experiment supports it
- Computational docking or predicted structures are hypothesis-generating only unless experimentally validated
- Distinguish: molecular Kd, kon, koff, EC50, sensor LOD, analytical working range, signal gain, response time, measurement/interrogation time, biological concentration range

## Poster freeze

Forbidden: polished/final poster, PowerPoint, Canva, Figma, Illustrator, print-ready 90×120 cm artwork.

Allowed: `poster/theses.md` and markdown storyboards (panel title, claim, evidence IDs, figure idea).

## Round protocol

0. Bootstrap (this tree). No science claims. No core sources.
1. Six isolated literature scouts. Candidates only.
2. Double extraction of top papers, citation audit, contradiction hunt. Promote claims only when evidential status is clear.
3. Four isolated thesis proposals; two red-team scorings; discard below 75; finalists at 85+.
4. At least six analysis proposals; implement top two in isolated worktrees.
5. Independent clean-checkout replication; reject unreproducible or overstated figures.
6. Bounded meta-improvement: A/B patches, frozen benchmark, stop at six meta rounds or two consecutive gains under two percentage points.

Nightly deliverable: `reports/nightly_summary.md` with the 13 required sections. Do not report planned work as completed.

## Validation

```bash
python3 scripts/check_structure.py
python3 scripts/validate_ledgers.py
python3 scripts/forbid_pdfs.py
python3 -m unittest discover -s tests -v
```
