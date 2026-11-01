---
title: Software Engineering as Knowledge Discovery
type: concept
status: draft
category: concepts
summary: 软件开发把未知问题与业务判断逐步转成可执行、可检验的知识；外部变化会加速模型失效，但未知本身已足以要求持续学习。
tags: [software-engineering, learning, cognition, knowledge, feedback]
sources:
  - inline:software-engineering-learning-imperative-2026-11-01
  - wiki/sources/默会知识 AI 永远都不可能替代的技能 Source Guide.md
relationships:
  - target: "[[wiki/topics/Modern Software Engineering]]"
    type: related_to
  - target: "[[wiki/concepts/Tacit Knowledge]]"
    type: uses
  - target: "[[wiki/concepts/Executable Specification]]"
    type: related_to
  - target: "[[wiki/concepts/Feedback Loops]]"
    type: uses
aliases:
  - 软件工程作为知识发现
  - 软件开发的知识发现本质
  - Software Development as Knowledge Acquisition
provenance:
  extracted: 0.58
  inferred: 0.34
  ambiguous: 0.08
base_confidence: 0.55
lifecycle: draft
lifecycle_changed: 2026-11-01
tier: supporting
created: 2026-11-01T22:57:50+0800
updated: 2026-11-01T22:57:50+0800
---

# Software Engineering as Knowledge Discovery

软件开发不只是把一份完整需求翻译成代码。它也在发现问题边界、业务规则、失败模式、价值取舍和系统约束，再把暂时理解转成可执行、可反驳的结构。

## Core Distinction

“世界会变化”和“我们一开始就不知道完整答案”是两种不同的不确定性：

- **外部变化**使已经正确的模型过期，要求系统与组织重新学习。
- **先验未知**意味着模型在第一次构建时就不完整，即使环境冻结，也必须通过实践暴露遗漏。
- **默会知识**意味着相关知识可能存在于人的判断和行动里，却不能一次性完整转录为静态文本。

因此，变化会提高学习速度不足的代价，却不是学习必要性的唯一来源。只要问题知识不完备，开发就包含发现活动。^[inferred]

## The Knowledge Conversion Loop

```text
未知问题与局部经验
        ↓
对话、实例、原型与模型
        ↓
规格、代码与测试中的可执行假设
        ↓
运行、失败、用户行为与生产证据
        ↓
修正问题模型、规则与系统边界
```

这条循环不是把知识无损搬运到代码。每一层都在选择、压缩和形式化：

- 业务对话把分散经验变成可共享的候选解释；
- examples、Given-When-Then 和原型把判断放进具体情境；
- [[wiki/concepts/Executable Specification|可执行规格]]把部分意图变成机器可检查承诺；
- 代码让模型真正产生行为与后果；
- [[wiki/concepts/Feedback Loops|反馈]]暴露规格、实现、环境或价值判断的偏差。

规格可执行不等于规格正确。它只使某些承诺更容易被重复检查；是否对准真实需要仍属于 validation。^[inferred]

## Why Practice Reveals Unknowns

会议和文档主要处理已经进入注意范围的问题。原型、切片、测试和真实运行还会生成新的证据：

- 某条规则无法覆盖边界案例；
- 两位业务专家依赖不同的隐含前提；
- 单独正确的组件在组合后产生新行为；
- 用户实际目标不同于最初表达；
- 质量属性只在负载、故障或组织交接中显现。

这类证据使“不知道自己不知道什么”逐步变成可命名、可建模、可验证的问题。把这一过程称为具体的“五阶无知模型”或归于某位作者，需要回到原始材料核验。^[ambiguous]

## Tacit Knowledge and Shared Understanding

[[wiki/concepts/Tacit Knowledge|默会知识]]不是“永远不能说”的神秘内容，而是无法在当前表达、记录与训练条件下一次性完整外化的技能和判断。^[inferred]

软件工程通过多种社会与技术机制提高传递带宽：

- 与业务专家共同工作，而不是只传递需求文档；
- 用具体例子、事件、反例和边界场景校准词义；
- 让模型、原型和测试成为可共同指认的中介物；
- 用代码评审、结对、事件风暴和运行复盘传递判断依据；
- 把重复出现且可稳定表达的判断沉淀为规则、规格、检查与工具。

这些机制不能消除默会层，但能不断改变显性与默会的边界。^[inferred]

## Relation to Modern Software Engineering

[[wiki/topics/Modern Software Engineering]]把“成为学习专家”与“管理复杂性”放在更完整的价值、规格、构造、证据、演化和治理闭环中。本概念页只解释学习回路为什么不可缺少，不主张知识发现等同于软件工程的全部。

学习与复杂性管理互相制约：每次发现都可能要求系统改变，而模块化、信息隐藏、低反馈延迟和可逆发布又降低下一次学习的成本。^[inferred]

## Context-Sensitive Action

[[wiki/concepts/Cynefin Framework]]提醒团队按情境选择动作：

- obvious 问题可以标准化；
- complicated 问题可以分析并调用专家知识；
- complex 问题需要安全的小探针，再观察模式；
- chaotic 问题先止损，再恢复感知能力。

因此，“经验主义”不是拒绝计划或把所有工作都做成实验，而是在无法可靠先验推导的部分缩小批量、缩短反馈，并让失败保持可承受。^[inferred]

## Open Questions

- 怎样判断一个未知可以通过分析消除，还是必须通过运行探针暴露？
- 哪些业务判断适合形式化为规格，哪些应保留人工裁决和责任入口？
- AI 扩大知识外化能力后，会减少哪些默会层，又会生成哪些新的判断盲区？

## Related

- [[wiki/sources/软件工程为何必须成为学习专家 Source Guide]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/concepts/Tacit Knowledge]]
- [[wiki/concepts/Knowledge Types]]
- [[wiki/concepts/Cynefin Framework]]
- [[wiki/concepts/Executable Specification]]
- [[wiki/concepts/Feedback Loops]]
- [[wiki/concepts/业务隐含复杂度]]
