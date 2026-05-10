---
title: Design-First Collaboration
type: concept
status: seed
category: concepts
summary: Design-first collaboration makes AI design decisions explicit through staged alignment before any implementation code is generated.
sources:
  - https://martinfowler.com/articles/reduce-friction-ai/design-first-collaboration.html
created: 2026-05-05T17:25:00+08:00
updated: 2026-05-05T17:25:00+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.84
  inferred: 0.16
  ambiguous: 0.0
aliases:
  - design-first AI collaboration
  - whiteboard before keyboard
tags:
  - ai-coding
  - software-engineering
  - workflow
---
# Design-First Collaboration

Design-first collaboration is the practice of making an AI coding assistant discuss design before it writes implementation code.

Rahul Garg's [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]] frames the core failure as the "Implementation Trap": the assistant jumps from requirement to code, silently embedding design decisions about scope, component boundaries, data flow, interfaces, error handling, and integration.

## Five Levels

The article proposes a staged design conversation:

1. Capabilities: confirm what the system needs to do and what is out of scope.
2. Components: identify services, modules, and major abstractions.
3. Interactions: describe data flow, API calls, events, and integration paths.
4. Contracts: agree on function signatures, types, schemas, and interfaces.
5. Implementation: write code only after the previous levels are approved.

The key rule is: no code until Level 5.

## Why It Works

Design-first collaboration moves disagreement to the cheapest point. A wrong abstraction or scope expansion can be corrected while it is still a design proposal instead of after it has been woven through generated code.

It also manages cognitive load. The reviewer does not have to evaluate scope, architecture, integration, contracts, and code quality all at once; each layer gets its own checkpoint.

This is the design-side partner to [[wiki/concepts/Knowledge Priming]]: priming provides project vocabulary and constraints, while design-first collaboration provides the sequence for using that context.

## Contracts As A Testing Bridge

The contracts level creates a natural bridge to [[wiki/topics/Testing Strategy]] and [[wiki/topics/Spec-Driven Development]].

Once interfaces, types, and schemas are agreed, the assistant can generate tests before implementation. For teams using TDD, this creates an AI-friendly path from design agreement to executable checks. For teams not using TDD, contracts still act as reviewable specifications that expose misunderstandings before code exists.

## Lattice Example

The article's Lattice sidebar gives one implementation example: the `design-first` atom encodes the five-level methodology as an installable skill, while the `design-blueprint` molecule loads context, walks the levels, and persists the approved blueprint.

That example strengthens [[wiki/topics/AI Skills Workflow]]: a skill can preserve a collaboration discipline under deadline pressure by making the workflow explicit and reusable. ^[inferred]

## Failure Modes

- Trivial tasks may not justify all five levels.
- The assistant may try to collapse levels or attach code too early.
- The developer must actively calibrate the level of design detail to task complexity.
- Design-first reduces hidden disagreement, but it does not prove that the agreed design is correct. ^[inferred]

## Related

- [[wiki/concepts/AI Collaboration Scaffolding]]
- [[wiki/concepts/Knowledge Priming]]
- [[wiki/topics/Spec-Driven Development]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/topics/Frontend Development Workflow]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]]
