# BIOC1600 aptamer research swarm

Founding operating manual for the HKU BIOC1600 Topic 1 swarm on aptamer-based biosensors.

Provisional scientific question (must be tested, not assumed):

> Can an aptamer actually keep up with neurochemical signaling? What do affinity, selectivity, binding kinetics, sensor transduction, immobilization and biological context jointly determine about the usefulness of a glutamate aptamer biosensor?

Do not force the slogan “aptamer quality is not a single number.” If verified evidence supports a better thesis, return that thesis and the evidence that displaced the original.

This repository’s desired handoff is `reports/mission3_entry.md` (Mission 3 front door) plus `reports/nightly_summary.md` (PI nightly). Not a finished poster.

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
- Live Mission-2/3 vehicle: `cursor/m2-int-honesty-245a` ([PR 32](https://github.com/bobshenruililin/BIOC1600-1/pull/32), draft, not merged). Mission 3 starts at `reports/mission3_entry.md`, not on the historical swarm branch.
- Analysis implementations: separate branches and git worktrees (`cursor/analysis-<name>-634f`)
- Two writers never share a working tree
- Thesis-tournament agents must not see one another’s proposals during generation
- At least one thesis candidate must **challenge the current framing** rather than refine it (observed Round 3 failure: 4/4 isolated writers collapsed to the same “cannot claim neurodynamics” sentence). Adopted after one meta A/B on that observed collapse.

## Swarm Scheduling and Concurrency

The project has effectively unlimited Grok inference budget but limited simultaneous subagent capacity.

Treat these as separate resources.

Spawn agents until the next agent is more likely to repeat an existing line of reasoning than uncover a new one. That stopping rule is independent of how many agents can run at once.

Observed ceiling (Mission 1): launching more than about **10** delegated agents returns `Async subagent limit of 10 reached`. Those errors are orchestration failures, not empty searches.

### Concurrency

- Never intentionally exceed **8 concurrently active delegated subagents**.
- The observed system ceiling is approximately 10; the project ceiling of 8 preserves recovery and orchestration headroom.
- Premium-model agents count toward the same concurrency budget.
- Do not launch another wave until sufficient slots from the prior wave have completed.
- Do not respond to abundant inference budget by maximizing simultaneous concurrency.

### Waves

Large research programs should run as sequential waves.

Typical pattern:

**Wave A — independent generation**
6–8 agents investigate the hard question independently.

**Wave B — orthogonal exploration**
6–8 agents investigate alternative mechanisms, counterexamples, missing evidence, or wildcard directions.

**Wave C — adversarial discrimination**
4–8 agents receive candidate conclusions and attempt to distinguish among them.

**Wave D — senior review**
1–2 premium reviewers inspect original evidence and candidate reports.

A mission may contain many total agent runs. Only simultaneous execution is limited.

### Independence

When blind independence is required:

- later independent agents must not receive earlier conclusions;
- the orchestrator may provide the same source corpus and task specification;
- do not contaminate independent generation with consensus summaries.

### Failure recovery

A launch or capacity error is an orchestration failure, not a scientific result.

When a subagent fails to start:

1. record the failed task;
2. allow running agents to finish;
3. preserve their work;
4. requeue only the missing task in a later wave;
5. do not restart successfully completed work.

Do not shrink the intellectual scope of a failed launch. Do not close a science gate until every required research lane has completed or is explicitly documented as genuinely blocked (not launch-capped). Premium review begins only after the evidence it is meant to review is complete.

When an agent fails after producing partial work, inspect and preserve useful artifacts before deciding whether to resume or rerun it.

### Nested agents

Do not allow ordinary worker subagents to spawn additional research swarms unless the mission explicitly calls for hierarchical delegation.

Prefer top-level orchestration so concurrency, independence and provenance remain observable.

### Checkpointing

After every substantial wave:

- preserve completed outputs;
- update mission state;
- record failures;
- record unresolved disagreements;
- commit important artifacts when appropriate.

Do not depend on temporary subagent state as the sole copy of research work.

### Optimization target

Optimize:

**scientific information gained per wave**

not:

**number of agents simultaneously running**.

Stop adding agents to a wave when the next one is more likely to repeat an existing line of reasoning than uncover a new one.

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

Mission 2/3 note: Rounds 0–6 above are the overnight bootstrap protocol (historical). Mission 2 froze at REVISE with QUANTITATIVE FLAGSHIP NONE; highest-information experiment is locked U2. Mission 3 entry is `reports/mission3_entry.md` with storyboard `poster/storyboards/mission3.md`. READY FOR MISSION 3: YES after the 2026-09-12 PI decision in `state/decisions.md`. Gate stays REVISE. Not group-final. Do not reopen Mission 2. Do not manufacture PASS.

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
