---
title: Context Management
type: topic
status: seed
source_count: 2
updated: 2026-04-21
aliases:
  - 上下文管理
tags:
  - ai
  - agents
  - context
---

# Context Management

在当前 AI / Agent 知识簇里，上下文管理已经被明确视为 agent 的核心任务之一，而不是实现细节。

## Why it matters

如果上下文组织不好，会直接带来几个问题：

- 模型不知道当前任务的边界
- 有价值信息被淹没在杂音里
- 任务拆分和工具调用失去依据

所以很多 agent 质量问题，本质上不是模型能力不够，而是上下文没有被设计好。

## Practical role

在工作流里，上下文管理至少承担三件事：

- 保留完成任务所需的最小必要信息
- 让任务拆分和下一步决策有依据
- 让工具调用发生在正确边界内

## Upstream concepts

- [[wiki/concepts/Agent]]
- [[wiki/concepts/LLM]]

## Peer topics

- [[wiki/topics/Tool Routing]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/AI Skills Workflow]]

## Downstream synthesis

- [[wiki/syntheses/AI Engineering Workflow]]

## Source notes

- [[journals/2026_04_04]]
