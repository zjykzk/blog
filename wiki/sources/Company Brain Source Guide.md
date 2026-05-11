---
title: Company Brain Source Guide
type: source
status: seed
category: sources
summary: Source guide for NanoThoughts' Company Brain series, covering factual, interaction, action memory, and memory as shared state for governed agents.
sources:
  - https://nanothoughts.substack.com/p/company-brain-why-most-companies
  - https://open.substack.com/pub/nanothoughts/p/company-brain-part-2-factual-memory?utm_campaign=post&utm_medium=web
  - https://open.substack.com/pub/nanothoughts/p/company-brain-part-3-interaction?utm_campaign=post&utm_medium=web
  - https://nanothoughts.substack.com/p/company-brain-part-4-action-memory
  - https://nanothoughts.substack.com/p/memory-is-state-not-a-service
created: 2026-05-08T15:58:41+08:00
updated: 2026-05-11T10:27:21+08:00
base_confidence: 0.78
lifecycle: draft
lifecycle_changed: 2026-05-08
provenance:
  extracted: 0.85
  inferred: 0.13
  ambiguous: 0.02
aliases:
  - Company Brain article source guide
  - NanoThoughts Company Brain
  - Sentra company brain source
tags:
  - agents
  - organization
  - memory
---
# Company Brain Source Guide

This page guides NanoThoughts' Company Brain series, currently including "Company Brain: Why Most Companies Have Data But No Memory," "Company Brain, Part 2: Factual Memory," "Company Brain, Part 3: Interaction Memory," "Company Brain, Part 4: Action Memory," and "Memory is State, Not a Service."

## Source Identity

- Part 1 URL: https://nanothoughts.substack.com/p/company-brain-why-most-companies
- Part 2 URL: https://open.substack.com/pub/nanothoughts/p/company-brain-part-2-factual-memory?utm_campaign=post&utm_medium=web
- Part 2 accessible extraction URL: https://nanothoughts.substack.com/p/company-brain-part-2-factual-memory?utm_campaign=post&utm_medium=web&triedRedirect=true
- Part 3 URL: https://open.substack.com/pub/nanothoughts/p/company-brain-part-3-interaction?utm_campaign=post&utm_medium=web
- Part 3 accessible extraction URL: https://nanothoughts.substack.com/p/company-brain-part-3-interaction?utm_campaign=post&utm_medium=web&triedRedirect=true
- Part 4 URL: https://nanothoughts.substack.com/p/company-brain-part-4-action-memory
- Part 4 accessible extraction URL: https://nanothoughts.substack.com/p/company-brain-part-4-action-memory
- State-substrate article URL: https://nanothoughts.substack.com/p/memory-is-state-not-a-service
- Publication: NanoThoughts on Substack
- Main topic: organizational memory as the missing substrate for company agents and AI-native organizations
- Extraction note: the directly fetched Substack HTML contained each article body, extracted from the embedded `body_html` field. The user-provided open.substack.com URL was preserved as the source identity for Parts 2 and 3; Part 4 used the canonical NanoThoughts URL directly.

## Core Claims

- The hardest part of organizational work is often institutional friction: shared context decays across conversations, meetings, and follow-ups.
- AI makes this problem more visible because work can move faster while the shared context behind that work stays fragile.
- A company brain is not company-wide search, a document chatbot, meeting notes, or ordinary workflow automation.
- A company brain is a living, permissioned model of how an organization remembers, reasons, and acts.
- The company brain requires factual memory, interaction memory, a context graph and reasoning layer, and governed action.
- Agents fail not only because companies lack data, but because companies lack memory of why the data means what it means.
- Part 2 reframes factual memory as the first layer: it answers what exists, what happened, where the source is, who owns it, when it changed, and how a thing works.
- Factual memory should emerge from individual work becoming shared work and shared work becoming institutional memory, rather than demanding that people feed a central repository.
- Durable company memory needs provenance, permissions, ownership, freshness, source-of-truth boundaries, relationships between artifacts, and role-specific answers.
- The source describes this durable layer as closer to a semantic file system than to simple RAG over enterprise data.
- Part 3 frames interaction memory as the second layer: memory of what happened between people before artifacts existed.
- Interaction memory preserves why something happened, what people meant, what they debated, what they promised, which assumptions were fragile, and what was left unresolved.
- Transcripts and summaries are not enough because the hard problem is interpretation.
- Organizational ontology decides whether conversation fragments are remembered as decisions, commitments, objections, escalations, dependencies, assumptions, customer pains, owners, precedents, or open questions.
- A useful interaction memory updates the context graph, letting the company reread its own past as later evidence changes meaning.
- Permission boundaries are central because interaction memory can either feel like surveillance or like the company stopped losing the thread.
- Part 4 frames action memory as the third layer: memory of when workflows should wake up, when they should stay still, what path should run, and what happened after execution.
- Action memory has four parts: procedural memory, trigger memory, execution memory, and outcome memory.
- Doing nothing is a first-class action; a trusted company brain must know when to wait, ask approval, notify, stop, or deliberately not mutate a system.
- The action layer closes the loop by turning successful actions into precedent, failed actions into risk memory, human corrections into signals, and workflow changes into future operating memory.
- The state-substrate article argues that factual, interaction, and action memory only work as three views of one shared state; if each tool remembers separately, the company inherits fragmented local truths.
- Ontologies should act as lenses over the same underlying memory, allowing sales, product, support, legal, finance, executives, and agents to read the same artifact differently without splitting the substrate.
- State changes should be first-class memory primitives: what became true, who owns it, what commitment was created, what action followed, and what the outcome taught the company.

