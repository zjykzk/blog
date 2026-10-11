---
title: >-
  Causal Reasoning
category: concepts
type: concept
status: draft
tags: [thinking, reasoning, mechanism, probability, judgment]
aliases:
  - 因果推理
  - 因果判断
  - causal inference
sources:
  - conversation:2026-09-07
  - wiki/sources/概念 因果 规律 机制与知识 Source Guide.md
created: 2026-09-07T23:52:13+0800
updated: 2026-10-11T17:53:08+08:00
summary: >-
  因果推理判断主动改变某个因素后结果是否会变化，核心是把相关性、共同原因、选择偏差和真实干预效应区分开。
provenance:
  extracted: 0.72
  inferred: 0.28
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-09-07
tier: supporting
---
# Causal Reasoning

因果推理是判断“如果主动改变 A，B 是否会因此变化”的推理方式。

## What It Is

因果推理不只是寻找两个现象是否一起出现，而是追问一个反事实问题：

```text
如果其他条件尽量不变，把 A 从不发生改成发生，B 会不会跟着变？
```

因此，它的核心对象不是历史数据里的模式，而是干预后的世界。相关性回答“看到 A 时，B 是否更常出现”；因果推理回答“改变 A 时，B 的结果分布是否会改变”。在形式上，统计依赖可以写成 `P(B | A) != P(B)`，因果效应则需要进入 `P(B | do(A))` 这类干预语义。

这让因果推理成为 [[wiki/concepts/Relation as Contextual Constraint|关系作为语境约束]] 中更强的一类关系：它不仅要求两个对象在语境中有关，还要求这种关系在主动干预下仍能改变结果。

## How It Works

因果推理通常从三个对象开始：处理、结果和混杂因素。

处理是要改变的东西，结果是要观察的后果，混杂因素是同时影响处理和结果、从而制造假象的变量。比如平台发现“收到优惠券的人购买率更高”。这里“是否收到优惠券”是处理，“是否购买”是结果，“用户活跃度”可能是混杂因素，因为活跃用户更可能被系统发券，也更可能本来就会购买。

如果不处理混杂因素，分析会把“人本来更可能买”错算成“优惠券让人购买”。这就是因果推理和普通预测之间的关键差别：预测模型可以利用任何稳定相关性提高预测准确率；因果推理必须判断这个关系在行动后是否仍然成立。^[inferred]

一条最小因果推理链可以写成：

```text
处理 A -> 结果 B
    ^        ^
    |        |
混杂因素 C --+
```

好的因果分析会继续追问：C 是否同时影响 A 和 B？有没有反向因果，即 B 影响 A？有没有选择偏差，即样本进入观察的方式已经改变了关系？有没有中介变量，即 A 通过某个路径 M 影响 B？

## From Correlation to Intervention

“带伞的人更容易出现在下雨天”只说明带伞和下雨相关。因果推理会问：如果让所有人都带伞，雨会变多吗？不会。天气才是共同原因，它同时影响是否带伞和是否下雨。

“医院 A 死亡率比医院 B 高”也不能直接推出医院 A 医术更差，因为医院 A 可能收治更多重症患者。患者病情同时影响进入哪家医院和死亡风险；如果不控制病情，医院差异就可能只是病例结构差异。

“使用 AI 工具的人产出更高”同样需要拆开：是工具提高了产出，还是高产出的人更愿意使用工具？是否存在岗位、能力、任务类型、管理要求等共同原因？如果把同类人随机分成使用和不使用，结果差异还会存在吗？这些问题把叙事从“看起来有关”推进到“是否值得作为行动杠杆”。^[inferred]

## Methods and Boundaries

最干净的因果证据来自随机实验，因为随机分配能打断很多混杂路径。不能实验时，倾向得分匹配、双重差分、工具变量、断点回归等方法，本质上都在尝试从观测数据中构造一个更接近反事实的比较。

这些方法不是魔法。它们依赖前提：随机化是否真的执行，趋势是否可比，工具变量是否只通过处理影响结果，断点附近的个体是否可比。因果推理因此既需要 [[wiki/topics/Probability|概率]] 的不确定性语言，也需要 [[wiki/concepts/Mechanism Model|机制模型]] 对变量、路径和边界的解释。

这也解释了为什么因果推理不能只等同于“找根因”。根因分析常从一个已发生结果向前追问原因；因果推理还要判断：如果改变候选原因，未来结果是否会改变。前者偏诊断，后者偏干预判断。^[inferred]

## When to Use

只要问题里含有“如果我做 X，会不会导致 Y 改变”，就应该进入因果推理。它适合用于产品实验、政策评估、医学疗效、教育干预、管理改进、工程治理和个人决策。

使用时先问五个问题：

1. 我想改变的处理是什么？ ^[inferred]
2. 我要观察的结果是什么？ ^[inferred]
3. 哪些变量同时影响处理和结果？ ^[inferred]
4. 有没有反向因果、选择偏差或遗漏变量？ ^[inferred]
5. 什么比较最接近“同一对象在做与不做之间的差异”？ ^[inferred]

因果推理的判断抓手可以压缩成一句话：**不要把历史数据里的同现关系直接当成行动杠杆；先问干预是否会改变结果，以及这个判断依赖哪些可被反驳的假设。**

## Related

- [[wiki/concepts/Relation as Contextual Constraint]]
- [[wiki/concepts/Mechanism Model]]
- [[wiki/topics/Probability]]
- [[wiki/concepts/Knowledge Types]]
- [[wiki/concepts/Reasoning as Structure Mapping]]
- [[wiki/topics/Critical Thinking]]
- [[wiki/sources/概念 因果 规律 机制与知识 Source Guide]]
- [[wiki/sources/Theory Is All You Need Source Guide]]
