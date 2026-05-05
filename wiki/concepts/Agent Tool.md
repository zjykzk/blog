---
title: Agent Tool
type: concept
status: seed
category: concepts
summary: Agent tools are schema-defined action surfaces that let an agent inspect, change, retrieve, or validate external state under harness control.
sources:
  - https://addyosmani.com/blog/agent-harness-engineering/
  - https://x.com/akshay_pachaar/status/2041146899319971922
created: 2026-04-20
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.76
  inferred: 0.24
  ambiguous: 0.0
source_count: 4
updated: 2026-05-05T15:10:00+08:00
aliases:
  - agent tools
  - router and adapter
tags:
  - ai
  - agents
  - tools
---

# Agent Tool

Agent tools are the action surface exposed by an [[wiki/topics/AI Harness]] to a model. They are usually represented as schemas: names, descriptions, parameters, permissions, execution behavior, and result formatting.

The older notes had a source mismatch: `pages/Agent tool.md` mainly preserved think-tool excerpts, while router / adapter notes appeared in `pages/llm.md`. This page now treats those as partial examples of the broader tool concept.

先按“概念聚合页”的方式整理后，可以得到一个更稳定的抽象：

- `router` 用来分派任务
- `adapter` 用来生成某种具体产物，例如一段代码
- 单步决策的效果最好
- think tool 则更像一个提醒模型暂停并重新审视问题的流程工具

这意味着工具设计应尽量保持职责单一，让 agent 在一次调用中完成一个清晰动作，而不是把多阶段推理硬塞进单个工具。

## Harness responsibilities

The tool layer is not only the list of available functions. A production harness also has to manage:

- tool registration and schema injection
- argument extraction and validation
- permission checks before execution
- sandboxed execution where needed
- result capture and formatting back into model-readable observations
- error reporting that lets the loop recover

This means tool design is simultaneously capability design and boundary design. A tool gives the model an action, while the harness decides how that action is represented, constrained, executed, and reported back.

## Tool scoping

The source's main design implication is that more tools are not automatically better. Large tool surfaces increase prompt overhead and can make action selection noisier.

A better default is to expose the smallest useful tool set for the current task, then retrieve or reveal additional tools only when the task demands them. This connects tool design directly to [[wiki/topics/Context Management]] and [[wiki/concepts/Context Information Density]].

Addy Osmani's harness-engineering article sharpens this into two operational rules:

- tool names, descriptions, and schemas are part of the prompt surface, so every unnecessary or overlapping tool competes for model attention
- MCP and external tool descriptions are trusted text that the model reads, so tool installation is also a prompt-trust decision

This means tool scoping is both a context-quality problem and a security boundary problem. ^[inferred]

## Note on source mismatch

当前 source note 存在文件名与内容的历史错位：

- `pages/Agent tool.md` 里保留的是 think tool 摘录
- `pages/llm.md` 里保留的是 router / adapter 摘录

第一轮先不重命名旧文件，只在 wiki 层完成语义归并。

## Navigation

- [[wiki/concepts/Agent]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/maps/AI Map]]

## Source notes

- `pages/Agent tool.md`
- `pages/Agent.md`
- [[wiki/sources/Agent Harness Anatomy Source Guide]]
- [[wiki/sources/Agent Harness Engineering Source Guide]]
