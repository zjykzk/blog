---
title: Agentic Control Loop
type: concept
status: seed
summary: Agentic Control Loop models an LLM agent as perception, memory update, planning, action, execution feedback, and repeated state transition.
category: concepts
sources:
  - https://arxiv.org/abs/2601.12560v1
created: 2026-05-13T10:37:07+08:00
updated: 2026-05-13T10:37:07+08:00
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: "2026-05-13"
provenance:
  extracted: 0.82
  inferred: 0.16
  ambiguous: 0.02
aliases:
  - agentic control loop
  - POMDP agent loop
  - LLM agent control loop
tags:
  - agents
  - architecture
  - control-loop
---
# Agentic Control Loop

Agentic Control Loop 把 LLM agent 看成一个动态控制系统，而不是一次性的文本生成器。论文把 agent system 写成 `A = <S, O, M, T, π>`：环境状态空间、观察空间、内部记忆空间、动作或工具空间、策略。

这个循环包含几步：

- perception function 把不可完全可见的环境状态转换成部分观察
- memory update mechanism 把新观察、上一轮 reasoning trace 和执行反馈合入内部状态
- cognitive planning 生成 thought、plan 或更结构化的层级计划
- action policy 从工具/动作空间中选择动作
- environment transition 和 execution feedback 进入下一轮循环

这个模型的价值是把 [[wiki/concepts/Agent]] 从“会调用工具的模型”提升为“在部分可观察环境中持续感知、记忆、计划、行动并接收反馈的系统”。它也解释了为什么 [[wiki/topics/AI Harness]] 的边界设计重要：harness 决定哪些观察进入循环、哪些记忆可用、哪些动作允许执行、哪些反馈能回流。

## Design Consequence

如果 agent 是控制循环，那么失败也不只是“模型回答错了”。失败可能发生在观察、记忆、计划、动作选择、工具执行、反馈解释、停止条件中的任一环节。^[inferred]

这会把 debugging 从 prompt 修改推进到系统诊断：

- observation 是否足够、是否被噪音污染
- memory 是否写入了错误状态或检索了过期信息
- plan 是否和当前权限、时间、工具能力匹配
- action 是否经过 [[wiki/concepts/Agent Tool]] 的参数验证与权限检查
- feedback 是否能被 [[wiki/concepts/Verification Loop]] 转成下一轮可用信号

## Related

- [[wiki/concepts/Agent]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Agent Action Space]]
- [[wiki/sources/Agentic Artificial Intelligence Paper Source Guide]]
