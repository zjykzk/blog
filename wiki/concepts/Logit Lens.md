---
title: Logit Lens
type: concept
status: seed
category: concepts
tags:
  - llm
  - inference
  - mechanism
aliases:
  - logit-lens probing
  - intermediate decoding
sources:
  - https://kcnrpnk9jqxn.feishu.cn/wiki/LDSUwt1Gfi5uOmkhRXScfIExnBb
created: 2026-08-30T21:03:10+0800
updated: 2026-08-30T21:03:10+0800
summary: Logit Lens applies a model's final normalization and vocabulary projection to intermediate residual states to inspect which tokens are linearly decodable at each layer.
provenance:
  extracted: 0.94
  inferred: 0.06
  ambiguous: 0.0
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-08-30
tier: supporting
relationships:
  - target: "[[wiki/concepts/Logits]]"
    type: uses
  - target: "[[wiki/concepts/Unembedding and Weight Tying]]"
    type: uses
  - target: "[[wiki/concepts/Transformer Residual Stream]]"
    type: related_to
---

# Logit Lens

Logit Lens is a diagnostic probe that decodes an intermediate Transformer residual state with the model's final normalization and LM head. It asks: if this state were projected into the vocabulary now, which token directions would be most visible?

For an intermediate state $h_l$, the basic probe is

$$
z_l = U\,\operatorname{LN}_{f}(h_l)+b,
$$

where $\operatorname{LN}_{f}$ is the model's final normalization and $U$ is its [[wiki/concepts/Unembedding and Weight Tying|unembedding]] matrix. Ranking or applying softmax to $z_l$ exposes vocabulary-level signals carried by the [[wiki/concepts/Transformer Residual Stream|residual stream]] at layer $l$.

## GPT-2 `" Paris"` Trace

The source runs GPT-2 Small with the prompt `The capital of China is Beijing. The capital of France is`. It probes the final position and tracks token ID 6342, decoded as `" Paris"`. The reported values are rounded outputs from that run:

| Probe point | `" Paris"` rank | `" Paris"` probability | Top-1 token | Top-1 probability |
|---|---:|---:|---|---:|
| Embedding | 28,383 | 0.00% | `" destro"` | 78.71% |
| Layer 0 | 20,486 | 0.00% | `" not"` | 30.87% |
| Layer 1 | 19,374 | 0.00% | `" not"` | 26.13% |
| Layer 2 | 13,804 | 0.00% | `" now"` | 33.40% |
| Layer 3 | 8,353 | 0.00% | `" also"` | 39.08% |
| Layer 4 | 3,494 | 0.00% | `" not"` | 32.38% |
| Layer 5 | 1,086 | 0.00% | `" not"` | 42.29% |
| Layer 6 | 148 | 0.01% | `" also"` | 64.14% |
| Layer 7 | 24 | 0.55% | `" also"` | 26.80% |
| Layer 8 | 1 | 88.35% | `" Paris"` | 88.35% |
| Layer 9 | 1 | 91.01% | `" Paris"` | 91.01% |
| Layer 10 | 1 | 97.68% | `" Paris"` | 97.68% |
| Layer 11 | 1 | 74.67% | `" Paris"` | 74.67% |

The trace shows a sharp transition at Layer 8, but it is not monotonic: the probed probability rises to 97.68% at Layer 10 and then falls to 74.67% at Layer 11. A later layer can recalibrate competing logits while preserving the same top-ranked token. Layer depth therefore should not be read as a guaranteed steady increase in one candidate's probability.

## What the Probe Does and Does Not Show

Logit Lens shows what is directly decodable through one fixed vocabulary projection. It can reveal when a candidate becomes prominent, compare ranks across layers, and identify abrupt changes worth investigating.

It is diagnostic, not causal. An intermediate state is not normally sent to the final decoder at that point, and the probe does not establish which attention head, FFN feature, or earlier activation caused a candidate to rise. A high intermediate probability is not a decision event, proof that the model has completed a reasoning step, or evidence that later computation is redundant. Causal claims require interventions such as ablation or activation patching rather than decoding alone. ^[inferred]

The numerical trace is also checkpoint-, prompt-, tokenizer-, software-version-, precision-, and implementation-dependent. The table characterizes the reported GPT-2 run; it is not a universal layer schedule for GPT-2, for the question about France, or for Transformer models generally. Even apparently small changes to the few-shot prefix or checkpoint can change ranks and probabilities.

Because intermediate representations may not be aligned with the final decoder, raw Logit Lens can also produce misleading early-layer tokens. Learned translator variants such as a tuned lens address this alignment problem, but their outputs remain probes rather than the model's causal execution trace. ^[inferred]

## Related

- [[wiki/concepts/Logits]]
- [[wiki/concepts/Unembedding and Weight Tying]]
- [[wiki/concepts/Transformer Residual Stream]]
- [[wiki/concepts/Next-Token Pipeline]]
- [[wiki/sources/Life of a Token Source Guide]]

## Sources

- [Life of a Token](https://kcnrpnk9jqxn.feishu.cn/wiki/LDSUwt1Gfi5uOmkhRXScfIExnBb)
