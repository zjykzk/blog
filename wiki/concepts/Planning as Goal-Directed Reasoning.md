---
title: Planning as Goal-Directed Reasoning
type: concept
status: draft
category: concepts
tags:
  - planning
  - reasoning
  - agents
  - problem-solving
aliases:
  - 规划作为面向目标的推理
  - 规划 vs 推理
  - Planning vs Reasoning
sources:
  - https://chatgpt.com/share/6a8bbde7-a668-83ee-a76f-60ff58322ccb
created: 2026-08-24T11:50:39+0800
updated: 2026-08-24T11:50:39+0800
summary: 规划是一种面向目标的推理：从目标倒推行动序列，在动作的顺序、依赖、代价与不确定性下，为跨越当前状态到目标状态推演出一条可接受的路径。
provenance:
  extracted: 0.9
  inferred: 0.1
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-08-24
tier: supporting
relationships:
  - target: "[[wiki/concepts/Retrieval vs Reasoning]]"
    type: related_to
  - target: "[[wiki/concepts/Agent State]]"
    type: uses
  - target: "[[wiki/syntheses/Agent as Problem-Solving System]]"
    type: related_to
---

# Planning as Goal-Directed Reasoning

规划通常是推理的结果之一，但**规划 ≠ 推理**：推理判断"应该怎么做"，规划把这个判断组织成"具体做什么、按什么顺序做"。

## What It Is

> 推理：`S → 判断`
> 规划：`S + Goal → Action Sequence`
> 行动：`S + Action → S'`

以"把服务 P99 从 500ms 降到 100ms"为例：先**推理**——P99=500ms → Trace 显示 70% 耗在 DB → 慢查询集中在 SQL A → SQL A 没用有效索引 → 判断主要瓶颈是 SQL A；再**规划**——1.分析执行计划 2.确认索引方案 3.创建索引 4.灰度流量 5.观察 P99 6.仍不达标则继续分析。

规划可以看成一种**面向行动的推理**，是推理这个总类下的一个分支：

```text
推理
├── 因果推理 —— 为什么发生？
├── 演绎推理 —— 根据规则能推出什么？
├── 归纳推理 —— 从多个案例总结规律
├── 诊断推理 —— 什么原因导致当前现象？
├── 预测推理 —— 接下来可能发生什么？
└── 规划推理 —— 为达到目标应采取什么行动？
```

## The Key Difference: Backward from the Goal

普通推理是**从事实推出结论**（`A>B, B>C ⇒ A>C`），在解释"世界是什么样"。规划是**从目标反过来寻找行动路径**，在寻找"世界应该如何变化"：

```text
目标：P99 < 100ms
   ↑ 需要
DB 延迟 < 50ms
   ↑ 需要
SQL A < 10ms
   ↑ 需要
添加索引
   ↑ 需要
先确认执行计划
```

规划本身其实**也是推理**，只是它推理的对象从"现在的事实"变成了"**可能的未来状态**"：`现在 → 假设执行 A → 未来状态 S₁ → 假设执行 B → 未来状态 S₂ → … → 目标`。因此 Planning = 对行动和未来状态进行推理。

## Why Planning Is Needed

> **规划存在，是因为目标状态和当前状态之间通常隔着多个动作，而且动作之间存在依赖、不确定性和代价。**

- **简单任务不需要规划**："2+3=?"一个动作就结束，此时 Reasoning ≈ Action。
- **长程依赖**：`A₁→…→A₆` 中 A₁ 的价值可能直到 A₆ 才体现（先读配置文件本身没解决问题，却可能引出"发现被关闭的 feature flag → 打开 → 测试通过"）。规划让系统能为了未来目标，执行当前暂时没有直接收益的动作。
- **动作依赖（Precondition）**：部署必须 编译→测试→构建镜像→推送→部署，因为 Deploy 需要 ImageExists=true、BuildImage 需要 BuildPassed=true。规划就是发现和组织这些前置条件。
- **资源与代价**：面对多个方案（重启：低成本/中风险；扩容：高成本/低风险；重构：极高成本/长期），目标不只是"找到能成功的方法"，而是**找到满足目标约束的较优路径**——`目标+约束+成本+风险+可用资源 → 最优/可接受路径`。这已接近经典的**搜索 / Optimization 问题**。

只靠"现想现做"（reactive：观察→推理→行动→观察）能应付简单任务，但复杂任务里**当前最好的动作可能取决于未来几步**（走迷宫：眼前更近的 A 是死路，B→C→D 才通出口），必须考虑当前动作对未来状态的影响。

## Relation to the Agent Loop

在 [[wiki/syntheses/Agent as Problem-Solving System|Agent 问题求解闭环]]里，规划位于推理和行动之间：一旦"行动"不是一步而是 `A→B→C→D`，就要插入 `推理 → 规划 → 行动`。它消费当前 [[wiki/concepts/Agent State|状态]]与目标，输出一条要作用于环境的动作序列。

> **Reasoning 是"认知"，Planning 是"面向目标的认知"，Action 是"把认知作用于世界"。** 这比把 Agent 理解成"LLM + Tools"要深一层。

## Related

- [[wiki/concepts/Retrieval vs Reasoning]]
- [[wiki/concepts/Agent State]]
- [[wiki/concepts/LLM Reasoning as In-Context Computation]]
- [[wiki/concepts/Agentic Control Loop]]
- [[wiki/syntheses/Agent as Problem-Solving System]]
- [[wiki/sources/检索推理规划与Agent问题求解 Source Guide]]