## Promotion Decisions

Promoted to concept pages:

- [[wiki/concepts/Company Brain]] — the source's central construct.
- [[wiki/concepts/Factual Memory]] — Part 2's first layer of company memory.
- [[wiki/concepts/Interaction Memory]] — Part 3's second layer of company memory.
- [[wiki/concepts/Action Memory]] — Part 4's third layer of company memory and the bridge from remembered context to operational continuity.
- [[wiki/concepts/Organizational Ontology]] — the interpretation scheme that turns conversation into structured memory.
- [[wiki/concepts/Semantic File System]] — the relationship-rich durable memory substrate contrasted with simple RAG and sharpened by the state-substrate article into entities, facts, state changes, and typed relationships.
- [[wiki/concepts/Organizational Memory]] — the decision-bearing memory layer.
- [[wiki/concepts/Context Graph]] — the reasoning layer connecting facts, decisions, tradeoffs, assumptions, commitments, and interactions.
- [[wiki/concepts/Governed Action]] — the action-coordination layer distinct from brittle automation.
- [[wiki/concepts/Institutional Friction]] — the organizational failure mode that motivates the source.

Across the series, updated existing pages:

- [[wiki/topics/AI Memory]] — extended from agent memory to organization-level memory substrates, including factual memory, interaction memory, action memory, and semantic file-system structure.
- [[wiki/topics/AI Harness]] — added company-brain context as an enterprise governance substrate for agents.
- [[wiki/syntheses/AI Engineering Workflow]] — added organizational substrate as a layer above coding-agent workflow.
- [[wiki/sources/Agent Engineering Source Guide]] — registered the series as an enterprise agent-source bridge.
- [[wiki/sources/Memory Is State Not a Service Source Guide]] — captured the state-substrate article as a focused source guide inside the same Company Brain cluster.
- [[wiki/maps/AI Map]] — added navigation entries for the new cluster.

## Relationship to Existing Wiki

This source extends the current AI / Agent cluster in three directions:

1. From single-agent memory and context management toward organization-level memory.
2. From central repositories and search boxes toward emergent memory across individual, team, company artifacts, and human communication.
3. From coding-agent harnesses toward enterprise action memory and action governance across human communication, data, workflows, outcomes, and agents.

It also connects the AI cluster to management and coordination topics because the base problem is organizational shared reality, not model capability alone. ^[inferred]

## Open Questions

- How should a company brain represent permission boundaries without becoming surveillance infrastructure?
- Which relationships in the semantic file system should be explicit, inferred, or left as source-linked traces?
- What minimum context graph is enough to improve decisions without requiring heavyweight ontology work?
- Which wedge wins commercially: meeting communication, enterprise search, workflow automation, or integrated operating-system capture?
- How should agents cite organizational memory when acting on behalf of different roles?
- Which action outcomes should become precedent, risk memory, or workflow changes?
- How can the system model doing nothing as an auditable, intentional action rather than absence of action?
- Which interaction ontology is stable enough for reliable memory but flexible enough to reinterpret past conversations?
- Does a single semantic memory substrate generalize across verticals while role and industry ontologies specialize, or do different verticals require different substrates?
- How should raw conversation, summary, aggregate signal, and company-record status be separated?

## Related

- [[wiki/concepts/Company Brain]]
- [[wiki/concepts/Organizational Memory]]
- [[wiki/concepts/Factual Memory]]
- [[wiki/concepts/Interaction Memory]]
- [[wiki/concepts/Action Memory]]
- [[wiki/concepts/Organizational Ontology]]
- [[wiki/concepts/Semantic File System]]
- [[wiki/concepts/Context Graph]]
- [[wiki/concepts/Governed Action]]
- [[wiki/concepts/Institutional Friction]]
- [[wiki/sources/Memory Is State Not a Service Source Guide]]
- [[wiki/topics/AI Memory]]
- [[wiki/topics/AI Harness]]
- [[wiki/sources/Agent Engineering Source Guide]]
