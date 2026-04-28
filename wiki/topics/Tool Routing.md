---
title: Tool Routing
type: topic
status: growing
source_count: 4
updated: 2026-04-22
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

但随着 agent 开始拥有真实工具能力，还需要再补一个区分：routing 不等于 authorization。

也就是说，系统里至少存在两类不同判断：

- 该把当前任务或子任务路由到哪个工具
- 这个动作在当前策略和权限边界内是否允许发生

前者解决 capability match，后者解决 permission match。

如果这两层被混在一起，系统就容易把“模型选对了工具”误当成“这个动作应该被执行”。

## Routing boundary

从这个角度看，tool routing 的边界应该被收得更明确：

- routing 负责选择下一步能力路径
- authorization gate 负责决定该路径是否可以真正落地
- adapter 负责把被允许的动作翻译成具体执行形态

一个成熟的 agent system，通常不是让某个单一组件同时承担这三层职责，而是把它们分开，使错误更容易定位，边界更容易审计。

## Upstream concepts

- [[wiki/concepts/Agent Tool]]
- [[wiki/concepts/LLM]]
- [[wiki/concepts/Agent]]

## Peer topics

- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/AI Skills Workflow]]

## Design implication

这也意味着，tool routing 不该只被理解为“模型会不会选工具”的 prompt 技巧，而应被理解为 agent architecture 里的一个独立层。

当系统规模变大时，至少要分别回答：

- 哪个工具或能力最适合当前问题
- 哪些动作必须先过策略检查
- 哪些高风险动作需要升级为人类确认
- 被允许的动作如何稳定映射到具体执行接口

因此好的 routing 设计，重点不只是提高命中率，还在于让 capability selection、policy enforcement 和 execution translation 之间的边界保持清晰。

## Downstream synthesis

- [[wiki/syntheses/AI Engineering Workflow]]

## Source notes

- `pages/llm.md`
- [[wiki/sources/Before the Tool Call Source Guide]]
