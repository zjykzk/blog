---
title: Company Brain
type: concept
status: seed
category: concepts
summary: A company brain is a permissioned organizational memory substrate where factual, interaction, and action memory turn company context into governed work.
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
  extracted: 0.82
  inferred: 0.16
  ambiguous: 0.02
aliases:
  - company memory substrate
  - enterprise general intelligence
  - organizational brain
tags:
  - agents
  - memory
  - organization
---
# Company Brain

A company brain is a living, permissioned model of how an organization remembers, reasons, and acts. The source argues that this is not merely company search, a document chatbot, meeting notes, or workflow automation. Part 4 makes the action layer explicit: the company must remember when work should wake up, which path should run, and how outcomes feed back into memory.

## Core Problem

The motivating problem is [[wiki/concepts/Institutional Friction]]: conversations lose context, meetings create ambiguous follow-ups, and different people leave with different versions of what was decided.

The source frames this as a coordination problem before it is an agent problem. AI increases the speed of work, but shared organizational context often remains fragile.

## Layered Structure

Across the series, a Company Brain has three progressively stronger memory/action layers:

- **[[wiki/concepts/Factual Memory]]**: what exists, what happened, where evidence lives, who owns it, when it changed, and how things connect.
- **[[wiki/concepts/Interaction Memory]]**: what people meant, debated, promised, assumed, and left unresolved before artifacts formalized the work.
- **[[wiki/concepts/Action Memory]]**: how the company moves; when workflows should wake up, when they should stay still, what guardrails apply, and what happened after execution.
- **[[wiki/concepts/Governed Action]]**: the execution-governance surface that decides whether to act, wait, ask, escalate, stop, or require approval.

The first article also describes the broader formula as factual memory + human communication + [[wiki/concepts/Context Graph]] and reasoning + governed action = company brain.

## Why Search Is Not Enough

Part 2 argues that factual memory is not a shared drive, wiki, enterprise search box, or simple RAG over enterprise data. Durable memory needs provenance, permissions, ownership, freshness, source-of-truth boundaries, and relationships between artifacts.

Part 3 adds that transcripts and summaries are also not enough. Many decisions are made in conversation; the later ticket, CRM update, roadmap note, or launch doc is often a compressed artifact of earlier interaction.

This connects to [[wiki/concepts/Organizational Memory]]: the company needs memory that can bear on present decisions, not only an archive of records.

## Interaction Layer

[[wiki/concepts/Interaction Memory]] is the layer where a Company Brain remembers how meaning was created. It should preserve why something happened, how people expected work to be done, what constraint mattered, which assumption was fragile, and what was left unsaid.

This layer depends on [[wiki/concepts/Organizational Ontology]]. A single meeting sentence can encode a launch plan, legal dependency, customer commitment, sales risk, action items, and a non-closed decision. The ontology decides what the system remembers.


## Action Layer

Part 4 names [[wiki/concepts/Action Memory]] as the third layer. It is partly agentic: it notices changed conditions, decides whether anything should happen, chooses a path, respects guardrails, and either acts or asks a human to act.

The source breaks action memory into procedural memory, trigger memory, execution memory, and outcome memory. This makes the company remember not only the official workflow, but also when the workflow becomes relevant, what actually happened, and whether the result was successful.

A key claim is that doing nothing is a first-class action. A trusted company brain must know when to wait, ask approval, notify without mutating a system, stop, or deliberately do nothing.

## Agent Implication

Agents fail not only because companies lack data. The series argues that agents also fail when companies lack memory of why data means what it means and how work should actually proceed after the context is understood.

A company brain therefore becomes part of the upstream substrate for [[wiki/topics/AI Harness]]: agents need permissions, provenance, lineage, context, interaction rationale, and escalation paths before they can safely act inside company systems. ^[inferred]

## Emergence from Individual Work

Part 2 argues that company memory should be built from the individual outward. A personal note may become a team doc; a team doc may become a roadmap decision; a roadmap decision may become a customer commitment.

Part 3 extends this outward path into communication: before many artifacts exist, the reason for work is created in meetings, messages, calls, and emails.

This creates a boundary problem: useful company memory must emerge from work traces without converting every private note, personal exchange, or half-formed opinion into a company record.

## Build Paths

The article names two possible architectures:

- **Aggregation**: connect to existing tools such as email, calendar, Slack, documents, CRM, project management, support, code, workflows, and meetings.
- **Vertical integration**: let a young company adopt memory, reasoning, and action as primitives from the beginning.

The author is unsure which architecture wins, but argues that companies that start earlier gain an advantage because context can form before it fragments.

## Open Questions

- Which parts of company memory should be modeled explicitly, and which should stay as provenance-linked traces?
- How can a company brain avoid becoming an executive surveillance dashboard?
- How should permissions and role-specific abstraction levels be represented so the same memory substrate can serve ICs, managers, CEOs, and agents?
- How can proactive factual, interaction, and action memory help work without making employees feel watched?
- What ontology is stable enough to structure interactions but flexible enough to let the company reread its own past?
- How can action memory capture actual operating paths without confusing useful exceptions with bad process hygiene?

## Related

- [[wiki/concepts/Organizational Memory]]
- [[wiki/concepts/Factual Memory]]
- [[wiki/concepts/Interaction Memory]]
- [[wiki/concepts/Action Memory]]
- [[wiki/concepts/Organizational Ontology]]
- [[wiki/concepts/Semantic File System]]
- [[wiki/concepts/Institutional Friction]]
- [[wiki/concepts/Context Graph]]
- [[wiki/concepts/Governed Action]]
- [[wiki/topics/AI Memory]]
- [[wiki/topics/AI Harness]]
- [[wiki/sources/Company Brain Source Guide]]
