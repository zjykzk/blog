---
title: Token Embedding
type: concept
status: seed
category: concepts
tags:
  - llm
  - mechanism
  - inference
aliases:
  - token embedding lookup
  - input embedding
sources:
  - https://kcnrpnk9jqxn.feishu.cn/wiki/LDSUwt1Gfi5uOmkhRXScfIExnBb
created: 2026-08-30T21:03:10+0800
updated: 2026-08-30T21:03:10+0800
summary: Token embedding maps each vocabulary ID to a learned vector that initializes a transformer's token representation; the lookup itself is static across contexts.
provenance:
  extracted: 0.74
  inferred: 0.26
  ambiguous: 0.0
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-08-30
tier: supporting
relationships:
  - target: "[[wiki/concepts/Tokenization]]"
    type: uses
  - target: "[[wiki/concepts/Next-Token Pipeline]]"
    type: related_to
  - target: "[[wiki/concepts/Transformer Residual Stream]]"
    type: related_to
---

# Token Embedding

Token embedding is the learned lookup that turns a discrete token ID into a continuous vector. [[wiki/concepts/Tokenization]] determines the ID; the embedding table supplies the numeric representation on which the model can perform dot products, additions, and matrix multiplications.

## Core Mechanism

For vocabulary size $V$ and model width $d_{model}$, an input embedding table is

$$
E \in \mathbb{R}^{V \times d_{model}}.
$$

Given token IDs $x \in \{0, \ldots, V-1\}^{B \times T}$, lookup selects one row per ID:

$$
X_{b,t,:} = E_{x_{b,t},:},
\qquad X \in \mathbb{R}^{B \times T \times d_{model}}.
$$

At inference time this operation is a gather, not a new learning step. The table values were learned during training; the token IDs remain arbitrary row indices whose numerical differences carry no semantic meaning.

In the source's GPT-2 Small trace, $V=50{,}257$ and $d_{model}=768$, so `wte` has shape `[50257, 768]`. The five-token example changes shape from `[1, 5]` IDs to `[1, 5, 768]` vectors. These are GPT-2 Small configuration values, not constants of token embedding or of transformers generally.

## What the Vector Represents

Training can arrange tokens so that useful similarities and relations are reflected in the table's geometry. The source probes one GPT-2 checkpoint with analogies such as $king-man+woman$ and $France+(Tokyo-Japan)$, and discusses linear representation and superposition as explanations for distributed features. Such arithmetic is a diagnostic result and such explanations are hypotheses: they do not imply that every semantic relation is linear, every checkpoint yields the same neighbors, or every concept has one stable direction. ^[inferred]

Individual coordinates are not assigned human-readable meanings. Features may be distributed across directions and may share dimensions, so reading one coordinate as a named concept is generally unjustified. ^[inferred]

## Boundaries

### Not a contextual hidden state

The lookup returns the same row whenever the same token ID appears. It does not yet know the token's position, neighboring tokens, or intended sense. Position information and transformer layers subsequently update the per-position representation; those contextual states flow through the [[wiki/concepts/Transformer Residual Stream]].

This distinction explains why the embedding for a polysemous token remains fixed while [[wiki/concepts/Self-Attention|self-attention]] can produce different contextual updates for different sentences.

### Not a retrieval embedding

A token embedding is an internal vocabulary-row parameter. A retrieval embedding normally represents a query, passage, image, or other item for similarity search in an external index. Both are vectors, but their units, objectives, producers, and operational roles differ; one should not infer retrieval quality from the geometry of a language model's token table. ^[inferred]

## Why It Matters

Token embedding marks the transition from symbolic IDs to the fixed-width numeric stream used by the [[wiki/concepts/Next-Token Pipeline]]. Keeping it separate from later hidden states prevents two common errors: treating ID arithmetic as semantic computation and treating a context-free lookup as the model's final meaning for a token.

## Related

- [[wiki/concepts/Tokenization]]
- [[wiki/concepts/Next-Token Pipeline]]
- [[wiki/concepts/Transformer Residual Stream]]
- [[wiki/concepts/Linear Layer]]
- [[wiki/sources/Life of a Token Source Guide]]

## Sources

- <https://kcnrpnk9jqxn.feishu.cn/wiki/LDSUwt1Gfi5uOmkhRXScfIExnBb>
