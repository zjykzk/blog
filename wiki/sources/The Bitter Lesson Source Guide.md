---
title: The Bitter Lesson Source Guide
type: source
status: draft
category: sources
tags:
  - training
  - llm
  - cognition
  - article
aliases:
  - Bitter Lesson
  - Rich Sutton Bitter Lesson
  - 苦涩的教训
sources:
  - http://www.incompleteideas.net/IncIdeas/BitterLesson.html
  - conversation:2026-08-16
created: 2026-08-16T16:29:01+0800
updated: 2026-08-16T16:29:01+0800
summary: >-
  Source guide for Rich Sutton's 2019 essay The Bitter Lesson, arguing that general methods scaling with computation — search and learning — beat built-in human knowledge in the long run.
provenance:
  extracted: 0.85
  inferred: 0.13
  ambiguous: 0.02
base_confidence: 0.5
lifecycle: draft
lifecycle_changed: 2026-08-16
---

# The Bitter Lesson Source Guide

> Source: Rich Sutton, "The Bitter Lesson" (2019-03-13), `http://www.incompleteideas.net/IncIdeas/BitterLesson.html`. Full essay pasted inline in the capturing conversation.

## What It Covers

这篇短文从 70 年 AI 研究史提炼出一个反复出现的模式：**能随算力扩展的通用方法，长期总会压过依赖人类领域知识的方法**。其根本驱动力是摩尔定律（更一般地说，单位算力成本持续指数级下降）。

## Key Points

- 长期唯一起决定作用的，是**对算力的利用**；人类知识路线短期有效、令研究者满足，但长期会触顶甚至阻碍进步。^[extracted]
- 两类能"任意随算力扩展"的方法是 **search（搜索）** 与 **learning（学习）**。^[extracted]
- 历史例证：计算机国际象棋（1997 深度搜索击败 Kasparov）、计算机围棋（搜索 + 自我对弈价值函数）、语音识别（HMM 等统计方法胜过基于音素/声道知识的方法）、计算机视觉（卷积网络取代 SIFT/边缘/广义柱体等手工特征）。^[extracted]
- 苦涩之处在于：胜利总是"通用、可扩展的方法"战胜"研究者偏爱的、以人为中心的方法"，且常常不被完全接受。^[extracted]
- 第二个更深的结论：**心智的实际内容无可救药地复杂**；不该把这种复杂性手工写进系统，而应只内置"能发现并捕获这种复杂性的元方法"。^[extracted]
- 收口句："the search for them should be by our methods, not by us"——要造能像我们一样去发现的 agent，而不是装着我们已发现之物的 agent。^[extracted]

## How It Enters the Wiki

这篇文章不作为一次性摘要，而是支撑两页可复用概念：

- [[wiki/concepts/Search and Learning as Meta-Methods]] —— 为什么 search / learning 是"元能力"，其本质是什么，以及人类学习/搜索为何是同一台引擎（算力预付在演化与文化）。
- [[wiki/concepts/Class as Learned Invariance]] —— 承接文中"内置不变性"的思想，回答学习如何判断"同一类"：把类理解为学到的等价关系/不变性。

## Open Questions

- Bitter Lesson 常被误读为"人类知识无用"。文中其实说的是二者"不必对立，但实践中往往此消彼长"；边界仍取决于时间尺度与算力预期。^[ambiguous]
- "只内置元方法"在工程上并不彻底：卷积、注意力等仍是被内置的结构先验；如何界定"元方法"与"领域知识"的分界仍有争议。^[inferred]

## Related

- [[wiki/concepts/Search and Learning as Meta-Methods]]
- [[wiki/concepts/Class as Learned Invariance]]
- [[wiki/topics/Learnable Structure in Data]]
- [[wiki/concepts/Mechanism Model]]
- [[wiki/maps/AI Map]]
- [[wiki/maps/Learning Map]]
