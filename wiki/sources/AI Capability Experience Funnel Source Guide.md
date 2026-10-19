---
title: AI Capability Experience Funnel Source Guide
type: source
status: draft
category: sources
tags: [article, agents, llm, ai-coding, judgment]
aliases:
  - Karpathy AI capability funnel
  - AI 能力体验漏斗原帖
  - AI shared understanding gap
relationships:
  - target: "[[wiki/concepts/AI Capability Experience Funnel]]"
    type: related_to
  - target: "[[wiki/concepts/Agent]]"
    type: related_to
  - target: "[[wiki/topics/AI Harness]]"
    type: related_to
  - target: "[[wiki/concepts/Verification Gap]]"
    type: related_to
sources:
  - https://x.com/karpathy/status/2109361546505966046
  - conversation:2026-10-17
created: 2026-10-17T23:51:28+0800
updated: 2026-10-17T23:51:28+0800
summary: >-
  Karpathy 用四层人群漏斗解释为何公众、普通用户、专业用户与内部前沿使用者像活在不同 AI 现实中；任务跨度、领域可验证性与访问权限共同放大理解差距。
provenance:
  extracted: 0.55
  inferred: 0.40
  ambiguous: 0.05
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-17
tier: supporting
---

# AI Capability Experience Funnel Source Guide

