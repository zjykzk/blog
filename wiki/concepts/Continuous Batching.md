---
title: Continuous Batching
type: concept
status: seed
summary: Continuous batching lets an inference engine mix newly arrived and already-running requests at each generation step.
category: concepts
sources:
  - https://www.aleksagordic.com/blog/vllm
  - inline:life-of-a-token-2026-05-09
created: 2026-05-06T12:17:59+08:00
updated: 2026-05-09T00:00:00+08:00
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-05-06
provenance:
  extracted: 0.86
  inferred: 0.14
  ambiguous: 0.0
aliases:
  - iteration-level batching
tags:
  - ai
  - llm
  - inference
  - scheduling
---

# Continuous Batching

Continuous batching lets an LLM inference engine reconsider the active batch at every engine step, so new requests can join while older requests continue decoding.

In the vLLM walkthrough, this is contrasted with a synchronous offline example where the engine receives a fixed prompt list and cannot inject new requests mid-run.

## Mechanism

The scheduler keeps waiting and running queues. At each step it can:

- schedule decode work for requests already running
- schedule prefill work for new requests waiting to enter execution
- allocate additional [[wiki/concepts/KV Cache]] blocks for the tokens being processed
- flatten active sequences into a single forward-pass representation

Custom attention kernels and [[wiki/concepts/Paged Attention]] metadata let this flattened execution avoid right-padding every request to the same length.

## Why it matters

Without continuous batching, an engine either wastes compute on padding or waits for a fixed batch to finish before accepting more work. Continuous batching improves utilization by treating the batch as a dynamic set of token work rather than a fixed group of requests. ^[inferred]

The Life of a Token source adds a hardware reason: decode often reuses the same model weights for very little per-token computation, so batching lets multiple requests amortize memory movement across more token work.

The tradeoff is that scheduling becomes a first-class part of [[wiki/topics/LLM Inference Systems]]: token budgets, cache block availability, preemption, and request priority all influence which tokens run next.

## Related

- [[wiki/concepts/Paged Attention]]
- [[wiki/concepts/Prefill Decode Split]]
- [[wiki/concepts/LLM Inference Benchmarking]]
- [[wiki/concepts/Autoregressive Decoding]]
- [[wiki/sources/vLLM Inference Systems Source Guide]]
- [[wiki/sources/Life of a Token Source Guide]]
