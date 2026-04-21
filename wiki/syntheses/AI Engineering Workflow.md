---
title: AI Engineering Workflow
type: synthesis
status: growing
source_count: 5
updated: 2026-04-21
aliases:
  - AI 工作流
  - Agent workflow
tags:
  - synthesis
  - ai
  - agents
  - workflow
---

# AI Engineering Workflow

这页把当前 vault 里关于 Agent、LLM、工具设计、编码准则、需求映射的内容串成一条更完整的 AI 工程工作流。

## 1. Start from the right mental model of an agent

Agent 不是“会聊天的模型”，而是一个执行系统。它至少要处理三件事：

- 知道模型能做什么、不能做什么
- 管理上下文
- 调用工具

这意味着，真正的工程问题不是“模型聪不聪明”，而是：

- 任务能否被拆成可执行步骤
- 上下文是否被组织得足够清楚
- 工具调用是否让模型在正确边界内工作

参考：[[wiki/concepts/Agent]]

## 2. Separate model capability from workflow control

LLM 本身有模型内建能力，例如 extended thinking；但工程系统里还会引入另一层：外部流程控制。

例如：

- think tool：提醒模型停下来重新审视问题
- router：决定任务应该分派到哪里
- adapter：负责生成某种具体产物

因此一个重要区分是：

- 模型能力解决“它能想多深”
- 工作流与工具设计解决“它该怎么被用”

参考：[[wiki/concepts/LLM]]、[[wiki/concepts/Agent Tool]]

## 3. Keep tools narrow and decision units small

当前笔记里一个很重要的判断是：单步决策效果最好。

这会直接影响工具设计：

- 一个工具最好只负责一个清晰动作
- router 负责分派，不顺手生成产物
- adapter 负责产出，不顺手承担复杂调度
- think tool 负责提醒暂停，而不是替代结构化流程

这条原则的价值，在于降低 agent 一次调用里混入太多隐含任务的概率。

## 4. Constrain behavior with coding guidelines

即使工具设计正确，LLM 在编码时仍然容易出现默认假设、过度设计、顺手大改、没有验证闭环等问题。

所以需要一组行为约束：

- Think before coding
- Simplicity first
- Surgical changes
- Goal-driven execution

这些规则的作用，不是让模型更保守，而是让它更像一个能做局部、可验证、可交付修改的工程协作者。

参考：[[wiki/topics/Karpathy Guidelines]]

## 5. Normalize requirements before implementation

当输入是用户故事、PRD 或一句模糊需求时，不要直接开始写代码。

中间应先经过 requirement normalization，把输入拆成：

- use case
- entry
- business rules
- domain objects
- data access
- external calls
- errors
- assumptions

然后再做架构映射：

- `api/` 放协议入口
- `service/` 放业务语义
- `infra/` 放技术实现
- `pkg/` 放无业务语义的纯工具

这样才能让 AI 的输出从“会写代码”上升到“能稳定放对地方”。

参考：[[wiki/topics/Requirement to Architecture Mapping]]

## 6. End-to-end workflow

把上面几层连起来，可以形成一条更完整的 AI 工程链路：

1. 先明确 agent 视角下的任务边界
2. 区分模型能力和外部流程控制
3. 把工具做窄，把决策单元做小
4. 用 coding guidelines 约束默认行为
5. 先归一化需求，再决定实现分层
6. 最后进入实现与验证

## Why this synthesis matters

如果没有这条综合链路，AI 工程容易只剩下局部技巧：

- 只谈 prompt，不谈工作流
- 只谈模型能力，不谈工具设计
- 只谈写代码，不谈需求归一化
- 只谈产出速度，不谈验证闭环

把这些内容串起来后，AI 才更像一个可设计、可约束、可复用的工程系统。

## Upstream concepts

- [[wiki/concepts/Agent]]
- [[wiki/concepts/Agent Tool]]
- [[wiki/concepts/LLM]]

## Upstream topics

- [[wiki/topics/Karpathy Guidelines]]
- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/Tool Routing]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/AI Harness]]

## Navigation

- [[wiki/maps/AI Map]]
