---
title: Effective Harnesses for Long-Running Agents Source Guide
category: sources
tags: [agents, harness, anthropic, memory, context]
sources:
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
  - https://www.anthropic.com/research/long-running-Claude
created: 2026-09-11T00:00:00+0800
updated: 2026-09-11T00:00:00+0800
summary: >-
  Anthropic 工程文章：用初始化 Agent（搭环境+任务清单）与执行 Agent（逐 feature 增量推进+留 git/进度工件）两种初始 prompt，让 agent 跨多个上下文窗口稳定接力完成长任务。
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.00
base_confidence: 0.60
lifecycle: draft
lifecycle_changed: 2026-09-11
---

# Effective Harnesses for Long-Running Agents Source Guide

> Source: Anthropic Engineering, "Effective harnesses for long-running agents", 2025-11-26. https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
> 关联一手来源: Anthropic Science, "Long-running Claude for scientific computing", 2026-03-23. https://www.anthropic.com/research/long-running-Claude

## What It Covers

文章处理「长时运行 agent」的核心工程问题：agent 只能在离散会话中工作，每个新会话对之前一无所知（比喻为轮班工程师无前任记忆），而上下文窗口有限、复杂项目装不进单窗口。作者给出一套双 prompt 的 harness：一个**初始化 Agent** 在首个会话搭环境，一个**执行 Agent** 在此后每个会话增量推进并留下清晰工件。代码见 Claude 官方 `autonomous-coding` quickstart。

作者明确脚注：所谓「两个 agent」只是**初始 user prompt 不同**，system prompt、工具集与整体 harness 完全相同。

## Key Points

- 单靠 compaction 不够：前沿模型只给「build a clone of claude.ai」这样的高层 prompt，在多窗口循环下仍做不出生产级应用。^[extracted]
- 两个失败模式：**一把梭**（想 one-shot，中途耗尽上下文，把半成品无文档甩给下一轮）与**过早收工**（后续 agent 看到有进展就宣布完成）。^[extracted]
- **初始化 Agent 产物**：`init.sh`（起开发服务器）、`claude-progress.txt`（历轮进度日志）、初始 git commit（固定初始文件）。^[extracted]
- **任务清单（feature list）**：扩展用户需求成详尽、可端到端测试的清单（claude.ai 克隆案例 200+ 条），全部初始 `failing`；用 JSON 而非 Markdown（模型更不易误改）；每条含 `description` 与 `steps`。执行 Agent **只能改 `passes` 字段**，「It is unacceptable to remove or edit tests」。^[extracted]
- **执行 Agent 增量推进**：一次只做一个 feature；用描述性 git commit + 进度文件收尾，保持「可合并主干」的干净状态；坏改动可 `git revert` 回滚。^[extracted]
- **开局仪式**：`pwd` → 读进度文件与 git log → 用 `init.sh` 起服并跑基础端到端测试（先修破损再开新 feature）→ 读清单挑最高优先级未完成项。^[extracted]
- **端到端测试**：给浏览器自动化工具（Puppeteer MCP），要求「像真人用户一样」验证，否则易把没跑通的 feature 标成完成。局限：看不到浏览器原生 alert 弹窗。^[extracted]
- **科学计算版（关联来源）**：进度文件称 `CHANGELOG.md`，是「agent 的可移植长期记忆／实验室笔记」；应记录当前状态、已完成、**失败尝试及原因**、精度表、已知局限；配 test oracle、git 协调、Ralph loop。C 编译器项目跨越约 2000 会话；Fermat 大定理形式化跨越 11 天。^[extracted]

## Open Questions

- 单一通用执行 Agent 是否最优，还是专门化的 testing/QA/cleanup agent 更好？（作者列为 future work）^[extracted]
- 这套主要在全栈 web app 验证的方法，如何推广到科研、金融建模等领域？^[extracted]

## Related

- [[wiki/concepts/Long-Running Agent Harness]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Memory]]
- [[wiki/sources/Codex Maxxing for Long Running Work Source Guide]]
- [[wiki/sources/The AI-Native SDLC Playbook Source Guide]]
