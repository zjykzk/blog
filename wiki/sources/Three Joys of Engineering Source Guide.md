---
title: Three Joys of Engineering Source Guide
type: source
status: draft
category: sources
tags: [article, software-engineering, ai-coding, cognition, judgment]
aliases:
  - Making Knowing and Mattering Under AI Agents
  - AI Agent 时代的三种工程之乐
sources:
  - https://www.linkedin.com/posts/addyosmani_ai-programming-softwareengineering-activity-7514210769282994176-fOyn
  - conversation:2026-10-12
source_url: https://www.linkedin.com/posts/addyosmani_ai-programming-softwareengineering-activity-7514210769282994176-fOyn
source_id: linkedin.com/addyosmani/7514210769282994176
authors: [Addy Osmani]
published: 2026-10-09
created: 2026-10-12T23:14:28+0800
updated: 2026-10-12T23:14:28+0800
summary: >-
  Addy Osmani 用 making、knowing、mattering 拆解工程师面对 AI Agent 的解放感与失落感，并指出“选择答案”无法替代独立生成答案所维持的系统理解。
provenance:
  extracted: 0.66
  inferred: 0.30
  ambiguous: 0.04
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-12
tier: supporting
relationships:
  - target: "[[wiki/concepts/Engineering Work Three Joys]]"
    type: related_to
  - target: "[[wiki/concepts/Cognitive Debt]]"
    type: related_to
  - target: "[[wiki/concepts/Agent Loop Human Judgment Positions]]"
    type: related_to
  - target: "[[wiki/concepts/Agentic Engineering]]"
    type: related_to
---

# Three Joys of Engineering Source Guide

