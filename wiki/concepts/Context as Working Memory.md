---
title: Context as Working Memory
type: concept
status: draft
category: concepts
tags:
  - agents
  - context
  - memory
  - llm
aliases:
  - 上下文作为工作记忆
  - Context vs Memory
  - 上下文 vs 记忆
sources:
  - https://chatgpt.com/share/6a8bbde7-a668-83ee-a76f-60ff58322ccb
created: 2026-08-24T11:50:39+0800
updated: 2026-08-24T11:50:39+0800
summary: 上下文是 Agent 的工作记忆载体（当前正在被模型使用的信息状态），记忆是更广义的信息持久化机制；上下文承担记忆功能但不等于记忆。
provenance:
  extracted: 0.9
  inferred: 0.1
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-08-24
tier: supporting
relationships:
  - target: "[[wiki/concepts/Agent State]]"
    type: related_to
  - target: "[[wiki/concepts/LLM Reasoning as In-Context Computation]]"
    type: related_to
  - target: "[[wiki/topics/AI Memory]]"
    type: related_to
---

# Context as Working Memory

可以说"上下文承担了记忆的功能"，但严格来说**上下文不等于记忆**。

> **Memory 是"保存信息的能力/机制"；Context 是"当前正在被模型使用的信息状态"。**

## Why Context Looks Like Memory

Agent 在当前任务中，可以通过上下文"记住"之前发生/发现/做了什么、结果如何、现在基于什么继续。这些信息进入 context——用户任务、已读代码、已发现问题、已执行操作、测试结果、中间结论。所以 **Context 可以充当 Agent 的工作记忆（working memory）**。

## But Memory Is Broader

```text
                 Memory  "系统保存的信息"
        ┌──────────┴──────────┐
   短期/工作记忆            长期记忆
     Context              Memory Store
   当前任务可见          当前任务之外仍保存
```

- **Context**：「刚才测试失败，错误在 `foo.go:123`」——任务结束后可能就消失。
- **长期记忆**：「这个项目的测试通常需要先启动 Redis」——下次做完全不同的任务时仍可检索。

人脑类比：长期记忆 → 提取当前需要的信息 → 工作记忆 → 当前思考 → 行动。Agent 同理：

```text
Long-term Memory → Retrieval → Context → Reasoning → Action → Observation → Context 更新
```

Agent 做了 100 个动作时，不可能永远把全部历史塞进 Context，所以需要 `历史事件 → 压缩/总结 → 长期记忆 → 需要时检索 → 重新进入 Context`。这与 [[wiki/topics/Context Management|上下文管理]]和 [[wiki/topics/AI Memory|AI 记忆]]处理的是同一压力。

## Context as a "Temporary Program"

System Prompt + 任务 + 历史对话 + 工具描述 + 代码 + 检索结果 + 之前执行结果，组合起来形成**当前 Agent 的临时工作环境**：

```text
Context = 知识(Knowledge) + 规则(Rules) + 状态(State)
          + 历史(History) + 证据(Evidence)
              ↓
             LLM
              ↓
        当前决策 / 推理
```

所以 Agent 的上下文不是简单的"聊天记录"，它同时承担：工作记忆、临时知识库、任务状态、操作规则、历史经验、中间推理结果。这也是它作为 [[wiki/concepts/LLM Reasoning as In-Context Computation|上下文内计算]]载体的原因——[[wiki/concepts/LLM Reasoning as In-Context Computation|in-context learning]]从上下文构造临时策略，而推理是在这个工作记忆上持续进行的计算。

## The Three-Way Distinction

最准确的说法不是 `Context = Memory`，而是：

> **Context 是 Agent 的工作记忆载体；Memory 是更广义的信息持久化机制。**

再往前一步会碰到第三个概念——[[wiki/concepts/Agent State|State]]。三者处于不同层次：**Memory** 保存过去信息，**Context** 是当前交给模型处理的信息，**State** 是系统实际处于的情况。Context 是"模型看到的东西"，State 是"系统实际上处于的东西"，二者可能完全不同。^[inferred]

## Related

- [[wiki/concepts/Agent State]]
- [[wiki/concepts/LLM Reasoning as In-Context Computation]]
- [[wiki/concepts/Retrieval vs Reasoning]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Memory]]
- [[wiki/syntheses/Agent as Problem-Solving System]]
- [[wiki/sources/检索推理规划与Agent问题求解 Source Guide]]
