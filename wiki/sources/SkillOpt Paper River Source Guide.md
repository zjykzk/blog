---
title: SkillOpt Paper River Source Guide
category: sources
tags: [paper, arxiv, agents, skills, optimization]
sources:
  - conversation:2026-06-11
  - https://arxiv.org/abs/2605.23904
created: 2026-06-11T10:39:52+0800
updated: 2026-06-11T10:39:52+0800
summary: >-
  保留 SkillOpt 论文倒读法：从 ReAct、Reflexion、文本优化、GEPA 与技能库路线，说明 agent skill 自进化如何从生成技能推进到治理技能改动。
provenance:
  extracted: 0.92
  inferred: 0.08
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-06-11
aliases:
  - SkillOpt 论文倒读法
  - SkillOpt paper river
---
# SkillOpt Paper River Source Guide

> Source: 当前会话生成的 SkillOpt 论文倒读法，基于 arXiv:2605.23904。

## Capture Policy

这页保存的是会话中生成的 paper-river 阅读路径，而不是完整替代 SkillOpt 原论文 source guide。它的价值在于保留“agent skill 自进化问题如何演化”的问题线：从可见轨迹、语言反馈、文本优化、轨迹反思，到技能改动的诊断、选择和验证。

## What It Covers

SkillOpt 讨论的问题是：如果一个 agent skill 在任务中失败，系统能不能不只是改当前答案，而是把失败转化为可复用、可检查、可验证的 skill 改动。

这条线属于 [[wiki/concepts/Skill Self-Evolution]] 和 [[wiki/topics/AI Skills Workflow]] 的交叉处。已有工作说明了 skills 可以作为可复用能力包，也说明了 prompt 和文本化控制资产可以被优化；SkillOpt 的关键推进是把 skill evolution 从“生成一个更好技能”推进到“管理一次技能变更”。

## Preserved Content

### 核心问题

LLM agent 的错误通常不是一个参数坏了，而是长过程里某个判断、工具选择、边界条件或检查步骤漏了。一次失败可以被写成反思，可以被抽成技能，也可以被优化器拿去改写文本。但这三件事各有风险：

- 反思太散，可能只对当前任务有效。
- 技能太难写，经验不一定能稳定迁移。
- 自动优化容易只追训练题分数，把坏归因写进共享技能。

SkillOpt 的主张是：skill 不只是 prompt 片段，而是会影响未来行为的操作规程。这样的对象如果能自动改，就需要根因分析、候选比较和前后验证。

### 溯源地图

```text
[2022] ReAct
  |
  | 问题: LLM 会说答案，但工具使用过程不可检查。
  | 解法: 把 thought / action / observation 交错摊开。
  v
[2023] Reflexion / Self-Refine
  |
  | 问题: 轨迹可见，但失败教训没有沉淀。
  | 解法: 把失败写成自然语言反馈，再用于下一轮。
  v
[2023] OPRO / DSPy
  |
  | 问题: prompt 和 LM pipeline 靠人手调，复杂后难维护。
  | 解法: 把 prompt / module 当成可评测、可搜索、可编译对象。
  v
[2024] TextGrad
  |
  | 问题: 文本对象不能像 tensor 一样反向传播。
  | 解法: 让 LLM 把批评写成类似 gradient 的修改方向。
  v
[2025] GEPA
  |
  | 问题: scalar reward 说明分数差，却不说明轨迹为什么失败。
  | 解法: 读取执行轨迹和评估轨迹，反思并进化文本化控制资产。
  v
[2026] Trace2Skill / EvoSkill / SkillsBench
  |
  | 问题: agent 需要长期可复用技能，而不是只优化 prompt。
  | 解法: 从轨迹中挖技能，演化技能库，并评估技能迁移。
  v
[2026] SkillOpt
  |
  | 问题: 技能会自己改以后，坏归因和坏合并会污染未来行为。
  | 解法: root-cause analysis + pairwise selection + before/after validation。
```

### 从可见轨迹到可复用教训

ReAct 的转折是把 agent 的“想”和“做”摊开。它让错误有了定位点：失败可能来自推理、动作选择、工具观察解释或停止条件。这个动作解决了黑箱问题，但没有解决长期学习问题；轨迹看完就过去了。

Reflexion 和 Self-Refine 把这一步推进成“错题本”：模型读自己的失败，写出自然语言反馈，再用反馈修下一轮。它们证明语言批评比单个分数更有信息量，但这些反馈通常仍绑定在局部任务上，未必能成为可检索、可维护、可迁移的能力。

