---
title: Agent Memory Mechanism Families
type: concept
status: seed
category: concepts
summary: Agent Memory Mechanism Families compares context compression, retrieval stores, reflection, hierarchical virtual memory, learned control, and parametric memory.
sources:
  - https://arxiv.org/abs/2603.07670
created: 2026-05-13T09:59:22+08:00
updated: 2026-05-13T09:59:22+08:00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-05-13
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.0
aliases: [memory mechanism families]
tags:
  - agents
  - memory
---
# Agent Memory Mechanism Families

Agent Memory Mechanism Families are the implementation families surveyed in [[wiki/sources/Memory for Autonomous LLM Agents Source Guide]] for turning agent history into usable future action.

## Families

1. **Context-resident compression** keeps memory in the prompt through windows, rolling summaries, hierarchical summaries, and task-conditioned compression.
2. **Retrieval-augmented memory stores** keep interaction records outside the prompt and retrieve them with vector search, sparse search, metadata filters, query reformulation, or structured writes.
3. **Reflective memory** stores self-critiques, post-mortems, and rules of thumb derived from success/failure trajectories.
4. **Hierarchical virtual context** pages information between active context, recall storage, archival stores, and sometimes multimodal or procedural stores.
5. **Policy-learned memory management** treats store, retrieve, update, summarize, and discard as actions optimized against downstream task performance.
6. **Parametric memory** stores knowledge in model weights or adapters, giving seamless use but weak auditability and deletion.

## Key Tradeoffs

Context-resident memory is transparent and cheap to prototype, but suffers summarization drift and attentional dilution.

Retrieval stores preserve more history, but shift the bottleneck from capacity to relevance: the agent needs records that are useful for the current decision, not just semantically similar.

Reflective memory can improve adaptation, but incorrect reflections can become self-reinforcing false beliefs unless grounded in specific episodic evidence.

Hierarchical memory gives the LLM an operating-system-like virtual memory illusion, but orchestration failures are often silent: the agent simply fails to page in the relevant record.

Learned memory control offers more headroom, but creates training cost, transfer, deletion, and interpretability risks.

## Design Implication

The families are not mutually exclusive. Production agents usually need a hybrid: context for live working state, external stores for durable records, reflection for reusable lessons, and instrumentation to see which memory operations actually helped. ^[inferred]

## Related

- [[wiki/topics/AI Memory]]
- [[wiki/concepts/Agent Memory Write-Manage-Read Loop]]
- [[wiki/concepts/Agent Memory Evaluation Stack]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/AI Memory 4W Taxonomy]]
- [[wiki/sources/Memory for Autonomous LLM Agents Source Guide]]
