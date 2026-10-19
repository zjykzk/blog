---
title: Agent
type: concept
status: seed
category: concepts
summary: Agent is a control-loop system that uses perception, memory, planning, tools, and feedback to act in an environment over time.
sources:
  - https://arxiv.org/abs/2601.12560v1
  - https://x.com/karpathy/status/2109361546505966046
created: 2026-04-20
base_confidence: 0.68
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
source_count: 2
updated: 2026-10-17T23:51:28+0800
aliases:
  - agent
  - LLM agent
tags:
  - agents
  - concept
---
# Agent

Agent 不应该只被理解为“会聊天的大模型”或“模型 + 工具调用”。更稳的定义是：agent 是一个在环境中持续运行的控制循环，通过观察、记忆、规划、动作和反馈改变环境状态。

[[wiki/sources/Agentic Artificial Intelligence Paper Source Guide]] 给出一个形式化版本：LLM-based agent system 可以写成 `A = <S, O, M, T, π>`，其中 `S` 是环境状态空间，`O` 是观察空间，`M` 是内部记忆空间，`T` 是动作或工具空间，`π` 是策略。

## Core Tasks

从执行系统视角看，agent 至少需要处理几件事：

- 感知当前环境中的可见状态，而不是假定自己拥有完整世界
- 维护内部记忆或状态，而不是每轮从零开始
- 形成 reasoning trace、plan 或局部策略
- 通过 [[wiki/concepts/Agent Tool]] 或其他动作接口改变外部状态
- 接收执行反馈，并把反馈带回下一轮循环

这让 [[wiki/concepts/Agentic Control Loop]] 成为更基础的定义：tool use 只是 agent action space 的一部分，memory、feedback、permission、recovery 和 stop condition 同样决定系统性质。

## Boundary

Agent 与普通 LLM 调用的差别，不在于“是否输出了多段推理文本”，而在于它是否被放进一个能跨步骤保存状态、选择动作、执行动作并吸收反馈的运行系统。^[inferred]

因此，讨论 agent 能力时不应只问模型强不强，还要问 [[wiki/topics/AI Harness]] 如何组织上下文、工具、权限、记忆、验证和恢复。

## Capability Layers

[[wiki/concepts/AI Capability Experience Funnel]] 进一步要求区分三层：模型本身的潜在能力、模型进入工具与反馈环境后的系统能力，以及具体用户在自己的访问等级、任务跨度和工作流中实际体验到的能力。

同一模型在短问答、真实代码库和跨周长任务中暴露的不是同一组能力；同一任务在没有工具、状态与验证器的聊天界面中，也不能代表它在完整 Agent 系统中的上限。反过来，少数高预算内部系统的表现同样不能直接代表普通用户已经获得的能力。^[inferred]

## Upstream Concepts

- [[wiki/concepts/LLM]]
- [[wiki/concepts/Agentic Control Loop]]

## Downstream Topics

- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Memory]]
- [[wiki/topics/Tool Routing]]
- [[wiki/topics/AI Harness]]

## Cross-links

- [[wiki/concepts/Agent Tool]]
- [[wiki/concepts/Agent Action Space]]
- [[wiki/concepts/Agent State]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Agentic AI Architecture Taxonomy]]
- [[wiki/concepts/AI Capability Experience Funnel]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/syntheses/Agent as Problem-Solving System]]
- [[wiki/maps/AI Map]]

## Source Notes

- [[wiki/sources/Agentic Artificial Intelligence Paper Source Guide]]
- [[wiki/sources/AI Capability Experience Funnel Source Guide]]
- `pages/Agent.md`
- `journals/2026_04_04.md`
