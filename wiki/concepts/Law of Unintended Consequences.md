---
title: >-
  Law of Unintended Consequences
category: concepts
tags: [software-engineering, systems, complexity, feedback]
sources:
  - inline:laws-of-software-engineering-unintended-consequences-2026-06-09
created: 2026-06-09T10:20:40+08:00
updated: 2026-06-09T10:20:40+08:00
summary: >-
  The Law of Unintended Consequences warns that interventions in complex systems can create benefits, side effects, or perverse results not predicted by the original plan.
provenance:
  extracted: 0.78
  inferred: 0.22
  ambiguous: 0.00
base_confidence: 0.32
lifecycle: draft
lifecycle_changed: 2026-06-09
type: concept
status: draft
aliases:
  - Unintended Consequences
  - 意外后果法则
---
# Law of Unintended Consequences

The Law of Unintended Consequences says that significant changes in a complex system can produce results that the planner did not fully predict.

## Core Claim

The law is not simply “things go wrong.” It says outcomes are hard to predict because systems contain interdependencies, feedback, delayed effects, and human adaptations.

The source separates unintended consequences into three kinds:

- **Unexpected benefits**: the intervention produces a useful surprise.
- **Unexpected drawbacks**: the intervention produces side effects that hinder the original goal.
- **Perverse results**: the intervention worsens the very problem it was meant to solve.

In software engineering, the law appears when a fix, feature, policy, or optimization changes behavior elsewhere in the system: regressions, performance degradation, increased load, full disks from logging, or user workarounds that defeat the original intention.

## Why It Matters in Software

Software systems are not only code. They are code plus users, operations, data, incentives, workloads, dependencies, documentation, and historical behavior. That means a local change can travel through non-obvious paths before its real effect appears. ^[inferred]

This connects directly to [[wiki/sources/Hyrums Law Source Guide|Hyrum's Law]]: if another module, user, or integration depended on the old behavior, a “fix” can become a regression from that dependent actor's point of view.

It also connects to [[wiki/topics/Thinking in Systems]] and [[wiki/concepts/Feedback Loops]] because the surprising result often comes from feedback that the original plan did not model.

## Engineering Use

A useful engineering reading of the law is: every meaningful intervention should be treated as a hypothesis about a system, not as a guaranteed command over that system. ^[inferred]

This pushes teams toward:

- small reversible changes when possible
- observability around expected and unexpected effects
- rollback and mitigation paths
- monitoring for second-order effects, not only direct success metrics
- post-change review when reality contradicts the plan

## Open Questions

- How can teams distinguish a tolerable side effect from an early sign of a perverse result?
- Which change classes need explicit second-order-effect monitoring before release?
- How should product metrics include harms produced outside the narrow success metric?

## Sources

- [[wiki/sources/Law of Unintended Consequences Source Guide]] — pasted chapter excerpt from *Laws of Software Engineering* material.

## Related

- [[wiki/topics/Modern Software Engineering]]
- [[wiki/topics/Thinking in Systems]]
- [[wiki/concepts/Feedback Loops]]
- [[wiki/sources/Hyrums Law Source Guide|Hyrum's Law Source Guide]]
- [[wiki/maps/CS Map]]
