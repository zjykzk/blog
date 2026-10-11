---
title: Self-Attention
type: concept
status: seed
category: concepts
tags:
  - llm
  - mechanism
  - context
  - inference
aliases:
  - scaled dot-product self-attention
  - multi-head self-attention
sources:
  - https://kcnrpnk9jqxn.feishu.cn/wiki/LDSUwt1Gfi5uOmkhRXScfIExnBb
created: 2026-08-30T21:03:10+0800
updated: 2026-08-30T21:03:10+0800
summary: Self-attention compares learned queries and keys to compute input-dependent mixtures of values, routing information across permitted sequence positions.
provenance:
  extracted: 0.79
  inferred: 0.21
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
  - target: "[[wiki/concepts/KV Cache]]"
    type: related_to
  - target: "[[wiki/concepts/Autoregressive Decoding]]"
    type: related_to
---

# Self-Attention

Self-attention is a learned information-routing operation within a sequence. Each position derives a query that expresses what to match, a key that participates in matching, and a value that carries the information to mix. All three come from the same current sequence representation, which is why the operation is *self*-attention.

## Scaled Dot-Product Attention

For one head with input $X \in \mathbb{R}^{B \times T \times d_{model}}$ and learned projections $W_Q,W_K,W_V \in \mathbb{R}^{d_{model} \times d_h}$:

$$
Q=XW_Q, \qquad K=XW_K, \qquad V=XW_V,
$$

where $Q,K,V \in \mathbb{R}^{B \times T \times d_h}$. The head computes

$$
A = \operatorname{softmax}\!\left(\frac{QK^\top}{\sqrt{d_h}} + M\right),
\qquad O = AV.
$$

$A \in \mathbb{R}^{B \times T \times T}$ contains one distribution over source positions for each destination position. Division by $\sqrt{d_h}$ controls score scale before softmax. The learned projections, not the dot product alone, make matching useful.

For causal self-attention, the mask is

$$
M_{ij}=
\begin{cases}
0, & j \le i,\\
-\infty, & j > i,
\end{cases}
$$

so position $i$ can mix values only from itself and earlier positions. This is the attention-side constraint used by [[wiki/concepts/Autoregressive Decoding]].

## Multi-Head Attention

With $h$ heads, the model performs these computations in parallel, concatenates their outputs, and applies an output projection:

$$
\operatorname{MHA}(X)=\operatorname{Concat}(O^{(1)},\ldots,O^{(h)})W_O.
$$

When $h d_h=d_{model}$, the result returns to shape $[B,T,d_{model}]$ and can be added as a delta to the [[wiki/concepts/Transformer Residual Stream]]. The Q, K, V, and output maps are learned [[wiki/concepts/Linear Layer|linear projections]].

In the source's GPT-2 Small trace, $d_{model}=768$, $h=12$, and $d_h=64$. For its five-token, single-request example, combined QKV has shape `[1, 5, 2304]`, each projection reshapes to `[1, 12, 5, 64]`, attention weights have shape `[1, 12, 5, 5]`, and the projected result returns to `[1, 5, 768]`. These dimensions and the reported head weights describe that checkpoint, layer, prompt, and software setup; they are not transformer-wide constants.

## What It Changes

A token embedding is context-free. Self-attention instead produces an input-dependent mixture of value vectors, allowing a position to receive signals from other permitted positions. In the source's example, one Layer 0 head routes substantial weight from the last token toward `" capital"` and `" France"`; that trace illustrates the mechanism but does not establish a permanent semantic function for the head.

The resulting update is contextual, but self-attention does not by itself complete the prediction. Feed-forward transformations, residual additions, normalization, later layers, and the language-model head all contribute to the eventual [[wiki/concepts/Next-Token Pipeline|next-token distribution]].

## Interpretability Boundaries

- Attention weights are the mixture coefficients for values in one head at one layer. They are not a complete causal explanation of the model's output: value content, output projection, residual pathways, other heads, and downstream computation can change or cancel their effects. ^[inferred]
- A high weight means a larger coefficient in that local mixture, not automatically semantic importance, factual reliance, or causal necessity. Intervention or ablation is needed to test causal claims. ^[inferred]
- Single heads do not have guaranteed fixed roles. The source's labels such as self-focused, first-token-focused, or content-routing describe observed patterns for one input; head behavior overlaps and changes with input, layer, model, and training.
- Self-attention routes representations already inside the model. It is distinct from external retrieval and does not by itself explain where factual associations were learned or stored. ^[inferred]

## Inference Consequences

During decoding, prior keys and values remain reusable under the causal mask. [[wiki/concepts/KV Cache]] stores them so each new step computes only the new position's projections instead of rebuilding all prior K/V rows. [[wiki/concepts/Paged Attention]] concerns how an inference system stores and addresses that cache; it is not a different mathematical definition of self-attention.

## Related

- [[wiki/concepts/Next-Token Pipeline]]
- [[wiki/concepts/Transformer Residual Stream]]
- [[wiki/concepts/Linear Layer]]
- [[wiki/concepts/KV Cache]]
- [[wiki/concepts/Autoregressive Decoding]]
- [[wiki/concepts/Paged Attention]]
- [[wiki/sources/Life of a Token Source Guide]]

## Sources

- <https://kcnrpnk9jqxn.feishu.cn/wiki/LDSUwt1Gfi5uOmkhRXScfIExnBb>
