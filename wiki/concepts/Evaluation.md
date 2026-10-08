---
title: Evaluation
type: concept
status: draft
category: concepts
summary: Evaluation is the act of placing an object inside a scale so its value, quality, meaning, or position can appear.
tags:
  - thinking
  - concepts
  - judgment
sources:
  - /Users/zenk/Documents/notes/20260506T204024--概念解剖-评价__concept.org
  - https://mathandai.org/multilingual.php?lang=zh
  - https://hamel.dev/blog/posts/evals-faq/
provenance:
  extracted: 0.74
  inferred: 0.26
  ambiguous: 0.00
base_confidence: 0.73
lifecycle: draft
lifecycle_changed: 2026-05-06
created: 2026-05-06T20:58:15+08:00
updated: 2026-10-05T16:18:21+0800
aliases:
  - 评价
  - assessment
  - appraisal
  - value judgment
---
# Evaluation

Evaluation is the act of placing an object inside a scale so its value, quality, meaning, or position can appear.

Its central danger is mistaking evaluation for pure preference, neutral measurement, or final judgment. Evaluation always contains an object, a scale, a context, and the evaluator's position.

## Core Structure

- Evaluation begins with an object whose worth, quality, or meaning is not yet settled.
- It applies a scale: criteria, standards, weights, norms, goals, or expectations.
- It happens inside a context, so the same object can receive different evaluations in family, school, market, science, or governance settings.
- It produces consequences: the evaluated object may be selected, ranked, corrected, ignored, internalized, or reshaped.

A compact formula is:

```text
Evaluation = object + scale + context + evaluator position -> value form
```

## Evaluation and Judgment

Evaluation is one operation inside [[wiki/syntheses/Thinking and Judgment Workflow]]: it gives judgment a scale, but judgment still has to decide whether that scale is appropriate.

This matters because a precise score can still be a weak evaluation if it measures the wrong thing. Strong evaluation should reveal the object's structure and direction, not merely compress it into a sortable number. ^[inferred]

## Relation to Thinking Tools

[[wiki/topics/Critical Thinking]] audits evaluation by asking whether the criteria, evidence, assumptions, and omissions are defensible.

[[wiki/topics/Mental Models]] provide reusable scales for evaluation, but they also risk making one scale look like the whole world. ^[inferred]

[[wiki/topics/Categorical Thinking]] often precedes evaluation: once a thing is classified, a category-specific standard becomes available.

[[wiki/concepts/Application]] depends on evaluation because practical action needs feedback about whether an abstract method actually fits a concrete situation.

## Failure Modes

- Treating personal liking as if it were a full evaluation.
- Treating quantitative scoring as if it were automatically objective.
- Using a scale that hides the object's most important qualities. ^[inferred]
- Letting evaluation become a tool of conformity rather than a way to help the object become more legible and more capable. ^[inferred]

## Proxy Validity When Production Changes

代理指标与最终目标之间的关联，需要在成果生产方式改变后重新检验。过去“解出难题”常伴随新方法与人的理解；AI 可以直接给出成果时，解题表现就不能单独证明使用者的理解、方法迁移或共同体培养能力同步增长。[[wiki/sources/Math and AI Misalignment Source Guide|数学与 AI 的目标错位]] 提供了这一风险案例，但没有证明所有解题评测均已失效。^[inferred]

评价既观察活动，也通过奖励和资源配置改变活动。若持续奖励易计数的产出，却不承认解释、整合和培养的贡献，就可能使指标提升与长期目标发生偏离；这条机制需要结合具体情境和证据判断。^[inferred]

## AI Product Evaluation as an Adaptive Loop

[[wiki/sources/AI Evals FAQ Source Guide|AI Evals FAQ]] 把产品评估放进一条由真实失败驱动的循环：审阅 traces，归纳 failure taxonomy，把领域专家的判断写成 rubric，再选择代码断言、人工审阅或经人工标签验证的分类器执行检查。生产中新发现的失败进入回归集，评估结果则指导 prompt、retrieval、tool、应用代码或产品流程的下一轮修改。

这条循环说明，评价尺度不是天然固定的。团队会在看到新输出后补充要求，产品与用户也会持续变化；因此 eval set 与 rubric 必须演化，历史分数只有在测试对象、案例难度和尺度保持可比时才适合直接比较。^[inferred]

好的 product eval 应检查单一、具体、可行动的失败。综合分数可以用于总览，但必须保留各项明细，才能知道究竟是哪种用户问题改善或恶化。

## Source Compression

The concept-anatomy source compresses evaluation into one sentence: evaluation is not saying whether something is good or bad, but making it appear in a particular value-form through a particular scale.

## Related

- [[wiki/sources/AI Evals FAQ Source Guide]]
- [[wiki/sources/Math and AI Misalignment Source Guide]]
- [[wiki/sources/Evaluation Concept Anatomy Source Guide]]
- [[wiki/topics/Critical Thinking]]
- [[wiki/topics/Mental Models]]
- [[wiki/topics/Categorical Thinking]]
- [[wiki/concepts/Application]]
- [[wiki/syntheses/Thinking and Judgment Workflow]]
