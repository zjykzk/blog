---
title: Context Information Density
type: concept
status: seed
summary: Context information density treats agent context quality as the ratio of decision-relevant signal to finite active context budget.
provenance:
  extracted: 0.78
  inferred: 0.22
  ambiguous: 0.0
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-05-04
source_count: 1
updated: 2026-05-04
aliases:
  - context information density maximization
  - contextual information density
  - 上下文信息密度
tags:
  - ai
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
- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/GenericAgent Paper Source Guide]]
