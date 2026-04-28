---
title: Epiplexity Paper Notes
type: source
status: seed
source_count: 1
updated: 2026-04-24
aliases:
  - From Entropy to Epiplexity
  - Epiplexity Notes
tags:
  - paper
  - ai
  - information-theory
  - source
source: https://arxiv.org/html/2601.03220
---

# Epiplexity Paper Notes

这页保留论文 *From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence* 的阅读笔记，并作为 `[[wiki/concepts/Epiplexity]]` 的来源层。

## Current role

这篇 paper 对这个 wiki 的价值，不在于补充一条新的术语，而在于改写一个更底层的问题：

- 数据的价值，不只是“有多少信息”
- 更是“在有限算力下，能学到多少结构”

它适合作为理解数据选择、合成数据、自我对弈、预训练泛化差异的一张上游 source note。

## Core claims from the paper

### Problem

你训练一个 AI 下棋，给它看一百万局棋谱。另一个 AI 只看规则，自己跟自己下。按传统信息论，棋谱信息量远大于规则——但 AlphaZero 证明了后者学得更好。为什么“信息少”反而“学得多”？

### Perspective

传统信息论（香农熵、柯氏复杂度）默认观察者有无限计算力。

但真实学习者——无论是人还是 AI——都有计算预算。所以同一份数据，不应该只问“包含多少信息”，还要问“在给定算力下，观察者到底能从里面提取出多少结构”。

论文把数据拆成两部分：

- 时间受限熵：对当前观察者来说看起来像随机的部分
- Epiplexity：对当前观察者来说可提取、可学习、可压缩的结构

因此，同一个对象对不同算力的观察者，结构含量并不相同。

### Result

论文在国际象棋、元胞自动机、语言模型、图像等场景中都给出证据：epiplexity 更高的数据集，训练出来的模型泛化更强。

作者进一步推测，这也许解释了为什么文本预训练通常比图像预训练更容易迁移：文本里可被有限算力模型提取的结构密度更高。

### One-sentence takeaway

数据的价值不在于“有多少信息”，而在于“有限算力下能学到多少结构”。

## What I want to keep

### 数据选择的反直觉

我以前更自然的判断是：

- 数据越多
- 信息越多
- 模型就越容易学好

这篇 paper 逼我把问题改写成：

- 这些数据里，真正可学习的结构有多少？
- 不可学习噪音占了多少训练预算？

于是“100 万条重复评论”未必比“1 万条结构化反馈”更有价值。

前者也许信息总量更大，但后者的 epiplexity 更高。

### 生成数据的合理性

传统观念里，真实数据是信息源，合成数据只是复制。

这篇 paper 提供了另一个解释：如果模型已经学到了一部分结构，那么合成数据可能是在做“提纯”，不是在“造假”。

- 真实数据 = 结构 + 噪音
- 合成数据 = 把结构从噪音里分离并浓缩

AlphaZero 就是这个直觉最强的例子：规则 + 自我对弈，比直接模仿海量人类棋谱更能逼近稳定战术结构。

### 我想保留的一句话

生成数据不是“造假”，是“提纯”。

## Open questions

这篇 paper 让我最想继续追问的，不是 epiplexity 本身，而是结构的可组合性。

- 如果数据集 A 的 epiplexity 很高，数据集 B 的 epiplexity 也很高
- 这两组结构能否在同一个模型里叠加？
- 还是会相互压制、相互干扰？

比如：

- 文本预训练学到语言结构
- 代码预训练学到逻辑结构

混合训练到底是在叠加结构，还是在制造冲突？

如果高 epiplexity 只是“必要条件”，那么结构之间是否兼容，也许才是泛化继续提升的“充分条件”之一。

## Promoted wiki pages

- [[wiki/concepts/Epiplexity]]
- [[wiki/topics/Learnable Structure in Data]]

## Source

- Paper: https://arxiv.org/html/2601.03220
- Original note: `/Users/zenk/Documents/notes/20260313T211723--paper-epiplexity__read.org`
