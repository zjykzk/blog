---
title: Next-Token Pipeline
type: concept
status: seed
summary: The next-token pipeline turns text into token IDs, vectors, contextual hidden states, logits, probabilities, and finally one sampled output token.
category: concepts
sources:
  - inline:life-of-a-token-2026-05-09
created: 2026-05-09T00:00:00+08:00
updated: 2026-05-09T00:00:00+08:00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-09
provenance:
  extracted: 0.9
  inferred: 0.1
  ambiguous: 0.0
aliases:
  - LLM next-token pipeline
  - token pipeline
tags:
  - llm
  - inference
  - transformer
---
# Next-Token Pipeline

The next-token pipeline is the sequence of transformations that turns an input string into a probability distribution over the next token, then samples one token from that distribution.

## Key Ideas

- The pipeline begins with [[wiki/concepts/Tokenization]], which converts text into token IDs.
- Token IDs are lookup keys, not semantic numbers; embeddings convert them into vectors that can participate in dot products, additions, and matrix multiplications.
- Position information is added so the model can distinguish the same token appearing in different sequence positions.
- Transformer layers repeatedly combine self-attention, feed-forward computation, normalization, and [[wiki/concepts/Transformer Residual Stream|residual stream]] updates.
- Self-attention routes information across prior positions; FFN layers transform each position independently after routing has happened.
- The final hidden vector at the last position is projected by the LM head into logits over the vocabulary.
- Softmax and sampling turn logits into the next token; [[wiki/concepts/Autoregressive Decoding]] then feeds that token back into the next step.

## Why it matters

The pipeline separates model computation from serving-system orchestration. The model computes logits from a context; [[wiki/topics/LLM Inference Systems]] decide how to batch, cache, schedule, and serve that computation. ^[inferred]

This distinction explains why a model can be fixed while latency, cost, and throughput change dramatically under different [[wiki/concepts/KV Cache]], [[wiki/concepts/Prefill Decode Split]], and [[wiki/concepts/Continuous Batching]] designs.

## Related

- [[wiki/concepts/LLM]]
- [[wiki/concepts/Neural Network Inference Boundary]]
- [[wiki/topics/LLM Inference Systems]]
- [[wiki/sources/Life of a Token Source Guide]]
