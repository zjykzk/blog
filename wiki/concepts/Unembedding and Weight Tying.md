---
title: Unembedding and Weight Tying
type: concept
status: seed
category: concepts
tags:
  - llm
  - inference
  - probability
aliases:
  - unembedding
  - output embedding
  - LM head weight tying
sources:
  - https://kcnrpnk9jqxn.feishu.cn/wiki/LDSUwt1Gfi5uOmkhRXScfIExnBb
created: 2026-08-30T21:03:10+0800
updated: 2026-08-30T21:03:10+0800
summary: Unembedding linearly projects a hidden state into one logit per vocabulary item; weight tying reuses input-embedding parameters for this output projection in some architectures.
provenance:
  extracted: 0.92
  inferred: 0.08
  ambiguous: 0.0
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-08-30
tier: supporting
relationships:
  - target: "[[wiki/concepts/Linear Layer]]"
    type: uses
  - target: "[[wiki/concepts/Logits]]"
    type: related_to
  - target: "[[wiki/concepts/Next-Token Pipeline]]"
    type: related_to
---

# Unembedding and Weight Tying

Unembedding is the output projection that maps a model-width hidden state to one raw score for every item in the vocabulary. It reverses the *dimensional direction* of embedding, but it does not directly recover text or a token ID.

## Hidden State to Vocabulary Logits

With column-vector notation, let the final hidden state be $h \in \mathbb{R}^{d_{model}}$, the vocabulary size be $V$, and the unembedding matrix be $U \in \mathbb{R}^{V\times d_{model}}$. The LM head computes

$$
z = Uh+b, \qquad z \in \mathbb{R}^{V}.
$$

Each component $z_i$ is the [[wiki/concepts/Logits|logit]] for vocabulary item $i$. In row-vector notation the same operation is $z=hU^\top+b$; apparent transposes in descriptions and code often reflect only this notation choice.

The stages must remain distinct:

~~~text
hidden state [d_model]
        ↓ unembedding / LM head
vocabulary logits [V]          raw real-valued scores
        ↓ logit processing + softmax
probabilities [V]              normalized distribution
        ↓ greedy choice or sampling
token ID                       one vocabulary index
        ↓ tokenizer decode
text token                     the corresponding byte/string piece
~~~

A logit is neither a token ID nor a probability. Softmax turns the score vector into probabilities; a decoding rule then selects one index. Only that selected vocabulary index is a token ID. This boundary connects the learned model computation to [[wiki/concepts/Autoregressive Decoding|autoregressive decoding]].

## Weight Tying

Let the input embedding table be $E \in \mathbb{R}^{V\times d_{model}}$. A tied model reuses this parameter matrix for the output projection, so $U=E$ in column-vector notation and $z=hE^\top$ in row-vector notation. The same learned token vectors therefore serve two roles:

- embedding looks up row $E_i$ to map token ID $i$ into model space;
- unembedding compares the hidden state with every row $E_i$ to produce vocabulary logits.

GPT-2 ties its input embedding and LM-head weights. That is an architecture-specific parameter-sharing choice, not the definition of unembedding and not a universal property of language models. Other architectures can use an independent output matrix, partial or factorized tying, adapters, or different bias conventions. Code and checkpoint metadata are the authority for a particular model. ^[inferred]

Weight tying also does not make embedding and unembedding semantic inverses. Embedding selects one learned row, while unembedding produces simultaneous scores against all rows; neither operation reconstructs the other's input exactly. ^[inferred]

## Decoding Boundary

Unembedding fixes the raw vocabulary scores for a given hidden state and model execution. It does not determine which token will be emitted. Temperature, masks, repetition penalties, logit bias, top-k, top-p, and the sampling random seed can all affect the later choice.

Top-k sampling in particular does **not** guarantee selection of the top-1 token. It retains the $k$ highest-scoring candidates, renormalizes their probabilities, and samples among them. The top-1 token is guaranteed only under a deterministic rule such as greedy decoding, or when the post-processing distribution assigns all selectable mass to that token.

## Related

- [[wiki/concepts/Linear Layer]]
- [[wiki/concepts/Logits]]
- [[wiki/concepts/Next-Token Pipeline]]
- [[wiki/concepts/Autoregressive Decoding]]
- [[wiki/sources/Life of a Token Source Guide]]

## Sources

- [Life of a Token](https://kcnrpnk9jqxn.feishu.cn/wiki/LDSUwt1Gfi5uOmkhRXScfIExnBb)
