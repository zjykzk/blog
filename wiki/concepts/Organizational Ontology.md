---
title: Organizational Ontology
type: concept
status: seed
category: concepts
summary: Organizational ontology is the set of concepts and relationships a company uses to interpret conversations as decisions, commitments, risks, assumptions, and open questions.
sources:
  - https://open.substack.com/pub/nanothoughts/p/company-brain-part-3-interaction?utm_campaign=post&utm_medium=web
created: 2026-05-08T20:54:16+08:00
updated: 2026-05-08T20:54:16+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-08
provenance:
  extracted: 0.72
  inferred: 0.25
  ambiguous: 0.03
aliases:
  - company ontology
  - interaction ontology
  - enterprise ontology
tags:
  - organization
  - knowledge-graph
  - memory
  - ai
---

# Organizational Ontology

Organizational ontology is the set of concepts and relationships a company uses to make sense of its domain and its conversations. In the Company Brain source, ontology decides whether a piece of conversation becomes a decision, commitment, objection, escalation, dependency, assumption, customer pain, owner, precedent, or open question.

## Why It Matters

The same sentence can mean different things under different business lenses. “We can ship this Friday if legal signs off and Acme is okay with the beta limitation” can be a launch plan, an approval dependency, a conditional customer commitment, a deal risk, a set of follow-ups, and evidence that the decision is not closed.

The labels are not just metadata. They decide what gets remembered and how future retrieval or reasoning will treat the interaction.

## Interaction Interpretation

[[wiki/concepts/Interaction Memory]] depends on organizational ontology because transcripts and summaries do not preserve enough structure by themselves. The system has to interpret what changed, what stayed open, who is responsible, which prior discussions matter, and which assumptions are fragile.

This makes ontology a practical memory-control surface rather than a purely academic taxonomy. ^[inferred]

## Dynamic Rereading

The source argues that a company must be able to reread its own past. When the ontology or later context changes, an old interaction may acquire new meaning: a casual objection can become churn evidence, a technical concern can explain a launch slip, or an email approval can become precedent.

A static archive stores the sentence once. A living [[wiki/concepts/Context Graph]] allows the same sentence to be reinterpreted as relationships, risks, commitments, and evidence change over time. ^[inferred]

## Boundary with Surveillance

Ontology also shapes permission boundaries. If every conversational trace becomes a company-wide record, interaction memory becomes surveillance. If nothing is interpreted, the company keeps losing rationale.

A trustworthy ontology must distinguish personal context, team context, company record, quoteable evidence, summarized evidence, and aggregate signal.

## Related

- [[wiki/concepts/Interaction Memory]]
- [[wiki/concepts/Company Brain]]
- [[wiki/concepts/Context Graph]]
- [[wiki/concepts/Organizational Memory]]
- [[wiki/concepts/Factual Memory]]
- [[wiki/concepts/Semantic File System]]
- [[wiki/topics/AI Memory]]
- [[wiki/sources/Company Brain Source Guide]]
