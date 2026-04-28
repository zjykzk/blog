---
title: Karpathy Guidelines
type: topic
status: growing
source_count: 2
updated: 2026-04-20
aliases:
  - karpathy-guidelines
tags:
  - ai
  - coding
  - guidelines
---

# Karpathy Guidelines

这组 guideline 的核心目的是降低 LLM 写代码时常见的失误，尤其是：默认假设、过度设计、顺手大改、以及缺少可验证目标。

## Core principles

### Think before coding

- 不要假设
- 不要隐藏困惑
- 有歧义时显式提出
- 有更简单方案时要说出来

### Simplicity first

- 只写解决问题所需的最小代码
- 不为单次使用抽象
- 不加用户没要的灵活性
- 不为不可能发生的场景加防御代码

### Surgical changes

- 只改必须改的地方
- 不顺手清理无关区域
- 跟随现有风格
- 只移除因本次修改导致的 orphan

### Goal-driven execution

- 先把任务变成可验证目标
- 修 bug 先写能复现的测试
- 重构前后都要能验证

## Why it matters

这些规则适合拿来约束 LLM 协作中的默认行为，让输出更像成熟工程师的局部、可验证修改，而不是泛化式“重写一遍”。

## Navigation

- [[wiki/maps/AI Map]]
- [[wiki/topics/Requirement to Architecture Mapping]]

## Source notes

- `pages/karpathy-guidelines.md`
- `pages/项目___AI___skills.md`
