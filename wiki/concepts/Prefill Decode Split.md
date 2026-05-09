---
title: Prefill Decode Split
type: concept
status: seed
summary: The prefill/decode split separates full-prompt processing from token-by-token generation because they stress GPU systems differently.
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
  extracted: 0.9
  inferred: 0.1
  ambiguous: 0.0
aliases:
  - prefill and decode
  - disaggregated prefill decode
tags:
  - ai
  - llm
  - inference
  - serving
---

# Prefill Decode Split

The prefill/decode split is the distinction between processing prompt tokens and generating output tokens.

In prefill, the model runs over the prompt and builds [[wiki/concepts/KV Cache]] state. In decode, the model processes the newest token while reading prior KV state for the full sequence.

The Life of a Token source frames this as a split between reading the known prompt and running [[wiki/concepts/Autoregressive Decoding|autoregressive decoding]]: prefill can process known input tokens together, but generated tokens must be produced one at a time because each sampled token changes the context for the next prediction.

## Different performance profiles

The source frames prefill as usually compute-bound and decode as often memory-bandwidth-bound.

That difference matters because a long prompt can monopolize an engine step if it is prefilling all at once, while decode traffic is latency-sensitive because users perceive inter-token delay.

## Chunked prefill

Chunked prefill handles long prompts by splitting prompt processing into smaller chunks, preventing one long prefill from blocking other requests for too long.

In vLLM V1, chunked prefill can be controlled with `long_prefill_token_threshold`, and it can also occur when a prompt exceeds the step token budget.

## Disaggregated P/D

Disaggregated prefill/decode goes further: separate prefill workers compute and upload KV state, while decode workers load that KV state and continue generation.

The source presents this as a way to control time-to-first-token and inter-token latency separately, especially when live traffic contains a shifting mix of long prompts and active decodes.

## Related

- [[wiki/topics/LLM Inference Systems]]
- [[wiki/concepts/Paged Attention]]
- [[wiki/concepts/Continuous Batching]]
- [[wiki/concepts/LLM Inference Benchmarking]]
- [[wiki/concepts/Autoregressive Decoding]]
- [[wiki/sources/vLLM Inference Systems Source Guide]]
- [[wiki/sources/Life of a Token Source Guide]]
