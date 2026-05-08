---
title: Interaction Memory
type: concept
status: seed
category: concepts
summary: Interaction memory preserves what people meant, debated, promised, assumed, and left unresolved before action memory decides what should happen next.
sources:
  - https://open.substack.com/pub/nanothoughts/p/company-brain-part-3-interaction?utm_campaign=post&utm_medium=web
  - https://nanothoughts.substack.com/p/company-brain-part-4-action-memory
created: 2026-05-08T20:54:16+08:00
updated: 2026-05-08T22:24:16+08:00
base_confidence: 0.61
lifecycle: draft
lifecycle_changed: 2026-05-08
provenance:
  extracted: 0.82
  inferred: 0.16
  ambiguous: 0.02
aliases:
  - company interaction memory
  - communication memory
  - organizational interaction memory
tags:
  - ai
  - memory
  - organization
  - coordination
---

# Interaction Memory

Interaction memory is the second layer of a [[wiki/concepts/Company Brain]]. It preserves what happened between people before artifacts appeared: why something happened, how people expected work to be done, which constraint mattered, which assumption was fragile, and what was left unsaid.

The source contrasts it with [[wiki/concepts/Factual Memory]]. Factual memory remembers artifacts and facts; interaction memory remembers how meaning was created in meetings, messages, emails, customer calls, complaints, and debates.

## Core Problem

Companies make many decisions in conversation, while databases and documents often record only the aftermath. A CRM field may say an account is at risk, but the customer call explains the real objection; a roadmap note may say launch slipped, but the meeting explains the tradeoff.

A transcript, summary, or meeting note is not enough. The hard problem is interpretation: what was actually decided, what was implied, what people disagreed about, which objection was real, and which casual commitment will later matter.

## Ontology Dependence

Interaction memory depends on [[wiki/concepts/Organizational Ontology]]. The same sentence can encode a launch plan, legal dependency, customer commitment, sales risk, follow-up, and non-final executive decision at once.

Because meaning depends on ontology and later context, interaction memory cannot be a static note archive. The company has to be able to reread its own past: a casual objection can later become churn evidence, a technical concern can explain a launch slip, and an email approval can become precedent.

## Context Graph Update

A useful interaction should update the [[wiki/concepts/Context Graph]], not only produce a note. It can change what the company believes, what it has promised, what remains unresolved, and what should happen next.

The graph needs to connect people, teams, customers, projects, commitments, decisions, risks, assumptions, dependencies, and time. This turns interactions into structured [[wiki/concepts/Organizational Memory]] rather than detached transcripts.

## Product Boundary

Interaction memory sits close to how people think, negotiate, disagree, and change their minds. Too little memory makes the company forget why things happened; too much memory creates noise or surveillance risk.

A trustworthy system must model permission boundaries: some interactions are personal, some are team context, some are company records, some can be summarized but not quoted, and some should update aggregate memory without exposing the raw conversation broadly.

## Interface Shape

The source argues that the interface should not be only a meeting recorder. Before an interaction, it should surface prior commitments, open issues, decision history, and unresolved questions. Afterward, it should identify decisions, assumptions, risks, and follow-ups. Later, it should notice cross-interaction patterns that no single person holds.

Example role-specific questions include:

- IC: what changed in the last architecture discussion, what assumptions still need validation, and who owns the next step?
- Manager: which commitments did the team make across customer calls and internal meetings this week, and which are implied but unassigned?
- CEO: where are teams making decisions from different assumptions?

## Bridge to Action

Interaction memory explains what people meant, debated, promised, and left unresolved. Without it, agents remain downstream of incomplete context: they may retrieve the ticket or update the CRM without knowing the human reason the work matters.

The source frames interaction memory as the bridge from memory toward action: once a company remembers facts and understands interaction meaning, it still needs [[wiki/concepts/Action Memory]] to know when work should wake up and [[wiki/concepts/Governed Action]] to decide whether to execute, ask, wait, escalate, or stop.

## Related

- [[wiki/concepts/Company Brain]]
- [[wiki/concepts/Factual Memory]]
- [[wiki/concepts/Organizational Ontology]]
- [[wiki/concepts/Context Graph]]
- [[wiki/concepts/Organizational Memory]]
- [[wiki/concepts/Action Memory]]
- [[wiki/concepts/Governed Action]]
- [[wiki/concepts/Institutional Friction]]
- [[wiki/topics/AI Memory]]
- [[wiki/sources/Company Brain Source Guide]]
