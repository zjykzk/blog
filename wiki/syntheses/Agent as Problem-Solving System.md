---
title: Agent as Problem-Solving System
type: synthesis
status: draft
category: syntheses
tags:
  - synthesis
  - agents
  - reasoning
  - problem-solving
  - llm
aliases:
  - Agent 作为问题求解系统
  - 问题求解闭环
  - Problem-Solving Loop
sources:
  - https://chatgpt.com/share/6a8bbde7-a668-83ee-a76f-60ff58322ccb
created: 2026-08-24T11:50:39+0800
updated: 2026-08-24T11:50:39+0800
summary: 把大模型定位为问题求解系统里的推理引擎之一，用目标+状态+记忆+检索+推理+规划+行动+反馈的统一闭环，将问题求解重述为状态空间搜索与不确定性收窄。
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-08-24
tier: supporting
relationships:
  - target: "[[wiki/concepts/Agentic Control Loop]]"
    type: extends
  - target: "[[wiki/concepts/Retrieval vs Reasoning]]"
    type: uses
  - target: "[[wiki/concepts/Planning as Goal-Directed Reasoning]]"
    type: uses
  - target: "[[wiki/concepts/Agent State]]"
    type: uses
---

# Agent as Problem-Solving System

> **大模型本身更像一个"认知引擎"；Agent / 问题求解系统则是一个完整的"问题求解闭环"。大模型只是这个系统里的"Reasoning Engine"之一。**

这页把一次概念澄清对话（检索、推理、规划、上下文、记忆、状态）组装成一个统一模型，说明为什么真正的智能不是"会推理的大模型"，而是一个能检索世界、建立状态、推理、规划、行动、观察结果并不断修正自己的系统。

## The Unified Loop

真正完整的"智能"接近于：

> **目标 + 状态 + 记忆 + 检索 + 推理 + 规划 + 行动 + 反馈**
> Goal + State + Memory + Retrieval + Reasoning + Planning + Action + Feedback

```text
                    ┌─────────────┐
                    │    Goal     │  目标（驱动因素）
                    └──────┬──────┘
                           ↓
                    ┌─────────────┐
                    │    State    │  当前状态
                    └──────┬──────┘
                           ↓
        ┌──────────────────┴──────────────────┐
        ↓                                     ↓
   Retrieval 获取信息                    Reasoning 理解/推理
        └──────────────────┬──────────────────┘
                           ↓
                        Planning 规划
                           ↓
                         Action 行动
                           ↓
                     World changes 世界改变
                           ↓
                        Observe 观察
                           └──────────→ State
```

- **核心循环**：理解 → 检索 → 推理 → 规划 → 行动 → 观察 → 循环（不是线性流水线）。
- **支撑要素**：记忆 + 工具 + 环境——**记忆贯穿整个循环，工具连接 Agent 与环境**（工具不是目的，而是 Agent 作用于环境的接口）。
- **驱动因素**：目标——没有目标就不知道为什么做（"P99 是 500ms"只是状态，"把 P99 降到 100ms"才定义了问题）。

这一模型建立在各组成部分的独立澄清之上：[[wiki/concepts/Retrieval vs Reasoning|检索 vs 推理]]、[[wiki/concepts/Planning as Goal-Directed Reasoning|规划作为面向目标的推理]]、[[wiki/concepts/Agent State|状态作为充分信息]]、[[wiki/concepts/Context as Working Memory|上下文作为工作记忆]]、[[wiki/concepts/LLM Reasoning as In-Context Computation|LLM 推理作为上下文内计算]]。

## Problem Solving vs Answering Questions

理解 Agent 最重要的区别：

| | 普通问答 | 问题求解 |
|---|---|---|
| 结构 | `问题 → 答案` | `目标 → 状态 → 行动 → 新状态 → …… → 目标达成` |
| 例子 | "Redis 为什么快" → 一段解释，结束 | "我的 Redis 延迟为什么突然升高" → 读监控→查慢命令→看流量→定位根因→调容量→再观察→解决 |
| 主要任务 | 生成一个好的答案 | **改变世界状态**，使世界从当前状态到达目标状态 |

同理 Chatbot（`Input → LLM → Output`）与 Agent（带 Observe 回环的 `Goal → Reason → Plan → Act`）的差别："帮我把这个 Bug 修掉"——Chatbot 给一段修复代码；Agent 读代码→理解架构→定位→改→跑测试→失败→分析→再改→通过→完成。后者才是问题求解系统。

## Problem Solving as State-Space Search

`S0=当前问题状态`，系统可采取不同动作（查库/看日志/看监控/改配置/重部署），每个动作产生新状态，最终寻找一条路径：

```text
S0 → S3 → S7 → S12 → Goal
```

> **问题求解，本质上可以看成在状态空间中寻找一条从"当前状态"到"目标状态"的路径。**

## Problem Solving as Uncertainty Reduction

这是最值得理解的一层。"服务延迟为什么升高"一开始有 A(DB)/B(Redis)/C(网络)/D(CPU)/E(GC)/F(下游) 六种可能，处于高不确定状态。检索 CPU 正常排除 D，GC 正常排除 E，Trace 显示 80% 耗在 DB → A↑↑，继续调查发现某 SQL 延迟异常 → 索引缺失 → Root Cause。问题空间逐步收窄：

```text
████████████████████  →  ██████████  →  ████  →  █  →  Root Cause
```

> **问题求解系统的一个核心功能，就是通过观察、检索、推理和行动，不断缩小可能状态空间。**

## The Role of Each Piece

- **检索给推理提供世界状态**——模型自身知识有限且可能过时，`LLM → 提出信息需求 → 检索(日志/监控/Trace/DB/代码/配置) → 返回证据 → LLM 推理`。
- **行动改变世界**——很多问题不能只靠观察解决（磁盘快满：清理旧日志 → 95%→72%），于是从"感知→思考"变成"感知→思考→行动→感知→思考→…"。
- **记忆提供时间历史**——环境告诉 Agent"现在世界是什么样"，记忆告诉 Agent"过去发生过什么"，从而不重复失败（A 失败 → 尝试 B，而非反复试 A）。
- **状态是历史的压缩**——Agent 努力让"自己对 State 的理解"尽可能接近"真实 State"，这引出 Observation、Evidence、Feedback、Evaluation。

一句分界线：**检索是在扩大系统所知道的世界；推理是在已有世界模型上计算；行动是在现实世界中改变状态。**

## Relation to Existing Pages

- 与 [[wiki/concepts/Agentic Control Loop]] 同构：那页给出 `A = <S, O, M, T, π>` 的形式化 POMDP 视角，本页从"问题求解 / 认知引擎"视角把同一循环重述为目标驱动的状态空间搜索。二者互为印证。
- 与 [[wiki/concepts/Agent]] 一致：agent 不是"会聊天的大模型"或"模型 + 工具调用"，而是持续运行、跨步骤保存状态的控制系统。
- 与 [[wiki/syntheses/Agent System Design Space]] 互补：设计空间比较架构维度，本页给出"为什么需要这些维度"的认知论证。

## Related

- [[wiki/concepts/Agent]]
- [[wiki/concepts/Agentic Control Loop]]
- [[wiki/concepts/Retrieval vs Reasoning]]
- [[wiki/concepts/Planning as Goal-Directed Reasoning]]
- [[wiki/concepts/Agent State]]
- [[wiki/concepts/Context as Working Memory]]
- [[wiki/concepts/LLM Reasoning as In-Context Computation]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/检索推理规划与Agent问题求解 Source Guide]]
