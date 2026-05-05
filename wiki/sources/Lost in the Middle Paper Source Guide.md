---
title: Lost in the Middle Paper Source Guide
type: source
status: seed
category: sources
summary: Source guide for the Lost in the Middle paper, focused on long-context positional bias and evaluation protocols for usable context.
sources:
  - https://arxiv.org/abs/2307.03172
created: 2026-05-05T15:45:00+08:00
updated: 2026-05-05T15:45:00+08:00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.0
aliases:
  - Lost in the Middle
  - How Language Models Use Long Contexts
tags:
  - paper
  - ai
  - llm
  - context
  - evaluation
---

# Lost in the Middle Paper Source Guide

This page tracks Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang's paper "Lost in the Middle: How Language Models Use Long Contexts" as a source for the AI / context-management cluster.

## Source Role

The paper is a high-value empirical source for [[wiki/topics/Context Management]] because it separates nominal context length from usable context.

Its durable contribution is not a new agent architecture. It is an evaluation lens: if a model robustly uses long context, its performance should not change much when relevant information moves from the beginning to the middle to the end of the same input.

## Extracted Claims

- The paper studies how language models use long contexts on multi-document question answering and key-value retrieval.
- Performance often follows a U-shaped curve: strongest when relevant information is at the beginning or end, weaker when it is in the middle.
- Extended-context variants are not necessarily better at using context than their shorter-context counterparts when both can fit the input.
- Some models can perform perfectly on synthetic key-value retrieval, but other models still degrade when the relevant key-value pair is in the middle.
- Encoder-decoder models are relatively robust within their training-time sequence length, but show middle-position degradation when evaluated beyond that length.
- Query-aware contextualization dramatically improves synthetic key-value retrieval, but minimally changes multi-document QA trends.
- Instruction fine-tuning alone does not explain the U-shaped curve; base and instruction-tuned models can both show it.
- In open-domain QA, reader accuracy can saturate before retriever recall, so adding more retrieved documents may yield only marginal answer improvement while increasing cost and latency.

## Promoted Knowledge

### [[wiki/concepts/Lost in the Middle Effect]]

The paper directly motivates a stable concept page for middle-context degradation and positional robustness.

### [[wiki/topics/Context Management]]

The paper strengthens the claim that context management must handle ordering and salience, not only compression and token budgeting.

### [[wiki/concepts/Context Information Density]]

The paper adds a positional constraint to density: information is not equally usable just because it is present inside the active window.

### [[wiki/syntheses/Agent System Design Space]]

The paper adds an evaluation surface for agent systems: how robustly does the system preserve and position decision-critical evidence under long contexts?

## Open Questions

- How should production RAG systems measure best-case versus worst-case positional performance?
- Should harnesses deliberately duplicate critical evidence at the start and end of context, or does that create too much redundancy? ^[inferred]
- How do newer long-context models after 2023 change the severity of this effect? ^[ambiguous]

## Related

- [[wiki/sources/Agent Systems Papers Source Guide]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Context Information Density]]
- [[wiki/concepts/Lost in the Middle Effect]]
- [[wiki/syntheses/Agent System Design Space]]
