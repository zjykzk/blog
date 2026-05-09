---
title: Autoregressive Decoding
type: concept
status: seed
summary: Autoregressive decoding generates one token at a time because each newly sampled token becomes part of the context for the next step.
category: concepts
sources:
  - inline:life-of-a-token-2026-05-09
created: 2026-05-09T00:00:00+08:00
updated: 2026-05-09T00:00:00+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-09
provenance:
  extracted: 0.9
  inferred: 0.1
  ambiguous: 0.0
aliases:
  - autoregressive generation
  - token-by-token decoding
tags:
  - ai
  - llm
  - inference
  - decoding
---

# Autoregressive Decoding

Autoregressive decoding is the loop where an LLM samples one token, appends it to the context, and uses the enlarged context to predict the next token.

## Key Ideas

- The next output token depends on all previous tokens, including tokens the model generated in earlier steps.
- This creates a loop-carried dependency: token `n + 1` cannot be computed before token `n` has been sampled.
- The prompt can be processed in parallel during prefill, but generated output tokens are produced serially during decode.
- [[wiki/concepts/KV Cache]] reduces repeated work by keeping prior key/value tensors, but it does not remove the causal dependency between generated tokens.
- Sampling controls such as temperature, top-k, top-p, and greedy decoding choose how the probability distribution becomes a concrete next token.

## Why it matters

Autoregressive decoding is the mechanical reason output tokens are expensive: each visible token requires another model step, another read of model weights, and another update to request state. ^[inferred]

This makes [[wiki/concepts/Prefill Decode Split]], [[wiki/concepts/Continuous Batching]], and [[wiki/concepts/Speculative Decoding]] central serving concerns rather than optional optimizations.

## Related

- [[wiki/concepts/Next-Token Pipeline]]
- [[wiki/concepts/KV Cache]]
- [[wiki/concepts/Prefill Decode Split]]
- [[wiki/concepts/Continuous Batching]]
- [[wiki/concepts/Speculative Decoding]]
- [[wiki/sources/Life of a Token Source Guide]]
