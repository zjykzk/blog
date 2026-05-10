---
title: Speculative Decoding
type: concept
status: seed
summary: Speculative decoding proposes multiple cheap draft tokens and verifies them with the large model to reduce expensive decoding steps.
category: concepts
sources:
  - https://www.aleksagordic.com/blog/vllm
created: 2026-05-06T12:17:59+08:00
updated: 2026-05-06T12:17:59+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-06
provenance:
  extracted: 0.9
  inferred: 0.1
  ambiguous: 0.0
aliases:
  - specdec
tags:
  - llm
  - inference
  - decoding
---
# Speculative Decoding

Speculative decoding accelerates autoregressive generation by using a cheaper proposal mechanism to draft several candidate tokens, then asking the large model to verify them in one pass.

The source describes the standard form as draft, verify, then accept/reject from left to right. The large model remains the distribution that matters; the draft model only proposes candidates.

## Acceptance logic

For each draft token, the large model either accepts it directly, accepts it probabilistically according to the ratio between large-model and draft probabilities, or rejects and samples from a corrected distribution.

If all drafted tokens are accepted, the large model can also provide one additional token from the same verification pass.

This is why the method can preserve the target model's sampling distribution while reducing the number of large-model decode steps.

## vLLM variants

The source notes that vLLM V1 focuses on proposal schemes such as n-gram, EAGLE, and Medusa rather than the simple small-draft-LLM method.

Operationally, the inference engine must allocate enough cache slots for the drafted tokens, run a large-model forward pass over the candidate continuation, then use a rejection sampler instead of ordinary next-token sampling.

## Related

- [[wiki/topics/LLM Inference Systems]]
- [[wiki/concepts/Prefill Decode Split]]
- [[wiki/concepts/Continuous Batching]]
- [[wiki/sources/vLLM Inference Systems Source Guide]]
