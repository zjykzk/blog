---
title: Context Graph
type: concept
status: seed
category: concepts
summary: A context graph connects facts, decisions, tradeoffs, assumptions, owners, and evidence so company knowledge becomes usable reasoning context.
sources:
  - https://nanothoughts.substack.com/p/company-brain-why-most-companies
created: 2026-05-08T15:58:41+08:00
updated: 2026-05-08T15:58:41+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-08
provenance:
  extracted: 0.74
  inferred: 0.24
  ambiguous: 0.02
aliases:
  - reasoning layer
  - organizational context graph
  - company reasoning layer
tags:
  - ai
  - memory
  - knowledge-graph
  - organization
---

# Context Graph

A context graph is the reasoning layer that turns organizational facts into a model of the company.

In the source's example, a customer call connects to an opportunity, the opportunity connects to a product gap, the gap connects to an engineering tradeoff, the tradeoff connects to a roadmap decision, and the decision connects to strategy.

## What It Preserves

A context graph preserves relationships that ordinary company tools often store as separate artifacts:

- customer signals and sales objections
- product gaps and support complaints
- engineering constraints and tradeoffs
- roadmap decisions and strategic priorities
- owners, commitments, blockers, and follow-ups
- evidence strength, stale context, and conflicting assumptions

This graph is not just a retrieval index. It is a structure for deciding what a fact means in the current situation. ^[inferred]

## Metacognitive Role

The article places metacognition in this layer. A company brain should notice when:

- evidence is weak
- context is stale
- teams hold conflicting assumptions
- a commitment has no owner
- an agent needs help

This makes the context graph close to a governance and verification surface for [[wiki/topics/AI Harness]]. ^[inferred]

## Failure Mode

Without a context graph, companies retain searchable fragments but lose decision rationale. Facts can remain visible while their meaning is gone.

## Related

- [[wiki/concepts/Company Brain]]
- [[wiki/concepts/Organizational Memory]]
- [[wiki/concepts/Governed Action]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Knowledge as Network]]
- [[wiki/sources/Company Brain Source Guide]]
