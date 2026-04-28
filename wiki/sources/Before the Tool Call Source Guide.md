---
title: Before the Tool Call Source Guide
type: source
status: seed
source_count: 1
updated: 2026-04-22
aliases:
  - 2603.20953 source guide
  - Open Agent Passport paper
  - Deterministic Pre-Action Authorization paper
tags:
  - paper
  - arxiv
  - agents
  - authorization
  - security
  - source
---

# Before the Tool Call Source Guide

## Current role

这篇 arXiv 论文更适合作为单篇 source-facing note 进入当前仓库，而不是直接升格成稳定 topic 页。

它的重要性不在于“又多了一个 agent system 实现”，而在于它把一个经常被默认掉的问题单独抽了出来：agent 在真正调用工具之前，是否存在一个确定性的、可审计的授权层。

对当前仓库来说，这更像一个高价值输入判断：它可以喂给 agent / harness / tool routing 相关页面，但是否足以形成独立稳定 topic，还要看后续是否有更多来源共同支撑。

## Source metadata

- Title: *Before the Tool Call: Deterministic Pre-Action Authorization for Autonomous AI Agents*
- arXiv: https://arxiv.org/abs/2603.20953
- PDF: https://arxiv.org/pdf/2603.20953
- arXiv ID: `2603.20953`
- Author: Uchi Uchibeke
- Submitted: 2026-03-21
- Ingested: 2026-04-22

## Why ingest this

- 它把“tool use safety”从提示词层或事后审计层，前移到了执行前的 policy enforcement。
- 它提出的不是模糊的“让模型更谨慎”，而是一个同步拦截、策略判定、签名审计的执行机制。
- 这类设计会直接影响我们如何理解 harness、tool boundary、权限模型和 agent 可治理性。
- 对 AI / Agent 知识簇来说，这篇论文补的是“执行前授权”这一层，而不是通用 agent workflow。

## Distilled claims

- 论文提出了一个明确问题：autonomous agent 在调用工具前，通常缺乏标准化的 pre-action authorization 机制。
- 它给出的核心方案是 Open Agent Passport（OAP）：在工具执行前同步拦截 action request，再基于 declarative policy 做确定性判定。
- OAP 不只做 allow / deny，还会产出 signed audit records，使每次动作决策可以被回溯和校验。
- 论文报告的重点结果不是大模型能力提升，而是治理层效果：在 1,000 次决策中中位 enforcement latency 为 53ms，同时 restrictive policy 在 adversarial testing 下显著提高了阻断能力。
- 这篇论文的核心判断是：agent safety 不能只依赖模型行为对齐，还需要一个独立于模型生成内容的执行前控制层。
- 从系统设计角度看，它把安全、合规、质量控制和操作边界统一成了“tool invocation gate”问题。

## Candidate wiki destinations

### [[wiki/topics/AI Harness]]

可吸收的判断：
- harness 不只是上下文封装和工具接线层，也可以是执行前授权的制度层。
- 真正关键的不是“agent 能不能调用工具”，而是“调用前是否经过独立于模型输出的策略判定”。
- 这会强化一个判断：安全边界不应完全内嵌在 prompt 或模型自觉里。

### [[wiki/topics/Tool Routing]]

可吸收的判断：
- tool routing 不只是选哪个工具，也包括动作是否应被允许发生。
- route selection 和 authorization gate 应被区分：前者解决 capability match，后者解决 permission and policy match。
- 这能帮助避免把“选对工具”和“允许执行”混成一个问题。

### [[wiki/topics/AI Skills Workflow]]

可吸收的判断：
- workflow 设计除了顺序与边界，还要考虑每个 action step 是否需要显式授权语义。
- 一个成熟 workflow 不只是让 agent 会做事，也要让系统知道什么事在什么条件下可以做。

## What should stay source-only

以下内容目前更适合留在 source layer，而不是直接升格成稳定 wiki 结论：

- OAP reference implementation 的具体实现细节
- 论文中 adversarial test 的具体攻击样本与枚举
- latency benchmark 的实验设置细节
- “restrictive policy 一定优于其他治理模型”这类尚未跨来源验证的强结论

当前更值得吸收的是它提出的问题切分方式：把模型行为、工具能力、权限判定、审计记录拆成不同层，而不是把它们统称为 agent safety。

## Open questions

- 当前仓库是否需要单独形成一个更明确的 topic，例如 tool authorization / agent governance？
- 对 agent system 来说，pre-action authorization 应被视为 harness 的子机制，还是一层独立架构组件？
- 如果后续继续 ingest MCP、安全沙箱、policy engine 相关资料，是否应形成一个更稳定的 synthesis，把“tool use”与“governance boundary”统一起来？
