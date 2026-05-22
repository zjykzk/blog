---
title: Agent Engineering Source Guide
type: source
status: seed
category: sources
summary: 这页用于收拢“agent engineering / harness / workflow”这一类更偏工程综述与系统实践的来源材料。
sources: []
created: 2026-04-23
base_confidence: 0.70
lifecycle: draft
lifecycle_changed: 2026-05-05
source_count: 16
updated: 2026-05-20T04:11:49+08:00
aliases:
  - agent engineering source cluster
  - harness workflow source guide
  - agent engineering sources
tags:
  - agents
  - engineering
  - harness
---
# Agent Engineering Source Guide

## Current role

这页用于收拢“agent engineering / harness / workflow”这一类更偏工程综述与系统实践的来源材料。

它和 `Agent Systems Papers Source Guide` 不完全重合：后者更偏论文来源组织，这页则覆盖更广，包括工程文章、实践综述与系统设计拆解。

## Why keep this as a separate source guide

当来源不再只是论文，而开始混入高质量工程文章、框架设计总结和系统实践拆解时，只用 “papers” 这一层已经不够。

这层 guide 的价值在于：

- 把 agent engineering 相关来源从一般 AI 材料里单独拎出来
- 区分“概念性 topic”与“来源组织层”
- 为 `AI Harness`、`Context Management`、`AI Skills Workflow`、`Agent System Design Space` 提供稳定入口
- 帮助判断哪些材料适合先留在 source layer，哪些已经足以升格为 topic / synthesis

## Promotion rule

这类来源优先遵循这条路径：

1. 先进入单篇 source guide
2. 在单篇 guide 中明确哪些判断值得提升
3. 优先提升到相关 topic（如 harness、context、workflow）
4. 当多来源共同支撑一个更高层框架时，再进入 synthesis

## Current examples

- [[wiki/sources/Agent Harness Qiaomu Article Source Guide]]
- [[wiki/sources/Dive into Claude Code Source Guide]]
- [[wiki/sources/Before the Tool Call Source Guide]]
- [[wiki/sources/Agent Systems Papers Source Guide]]
- [[wiki/sources/Prompt Caching Claude Code Case Study Source Guide]]
- [[wiki/sources/Agent Harness Anatomy Source Guide]]
- [[wiki/sources/Agent Harness Engineering Source Guide]]
- [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]]
- [[wiki/sources/Claude Code Skills Source Guide]]
- [[wiki/sources/Seeing Like an Agent Source Guide]]
- [[wiki/sources/Harness Engineering Source Guide]]
- [[wiki/sources/ADK Skill Design Patterns Source Guide]]
- [[wiki/sources/Coding with AI Source Guide]]
- [[wiki/sources/Company Brain Source Guide]]
- [[wiki/sources/Team AI Coding Harness Seminar Source Guide]]
- [[wiki/sources/Harness Engineering Is Cybernetics Source Guide]]
- [[wiki/sources/Agentic-First Source Guide]]

The prompt-caching guide now covers both a secondary case-study explainer and Thariq's original Claude Code article, which contributes the production-harness angle: cache-hit monitoring, stable mode tools, deferred tool loading, and cache-safe compaction.

The agent-harness anatomy guide contributes the broad component inventory: orchestration loop, tool layer, memory, context management, prompt construction, output parsing, state management, error handling, guardrails, verification, and subagent orchestration.

Addy Osmani's harness-engineering guide contributes the operational discipline: treat agent mistakes as harness improvement signals, then encode the lesson as rules, hooks, checks, done conditions, tool-surface changes, or workflow splits.

Rahul Garg's friction-reduction guide contributes the team collaboration layer: prime context, align design, anchor decisions, encode standards, and run a feedback flywheel.

Thariq Shihipar's Claude Code skills guide contributes the skill-operating layer: skills can bundle references, scripts, assets, memory, setup, and on-demand hooks, while progressive disclosure keeps the always-loaded context small.

Thariq Shihipar's "Seeing like an Agent" guide contributes the action-space design layer: observe model behavior, keep the top-level tool surface small, and choose between tools, skills, search, and subagents based on what the model can actually use.

Google Cloud Tech and Lavi Nigam's ADK skill-pattern guide contributes the skill content-design layer: Tool Wrapper, Generator, Reviewer, Inversion, and Pipeline are five ways to structure SKILL.md logic around different agent failure modes.

Martin Fowler's harness-engineering guide contributes the user-side workbench layer: developers can shape coding-agent behavior through context, rules, templates, computational checks, inferential review artifacts, and feedback loops.

Chris Parsons' coding-with-AI guide contributes the trainer-role layer: production AI coding shifts senior engineering attention from approving every diff to training the harness through markdown rules, skills, checks, reset discipline, and verification surfaces.

NanoThoughts' company-brain guide contributes the enterprise substrate layer: agents need organizational memory, communication context, action memory, reasoning graphs, and governed action before they can safely operate on company reality.

TechLead 少个分号's seminar recap contributes the team-discipline layer: harness must also shape human requirements, testing, self-test, and review behavior so AI generation can enter a closed verification loop.

George's harness-cybernetics article contributes the control-loop analogy: harness engineering is the move from direct code manipulation to designing sensors, actuators, desired state, and calibration rules around agentic coding.

James Pritchard's Agentic-First article contributes the platform-and-process layer: agent performance depends on file-oriented architecture, mode-aware context, edit-time validation, and moving human oversight to boundaries instead of preserving legacy workflow checkpoints.

## Main promotion destinations

- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/Tool Routing]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/concepts/Prompt Caching]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/AI Collaboration Scaffolding]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Agent Skill Design Patterns]]
- [[wiki/concepts/Agent Action Space]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/concepts/Feedforward and Feedback Controls]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/concepts/Harnessability]]
- [[wiki/concepts/Agentic Engineering]]
- [[wiki/concepts/Governed Action]]
- [[wiki/concepts/Context Graph]]
- [[wiki/concepts/Organizational Memory]]
- [[wiki/concepts/Company Brain]]
- [[wiki/concepts/Action Memory]]

## What belongs here

更适合挂到这里的来源通常有这些特征：

- 讨论 agent system 的运行层，而不只是模型能力本身
- 会同时涉及 harness、workflow、context、verification、tooling、safety 等多个维度
- 更像系统设计拆解或工程综述，而不是单点技巧帖

## What should stay source-level

以下内容通常应继续留在 source layer，而不应急着升格成稳定 wiki 结论：

- 单篇文章中的框架对比细节
- 某个作者自己的组件枚举方式
- 尚未被多来源共同支撑的趋势判断
- 主要依赖比喻成立的解释方式

## Relationship to papers source guide

可以这样区分：

- `Agent Systems Papers Source Guide`：偏论文来源组织
- `Agent Engineering Source Guide`：偏工程实践来源组织

两者都可以流向同一批 topic / synthesis，但来源类型不同，组织职责也不同。

## Next additions

后续如果继续 ingest 关于 Codex、Devin、OpenClaw、Claude Code、tool sandbox、evaluation loop、agent runtime 的高质量工程材料，都可以先挂到这里，再决定往哪些 topic / synthesis 提升。
