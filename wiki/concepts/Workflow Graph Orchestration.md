---
title: Workflow Graph Orchestration
type: concept
status: seed
summary: Workflow Graph Orchestration models agent work as explicit state-machine or graph traversal so control, persistence, guard nodes, and recovery stay inspectable.
category: concepts
sources:
  - https://arxiv.org/abs/2601.12560v1
created: 2026-05-13T10:37:07+08:00
updated: 2026-05-13T10:37:07+08:00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: "2026-05-13"
provenance:
  extracted: 0.78
  inferred: 0.20
  ambiguous: 0.02
aliases:
  - graph based orchestration
  - flow engineering
  - workflow graphs
tags:
  - agents
  - orchestration
  - workflow
---
# Workflow Graph Orchestration

Workflow Graph Orchestration 是把 agent 执行建模为显式 workflow graph 或 state machine 的架构模式。节点可以是 LLM 调用、工具调用、审批点、验证点或状态更新；边定义哪些转移被允许。

论文把这种模式称为从 open-ended multi-agent chat loop 转向 flow engineering 的行业变化：开发者设计控制结构，LLM 在局部节点内做推理、参数化工具调用和恢复。

典型收益包括：

- typed state 和 checkpoint 让长任务可恢复
- guard nodes 和 approval steps 让高风险动作回到权限边界
- workflow boundary 降低 runaway loop 的动作空间
- 显式 graph 让 debug、observability 和 evaluation 更容易落地

## Relation to Harness

Workflow graph 不是 multi-agent 的装饰，而是 [[wiki/topics/AI Harness]] 的一种控制形态。它把“agent 下一步做什么”从完全交给模型，改成由外部结构限定可走路径，再让模型在路径内部处理局部不确定性。^[inferred]

这也解释了为什么 [[wiki/syntheses/Agent System Design Space]] 中的 delegation、isolation、verification、recovery 应被放在一起看：它们都需要一个能记录状态、限定转移、接收反馈的控制层。

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/concepts/Agentic Control Loop]]
- [[wiki/concepts/Agent Evaluation CLASSic Framework]]
- [[wiki/sources/Agentic Artificial Intelligence Paper Source Guide]]
