---
title: Agent System Design Space
type: synthesis
status: seed
source_count: 1
updated: 2026-04-23
aliases:
  - Agent architecture design space
  - AI agent system design space
tags:
  - synthesis
  - ai
  - agents
  - architecture
---

# Agent System Design Space

这页把 `AI Harness`、`Context Management`、`AI Skills Workflow` 串起来，不把 agent system 看成固定架构，而把它看成一个 design-space 问题：不同系统面对的是相似约束，但会因为价值排序和部署环境不同，长出不同答案。

## 1. Start from values, not mechanisms

很多关于 agent 的讨论，容易从机制出发：有没有 tool use、有没有 memory、有没有 multi-agent、有没有 workflow。

但如果只从机制看，容易把实现误当成问题本身。

更稳的起点是先问：这个系统到底想保护和放大什么。

从当前材料往上抽，可以先看到几类更基础的目标：

- 人类是否还保有关键决策权
- 系统是否在安全边界内工作
- 执行是否可靠、可恢复、可连续
- 外部接口是否真的在放大能力，而不是只在堆功能
- 上下文受限时，系统是否还能维持有效工作

机制是答案，价值排序才是题目。

## 2. The core loop is not the whole system

表面上看，很多 agent system 都可以被压成一个很简单的 loop：读上下文、调用模型、决定动作、执行动作、再继续下一轮。

但真正决定系统性质的，往往不是这个 loop 本身，而是 loop 外围的运行秩序。

也就是说：

- loop 决定系统怎样继续运转
- harness 决定系统在什么边界内运转

因此两个系统即使共享相似的 loop，只要外围的权限、压缩、隔离、恢复机制不同，最后的系统性质也会明显不同。

## 3. The main design surfaces

如果把 agent 当成一个系统而不是一个提示词技巧，那么至少有几块设计面必须被单独看待。

### Permission and approval boundary

系统需要决定：

- 哪些动作可以自动执行
- 哪些动作必须回到人类确认
- 哪些动作要在更严格的边界里运行

这不是一个附属开关，而是 agent 是否可控的核心结构。

### Context compression and reconstruction

上下文永远不是无限的，所以系统要决定：

- 什么该被保留
- 什么该被压缩
- 什么该在下一轮被恢复出来

因此 context management 不是 token 工程小技巧，而是 system design 的核心组件。

### Extension surfaces

skill、hook、plugin、MCP 这些看起来分散的接口，实际上都在回答同一个问题：系统如何扩展自己的能力边界。

重点不只是“能不能接更多东西”，而是这些扩展是否让系统更稳定、更清楚、更可复用。

### Delegation and isolation

当任务变复杂时，系统是否能把局部问题隔离出去单独处理，会直接影响整体稳定性。

委派不是为了制造 multi-agent 的表面热闹，而是为了：

- 把任务边界切清楚
- 降低上下文污染
- 控制执行环境
- 让结果能够回流而不是把噪音一起带回来

### Persistence and recovery

一个 agent system 不能只考虑当前回合，还要考虑：

- 状态如何留下来
- 中断之后如何恢复
- 历史如何继续成为后续动作的依据

如果没有这一层，很多“会做事”的 agent 只能停留在短时演示，而很难变成连续工作的系统。

## 4. Why environment changes the architecture

同一类 agent 设计问题，在不同环境里并不会得到同一个最优解。

例如：

- 本地 CLI agent 更强调人机协同、权限确认和本地工具边界
- 托管式 agent 更可能强调控制平面、租户隔离和统一扩展注册
- 企业内部系统更关心审计、权限收敛和可治理性
- 强沙箱 workflow 更关心隔离、恢复和可重复执行

所以 agent architecture 不是静态模板，而是环境约束下的解空间。

## 5. A practical evaluation lens for agent systems

如果不想被具体实现细节牵着走，可以用一组更稳定的问题来评估 agent system：

- 它在放大什么能力
- 它在约束什么风险
- 它把什么决策留给人
- 它如何处理上下文受限的问题
- 它是否有 verification / evaluation loop 来纠偏自身输出
- 它如何隔离复杂任务和执行环境
- 它如何记录状态，并在中断后恢复连续性

这样看，agent system 的差异不再只是 feature list 的差异，而是系统秩序设计的差异。

## Why this synthesis matters

如果没有这一层 synthesis，我们很容易把 agent 讨论切碎成很多局部话题：

- 只谈 loop，不谈外围秩序
- 只谈工具，不谈边界设计
- 只谈上下文，不谈恢复与连续性
- 只谈扩展能力，不谈人类决策权

把这些主题重新压到同一张图里之后，agent 才更像一个可比较、可设计、可解释的系统对象。

## Upstream topics

- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Skills Workflow]]

## Upstream source notes

- [[wiki/sources/Managed Agents Source Guide]]

## Navigation

- [[wiki/maps/AI Map]]
