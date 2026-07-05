---
title: Agent Evaluation Metric Vector
type: concept
status: seed
summary: Agent Evaluation Metric Vector treats agent evaluation as a trajectory-level vector of success, cost, tool correctness, robustness, safety, and intervention metrics.
category: concepts
sources:
  - https://arxiv.org/pdf/2601.01743
created: 2026-07-05T12:25:46+0800
updated: 2026-07-05T12:25:46+0800
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: "2026-07-05"
provenance:
  extracted: 0.9
  inferred: 0.09
  ambiguous: 0.01
relationships:
  - target: "[[wiki/concepts/Agent Evaluation CLASSic Framework]]"
    type: extends
  - target: "[[wiki/concepts/Verification Loop]]"
    type: uses
aliases:
  - agent metric vector
  - trajectory-level agent metrics
tags:
  - agents
  - evaluation
  - safety
---
# Agent Evaluation Metric Vector

Agent Evaluation Metric Vector 是一种把 agent 评估从单一成功率扩展为多维轨迹指标的框架。

[[wiki/sources/AI Agent Systems Architectures Applications and Evaluation Paper Source Guide]] argues that deployable agents should be measured by end-to-end task success, efficiency, tool correctness, trajectory quality, robustness, and safety/compliance together.

## Core Metrics

The paper starts from a benchmark with tasks `D = {1, ..., N}`. For task `i`, the agent produces a trajectory `τ_i` with `T_i` steps, a verifier returns success `s_i`, and the evaluation also tracks time, token counts, tool calls, and safety indicators.

Core task-performance metrics include:

$$
SuccessRate = \frac{1}{N}\sum_{i=1}^{N}s_i
$$

$$
\bar{R} = \frac{1}{N}\sum_{i=1}^{N}R_i, \quad \bar{t}=\frac{1}{N}\sum_{i=1}^{N}t_i, \quad \bar{T}=\frac{1}{N}\sum_{i=1}^{N}T_i
$$

## Metric Vector

The paper's reporting vector includes:

- task success and reward;
- completion time and trajectory length;
- token usage and estimated cost;
- tool-call count;
- tool selection accuracy, argument accuracy, and tool execution success;
- recovery rate after failed calls;
- valid-action rate and loop rate;
- robustness under perturbations, worst-case success, and variance across runs;
- violation rate, intervention rate, and interventions per step.

## Why It Matters

A single success rate can hide the actual system trade-off: an agent may complete a benchmark only by spending too many calls, retrying blindly, violating policy, depending on human intervention, or becoming too slow for production.

This extends [[wiki/concepts/Agent Evaluation CLASSic Framework]]: CLASSic names the high-level deployment dimensions, while the metric vector turns them into measurable trajectory fields. ^[inferred]

## Evaluation Consequence

For [[wiki/syntheses/Agent System Design Space]], this means agent architectures should be compared as Pareto trade-offs, not ranked by one number. A design that adds Tree-of-Thoughts, reflection, multi-agent debate, or extra verification must report not only whether success improves, but what happens to cost, latency, loop rate, side-effect containment, and reproducibility. ^[inferred]

## Related

- [[wiki/concepts/Agent Evaluation CLASSic Framework]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/AI Agent Systems Architectures Applications and Evaluation Paper Source Guide]]
