---
title: Transformer Feed-Forward Network
type: concept
status: seed
category: concepts
tags:
  - llm
  - inference
  - mechanism
aliases:
  - Transformer FFN
  - position-wise feed-forward network
  - Transformer MLP
sources:
  - https://kcnrpnk9jqxn.feishu.cn/wiki/LDSUwt1Gfi5uOmkhRXScfIExnBb
created: 2026-08-30T21:03:10+0800
updated: 2026-08-30T21:03:10+0800
summary: A Transformer FFN applies a learned nonlinear feature transformation independently at each token position, then writes the resulting update back to the residual stream.
provenance:
  extracted: 0.74
  inferred: 0.26
  ambiguous: 0.0
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-08-30
tier: supporting
relationships:
  - target: "[[wiki/concepts/Linear Layer]]"
    type: uses
  - target: "[[wiki/concepts/Transformer Residual Stream]]"
    type: related_to
  - target: "[[wiki/concepts/Next-Token Pipeline]]"
    type: related_to
---

# Transformer Feed-Forward Network

A Transformer feed-forward network (FFN) is the position-wise nonlinear sublayer that follows attention in a conventional Transformer block. Attention moves information among token positions; the FFN transforms the features already present at each position without directly reading other positions.

## Core Computation

Using row-vector notation, a two-layer GPT-2-style FFN computes

$$
\operatorname{FFN}(x)=\operatorname{GELU}(xW_1+b_1)W_2+b_2.
$$

For GPT-2 Small, the dimensions are

$$
768 \longrightarrow 3072 \longrightarrow 768,
$$

where $W_1 \in \mathbb{R}^{768\times3072}$ expands the residual representation, GELU introduces nonlinearity, and $W_2 \in \mathbb{R}^{3072\times768}$ projects the result back to the model width. The same parameters are applied independently to every sequence position. The output therefore has the same width as the input and can be added to the [[wiki/concepts/Transformer Residual Stream|residual stream]].

The width 3072 is a GPT-2 configuration choice, not part of the definition of an FFN. Other models choose different expansion ratios and intermediate widths.

## The Key-Value-Memory Interpretation

One useful interpretive view treats the columns of $W_1$ as learned feature or pattern detectors and the corresponding rows of $W_2$ as directions written back when those features activate. Under this view, the hidden state produces many match-like scores, the activation function modulates them, and $W_2$ combines their associated value-like vectors. This resembles a distributed key-value memory.

The analogy is not a literal implementation contract. An FFN does not perform an exact key lookup, its features can be superposed and polysemantic, and a fact need not reside in one detector-value pair. Describing an FFN as memory is an interpretive model of its learned computation, not proof that its parameters form a discrete database. ^[inferred]

GELU is also not a hard SQL-style `WHERE score > 0` gate. It is the smooth function $x\Phi(x)$: large negative inputs approach zero, but negative values are not categorically rejected and positive values are scaled continuously. The detector-and-filter language is therefore an approximation to a graded nonlinear transformation.

## Architectural Boundaries

The simple GELU equation describes GPT-2, not every modern Transformer. ^[inferred]

- Gated MLPs such as SwiGLU and GEGLU compute two input projections and multiply a transformed gate branch by a value branch before the output projection. They preserve the position-wise role but do not have the exact form $\operatorname{GELU}(xW_1+b_1)W_2+b_2$. ^[inferred]
- Mixture-of-experts (MoE) layers route each token to a subset of expert FFNs. The experts still perform position-wise feature transformations, while the router, expert capacity, and load balancing add behavior absent from a dense FFN. ^[inferred]
- Normalization placement, residual layout, activation choice, bias use, and expansion ratio vary by architecture. These choices must be checked against the specific checkpoint rather than inferred from GPT-2. ^[inferred]

## Why It Matters

The FFN gives each Transformer block nonlinear feature computation in addition to attention's cross-position routing. Because its output is an additive update, later blocks can combine FFN-derived features with attention-derived context throughout the [[wiki/concepts/Next-Token Pipeline]].

## Related

- [[wiki/concepts/Linear Layer]]
- [[wiki/concepts/Transformer Residual Stream]]
- [[wiki/concepts/Next-Token Pipeline]]
- [[wiki/concepts/Neural Network Inference Boundary]]
- [[wiki/sources/Life of a Token Source Guide]]

## Sources

- [Life of a Token](https://kcnrpnk9jqxn.feishu.cn/wiki/LDSUwt1Gfi5uOmkhRXScfIExnBb)