> 来源：[Addy Osmani 的 LinkedIn 帖子](https://www.linkedin.com/posts/addyosmani_ai-programming-softwareengineering-activity-7514210769282994176-fOyn)，2026-10-09。

## 来源边界

LinkedIn 对当前网络位置返回地区限制，正文由页面的公开元数据恢复。元数据包含完整主帖和评论数量，但不包含评论正文；本页只分析主帖，不把评论区观点归到作者名下。

原帖不是实证研究，而是一位长期使用 coding agents 的工程师对职业体验和能力变化的概念拆解。它适合提供诊断语言与风险假设，不足以单独证明工程师的技能、幸福感或就业结果会如何变化。^[inferred]

## 核心问题

为什么同样面对 AI Agent，一些工程师感到自己获得了一支全明星团队，另一些工程师却感到手艺正在死亡、工作变得空洞？

作者认为，“喜欢写代码”和“喜欢交付结果”的二分法过于粗糙。工程工作至少提供三种彼此交织的满足：

- **Making**：亲手塑造事物、获得即时反馈并进入心流；
- **Knowing**：拥有足够强的系统心理模型，以至于能预感故障和设计方向；
- **Mattering**：感到自己是系统依赖的专家，自己的判断与存在不可忽略。

工程师对 Agent 的反应不同，是因为 Agent 对这三种满足的影响并不相同，人们哀悼的也不是同一种损失。

## 概念结构

| 满足来源 | 满足的需要 | Agent 带来的变化 | 主要风险 |
|---|---|---|---|
| Making | 操作感、创造感、心流 | 从逐行塑造代码上移到塑造规格、系统和软件工厂 | 微观手艺感减少；系统级循环未必产生同样的心流 |
| Knowing | 内生心理模型、预判与解释能力 | 从独立生成方案转向识别和选择 Agent 给出的方案 | 熟悉感掩盖生成能力退化，形成 [[wiki/concepts/Cognitive Debt]] |
| Mattering | 专家身份、被需要感、责任感 | 从不可替代的实现者转向问题选择者、判断者和责任承担者 | 心理意义可以迁移，但组织地位和经济价值未必同步迁移 ^[ambiguous] |

这三项不是互斥人格类型，也不是工程工作的完备心理学分类。它们更像三种“心理收入”：同一工程师可以同时需要，只是权重和受损位置不同。^[inferred]

## 推理流程

1. 工程师对 Agent 出现彼此冲突的兴奋与失落。
2. “爱编码”和“爱交付”的二分法无法解释这些细微差异。
3. 把工程满足拆成 making、knowing、mattering 后，不同反应开始可解释。
4. Making 可以向更高抽象层迁移：工程师不再塑造每一行，而是塑造生产软件的系统。
5. Knowing 最容易无声退化：从候选方案中选择，与没有候选方案时独立构造，并不是同一种认知活动。
6. 如果工程师不再理解自己的代码库，就无法真正指导 Agent；控制关系会从“人指导 Agent”倒转为“Agent 提供人只能接受或拒绝的世界”。^[inferred]
7. Mattering 需要从“实现必须经过我”迁移到“由我决定问题、标准、品味与最终责任”。
8. 对旧工作方式的悲伤不等于适应失败，而是人在哀悼曾经承载身份与满足的东西。

## 变化机制

### 创造之乐向上迁移

```text
构思 → 编码 → 运行 → 观察 → 修改
                ↓
定义意图 → 设置约束 → Agent 执行 → 验证 → 修正系统
```

作者认为，只要新循环仍然足够快，工程师仍能在塑造系统或“软件工厂”时获得心流。这个判断依赖两个未展开的条件：人仍能感到结果与自己的选择有可见因果联系，并且等待、切换与审查没有打断反馈连续性。^[inferred]

### 理解力进入退化回路

```text
更多工作交给 Agent
→ 更少亲自构造、调试和回忆
→ 系统心理模型变弱
→ 更难判断 Agent 是否正确
→ 进一步依赖 Agent
```

原帖最关键的区分是：**recognition 不等于 generation**。从 Agent 的建议中挑选一个方案主要训练识别；在没有候选项时调出约束、构造结构并解释取舍，才训练生成。如果总在选择而不再生成，工程师可能仍觉得输出“看得懂”，却逐渐失去独立产生和反驳方案的能力。

### 重要之感重新定位

```text
代码生产成本下降
→ 实现者的稀缺性下降
→ 旧身份锚点动摇
→ 重要性转向问题选择、品味、验证、责任
```

这条路径提供的是职业意义的重建方式，而不是就业安全的证明。人的判断在工程系统中仍然必要，不自动意味着组织会给判断足够权力、时间、归属或经济回报。^[ambiguous]

## 可操作推论

- 对 Agent adoption 的诊断不应只问“效率提高了吗”，还要分别观察创造体验、系统理解和职业身份。^[inferred]
- 理解校准应偶尔采用“自由回答”而非“多项选择”：先由工程师预测设计、故障和约束，再查看 Agent 建议。^[inferred]
- 委托边界应保留一部分亲自解释、调试和构造的活动，使心理模型继续受到现实反馈。^[inferred]
- 工程师的责任不能只在最终审批时出现，而应保留在问题选择、任务切分、否决、验证标准和循环修正位置。^[inferred]
- 团队如果只奖励吞吐，不奖励理解、验证和责任，就会让个人很难把 mattering 从实现量迁移到判断质量。^[inferred]

## Open Questions

- 系统级编排能否为所有喜欢编码的人提供与手工实现相同的心流，还是只会为一部分人提供替代体验？
- 团队怎样测量“仍然看得懂，但已经想不出来”的早期认知债务？
- 哪些编码、调试和架构活动必须保留为人的生成性练习，哪些可以安全外包？
- 当组织按产出吞吐而不是判断质量奖励工程师时，mattering 的迁移怎样才能真实发生？
- 除 making、knowing、mattering 外，归属、服务用户、审美和学习是否还构成独立的工程满足来源？^[inferred]

## Related

- [[wiki/concepts/Engineering Work Three Joys]] — 从来源中抽出的稳定诊断框架。
- [[wiki/concepts/Cognitive Debt]] — 理解随委托扩大而退化的积累机制。
- [[wiki/concepts/Agent Loop Human Judgment Positions]] — 人在循环中仍需保留的判断与理解位置。
- [[wiki/concepts/Agentic Engineering]] — 人的工作从直接产出迁移到 harness、验证与判断配置。
- [[wiki/concepts/Attention as the Scarce Resource]] — 多 Agent 并行后人的注意力如何成为瓶颈。
- [[wiki/topics/Modern Software Engineering]] — 软件工程作为受现实反馈约束的问题求解活动。
- [[wiki/maps/AI Map]]
- [[wiki/maps/CS Map]]
