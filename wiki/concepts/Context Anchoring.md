---
title: Context Anchoring
type: concept
status: seed
category: concepts
summary: Context anchoring preserves feature-level AI collaboration decisions in a living document outside the chat session.
sources:
  - https://martinfowler.com/articles/reduce-friction-ai/context-anchoring.html
created: 2026-05-05T17:35:00+08:00
updated: 2026-05-05T17:35:00+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.84
  inferred: 0.16
  ambiguous: 0.0
aliases:
  - AI context anchoring
  - feature document
  - living ADR
tags:
  - ai
  - ai-coding
  - context
  - workflow
---

# Context Anchoring

Context anchoring is the practice of externalizing feature-level AI collaboration context into a living document outside the chat session.

Rahul Garg's [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]] frames the core failure as context trapped in an ephemeral conversation: developers keep long AI chats alive because decisions, rejected alternatives, constraints, and current state live nowhere else.

## Why Context Erodes

The article connects this problem to finite context windows and [[wiki/concepts/Lost in the Middle Effect]]: as a session grows, earlier decisions become harder for the model to use reliably.

Garg's practical observation is that the reasoning behind a decision often erodes faster than the decision itself. The assistant may remember that PostgreSQL was chosen, while losing the constraints and trade-offs that made PostgreSQL the right choice.

Opaque compaction can worsen this risk because the developer cannot see which reasoning was preserved, summarized, or dropped. The article's answer is to move important decision context into explicit external state.

## Feature Document

A context anchor is a feature-level working record, not a stable project primer.

- [[wiki/concepts/Knowledge Priming]] captures project-level context: stack, architecture, conventions, trusted examples, and naming patterns.
- Context anchoring captures feature-level history: decisions made during development, reasons, rejected alternatives, open questions, constraints, and current implementation state.

Together they form a two-layer context strategy: project context provides the vocabulary, while feature context provides the history.

The feature document functions like a living ADR: it records what was decided, why it was decided, what alternatives were rejected, and what remains unresolved. It can later graduate significant decisions into formal architecture decision records.

## Why Code Is Not Enough

Code captures outcomes, not reasoning. A codebase may show that BullMQ is used directly for retry handling, but not whether a wrapper abstraction was proposed and rejected or why the direct approach better fit the feature.

This makes context anchoring a companion to [[wiki/topics/Context Management]]: rather than preserving every chat turn, it preserves decision-relevant information in a compact artifact that can be loaded into a fresh session.

The token benefit is secondary but important: a short feature document can carry decision context that hundreds of lines of implementation code cannot express. That improves [[wiki/concepts/Context Information Density]]. ^[inferred]

## Calibration

Context anchoring is most valuable when the work spans multiple sessions, multiple developers, or enough elapsed time that re-establishing context becomes expensive.

For quick questions or trivial utilities, the documentation overhead is not justified. For a single-session feature, a few bullets may be enough. For multi-day or team-coordinated work, the full feature document breaks the cycle of keeping a long, decaying chat alive.

The litmus test is whether the developer can close the chat and start a new session without anxiety.

## Lattice Example

The article's Lattice sidebar gives one implementation example: the `context-anchoring` atom makes every molecule create or enrich a living document across sessions.

That strengthens [[wiki/topics/AI Skills Workflow]]: a skill can preserve not only instructions and project context, but also the durable state that lets future sessions resume without reconstructing prior reasoning. ^[inferred]

## Related

- [[wiki/concepts/AI Collaboration Scaffolding]]
- [[wiki/concepts/Knowledge Priming]]
- [[wiki/concepts/Design-First Collaboration]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Context Information Density]]
- [[wiki/concepts/Lost in the Middle Effect]]
- [[wiki/topics/Spec-Driven Development]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]]
