---
title: Linear Layer
type: concept
status: seed
category: concepts
tags:
  - llm
  - inference
  - transformer
aliases:
  - 线性层
  - 全连接层
  - fully connected layer
  - dense layer
  - affine layer
  - nn.Linear
sources:
  - conversation:2026-08-24
created: 2026-08-24T14:05:47+0800
updated: 2026-08-24T14:05:47+0800
summary: 线性层是神经网络最基础的一步计算 y=Wx+b：把输入向量重新加权组合、改变维度，参数 W、b 可学习；LM head 就是把隐藏状态投影成 logits 的线性层。
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-08-24
tier: supporting
relationships:
  - target: "[[wiki/concepts/Logits]]"
    type: related_to
  - target: "[[wiki/concepts/Next-Token Pipeline]]"
    type: related_to
  - target: "[[wiki/concepts/Transformer Residual Stream]]"
    type: related_to
---

# Linear Layer

线性层是神经网络最基础的一步计算：把一个输入向量乘以一个权重矩阵，再加上一个偏置向量。

## What It Is

数学形式只有一行：

$$
y = Wx + b
$$

- $x$：输入向量
- $W$：权重矩阵，训练学到的参数
- $b$：偏置向量，训练学到的参数
- $y$：输出向量

它有很多别名，指的都是同一个东西：线性层 = 全连接层 = fully connected layer = dense layer = `nn.Linear`（PyTorch）。严格说，纯 $Wx$ 才是线性变换，加上偏置 $b$ 后是**仿射变换**（affine transformation），但工程语境里统称线性层。

## How It Works

本质是**换坐标 + 缩放 + 混合**。每个输出分量都是所有输入分量的加权求和。以输入 3 维、输出 2 维为例：

$$
y_1 = w_{11}x_1 + w_{12}x_2 + w_{13}x_3 + b_1
$$

所以线性层做三件事：

- **改变维度**：输入维度和输出维度可以不同，可升维也可降维。
- **重新组合信息**：每个输出都是输入各分量的线性混合。
- **参数可学习**：$W$ 与 $b$ 在训练中被梯度调整。

### 为什么叫“线性”

因为纯 $Wx$ 满足可加性与齐次性：

$$
W(x_1 + x_2) = Wx_1 + Wx_2
$$

关键推论：多个纯线性变换叠加，本质仍等价于**一个**线性变换。因此若只堆线性层，再深也学不到复杂模式；神经网络必须在线性层之间插入**非线性激活函数**（ReLU、GELU 等），线性层才能组合出非线性表达能力。^[inferred]

## In the LLM Next-Token Path

[[wiki/concepts/Next-Token Pipeline|LM head]] 就是一个线性层，负责把上下文含义向量投影成词表分数：

~~~text
隐藏状态 h（如 768 维）
      ↓  线性层：z = W·h + b
logits z（如 50000 维 = 词表大小）
~~~

此时权重矩阵 $W$ 形状为 `[V, hidden]`（$V$ 为词表大小）。$W$ 的每一行对应一个 token，相当于该 token 的“特征模板”；隐藏状态与某行的点积越大，对应 token 的 [[wiki/concepts/Logits|logit]] 就越高。因此“把隐藏状态映射成 logits”本质就是一次线性层计算加一次点积匹配。

## When to Use

- 需要**改变表示维度**（投影、升降维、把某层输出接到不同宽度的下一层）时，用线性层。
- 需要让某个向量在所有分量间做**可学习的加权组合**时，用线性层。
- 读模型结构时，看到 `nn.Linear`、`Dense`、`fc`、`proj`、`lm_head` 等命名，基本都是同一个 $y=Wx+b$。
- 但线性层单独不能表达非线性关系：若任务需要非线性，必须在层间加激活函数，否则整个堆叠退化为一层。

## Related

- [[wiki/concepts/Logits]]
- [[wiki/concepts/Next-Token Pipeline]]
- [[wiki/concepts/Transformer Residual Stream]]
- [[wiki/concepts/LLM]]
