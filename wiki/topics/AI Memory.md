---
title: AI Memory
type: topic
status: seed
category: topics
summary: AI Memory is the persistent state layer that lets agents retain, manage, retrieve, forget, and evaluate experience beyond one context window.
sources:
  - https://baijia.online/homepage/survey/Survey%20on%20AI%20Memory.pdf
  - https://nanothoughts.substack.com/p/company-brain-why-most-companies
  - https://open.substack.com/pub/nanothoughts/p/company-brain-part-2-factual-memory?utm_campaign=post&utm_medium=web
  - https://open.substack.com/pub/nanothoughts/p/company-brain-part-3-interaction?utm_campaign=post&utm_medium=web
  - https://nanothoughts.substack.com/p/company-brain-part-4-action-memory
  - https://x.com/hwchase17/status/2040467997022884194
  - https://arxiv.org/abs/2603.07670
  - https://arxiv.org/abs/2605.03354v2
created: 2026-05-05T16:25:00+08:00
updated: 2026-06-10T21:35:12+08:00
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.81
  inferred: 0.17
  ambiguous: 0.02
aliases:
  - agent memory
  - LLM memory
tags:
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

## Agent Memory as a Managed Feedback Loop

[[wiki/sources/Memory for Autonomous LLM Agents Source Guide]] sharpens the operational model: memory is a write–manage–read loop coupled to perception, action, and feedback, not a passive append-only log.

The write side must filter, canonicalize, deduplicate, score priority, resolve contradictions, and delete when appropriate. The read side must decide whether retrieval is needed, reformulate queries when the immediate input is a poor query, rerank records, and budget context tokens.

This makes [[wiki/concepts/Agent Memory Write-Manage-Read Loop]] a central design model for long-running agents. A memory system fails not only when it forgets, but also when it writes the wrong thing, retrieves stale evidence, or keeps a false reflection alive.

## Mechanism Families and Evaluation

The same paper groups memory mechanisms into [[wiki/concepts/Agent Memory Mechanism Families]]: context-resident compression, retrieval stores, reflective memory, hierarchical virtual context, policy-learned control, and parametric memory.

Its evaluation lesson is that recall is not enough. [[wiki/concepts/Agent Memory Evaluation Stack]] asks whether memory improves task outcomes, preserves memory quality, stays efficient, and obeys governance requirements.

This reinforces a practical rule: long context is not memory. Long context enlarges working memory, but it does not by itself provide cross-session persistence, structured organization, selective retrieval, deletion, access control, or regression-tested memory behavior.

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

## Feedback Guideline Memory

[[wiki/sources/Memory-as-a-Tool Paper River Source Guide]] adds a feedback-specific memory pattern. Self-correction methods such as Self-Refine and Reflexion make current answers better, but their feedback signal often remains local to the current task or episode.

Memory-as-a-Tool treats rubric feedback as something that can be distilled into readable guideline files. The agent pays the cost of critique once, writes an abstract principle into a memory file, and later retrieves the relevant principle before answering a similar task. This makes memory less like a raw history store and more like a working manual that accumulates tested behavioral rules. ^[inferred]

The design pressure shifts from storage to governance: guideline memory needs naming, provenance, merge/split rules, conflict resolution, forgetting, and regression tests so bad abstractions do not become durable errors. ^[inferred]


## Circuit-Level Memory Diagnostics

[[wiki/sources/What Happens Inside Agent Memory Paper Source Guide]] adds a mechanistic layer beneath the external write–manage–read loop. The paper traces Qwen-3 memory-stage circuits across mem0 and A-MEM and reports that Manage routing becomes detectable before Write/Read content extraction and grounding.

The practical distinction is important for agent memory design: a small model may emit legal add/update/delete/none decisions before it can reliably represent the content those decisions are supposed to manage. That means routing competence must not be treated as proof of memory competence.

The source also reframes memory observability. A final wrong answer may come from a Write failure, a Manage failure, or a Read failure, and ordinary end-to-end accuracy hides this distinction. Circuit-level or stage-level diagnostics are useful because they try to localize the responsible operation rather than only measuring aggregate recall. ^[inferred]

The paper's numeric claims remain source-level: the reported 76.2% unsupervised localization accuracy, the 0.6B/4B emergence boundary, and the late-layer shared hub all come from one Qwen-3/transcoder setup.

## Related

- [[wiki/concepts/Agent Memory Write-Manage-Read Loop]]
- [[wiki/concepts/Agent Memory Mechanism Families]]
- [[wiki/concepts/Agent Memory Evaluation Stack]]
- [[wiki/sources/Memory for Autonomous LLM Agents Source Guide]]
- [[wiki/sources/What Happens Inside Agent Memory Paper Source Guide]]
- [[wiki/sources/Memory-as-a-Tool Paper River Source Guide]]

- [[wiki/concepts/AI Memory 4W Taxonomy]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Context Information Density]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/concepts/Company Brain]]
- [[wiki/concepts/Organizational Memory]]
- [[wiki/concepts/Context Graph]]
- [[wiki/syntheses/AI Memory × Context Graph]] — synthesis
- [[wiki/concepts/Factual Memory]]
- [[wiki/concepts/Semantic File System]]
- [[wiki/concepts/Interaction Memory]]
- [[wiki/concepts/Action Memory]]
- [[wiki/concepts/Organizational Ontology]]
- [[wiki/sources/Company Brain Source Guide]]
- [[wiki/sources/AI Memory Survey Source Guide]]
