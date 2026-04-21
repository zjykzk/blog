---
title: Tool Routing
type: topic
status: seed
source_count: 3
updated: 2026-04-21
aliases:
  - tool routing
  - router and adapter
tags:
  - ai
  - agents
  - tools
---

# Tool Routing

当前笔记里关于 router / adapter 的判断，可以进一步抽成一个独立主题：工具路由不是附属细节，而是 agent 系统的核心结构设计。

## Core idea

- router：负责分派任务
- adapter：负责生成某种具体产物
- 单步决策效果最好

## Why it matters

如果分派、产出、流程控制混在一起，agent 的一次调用就会承担过多隐含任务，质量会快速下降。

所以更稳的做法是：

- 让 router 只做路径判断
- 让 adapter 只做窄职责产出
- 让每一步都尽可能成为单步决策

## Upstream concepts

- [[wiki/concepts/Agent Tool]]
- [[wiki/concepts/LLM]]
- [[wiki/concepts/Agent]]

## Peer topics

- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/AI Skills Workflow]]

## Downstream synthesis

- [[wiki/syntheses/AI Engineering Workflow]]

## Source notes

- [[pages/llm]]
