---
title: Agent Evaluation CLASSic Framework
type: concept
status: seed
summary: Agent Evaluation CLASSic Framework evaluates agent systems by cost, latency, accuracy, security, and stability instead of static answer quality alone.
category: concepts
sources:
  - https://arxiv.org/abs/2601.12560v1
  - https://arxiv.org/pdf/2601.01743
created: 2026-05-13T10:37:07+08:00
updated: 2026-07-05T12:25:46+0800
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: "2026-05-13"
provenance:
  extracted: 0.83
  inferred: 0.15
  ambiguous: 0.02
aliases:
  - CLASSic framework
  - CLASSic metrics
  - agent evaluation metrics
tags:
  - agents
  - evaluation
  - safety
---
# Agent Evaluation CLASSic Framework

Agent Evaluation CLASSic Framework 是论文采用的五维 agent 评估框架：Cost、Latency、Accuracy、Security、Stability。

它的出发点是：agent 从封闭问答走向真实部署后，BLEU、ROUGE 或静态 accuracy 不足以说明系统质量。一个 agent 可能答案正确但太慢、太贵、不稳定，或在接入文件、代码、企业 API 后受到 prompt injection 影响。

## Five Dimensions

- **Cost**：层级规划、tree search、多 agent debate 会增加 token 与推理成本。
- **Latency**：真实环境需要等待、并发、时间感知；异步任务和安全关键场景会放大延迟问题。
- **Accuracy**：不只是单题答对，而是长任务中 tool use、state tracking、recovery、verification 的总体成功率。
- **Security**：tool-connected agent 面临 direct / indirect prompt injection、confused deputy、权限与审计边界问题。
- **Stability**：包括 infinite loops、agent paralysis、错误级联、失败后是否能改变策略或请求人类介入。

## Why It Matters

这个框架把 [[wiki/concepts/Verification Loop]] 从“质量检查”扩展成运行时评价机制：agent 是否值得部署，要同时看准确性、成本、延迟、安全和稳定性，而不是只看模型能力榜单。^[inferred]

它也补强了 [[wiki/topics/AI Harness]] 的评价问题：harness 的作用不是让 agent 更复杂，而是在这些维度之间做可观察、可审计、可调优的权衡。^[inferred]

[[wiki/sources/AI Agent Systems Architectures Applications and Evaluation Paper Source Guide]] makes the same evaluation pressure more concrete through [[wiki/concepts/Agent Evaluation Metric Vector]]: cost, latency, security, and stability should be visible in trajectory fields such as token usage, tool-call count, recovery rate, loop rate, violation rate, and intervention rate.

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Agentic Control Loop]]
- [[wiki/concepts/Agent Evaluation Metric Vector]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/Agentic Artificial Intelligence Paper Source Guide]]
