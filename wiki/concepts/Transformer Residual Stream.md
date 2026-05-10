---
title: Transformer Residual Stream
type: concept
status: seed
summary: The transformer residual stream carries token representations across layers while attention and FFN sublayers add learned deltas into it.
category: concepts
sources:
  - inline:life-of-a-token-2026-05-09
created: 2026-05-09T00:00:00+08:00
updated: 2026-05-09T00:00:00+08:00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-09
provenance:
  extracted: 0.84
  inferred: 0.16
  ambiguous: 0.0
aliases:
  - residual stream
  - transformer residual path
tags:
  - llm
  - transformer
  - inference
---
# Transformer Residual Stream

The transformer residual stream is the running hidden representation that survives across layers while each attention or feed-forward sublayer adds an incremental update.

## Key Ideas

- In the article's analogy, the residual stream is the main road; attention and FFN blocks are service areas that read the current state, compute a delta, and merge the delta back.
- Each transformer block preserves the same hidden-state shape while changing the representation's content.
- Residual connections help preserve earlier information because later layers add to the stream rather than fully replacing it.
- Residual connections also give gradients a direct additive path during training.
- The final hidden state can be read as the accumulated result of embedding information plus all attention and FFN updates.

## Why it matters

The residual-stream view helps separate routing from accumulation: attention can move contextual signals between positions, FFNs can inject learned feature updates, and the stream preserves their cumulative effect for the LM head. ^[inferred]

It also explains why intermediate probes such as logit lens can be suggestive without being exact: intermediate residual states are not necessarily optimized to be decoded directly. ^[inferred]

## Related

- [[wiki/concepts/Next-Token Pipeline]]
- [[wiki/concepts/LLM]]
- [[wiki/topics/LLM Inference Systems]]
- [[wiki/sources/Life of a Token Source Guide]]
