---
title: AI Collaboration Scaffolding
type: concept
status: seed
category: concepts
summary: AI collaboration scaffolding gives coding assistants onboarding context, design discussion, standards, anchors, and feedback loops so their output fits the team.
sources:
  - https://martinfowler.com/articles/reduce-friction-ai/
  - https://martinfowler.com/articles/reduce-friction-ai/knowledge-priming.html#ThisPatternInLattice
  - https://martinfowler.com/articles/reduce-friction-ai/design-first-collaboration.html
created: 2026-05-05T17:05:00+08:00
updated: 2026-05-05T17:25:00+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.80
  inferred: 0.20
  ambiguous: 0.0
aliases:
  - AI-assisted development scaffolding
  - AI collaboration patterns
tags:
  - ai
  - software-engineering
  - workflow
  - ai-coding
---

# AI Collaboration Scaffolding

AI collaboration scaffolding is the set of practices that makes AI coding assistants behave more like aligned teammates and less like generic code generators.

Rahul Garg's article [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]] frames the problem as a collaboration gap: developers often ask AI to generate code without the onboarding, design discussion, standards, shared memory, and feedback rituals they would naturally provide to a human pair.

## Five Patterns

The article proposes five patterns:

- **Knowledge Priming**: give the assistant curated project context before asking for code.
- **Design-First Collaboration**: discuss capabilities, components, interactions, and contracts before implementation.
- **Context Anchoring**: maintain a living document of decisions, constraints, and current state.
- **Encoding Team Standards**: turn tacit senior-developer judgment into reusable prompts, commands, or checks.
- **Feedback Flywheel**: capture what worked and what failed so the collaboration system improves over time.

Together these patterns create a shared mental model between human and assistant.

[[wiki/concepts/Knowledge Priming]] is the most infrastructure-like of the five patterns: the article recommends keeping project context in versioned, reviewable files rather than relying on a developer to paste reminders into each session. Its Lattice example implements this as a reusable skill/refiner pair that captures project identity and makes it available to other skills.

[[wiki/concepts/Design-First Collaboration]] is the design-alignment pattern: it reconstructs the human whiteboard by moving through capabilities, components, interactions, contracts, and implementation, with no code until the design is agreed.

## Why It Matters

The core failure mode is not that the model cannot code. It is that the assistant defaults to generic training-data patterns when project-specific context is absent.

That creates a frustration loop: generate, review, find misfit, regenerate, review again, then either heavily modify the output or abandon it.

Scaffolding attacks the cause: missing context, missing design alignment, missing standards, missing memory, and missing learning loop.

## Relationship To Existing Wiki Ideas

For [[wiki/syntheses/AI Engineering Workflow]], scaffolding fills the collaboration layer between requirement normalization and implementation.

For [[wiki/topics/Spec-Driven Development]], design-first collaboration and context anchoring act as lightweight spec disciplines even when a team is not using full SDD. ^[inferred]

For [[wiki/concepts/Harness Ratchet]], the feedback flywheel is the human-team version of turning repeated AI failures into durable workflow or rule changes. ^[inferred]

## Related

- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/concepts/Knowledge Priming]]
- [[wiki/concepts/Design-First Collaboration]]
- [[wiki/topics/Spec-Driven Development]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]]
