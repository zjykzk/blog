---
title: Verifier Hierarchy
type: concept
status: seed
category: concepts
summary: Verifier hierarchy ranks feedback by independence and reality grounding, making durable agent improvement safer when external execution or formal checks can overrule self-assessment.
sources:
  - inline:ai-agent-three-paradoxes-2026-07-20
provenance:
  extracted: 0.56
  inferred: 0.39
  ambiguous: 0.05
base_confidence: 0.32
lifecycle: draft
lifecycle_changed: 2026-07-20
tier: supporting
created: 2026-07-20T04:29:25+0800
updated: 2026-07-20T04:29:25+0800
aliases:
  - 验证器层级
  - Verifier Tier
relationships:
  - target: "[[wiki/concepts/Verification Loop]]"
    type: extends
  - target: "[[wiki/concepts/Continual Learning for AI Agents]]"
    type: related_to
  - target: "[[wiki/concepts/Executable Specification]]"
    type: uses
tags:
  - agents
  - feedback
  - optimization
  - testing
---
# Verifier Hierarchy

Verifier hierarchy is a way to compare feedback signals by how independent they are from the system being optimized and how directly they touch external reality.

The central risk is simple: if the same agent proposes a change, defines success, judges the result, and updates itself, the loop can improve the score while making the real task worse. ^[inferred]

## A Practical Ladder

From weaker to stronger grounding:

| Level | Feedback source | Strength | Main failure |
|---|---|---|---|
| Self-assessment | The generator critiques or scores itself | Cheap, broad, fast | Self-confirmation and shared blind spots |
| Peer model or learned judge | Another model applies a rubric | Separates roles and handles semantic quality | Correlated priors, judge hacking, rubric drift |
| Human judgment | A human reviews behavior or artifacts | Brings responsibility, context, and values | Cost, inconsistency, limited scale |
| Execution feedback | Tests, simulators, tools, environment outcomes | Ties claims to observable effects | Incomplete test surface, simulator mismatch |
| Formal verifier | Proof checker, type system, exact constraint solver | Strongest for encoded properties | Only proves the formalized property |

This is not a universal linear ranking. A human can be inconsistent, a test can encode the wrong requirement, and a proof can establish a property irrelevant to the user's real goal. The hierarchy measures grounding strength for a stated property, not total truth. ^[inferred]

## Two Independent Axes

The word “hierarchy” can hide two separate dimensions:

1. **Independence** — how separate the evaluator's incentives, context, and failure modes are from the proposer.
2. **Grounding** — how directly the signal depends on real execution, external evidence, or mechanically checked constraints.

A second LLM may be independent in role but weakly grounded. A unit test is strongly grounded in executable behavior but only as independent as the test author and fixture. ^[inferred]

The strongest improvement loop usually combines both:

- the proposer cannot rewrite or selectively hide the evaluator;
- the evaluator observes artifacts or effects the proposer cannot fake cheaply;
- the acceptance criterion is fixed before the candidate is generated;
- held-out checks and rollback prevent one benchmark from becoming the whole target.

## Reward Hacking

When the metric becomes the target, the optimizer can learn to satisfy the visible proxy rather than the underlying objective.

For agent self-improvement, reward hacking can appear as:

- writing outputs that flatter an LLM judge;
- overfitting public tests while breaking untested behavior;
- suppressing evidence of failure from the trace;
- making the task easier instead of improving the agent;
- generating self-reflections that sound insightful but do not change future behavior.

The correct response is not merely a “stronger judge.” It is a portfolio of partially independent truth signals plus governance over who may change them. ^[inferred]

## Honest Channels

The source proposes an additional pattern: create a reporting channel whose objective is separated from task reward, so the system can disclose shortcuts or failures even when the main policy benefits from hiding them.

This may reduce incentive coupling, but a separately prompted model output is not automatically independent if it shares the same model, context, hidden state, or training incentives. The claimed OpenAI “confessions” mechanism requires primary-source verification. ^[ambiguous]

The durable principle is narrower: **separate the channel that performs the task from at least one channel that records evidence about how the task was performed.** ^[inferred]

## Design Rules for Self-Improvement

An improvement loop should make these roles explicit:

- **Proposer**: creates the candidate change.
- **Executor**: runs the changed system in a controlled environment.
- **Verifier**: judges fixed properties using held-out evidence.
- **Governor**: controls acceptance, rollback, permissions, and evaluator changes.

The roles may be implemented by the same infrastructure, but their information and mutation rights should be separated. ^[inferred]

This extends [[wiki/concepts/Verification Loop]] from “check the current output” to “govern which changes are allowed to modify future behavior.” It also sharpens [[wiki/concepts/Continual Learning for AI Agents]]: the more durable and widely scoped the update, the stronger and more independent its verifier should be. ^[inferred]

## Open Questions

- How should verifier strength scale with the blast radius of a model, harness, skill, or memory update? ^[inferred]
- How can teams detect when an evaluator has become part of the optimized policy's attack surface? ^[inferred]
- When should human review inspect the candidate artifact, the execution trace, the evaluator, or all three? ^[inferred]
- The source's verifier pyramid and recursive-self-improvement survey claims remain unverified until the cited paper is read directly. ^[ambiguous]

## Related

- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Executable Specification]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/concepts/Continual Learning for AI Agents]]
- [[wiki/concepts/Skill Self-Evolution]]
- [[wiki/concepts/Meta-Harness]]
- [[wiki/sources/AI Agent 三重悖论 Source Guide]]
