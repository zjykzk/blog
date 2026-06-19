---
title: LLM Serving Request Structure
category: synthesis
type: synthesis
status: draft
tags:
  - llm
  - inference
  - serving
  - systems
sources:
  - conversation:2026-06-19
created: 2026-06-19T08:24:07+0800
updated: 2026-06-19T08:24:07+0800
summary: LLM serving 把请求组织成可调度的 token 工作流：GPU 利用率来自 batching，请求边界靠 batch slot、attention 元数据、KV block 和 role 模板维持。
provenance:
  extracted: 0.78
  inferred: 0.22
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-06-19
tier: supporting
aliases:
  - 大语言模型 Serving 请求结构
  - LLM serving request identity
  - chat message roles in serving
---

# LLM Serving Request Structure

## Context

LLM serving 不是简单地把一个模型进程挂到 HTTP 端口上，而是把用户消息、token 序列、GPU 批处理、KV cache、采样参数和流式响应组织成一套可调度的在线系统。

这个问题的关键不只是“模型如何生成 token”，还包括三条边界：

- 硬件边界：GPU 擅长大规模同构矩阵计算，不擅长被单个小请求零碎驱动。
- 请求边界：多个请求可以并行进入同一次前向计算，但不能在语义上互相污染。
- 对话边界：`system`、`user`、`assistant`、`tool` 等 role 必须被转成模型能识别的 token 结构。

## Finding / Decision

LLM serving 的核心结构可以压缩为一句话：

> serving 系统把多个独立请求重排成 GPU 喜欢的大规模 token 批处理，同时用调度器元数据、attention 边界、KV cache block table 和 chat template 维持“哪个 token 属于哪个请求、谁在对话里说话、现在轮到谁生成”。

模型本身只看 token IDs 和张量；请求身份、对话角色、工具结果、流式响应归属等语义边界主要由 serving/API 层和调度器维护。

## Reasoning

### 单请求会浪费 GPU

GPU 是吞吐机器，不是低延迟单任务机器。它的优势来自大量并行计算单元、Tensor Core、大矩阵乘法和高显存带宽。

单个 LLM 请求，尤其在 [[wiki/concepts/Autoregressive Decoding|autoregressive decoding]] 阶段，每一步通常只输入一个新 token。单请求 decode 的形状接近：

```text
[1, 1, hidden_dim]
```

这个粒度太小，不能充分占满 GPU 的并行计算单元。与此同时，每一步仍然要付出 kernel launch、调度、读取模型权重和访问 [[wiki/concepts/KV Cache]] 的固定成本。

Batching 的价值在于把多个用户的“下一个 token”合成同一次模型前向：

```text
[N, 1, hidden_dim]
```

这样昂贵的权重读取和 kernel 调度成本被多个请求共同摊薄。[[wiki/concepts/Continuous Batching]] 进一步把固定 batch 改成动态 batch：完成的请求退出，新来的请求加入，GPU 持续处理当前最合适的一组 token 工作。

### 并行不等于混淆请求

多个请求并行时，token 不是被无结构地混成一锅粥。serving 系统会维护显式映射：

```text
batch slot -> request_id
request_id -> sequence state
sequence state -> position_id
sequence state -> KV cache blocks
packed tokens -> sequence offsets
```

在普通 padded batch 中，batch 维度天然隔离请求：

```text
A: [A1, A2, PAD]
B: [B1, B2, B3]
C: [C1, PAD, PAD]
```

模型输出的第 0 行归还给 A，第 1 行归还给 B，第 2 行归还给 C。

在 packed sequence 中，tokens 可能物理上拼成一条长向量：

```text
tokens = [A1, A2, B1, B2, B3, C1]
cu_seqlens = [0, 2, 5, 6]
```

边界由 offset / `cu_seqlens` / attention metadata 表达，而不是靠 padding 表达。

### Attention 和 KV cache 负责运行时隔离

请求并行时，attention 不能跨请求读取。普通 batch 通过 batch 维度和 attention mask 隔离不同序列；高性能 serving 中则常用 sequence offset、slot mapping、block table 等元数据告诉 attention kernel 每个 token 可见哪些历史。

[[wiki/concepts/Paged Attention]] 把 [[wiki/concepts/KV Cache]] 切成固定大小的物理块。每个请求拥有自己的 block table：

```text
req_A -> [block 0, block 1]
req_B -> [block 7, block 8]
```

物理显存可以是一整片，但逻辑上每个请求只能读自己的 KV blocks。这类似操作系统用页表把同一片物理内存隔离成多个进程地址空间。^[inferred]

因此，GPU 可以在同一次矩阵计算里处理多个请求，但请求历史、当前位置、采样参数和输出归属仍然由调度器状态维护。

### `role` 是 API 层结构，不是模型内部字段

OpenAI 风格的 `messages` 用 `role` 表示对话中的发言者或信息来源：

- `system`：高层行为约束、身份、风格和安全边界。
- `user`：用户需求。
- `assistant`：模型先前回答或即将生成的位置。
- `tool`：外部工具返回的结果。

模型并不直接读取 JSON 里的 `role` 字段。serving/API 层会先校验 messages，然后用模型对应的 chat template 把 role 渲染成模型训练时见过的特殊 token 或文本格式。

例如：

```text
<|system|>
你是一个严谨的技术助手
<|user|>
什么是 KV Cache？
<|assistant|>
```

最后的 assistant 标记是 generation prompt，它告诉模型“现在轮到 assistant 继续生成”。

因此，`role` 的真实使用链路是：

```text
messages JSON
  -> role/order/tool-call validation
  -> apply_chat_template(messages)
  -> rendered prompt string
  -> tokenizer
  -> input_ids
  -> model forward
  -> generated assistant tokens
  -> API 包装为 role=assistant 的响应
```

### role 也是安全边界

同一句文本放在不同 role 中，控制含义不同。

`user` 里的“忽略之前所有指令”是用户请求，可能是 prompt injection。`tool` 里的同一句话通常只是网页、数据库或外部工具返回的数据，不应该被当成控制指令。^[inferred]

因此，role 不只是格式化便利，而是把指令、用户需求、助手历史和外部数据分层的安全机制之一。模型最终仍然只看到 role 被模板翻译后的 token，但上层 harness 和安全策略可以先基于 role 做校验、隔离和优先级处理。

## Implications

- 观察 LLM serving 性能时，要分开看 TTFT、inter-token latency、prefill tokens/s、decode tokens/s、queue time、GPU utilization、KV cache usage 和 batch size。单一 QPS 指标不足以解释瓶颈。^[inferred]
- serving 调度器不是附属模块，而是把 [[wiki/topics/LLM Inference Systems|LLM inference system]] 从“模型调用”变成“在线系统”的核心结构。
- 请求并发优化必须同时考虑吞吐和语义隔离：batching 提升硬件利用率，attention/KV 元数据保证不同请求不互相看见。
- chat API 的 messages/role 是结构化 prompt 的接口层；换模型时必须换到该模型对应的 chat template，否则 role 语义可能被破坏。
- 多轮 agent 和 tool calling 场景下，`tool` role 的隔离尤其重要：工具输出是外部事实或材料，不应自动升级为系统指令。^[inferred]

## Related

- [[wiki/topics/LLM Inference Systems]]
- [[wiki/concepts/Continuous Batching]]
- [[wiki/concepts/KV Cache]]
- [[wiki/concepts/Paged Attention]]
- [[wiki/concepts/Prefill Decode Split]]
- [[wiki/concepts/Autoregressive Decoding]]
- [[wiki/concepts/LLM]]
- [[wiki/topics/Context Management]]
