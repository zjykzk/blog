---
title: Tokenization
type: concept
status: seed
summary: Tokenization converts text into model vocabulary IDs, giving the neural network discrete symbols it can embed and process numerically.
category: concepts
sources:
  - inline:life-of-a-token-2026-05-09
created: 2026-05-09T00:00:00+08:00
updated: 2026-05-09T00:00:00+08:00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-09
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.0
aliases:
  - LLM tokenization
  - BPE tokenization
tags:
  - llm
  - inference
  - representation
---
# Tokenization

Tokenization is the step that converts raw text into a sequence of discrete token IDs from a model vocabulary.

## Key Ideas

- GPU kernels operate on numbers, so text must be converted into integers before it can enter an LLM.
- GPT-2 uses Byte Pair Encoding, which balances character-level and word-level representations by using learned subword units.
- A token may include leading whitespace, as in `" capital"`, because the tokenizer's vocabulary encodes frequent byte sequences rather than human word boundaries.
- Token IDs are arbitrary vocabulary indices; arithmetic on the IDs themselves does not carry semantic meaning.
- Embedding lookup is the transition from discrete symbol IDs into continuous vector space.

## Why it matters

Tokenization is part of the model contract: context length, cache identity, cost accounting, and prompt layout all depend on token sequences rather than human-visible characters. ^[inferred]

Exact token identity also matters for [[wiki/concepts/KV Cache]] and [[wiki/concepts/Prompt Caching]], because semantically similar text with different tokenization or ordering will not hit the same cached prefix.

## Related

- [[wiki/concepts/Next-Token Pipeline]]
- [[wiki/concepts/Prompt Caching]]
- [[wiki/concepts/KV Cache]]
- [[wiki/sources/Life of a Token Source Guide]]
