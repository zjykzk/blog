---
title: GEPA Paper River Source Guide
category: sources
tags:
  - paper
  - arxiv
  - agents
  - skills
  - optimization
sources:
  - conversation:2026-05-31
  - https://arxiv.org/abs/2507.19457
  - /Users/zenk/Documents/notes/20260531T111953--paper-river-gepa-reflective-prompt-evolution__paper_river.org
created: 2026-05-31T11:35:17+0800
updated: 2026-05-31T11:35:17+0800
summary: >-
  保留 GEPA 论文倒读法：从 APE、APO、DSPy、MIPROv2、TextGrad/GRPO 到 GEPA，说明 prompt/agent 优化如何从分数搜索转向轨迹反思与 Pareto 进化。
provenance:
  extracted: 0.66
  inferred: 0.28
  ambiguous: 0.06
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-05-31
---

# GEPA Paper River Source Guide

> Source: GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning, plus the generated paper-river note at `/Users/zenk/Documents/notes/20260531T111953--paper-river-gepa-reflective-prompt-evolution__paper_river.org`.

## Capture Policy

这页保存当前会话生成的 GEPA 论文倒读法，而不是替代 GEPA 原论文 source guide。它的价值在于保留“问题如何演化”的阅读路径：从自动 prompt 搜索，到多模块 LM 程序优化，再到使用执行轨迹和评估轨迹的反思式进化。

## What It Covers

GEPA 解决的问题是：复杂 AI 系统失败时，优化器不应只拿到一个 scalar reward。prompt、reasoning、tool calls、compiler errors、rubric feedback 和 evaluator traces 本来就是自然语言或可序列化文本；把这些信息压成一个分数，会丢掉“为什么错、哪个模块错、下一版规则该怎么写”的学习信号。

这条 paper river 把 GEPA 放进三条汇合的研究线：

- 自动提示工程：prompt 可以被生成、搜索、筛选。
- 复合 AI 系统优化：真实 workflow 是多模块程序，不是单个 prompt。
- 反馈学习：自然语言反馈、TextGrad 和 RL/GRPO 分别代表“保留诊断”和“用标量奖励训练”的两种压力。

## Preserved Content

### 问题之河

核心问题是：如果一个 AI 系统做错了，我们到底该用什么来教它变好？

最早的做法是人手写 prompt。之后，APE 一类方法把 prompt 看成可搜索的 instruction；APO/ProTeGi 用失败样本生成自然语言“梯度”；DSPy 把 prompt chain 变成声明式 LM pipeline；MIPROv2 在多模块程序中同时优化 instructions 和 demonstrations；TextGrad 与 GRPO 分别把问题推向 textual feedback 和 scalar reward training。GEPA 的转折是：不要急着把复杂轨迹压成一个分数，而要让 LLM 阅读轨迹、诊断失败、改写具体模块，并用 Pareto frontier 保留多种局部赢家。

### 溯源地图

```text
[2022/2023] APE - Large Language Models Are Human-Level Prompt Engineers
  |
  | 问题: prompt 靠人试太慢
  | 解法: 让 LLM 生成候选 instruction, 再按任务分数筛
  v
[2023] APO/ProTeGi - Automatic Prompt Optimization with "Gradient Descent"
  |
  | 问题: 只枚举候选不够会诊, 不知道当前 prompt 为什么差
  | 解法: 用 minibatch 失败样本生成自然语言 "gradient", 反向改 prompt
  v
[2024] DSPy - Declarative LM Pipelines
  |
  | 问题: 真实系统不是单个 prompt, 而是多模块 pipeline
  | 解法: 把 LM 调用声明成模块, 用 compiler/teleprompter 自动优化
  v
[2024] MIPROv2 - Optimize Instructions and Demonstrations
  |
  | 问题: 多模块程序要同时调 instruction 和 few-shot examples, 还有信用分配难题
  | 解法: 用程序感知/数据感知 proposal + minibatch surrogate + Bayesian optimization
  v
[2025] TextGrad + GRPO as pressure
  |
  | 问题: TextGrad 有语言反馈但容易沿单路迭代; GRPO 可训练权重但 rollout 太贵
  | 解法: 一个走 textual backprop, 一个走 scalar reward policy optimization
  v
[2025/2026] GEPA - Reflective Prompt Evolution Can Outperform RL
  |
  | 问题: 复杂系统的失败信息被全局分数压扁, 搜索又容易陷入局部最优
  | 解法: 读取执行/评估轨迹, 反思式改写模块 prompt, 用 Pareto frontier 保留多种赢家
  v
[2026] Early extensions and tooling
  |
  | 问题: GEPA 不只想优化 prompt, 还想优化代码、agent architecture、skills
  | 解法: optimize_anything / DSPy integration / agent skill evolution 等工程化扩展
```

这不是一条单一引用链，而是 GEPA 汇合的几条支流。确认的直接对比包括 MIPROv2、TextGrad、Trace/OptoPrime、GRPO；APE、APO/ProTeGi、DSPy 是更上游的问题来源。^[ambiguous]

### APE：prompt 先被看成可搜索程序

APE 的问题意识是：LLM 输出质量高度依赖 prompt，而有效 prompt 主要靠人试。它把 instruction 当成小程序，让 LLM 生成候选，再用任务分数筛选。

这一步的贡献是把“写 prompt”从手艺变成搜索问题。它的限制是：它主要处理单个 instruction，并且只知道哪个候选分高，不知道低分候选为什么错。

### APO/ProTeGi：失败样本开始变成自然语言梯度

