---
title: Managed Agents Source Guide
type: source
status: seed
source_count: 1
updated: 2026-04-25
aliases:
  - Scaling Managed Agents
  - Managed Agents
  - Decoupling the brain from the hands
tags:
  - agents
  - ai
  - harness
  - source
  - anthropic
source: https://www.anthropic.com/engineering/managed-agents
---

# Managed Agents Source Guide

## Current role

这篇 Anthropic engineering article 更适合作为一个 source-facing note 进入当前仓库，而不是直接升格成稳定 wiki 母页。

原因不是它不重要，而是它当前更像一个“托管式 agent 架构样本”：它提供的是一组关于 session、harness、sandbox、tool execution 和恢复机制的系统设计判断，适合先接入现有的 `AI Harness`、`Context Management` 和 `Agent System Design Space`，再看哪些结论值得进一步沉淀。

## Source metadata

- Title: *Scaling Managed Agents: Decoupling the brain from the hands*
- URL: https://www.anthropic.com/engineering/managed-agents
- Type: engineering article
- Ingested: 2026-04-25
- Parent source guide: [[wiki/sources/Agent Systems Papers Source Guide]]

## Why ingest this

- 它把托管式 agent 的系统复杂度，从“单个容器里塞下所有东西”，改写成“围绕稳定接口解耦 brain、hands 和 session”。
- 它强化了一个判断：harness 往往带着对模型弱点的假设，而这些假设会随着模型能力提升而过时。
- 它把 session log 从上下文窗口里抽离出来，强调 durable event stream 对恢复与长时任务的重要性。
- 它把 sandbox / credential boundary 说得更结构化：不是只讨论工具能不能调用，而是讨论执行环境应不应该接触 secrets。
- 它给出一个很有价值的 agent 扩展图景：many brains / many hands，而不是把整个系统死绑在一台 container 里。

## Distilled claims

- 文章主张：长时运行的 managed agents，应该围绕稳定接口构建，而不是围绕某一代 harness 实现构建。
- harness 的很多设计，本质上都编码了“模型现在还不够强”的假设；随着模型变强，旧 harness 可能变成约束而不是放大器。
- 早期 all-in-one container 方案的问题是：session、runtime、tools、code execution 和状态恢复都绑在一起，导致容器一旦失效，整个 agent 会话都变脆弱。
- 把 brain 和 hands 解耦之后，harness 可以通过统一执行接口对接 sandbox / tools，而不必把所有执行细节绑死在同一运行体内。
- 把 session log 放到 harness 之外后，session 可以通过 durable events 被回放和恢复，harness 崩掉也不必等于会话丢失。
- sandbox 与 credentials 分离是一种结构性安全提升：生成代码不应天然贴着 secrets 跑。
- session log 可以被理解为“上下文窗口之外的持久上下文”，而真正进入模型上下文的内容仍然需要 harness 负责塑形。
- 文章声称，这种架构还改善了启动延迟与 TTFT，并支持更灵活的扩展与恢复模型。

## Candidate wiki destinations

### [[wiki/topics/AI Harness]]

最直接的吸收对象。

可吸收的判断：
- harness 不应与具体执行容器死绑定
- harness 的价值之一，是在模型能力变化时仍保持接口稳定
- orchestration 与 execution 最好分层，而不是塞进一个不可替换的运行块里

### [[wiki/topics/Context Management]]

可部分吸收。

可吸收的判断：
- session log 不等于模型上下文窗口
- durable session context 与当前轮上下文塑形，是两层不同问题
- 长时 agent 的上下文设计必须把恢复能力考虑进去

### [[wiki/syntheses/Agent System Design Space]]

适合作为新的上游来源。

可吸收的判断：
- brain vs hands 是一种重要设计切面
- 托管式 agent 的环境约束，会显著改变 architecture 的最优解
- execution boundary、persistence boundary、credential boundary 应分开讨论

## What should stay source-only

以下内容目前更适合作为 source layer 保留，而不应直接升格为稳定 wiki 结论：

- 文中具体 API / interface 命名细节
- 具体延迟数字与性能声明
- 某一代内部实现为什么这样拆的局部工程历史
- “这种 managed architecture 就是通用最优解”这类过强结论

## Open questions

- 当前仓库是否应该补一个更明确讨论 `session as durable event log` 的 topic？
- `AI Harness` 是否需要继续拆出 execution boundary / persistence / recovery 等子主题？
- 如果后续继续 ingest 托管式 agent 系统文章，是否足以形成一个更清晰的 hosted-agent synthesis？
