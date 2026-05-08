---
title: Company Brain Source Guide
type: source
status: seed
category: sources
summary: Source guide for NanoThoughts' Company Brain series, covering factual memory, organizational context graphs, communication memory, and governed action.
sources:
  - https://nanothoughts.substack.com/p/company-brain-why-most-companies
  - https://open.substack.com/pub/nanothoughts/p/company-brain-part-2-factual-memory?utm_campaign=post&utm_medium=web
created: 2026-05-08T15:58:41+08:00
updated: 2026-05-08T20:38:05+08:00
base_confidence: 0.61
lifecycle: draft
lifecycle_changed: 2026-05-08
provenance:
  extracted: 0.84
  inferred: 0.14
  ambiguous: 0.02
aliases:
  - Company Brain article source guide
  - NanoThoughts Company Brain
  - Sentra company brain source
tags:
  - source
  - ai
  - agents
  - organization
  - memory
---

# Company Brain Source Guide

This page guides NanoThoughts' Company Brain series, currently including "Company Brain: Why Most Companies Have Data But No Memory" and "Company Brain, Part 2: Factual Memory."

## Source Identity

- Part 1 URL: https://nanothoughts.substack.com/p/company-brain-why-most-companies
- Part 2 URL: https://open.substack.com/pub/nanothoughts/p/company-brain-part-2-factual-memory?utm_campaign=post&utm_medium=web
- Part 2 accessible extraction URL: https://nanothoughts.substack.com/p/company-brain-part-2-factual-memory?utm_campaign=post&utm_medium=web&triedRedirect=true
- Publication: NanoThoughts on Substack
- Main topic: organizational memory as the missing substrate for company agents and AI-native organizations
- Extraction note: the directly fetched Substack HTML contained each article body, extracted from the embedded `body_html` field. The user-provided open.substack.com URL was preserved as the source identity for Part 2.

## Core Claims

- The hardest part of organizational work is often institutional friction: shared context decays across conversations, meetings, and follow-ups.
- AI makes this problem more visible because work can move faster while the shared context behind that work stays fragile.
- A company brain is not company-wide search, a document chatbot, meeting notes, or ordinary workflow automation.
- A company brain is a living, permissioned model of how an organization remembers, reasons, and acts.
- The company brain requires four integrated layers: factual memory, human communication, context graph and reasoning, and governed action.
- Agents fail not only because companies lack data, but because companies lack memory of why the data means what it means.
- Part 2 reframes factual memory as the first layer: it answers what exists, what happened, where the source is, who owns it, when it changed, and how a thing works.
- Factual memory should emerge from individual work becoming shared work and shared work becoming institutional memory, rather than demanding that people feed a central repository.
- Durable company memory needs provenance, permissions, ownership, freshness, source-of-truth boundaries, relationships between artifacts, and role-specific answers.
- The source describes this durable layer as closer to a semantic file system than to simple RAG over enterprise data.

## Promotion Decisions

Promoted to concept pages:

- [[wiki/concepts/Company Brain]] — the source's central construct.
- [[wiki/concepts/Factual Memory]] — Part 2's first layer of company memory.
- [[wiki/concepts/Semantic File System]] — the relationship-rich durable memory substrate contrasted with simple RAG.
- [[wiki/concepts/Organizational Memory]] — the decision-bearing memory layer.
- [[wiki/concepts/Context Graph]] — the reasoning layer connecting facts, decisions, tradeoffs, and assumptions.
- [[wiki/concepts/Governed Action]] — the action-coordination layer distinct from brittle automation.
- [[wiki/concepts/Institutional Friction]] — the organizational failure mode that motivates the source.

Across the series, updated existing pages:

- [[wiki/topics/AI Memory]] — extended from agent memory to organization-level memory substrates, including factual memory and semantic file-system structure.
- [[wiki/topics/AI Harness]] — added company-brain context as an enterprise governance substrate for agents.
- [[wiki/syntheses/AI Engineering Workflow]] — added organizational substrate as a layer above coding-agent workflow.
- [[wiki/sources/Agent Engineering Source Guide]] — registered the series as an enterprise agent-source bridge.
- [[wiki/maps/AI Map]] — added navigation entries for the new cluster.

## Relationship to Existing Wiki

This source extends the current AI / Agent cluster in two directions:

1. From single-agent memory and context management toward organization-level memory.
2. From central repositories and search boxes toward emergent memory across individual, team, and company artifacts.
3. From coding-agent harnesses toward enterprise action governance across human communication, data, workflows, and agents.

It also connects the AI cluster to management and coordination topics because the base problem is organizational shared reality, not model capability alone. ^[inferred]

## Open Questions

- How should a company brain represent permission boundaries without becoming surveillance infrastructure?
- Which relationships in the semantic file system should be explicit, inferred, or left as source-linked traces?
- What minimum context graph is enough to improve decisions without requiring heavyweight ontology work?
- Which wedge wins commercially: meeting communication, enterprise search, workflow automation, or integrated operating-system capture?
- How should agents cite organizational memory when acting on behalf of different roles?

## Related

- [[wiki/concepts/Company Brain]]
- [[wiki/concepts/Organizational Memory]]
- [[wiki/concepts/Factual Memory]]
- [[wiki/concepts/Semantic File System]]
- [[wiki/concepts/Context Graph]]
- [[wiki/concepts/Governed Action]]
- [[wiki/concepts/Institutional Friction]]
- [[wiki/topics/AI Memory]]
- [[wiki/topics/AI Harness]]
- [[wiki/sources/Agent Engineering Source Guide]]
