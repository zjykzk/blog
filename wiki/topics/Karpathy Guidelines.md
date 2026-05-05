---
title: Karpathy Guidelines
type: topic
status: growing
category: topics
summary: Karpathy Guidelines are coding constraints that reduce common LLM mistakes such as hidden assumptions, over-design, broad edits, and missing verification.
sources:
  - https://martinfowler.com/articles/reduce-friction-ai/encoding-team-standards.html
created: 2026-04-20
base_confidence: 0.53
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.72
  inferred: 0.28
  ambiguous: 0.0
source_count: 3
updated: 2026-05-05T17:45:00+08:00
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

[[wiki/concepts/Encoding Team Standards]] generalizes this page's role: guidelines become more valuable when they are encoded as versioned, shared instructions that execute in generation, refactoring, security checks, and review.

The difference is operational. A guideline page informs the human or assistant; an executable instruction applies the guideline as part of the workflow, with priority categories and expected output format. ^[inferred]

## Navigation

- [[wiki/maps/AI Map]]
- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/concepts/Encoding Team Standards]]

## Source notes

- `pages/karpathy-guidelines.md`
- `pages/项目___AI___skills.md`