APO/ProTeGi 看到的问题是：只枚举候选 prompt 很浪费，因为分数不解释失败原因。它用 minibatch 失败样本生成自然语言“gradient”，再把 prompt 往相反语义方向改。

这一步像把 prompt 优化从“看排行榜”推进到“看病历”。但它仍偏向单 prompt 或较简单任务，不能充分解决多模块 workflow 中的信用分配问题。

### DSPy：多模块 LM pipeline 成为优化对象

DSPy 的关键转折是把真实 LLM 系统看成 pipeline，而不是单次调用。它把 LM 调用声明成模块，让 compiler/teleprompter 优化整个 pipeline。

这给 GEPA 提供了对象模型：如果系统由多个模块组成，优化器就可以明确地说“我现在要改第 j 个模块的 prompt”。^[inferred]

### MIPROv2：多模块程序要同时调 instruction 和 examples

MIPROv2 延续 DSPy，处理更具体的问题：多模块 LM 程序既要优化 instruction，也要优化 few-shot demonstrations；还要用小批量评估降低成本，并处理模块间信用分配。

它的局限在于，主要还是把 rollout 变成分数或 surrogate signal。GEPA 的批判是：错误消息、推理链、工具输出和 evaluator feedback 本身就是学习信号，不应过早压缩。^[inferred]

### TextGrad 与 GRPO：两种压力汇入 GEPA

TextGrad 代表“文本版反向传播”：AI 系统里的 prompt、方案、代码等文本变量可以接收 LLM 生成的自然语言反馈。它保留了语言诊断，但容易沿单路迭代或依赖具体计算图形式。^[inferred]

GRPO 代表“用可验证奖励训练权重”：如果任务有明确 reward，就可以采样大量 rollouts 并按相对奖励更新策略。DeepSeekMath 显示这条路有效，但代价是 rollout 多、成本高，并且很多 API-only 或最大模型不能直接 fine-tune。

GEPA 对这两条路的综合是：保留 TextGrad 式自然语言诊断，但用进化与 Pareto frontier 维持多样候选；保留 RL 的评估压力，但不把所有诊断信息压成 scalar reward。

### GEPA：轨迹反思 + Pareto 候选池

GEPA 的优化循环是：

1. 运行当前系统，收集 execution trace 和 evaluation trace。
2. 让 reflection LM 阅读当前模块 prompt、轨迹、分数和文字反馈。
3. 反思失败原因，把经验写进新的 prompt。
4. 如果候选在 minibatch 上变好，就加入候选池。
5. 用 Pareto frontier 保留在不同样本上表现好的非支配候选。

GEPA 的强点不只是 mutation，而是保留“各有绝活”的候选，不急着只追平均分最高版本。对于 agent workflow，这相当于把一次次失败变成可读、可合并、可审查的经验资产。^[inferred]

### 2026 工程化延伸

截至 2026-05-31，尚未找到成熟论文系统性改进 GEPA。更明确的后续是工具化和工程化：

- `gepa-ai/gepa` 把方法包装成可优化任意文本 artifact 的库。
- DSPy 集成让 GEPA 进入 LM pipeline 优化工作流。
- Hermes Agent Self-Evolution 把 DSPy + GEPA 用到 agent skills、tool descriptions、system prompts 和代码演化上，并通过测试、大小限制、语义保持和 PR review 加护栏。

这说明 GEPA 的核心应用方向可能不止是 prompt optimization，而是让 skills、tool descriptions、routing rules、code templates 等文本化控制资产进入可评估的进化循环。^[inferred]

## Integration Decisions

这页应作为 GEPA paper-river 的 source 层材料保留。关于 GEPA 原论文的细节、实验表格和算法伪代码，可以后续单独创建 `GEPA Paper Source Guide`；这里不替代 primary paper capture。

可提升到稳定概念的候选是“trace-reflective optimization”：优化器读取执行和评估轨迹，以自然语言诊断失败并改写控制资产。当前先不新建概念页，因为已有 [[wiki/concepts/Skill Self-Evolution]]、[[wiki/concepts/Meta-Harness]]、[[wiki/concepts/Harness Ratchet]] 能承接大部分机制。

GEPA 与 [[wiki/concepts/Skill Self-Evolution]] 的关系：Skill self-evolution 可以把 GEPA 作为一种优化引擎，用于从 skill 运行失败中改写 instruction 或 code helper，但 skill 进入共享仓库仍需要 [[wiki/concepts/Verification Loop]] 和人工 review。^[inferred]

GEPA 与 [[wiki/concepts/Meta-Harness]] 的关系：两者都重视 raw traces。差异是 GEPA 主要优化文本化 prompt/artifact，Meta-Harness 搜索可执行 harness code，并让 coding-agent proposer 读取文件系统中的代码、分数和轨迹。^[inferred]

## Open Questions

- 当 evaluator 没有高质量文字反馈时，GEPA 的优势会下降到什么程度？
- Pareto frontier 保留多种局部赢家时，如何防止最终 prompt 变成冗长、过拟合的经验堆？
- Agent skill 自我演化应如何区分“优化 skill artifact 本身”与“优化到 benchmark 或 judge 偏好”？
- GEPA、Meta-Harness、SkillOS 这类外循环系统未来是否会合并成一个更通用的 trace-driven agent improvement stack？^[inferred]

## Related

- [[wiki/concepts/Skill Self-Evolution]]
- [[wiki/concepts/Meta-Harness]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/AI Harness]]
- [[wiki/sources/Skills-Coach Paper Source Guide]]
- [[wiki/sources/Meta-Harness Paper Source Guide]]
- [[wiki/sources/Agent Skills Survey Paper Source Guide]]
