---
title: Logits
type: concept
status: seed
category: concepts
tags:
  - llm
  - inference
  - probability
aliases:
  - logit
  - 原始预测分数
sources:
  - conversation:2026-08-21
created: 2026-08-21T22:52:35+0800
updated: 2026-08-21T22:52:35+0800
summary: Logits 是 LLM 在每个生成位置为整个词表产生的原始相对分数；softmax 和解码策略随后把这片可能性空间收缩成一个 token。
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-08-21
tier: supporting
relationships:
  - target: "[[wiki/concepts/Next-Token Pipeline]]"
    type: related_to
  - target: "[[wiki/concepts/Autoregressive Decoding]]"
    type: related_to
  - target: "[[wiki/concepts/LLM]]"
    type: related_to
---

# Logits

Logits 是神经网络在 softmax 之前输出的一组实数分数；对 LLM 来说，每个生成位置通常为词表中的每个候选 token 产生一个 logit。

## What It Is

若词表大小为 $V$，最后一个位置的隐藏状态为 $h_t$，语言模型头通常计算：

$$
z_t = W_{out}h_t + b, \qquad z_t \in \mathbb{R}^{V}
$$

$z_t$ 就是一组 logits，$z_{t,i}$ 对应词表中的第 $i$ 个 token。它们可以为正或为负，不要求总和为 1，也没有统一的最高分。

Logits 不是概率，也不是事实可信度。它只表示候选 token 在当前上下文中的相对竞争位置：最大 logit 指向模型最偏好的下一 token，不保证这个 token 所延续的陈述在现实中为真。

## How It Works

Softmax 把 logits 转成概率分布：

$$
p_i = \frac{\exp(z_i/T)}{\sum_j \exp(z_j/T)}
$$

其中 $T$ 是温度。两个候选的概率比由它们的 logit 差决定：

$$
\log\frac{p_i}{p_j} = \frac{z_i-z_j}{T}
$$

因此：

- 单个 logit 的绝对值不能独立解释；相对差值才决定概率比。
- 给所有 logits 加上同一个常数不会改变 softmax 概率。
- 降低温度会放大相对差值，使分布更集中；提高温度会让分布更平。
- softmax 只负责归一化分数，不能自动把结果校准为真实世界中的可靠置信度。

完整链路是：

~~~text
context tokens
      ↓
Transformer hidden state
      ↓
LM head
      ↓
raw logits over vocabulary
      ↓
logit processing + softmax
      ↓
probability distribution
      ↓
decode / sample
      ↓
next token
~~~

模型直接产生 *raw logits*。Temperature、repetition penalty、logit bias、非法 token mask、top-k、top-p 和 guided decoding 等策略在模型与最终选择之间改变或筛选这组分数；工程库有时也把处理后的分数笼统称为 logits。

## What Stays Fixed

Logits 不是一张随模型永久保存的固定分数表，而是固定模型对当前上下文的一次求值：

$$
z_t = f_{\theta}(x_1,\ldots,x_t)
$$

这里需要区分三层“固定”：

- *维度通常固定*：词表大小为 $V$ 时，每个生成位置通常输出 $V$ 个 logits。
- *映射可以固定*：模型权重 $\theta$ 冻结后，从精确输入状态到 raw logits 的数学函数固定。
- *具体数值动态变化*：prompt、生成位置或任一前文 token 改变，整组 logits 都会重新计算。

在模型权重、输入 token、attention mask、position IDs 和其他模型状态完全相同时，raw logits 在数学上是确定的。现实执行仍可能因量化方式、浮点精度、GPU kernel、并行归约或非确定性算子出现微小数值差异。

## Where Randomness Enters

正常推理通常会关闭 dropout，因此神经网络前向计算本身通常不是生成随机性的主要来源。随机性主要进入从概率分布选择 token 的 sampling 步骤：

$$
x_{t+1} \sim \operatorname{softmax}(\operatorname{Process}(z_t)/T)
$$

同一组 logits 可以在两次采样中产生不同 token。新 token 随后被加入上下文，[[wiki/concepts/Autoregressive Decoding|自回归解码]]再计算下一组 logits，于是两条生成轨迹开始分叉：

~~~text
same context → same raw logits → same probability distribution
                                      ↓ sampling
                               token A       token B
                                  ↓             ↓
                          context A       context B
                                  ↓             ↓
                          new logits A    new logits B
~~~

因此，完整生成可以同时具有“局部确定、全局随机”的性质：固定模型对固定状态的前向映射原则上确定，但随机选择经过上下文反馈后会改变后续所有状态。^[inferred]

## When to Use

Logits 是诊断 LLM 生成行为的关键边界：

- 判断模型本身偏好什么时，观察 raw logits 或 token log probabilities。
- 判断为什么两次回答不同且第一步就分叉时，比较真实 tokenized prompt、模型版本、adapter、raw logits 和执行精度。
- 第一组 logits 相同但输出不同，优先检查 sampling seed、temperature、top-k、top-p 和其他解码策略。
- 需要禁止、偏置或约束特定输出时，可以在 logits 与 sampling 之间使用 mask、logit bias 或 guided decoding，而不必重新训练模型。
- 评估事实可靠性时，不能把最高 logit 或 softmax 概率直接当作事实真值；仍需外部证据与验证机制。

## Concept Cluster

[[wiki/concepts/Next-Token Pipeline]] 给出 logits 的上下游位置：隐藏状态经 LM head 投影成 logits，softmax 与 sampling 再产生下一个 token。[[wiki/concepts/LLM]] 定义产生 raw logits 的参数化模型，[[wiki/topics/LLM Inference Systems]] 则负责执行模型、处理解码、维护缓存并服务请求。

这个分层可以压缩为：

~~~text
LLM              = 计算当前上下文的 raw logits
decoding policy  = 把 logits 变成一次 token 选择
inference system = 在硬件和并发约束下运行整个循环
~~~

## Related

- [[wiki/concepts/Linear Layer]]
- [[wiki/concepts/LLM]]
- [[wiki/concepts/Next-Token Pipeline]]
- [[wiki/concepts/Autoregressive Decoding]]
- [[wiki/concepts/Neural Network Inference Boundary]]
- [[wiki/topics/LLM Inference Systems]]
- [[wiki/topics/Probability]]

