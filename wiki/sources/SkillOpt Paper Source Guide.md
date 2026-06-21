---
title: >-
  SkillOpt Paper Source Guide
category: sources
type: source
status: draft
tags: [paper, arxiv, agents, skills, optimization]
sources:
  - https://arxiv.org/abs/2605.23904
  - https://arxiv.org/pdf/2605.23904
  - conversation:2026-06-11
created: 2026-06-11T11:00:54+0800
updated: 2026-06-11T11:00:54+0800
summary: >-
  Primary-paper guide for SkillOpt, preserving its controllable text-space optimizer for agent skills, validation gate, rejected-edit memory, slow/meta update, experiments, transfer, and limitations.
provenance:
  extracted: 0.82
  inferred: 0.16
  ambiguous: 0.02
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-06-11
aliases:
  - SkillOpt
  - SkillOpt paper
  - SkillOpt primary paper
---

# SkillOpt Paper Source Guide

> Source: *SkillOpt: Executive Strategy for Self-Evolving Agent Skills*, arXiv:2605.23904v2, submitted 2026-05-22 and revised 2026-05-25.

## Capture Policy

This page preserves the primary-paper layer for SkillOpt. It should be used for paper-grounded claims about the method, reported numbers, ablations, transfer experiments, learned artifacts, and limitations.

It complements [[wiki/sources/SkillOpt Paper River Source Guide]], which preserves the paper-river problem lineage from ReAct, Reflexion, text optimization, GEPA, and skill-evolution systems into SkillOpt. The paper-river page explains the historical problem line; this page preserves what the SkillOpt paper itself claims and tests.

## What It Covers

SkillOpt treats an agent skill document as trainable external state for a frozen target model. Instead of changing weights, adding inference-time calls, or rewriting a prompt ad hoc, it repeatedly runs the target model with the current skill, collects scored trajectories, asks a separate optimizer model to propose bounded text edits, and accepts a candidate skill only if it improves a held-out selection score.

The paper belongs in the wiki because it sharpens [[wiki/concepts/Skill Self-Evolution]] into a governed update loop. A skill is not just a reusable instruction bundle; it becomes an artifact that can be trained, validated, rejected, transferred, audited, and deployed as `best_skill.md`. This directly connects [[wiki/concepts/Agent Skill]], [[wiki/topics/AI Skills Workflow]], [[wiki/concepts/Verification Loop]], and [[wiki/maps/Self-Evolving Agents Map]].

## Preserved Content

### Problem Statement

Agent skills package procedures, domain heuristics, tool policies, output constraints, and failure modes. They adapt a frozen agent through external text rather than through weight updates.

The paper argues that current skill creation paths are unstable:

- hand-written skills depend on human prior knowledge and may not match the target domain or harness;
- one-shot model-generated skills do not reliably improve after observing failures;
- loosely controlled self-revision can make large semantic jumps, erase useful rules, or accumulate plausible but harmful edits;
- trajectory-to-skill systems can mine lessons but often lack a held-out acceptance gate.

SkillOpt's central question is therefore not "can an LLM write a skill?" but "how should a reusable skill document be optimized under feedback?"

### Core Idea

SkillOpt makes the deep-learning analogy operational:

```text
weight parameter       -> skill document
gradient direction     -> trajectory-derived edit direction
learning rate          -> textual edit budget
validation check       -> held-out selection gate
training history       -> rejected-edit buffer and slow/meta update
deployment artifact    -> compact best_skill.md
```

The target model and execution harness remain fixed. A separate optimizer model reads scored rollouts and proposes structured add/delete/replace edits. A textual learning-rate budget limits how much the skill can change at one step. The candidate skill is evaluated on a held-out selection split; only strict improvement is accepted.

### Method Loop

SkillOpt has a training-style outer loop:

```text
current skill
  -> rollout batch with frozen target model
  -> success and failure trajectories
  -> optimizer reflection over minibatches
  -> candidate add/delete/replace edits
  -> rank and clip under edit budget
  -> candidate skill
  -> held-out validation gate
  -> accept as current/best skill or reject and remember failure
```

The *forward pass* is rollout evidence. The target model runs tasks using the current skill, while the harness records task metadata, messages, tool calls, observations, command outputs, final answers, verifier feedback, and benchmark-specific context.

The *backward pass* is minibatch reflection. The optimizer separates failures from successes. Failure minibatches propose missing or corrective rules; success minibatches preserve behaviors that already work. The paper emphasizes this because single trajectories can produce anecdotal fixes, while minibatches expose reusable procedural errors.