### 从手调 prompt 到优化文本程序

OPRO 和 DSPy 把 prompt / LM pipeline 从一次性输入变成可优化对象。OPRO 让 LLM 生成候选 prompt，DSPy 把 LLM 调用组织为声明式模块，再通过编译和搜索优化指令、示例和模块组合。

TextGrad 进一步把批评变成“文本梯度”：虽然文本不能直接求数学梯度，但评审模型可以指出修改方向。这个方向让语言反馈进入优化循环，也暴露出新的风险：批评器自身可能不准，优化器可能把文本改成讨好批评器，而不是真正提升任务表现。

### GEPA 的关键转折：不要过早压成分数

GEPA 看到的问题是，复杂 agent 任务的失败原因藏在执行轨迹里。最终 reward 只能告诉系统“这次不好”，不能告诉系统“是搜索词错了、工具返回解释错了，还是最后一步漏了确认”。

GEPA 因而把优化信号从最终分数拉回执行过程：让 LLM 读取轨迹、诊断失败、生成改写，并通过进化和 Pareto selection 保留不同局部赢家。它适合优化 prompt、tool description、workflow rule、agent artifact 等文本化控制资产。

### 技能库路线把经验外化为操作资产

Trace2Skill、EvoSkill、SkillsBench 代表的问题转向是：经验不应该都塞进越来越长的 prompt，而应外化为可命名、可检索、可修改、可评估的技能。

这一步让 [[wiki/concepts/Agent Skill]] 成为长期能力载体。技能可以包含说明、约束、示例、脚本、资产和工作流门槛。它比局部反思更稳定，但也更危险：一旦错误经验被写成共享技能，它会污染后续许多任务。

### SkillOpt 的贡献：给技能演化加执行策略

SkillOpt 的问题不是“能不能写一个技能”，而是“能不能可靠地改一个技能”。它把 skill evolution 拆成三层策略：

- 根因分析：先读失败轨迹，判断失败是否真的来自 skill 本身。
- 成对选择：不要只接受一个候选修改，而是比较多个候选，判断哪个更像在修真正缺陷。
- 前后验证：修改后的 skill 要和修改前对照，确认提升不是偶然。

这把 skill evolution 从文本生成问题推向治理问题。skill 是可复用操作规程，因此每次改动都应该像代码变更一样有 diagnosis、candidate selection、validation 和 rollback 预期。^[inferred]

## Integration Decisions

这页应作为 SkillOpt paper-river 的 source 层材料保留。它补上了 [[wiki/sources/GEPA Paper River Source Guide]] 之后的一步：GEPA 说明轨迹反思怎样优化文本化控制资产；SkillOpt 说明当这个资产是共享 skill 时，优化本身需要变成可治理的变更流程。

SkillOpt 与 [[wiki/concepts/Skill Self-Evolution]] 的关系：前者可以作为后者的治理化实例。已有 Skill Self-Evolution 页面强调边界任务、变体优化、对照执行和可追溯评分；SkillOpt 强调失败根因、候选选择和改动前后验证。

SkillOpt 与 [[wiki/concepts/Verification Loop]] 的关系：它把 verification 从“当前任务是否成功”推进到“技能改动是否应该进入未来默认行为”。这更接近 skill CI，而不只是一次 task eval。^[inferred]

当前先不新建 “SkillOpt” 概念页，因为它更适合作为论文方法或 source 层入口；稳定可提升的概念是 “skill change governance” 或 “skill CI”，但需要更多后续论文或工程案例再沉淀。^[inferred]

## Open Questions

- SkillOpt 的 before/after validation 能否证明提升来自 skill 修改本身，而不是 evaluator 偏差或任务样本偶然性？
- 当一个 skill 被多个任务共享时，SkillOpt 如何检测对旧任务的回归？
- skill 改动是否需要像代码一样维护版本、依赖、冲突检测、权限边界和回滚策略？
- 高风险 skill 是否应强制进入人工审查，而不是自动合并？^[inferred]

## Related

- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Skill Self-Evolution]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/maps/Self-Evolving Agents Map]]
- [[wiki/sources/GEPA Paper River Source Guide]]
- [[wiki/sources/Skills-Coach Paper Source Guide]]
- [[wiki/sources/SkillOS Paper Source Guide]]
