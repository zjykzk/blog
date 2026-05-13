---
title: Agent Memory Evaluation Stack
type: concept
status: seed
category: concepts
summary: Agent Memory Evaluation Stack evaluates memory through task effectiveness, memory quality, efficiency, and governance rather than recall alone.
sources:
  - https://arxiv.org/abs/2603.07670
created: 2026-05-13T09:59:22+08:00
updated: 2026-05-13T09:59:22+08:00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-05-13
provenance:
  extracted: 0.86
  inferred: 0.14
  ambiguous: 0.0
aliases: [memory evaluation stack]
tags:
  - agents
  - memory
---
# Agent Memory Evaluation Stack

Agent Memory Evaluation Stack is the practical evaluation model from [[wiki/sources/Memory for Autonomous LLM Agents Source Guide]] for judging memory by agentic utility, not isolated recall.

## Four Layers

1. **Task effectiveness**: success rate, factual correctness, and plan completion.
2. **Memory quality**: precision/recall of retrieved records, contradiction rate, staleness distribution, and coverage of task-relevant facts.
3. **Efficiency**: latency per memory operation, prompt tokens consumed by memory, retrieval calls per step, and storage growth.
4. **Governance**: privacy leakage, deletion compliance, and access-scope violations.

## Why Retrieval Metrics Are Not Enough

Precision@k and nDCG can show whether a document was retrieved, but not whether the agent used it correctly or whether the retrieval was worth the latency.

For long-running agents, memory evaluation must include stale records, contradictions, forgetting quality, and privacy/deletion behavior.

## Benchmark Lessons

The paper compares LoCoMo, MemBench, MemoryAgentBench, and MemoryArena. The stable lesson is that long context is not the same as memory: systems can recall facts in long conversations and still fail on multi-session, decision-relevant tasks.

MemoryArena is especially important because it embeds memory inside agentic tasks where later subtasks depend on what was learned earlier; near-saturated LoCoMo models drop to 40–60% there.

## Testing Practice

A useful regression suite should isolate write policy, retrieval strategy, compression module, and memory-use behavior. Otherwise a benchmark score hides which component actually helped or failed. ^[inferred]

## Related

- [[wiki/topics/AI Memory]]
- [[wiki/concepts/Agent Memory Mechanism Families]]
- [[wiki/concepts/Agent Memory Write-Manage-Read Loop]]
- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/Memory for Autonomous LLM Agents Source Guide]]
