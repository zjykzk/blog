---
title: Long-Running Agent Harness
category: concepts
tags:
  - agents
  - harness
  - memory
  - context
  - workflow
aliases:
  - 长任务 harness
  - 长时运行 agent harness
  - Initializer Coding Agent Split
  - 初始化-执行 双角色
relationships:
  - target: "[[wiki/topics/AI Harness]]"
    type: part_of
  - target: "[[wiki/topics/Context Management]]"
    type: uses
  - target: "[[wiki/topics/AI Memory]]"
    type: uses
  - target: "[[wiki/concepts/Loop Engineering]]"
    type: related_to
  - target: "[[wiki/concepts/Verification Loop]]"
    type: uses
sources:
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://www.anthropic.com/research/long-running-Claude
  - conversation:2026-09-11
summary: >-
  Long-Running Agent Harness 把跨多个上下文窗口的长任务拆成规划角色（初始化 Agent 把大任务钉成可测任务清单+搭环境）与执行角色（逐条增量推进、每轮把代码/清单/进度/git 留作可续接工件），本质是把 agent 记忆外置到文件系统与 git。
provenance:
  extracted: 0.82
  inferred: 0.18
  ambiguous: 0.00
base_confidence: 0.60
lifecycle: draft
lifecycle_changed: 2026-09-11
tier: supporting
created: 2026-09-11T00:00:00+0800
updated: 2026-09-11T00:00:00+0800
---

# Long-Running Agent Harness

Long-Running Agent Harness 是一种让 agent 跨越多个上下文窗口持续推进同一个大任务的脚手架：用一个**初始化角色**把模糊的高层需求钉成一份可逐条测试的任务清单并搭好环境，再用一个**执行角色**每轮只推进一个 feature、并在会话结束时把代码、任务清单、进度笔记和 git 提交留成下一轮可直接续接的工件。

## What It Is

它解决的根本难题是：agent 只能在离散会话（session）中工作，**每个新会话对之前发生的事没有记忆**——就像一个软件项目由轮班工程师接力，每位接班者都不记得上一班干了什么。因为上下文窗口有限、复杂项目装不进单个窗口，agent 需要一种在会话之间「架桥」的机制。

关键前提：这里的「两个角色」并不是两套模型或两套系统，而是**同一套 harness、同一个 system prompt、同一批工具，只是第一个会话用了不同的初始 user prompt**。因此「初始化 Agent / 执行 Agent」是同一 harness 的两种启动模式，而非独立部署的两个 agent。

它也直接回应了两个真实失败模式：
- **一把梭（over-eager one-shot）**：agent 想一次实现整个 app，中途耗尽上下文，把半成品且无文档的状态甩给下一轮，下一轮只能靠猜。
- **过早收工（premature victory）**：后续 agent 环顾四周看到已有进展，就直接宣布任务完成。

单靠 compaction（上下文压缩）不足以解决——即便前沿模型在 SDK 里循环运行，只给一句「build a clone of claude.ai」这样的高层 prompt，仍会因上述失败模式而做不出生产级应用。

## How It Works

### 初始化角色（Initializer）——只规划，不实现
只在第一个会话运行，产出**环境与任务清单**，不写业务功能：
- **任务清单（feature list）**：把用户一句话需求扩展成一份详尽、可端到端测试的功能清单（claude.ai 克隆案例里 200+ 条），每条初始标记为 `failing`，作为「完整功能长什么样」的清晰轮廓。清单用 **JSON**（如 `feature_list.json`）而非 Markdown——因为模型更不容易误改 JSON；每条含 `description` 与可执行的 `steps`。
- **启动脚本 `init.sh`**：让后续会话能一键起开发服务器、跑基础测试，不必每轮重新摸索如何运行项目。
- **进度日志 `claude-progress.txt`**：记录历轮 agent 做了什么的自由格式笔记。
- **初始 git commit**：把初始文件与环境基线固定下来。

### 执行角色（Coding）——增量推进，干净收尾
之后每个会话运行，被约束为**一次只做一个 feature**：
- **开局仪式**：`pwd` 定位 → 读进度文件与 `git log` 找回状态 → 用 `init.sh` 起服务并跑一遍基础端到端冒烟测试（若上一轮留下破损先修复）→ 读任务清单挑最高优先级未完成项。
- **收尾仪式**：把改动以描述性 message 提交 git（坏改动可 `git revert` 回滚到可用状态）+ 更新进度文件 + 把对应 feature 的 `passes` 从 `false` 翻成 `true`。
- **清单纪律**：只允许改 `passes` 字段，**禁止删改测试项**（用强措辞约束，避免丢失或掩盖功能）。
- **完成判据**：只有经过端到端自验证（如用浏览器自动化像真人一样操作）才可标 `passing`；这治住「过早收工」。

### 记忆外置：中间成果如何留给下一轮
「把中间成果留给下一轮」被具体拆成三类持久化工件：**已完成的代码文件（git 固化）+ 更新后的任务清单（passes 翻转）+ 进度笔记**。下一轮据此在全新上下文窗口里秒进状态，消除「靠猜上轮发生了什么」的开销。这与 [[wiki/topics/Context Management|上下文管理]] 中长任务的三大手段一致——compaction、结构化笔记（agentic memory）、[[wiki/concepts/Agent Memory Mechanism Families|多角色/子 agent 架构]]；进度笔记正是「结构化笔记」的落地，是 agent 的可移植长期记忆。

在科学计算迁移版里，进度文件常叫 `CHANGELOG.md`，被明确称为「agent 的可移植长期记忆／实验室笔记」，并强调要记录**失败的尝试及原因**（否则后续会话会重蹈同样的死路），配合测试预言机（test oracle）、git 协调、以及在 agent 声称完成时把它踢回上下文追问「真的做完了吗」的 Ralph loop。

## When to Use

- 任务跨越数十分钟到数小时/数天、token 总量超过单个上下文窗口（大型代码迁移、从零搭全栈应用、跨越 ~2000 会话的编译器、跨越数天的科研代码）。
- 成功判据清晰、可自动验证（有参考实现、测试套件或可量化目标），且人类监督可以是间歇而非持续的。
- **不适合直接并行多 agent**：多数编码任务耦合深、可并行度低、agent 间实时协调仍弱，因此长任务编码更偏「顺序单执行 Agent 接力」；[[wiki/concepts/Agent Memory Mechanism Families|并行多 agent]] 的甜点在广度优先、可并行的研究/检索类任务（见 orchestrator-worker：lead agent 把 plan 存到 Memory 防上下文截断，子 agent 把产物写文件系统、只回传轻量引用）。

局限：端到端验证受工具能力约束（如浏览器自动化看不到原生 alert 弹窗，相关 feature 更易残留 bug）；该模式主要在全栈 web app 上验证，向其它领域推广仍是开放问题；「专门化 testing / QA / cleanup agent 是否比单一通用执行 agent 更优」也尚无定论。

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Memory]]
- [[wiki/concepts/Loop Engineering]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Agent Memory Write-Manage-Read Loop]]
- [[wiki/concepts/Agent State]]
- [[wiki/sources/Effective Harnesses for Long-Running Agents Source Guide]]
- [[wiki/sources/Codex Maxxing for Long Running Work Source Guide]]
