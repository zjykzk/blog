---
title: Theory Is All You Need Source Guide
type: source
status: seed
category: sources
summary: 这页保留 Teppo Felin 与 Matthias Holweg 的论文 Theory Is All You Need: AI, Human Cognition, and Causal Reasoning 的阅读导览。
sources: []
created: 2026-05-01
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-05
source_count: 1
updated: 2026-05-01
aliases:
  - Theory Is All You Need
  - AI Human Cognition and Causal Reasoning
  - Felin Holweg Theory Is All You Need
tags:
  - paper
  - cognition
  - causal-reasoning
source: /Users/zenk/Downloads/ssrn-4737265.pdf
---
# Theory Is All You Need Source Guide

这页保留 Teppo Felin 与 Matthias Holweg 的论文 *Theory Is All You Need: AI, Human Cognition, and Causal Reasoning* 的阅读导览。

论文的核心价值不在于证明“AI 不行”，而在于把 AI 和人的差异从“算力强弱”改写成“认知方向不同”：

- AI 擅长从过去数据里做预测、重组、翻译和模仿。
- 人能先持有一个尚未被数据支持的理论，再用因果推理和实验去制造新数据。

## Source facts

- Authors: Teppo Felin, Matthias Holweg
- Venue: *Strategy Science*, 2024
- DOI: https://doi.org/10.1287/stsc.2024.0189
- SSRN: https://ssrn.com/abstract=4737265
- Local PDF: `/Users/zenk/Downloads/ssrn-4737265.pdf`

## Core claim

AI 的基本动作是“从已有数据中预测下一个最可能的东西”。这在重复、稳定、可从过去外推的任务中很强。

但不确定性下的关键决策，经常不是预测过去会怎样延续，而是提出一个现在缺少证据的未来状态，然后设计实验让它变成现实。

所以论文真正反对的是一个隐含前提：把人脑和机器都当成输入-处理-输出装置。

## Problem

很多 AI 讨论默认：

- 人有偏见、算得慢、处理不了大数据。
- 机器处理数据更多、更稳定，所以最终会替代人做判断。
- 认知本质上就是信息处理和预测。

作者认为这个框架漏掉了人的一个关键能力：人不只是接收数据，也会决定什么数据值得找，甚至会通过行动把新数据造出来。

## Key distinction

### Data-belief symmetry

这是 AI 和贝叶斯式认知模型更接近的状态：

- 先有数据。
- 数据支持某个信念。
- 信念强度随证据强度更新。

这适合处理已经有大量样本、结构稳定的问题。

### Data-belief asymmetry

这是作者认为人类创新更关键的状态：

- 先有一个与现有数据不对称的信念。
- 它可能看起来像妄想、偏见或逆证据而行。
- 但这个信念驱动人去推理、行动、实验，最后生成原先不存在的数据。

这不是说“无视证据总是对的”。而是说，在新知识和新机会出现之前，证据常常本来就不存在。

## Wright brothers example

论文用重于空气的飞行说明这个差异。

当时很多科学判断都不支持人类飞行。大型鸟类、重量、失败案例和已有理论都能被解释成“飞不起来”的证据。

莱特兄弟没有把问题停在“现有数据支不支持飞行”。他们持有一个不被充分支持的信念：飞行可能。然后他们把这个信念拆成因果问题：

- 升力
- 推进
- 转向与控制

接下来他们不是泛泛搜集更多证据，而是围绕这些因果环节做定向实验。风洞、翼型测试、角度测试、地点选择，都是为了生成能检验理论的新数据。

这里的关键不是“相信自己”。关键是：

> 理论决定该看什么数据，也决定该制造什么数据。

## What this adds to the wiki

### 1. 对 LLM 的边界判断

这篇论文给 `[[wiki/concepts/LLM]]` 增加一个更底层的边界：LLM 的生成性主要是组合式生成。它能把已有语言结构重组得很流畅，但这不等于它拥有面向未来的因果理论。

所以不能只问“模型会不会输出新句子”，要问：

- 它是否提出了一个可行动的因果假设？
- 它是否知道该去生成哪些新数据？
- 它是否能区分频率更高的共识和少数但正确的理论？

### 2. 对 AI 工作流的启发

AI 更适合做：

- 摘取已有资料
- 重组表达
- 比较候选方案
- 暴露遗漏
- 作为策略讨论中的反方或陪练

人更需要保留：

- 问题定义
- 异质信念
- 因果假设
- 实验设计
- 最终判断责任

这与 `[[wiki/concepts/Cognitive Engineering]]` 的判断一致：好的人机系统不是把判断外包给 AI，而是让 AI 扩大人的认知带宽。

### 3. 对战略和产品判断的启发

如果所有人都使用同样的预测机器，输出会趋同。

真正的战略差异不来自“我比别人更会预测平均值”，而来自：

- 我相信哪个尚未被数据充分支持的未来？
- 我看到哪个别人没看到的因果路径？
- 我能做什么实验，把这个未来的一小块变成数据？

这与 `[[wiki/topics/Problem Framing]]` 和 `[[wiki/topics/Thinking in Systems]]` 可以接上：问题不是找到更多表层数据，而是重画因果结构和行动边界。

## Useful distinction to keep

预测型问题：

- 过去样本多
- 结构稳定
- 目标清楚
- 错误可以用历史数据校正

理论型问题：

- 样本少或不存在
- 结构正在变化
- 目标本身需要定义
- 需要通过行动和实验制造新数据

AI 在第一类问题里强。人和 AI 的联合系统，真正难的是第二类问题。

## Open questions

- 如果 LLM 没有自己的 forward-looking theory，它能否帮助人更好地构造 theory？
- 什么样的提示、工具和记忆结构能迫使 AI 从“预测答案”转向“帮助设计实验”？
- 在组织里，如何区分“有理论的逆势判断”和“只是自信的幻觉”？
- RAG 和专有语料能提高 AI 的特定性，但能否产生真正的异质信念，还是只会更好地服务人的理论？

## Promoted wiki pages

- [[wiki/concepts/LLM]]
- [[wiki/concepts/Cognitive Engineering]]
- [[wiki/topics/Problem Framing]]
- [[wiki/topics/Thinking in Systems]]
- [[wiki/maps/AI Map]]

## Related

- [[wiki/sources/Epiplexity Paper Notes]]
- [[wiki/sources/LLM Reasoning Is Latent, Not the Chain of Thought Source Guide]]
- [[wiki/sources/Qiaomu Best Prompt Source Guide]]

## Source

- Local PDF: `/Users/zenk/Downloads/ssrn-4737265.pdf`
- SSRN abstract: https://ssrn.com/abstract=4737265
- DOI: https://doi.org/10.1287/stsc.2024.0189
