---
title: Agent Systems Papers Source Guide
type: source
status: seed
source_count: 2
updated: 2026-04-23
aliases:
  - agent papers source
  - agent systems source guide
tags:
  - papers
  - agents
  - ai
  - source
---

# Agent Systems Papers Source Guide

## Current role

这页用于收拢“agent system 论文”这一类来源材料。

它的职责不是直接给出稳定结论，而是作为 source layer，记录哪些论文值得进入当前 AI / Agent 知识簇，以及它们分别更适合往哪些 topic / synthesis 提升。

## Why keep this as a separate source guide

单篇论文 source note 能处理单个输入，但当这类材料开始变多时，缺的往往不是下一篇摘要，而是一层更稳定的来源组织结构。

这层 guide 的价值在于：

- 让同类论文不再孤立存放
- 帮助区分“单篇观点”和“跨论文稳定判断”
- 为后续形成 agent architecture / harness / workflow 相关 synthesis 提供来源入口

## Promotion rule

这类论文进入 `wiki/` 时，优先遵循这条路径：

1. 先做单篇 source guide
2. 在单篇笔记里明确：哪些判断值得上升、哪些细节应留在 source layer
3. 把稳定判断提升到 `topics/`
4. 当多篇论文开始围绕同一问题形成统一观察框架时，再进入 `syntheses/`

## Current examples

- [[wiki/sources/Dive into Claude Code Source Guide]]
- [[wiki/sources/Before the Tool Call Source Guide]]
- [[wiki/sources/Managed Agents Source Guide]]

## Related source guides

- [[wiki/sources/Agent Engineering Source Guide]]

## Candidate promoted wiki pages

- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/syntheses/AI Engineering Workflow]]

## What should stay source-level

以下内容通常更适合留在单篇 source notes，而不是直接升格成稳定 wiki 结论：

- 具体实验细节
- 某个系统实现的局部机制枚举
- 针对单篇论文的逐点批评
- 尚未被多来源支持的强结论

## Next additions

后续如果继续 ingest OpenClaw、Codex、Devin 或其他 agent system 论文，可以继续挂到这里，再判断是否足以形成新的 topic / synthesis。