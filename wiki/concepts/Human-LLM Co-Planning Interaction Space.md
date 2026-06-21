---
title: Human-LLM Co-Planning Interaction Space
type: concept
status: seed
summary: Human-LLM Co-Planning Interaction Space classifies plan steering by mode, scope, and edit level so humans can choose between control, effort, and rewrite risk.
category: concepts
sources:
  - https://arxiv.org/abs/2605.23023
created: 2026-06-09T14:38:26+08:00
updated: 2026-06-09T14:38:26+08:00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: "2026-06-09"
provenance:
  extracted: 0.82
  inferred: 0.16
  ambiguous: 0.02
aliases:
  - human LLM co-planning
  - co-planning interaction design space
  - process-level plan steering
tags:
  - agents
  - orchestration
  - human-in-the-loop
---
# Human-LLM Co-Planning Interaction Space

Human-LLM Co-Planning Interaction Space 是论文《How to Steer Your Multi-Agent System》提出的多 agent 计划修订框架。它把人在计划生成后的介入方式拆成三根轴：mode、scope、level。

这页的关键不是复述 AMBIPOM 原型，而是保留一个可迁移判断：当 multi-agent plan 变成显式 [[wiki/concepts/Workflow Graph Orchestration|workflow graph]] 时，人类 steering 不再只是“看最终结果是否对”，而是可以在过程层对局部结构、全局策略和执行边界做分层干预。

## Three axes

- Mode 区分 structural direct manipulation 和 semantic natural-language feedback。前者直接改图，后者让 LLM 根据语言反馈重写计划。
- Scope 区分 global feedback 和 targeted feedback。global 影响整个 plan，targeted 只影响被选中的 subgraph，并需要和未修改部分重新集成。
- Level 区分 low-level edits 和 high-level structural operations。low-level edits 包括加删节点、边、agent 分配、输入输出字段；high-level operations 包括 merge、split、replan 等组合编辑。

这个三轴模型把“人要怎样控制 agent 系统”从一个抽象 human-in-the-loop 口号，变成可设计、可比较、可评估的交互空间。^[inferred]

## Effort-control-risk trade-off

论文的用户研究显示，使用者并不会稳定选择一种交互类型，而是按迭代阶段组装 hybrid workflow：先 review 或 execute 当前计划，再用 targeted/global text feedback 做较大结构修订，然后用 direct manipulation 或 LLM-assisted structural edit 修局部细节，最后再次执行验证。

不同交互类型对应不同风险结构：

- direct manipulation 控制力最高，但人工成本最高。
- LLM-assisted high-level DM 提供结构杠杆，风险相对有边界。
- targeted feedback 提供语义杠杆，同时限制影响范围。
- global feedback 写作成本最低，但 verification burden 和“blow up the plan”的风险最高。

因此，人类 steering 的真实瓶颈往往不是“能不能更快生成编辑”，而是编辑之后能否确认全局依赖、边界兼容性和执行有效性。^[inferred]

## Design consequence

对 [[wiki/topics/AI Harness]] 来说，这个概念补上一类控制面：harness 不只要决定工具、权限和 memory，也要决定人类如何在显式计划上介入。

一个成熟的 co-planning harness 应至少支持：

- 计划图可视化，暴露 agent subtasks、data dependencies、node status 和 execution trace。
- targeted revision 前后显示边界输入输出，避免局部改动破坏全局图。
- edit preview、compatibility validation、orphan node detection、I/O mismatch warning 等轻量验证。
- 根据选中 subgraph 主动推荐下一步交互方式，例如 split、merge、parallelize、repair binding。
- 针对代码、表格、图片、长文本等不同产物提供 domain-specific output inspection panel。

## Open Questions

- 该三轴空间是否能扩展到多人协作、去中心化 multi-agent 系统或长周期 deep research workflow，论文仍未验证。
- targeted feedback 为了降低上下文噪声而只给 selected subgraph 和边界 I/O；这在真实复杂系统中可能和全局一致性需要冲突。^[ambiguous]
- 论文用户研究样本较小且来自 LLM 经验较强的研究群体，实际团队采用时的人机分工可能不同。^[ambiguous]

## Related

- [[wiki/concepts/Workflow Graph Orchestration]]
- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/sources/Human-LLM Collaborative Planning Paper Source Guide]]
