---
title: Agent Tool
type: concept
status: seed
source_count: 2
updated: 2026-04-20
aliases:
  - agent tools
  - router and adapter
tags:
  - ai
  - agents
  - tools
---

# Agent Tool

当前在旧笔记中，`Agent tool` 这个文件名和其中的内容发生了错位：文件里实际保留的是 think tool 摘录，而 router / adapter 这段内容出现在旧的 `llm.md` 中。

先按“概念聚合页”的方式整理后，可以得到一个更稳定的抽象：

- `router` 用来分派任务
- `adapter` 用来生成某种具体产物，例如一段代码
- 单步决策的效果最好
- think tool 则更像一个提醒模型暂停并重新审视问题的流程工具

这意味着工具设计应尽量保持职责单一，让 agent 在一次调用中完成一个清晰动作，而不是把多阶段推理硬塞进单个工具。

## Note on source mismatch

当前 source note 存在文件名与内容的历史错位：

- `pages/Agent tool.md` 里保留的是 think tool 摘录
- `pages/llm.md` 里保留的是 router / adapter 摘录

第一轮先不重命名旧文件，只在 wiki 层完成语义归并。

## Navigation

- [[wiki/concepts/Agent]]
- [[wiki/maps/AI Map]]

## Source notes

- `pages/Agent tool.md`
- `pages/Agent.md`
