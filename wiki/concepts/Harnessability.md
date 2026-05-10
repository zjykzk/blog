---
title: Harnessability
type: concept
status: seed
category: concepts
summary: Harnessability is how easily a task, codebase, or workflow can be surrounded by context, controls, checks, and templates for effective agent work.
sources:
  - https://martinfowler.com/articles/harness-engineering.html
  - https://www.chrismdp.com/coding-with-ai/
created: 2026-05-06T22:24:21+08:00
updated: 2026-05-07T22:03:56+08:00
base_confidence: 0.61
lifecycle: draft
lifecycle_changed: 2026-05-06
provenance:
  extracted: 0.74
  inferred: 0.26
  ambiguous: 0.0
aliases:
  - harnessable
  - agent harnessability
tags:
  - agents
  - harness
  - software-engineering
---
# Harnessability

Harnessability is the degree to which a task, codebase, or workflow can be effectively surrounded by a [[wiki/concepts/Coding Agent User Harness]].

A harnessable situation gives the agent stable context, clear boundaries, repeatable starting points, and feedback that can be read by the agent or the humans guiding it.

## What Makes Work Harnessable

Work is more harnessable when it has:

- explicit task boundaries
- small decision units
- clear examples of desired output
- executable checks
- stable project vocabulary
- known architectural constraints
- repeatable templates or workflows
- review criteria that can be reused

Work is less harnessable when success depends on hidden context, large ambiguous judgment calls, unclear ownership, or checks that exist only in one person's head. ^[inferred]

## Relation to Codebase Design

Harnessability is not only a prompt property. It is also a software design property. ^[inferred]

A codebase with local tests, clear module boundaries, documented conventions, and predictable scripts gives a coding agent more reliable control surfaces than a codebase where every change requires tacit knowledge.

This connects harnessability to [[wiki/topics/Modern Software Engineering]]: design for humans and design for agents increasingly overlap around explicit boundaries, fast feedback, and recoverable changes. ^[inferred]

[[wiki/sources/Coding with AI Source Guide]] adds a throughput pressure test: as agent generation speed rises, harnessability depends less on how quickly code can be produced and more on how quickly the team can verify, reset, and feed lessons back into the harness.

A task is weakly harnessable when verifying the generated change takes almost as long as writing it manually. In that case, the team either needs a better review surface, a stronger automated gate, or a decision not to delegate that task yet.

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/concepts/Agentic Engineering]]
- [[wiki/concepts/Feedforward and Feedback Controls]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/concepts/Context Anchoring]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/sources/Harness Engineering Source Guide]]
- [[wiki/sources/Coding with AI Source Guide]]
