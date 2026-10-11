---
title: Positional Encoding
type: concept
status: seed
category: concepts
tags:
  - llm
  - mechanism
  - context
aliases:
  - position encoding
  - positional embedding
sources:
  - https://kcnrpnk9jqxn.feishu.cn/wiki/LDSUwt1Gfi5uOmkhRXScfIExnBb
created: 2026-08-30T21:03:10+0800
updated: 2026-08-30T21:03:10+0800
summary: Positional encoding injects token order into transformer representations through learned absolute vectors or position-dependent transformations such as RoPE.
provenance:
  extracted: 0.67
  inferred: 0.33
  ambiguous: 0.0
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-08-30
tier: supporting
relationships:
  - target: "[[wiki/concepts/Tokenization]]"
    type: related_to
  - target: "[[wiki/concepts/Next-Token Pipeline]]"
    type: related_to
  - target: "[[wiki/concepts/Autoregressive Decoding]]"
    type: related_to
---

# Positional Encoding

Positional encoding gives a transformer information about where tokens occur. A token embedding alone depends on token identity: the same ID selects the same row wherever it appears. Without an additional position signal, sequences containing the same tokens in different orders would begin from the same collection of token vectors.

## Learned Absolute Positions

For a learned absolute position table

$$
P \in \mathbb{R}^{L_{max} \times d_{model}},
$$

the model initializes position $t$ by adding the corresponding token and position rows:

$$
H^{(0)}_{b,t,:} = E_{x_{b,t},:} + P_{t,:},
\qquad H^{(0)} \in \mathbb{R}^{B \times T \times d_{model}}.
$$

The equal widths make elementwise addition possible while preserving the shape expected by later transformer blocks.

In the source's GPT-2 Small trace, `wpe` has shape `[1024, 768]`: 1,024 learned positions, each with the model's 768-dimensional width. Adding these vectors to the five token embeddings preserves shape `[1, 5, 768]`. The 1,024-position table and 768-wide vectors are properties of this GPT-2 configuration, not universal positional-encoding dimensions.

Because the table has a finite number of rows, an unmodified learned-absolute-position model has no trained lookup row beyond its configured position range. Increasing usable context therefore requires more than supplying a larger position index. ^[inferred]

## Rotary Position Embedding

RoPE injects position into attention projections rather than adding a learned vector to the residual stream. In a simplified form, it rotates each query and key according to its position:

$$
q_t' = R_t q_t,
\qquad k_s' = R_s k_s,
$$

so their score contains a relative-position-dependent rotation:

$$
(q_t')^\top k_s' = q_t^\top R_t^\top R_s k_s
= q_t^\top R_{s-t} k_s.
$$

This gives attention scores a useful dependence on relative displacement while retaining absolute phase information. ^[inferred]

RoPE does not guarantee accurate extrapolation to arbitrary sequence lengths. Behavior beyond the training range depends on learned content patterns, frequency choices, numerical precision, training context, and any interpolation or scaling method; longer accepted input is not the same as preserved model quality. ^[inferred]

## Boundaries

- Positional encoding supplies order information; it does not itself enforce autoregressive causality. The causal mask in [[wiki/concepts/Self-Attention|self-attention]] blocks access to future positions.
- Position is not token identity. [[wiki/concepts/Tokenization]] and token embedding say *what* symbol is present; positional encoding helps say *where* it occurs.
- A position-enhanced input is still only the start of contextual computation. Its later meaning is produced through attention and feed-forward updates accumulated in the [[wiki/concepts/Transformer Residual Stream]].

## Why It Matters

Order changes meaning, and [[wiki/concepts/Autoregressive Decoding]] depends on a direction through the sequence. Positional encoding makes order available to the [[wiki/concepts/Next-Token Pipeline]] while leaving the model width unchanged.

## Related

- [[wiki/concepts/Tokenization]]
- [[wiki/concepts/Next-Token Pipeline]]
- [[wiki/concepts/Transformer Residual Stream]]
- [[wiki/concepts/Autoregressive Decoding]]
- [[wiki/sources/Life of a Token Source Guide]]

## Sources

- <https://kcnrpnk9jqxn.feishu.cn/wiki/LDSUwt1Gfi5uOmkhRXScfIExnBb>
