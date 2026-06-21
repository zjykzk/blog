---
title: LLM Inference Systems
type: topic
status: seed
summary: LLM inference systems coordinate scheduling, KV cache memory, model execution, serving, scaling, and benchmarking to return tokens efficiently.
category: topics
sources:
  - https://www.aleksagordic.com/blog/vllm
  - inline:life-of-a-token-2026-05-09
created: 2026-05-06T12:17:59+08:00
updated: 2026-05-09T00:00:00+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-06
provenance:
  extracted: 0.86
  inferred: 0.14
  ambiguous: 0.0
aliases:
  - llm serving
  - inference engine
  - high-throughput inference
tags:
  - llm
  - inference
  - systems
---
# LLM Inference Systems

An LLM inference system is the runtime that turns incoming prompts into generated tokens under latency, throughput, memory, and serving constraints.

Aleksa Gordic's vLLM walkthrough is useful because it keeps the whole stack in one mental model: an offline engine, advanced decoding and cache features, multi-GPU execution, distributed serving, and benchmarking are layers of one token-serving system.

## Core loop

At the engine level, inference repeats three actions:

- schedule requests for the next step
- run a model forward pass and sample tokens
- postprocess outputs, detect stop conditions, and free finished request state

This loop is simple at the surface, but its behavior depends on how the system allocates [[wiki/concepts/KV Cache]] blocks, mixes prefill and decode work, and keeps request state across steps.

## Model-internal token path

The Life of a Token source adds the model-internal view below the serving loop: raw text becomes token IDs through [[wiki/concepts/Tokenization]], token IDs become vectors, transformer blocks update a [[wiki/concepts/Transformer Residual Stream|residual stream]], and the LM head projects the final hidden state into next-token logits.

That [[wiki/concepts/Next-Token Pipeline]] is still only one step of generation. [[wiki/concepts/Autoregressive Decoding]] wraps it in a serial loop where each sampled token is appended before the next token can be predicted.

## Main design pressures

High-throughput inference has to manage several tensions at once:

- [[wiki/concepts/Prefill Decode Split]]: prompt processing is usually compute-bound, while token-by-token decoding is often memory-bandwidth-bound.
- [[wiki/concepts/Paged Attention]]: KV memory must be allocated without wasting large contiguous slabs.
- [[wiki/concepts/Continuous Batching]]: new and old requests should share model steps without padding every sequence to the same length.
- [[wiki/concepts/Autoregressive Decoding]]: output tokens create a causal loop-carried dependency, so decode must advance one sampled token at a time.
- [[wiki/concepts/Speculative Decoding]]: multiple candidate tokens can be proposed and verified to reduce the number of expensive large-model steps.
- [[wiki/concepts/LLM Inference Benchmarking]]: latency, throughput, and goodput pull the system toward different operating points.

This makes inference serving a systems problem, not only a model problem. ^[inferred]

## Serving stack

The source describes a progression from a synchronous single-process engine to a serving stack with asynchronous frontend tasks, data-parallel engine replicas, load balancing, and FastAPI/OpenAI-compatible endpoints.

The conceptual boundary is:

- engine core: scheduling, model execution, cache allocation, request state
- executor: single-process or multi-process GPU execution
- serving layer: request routing, async output handling, load balancing, and HTTP endpoints

That split helps keep the model execution path stable while adding web and distributed-system machinery around it. ^[inferred]

## Related

- [[wiki/concepts/Next-Token Pipeline]]
- [[wiki/concepts/Tokenization]]
- [[wiki/concepts/Autoregressive Decoding]]
- [[wiki/concepts/KV Cache]]
- [[wiki/topics/High Concurrency]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/sources/vLLM Inference Systems Source Guide]]
- [[wiki/sources/Life of a Token Source Guide]]
