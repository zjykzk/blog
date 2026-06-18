---
title: LLM 协作思维阶段
category: concepts
type: concept
status: draft
tags: [llm, thinking, workflow, context]
sources:
  - conversation:2026-06-18
created: 2026-06-18T00:12:11+0800
updated: 2026-06-18T00:12:11+0800
summary: >-
  LLM 协作应显性化人类当前处于探索、头脑风暴、决策还是执行阶段，因为不同阶段需要不同的回答形态、深度和验证标准。
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-06-18
aliases:
  - Exploring Brainstorming Deciding Implementing
  - LLM 协作阶段
  - 思维阶段显性化
---
# LLM 协作思维阶段

LLM 协作思维阶段，是把人类解决复杂问题时所处的认知阶段显性化，让模型匹配当前真正需要的输出形态，而不是把所有请求都当成同一种问答或执行任务。

## What It Is

人在解决复杂问题时，并不总是处在同一个阶段。有时是在探索原理，有时是在发散可能性，有时是在做权衡决策，有时是在精确执行。阶段不同，模型应该承担的角色也不同。

这个框架把常见协作阶段分成四类：

1. Exploring（探索）：需要知识、原理、解释和类比，而不是代码实现或立即方案。
2. Brainstorming（头脑风暴）：需要广度和多种可能性，不急于收束到唯一结论。
3. Deciding（决策）：需要深度、逻辑和 trade-off，不需要长篇选项清单，而需要一个有充分理由的单一建议。
4. Implementing（执行）：需要精度、规范和可运行产物；之前的决策已经定下，目标是把它做对。

## How It Works

阶段显性化本质上是给 LLM 一个上层任务路由信号。它先回答“现在这轮协作的认知目标是什么”，再决定解释、发散、权衡或执行的比例。^[inferred]

```text
Exploring      -> 原理 / 背景 / 类比 / 概念边界
Brainstorming  -> 选项 / 变体 / 可能性 / 组合
Deciding       -> 权衡 / 取舍 / 风险 / 单一建议
Implementing   -> 精确步骤 / 代码 / 测试 / 验证
```

如果不显性化阶段，LLM 容易错配：在探索阶段过早给方案，在头脑风暴阶段过早下结论，在决策阶段堆列表，在执行阶段继续抽象讨论。^[inferred]

## Stage Details

### Exploring

探索阶段的核心是理解对象。好回答应该多解释“为什么”、提供类比、展开概念边界，并指出常见误解。此时过早进入实现，会让人跳过问题定义和原理建模。

### Brainstorming

头脑风暴阶段的核心是扩展搜索空间。好回答应该提供多种方向、不同假设和组合可能，不要急着压成一个答案。此时评价标准不是最优，而是覆盖足够多的可行分支。

### Deciding

决策阶段的核心是收束。好回答应该明确比较 trade-offs、识别关键约束、排除次优路径，并给出一个带理由的建议。此时不需要“十个选项”，需要的是判断。

### Implementing

执行阶段的核心是精度。好回答应该遵守已定决策，产出具体代码、配置、文档或操作步骤，并通过测试、运行或检查证明结果成立。此时继续讨论开放选项会降低交付质量。

## When to Use

这个框架适合用于复杂工程问题、学习问题、写作问题、产品决策和 AI 编程协作。它尤其适合在人类与 LLM 的长对话中作为模式声明：

```text
当前阶段：Exploring。请先帮我理解原理，不要急着给方案。
当前阶段：Deciding。请给一个建议，并说明为什么放弃其他选项。
当前阶段：Implementing。不要再发散，直接按已有决策完成并验证。
```

它也可以作为团队 AI 协作规范：需求讨论用 Exploring/Brainstorming，方案评审用 Deciding，开发落地用 Implementing。^[inferred]

## Related

- [[wiki/sources/面向 LLM 的清晰表达 Source Guide]] — 阶段显性化是面向 LLM 清晰表达的一种高层上下文约束。
- [[wiki/concepts/Human-LLM Co-Planning Interaction Space]] — co-planning 中的人类干预也需要按控制力度、范围和阶段选择交互方式。
- [[wiki/topics/Problem Framing]] — 探索和决策阶段都依赖先把问题边界和成功标准说清楚。
- [[wiki/topics/Context Management]] — 阶段信号是进入上下文的决策相关信息，可减少模型自由猜测。
