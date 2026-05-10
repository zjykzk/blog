---
title: Paged Attention
type: concept
status: seed
summary: Paged attention stores KV cache in fixed-size blocks so inference servers can allocate, reuse, and evict attention state efficiently.
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
  - paged KV cache
tags:
  - llm
  - inference
  - memory
---
# Paged Attention

Paged attention is an inference-server memory design that stores [[wiki/concepts/KV Cache]] state in fixed-size blocks rather than requiring each request to own one contiguous cache region.

In vLLM's V1 engine, the KV-cache manager maintains a pool of available blocks. Each request maps to a list of allocated blocks, and attention kernels use block metadata to find the correct key/value tensors during the forward pass.

## Why blocks matter

Autoregressive generation creates uneven sequence lengths:

- one request may have a short prompt and long output
- another may have a long prompt and short output
- requests finish at different times

Fixed-size cache blocks let the engine allocate just enough KV space for each request step, return blocks when a request finishes, and reuse blocks for future requests.

This makes [[wiki/concepts/Continuous Batching]] practical because the model can flatten many active sequences into one execution shape while still keeping per-request attention state separate.

## Prefix caching connection

Paged attention also supports prefix caching. The source describes complete token blocks being hashed, associated with allocated KV blocks, and looked up later when another request shares the same prefix.

Incomplete blocks are less reusable because prefix caching operates at block boundaries. A repeated prefix that does not align to complete blocks can still require recomputation for the trailing partial block.

## System implication

Paged attention turns "context length" into an allocation and indexing problem inside the serving system. ^[inferred]

That matters for [[wiki/topics/LLM Inference Systems]] because throughput is constrained not just by FLOPs, but by how efficiently the engine can allocate GPU memory, preserve cache hits, and free stale request state.

## Related

- [[wiki/concepts/KV Cache]]
- [[wiki/concepts/Prompt Caching]]
- [[wiki/concepts/Continuous Batching]]
- [[wiki/sources/vLLM Inference Systems Source Guide]]
