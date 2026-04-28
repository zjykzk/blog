---
title: Epiplexity
type: concept
status: seed
source_count: 1
updated: 2026-04-24
aliases:
  - 认知复杂度
  - 可学习结构密度
tags:
  - ai
  - ml
  - concept
  - information-theory
---

# Epiplexity

Epiplexity 不是在问一份数据“总共有多少信息”，而是在问：对一个算力有限的观察者来说，这份数据里到底有多少结构是可提取、可学习、可压缩的。

## What it is

传统信息论里的很多指标，默认观察者的计算能力足够强。

在这个前提下：

- 棋谱、图像、文本、随机串，都可以被讨论为某种固定的信息量
- 学习者能否看出结构，并不会直接进入定义本身

Epiplexity 改变了这个视角。

它把“观察者是算力受限的”直接放进问题定义里，于是信息不再只是对象本身的属性，也跟观察者能做多少计算有关。

用更直白的话说：

- 时间受限熵描述“你现在看起来仍然像随机的那部分”
- epiplexity 描述“你现在其实已经能从里面学出来的那部分结构”

所以，epiplexity 可以理解为一种面向有限算力学习者的“可学习结构密度”。

## Why it matters

它改变了评估数据价值的方式。

不是先问：

- 这里有多少数据？
- 这里总信息量有多大？

而是先问：

- 当前模型能从这里学到多少结构？
- 这些结构对泛化是否有帮助？
- 有多少训练预算被噪音消耗掉了？

这个视角能帮助解释几个反直觉现象：

- 规则 + 自我对弈，可能比海量人类棋谱更有用
- 精选数据，可能比大规模重复数据更有价值
- 合成数据，在某些阶段可能是在提纯结构，而不是伪造信息
- 文本预训练，也许比某些图像任务更容易迁移，因为结构密度更高

## Upstream concepts

- 信息
- 熵
- 柯氏复杂度
- 计算受限观察者

## Downstream topics

- [[wiki/topics/Learnable Structure in Data]]
- 数据选择
- 合成数据
- 自我对弈
- 预训练质量
- 泛化能力

## Cross-links

- [[wiki/maps/AI Map]]
- [[wiki/maps/Reading Map]]

## Source notes

- [[wiki/sources/Epiplexity Paper Notes]]
