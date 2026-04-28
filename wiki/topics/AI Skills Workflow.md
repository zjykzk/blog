---
title: AI Skills Workflow
type: topic
status: seed
source_count: 3
updated: 2026-04-22
aliases:
  - skills workflow
  - AI skills
tags:
  - ai
  - skills
  - workflow
---

# AI Skills Workflow

当前 source notes 里已经出现了一个很清楚的 workflow 雏形：

- 任务拆解要足够小
- 先对齐需求和现有代码口径，再做设计
- 写 skill 时，可以先和 AI 讨论出解决方案
- 再让 AI 把方案整理成可复用的方法论
- 最后再输出成 skill

## Why it matters

这说明 skill 不是“把 prompt 存起来”，而是把一次有效协作抽成稳定工作流。

## Practical pattern

1. 先把任务拆小
2. 对齐需求与现有实现约束
3. 和 AI 讨论方案
4. 把方案压缩成方法论
5. 再固化成 skill

这里还有一个容易被忽略的点：workflow 的价值不只是把步骤写出来，而是在构造一个更容易产生稳定 reasoning 的执行顺序。

也就是说，skill / workflow 不是单纯的 prompt 展开器，而是在安排：

- 哪些信息先进入上下文
- 哪些判断先做
- 哪些动作要被隔离出去
- 哪些中间结果要被压缩后再回流

## Reasoning implication

如果把 reasoning 看成 latent-state trajectory 的形成，那么 workflow 设计的意义就不只是“可复用”，而是“可稳定触发”。

同样一组能力：

- 顺序不同
- 边界不同
- 压缩点不同
- 子任务隔离方式不同

最后形成的系统质量会明显不同。

所以 workflow 设计其实在回答一个更深的问题：我们是在怎样安排一个 agent 的思考条件，而不只是安排它的执行步骤。

## Upstream topics

- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/topics/Karpathy Guidelines]]
- [[wiki/topics/Context Management]]

## Peer topics

- [[wiki/topics/Tool Routing]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Prompt Frequency]]

## Downstream synthesis

- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/syntheses/Agent System Design Space]]

## Navigation

- [[wiki/maps/AI Map]]

## Source notes

- `pages/项目___AI___skills.md`
- `journals/2026_04_01.md`
- [[wiki/sources/LLM Reasoning Is Latent, Not the Chain of Thought Source Guide]]
