---
title: >-
  SPDD Abstraction First Source Guide
type: source
status: draft
category: sources
tags:
  - article
  - software-engineering
  - ai-coding
  - architecture
  - requirements
sources:
  - https://martinfowler.com/articles/structured-prompt-driven/abstraction-first.html
  - conversation:2026-05-17
created: 2026-05-17T22:44:01+08:00
updated: 2026-05-17T22:44:01+08:00
summary: >-
  Source guide for the SPDD abstraction-first companion page, preserving its design-before-generation review checklist and operating principles.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.55
lifecycle: draft
lifecycle_changed: 2026-05-17
aliases:
  - Abstraction First
  - SPDD Abstraction First
---

# SPDD Abstraction First Source Guide

> Source: [Abstraction first](https://martinfowler.com/articles/structured-prompt-driven/abstraction-first.html), Wei Zhang and Jessie Jie Xia, MartinFowler.com, part of Structured-Prompt-Driven Development.

## Capture Policy

This page preserves the SPDD companion page as source-level material. It should be read as a detailed human-skill checklist attached to [[wiki/sources/Structured-Prompt-Driven Development Source Guide]], not as an independently validated universal software design method.

## What It Covers

The page defines the first SPDD capability as designing before generating code. Its central warning is that AI can move quickly into implementation while domain objects, collaboration patterns, and boundaries remain unclear, causing responsibility confusion, duplicated logic, inconsistent interfaces, and later review/rework cost.

It belongs in the wiki because it sharpens the design side of [[wiki/topics/Spec-Driven Development]] and [[wiki/concepts/Design-First Collaboration]]: before a prompt becomes executable, the team must decide what abstractions exist and how the generated work should be decomposed.

## Preserved Content

### Review focus: business intent before design mechanics

The page starts abstraction review by checking whether the prompt still matches the product owner's intent:

- Requirement fidelity: the Requirements section should preserve the user story's core purpose.
- Acceptance coverage: the prompt should cover the business acceptance criteria without omissions or reinterpretations.
- Term alignment: domain terms in the prompt should match the team's established business language.

This makes abstraction review more than object modelling. A clean model that captures the wrong business intent is still a failed prompt artifact. ^[inferred]

### Review focus: abstraction model

The page then asks reviewers to inspect whether the model is grounded in the actual domain:

- Entities and value objects should reflect real business objects and relationships.
- A lightweight visual model, such as a Mermaid class diagram, can make the reviewable structure explicit.
- The approach should solve the core business problem through a coherent flow rather than merely naming familiar patterns.
- Components, dependencies, inheritance, and implementation relationships should fit the existing technical context.

The emphasis is on structural fit. The abstraction layer is not a naming exercise; it is the place where domain model, design strategy, and codebase context are reconciled before generation.

### Review focus: boundaries and constraints

The page treats engineering standards and hard constraints as part of the abstraction, not as after-the-fact cleanup:

- Norms should encode team conventions such as naming, logging, and error handling.
- Non-negotiable limits, including performance and security guardrails, should be explicit.
- Boundaries should tell the model where not to invent, not only where to implement.

This connects directly to [[wiki/concepts/Encoding Team Standards]]: team standards become prompt-level controls only when they are concrete enough to guide generation and review.

### Review focus: executable tasks

The page's final review area is task decomposition:

- Work should be split into independent, testable technical units.
- The tasks should form a complete chain from requirement to deliverable behavior.
- Task descriptions should reduce uncertainty enough that the model does not need to guess missing details.

The task list is therefore a granularity control. It prevents the workflow from producing a large opaque diff that reviewers can only accept or reject as a whole.

### Required capabilities

The source names four capabilities behind abstraction-first SPDD:

- Structured modelling: convert complex requirements into entities, interactions, boundaries, and a shared solution model.
- Engineering trade-off decisions: choose between existing codebase patterns and new requirement pressure while preserving system coherence.
- Atomic task design: break an abstract solution into independently testable units.
- Visual communication: use lightweight diagrams to turn narrative requirements into explicit logic.

These capabilities are senior-engineering capabilities. The page does not claim the LLM replaces them; it positions them as the human work that makes generation governable.

### Operating principles

The source's operating principles can be compressed into four workflow rules:

- Do not generate code when design and boundaries are unclear.
- Define interface responsibilities before implementation details.
- Keep generation units small enough to build, finish, and review one piece at a time.
- Diagram early when a visual model can resolve ambiguity faster than wording.

These rules align with [[wiki/syntheses/Use Cases as AI Coding Traceability Anchors]] because both treat early structure as a way to carry intent through later implementation and verification.

## Integration Decisions

This page should remain a companion source guide rather than being merged into the main SPDD guide. The main page captures the full workflow; this page preserves the review checklist for one human capability inside that workflow.

The strongest promotable idea is "abstraction before generation", but the wiki already has related stable pages in [[wiki/concepts/Design-First Collaboration]], [[wiki/topics/Requirement to Architecture Mapping]], and [[wiki/syntheses/From User Story to Architecture]]. For now, this source should strengthen those pages rather than create a duplicate concept.

The page's checklist can later inform [[wiki/topics/AI Harness]] because it acts as a feedforward control: it constrains what the model is asked to generate before runtime feedback begins. ^[inferred]

## Open Questions

- How much abstraction detail is enough before generation begins?
- Which diagrams produce the most review value for SPDD: class diagrams, sequence diagrams, flow charts, or task dependency maps?
- Can automated checks detect weak abstraction boundaries, or is this mostly human review?

## Related

- [[wiki/sources/Structured-Prompt-Driven Development Source Guide]]
- [[wiki/topics/Spec-Driven Development]]
- [[wiki/concepts/Design-First Collaboration]]
- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/syntheses/From User Story to Architecture]]
- [[wiki/concepts/Encoding Team Standards]]
