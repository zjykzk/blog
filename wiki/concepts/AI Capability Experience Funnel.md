---
title: AI Capability Experience Funnel
type: concept
status: draft
category: concepts
tags: [agents, llm, harness, judgment, mechanism]
aliases:
  - AI 能力体验漏斗
  - AI 能力认知漏斗
  - AI shared understanding gap
relationships:
  - target: "[[wiki/sources/AI Capability Experience Funnel Source Guide]]"
    type: derived_from
  - target: "[[wiki/concepts/Agent]]"
    type: related_to
  - target: "[[wiki/topics/AI Harness]]"
    type: related_to
  - target: "[[wiki/concepts/Verification Gap]]"
    type: related_to
  - target: "[[wiki/concepts/Understanding]]"
    type: related_to
sources:
  - https://x.com/karpathy/status/2109361546505966046
  - conversation:2026-10-17
created: 2026-10-17T23:51:28+0800
updated: 2026-10-17T23:51:28+0800
summary: >-
  AI 能力体验漏斗说明，同一时期的人会因模型访问、任务跨度、领域可验证性与工作流成熟度不同，形成彼此冲突却局部合理的 AI 能力判断。
provenance:
  extracted: 0.35
  inferred: 0.60
  ambiguous: 0.05
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-17
tier: supporting
---

# AI Capability Experience Funnel

AI 能力体验漏斗是一个区分“模型潜力”和“用户实际体验”的框架：一个人看见的 AI 能力，不只由模型决定，还由访问等级、任务规模、执行跨度、领域可验证性和工作流成熟度共同决定。

## What It Is

社会中关于 AI 的分歧，不一定只是有人高估、有人低估。很多人实际接触到的是不同系统：

- 未接触者通过新闻和他人描述理解 AI；
- 偶尔用户通过短问答和免费聊天产品理解 AI；
- 专业用户通过真实代码库、数学问题和长任务理解 AI；
- 内部使用者通过更高预算、更长执行时间和更复杂编排理解 AI。

这些经验都可能真实，却无法直接相互校准。漏斗越往下，人越少，任务越大，系统越复杂，公开可复现性通常也越弱。

## Capability Layers

能力判断至少要拆成三层：

1. **模型能力**：模型参数和训练本身提供的潜在能力。
2. **系统能力**：模型加上工具、上下文、记忆、权限、环境、编排和验证器后形成的能力。
3. **体验到的能力**：具体用户在自己的访问等级、问题储备和工作方式中实际观察到的能力。

可以把它写成一个结构公式：

> 体验到的能力 ≈ 模型 × 访问 × 任务跨度 × 可验证性 × 工作流成熟度 × 大问题储备。^[inferred]

这不是定量模型，而是一个诊断表：任何一项不足，都可能使其他能力无法显现。^[inferred]

## How It Works

### 任务跨度暴露不同能力

短问答主要测语言生成和局部知识。长任务则要求状态保持、工具使用、计划修正、错误恢复、资源管理和停止判断。任务跨度改变后，被测试的已经不是同一种能力。^[inferred]

### 可验证性形成能力尖峰

代码和数学能提供编译、测试、证明检查、运行结果等快速反馈，因此容易形成训练和部署闭环。难形式化、反馈慢或依赖线下关系的领域，很难获得同样密度的反馈信号。

### Harness 把潜力变成系统行为

[[wiki/topics/AI Harness]] 决定模型能看到什么、能做什么、如何吸收失败、何时停止以及怎样接受验证。同一个模型放入不同 harness，会表现出明显不同的稳定性和任务上限。

### 使用经验产生双向复利

小任务带来有限收益，容易降低信任并减少投入；大任务成功则会促使用户继续建设工具、规则和验证环境，再把更大的任务交给系统。结果是能力差距从访问差异扩大为经验与基础设施差异。^[inferred]

## Change Mechanism

只要下面的速度关系成立，漏斗就会扩大：

> 前沿能力移动速度 > 产品扩散速度 > 组织改造速度 > 人类理解与制度适应速度。^[inferred]

与此同时，生成吞吐提高会把瓶颈推向 [[wiki/concepts/Verification Gap|验证]]、[[wiki/concepts/Attention as the Scarce Resource|注意力]]、[[wiki/concepts/Judgment Externalization|判定外化]] 和问责。系统越能做，越需要把“什么算完成、哪些风险不能接受、何时必须交还给人”写到模型之外。^[inferred]

## When to Use

这个框架适合：

- 比较不同人对 AI 能力的相反判断；
- 设计 AI 产品的用户分层与采用路径；
- 评估 Agent、工作流或组织的真实能力；
- 区分模型升级、系统工程和用户经验分别贡献了什么；
- 判断某个领域为何尚未出现代码领域那样的能力跃迁；
- 设计学习与评估任务，避免把工具访问优势误当成人的能力。

使用时应先问：

1. 比较双方接触的是同一模型和访问层吗？
2. 任务规模和执行时间相同吗？
3. 领域能提供什么外部真值信号？
4. 是否有工具、状态、权限、恢复和验证环境？
5. 用户是否真的拥有值得长期执行的问题？

## Boundary

- 漏斗描述的是经验分布，不是证明前沿系统每项能力主张都成立。
- 专业使用者也可能因成功选择偏差、高计算预算或强人工脚手架而高估通用性。^[inferred]
- 普通用户的弱体验不证明模型没有更强能力，但前沿演示也不证明这种能力已经便宜、可靠、普遍可用。
- 代码和数学的可验证性使其具有特殊地位，不能无条件外推到所有知识工作。
- 当产出超过人的理解速度时，成功率不再足以建立信任；还需要证据链、抽样、独立复现、风险分级和明确问责。^[inferred]

## Related

- [[wiki/sources/AI Capability Experience Funnel Source Guide]]
- [[wiki/concepts/Agent]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Verification Gap]]
- [[wiki/concepts/Judgment Externalization]]
- [[wiki/concepts/Understanding]]
- [[wiki/concepts/Attention as the Scarce Resource]]

