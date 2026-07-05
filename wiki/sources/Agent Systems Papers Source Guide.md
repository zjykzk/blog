---
title: Agent Systems Papers Source Guide
type: source
status: seed
summary: Source guide collecting agent-system papers and deciding which claims should stay source-level versus move into topics, concepts, and syntheses.
category: sources
sources:
  - https://arxiv.org/abs/2603.28052
  - https://arxiv.org/abs/2604.27488
  - https://arxiv.org/abs/2603.07670
  - https://arxiv.org/abs/2601.12560v1
  - https://arxiv.org/pdf/2601.01743
created: 2026-05-04
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.84
  inferred: 0.15
  ambiguous: 0.01
source_count: 5
updated: 2026-07-05T12:25:46+0800
aliases:
  - agent papers source
  - agent systems source guide
tags:
  - papers
  - agents
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
- [[wiki/sources/GenericAgent Paper Source Guide]]
- [[wiki/sources/Lost in the Middle Paper Source Guide]]
- [[wiki/sources/Memory for Autonomous LLM Agents Source Guide]]
- [[wiki/sources/AI Memory Survey Source Guide]]
- [[wiki/sources/Meta-Harness Paper Source Guide]]
- [[wiki/sources/Skills-Coach Paper Source Guide]]
- [[wiki/sources/Agentic Artificial Intelligence Paper Source Guide]]
- [[wiki/sources/AI Agent Systems Architectures Applications and Evaluation Paper Source Guide]]

The Lost in the Middle paper contributes an evaluation protocol for usable long context: move the relevant evidence across the input and measure best-case versus worst-case performance, rather than treating max context length as capability.

The Memory for Autonomous LLM Agents paper contributes a memory-engineering survey: write–manage–read loop, mechanism families, multi-session evaluation gaps, production write/read paths, observability, deletion, and open challenges.

The AI Memory survey contributes a broad taxonomy and evaluation vocabulary for memory systems, especially the distinction between context, memory, knowledge, and experience.

The Meta-Harness paper contributes a search-loop view of harness engineering: executable harnesses can be proposed, evaluated, logged, and evolved by a coding-agent proposer with access to prior code, scores, and traces.

The Skills-Coach paper contributes a skill-level version of the same broader theme: individual skills can be probed with generated tasks, optimized through instruction or code variants, compared under execution, and retained through traceable evaluation.

The Agentic Artificial Intelligence paper contributes an architecture-level survey frame: POMDP-style agentic control loop, six-dimensional architecture taxonomy, workflow-graph orchestration, and CLASSic evaluation across cost, latency, accuracy, security, and stability.

The AI Agent Systems survey contributes a policy–memory–tool–verifier–environment abstraction for [[wiki/concepts/Agent Transformer]], a trace-first infrastructure view of sandboxing/schema/permission/logging layers, and a trajectory-level [[wiki/concepts/Agent Evaluation Metric Vector]].

## Related source guides

- [[wiki/sources/Agent Engineering Source Guide]]

## Candidate promoted wiki pages

- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Memory]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/concepts/Agent Memory Write-Manage-Read Loop]]
- [[wiki/concepts/Agent Memory Mechanism Families]]
- [[wiki/concepts/Agent Memory Evaluation Stack]]
- [[wiki/concepts/AI Memory 4W Taxonomy]]
- [[wiki/concepts/Context Information Density]]
- [[wiki/concepts/Lost in the Middle Effect]]
- [[wiki/concepts/Meta-Harness]]
- [[wiki/concepts/Skill Self-Evolution]]
- [[wiki/concepts/Workflow Graph Orchestration]]
- [[wiki/concepts/Agent Evaluation CLASSic Framework]]
- [[wiki/concepts/Agentic AI Architecture Taxonomy]]
- [[wiki/concepts/Agentic Control Loop]]
- [[wiki/concepts/Agent Transformer]]
- [[wiki/concepts/Agent Evaluation Metric Vector]]
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
