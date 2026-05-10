---
title: >-
  LLM Training Stages
category: synthesis
type: synthesis
status: seed
tags:
  - llm
  - training
  - alignment
sources:
  - conversation:2026-05-09
created: 2026-05-09T21:39:04+08:00
updated: 2026-05-09T21:39:04+08:00
summary: >-
  LLM training stages differ by data shape, loss signal, and behavioral target: pretraining builds capability, SFT shapes instruction following, and RL optimizes preferences.
provenance:
  extracted: 0.86
  inferred: 0.14
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-09
aliases:
  - Pretraining SFT RL
  - LLM 预训练 SFT RL
  - LLM Post-training
---
# LLM Training Stages

## Context

Large language model training is easier to understand when pretraining, supervised fine-tuning, and reinforcement-learning-style alignment are separated by their training process rather than only by their names.

The key question is not just what each phase produces, but what a batch looks like, what loss is computed, and whether the model is imitating existing text or optimizing feedback from its own generated behavior.

## Finding / Decision

Pretraining, SFT, and RL differ along three axes:

- Pretraining learns the statistical structure of language and world knowledge from large text streams through next-token prediction.
- SFT continues next-token prediction on instruction-answer examples, usually masking the user side and supervising only assistant tokens.
- RL or preference optimization starts from an already instruction-tuned model and pushes generated answers toward higher reward or preferred responses instead of treating one demonstration as the only target.

A compact engineering reading is:

- Pretraining builds the capability distribution.
- SFT installs the interaction protocol.
- RL reshapes the selection preference among possible answers.

## Reasoning

### Pretraining optimizes text likelihood

Pretraining data is ordinary text: books, code, web pages, papers, conversations, and other large corpora. After [[wiki/concepts/Tokenization]], a sequence such as `x1, x2, ..., xn` becomes a dense source of supervision: each position asks the model to predict the next token.

The training loop is teacher-forced next-token prediction:

```text
for batch in pretraining_data:
    tokens = batch.text_tokens
    logits = model(tokens[:-1])
    loss = cross_entropy(logits, tokens[1:])
    update(model, loss)
```

The target is `P(x_t | x_<t)`. This makes pretraining data-efficient at scale because almost every token position produces a learning signal. It also explains why a base model is fundamentally a continuation model: it learns how text tends to continue, not necessarily how an assistant should obey a user.

### SFT optimizes demonstration-answer likelihood

SFT data is no longer arbitrary text. It is structured as instruction-following examples, usually `user prompt -> assistant answer`, sometimes across multiple dialogue turns.

The conversation is serialized through a chat template, but the loss is typically masked so the model is not trained to generate the user's prompt. Only the assistant side contributes to the cross-entropy loss:

```text
tokens = [user_prompt_tokens][assistant_answer_tokens]
labels = [-100 ... -100][assistant_answer_tokens]
loss = cross_entropy(model(tokens), labels, ignore_index=-100)
```

This is still language-model training, but on a different distribution. The model is no longer matching internet text in general; it is matching idealized assistant behavior under an instruction. This turns the base model from a document simulator into an instruction-following interface. It does not by itself solve the problem of choosing among many acceptable answers.

### RL optimizes generated behavior under reward or preference

RLHF-style training changes the training object. The model receives a prompt, generates its own answer, and the update is driven by reward or preference rather than a single demonstration trajectory.

A classical RLHF pipeline has three roles:

- A policy model, often initialized from SFT.
- A frozen reference model, often the original SFT model.
- A reward model trained from human or AI preference rankings.

Preference data usually has the form:

```text
prompt, chosen_answer, rejected_answer
```

The reward model is trained so `R(prompt, chosen)` exceeds `R(prompt, rejected)`, commonly with a loss shaped like:

```text
-log sigmoid(R(chosen) - R(rejected))
```

Then the policy is optimized to generate answers with higher reward while staying close to the reference model:

```text
maximize reward(prompt, answer) - beta * KL(policy || reference)
```

The KL term matters because reward-only optimization can make the model exploit the reward model: becoming verbose, evasive, over-safe, repetitive, or stylistically distorted. The reference model acts as a behavioral anchor.

Modern preference methods such as DPO often replace the explicit PPO loop with a direct loss over `prompt, chosen, rejected` pairs. DPO is not traditional online RL, but it serves the same post-training purpose: make the current model prefer the chosen answer over the rejected answer relative to a reference model.

### Teacher forcing is the hinge

Pretraining and SFT usually use teacher forcing. The model is evaluated on the true next token at each position, even if it would have predicted something else. This makes training stable and dense, but it optimizes likelihood along fixed text trajectories.

RL-like post-training evaluates the model closer to deployment behavior: the model generates a full answer and then receives feedback on the result. This makes it better suited to shaping global answer quality, but also more expensive and more vulnerable to reward-design failures.

## Implications

The three stages should not be treated as interchangeable ways to "put knowledge into a model." They solve different control problems:

- Pretraining asks: what reusable structure can be compressed from large text?
- SFT asks: how should the model map user instructions into assistant responses?
- RL asks: when many responses are possible, which kind should the model prefer?

This distinction prevents several common confusions:

- SFT is not a miniature replacement for pretraining; it is behavior shaping on top of a learned capability base.
- RL is not a way to create knowledge from nothing; it redirects an already capable model toward preferred behavior.
- A post-trained assistant still runs through the same [[wiki/concepts/Next-Token Pipeline]] at inference time; training changes the weights and behavior distribution, not the fact that generation is autoregressive.
- Data quality means different things at each stage: broad learnable structure for pretraining, clear demonstrations for SFT, and reliable comparative judgment for RL or preference optimization.

## Related

- [[wiki/concepts/LLM]]
- [[wiki/concepts/Tokenization]]
- [[wiki/concepts/Next-Token Pipeline]]
- [[wiki/topics/Learnable Structure in Data]]
- [[wiki/sources/How LLMs Actually Work Source Guide]]
- [[wiki/maps/AI Map]]
