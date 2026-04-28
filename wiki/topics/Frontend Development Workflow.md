---
title: Frontend Development Workflow
type: topic
status: draft
source_count: 1
updated: 2026-04-26
aliases:
  - 前端开发流程
  - frontend development process
  - frontend workflow
tags:
  - frontend
  - software-engineering
  - workflow
  - ux
---

# Frontend Development Workflow

Frontend development workflow 不是一条把设计稿翻译成页面的生产线，而是一套持续对齐用户任务、界面行为与系统行为的工作方法。

## Core idea

更稳的理解，不是把前端流程看成“需求 → UI → 开发 → 测试 → 上线”的交接顺序，而是把它看成一个连续回路：

- 从用户任务出发，而不是从页面切分出发
- 把任务翻译成交互行为、状态变化、反馈与错误恢复
- 在原型、实现、联调和发布前后不断验证这些行为是否成立
- 尽早暴露并修正用户意图、界面表现与系统行为之间的失配

从这个角度看，前端流程的目标不是单纯更快出页面，而是更早发现做错了什么、为什么错、错在哪里最先对用户显形。

## Start from task flow, not screen flow

前端流程的起点，不应是“要做几个页面、拆几个组件”，而应是“用户试图完成什么任务”。

这意味着更重要的不是先切 screen，而是先说清：

- 用户是谁
- 想完成什么
- 会经历哪些关键步骤
- 可能在哪些地方犹豫、误解、失败或回退

如果任务流一开始就没有被讲清楚，后续页面拆分、组件抽象与工程实现，很容易变成对错误问题的高效执行。

## Model interaction and state explicitly

前端工作最难的部分，通常不在像素本身，而在行为与状态：

- 状态如何随时间演化
- 异步请求如何影响界面可见性
- 错误如何被感知与恢复
- 页面是否诚实反映系统当前状态
- 多个局部更新之间是否保持一致

这说明在 `User Stories` 和 `Requirement to Architecture Mapping` 之间，还需要一个经常被省略的中间层：**交互语义与状态语义**。

很多所谓“体验 vs 工程”的冲突，其实是因为这层语义长期隐含存在，直到实现阶段才以返工、例外分支和一致性问题的形式爆出来。

## Build validation into the workflow

前端流程不应该把验证只留在末端。真正有效的做法，是在不同成本层级上，尽早发现不同类型的问题：

- 原型 / 任务演练：看用户是否理解路径与反馈
- 实现阶段：看状态建模与交互语义是否自洽
- 联调阶段：看界面行为与系统行为是否一致
- 发布后观察：看真实使用是否暴露出新的断裂

这也重新定义了“快”的意义。快不是更快堆出页面，而是更快让问题显形、更快确认假设是否成立、更快把高成本返工前移成低成本修正。

## Treat frontend as mismatch detection

前端之所以在流程里独特，不只是因为它负责界面，而是因为它经常最早暴露系统在哪里对用户失真。

用户任务、界面反馈与系统状态一旦失配，前端通常是最先出现症状的地方：

- 用户以为会发生 A，界面暗示 B，系统实际执行 C
- 状态已经变化，但界面还在撒谎
- 技术上“能跑”，但用户根本看不懂接下来该做什么

因此，更有生产力的理解是：前端 workflow 的价值不只是交付页面，而是持续暴露并修正这些失配。成熟团队和普通团队的差别，也往往不在于谁更会堆视觉细节，而在于谁能把这种失配识别与纠偏变成默认机制，而不是靠个别人临场敏感。

## Peer topics

- [[wiki/topics/Modern Software Engineering]]
- [[wiki/topics/Spec-Driven Development]]
- [[wiki/topics/User Stories]]
- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/topics/Testing Strategy]]

## Downstream synthesis

- [[wiki/syntheses/From User Story to Architecture]]

## Navigation

- [[wiki/maps/CS Map]]
- [[wiki/index]]

## Source notes

- [[wiki/sources/Frontend Development Workflow Roundtable Source Guide]]
