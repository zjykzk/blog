---
title: Context Graph
type: concept
status: seed
category: concepts
summary: A context graph connects artifacts, owners, decisions, commitments, triggers, evidence, freshness, and permissions so facts can guide action.
sources:
  - https://nanothoughts.substack.com/p/company-brain-why-most-companies
  - https://open.substack.com/pub/nanothoughts/p/company-brain-part-2-factual-memory?utm_campaign=post&utm_medium=web
  - https://open.substack.com/pub/nanothoughts/p/company-brain-part-3-interaction?utm_campaign=post&utm_medium=web
  - https://nanothoughts.substack.com/p/company-brain-part-4-action-memory
created: 2026-05-08T15:58:41+08:00
updated: 2026-05-08T22:24:16+08:00
base_confidence: 0.78
lifecycle: draft
lifecycle_changed: 2026-05-08
provenance:
  extracted: 0.78
  inferred: 0.20
  ambiguous: 0.02
aliases:
  - reasoning layer
  - organizational context graph
  - company reasoning layer
tags:
  - memory
  - knowledge-graph
  - organization
---
# Context Graph

A context graph is the reasoning layer that turns organizational facts into a model of the company.

In the first source's example, a customer call connects to an opportunity, the opportunity connects to a product gap, the gap connects to an engineering tradeoff, the tradeoff connects to a roadmap decision, and the decision connects to strategy.

Part 2 gives a more artifact-centric chain: a customer call connects to an account, the account connects to open issues, issues connect to tickets, tickets connect to product areas, product areas connect to owners, and owners connect to decisions.

## What It Preserves

A context graph preserves relationships that ordinary company tools often store as separate artifacts:

- customer signals and sales objections
- product gaps and support complaints
- engineering constraints and tradeoffs
- roadmap decisions and strategic priorities
- owners, commitments, blockers, and follow-ups
- evidence strength, stale context, and conflicting assumptions
- provenance, permissions, ownership, freshness, and source-of-truth boundaries

This graph is not just a retrieval index. It is a structure for deciding what a fact means in the current situation. ^[inferred]

The source calls the durable version closer to a [[wiki/concepts/Semantic File System]] than to simple RAG: relationship quality determines memory quality.

## Interaction Updates

Part 3 makes the context graph the target of [[wiki/concepts/Interaction Memory]]. A meeting should not only produce a note; it should update the map of what the company believes, what it has promised, what remains unresolved, and what should happen next.

The interaction layer adds people, teams, customers, projects, commitments, decisions, risks, assumptions, dependencies, and time as graph nodes or relations. This lets the company reread past interactions when later evidence changes their meaning.


## Action Updates

Part 4 extends the context graph toward [[wiki/concepts/Action Memory]]. Conditions such as churn risk, unresolved support-ticket age, discount thresholds, approaching renewals, late commitments, changed metrics, meeting promises, and agent actions needing review should wake up the relevant operating path.

After action, the graph should also absorb execution and outcome traces: who approved, which handoff failed, what workaround was used, whether the customer renewed, whether technical debt was created, and whether a human correction should change future behavior.

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
- [[wiki/topics/AI Memory]]
- [[wiki/syntheses/AI Memory × Context Graph]] — synthesis
- [[wiki/concepts/Organizational Memory]]
- [[wiki/concepts/Factual Memory]]
- [[wiki/concepts/Interaction Memory]]
- [[wiki/concepts/Organizational Ontology]]
- [[wiki/concepts/Semantic File System]]
- [[wiki/concepts/Action Memory]]
- [[wiki/concepts/Governed Action]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Knowledge as Network]]
- [[wiki/sources/Company Brain Source Guide]]
