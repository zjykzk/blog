---
title: Context Information Density
type: concept
status: seed
summary: Context information density treats agent context quality as the ratio of decision-relevant signal to finite active context budget.
category: concepts
sources:
  - https://arxiv.org/abs/2307.03172
  - inline:ai-coding-information-theory-cheer-2026-07-12
created: 2026-05-04
provenance:
  extracted: 0.80
  inferred: 0.20
  ambiguous: 0.0
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-05-04
source_count: 2
updated: 2026-07-12T23:19:18+0800
aliases:
  - context information density maximization
  - contextual information density
  - 上下文信息密度
tags:
  - agents
  - context
  - memory
---
# Context Information Density

Context information density is the design target of keeping decision-relevant information available inside a limited active context while excluding irrelevant or redundant material.

The GenericAgent paper argues that long-horizon agent performance is limited less by nominal context length than by the density of usable information maintained during execution.

## Core tension

The paper frames context quality around two primary requirements:

- **Completeness**: the information needed for the current decision must be present.
- **Conciseness**: irrelevant or redundant material must be excluded.
- **Naturalness**: the representation should stay semantically legible enough for the model to use.

Completeness and conciseness are structurally in tension. Adding more material may preserve details but dilute attention; compressing material may improve focus but omit needed constraints. This tension remains even when context windows grow, because the model still has finite effective attention.

[[wiki/sources/Lost in the Middle Paper Source Guide]] adds a third constraint: positional usability. A fact can be present, relevant, and still underused if it sits in a low-utility region of a long context.

This is why density cannot be measured only by counting relevant tokens. It also depends on whether those tokens are placed where the model can retrieve and apply them. ^[inferred]

[[wiki/sources/AI Coding 信息论框架 Source Guide]] gives this principle an information-theoretic interpretation: useful context increases mutual information with the target output, while redundant, stale, conflicting, or wrong context consumes attention without reliably shrinking the model's remaining guess space. Its practical proxy is not context size but $I(X;Y)/|Context|$. Because real task distributions are not directly measurable, this ratio is an engineering lens rather than an operational metric. ^[inferred]

The same source separates low density from wrong direction. Low-density context mainly dilutes attention; incorrect or obsolete context can also push the model toward a false project prior, making confident errors more likely. ^[inferred]

## Agent design implications

Context information density turns [[wiki/topics/Context Management]] from token housekeeping into a core design constraint for [[wiki/concepts/Agent]] systems.

In GenericAgent, the principle is implemented through four mechanisms:

- A minimal atomic tool set reduces prompt-resident tool overhead.
- Hierarchical memory keeps only a small orientation layer visible by default and retrieves deeper facts or SOPs on demand.
- Self-evolution distills verified trajectories into reusable SOPs and executable code.
- Context truncation and compression keep active history below a compact budget during long executions.

The deeper claim is that memory, tools, and compression should be evaluated by whether they increase the active context's decision value, not by whether they maximize the amount of visible information. ^[inferred]

## Relationship to existing wiki ideas

This concept sharpens the current [[wiki/topics/AI Harness]] view: a harness is not only a runtime order layer, but also a density-preserving layer that decides what information enters the model at each step. ^[inferred]

It also gives [[wiki/syntheses/Agent System Design Space]] a stronger evaluation axis: agent architectures can be compared by how they balance completeness, conciseness, memory reuse, and tool overhead under long-horizon execution.

## Open Questions

- How should context information density be measured outside a paper benchmark?
- When does aggressive compression destroy the information needed for later recovery?
- Which parts of agent memory should be human-reviewed before promotion into reusable SOPs?

## Related

- [[wiki/topics/Context Management]]
- [[wiki/concepts/Lost in the Middle Effect]]
- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/GenericAgent Paper Source Guide]]
- [[wiki/sources/Lost in the Middle Paper Source Guide]]
- [[wiki/concepts/AI Coding Information-Theoretic Framework]]
- [[wiki/sources/AI Coding 信息论框架 Source Guide]]