> Source: Andrej Karpathy, [X post on the widening gap in shared understanding of LLM capability](https://x.com/karpathy/status/2109361546505966046)

## What It Covers

Karpathy 讨论的不是一个普通的“AI 很强”判断，而是人们为何会对 AI 能力形成彼此冲突、却各自符合亲身经验的认识。公众、免费聊天产品用户、在代码和数学中使用前沿模型的专业者，以及能接触内部前沿系统的少数人，实际观察到的是不同任务尺度、不同系统配置和不同能力边界。

帖子的核心命题是：**对 LLM 能力的共享理解正在缩小，而不是自然趋同。** 大多数人看到的仍是偶尔犯傻的聊天机器人；少数专业者已经看到数周或数月的数字工作被 Agent 显著压缩；极少数内部使用者则声称看到远超公开产品的长程、多 Agent 系统。

## Population Funnel

Karpathy 用一组明确标为 “napkin math” 的粗略数字描绘漏斗。这些数字适合表达数量级，不应当作经过抽样验证的人口统计。

| 人群 | 粗略规模 | 直接经验 |
|---|---:|---|
| 几乎没有接触 LLM | 约 60 亿人，约 75% | AI 主要是新闻或他人描述中的抽象对象 |
| 免费产品的偶尔用户 | 约 10～20 亿人，约 20% | 更好的搜索、写作助手、会犯傻的聊天机器人，偶尔尝试订票等 Agent 功能 |
| 在数学和代码中专业使用前沿模型 | 约 2000 万人，约 0.2% | 建应用、复制或翻译应用、从二进制反编译应用，以及把部分数周或数月项目压缩到更短周期 |
| 接触内部前沿系统 | 约 5000 人，约 0.00006% | Karpathy 描述为数千 Agent 持续数周协作、机器速度的网络攻防、科学发现与前沿数学推进 |

帖子还用两个例子说明人类理解开始落后于机器产出：OpenAI-HF 事件仍需要持续“考古”，数学家可能需要很久才能消化 722 篇前沿数学手稿。这些例子表达的是审查吞吐压力，不足以单独证明相关系统已经稳定获得全面自主科研能力。^[ambiguous]

## Assumptions

### 能力随问题规模和时间跨度显现

一个只需一段话回答的问题几乎不会压到系统能力边界。要看到巨大杠杆，用户必须拥有一批真正关心、规模足够大、执行跨度足够长的问题。这个假设解释消费用户与专业用户为何会看到不同 AI。

### 能力分布是锯齿状的

AI 能力首先在数字化、可验证且经济价值高的领域形成尖峰。Karpathy 将其归因于在精心选择的环境组合上进行可验证奖励强化学习，而环境选择又受到潜在商业回报驱动。代码和数学因此比大量难验证、反馈缓慢或依赖线下互动的工作更容易率先跃迁。

### 访问权限决定可见前沿

免费层、付费层与内部层不是同一产品的轻微差异，而可能让用户接触不同模型、计算预算、Agent 编排规模与持续时间。对能力的判断因此同时包含了技术事实与制度化访问差异。^[inferred]

### 亲身经验比公开叙事更能更新判断

知道“AI 在进步”和亲眼看见自己数周的工作被压缩，不会产生同样的世界模型。认知差距首先是一种经验分层，其次才是信息分层。^[inferred]

### 内部系统是外部世界的预览

帖子把内部前沿能力视为外部产品未来可能获得的能力。这是论证中最强、也最难从外部核验的假设。系统是否能从少数高投入环境稳定扩散到一般组织，还取决于成本、权限、数据、可靠性、产品化和责任边界。^[ambiguous]

## Conceptual Structure

原帖明确提出三个漏斗驱动因素：

1. **Ambition / problem size / horizon**：问题是否足够大、足够难，执行时间是否足够长。
2. **Jaggedness / domain**：任务是否位于数字化、可验证、经济价值高的能力尖峰。
3. **Access**：用户接触免费、付费还是内部前沿系统。

讨论进一步可区分三层能力：

| 层 | 问题 |
|---|---|
| 模型能力 | 模型参数和训练本身潜在能完成什么？ |
| 系统能力 | 模型连上工具、上下文、记忆、权限、环境和验证器后能完成什么？ |
| 体验到的能力 | 某个用户在自己的任务、访问等级和工作流中实际看见什么？ |

因此，有效能力不宜归结为一个模型分数。它更接近：

> 体验到的 AI 能力 ≈ 模型 × 访问等级 × 任务跨度 × 领域可验证性 × 工作流成熟度 × 大问题储备。^[inferred]

这里的乘法不是可计算公式，而是在强调任何一项接近零，都可能让其余能力无法显现。^[inferred]

## Reasoning Flow

1. 人们对 AI 能力的判断正在越来越分裂。
2. 不同人接触到的产品层级、任务规模和领域不同，因此他们并未观察同一个对象。
3. 普通聊天问题无法暴露长程系统能力；代码和数学又因可验证性形成局部能力尖峰。
4. 免费、付费与内部访问进一步把这种差异制度化。
5. 于是同一时期会同时存在四种经验：AI 与我无关、AI 只是普通助手、AI 正在重写专业工作、AI 产出已经开始超过人类理解吞吐。
6. 只要前沿系统移动得比能力扩散、组织改造和社会理解更快，共享理解差距就会扩大。^[inferred]

论证的最后一步依赖内部观察者的可信度。帖子提供了能力方向和主观体验的高信号描述，但没有公开实验设计、成本、失败率、人工脚手架比例或可复现证据。^[ambiguous]

## Change Mechanisms

### 低使用均衡

> 小问题 → 提升有限 → 低信任 → 不投入环境和工作流 → 继续只问小问题。^[inferred]

偶尔使用者很容易从弱任务得到弱结果，再把结果归因于模型总体能力。因为缺少进一步投入，他们也很难获得推翻原判断的新经验。

### 高使用复利

> 大而真实的任务 → 投入工具、上下文和验证 → 得到明显结果 → 信任与操作能力提高 → 委托更长、更难的任务。^[inferred]

高使用者积累的不只是模型访问权，还包括问题分解、环境设计、失败恢复和结果判断经验。能力差距由此从访问差异变成经验复利。

### 可验证领域的产业反馈

> 可验证 → 可做强化学习 → 能力提升 → 商业价值显现 → 更多资金与算力 → 更好的训练和验证环境。^[inferred]

这条正反馈解释了为什么代码和数学会先形成尖峰，也说明不能直接把这些领域的进展平均外推到所有知识工作。

### 生成与理解的速度失配

当前沿系统能持续生成代码、证明、攻击路径或研究材料时，人的瓶颈会从“做不出来”迁移到理解、验证、选择、否决和承担后果。这与 [[wiki/concepts/Verification Gap]] 和 [[wiki/concepts/Attention as the Scarce Resource]] 描述的是同一组压力。^[inferred]

## Implications for Current Work

### Agent 化软件工程

代码正处于数字化、可执行验证和高经济价值的交叉点。要观察和利用前沿能力，应把任务设计成长程闭环：目标、计划、隔离执行、测试与静态检查、独立审查、证据化交付和失败恢复。模型的价值应以端到端交付时间、缺陷和恢复能力衡量，而不是代码生成量。^[inferred]

### 智能评估与学习能力判断

评价“AI 能力”时必须控制模型等级、工具权限、任务跨度和领域可验证性，否则会把访问优势误判为人的能力。评价人的能力则更应观察其能否建模、验证、纠正和迁移，而不只是能否得到一次正确答案。^[inferred]

### 多 Agent、Skills 与长程工作流

能力单位应当是模型、工具、状态、工件、编排和验证器组成的系统，而不是 Agent 数量。checkpoint、可发现工件、审计记录、恢复协议和最终质量门决定长任务能否把模型潜力转化成稳定产出。^[inferred]

### Wiki 与个人知识系统

知识系统可以为 Agent 提供“大问题蓄水池”、长期上下文和证据界面。但当机器生成速度超过人的阅读速度时，Wiki 的关键功能不再是保存更多内容，而是控制理解债务：区分证据、推断、争议、待验证判断和会迫使结论改变的条件。^[inferred]

### 家庭学习

学习场景必须反向理解效率：AI 可以快速生成练习与解释，但学习者的理解速度本身就是目标，不能被绕过。掌握仍需用无提示回忆、因果解释、边界辨析、陌生迁移和延迟复测来验证。^[inferred]

## Boundaries and Open Questions

- 人群规模来自作者的数量级估算，不是调查结果。
- “数千 Agent 协作数周”可能同时包含模型能力、计算规模、工具链、人类脚手架和组织投入，不能只归因于裸模型。
- 代码与数学是高可验证领域，其经验不能直接代表医疗、管理、教育、关系和制度工作。
- 内部前沿系统的失败率、成本、人工介入和成功选择偏差没有公开。
- 免费产品未来可能缩小访问差距，但任务设计、组织数字化和验证能力的差距仍可能保留。
- 当人类无法逐件理解机器产出时，什么样的抽样、形式验证、独立复现与问责结构足以建立信任？

## Related

- [[wiki/concepts/AI Capability Experience Funnel]]
- [[wiki/concepts/Agent]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Verification Gap]]
- [[wiki/concepts/Judgment Externalization]]
- [[wiki/concepts/Understanding]]
- [[wiki/concepts/Attention as the Scarce Resource]]
- [[wiki/sources/Coding Is Not Solved Source Guide]]