The *bounded update* is the textual learning-rate mechanism. Instead of allowing whole-skill rewrites, SkillOpt ranks candidate edits and clips them to a scheduled budget. Patch mode uses localized append, insert, replace, and delete operations; rewrite mode exists as an alternative but is not the main stability story.

The *validation gate* turns reflection into propose-and-test optimization. Candidate skills must improve over the current selection score. Rejected edits are not discarded as useless text; they become negative feedback for later optimizer calls in the same epoch.

The *slow/meta update* stores longer-horizon regularities. Local skill edits capture fast procedural corrections, while a protected slow-update field and optimizer-only meta skill preserve what seems stable across an epoch. This keeps deployment compact while allowing training to accumulate history.

### Default Deployment Shape

The deployed output is a compact `best_skill.md` skill file, roughly 300-2,000 tokens in the reported runs. It adds no optimizer calls at inference time. Training cost is paid before deployment; deployment only prepends or loads the optimized skill artifact.

### Benchmarks, Models, and Harnesses

The main study covers six benchmarks:

- SearchQA
- SpreadsheetBench
- OfficeQA
- DocVQA
- LiveMathematicianBench
- ALFWorld

It evaluates seven target models, including frontier GPT variants and smaller Qwen models, and three execution modes:

- direct chat, where the skill is prepended to the model context;
- Codex harness, where the current skill is rendered to task workspaces and execution traces are read back;
- Claude Code harness, using the same broad workspace contract.

Baselines include no skill, human-written skills, one-shot LLM skills, Trace2Skill, TextGrad, GEPA, and EvoSkill.

### Headline Results

The headline claim is broad: SkillOpt is best or tied-best on all 52 evaluated model/benchmark/harness cells.

On GPT-5.5 in direct chat, the paper reports:

| Benchmark | No Skill | SkillOpt | Gain |
| --- | ---: | ---: | ---: |
| SearchQA | 77.7 | 87.3 | +9.6 |
| SpreadsheetBench | 41.8 | 80.7 | +38.9 |
| OfficeQA | 33.1 | 72.1 | +39.0 |
| DocVQA | 78.8 | 91.2 | +12.4 |
| LiveMathematicianBench | 37.6 | 66.9 | +29.3 |
| ALFWorld | 83.6 | 95.5 | +11.9 |

The GPT-5.5 average gain is +23.5 points in direct chat, +24.8 points inside the Codex loop, and +19.1 points inside the Claude Code loop.

The paper also reports that SkillOpt beats an oracle that selects the best per-cell competitor among six competing methods by +5.4 points on the GPT-5.5 direct-chat average.

### Ablations

The ablations argue that the main gains are not a fragile batch-size artifact. SearchQA saturates early, while more procedural tasks benefit from more training evidence: SpreadsheetBench rises from 47.5 to 78.0 and LiveMathematicianBench from 59.1 to 70.5 as the optimizer sees 1% to 100% of the training partition.

The most important components are:

- bounded text-space learning, which prevents uncontrolled rewrites;
- held-out validation gating, which blocks plausible but harmful edits;
- rejected-edit feedback, which gives the optimizer negative memory;
- epoch-wise slow/meta update, which preserves long-horizon direction.

The paper reports that removing the rejected-edit buffer drops SpreadsheetBench from 77.5 to 72.9 in the relevant ablation. Removing both meta skill and slow update is more damaging, dropping SpreadsheetBench from 77.5 to 55.0. These results support the claim that stability comes from governance of edits, not from reflection text alone.

### Transfer

SkillOpt's transfer experiments ask whether the learned skill is a reusable artifact rather than a benchmark-specific prompt.

Cross-model transfer is positive in all reported non-identical source-target rows. For example, a SpreadsheetBench skill trained on GPT-5.4 transfers to GPT-5.4-mini with +9.4 over that target model's no-skill baseline, recovering much of the in-domain gain.

Cross-harness transfer is the clearest deployment signal. A SpreadsheetBench skill trained inside Codex transfers to Claude Code with +59.7 over the Claude Code no-skill baseline, moving 22.1 to 81.8. The reverse Claude-Code-to-Codex transfer adds +43.6, moving 27.5 to 71.1.

Cross-benchmark transfer is smaller but positive in the reported OlympiadBench-to-Omni-MATH rows across three target models.

