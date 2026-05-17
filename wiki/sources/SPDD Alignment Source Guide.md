---
title: >-
  SPDD Alignment Source Guide
type: source
status: draft
category: sources
tags:
  - article
  - software-engineering
  - ai-coding
  - requirements
  - testing
sources:
  - https://martinfowler.com/articles/structured-prompt-driven/alignment.html
  - conversation:2026-05-17
created: 2026-05-17T22:44:01+08:00
updated: 2026-05-17T22:44:01+08:00
summary: >-
  Source guide for the SPDD alignment companion page, preserving its intent-locking checklist for scope, language, acceptance, and constraints.
provenance:
  extracted: 0.87
  inferred: 0.11
  ambiguous: 0.02
base_confidence: 0.55
lifecycle: draft
lifecycle_changed: 2026-05-17
aliases:
  - Alignment
  - SPDD Alignment
---

# SPDD Alignment Source Guide

> Source: [Alignment](https://martinfowler.com/articles/structured-prompt-driven/alignment.html), Wei Zhang and Jessie Jie Xia, MartinFowler.com, part of Structured-Prompt-Driven Development.

## Capture Policy

This page preserves the SPDD companion page as source-level material. It should be used as a checklist for intent alignment inside [[wiki/sources/Structured-Prompt-Driven Development Source Guide]], while keeping the source's claims separate from broader requirements-engineering doctrine.

## What It Covers

The page defines alignment as making scope, non-scope, standards, and hard constraints explicit before implementation. Its practical concern is that AI-assisted teams can get fast output but slow rework when "what we will do" and "what we will not do" are left implicit.

It belongs in the wiki because it connects SPDD to [[wiki/topics/Requirement to Architecture Mapping]], [[wiki/topics/User Stories]], and [[wiki/syntheses/Requirements Expression Beyond Use Cases]]: generated code is only useful when upstream intent, vocabulary, rules, and dependencies are settled enough to test.

## Preserved Content

### Anchor on business value and outcomes

The first alignment checkpoint is business value:

- Identify the real user pain point rather than merely naming a feature.
- State the value hypothesis and how the team would know whether it was realized.
- Make non-goals explicit so the prompt does not silently expand scope.

This is a scope-control move. In SPDD, the structured prompt becomes a boundary object, so unresolved business value or missing non-goals can turn into generated work that looks complete but solves the wrong problem. ^[inferred]

### Align on domain language

The second checkpoint is domain vocabulary:

- Define key terms in the current context.
- Ensure developers and domain experts use the same words for the same meanings.
- Watch for the inverse ambiguity: different words that hide the same meaning.

This source-level checklist is close to DDD's ubiquitous-language concern, but the page uses it specifically to reduce prompt ambiguity before AI generation. It should therefore link to [[wiki/concepts/Domain-Driven Design]] without being collapsed into a DDD note.

### Make rules and acceptance criteria testable

The third checkpoint asks whether the business rules are expressed as testable acceptance:

- The normal business flow should be complete.
- Important exceptions and limits should be stated.
- The business-side definition of acceptance should be explicit.

This connects alignment to [[wiki/topics/Testing Strategy]]: acceptance criteria are not only product documentation, but an eventual verification surface for generated behavior.

### Confirm dependencies and hidden constraints

The fourth checkpoint is constraint discovery:

- Identify upstream modules, decisions, or unfinished work that the change depends on.
- Preserve existing business rules and special data-handling behavior.
- Surface legacy constraints before the model generates a locally plausible but system-incompatible change.

The page's "hidden constraint" framing matters because LLMs tend to optimize for the visible request. SPDD alignment tries to move invisible organizational and system constraints into the artifact before generation. ^[inferred]

### Capabilities and notable duplication

The fetched page's "Capabilities you need" section repeats the dependency and legacy-constraint bullets rather than expanding into a broader capability list. That may be an editorial duplication in the source. It should be preserved as source behavior rather than silently corrected into invented capabilities. ^[ambiguous]

The implied capability is early constraint discovery: the team must be able to find upstream dependencies, legacy rules, and special cases before implementation begins. ^[inferred]

### Operating principle: stage-gated validation

The page's operating principle is a strict sequence:

- Analysis document first.
- Structured prompt second.
- Code third.

If an earlier artifact is not aligned, the workflow should not advance. This is a stage gate: it converts alignment from a general value into a process rule.

## Integration Decisions

This guide should stay source-level because it is a companion checklist, not a full requirements methodology. Its durable contribution is the intent-locking lens inside SPDD.

The page should inform [[wiki/syntheses/Use Cases as AI Coding Traceability Anchors]] because it explains the upstream intent checks that make later traceability meaningful: pain point, value hypothesis, vocabulary, acceptance, non-goals, dependencies, and legacy constraints.

The page also strengthens [[wiki/concepts/AI Collaboration Scaffolding]] because alignment is part of scaffolding: teams must decide what context and constraints the assistant receives before implementation.

## Open Questions

- How should SPDD represent non-goals so they remain visible during later prompt updates and sync operations?
- What is the minimum domain-language artifact needed before generation: glossary, examples, decision table, or use-case narrative?
- Can alignment gates be automated, or do they mainly require human agreement?

## Related

- [[wiki/sources/Structured-Prompt-Driven Development Source Guide]]
- [[wiki/topics/Spec-Driven Development]]
- [[wiki/topics/User Stories]]
- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/syntheses/Requirements Expression Beyond Use Cases]]
- [[wiki/concepts/Domain-Driven Design]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/concepts/AI Collaboration Scaffolding]]
