---
title: Life of a Token Source Guide
type: source
status: seed
summary: Source guide for the Life of a Token article, focused on the next-token path through tokenization, embeddings, attention, FFN, residual stream, sampling, cache, and GPU limits.
category: sources
sources:
  - inline:life-of-a-token-2026-05-09
created: 2026-05-09T00:00:00+08:00
updated: 2026-05-09T00:00:00+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-09
provenance:
  extracted: 0.94
  inferred: 0.06
  ambiguous: 0.0
aliases:
  - Life of a Token
  - LLM Next-Token Pipeline Source Guide
tags:
  - source
  - ai
  - llm
  - inference
  - transformer
---

# Life of a Token Source Guide

This page tracks the pasted article "Life of a Token: LLM's Next-Token Pipeline" as a source for the model-internal side of the AI inference cluster.

## Source identity

- Source: inline paste, `inline:life-of-a-token-2026-05-09`
- Title: Life of a Token: LLM's Next-Token Pipeline
- Model traced: GPT-2 Small
- Main example: `The capital of France is` → ` Paris`
- Scope: tokenization, embedding, positional encoding, self-attention, FFN, residual stream, LM head, sampling, autoregressive decoding, KV cache, and GPU execution.

## Extracted claims

- LLMs process text as token IDs, not as raw characters or words.
- GPT-2 uses BPE tokenization and a 50,257-token vocabulary.
- Token IDs are arbitrary lookup keys; semantic computation starts after token IDs are mapped into embedding vectors.
- GPT-2 Small maps each token into a 768-dimensional hidden representation.
- Position information is added because token embeddings alone do not encode sequence order.
- Self-attention routes information between positions using query, key, and value projections.
- Causal masking prevents a position from attending to future tokens, so next-token prediction uses the last position's hidden state.
- Feed-forward networks can be read as key-value memory-like modules that match patterns and inject learned feature updates.
- Residual connections let each transformer sublayer add a delta to a shared stream rather than replacing the whole representation.
- The LM head maps the final hidden vector back into logits over the vocabulary.
- Sampling turns the probability distribution into one token using choices such as greedy decoding, temperature, top-k, or top-p.
- Autoregressive generation must feed each generated token back into the next step, so output tokens are generated serially.
- [[wiki/concepts/KV Cache]] avoids recomputing prior key/value tensors during decode.
- Decode can be memory-bandwidth-bound because each new token reuses the whole model but performs relatively little computation.
- [[wiki/concepts/Continuous Batching]] improves hardware utilization by letting multiple decode streams share loaded weights.

## Integration decisions

The source strengthens [[wiki/topics/LLM Inference Systems]] by adding the model-internal token pipeline beneath the serving-system view from vLLM.

The durable concepts extracted from this source are [[wiki/concepts/Next-Token Pipeline]], [[wiki/concepts/Tokenization]], [[wiki/concepts/Transformer Residual Stream]], [[wiki/concepts/Autoregressive Decoding]], and [[wiki/concepts/Neural Network Inference Boundary]].

## Open questions

- Which numerical traces are stable across tokenizer/model/library versions, and which are artifacts of the exact GPT-2 checkpoint and prompt? ^[ambiguous]
- How should mechanistic-interpretability probes be represented without overstating what they prove about the model's actual decision path? ^[inferred]

## Related

- [[wiki/topics/LLM Inference Systems]]
- [[wiki/concepts/LLM]]
- [[wiki/concepts/KV Cache]]
- [[wiki/concepts/Prefill Decode Split]]
- [[wiki/maps/AI Map]]
