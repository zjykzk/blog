---
title: >-
  Agentic Reasoning for LLMs Paper Source Guide
category: references
type: source
status: draft
tags: [paper, arxiv, agents, reasoning, survey]
sources:
  - https://arxiv.org/pdf/2601.12538
  - /Users/zenk/Documents/notes/20260621T114118--paper-agentic-reasoning__paper.org
  - /Users/zenk/Documents/notes/20260621T132501--qa-agentic-reasoning__qa.org
created: 2026-06-21T13:32:21+0800
updated: 2026-06-21T13:32:21+0800
summary: >-
  Source guide for arXiv 2601.12538, treating agentic reasoning as reasoning joined to action, feedback, memory, learning, and multi-agent coordination.
provenance:
  extracted: 0.94
  inferred: 0.06
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-06-21
aliases:
  - Agentic Reasoning for Large Language Models
  - Agentic Reasoning Paper
  - 智能体推理论文
---

# Agentic Reasoning for LLMs Paper Source Guide

> Source: Tianxin Wei et al., *Agentic Reasoning for Large Language Models: Foundations, Evolution, Collaboration*, arXiv 2601.12538v1.

## What It Covers

This paper is a survey of agentic reasoning for large language models. It frames the shift from static LLM reasoning to agentic reasoning as a shift from *generating an answer inside a fixed prompt* to *using reasoning to organize perception, planning, action, feedback, memory, learning, and collaboration*.

The source is best read as a roadmap rather than an experimental paper. It does not introduce a new model or report a new benchmark win. Its value is the organizing frame: agentic reasoning sits across three environmental layers and two optimization modes.

## Core Claim

The paper's central claim is that reasoning becomes agentic when it drives an interactive loop rather than only producing a text answer.

In a static task, the model receives a problem and emits an answer. In an agentic task, the model must observe, plan, act, inspect feedback, update state, and choose the next action. This turns reasoning into a control signal for [[wiki/concepts/Agentic Control Loop]], not merely a chain-of-thought style output.

A compact reading:

```text
static reasoning: prompt -> answer
agentic reasoning: observation -> reasoning -> action -> feedback -> memory/update -> next action
```

This supports the existing wiki view that an [[wiki/concepts/Agent]] is a control-loop system rather than merely a model with tools.

## Three Layers of Agentic Reasoning

The paper organizes agentic reasoning by environmental dynamics:

- *Foundational agentic reasoning* covers single-agent capabilities in relatively stable environments: planning, tool use, and search.
- *Self-evolving agentic reasoning* covers feedback, memory, and adaptation across episodes, so the agent can improve through experience rather than restart from the same state every time.
- *Collective multi-agent reasoning* covers role assignment, communication, shared memory, collaboration, and group-level coordination.

This three-layer map is useful because many systems are all called “agents” even when they sit at different complexity levels. A tool-using single agent, a memory-updating self-improving agent, and a multi-agent organization are not the same object. They differ in failure modes, evaluation needs, and governance burden.

## Two Optimization Modes

Across all three layers, the paper distinguishes two ways to improve reasoning behavior:

- *In-context reasoning* scales test-time interaction without changing model parameters. Examples include orchestration, search, tool use, structured workflows, and adaptive prompting.
- *Post-training reasoning* internalizes reasoning strategies into model weights through supervised fine-tuning or reinforcement learning.

The engineering distinction is:

```text
in-context orchestration = behavior guided at runtime
post-training optimization = behavior learned into the model
```

This distinction connects to [[wiki/topics/AI Harness]]: some capabilities should live in the harness as runtime orchestration, while repeated stable behaviors may deserve consolidation into skills, memory, training data, or model behavior. ^[inferred]

## Benchmark and Evidence Landscape

The survey's evidence is mostly cartographic: it collects systems, applications, and benchmarks rather than running a new unified experiment.

Representative benchmark scale from the reading notes:

- ToolQA has 1,530 dialogues and 13 specialized tools.
- APIBench covers 1,645 real APIs and 16,450 instruction-API pairs.
- ToolBench collects 16,464 real APIs across 49 categories.
- MTU-Instruct contains 54,798 dialogues involving 136 tools.
- LONGMEMEVAL pushes multi-session dialogue history up to 1.5M tokens.
- MemBench contains 60K episodes.
- MineLand supports up to 64 agents in Minecraft-style multi-agent settings.
- TeamCraft has 55,000 procedurally generated collaborative tasks.

These numbers show the evaluation frontier moving away from “is the final answer correct?” toward “can the system select tools, maintain memory, coordinate agents, and remain auditable across long interactions?” ^[inferred]

## Key Insight Preserved from the Reading

The strongest distilled insight from the paper reading is:

> 推理的边界，就是责任链的边界。

If reasoning stays inside text generation, responsibility is attached mainly to the answer. Once reasoning chooses tool calls, writes memory, updates future behavior, or coordinates multiple agents, responsibility extends to action consequences, future state, and organizational attribution. ^[inferred]

This matters for [[wiki/concepts/Governed Action]]: agentic reasoning expands capability and responsibility at the same time.

## Practical Design Implications

When designing an agentic system, start by drawing the action loop:

```text
what it observes -> what it can do -> how it knows it was wrong -> what it keeps for next time
```

Then decide whether the current problem is mainly:

- foundational capability: planning, tool use, search;
- self-evolution: feedback, memory, skill accumulation;
- collective coordination: role assignment, communication, shared state.

Finally decide whether the capability should be handled through in-context orchestration or post-training/internalized behavior.

This yields a practical routing question:

```text
one-off or changing task -> runtime orchestration
stable repeated behavior -> skill, memory, harness rule, or training signal
```

## Limitations and Cautions

The paper's main weakness is that it may over-center “reasoning” as the unifying explanation for agent success. Some improvements in agent systems may come from retrieval quality, tool interface design, reward engineering, environment constraints, workflow decomposition, or governance structure rather than from stronger reasoning itself. ^[inferred]

The survey also does not provide a unified empirical protocol for comparing its categories. It gives a map of the field, not a single ranking of methods.

## Open Questions

- How should agentic reasoning benchmarks compare systems when tool quality, environment design, memory policy, and model ability are all entangled?
- When should a behavior be left as harness orchestration, and when should it be internalized through training?
- How can memory updates and multi-agent collaboration be made auditable enough for real deployment?
- What governance layer is needed when reasoning controls actions with delayed or distributed consequences?

## Related

- [[wiki/maps/AI Map]] — broader AI, Agent, and LLM knowledge cluster.
- [[wiki/concepts/Agent]] — agent as a perception-memory-planning-action-feedback system.
- [[wiki/concepts/Agentic Control Loop]] — control-loop model that this paper reinforces.
- [[wiki/topics/AI Harness]] — runtime order layer where much in-context agentic reasoning is implemented.
- [[wiki/topics/AI Memory]] — memory as the persistence and adaptation surface for self-evolving agents.
- [[wiki/concepts/Governed Action]] — action governance becomes more important as reasoning gains tool and memory effects.
- [[wiki/sources/Agentic Artificial Intelligence Paper Source Guide]] — nearby survey on agentic AI architectures and control loops.
