---
title: Agent Knowledge Architecture
type: synthesis
status: draft
category: syntheses
tags: [agents, context, memory, harness, architecture]
aliases:
  - Agent 知识架构
  - Agent Knowledge Types
  - Agent 知识分类
sources:
  - conversation:2026-09-09
  - https://denis2054.github.io/Context-Engineering-for-Multi-Agent-Systems/media/three_tier_context_engines.html
  - wiki/concepts/Knowledge Types
created: 2026-09-09T21:39:46+0800
updated: 2026-10-11T17:53:08+08:00
summary: >-
  Agent 知识架构按决策作用区分事实、语义、情景、程序、因果、规范、目标、能力和元知识，再按时间尺度与约束强度决定其运行时落点。
provenance:
  extracted: 0.45
  inferred: 0.55
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-09-09
tier: supporting
relationships:
  - target: "[[wiki/concepts/Knowledge Types]]"
    type: derived_from
  - target: "[[wiki/topics/AI Harness]]"
    type: uses
  - target: "[[wiki/topics/Context Management]]"
    type: uses
  - target: "[[wiki/sources/The Tiers of Context Engines Source Guide]]"
    type: derived_from
---

# Agent Knowledge Architecture

Agent 知识架构不是一套穷尽所有知识的哲学分类，而是一套面向行动的工程模型：按知识在决策中的作用拆开存储、检索、约束和更新机制，使 Agent 知道世界怎样、应该怎样做、为什么这样做、允许做到哪里，以及何时不该相信自己。^[inferred]

## 事实与程序构成最小行动闭环

`factual knowledge + procedural knowledge` 之所以常被 Agent 架构单独强调，是因为它们构成从认识到行动的最小闭环：

```text
事实知识：当前世界是什么样
程序知识：在这种世界状态下怎样行动
```

例如，“订单金额为 800 元”是事实，“超过 500 元必须进入审批步骤”是程序。只有两者同时进入上下文，Agent 才能推出“这笔退款不能直接执行”。

程序知识不只是一段关于做法的文字。它真正可执行的部分可以称为**行动结构**：

```text
触发条件
→ 前置检查
→ 动作顺序
→ 条件分支
→ 权限边界
→ 停止与升级条件
→ 结果验证
```

因此，程序知识是“怎样做”的知识总类，行动结构是其中能够组织和约束一次实际执行的骨架。松散经验只有被外化为步骤、分支、权限和验证条件，才更适合被 Agent 稳定复用。^[inferred]

## 生产级 Agent 需要更完整的知识分工

事实与程序足以解释最小执行循环，却不足以覆盖高风险、长时运行和可审计 Agent 的全部决策条件。更实用的分类按知识的决策作用展开：^[inferred]

| 知识类型 | 回答的问题 | Agent 中的典型内容 | 更合适的运行时落点 |
|---|---|---|---|
| 事实知识 | 当前有哪些对象、属性、事件和证据？ | 订单状态、系统指标、政策条款 | 数据库、文档检索、事实 RAG |
| 语义知识 | 这些对象是什么，彼此如何关联？ | 领域术语、实体关系、状态含义 | Ontology、schema、知识图谱 |
| 情景知识 | 过去发生过什么？ | 历史会话、故障案例、处理结果 | 事件库、长期记忆、案例检索 |
| 程序知识 | 这件事应该怎样完成？ | SOP、Skill、Runbook、工作流 | Skill registry、流程引擎、程序 RAG |
| 因果知识 | 为什么发生，干预后会怎样？ | 故障机制、风险传播、动作后果 | 因果图、专家模型、仿真与实验 |
| 规范知识 | 什么允许、禁止或必须做？ | 权限、合规、审批、禁止条件 | Policy engine、权限系统、硬门禁 |
| 目标与偏好 | 什么结果更好，如何权衡？ | 成功标准、风险偏好、成本与时延目标 | 任务契约、优先级、目标函数 |
| 能力知识 | 系统能做什么，怎样调用？ | Tool/Agent schema、权限、成本、副作用 | Tool Registry、Agent Registry、MCP |
| 元知识 | 这些知识是否可靠、完整和新鲜？ | 来源、版本、置信度、冲突、未知项 | 元数据、评估器、引用与升级机制 |

