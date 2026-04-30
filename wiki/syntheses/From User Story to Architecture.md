---
title: From User Story to Architecture
type: synthesis
status: growing
source_count: 3
updated: 2026-05-01
aliases:
  - 从用户故事到架构
tags:
  - synthesis
  - requirements
  - architecture
  - software-engineering
---

# From User Story to Architecture

这页综合的不是单一技巧，而是一条完整路径：需求如何从业务表达，一路变成可以实现、可以验证、可以维护的架构决策。

## Step 1: Start with user value

好的起点不是技术设计，而是用户故事：

- 谁要这个能力
- 想做什么
- 为什么值得做

如果这一层不清楚，后面的架构映射往往只是把模糊问题翻译成模糊代码。

参考：[[wiki/topics/User Stories]]

## Step 2: Normalize before designing

在开始分层之前，先把输入归一化成稳定结构：

- use case
- entry
- input / output
- business rules
- domain objects
- data access
- external calls
- errors
- assumptions

这样做的价值，是把“讨论需求”和“讨论实现”之间插入一层中间表示，减少跳步设计。

参考：[[wiki/topics/Requirement to Architecture Mapping]]

## Step 2.5: Produce intermediate artifacts

归一化不是抽象练习。它的价值在于每一步都产出一个可以检查的中间结果：

```text
业务场景
  -> 需求说明、约束清单

领域建模
  -> 领域词表、业务规则表、权限规则表

用例定义
  -> 触发者、输入、输出、主流程、异常流程

职责划分
  -> 核心逻辑、外围设施、模块边界

运行设计
  -> 数据流、状态机、接口调用链

失败设计
  -> 错误码、重试策略、幂等策略

代码设计
  -> 目录结构、类型定义、接口定义、函数职责
```

这一步防止需求直接坠落成代码。工程师要让每个中间结果都能被讨论、推翻、修正，然后再进入下一层。

## Step 3: Map decisions to layers

归一化之后，再判断每一条信息应该落在哪层：

- 接请求、对外协议、错误码 → `api/`
- 业务规则、状态流转、领域对象 → `service/`
- 外部能力接口定义 → `service/` 内接口
- 技术实现 → `infra/`
- 纯技术工具 → `pkg/`

这一步的本质不是目录摆放，而是防止业务语义和技术实现混在一起。

## Step 4: Verify through testing strategy

如果映射完以后没有验证路径，这套结构仍然是纸上设计。

因此需要把测试策略一起考虑：

- 用 Test Quadrants 检查覆盖范围是否完整
- 用 Test Pyramid 决定自动化测试投入比例

也就是说，架构不是“画完图”就结束，而是要能进入验证闭环。

参考：[[wiki/topics/Testing Strategy]]

## Why this synthesis matters

这三者连起来，才形成一条真正能复用的方法链：

- 用户故事回答“为什么做”
- 架构映射回答“怎么分层落地”
- 测试策略回答“怎么验证它真的成立”

缺任何一段，工程都会失衡：

- 只有用户故事，没有架构映射 → 难以稳定落地
- 只有架构映射，没有用户价值 → 容易做成形式主义
- 只有设计，没有验证 → 架构无法闭环

## Upstream topics

- [[wiki/topics/User Stories]]
- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/topics/Modern Software Engineering]]

## Navigation

- [[wiki/maps/CS Map]]
- [[wiki/index]]
