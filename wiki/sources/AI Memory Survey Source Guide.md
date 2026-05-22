---
title: AI Memory Survey Source Guide
type: source
status: seed
category: sources
summary: Source guide for Survey on AI Memory, focused on memory theory, the 4W taxonomy, single/multi-agent memory, evaluation, and open challenges.
sources:
  - https://baijia.online/homepage/survey/Survey%20on%20AI%20Memory.pdf
created: 2026-05-05T16:25:00+08:00
updated: 2026-05-05T16:25:00+08:00
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.0
aliases:
  - Survey on AI Memory
  - AI Memory survey
tags:
  - paper
  - agents
  - memory
  - survey
---
# AI Memory Survey Source Guide

This page tracks "Survey on AI Memory: Theories, Taxonomies, Evaluations, and Emerging Trends" as a source for the AI / agent memory cluster.

## Source Role

The survey is a broad organizing source. Its value for this wiki is not a single benchmark result, but a vocabulary for relating memory, context, agent workflows, multi-agent collaboration, and evaluation.

The most reusable contribution is the [[wiki/concepts/AI Memory 4W Taxonomy]], which classifies memory by lifecycle, content type, storage form, and modality.

## Extracted Claims

- Memory enables agents to maintain behavioral coherence, make decisions from history, and collaborate more effectively.
- Standard LLMs face two memory-related bottlenecks: finite context windows and stateless interactions.
- AI memory can be distinguished from LLM memory and agent memory: LLM memory concerns prediction mechanics, agent memory supports autonomous workflows, and AI memory is the broader persistence and adaptation layer.
- Memory is distinct from context: context is the bounded runtime buffer, while memory persists outside a single inference call and is retrieved back into context when needed.
- Memory is distinct from knowledge: memory preserves dynamic, context-rich traces, while knowledge is consolidated for stability and reuse.
- Memory is distinct from experience: experience is processed memory that becomes transferable strategy or skill.
- The survey derives three design patterns from cognitive theories: index/content separation, multiphase consolidation, and structured workspace coordination.
- In multi-agent systems, memory supports explicit communication through natural language or structured schemas, implicit communication through latent/state sharing, and task- or step-level memory sharing.
- Memory evaluation spans factual recall, memory updating, personalization, stateful environment tasks, multimodal memory, latency, capacity, and privacy.

## Promoted Knowledge

### [[wiki/topics/AI Memory]]

The survey justifies a topic page for memory as a persistent state layer in agent systems.

### [[wiki/concepts/AI Memory 4W Taxonomy]]

The survey's 4W taxonomy is the cleanest new concept to preserve as a reusable classifier.

### [[wiki/topics/Context Management]]

The survey clarifies that memory and context form a loop: memory persists outside the active window, while context is the runtime workspace into which selected memory is injected.

### [[wiki/syntheses/Agent System Design Space]]

The survey adds memory lifecycle, content type, storage representation, modality, sharing, and governance as design surfaces for comparing agent systems.

## Open Questions

- Which memory evaluation metrics predict real agent task success rather than isolated recall?
- How should agents decide when a raw trace has earned promotion into durable knowledge or reusable experience? ^[inferred]
- How should shared memory in multi-agent systems handle provenance, write conflicts, and access control? ^[inferred]
- How should privacy and forgetting be implemented when memory contains user preferences, medical history, or long-term personal profiles?

## Related

- [[wiki/sources/Agent Systems Papers Source Guide]]
- [[wiki/sources/GenericAgent Paper Source Guide]]
- [[wiki/sources/Lost in the Middle Paper Source Guide]] — adjacent context-limit paper for the boundary between remembered state and active context.
- [[wiki/topics/AI Memory]]
- [[wiki/concepts/AI Memory 4W Taxonomy]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/Agent System Design Space]]
