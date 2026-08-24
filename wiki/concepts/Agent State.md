---
title: Agent State
type: concept
status: draft
category: concepts
tags:
  - agents
  - state
  - memory
  - problem-solving
aliases:
  - Agent 状态
  - State as Sufficient Information
  - 状态作为充分信息
sources:
  - https://chatgpt.com/share/6a8bbde7-a668-83ee-a76f-60ff58322ccb
created: 2026-08-24T11:50:39+0800
updated: 2026-08-24T11:50:39+0800
summary: 状态是在某时刻为了决定"接下来会发生什么"而必须知道的全部相关信息；它是对历史的压缩、是对世界的充分抽象，而不是世界本身或全部信息。
provenance:
  extracted: 0.9
  inferred: 0.1
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-08-24
tier: supporting
relationships:
  - target: "[[wiki/concepts/Context as Working Memory]]"
    type: related_to
  - target: "[[wiki/concepts/Agentic Control Loop]]"
    type: related_to
  - target: "[[wiki/syntheses/Agent as Problem-Solving System]]"
    type: related_to
---

# Agent State

> **状态，是在某个时刻，描述一个系统为了决定"接下来会发生什么"而必须知道的全部相关信息。** 换句话说，状态 = 系统当前"处于什么情况"。

## What It Is

状态的核心是可预测性：知道当前状态就能决定接下来允许发生什么。红绿灯 `红灯 → 等待 → 绿灯`，形式化为状态转移函数：

$$
S_{t+1} = T(S_t, A_t)
$$

例如 `余额=100`，执行"消费 30"，得到 `余额=70`（S₀=100, A₀=消费30, S₁=70）。

## State Is Not "All Information"

状态不是系统拥有的全部信息，而是**决定系统未来行为所需要的当前信息**。象棋当前局面（棋盘 + 棋子位置 + 轮到谁 + 特殊规则状态）构成状态；"昨天和朋友下过什么棋"通常不属于当前状态。

**状态是对历史的一种压缩。** 控制论、强化学习、规划里常隐含：如果知道当前状态，就足以决定未来如何演化，而不必知道完整历史（当前棋盘 > 过去 100 步棋谱）。这解释了 Agent 为什么需要[[wiki/topics/AI Memory|记忆]]——历史很长时全塞进上下文很昂贵，Agent 会把历史压缩成当前状态（Bug 位于 auth.go / 已试方案 A 失败 / 方案 B 未试 / 测试仍失败）。**Memory 的一个重要作用就是帮助 Agent 从过去的信息恢复/构造当前状态。**

## State Is Not the World Itself

状态是一种**抽象**。现实世界（整个公司、所有员工、所有代码、所有数据库、所有历史……）不可能全部表示，于是针对某个问题选择"与当前问题相关的信息"构造 State：

> **状态不是世界本身，而是为了某个问题而对世界进行的充分抽象。**

## Three Layers: Environment State, Agent State, Context

Context、Memory、State 三个概念容易混，但处于不同层次：

```text
          Agent State
       ┌──────┴──────┐
   Environment     Internal State
      State            │
                    Context
                       │
                  LLM 可见部分
```

- **Environment State（环境状态）**：真实世界——auth.go 当前内容、数据库当前数据、Git 当前 commit、测试当前结果。
- **Agent State（内部状态）**：Agent 当前认为的东西——"Bug 大概率在 token expiration / 下一步该看 auth.go"。
- **[[wiki/concepts/Context as Working Memory|Context]]**：真正送给 LLM 的工作信息——用户任务 + 相关代码 + 错误日志 + 之前操作 + 当前结论。

闭环：

```text
Environment State
   │ Observation
   ▼
Agent State
   │ Context construction
   ▼
Context
   │ LLM reasoning
   ▼
Action
   ▼
Environment State'
```

## Why It Matters

最值得注意的一点：**Context 是"模型看到的东西"，State 是"系统实际上处于的东西"，二者可能完全不同。** 一个优秀的 Agent，本质上就是在努力让"自己对 State 的理解"尽可能接近"真实 State"。^[inferred]

这引出 Agent 的核心问题：**Agent 怎么知道自己对当前 State 的理解是对的？**——这自然通向 Observation、Evidence、Feedback 和 Evaluation，也是 [[wiki/concepts/Verification Loop|验证循环]]要处理的问题。

## Related

- [[wiki/concepts/Context as Working Memory]]
- [[wiki/concepts/Agentic Control Loop]]
- [[wiki/concepts/Agent]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/topics/AI Memory]]
- [[wiki/syntheses/Agent as Problem-Solving System]]
- [[wiki/sources/检索推理规划与Agent问题求解 Source Guide]]
