---
title: Confusion Matrix
type: concept
status: draft
category: concepts
tags: [metrics, testing, judgment, agents]
aliases:
  - 混淆矩阵
  - 最终结论混淆矩阵
relationships:
  - target: "[[wiki/concepts/Evaluation]]"
    type: implements
  - target: "[[wiki/concepts/Agent Evaluation Metric Vector]]"
    type: related_to
  - target: "[[wiki/topics/Rule Adjudication Agent Evaluation]]"
    type: related_to
sources:
  - conversation:2026-10-10
created: 2026-10-10T19:36:48+0800
updated: 2026-10-10T19:36:48+0800
summary: >-
  混淆矩阵把标准答案与系统预测交叉计数，使总体准确率隐藏的漏报、误伤、错误拒判和过度裁决方向可见。
provenance:
  extracted: 0.87
  inferred: 0.12
  ambiguous: 0.01
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-10
tier: supporting
---

# Confusion Matrix

混淆矩阵是一张把标准答案与系统预测交叉统计的表。它不仅回答“一共答对多少”，还回答“把哪一类错判成了哪一类”。

## What It Is

矩阵的一条轴放标准答案，另一条轴放系统输出。对角线表示预测正确，非对角线表示具体的错误方向。

在二分类里，混淆矩阵区分 true positive、false positive、false negative 和 true negative；在多分类规则裁决中，它可以继续扩展为违规、符合、不适用、证据不足和人工复核等类别。

它与单一 accuracy 的关键差别是：accuracy 把所有错误合并，混淆矩阵保留错误的对象与方向。两个系统即使准确率相同，也可能具有完全不同的风险。

## How It Works

下面是一个虚构示例，数字只用于说明读法：

| 标准答案 \\ Agent 判断 | 违规 | 符合 | 证据不足 | 不适用 | 人工复核 |
|---|---:|---:|---:|---:|---:|
| 违规 | 80 | 8 | 5 | 3 | 4 |
| 符合 | 5 | 85 | 3 | 5 | 2 |
| 证据不足 | 10 | 15 | 65 | 3 | 7 |
| 不适用 | 2 | 3 | 2 | 90 | 3 |
| 人工复核 | 3 | 2 | 5 | 4 | 86 |

第一行表示 100 个真实违规案例中，80 个被正确发现，8 个被错误放行，5 个被拒绝判断，3 个被误判为规则不适用，4 个被送去人工复核。

第三行展示了另一类风险：真实答案是证据不足时，Agent 有 10 次武断地判为违规、15 次武断地判为符合。这些“过度裁决”在总体准确率里只表现为普通错误，但在自动处罚、拒绝交易或合规报告中可能具有不同后果。

## When to Use

当输出是互斥类别，而且标准答案足够可信时，混淆矩阵适合检查分类器或规则裁决 Agent 的最终结论。

在 [[wiki/topics/Rule Adjudication Agent Evaluation|规则裁决 Agent 评测]] 中，至少关注三个方向：

- 真实违规被判为符合或不适用：漏报；
- 真实符合被判为违规：误伤；
- 真实证据不足被判为违规或符合：过度裁决。

风险发现系统通常更重视减少漏报，自动执法或封禁系统通常更重视减少误伤。矩阵本身不决定哪种错误更严重；业务规则必须为不同格子赋予代价。^[inferred]

混淆矩阵只评价最终类别，不说明推理过程是否正确。一个 Agent 可能碰巧给出正确标签，却使用了错误规则或虚构证据；因此它必须与规则适用性、构成要件、证据引用、例外处理和轨迹检查结合。

如果标签彼此重叠、标准答案不可靠，或任务输出是连续分数而不是类别，普通混淆矩阵就不再足够，需要改用多标签指标、回归指标或人工裁决。

## Related

- [[wiki/topics/Rule Adjudication Agent Evaluation]] — 将混淆矩阵放入完整裁决链。
- [[wiki/concepts/Agent Evaluation Metric Vector]] — 将成功率扩展为多维 Agent 轨迹指标。
- [[wiki/concepts/Evaluation]] — 评价尺度与语境的一般结构。
- [[wiki/concepts/Judgment Externalization]] — 让标准答案和裁决依据可保存、复核和修正。

