---
title: Lost in the Middle Effect
type: concept
status: seed
category: concepts
summary: The lost-in-the-middle effect is the long-context failure mode where models use information best at the beginning or end and worse in the middle.
sources:
  - https://arxiv.org/abs/2307.03172
created: 2026-05-05T15:45:00+08:00
updated: 2026-05-05T15:45:00+08:00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.82
  inferred: 0.18
  ambiguous: 0.0
aliases:
  - lost in the middle
  - long-context positional bias
  - middle-context degradation
tags:
  - ai
  - llm
  - context
  - evaluation
---

# Lost in the Middle Effect

The lost-in-the-middle effect is a long-context failure mode: language models often perform best when relevant information appears at the beginning or end of the input context, and worse when the same information appears in the middle.

The paper [[wiki/sources/Lost in the Middle Paper Source Guide]] finds this pattern in multi-document question answering and in a synthetic key-value retrieval task.

## Core Pattern

The effect appears as a U-shaped performance curve:

- information near the beginning benefits from primacy bias
- information near the end benefits from recency bias
- information in the middle is less reliably retrieved or used

This means nominal context length is not the same as usable context length.

## Why It Matters

For [[wiki/topics/Context Management]], the effect turns context ordering into a correctness issue, not just a formatting detail.

Adding more documents can increase retriever recall while reducing or barely improving answer accuracy, because the reader model may fail to use the extra context effectively.

For [[wiki/concepts/Context Information Density]], the effect sharpens the density target: relevant information must not only be present, but also placed where the model can actually use it.

## Design Implications

The paper suggests several practical implications:

- evaluate long-context models by moving relevant information across positions, not just by testing maximum window size
- avoid assuming an extended-context model is better at using context than its shorter-context counterpart
- rerank or truncate retrieved documents so likely-answering evidence appears in high-utility positions
- treat middle placement as a risk when building retrieval-augmented generation prompts

For agent systems, this becomes a harness responsibility: the [[wiki/topics/AI Harness]] should decide not only what enters context, but where decision-critical evidence lands. ^[inferred]

## Related

- [[wiki/topics/Context Management]]
- [[wiki/concepts/Context Information Density]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/Lost in the Middle Paper Source Guide]]
- [[wiki/sources/Agent Systems Papers Source Guide]]
