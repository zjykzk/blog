---
title: AI Memory
type: topic
status: seed
category: topics
summary: AI Memory is the persistent state layer that lets agents retain, retrieve, update, and consolidate experience beyond a single context window.
sources:
  - https://baijia.online/homepage/survey/Survey%20on%20AI%20Memory.pdf
  - https://nanothoughts.substack.com/p/company-brain-why-most-companies
created: 2026-05-05T16:25:00+08:00
updated: 2026-05-08T15:58:41+08:00
base_confidence: 0.52
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.78
  inferred: 0.20
  ambiguous: 0.02
aliases:
  - agent memory
  - LLM memory
tags:
  - ai
  - agents
  - memory
  - context
---

# AI Memory

AI Memory is the persistence layer that lets an AI system retain historical information, retrieve it into active context, update it over time, and consolidate repeated experience into more reusable forms.

The survey [[wiki/sources/AI Memory Survey Source Guide]] frames memory as a core capability for agents because standard LLM calls are bounded by finite [[wiki/topics/Context Management]] and usually stateless across sessions.

## Why Memory Matters

Memory shifts an AI system from isolated response generation toward continuous adaptation.

The survey emphasizes several capabilities:

- behavioral coherence across long interactions
- personalization through user preference and profile retention
- experience reuse across related tasks
- long-horizon planning supported by task history
- multi-agent collaboration through shared artifacts or shared memory
- lifelong improvement through reflection, consolidation, and knowledge updating

This makes memory part of [[wiki/topics/AI Harness]], not just an application database. The harness decides what gets encoded, what gets retrieved, what gets forgotten, and what can be trusted.

## Boundaries

The survey distinguishes several neighboring ideas:

- **LLM memory**: parametric weights and runtime context mechanics that support immediate prediction.
- **Agent memory**: workflow-oriented storage used by perception, planning, action, reflection, and tool use.
- **AI memory**: the broader cognitive layer for persistence, adaptation, and lifelong evolution.
- **Context**: the active bounded window used for the current inference step.
- **Knowledge**: consolidated, stable abstractions derived from validated memory.
- **Experience**: processed memory that becomes transferable strategy or skill.

The useful operational loop is: store historical traces, retrieve relevant pieces into context, use them for action, then update memory from the result.

## Design Patterns

The survey derives three memory design patterns from cognitive psychology and neuroscience:

- **Index and content separation**: keep compact retrieval keys or indexes separate from richer stored content.
- **Multiphase consolidation**: turn recent traces into summaries, reflections, skills, or stable knowledge at selected moments.
- **Structured workspace coordination**: use specialized buffers and a controller to integrate verbal, visual, tool, and long-term information before action.

These patterns connect directly to [[wiki/concepts/Context Information Density]]: memory should improve what the model can use now, not simply maximize what the system remembers. ^[inferred]

## Evaluation Lens

Memory quality should not be evaluated only by recall. The survey organizes evaluation around:

- retrieval accuracy and recall
- knowledge updating and temporal reasoning
- personalization and preference adherence
- sequential decision quality in stateful environments
- multimodal memory over image, audio, video, and embodied traces
- cost, latency, capacity, and privacy constraints

For agent systems, memory is successful when it improves downstream behavior under real task constraints, not when it merely stores more records. ^[inferred]

## Organizational Memory Layer

[[wiki/sources/Company Brain Source Guide]] extends the memory problem from individual agents to organizations. A company also needs memory that can bear on present decisions: why a customer request mattered, which tradeoffs were considered, who owned the context, and which assumptions conflicted.

This adds a group-level counterpart to agent memory: [[wiki/concepts/Organizational Memory]] stores not only artifacts, but decision rationale and "who knows what" signals. For enterprise agents, this memory becomes upstream context; without it, an agent can retrieve company data while missing why the data means what it means. ^[inferred]

A [[wiki/concepts/Company Brain]] can be read as organization-scale AI memory plus communication capture, [[wiki/concepts/Context Graph|context graph]] reasoning, and [[wiki/concepts/Governed Action|governed action]]. ^[inferred]

## Related

- [[wiki/concepts/AI Memory 4W Taxonomy]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Context Information Density]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/concepts/Company Brain]]
- [[wiki/concepts/Organizational Memory]]
- [[wiki/concepts/Context Graph]]
- [[wiki/sources/Company Brain Source Guide]]
- [[wiki/sources/AI Memory Survey Source Guide]]
