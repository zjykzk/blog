---
title: Learnable Structure in Data
type: topic
status: seed
source_count: 1
updated: 2026-04-25
aliases:
  - 数据中的可学习结构
  - Data Value as Learnable Structure
tags:
  - ai
  - data
  - training
  - topic
---

# Learnable Structure in Data

评估数据价值时，一个更稳的起点，不是先问“这里有多少信息”，而是先问：对当前模型来说，这里到底有多少结构是可学习的。

## Core idea

很多关于数据质量的直觉，默认把“数据量大”近似成“价值高”。

但从有限算力学习者的角度看，更关键的问题其实是：

- 数据里有多少结构能被当前模型提取出来
- 有多少训练预算会被不可学习噪音消耗掉
- 学到的结构是否真的能迁移到新任务上

所以，数据价值更接近“可学习结构密度”，而不只是原始信息总量。

## Why it matters

这个视角会直接改变很多数据决策。

### 数据选择

不是默认更多数据就更好，而是优先寻找结构更密、重复更少、对泛化更有帮助的数据。

这也是为什么：

- 1 万条结构化反馈，可能比 100 万条重复评论更有价值
- 精选语料，可能比粗糙堆量更有效

### 训练方式

如果一个系统能通过规则、自我对弈、或其它方式反复生成稳定结构，那么它学到的东西，可能比直接模仿历史样本更稳。

这也是为什么：

- 规则 + self-play，可能比直接吃海量棋谱更有效
- 训练目标设计，往往和数据本身一样重要

### 合成数据

如果模型已经学到了一部分结构，那么合成数据未必只是复制，也可能是在做结构提纯。

这时真正的问题不是“它是不是真实的”，而是：

- 它保留了哪些结构
- 它去掉了哪些噪音
- 它是否仍然支持泛化

## Peer topics

- [[wiki/topics/Probability]]
- [[wiki/topics/Problem Framing]]
- [[wiki/topics/Mental Models]]

## Navigation

- [[wiki/maps/AI Map]]
- [[wiki/maps/Reading Map]]
- [[wiki/index]]

## Source notes

- [[wiki/sources/Epiplexity Paper Notes]]
- [[wiki/concepts/Epiplexity]]
- [[wiki/topics/Probability]]
