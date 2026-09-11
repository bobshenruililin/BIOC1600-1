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

## Subagent concurrency and wave scheduling

Observed failure (Mission 1): the runtime async ceiling is 10 delegated agents. Launching more than that returns `Async subagent limit of 10 reached`. Those launch errors are **not** scientific results. They do not mean a lane was searched and found empty.

Policy for this project:

- Maximum **8** concurrently active delegated agents, including premium-model subagents. Leave headroom for recovery or system delegation.
- Schedule work in sequential waves of at most 8. Do not start the next wave until the current wave has returned or been marked failed-to-launch.
- After each wave, commit or otherwise preserve important artifacts before launching the next.
- Re-run only missing work. Do not duplicate successfully completed work merely to restore symmetry. Do not reduce the intellectual scope of a failed launch.
- When tournament isolation requires independence, a later wave must not be given earlier-wave conclusions (or paths that contain them).
- Premium review begins only after the evidence it is meant to review is complete.
- Do not close a science gate until every required research lane has completed or is explicitly documented as genuinely blocked (not launch-capped).

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

## Research Effort Standard

This project rewards changes in understanding, not completion speed or output volume.

Do not stop because a plausible answer has been found.

For any load-bearing scientific question, the research process is incomplete until the applicable items below have been addressed:

1. **Best supporting case**
   Identify the strongest primary evidence supporting the current interpretation.

2. **Best opposing case**
   Search deliberately for evidence that weakens, contradicts, or limits it.

3. **Context**
   Determine whether apparently conflicting studies differ in construct, experimental system, matrix, timescale, endpoint, or biological regime.

4. **Inference boundary**
   State separately:
   - what was measured;
   - what was inferred;
   - what remains unknown.

5. **Falsifier**
   State what observation or experiment would materially weaken the current conclusion.

6. **High-information next step**
   Identify the experiment, analysis, or source most likely to change our understanding.

7. **Independent thought**
   Load-bearing conclusions require independent review by an agent that did not see the originating agent's reasoning before generating its own assessment.

8. **Wildcard exploration**
   For major missions, investigate at least one scientifically plausible direction not specified by the parent prompt.
   Do not manufacture novelty.
   If no useful result emerges, record which direction was examined and why it was rejected.

9. **Negative-search integrity**
   “No evidence found” is not sufficient by itself.
   Record enough of the search strategy, terminology, source chains, and near-misses to establish what was actually investigated.

10. **Do not optimize for agreement**
    A valid counterexample or fatal flaw outweighs majority consensus.

11. **Do not optimize for volume**
    Ten redundant papers are less valuable than one decisive experiment.

12. **Do not optimize for speed**
    Finishing early is not a success metric.

13. **Do not pad work**
    Extra words, agents, searches, or computations that cannot plausibly alter an inference are not additional rigor.

14. **Completion is not acceptance**
    An agent may finish a mission whose gate status is REVISE or FAIL.
    Never weaken acceptance criteria merely to obtain PASS.

## Before Closing a Major Mission

The orchestrator must answer:

- What did we believe before this mission?
- What changed?
- What surprised us?
- What was tested and rejected?
- What important uncertainty remains?
- Which result most threatens our preferred thesis?
- Which result most strengthens it?
- What is the highest-information next action?
- What work was not done, and why was it judged low value?
- Is another research round likely to change a decision?

If these questions cannot be answered substantively, the mission is not ready for closure.

## Validation

```bash
python3 scripts/check_structure.py
python3 scripts/validate_ledgers.py
python3 scripts/forbid_pdfs.py
python3 -m unittest discover -s tests -v
```