这些类型不是互斥标签。“金额超过 500 元的退款必须由主管批准”同时包含阈值事实、角色语义、规范约束和审批程序。分类的目的不是把每句话塞进唯一盒子，而是识别它在一次决策中承担哪些作用。^[inferred]

## 状态不是普通的长期知识

Agent 还需要当前执行状态，例如“身份已验证”“审批正在等待”“退款接口尚未调用”和“重试次数为 2”。这类信息看似也是事实，但它具有任务隔离、即时变化和强一致性要求，不应与长期知识混进同一个普通 RAG。^[inferred]

```text
长期知识：跨任务可复用
情景记忆：过去具体发生过什么
当前状态：本次执行现在走到哪里
```

当前状态更适合由 [[wiki/concepts/Agent State|任务状态]]、数据库或工作区按任务 ID 管理；否则上一次任务中的“已审批”可能污染当前任务。

## 同一知识还要经过两个维度再分类

只按内容类型分类仍然不够。Agent 系统还需要同时判断知识的时间尺度和执行强度。^[inferred]

### 时间尺度

```text
稳定知识 → 版本化规则 → 历史事件 → 当前实时状态
```

同一句“退款期限为 7 天”可能是长期稳定定义，也可能只是某个版本的政策。系统必须保留生效时间、记录时间和被替代关系，避免旧规则作为“幽灵知识”继续参与决策。

### 执行强度

```text
供模型参考的资料
→ 必须引用的权威来源
→ 必须遵循的结构化流程
→ 模型不可绕过的硬约束
```

这条轴决定知识应该只是进入 prompt，还是进入确定性的系统控制。高风险权限、金额阈值和审批要求不应只写在文档里期待模型记住，而应落在 policy、schema、权限检查和执行门禁中。^[inferred]

## Context Engine 把知识编译成行动

Context Engine 的核心工作不是把所有知识放进一个向量数据库，而是为当前任务装配不同性质的上下文：^[inferred]

```text
目标与偏好
+ 当前状态
+ 事实与语义
+ 历史情景
+ 因果模型
+ 程序与行动结构
+ 工具能力
+ 规范约束
+ 来源和置信度
────────────────
候选计划 → 授权 → 执行 → 验证 → 状态更新
```

例如生产服务延迟升高时，事实层提供实时指标和最近发布，情景层召回相似事故，因果层提出可检验机制，程序层加载排障 Runbook，能力层声明可查询或回滚的工具，目标层规定恢复与一致性的权衡，规范层决定谁能批准回滚，元知识层提醒历史案例只是候选假设而非当前证据。

这也说明 [[wiki/topics/AI Harness]] 与知识架构的关系：知识层提供可参与决策的材料，harness 决定哪些材料何时加载、哪些规则必须执行、哪些动作需要授权，以及执行结果如何反馈成新状态和新记忆。^[inferred]

## 设计判断

为 Agent 设计知识系统时，可以依次追问：

1. 这份知识在决策中负责描述、解释、指导、限制、评价，还是校准？ ^[inferred]
2. 它是稳定知识、版本化规则、历史事件，还是当前任务状态？ ^[inferred]
3. 它只供参考，还是必须引用、必须执行或不可绕过？ ^[inferred]
4. 它的来源、所有者、生效时间、适用范围和失效条件是什么？ ^[inferred]
5. 它应该由语义检索找到，还是由 schema、状态机、权限和 policy 确定性地执行？ ^[inferred]

最终原则是：**不要按“都是文本”来组织 Agent 知识，而要按“它怎样改变决策与行动”来组织。** ^[inferred]

## Related

- [[wiki/concepts/Knowledge Types]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Memory]]
- [[wiki/concepts/Agent State]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Agent Tool]]
- [[wiki/concepts/Factual Memory]]
- [[wiki/concepts/Action Memory]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/The Tiers of Context Engines Source Guide]]
