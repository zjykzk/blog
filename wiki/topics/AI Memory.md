---
title: AI Memory
type: topic
status: seed
category: topics
summary: AI Memory is the persistent state layer that lets agents and organizations retain, retrieve, update, and learn from experience beyond one context window.
sources:
  - https://baijia.online/homepage/survey/Survey%20on%20AI%20Memory.pdf
  - https://nanothoughts.substack.com/p/company-brain-why-most-companies
  - https://open.substack.com/pub/nanothoughts/p/company-brain-part-2-factual-memory?utm_campaign=post&utm_medium=web
  - https://open.substack.com/pub/nanothoughts/p/company-brain-part-3-interaction?utm_campaign=post&utm_medium=web
  - https://nanothoughts.substack.com/p/company-brain-part-4-action-memory
  - https://x.com/hwchase17/status/2040467997022884194
created: 2026-05-05T16:25:00+08:00
updated: 2026-05-09T22:17:54+08:00
base_confidence: 0.78
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.79
  inferred: 0.19
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

Part 2 names [[wiki/concepts/Factual Memory]] as the first layer of this company-scale memory. It is not just retrieval: it needs provenance, permissions, ownership, freshness, source-of-truth boundaries, and role-specific answers. The proposed implementation shape is closer to a [[wiki/concepts/Semantic File System]] than to a central repository or enterprise-search chatbot.

Part 3 adds [[wiki/concepts/Interaction Memory]] as a second organization-scale layer. It stores interpreted communication traces: decisions, commitments, objections, assumptions, dependencies, risks, and unresolved questions. This layer depends on [[wiki/concepts/Organizational Ontology]] because the same conversation can mean different things from product, legal, customer, sales, action, or executive lenses.

Part 4 adds [[wiki/concepts/Action Memory]] as the third layer. It stores procedures, triggers, execution traces, and outcomes so company memory can notice when conditions changed, select the right path, respect guardrails, and learn from what happened after action.

## Context-Level Continual Learning

[[wiki/sources/Continual Learning for AI Agents Source Guide]] sharpens the boundary between memory and other learning layers. Context-level learning updates configuration outside the harness: instructions, skills, tools, user memory, team memory, org memory, or tenant memory.

The source distinguishes two update timings: hot-path memory writes while the agent is working, and background consolidation jobs that process recent traces after the fact. Hot-path writes make memory immediately usable; background writes reduce interaction latency and can apply more deliberate consolidation. ^[inferred]

This means AI memory design must answer not only what to store, but also when to store it, who or what scope owns it, and whether the update was explicitly requested or harness-initiated. ^[inferred]


## Related

- [[wiki/concepts/AI Memory 4W Taxonomy]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Context Information Density]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/concepts/Company Brain]]
- [[wiki/concepts/Organizational Memory]]
- [[wiki/concepts/Context Graph]]
- [[wiki/concepts/Factual Memory]]
- [[wiki/concepts/Semantic File System]]
- [[wiki/concepts/Interaction Memory]]
- [[wiki/concepts/Action Memory]]
- [[wiki/concepts/Organizational Ontology]]
- [[wiki/sources/Company Brain Source Guide]]
- [[wiki/sources/AI Memory Survey Source Guide]]
