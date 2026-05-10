---
title: LLM Inference Benchmarking
type: concept
status: seed
summary: LLM inference benchmarking compares latency, throughput, and goodput under request shapes and service-level objectives.
category: concepts
sources:
  - https://www.aleksagordic.com/blog/vllm
created: 2026-05-06T12:17:59+08:00
updated: 2026-05-06T12:17:59+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-06
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.0
aliases:
  - inference goodput
  - TTFT
  - ITL
tags:
  - llm
  - inference
  - benchmarking
---
# LLM Inference Benchmarking

LLM inference benchmarking measures how a serving system trades latency against throughput under concrete workloads.

The vLLM walkthrough names the core metrics:

- TTFT: time from request submission to first output token
- ITL: time between consecutive output tokens
- TPOT: average time per output token
- end-to-end latency: total request time
- throughput: tokens or requests processed per second
- goodput: throughput that satisfies service-level objectives

## Latency and throughput tension

For interactive products, users notice TTFT and ITL. For offline workloads, total token throughput may matter more.

The source's simplified roofline explanation is that larger decode batches can amortize model weight I/O and improve throughput, but after the hardware saturates, additional work increases per-step latency.

So benchmark results are only meaningful relative to workload shape and SLOs. ^[inferred]

## vLLM benchmarking modes

The source describes three vLLM benchmark entry points:

- `latency`: short input, fixed output, small batch, repeated iterations
- `throughput`: many prompts submitted together to measure aggregate processing rate
- `serve`: a live-server workload using sampled request arrivals and optional concurrency limits

This matters because a system can look good in offline throughput and still fail an interactive goodput target. ^[inferred]

## Related

- [[wiki/topics/LLM Inference Systems]]
- [[wiki/concepts/Prefill Decode Split]]
- [[wiki/concepts/Continuous Batching]]
- [[wiki/sources/vLLM Inference Systems Source Guide]]
