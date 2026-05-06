---
title: LLM
type: concept
status: seed
category: concepts
summary: 当前旧笔记里与 LLM 相关的两类判断混在了一起：
sources:
  - https://www.aleksagordic.com/blog/vllm
created: 2026-05-01
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.0
source_count: 3
updated: 2026-05-06T12:17:59+08:00
aliases:
  - llm
tags:
  - ai
  - llm
  - concept
---

# LLM

当前旧笔记里与 LLM 相关的两类判断混在了一起：

- `think tool` 是提醒模型停下来想一下的工具，没有输入
- 它不同于 extended thinking 这类模型内建能力
- router / adapter 体现的是 agent 系统如何把模型能力包装成更可控的执行单元

因此在 LLM 视角下，更重要的是区分两层：

- 模型内建能力，例如 extended thinking
- 外部流程控制与工具设计，例如 think tool、router、adapter

这个区分很重要，因为它把“外部流程控制”与“模型内部推理能力”分开来看。

## Boundary

`[[wiki/sources/Theory Is All You Need Source Guide]]` 提供了另一个边界：LLM 的生成性主要来自对既有语言结构的重组、翻译和预测。

所以评估 LLM 时，不只看它能否生成新文本，还要问它是否能提出可行动的因果假设，并知道该通过什么实验生成新数据。

## Runtime boundary

The vLLM source adds a serving-side boundary: an LLM is not the same thing as an [[wiki/topics/LLM Inference Systems|inference system]].

The model defines the transformer computation and sampling distribution, while the inference system decides scheduling, [[wiki/concepts/KV Cache]] allocation, batching, prefill/decode handling, speculative decoding, serving endpoints, and benchmark tradeoffs.

That distinction matters because user-visible latency, throughput, and cost can change substantially while the underlying model weights stay the same. ^[inferred]

## Cross-links

- [[wiki/concepts/Agent]]
- [[wiki/topics/LLM Inference Systems]]
- [[wiki/maps/AI Map]]

## Source notes

- `pages/llm.md`
- [[wiki/sources/Theory Is All You Need Source Guide]]
- [[wiki/sources/vLLM Inference Systems Source Guide]]
