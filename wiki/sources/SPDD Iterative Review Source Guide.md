---
title: >-
  SPDD Iterative Review Source Guide
type: source
status: draft
category: sources
tags:
  - article
  - software-engineering
  - ai-coding
  - architecture
  - testing
sources:
  - https://martinfowler.com/articles/structured-prompt-driven/iterative-review.html
  - conversation:2026-05-17
created: 2026-05-17T22:44:01+08:00
updated: 2026-05-17T22:44:01+08:00
summary: >-
  Source guide for the SPDD iterative-review companion page, preserving its prompt/code consistency, functional validation, and review-loop guidance.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.55
lifecycle: draft
lifecycle_changed: 2026-05-17
aliases:
  - Iterative Review
  - SPDD Iterative Review
---

# SPDD Iterative Review Source Guide

> Source: [Iterative Review](https://martinfowler.com/articles/structured-prompt-driven/iterative-review.html), Wei Zhang and Jessie Jie Xia, MartinFowler.com, part of Structured-Prompt-Driven Development.

## Capture Policy

This page preserves the SPDD companion page as source-level material. It captures the source's review loop and should be linked back to [[wiki/sources/Structured-Prompt-Driven Development Source Guide]] rather than promoted directly into a general code-review doctrine.

## What It Covers

The page defines iterative review as turning AI output into a controlled engineering loop rather than a one-shot draft. Its central risk is solution drift: teams may keep asking the model to patch output until the design no longer matches intent, or restart repeatedly and lose cost/time control.

It belongs in the wiki because it connects [[wiki/concepts/Verification Loop]], [[wiki/topics/Testing Strategy]], and [[wiki/concepts/Context Anchoring]] to SPDD's specific rule that prompt artifacts and code must stay synchronized.

## Preserved Content

### Review focus: prompt and code consistency

The first review checkpoint is whether the structured prompt stays ahead of implementation when logic changes. If a refactor moves business logic or changes behavior, the prompt should be updated first so the generated code remains traceable to the current intent.

This makes the prompt a living source artifact rather than a historical instruction. The review question is not only "does the code work?" but "does this code still correspond to the prompt version that explains why it exists?"

### Review focus: architecture and responsibility boundaries

The second checkpoint is structural:

- Code should follow the intended layered architecture.
- Interfaces and implementations should have clean responsibility boundaries.
- Generated code should not smuggle business logic into the wrong layer.

This is the review counterpart to [[wiki/sources/SPDD Abstraction First Source Guide]]: abstraction-first work defines the intended structure; iterative review checks whether generated code preserved it.

### Review focus: cross-cutting engineering standards

The page lists several standards reviewers should inspect:

- Exception handling should follow the team's global strategy rather than local ad hoc `try/catch` blocks.
- Object construction and field initialization should stay encapsulated inside domain objects when appropriate, rather than leaking across service code.
- Maintainability smells such as magic numbers and long methods should be checked.
- Team-specific conventions remain part of review, not optional polish.

This aligns with [[wiki/concepts/Encoding Team Standards]] because prompt-driven generation still needs organization-specific norms to be visible and enforceable.

### Review focus: hallucination and correctness

The page treats hallucination as a code-review category:

- The generated code should implement what the prompt describes.
- Imports and dependencies should be correct and minimal.
- Review should catch syntax, compilation, invented API, and assumption failures.

This is a practical boundary on AI coding: correctness is not guaranteed by prompt quality alone. The review loop still needs executable checks and human inspection.

### Required capabilities

The source names four capabilities for iterative review:

- Prompt debugging: fix behavior drift by updating the prompt and regenerating, rather than patching code manually in ways that bypass the artifact.
- Functional validation: run the system locally and observe behavior against business expectations.
- Deep code review: after behavior is correct, inspect maintainability, structure, and risk.
- Asset integrity: ensure committed code maps cleanly to the exact prompt version.

This capability list is the strongest bridge from SPDD to [[wiki/syntheses/AI Engineering Workflow]]: the workflow's quality depends on maintaining the prompt/code relationship, not merely on accepting generated output. ^[inferred]

### Operating principles

The page gives two operating principles:

- Treat the structured prompt as a first-class source artifact. Requirement changes and bug fixes should update prompt and code together.
- Validate behavior first, then do deeper code review. If behavior is wrong, iterate on the prompt before investing in detailed structural review.

The second rule is source-specific and should stay source-level for now. It prioritizes functional feedback before deeper review, which may be useful for AI generation loops but can conflict with some test-first or design-first practices depending on context. ^[ambiguous]

## Integration Decisions

This source guide should remain separate from the main SPDD page because it preserves the operational review checklist that the main article only summarized.

The "prompt as code" principle should strengthen [[wiki/concepts/Context Anchoring]] and [[wiki/concepts/Verification Loop]]: a durable prompt artifact gives future reviewers something to compare against, while tests and local execution provide external feedback.

The page should also inform [[wiki/topics/Testing Strategy]] because it stages quality gates: observable behavior first, then deeper implementation review, while preserving prompt/code traceability.

## Open Questions

- When does prompt-first correction become slower than a direct code fix?
- How should teams version prompt artifacts so code review can compare a diff to the exact prompt that produced it?
- What automated checks can prove prompt/code consistency beyond simple file presence?

## Related

- [[wiki/sources/Structured-Prompt-Driven Development Source Guide]]
- [[wiki/sources/SPDD Abstraction First Source Guide]]
- [[wiki/topics/Spec-Driven Development]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Context Anchoring]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/syntheses/AI Engineering Workflow]]
