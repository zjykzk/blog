---
title: Knowledge Priming
type: concept
status: seed
category: concepts
summary: Knowledge priming gives AI coding assistants curated, versioned project context before generation so they fit local architecture and conventions.
sources:
  - https://martinfowler.com/articles/reduce-friction-ai/knowledge-priming.html#ThisPatternInLattice
created: 2026-05-05T17:15:00+08:00
updated: 2026-05-05T17:15:00+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.82
  inferred: 0.18
  ambiguous: 0.0
aliases:
  - project context priming
  - AI knowledge priming
tags:
  - ai
  - ai-coding
  - context
  - workflow
---

# Knowledge Priming

Knowledge priming is the practice of giving an AI coding assistant curated project context before asking it to generate code.

Rahul Garg's [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]] frames the problem as a default-behavior failure: without local context, the assistant tends to produce generic code shaped by training data rather than the team's stack, architecture, conventions, and history.

## What Gets Primed

A useful priming document is not comprehensive documentation. It is a compact onboarding packet for the assistant:

- architecture overview
- current tech stack and versions
- curated sources the team trusts
- project structure
- naming conventions
- examples of code the team considers good
- anti-patterns the assistant should avoid

The important property is selection. The priming document should contain the minimum high-signal context needed to steer generation toward this codebase.

## Infrastructure, Not Habit

The stronger form of knowledge priming is to treat the priming document as project infrastructure instead of a copy-paste ritual.

That means the context should live in a versioned file, be reviewed like code, and load automatically or be easy to reference from the coding assistant. This turns priming into shared team infrastructure rather than an individual productivity habit.

This directly supports [[wiki/concepts/AI Collaboration Scaffolding]]: priming handles the onboarding layer before design discussion, standards enforcement, and feedback loops.

## Lattice Example

The article's Lattice sidebar gives one implementation example: Lattice encodes the practice as a `knowledge-priming` atom and pairs it with a `knowledge-priming-refiner` that interviews the user, captures project identity, and writes the result to a versioned file read by other skills.

That example connects knowledge priming to [[wiki/topics/AI Skills Workflow]]: a skill is not just a saved prompt, but a reusable workflow for collecting, compressing, and reusing context. ^[inferred]

## Failure Modes

- Too much context dilutes attention and can make the assistant less focused.
- Vague context such as "use modern best practices" does not override generic defaults.
- Stale priming documents can teach the assistant outdated local patterns.
- Priming is not a guarantee; it reduces avoidable mismatch but does not replace review.

## Related

- [[wiki/concepts/AI Collaboration Scaffolding]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]]