### Learned Artifacts

The final skills are small and editable. Across six benchmarks, final `best_skill.md` artifacts range from 379 tokens to 1,995 tokens, with a median around 920 tokens.

The edit economy is striking: only 1-4 accepted bounded updates survive into the final skill. LiveMathematicianBench's +29.3 point gain over no skill comes from one accepted edit; OfficeQA's +39.0 point gain also comes from one accepted edit. The optimizer proposes many more edits during training, but most die at the gate.

The learned rules are procedural rather than instance-specific. Examples in the paper include:

- SpreadsheetBench: inspect workbook structure and formulas, then write evaluated static values across the full requested target range instead of relying on Excel recalculation.
- DocVQA: bind the question to the exact visual row, header, or field before copying the aligned answer span.
- ALFWorld: keep a visited/frontier ledger, diversify search after repeated same-type failures, and avoid revisiting the destination until holding the target.

These examples matter because they show the optimized artifact learning domain procedure, not memorizing individual answers.

### Qualitative Skill Evolution

In ALFWorld, the initial skill is a generic search-transform-place household plan. Accepted edits make it more stateful: exact object-name matching, visited-location memory, destination memory, pick-two progress locks, and direct completion rules. In the representative run, held-out test performance improves from 49.3 to 74.6.

In SpreadsheetBench, the initial skill already says to use Python spreadsheet libraries and preserve unrelated workbook content. Accepted edits turn this into workbook forensics: inspect the real workbook rather than previews, locate headers and ranges across sheets, normalize keys and cell types, preserve formatting, and write evaluated static values when the grader reads cell values.

### Limitations and Caveats

The method depends on selection split quality. If the held-out gate is not representative, SkillOpt can select rules that overfit the selection distribution. This is especially important when a skill is meant to serve many future task families. ^[inferred]

The optimizer only sees what the harness records. If traces omit the real cause of failure, the optimizer can propose edits that diagnose the wrong mechanism. ^[inferred]

The paper's analogy to deep-learning optimization is useful but not mathematically equivalent. Textual edit budgets behave like learning rates only at the operational level; they do not guarantee smoothness of the skill-to-behavior landscape. ^[inferred]

Deployment is cheap, but training may still be expensive. The paper reports cost-per-point regimes from 0.6M-46.4M training tokens per absolute test-point gain, depending on benchmark trajectory length and context richness.

## Integration Decisions

This page should be the primary link for factual claims about SkillOpt's algorithm, benchmarks, ablations, and reported numbers.

[[wiki/sources/SkillOpt Paper River Source Guide]] should remain the source for lineage claims: how the problem evolves from ReAct, Reflexion, text optimization, GEPA, and prior skill-evolution systems toward skill-change governance.

SkillOpt strengthens [[wiki/concepts/Skill Self-Evolution]] in a specific direction: skill evolution should be governed like a change process. The stable concept is not merely "skills can improve themselves"; it is that a skill update needs evidence, bounded change, held-out acceptance, rejected-change memory, and deployment separation.

SkillOpt also extends [[wiki/concepts/Verification Loop]]. Verification is not only used to judge whether the current task succeeded; it is used to decide whether a change to future default behavior should survive.

The paper is adjacent to [[wiki/sources/Skills-Coach Paper Source Guide]] and [[wiki/sources/SkillOS Paper Source Guide]]. Skills-Coach emphasizes boundary-task generation and comparative execution for one skill; SkillOS trains repository-level skill curation; SkillOpt focuses on optimizing one persistent skill document with validation-gated text edits.

## Open Questions

- How representative must the held-out selection split be for skill changes to remain useful across future tasks?
- How should SkillOpt detect regressions when one skill is shared by many task families?
- Can the rejected-edit buffer become stale if the skill distribution shifts after several accepted edits?
- What happens when multiple skills interact and an edit improves one skill but changes routing, precedence, or conflicts in a skill repository? ^[inferred]
- Can human reviewers inspect accepted edits cheaply enough for high-risk domains, or does validation score become the de facto reviewer? ^[inferred]

## Related

- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Skill Self-Evolution]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/maps/Self-Evolving Agents Map]]
- [[wiki/sources/SkillOpt Paper River Source Guide]]
- [[wiki/sources/GEPA Paper River Source Guide]]
- [[wiki/sources/Skills-Coach Paper Source Guide]]
- [[wiki/sources/SkillOS Paper Source Guide]]
