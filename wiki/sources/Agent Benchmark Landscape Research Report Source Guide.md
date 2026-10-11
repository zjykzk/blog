---
title: Agent Benchmark Landscape Research Report Source Guide
type: source
status: draft
category: sources
tags: [survey, agents, metrics, testing, judgment]
aliases:
  - Agent 评测集研究报告
  - Agent Benchmark Landscape
relationships:
  - target: "[[wiki/concepts/Agent Evaluation Metric Vector]]"
    type: related_to
  - target: "[[wiki/concepts/Agent Evaluation CLASSic Framework]]"
    type: related_to
  - target: "[[wiki/topics/Rule Adjudication Agent Evaluation]]"
    type: related_to
  - target: "[[wiki/concepts/Evaluation]]"
    type: related_to
sources:
  - /Users/zenk/Documents/Agent_Benchmark_Landscape_Research_20261010/research_report_20261010_agent_benchmark_landscape.md
  - conversation:2026-10-10
created: 2026-10-10T19:36:48+0800
updated: 2026-10-10T19:36:48+0800
summary: >-
  42 个一手与官方来源构成的 Agent 评测集研究导览，比较通用助手、工具调用、代码、Web/GUI 与安全评测，并提出静态回归、fresh/OOD 和私有 canary 三层组合。
provenance:
  extracted: 0.82
  inferred: 0.16
  ambiguous: 0.02
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-10
tier: supporting
---

# Agent Benchmark Landscape Research Report Source Guide

> Source: [Agent 评测集：能力地图、测量陷阱与选型框架](/Users/zenk/Documents/Agent_Benchmark_Landscape_Research_20261010/research_report_20261010_agent_benchmark_landscape.md)

## What It Covers

这份报告以 42 个学术论文、官方文档和 leaderboard 为来源，比较五类 Agent 评测：通用助手与办公、工具调用与事务对话、软件工程与科研、Web/GUI/computer-use、安全与对抗。

报告不复制某一时点的模型排名，而是比较较稳定的结构：被测构念、环境真实性、判分器、可靠性指标、污染风险和 benchmark 生命周期。其证据账本、主张账本、HTML、PDF 与验证结果保存在同一 Documents 目录。

## Key Points

- 不存在一套可以充当“Agent 综合高考”的单一评测集。GAIA 核对最终短答案，tau-bench 核对事务后的数据库状态，SWE-bench 核对仓库补丁，WebArena 与 OSWorld 核对网页或操作系统终态；这些百分比不是同一测量单位。
- 选评测集前要先确定构念、环境、grader 和版本。一个分数只有在这些条件与目标部署一致时，才具有决策意义。
- pass@k 表示多次采样中至少一次成功，适合有强 verifier 的搜索流程；pass^k 表示多次独立运行全部成功，更接近重复交付的可靠性要求。
- 公开静态集便于回归和复现，但会受到污染与 benchmark-specific 调优；滚动 fresh set 更抗污染，却会改变难度和分布。
- 推荐三层评测组合：版本化静态回归集、fresh/private/OOD 集、从真实业务流量构造的私有 canary。
- 报告不主张把成功率、成本、时延、安全和人工介入压成一个未经解释的总分；更好的输出是 [[wiki/concepts/Agent Evaluation Metric Vector|多维指标向量]] 和 Pareto profile。
- 规则裁决 Agent 是上述通用框架的一个专门实例：它需要把最终标签继续拆成适用性、事实、构成要件、例外和证据充分性，并用 [[wiki/concepts/Confusion Matrix|混淆矩阵]]展开错误方向。^[inferred]

## Open Questions

- 如何为中文法规、企业制度和本地应用构造具有真实代表性的私有案例？
- 如何在规则变化时同时保留历史可比性与当前有效性？
- 如何给漏报、误伤、错误拒判和过度裁决分配业务代价？
- 如何证明公开 benchmark 的改善能够迁移到真实业务流量？

## Related

- [[wiki/concepts/Agent Evaluation CLASSic Framework]] — Cost、Latency、Accuracy、Security、Stability 五维。
- [[wiki/concepts/Agent Evaluation Metric Vector]] — 轨迹级多维指标。
- [[wiki/topics/Rule Adjudication Agent Evaluation]] — 面向合规与规则判断的专门评测方法。
- [[wiki/concepts/Confusion Matrix]] — 最终分类错误的方向结构。
- [[wiki/sources/AI Evals FAQ Source Guide]] — 从真实 traces 和 failure taxonomy 建立产品评测。

