---
title: KV Cache
type: concept
status: seed
summary: KV cache stores transformer key/value tensors so repeated prefixes or generated histories do not need full attention recomputation.
category: concepts
sources:
  - https://x.com/_avichawla/article/2044670188998803855
  - https://www.aleksagordic.com/blog/vllm
  - inline:life-of-a-token-2026-05-09
created: 2026-05-05T00:00:00+08:00
updated: 2026-05-09T00:00:00+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.9
  inferred: 0.1
  ambiguous: 0.0
aliases:
  - key value cache
  - transformer KV cache
tags:
  - llm
  - inference
  - caching
---
# KV Cache

KV cache is the stored key/value state a transformer can reuse after it has already processed a token sequence.

## Core mechanism

Transformer inference has two broad phases:

- prefill: process the full input prompt and build internal attention state
- decode: generate new tokens one at a time while reading prior state

During attention, each token produces query, key, and value vectors. The key and value vectors for a token are determined by the preceding token sequence; once computed for a fixed prefix, they do not need to be recomputed for the same prefix.

The Life of a Token source frames this as memoization inside [[wiki/concepts/Autoregressive Decoding]]: each generated token appends new K/V rows, while prior rows remain valid because causal masking prevents future tokens from changing past attention state.

The [[wiki/concepts/Prompt Caching]] source describes provider-side prompt caching as persisting those key/value tensors and indexing them by a hash of the token sequence.

## Why it matters

Prefill over a long prefix is compute-heavy. If an agent resends the same long static prompt every turn, recomputing the same key/value tensors wastes compute and money.

KV reuse lets the service skip prefill for cache-hit tokens and continue from the stored state. That is why prompt layout becomes a system-design concern in long-running [[wiki/concepts/Agent]] workflows.

## Prefix identity

The cache only helps when the token sequence matches. A different order, an injected timestamp, a shuffled tool schema, or a changed tool definition creates a different hash and forces recomputation.

This is the lower-level reason prompt caching is brittle: the cache does not understand semantic equivalence; it sees exact token identity. ^[inferred]

## Relationship to context design

KV cache is not itself memory, retrieval, or summarization. It is an inference-server representation of an already-seen token prefix.

That distinction matters for [[wiki/topics/Context Management]]:

- memory decides what information should be brought back
- summarization decides how history should be compressed
- prompt caching decides whether unchanged prefix computation can be reused

These mechanisms can support each other, but they solve different problems.

## Paged serving

The vLLM source adds the serving-system view of KV cache: the cache is not only a provider-side prompt prefix optimization, but also a live GPU memory object that must be allocated, indexed, reused, and freed during request scheduling.

In [[wiki/concepts/Paged Attention]], the inference engine stores KV state in fixed-size blocks. Each request owns a list of blocks, and the scheduler allocates more blocks as prefill or decode work adds tokens.

This makes KV cache part of the scheduler's resource accounting: a request can run only if enough cache slots are available for its next tokens.

Prefix caching then adds a second reuse path: complete token blocks can be hashed and reused across requests that share the same prefix.

## Open Questions

- What cache eviction, tenant isolation, and TTL policies are used by each model provider? ^[ambiguous]
- How should agent frameworks expose cache diagnostics without making application code depend too tightly on one provider's API shape? ^[inferred]

## Sources

- [[wiki/sources/Prompt Caching Claude Code Case Study Source Guide]]
- [[wiki/sources/vLLM Inference Systems Source Guide]]
- [[wiki/sources/Life of a Token Source Guide]]

## Related

- [[wiki/concepts/Prompt Caching]]
- [[wiki/concepts/Paged Attention]]
- [[wiki/concepts/Prefill Decode Split]]
- [[wiki/concepts/Autoregressive Decoding]]
- [[wiki/topics/LLM Inference Systems]]
- [[wiki/concepts/LLM]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Harness]]
