---
title: >-
  配置 钩子 代码库与技能放置决策 Source Guide
category: sources
tags: [agents, harness, skills, llm-wiki]
sources:
  - conversation:2026-05-15
created: 2026-05-15T22:32:37+08:00
updated: 2026-05-15T22:32:37+08:00
summary: >-
  这页保存一棵判断树：固定指令、可靠自动化、代码库规范和手动技能分别应该放在哪里。
provenance:
  extracted: 0.94
  inferred: 0.06
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-15
aliases:
  - Config Hook Codebase Skill Placement
  - 技能放置判断树
---

# 配置 钩子 代码库与技能放置决策 Source Guide

> Source: conversation:2026-05-15，关于“固定指令、自动化、代码库修复与技能”的放置判断树。

## Capture Policy

这页保存一段双语判断树作为 source-level 决策材料。它不把所有结论抽象成一个新概念，而是保留问题顺序、分支答案和每个放置位置背后的理由。

## What It Covers

这棵判断树回答一个元问题：当想让 LLM 或开发流程稳定表现出某种行为时，这个行为应该放进项目配置、hook、代码库，还是 skill。

它属于 [[wiki/topics/AI Skills Workflow]] 和 [[wiki/topics/AI Harness]] 的交界：skill 适合主动触发的特定流程；harness/config/hook/codebase 承担更基础、更可靠或更结构性的约束。

## Preserved Content

### 第一问：是否每次会话都需要发生

如果某件事需要在每次会话中都发生，答案是 **Project config / 项目配置**。

固定指令应该放进配置文件，而不是放进 skill。LLM 在每次会话开始时都会读取配置文件，因此不需要用户额外调用。配置适合承载 standing instructions：稳定、全局、每次都应该生效的协作规则。

### 第二问：是否需要自动发生，且不依赖记忆

如果某件事不需要每次会话都发生，但需要在特定条件下自动、可靠地发生，答案是 **hook / 钩子**。

可靠自动化应该属于 hook。hook 不会忘记执行；skill 会忘记，因为 skill 需要用户记得手动输入或触发。凡是“必须自动发生，而不能依赖人想起来”的行为，都更接近 harness 层的自动化，而不是知识或流程说明。

### 第三问：LLM 是否因为代码库不一致或难导航而困难

如果问题来自代码库本身不一致、缺少清晰模式或难以导航，答案是 **fix the codebase / 修复代码库**。

代码本身就是规范。与其给 LLM 写一段额外说明，不如把它指向一个展示目标模式的文件。如果短期确实不能修复，skill 可以作为临时创可贴；但不能把 skill 当成根本解决方案。^[inferred]

这个分支强调：当问题是结构性质量问题时，正确的持久资产是更清晰的代码、目录、示例和约定，而不是更多外部提示。

### 第四问：是否是在已知流程节点主动触发的特定工作流

如果某件事不是每次会话都需要，不需要自动发生，也不是代码库结构问题，而是一个用户会在已知节点主动触发的具体工作流，答案才是 **skill / 技能**。

skill 的合理定位是：有意识、不频繁、边界清楚、用户主动触发的工作流程。手动调用只在这种情况下有意义。skill 应该保持专注和具体，不应该承载全局规范、可靠自动化或代码库设计缺陷。

## Decision Tree

```text
Does this need to happen every time, in every session?
├─ yes → Project config
└─ no
   └─ Does it need to happen automatically without you remembering?
      ├─ yes → Hook
      └─ no
         └─ Is the LLM struggling because your codebase is inconsistent or hard to navigate?
            ├─ yes → Fix the codebase
            └─ no
               └─ Is this a specific workflow you deliberately trigger at a known point?
                  ├─ yes → Skill
                  └─ no → Do not add a skill by default
```

## Integration Decisions

- 这页保留为 source guide，因为原材料是一棵可复用的判断树，而不是一次跨来源综合。
- “skill 是最后一类放置位置”应连接到 [[wiki/concepts/Agent Skill]]，但不替代该概念页的定义。
- “hook 不会忘，skill 会忘”应连接到 [[wiki/topics/AI Harness]]，因为它描述的是运行时可靠性和自动化边界。
- “代码即规范”应连接到 [[wiki/concepts/Encoding Team Standards]]：当规范可以被编码进仓库结构和示例时，不应只依赖提示或技能。^[inferred]

## Related

- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Encoding Team Standards]]
