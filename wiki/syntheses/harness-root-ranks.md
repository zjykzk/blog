---
title: >-
  Harness Root Ranks
category: synthesis
tags:
  - agents
  - harness
  - architecture
  - rank
sources:
  - conversation:2026-05-07
created: 2026-05-07T18:33:29+08:00
updated: 2026-05-07T18:33:29+08:00
summary: >-
  Harness can be reduced to five root ranks: boundary, density, action, loop, and evolution; these generate its components and runtime behavior.
provenance:
  extracted: 0.86
  inferred: 0.14
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-07
aliases:
  - harness 的秩
  - AI harness root ranks
---
# Harness Root Ranks

## Context

Harness is often described through component lists: prompts, tools, context policy, hooks, sandboxes, subagents, memory, observability, recovery paths, and service APIs. Component lists are useful, but they do not explain what generates the component set.

A rank-style analysis asks for the independent generators behind a field: the smallest set of forces that can regenerate the observed phenomena. Applied to [[wiki/topics/AI Harness]], the question is not which parts a harness contains, but which structural forces make those parts necessary. ^[inferred]

## Finding

Harness has five root ranks:

1. Boundary rank: what may happen, what must stop, and what must return to human or policy authority.
2. Density rank: what information remains visible, recoverable, stable, and useful under finite context.
3. Action rank: which capabilities the model can perceive, choose, compose, and execute.
4. Loop rank: how action is verified, repaired, retried, escalated, or stopped.
5. Evolution rank: how failures and new model capabilities change the harness itself.

Together, these ranks define harness as a runtime order layer that turns model capability into controllable, recoverable, verifiable, reusable, and evolvable agent behavior. ^[inferred]

## Reasoning

Boundary rank generates permission systems, approval gates, sandboxing, pre-action authorization, audit records, guardrails, and human decision authority. A model proposing an action is not the same as the system allowing that action to occur. [[wiki/syntheses/Agent System Design Space]] treats permission and approval boundaries as core architecture, while [[wiki/topics/AI Harness]] frames harness as the layer that defines what can happen inside the agent loop.

Density rank generates context management, memory retrieval, context compression, prompt caching, progressive disclosure, deferred tool loading, and positional robustness. [[wiki/concepts/Context Information Density]] frames context quality as decision-relevant signal under finite active context, not as maximal visible information. This rank explains why harnesses must manage both semantic usefulness and runtime economics such as cache-stable prefixes. ^[inferred]

Action rank generates tool design, skill disclosure, MCP/plugin surfaces, subagent routing, tool schemas, and action-space fit. [[wiki/concepts/Agent Action Space]] defines the agent's action space as what the model can perceive, choose, compose, and execute through harness surfaces. This rank explains why adding tools can both increase capability and increase confusion.

Loop rank generates verification loops, tests, linters, typechecks, visual checks, evaluator models, recovery paths, retry policies, continuation loops, and done conditions. [[wiki/concepts/Verification Loop]] treats verification as part of the harness, not as a final QA ritual. [[wiki/concepts/Feedforward and Feedback Controls]] and [[wiki/concepts/Computational and Inferential Controls]] further distinguish when the harness should steer before action, inspect after action, execute objective checks, or preserve judgment in rubrics.

Evolution rank generates harness ratchets, repository rules, hooks, workflow splits, templates, and removal of stale scaffolding. [[wiki/concepts/Harness Ratchet]] turns repeated agent failures into durable harness improvements. The same rank also explains why harness rules must be removed or revised when stronger models make old scaffolding redundant. ^[inferred]

## Implications

Harness quality should not be judged by feature count alone. A harness with many tools but weak boundaries can be unsafe; one with large context but poor density can bury the decision signal; one with strong prompts but no loop can compound errors; one with rules but no evolution can accumulate stale context noise.

The five-rank frame gives a compact diagnostic checklist:

- Boundary: does the system know what must not happen automatically?
- Density: does the model see the right information in a usable position and stable prefix shape?
- Action: is the capability surface matched to the model, task, and environment?
- Loop: does the system receive usable truth signals after action?
- Evolution: do repeated failures change durable harness structure rather than becoming new prompt problems?

## Structure

```text
                 [model latent capability]
                         |
                         v
+------------------------------------------------+
|                harness runtime order           |
+------------------------------------------------+
| boundary: allow / deny / ask / audit           |
| density: context / memory / cache / position   |
| action: tools / skills / hooks / subagents     |
| loop: verify / recover / retry / escalate      |
| evolution: failures -> rules / checks / forms  |
+------------------------------------------------+
                         |
                         v
           [controllable recoverable agent work]
```

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/concepts/Context Information Density]]
- [[wiki/concepts/Agent Action Space]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Feedforward and Feedback Controls]]
- [[wiki/concepts/Computational and Inferential Controls]]
