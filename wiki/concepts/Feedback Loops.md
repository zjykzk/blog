---
title: Feedback Loops
type: concept
status: draft
category: concepts
summary: Feedback loops are system structures where results flow back to influence future causes, creating growth, stability, or oscillation.
tags: []
sources:
  - https://martinfowler.com/articles/reduce-friction-ai/feedback-flywheel.html
  - https://donellameadows.org/wp-content/userfiles/iceberg-model.pdf
  - mobu/读书/架构师启示录-知识模型、落地方法与思维模式.md
  - mobu/读书/架构师启示录-知识模型、落地方法与思维模式_第8章及以后章节.md
created: 2026-04-26
base_confidence: 0.61
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.94
  inferred: 0.06
  ambiguous: 0.00
updated: 2026-05-13T00:06:14+08:00
aliases:
  - 反馈回路
  - Feedback Loop
  - Positive and Negative Feedback
---
# Feedback Loops

反馈回路是系统里“结果反过来影响原因”的闭环。

没有回路，就只有线性因果；有了回路，系统才会出现增长、稳定、振荡、失控、恢复这些动态行为。

## 两种基本类型

### 正反馈

结果会进一步放大自己。

典型表现：
- 增长越来越快
- 优势越滚越大
- 失控一旦开始就难停下

它能产生增长，也能产生泡沫、垄断、崩塌。

### 负反馈

结果会反过来抑制偏离，把系统拉回某个目标区间。

典型表现：
- 自动调节
- 保持稳定
- 偏了再拉回

它是稳定性的来源，但如果回路太慢、太弱，也可能导致迟钝或振荡。

## 为什么重要

系统行为往往不是由单个动作决定，而是由回路决定。

在 [[wiki/concepts/Iceberg Model]] 里，反馈回路属于把事件变成重复模式的结构层；如果不识别回路，人容易把系统行为误读成单个事件。^[inferred]

所以分析问题时，关键不是只问“谁影响了谁”，而是问：

- 这个结果会不会反过来作用于自己？
- 这个作用是在放大，还是在纠偏？
- 回路里有没有延迟？

## 延迟会让回路变得反直觉

很多系统出问题，不是没有负反馈，而是负反馈来得太慢。

这样人就会：
- 在有效动作见效前放弃
- 在系统已经过头后继续加码
- 把真正原因和表面结果配错

所以回路分析几乎总要和延迟一起看。

## 四个常见场景

### 产品

更好的体验 -> 更高留存 -> 更多行为数据 -> 更好的产品优化 -> 更好的体验

### 组织

KPI -> 行为选择 -> 文化固化 -> 强化 KPI 的现实合理性 -> 更强 KPI 依赖

### 学习

输出 -> 发现漏洞 -> 修正理解 -> 更高质量输入 -> 更强输出

### AI Agent

更好的记忆 -> 更好的决策 -> 更高质量结果 -> 更好的记忆写回

### AI-assisted development

[[wiki/concepts/Feedback Flywheel]] is a concrete software-engineering feedback loop: AI collaboration produces outputs, reviews, corrections, accepted work, and rework; those signals update priming documents, context anchors, standards, workflows, checks, and guardrails.

The delay matters. If the team waits too long to update the artifacts, the same AI mistakes repeat. If the team updates after every isolated event, the system can accumulate noisy rules. ^[inferred]

### 架构演进与系统维护

《架构师启示录》把敏捷理解为一种负反馈：尽快知道当前进度和目标之间的差距，然后据此调整行动。DevOps 则减少研发、QA、运维之间的信息差，让反馈更快进入交付链路。

在系统维护中，笔记还把系统问题分为事件、行为、结构三个层次：事件是负载变高，行为是负载在某类情况下持续变高，结构才是产生这些事件和行为的根因。这使反馈回路不只是一个抽象系统概念，也成为架构演进和故障分析的方法。

## 一个判断句

如果某个结果会通过某条路径回头影响自己，那你看到的就不是链，而是环。

## Related

- [[wiki/topics/Thinking in Systems]]
- [[wiki/concepts/Iceberg Model]]
- [[wiki/topics/Problem Framing]]
- [[wiki/topics/Learning Methodology]]
- [[wiki/concepts/Leverage Points]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/topics/Thinking in Systems]]
