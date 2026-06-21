---
title: Self-Evolving Agents Map
type: map
status: seed
category: maps
tags:
  - agents
  - harness
  - skills
  - memory
  - optimization
sources:
  - conversation:2026-05-31
created: 2026-05-31T15:02:10+0800
updated: 2026-06-11T22:36:02+0800
summary: >-
  自进化 agent 地图按学习发生的层次组织已实现系统：运行时认知、技能、技能仓库、harness 代码和记忆基线。
provenance:
  extracted: 0.72
  inferred: 0.24
  ambiguous: 0.04
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-31
aliases:
  - 自进化 Agent 地图
  - Self-Evolving Agent Systems
---
# Self-Evolving Agents Map

自进化 agent 不是一类单一系统，而是一组把执行轨迹、评估反馈、记忆、技能、工具说明或 harness 代码写回未来行为的系统。关键问题不是“它有没有 memory”，而是：学习发生在哪一层，更新什么对象，由什么反馈决定是否保留。

## 分层总览

```text
模型权重层
  - 当前 wiki 尚未把某个已实现 agent 作为重点
  - 影响上限最高，但慢、贵、不可 inspect

Harness code 层
  - Meta-Harness
  - 搜索可执行 agent 外壳：prompting、retrieval、memory update、tool orchestration

Skill repository 层
  - SkillOS
  - 训练 curator 管理一整个 SkillRepo：insert / update / delete

单个 skill / prompt / tool description 层
  - Skills-Coach
  - Hermes Agent Self-Evolution
  - GEPA as optimizer
  - SkillOpt

运行时 cognition / memory 层
  - AutoAgent
  - GenericAgent
  - Voyager
  - Reflexion

底层 memory substrate / baseline
  - MemGPT
  - ReasoningBank
  - MemP
  - Memory-as-a-Tool
```

这个分层来自 [[wiki/concepts/Continual Learning for AI Agents]] 的判断：agent continual learning 不应只理解成 model-weight update；harness、context、memory、skill 都可以成为可检查的学习表面。

## 运行时自进化 Agent

### AutoAgent

AutoAgent 是运行时自适应最完整的一类系统。它维护 internal cognition、external cognition、elastic memory 和 composite actions：工具、同伴、环境反馈、行动链都可以从轨迹中被修订。它的核心动作是“意图-结果对账”：本来想让工具或同伴达到什么结果，实际发生了什么。

AutoAgent 的价值在于把任务执行变成认知更新：动作失败不只留在上下文里，而会改写下一次工具选择、同伴选择和复合动作生成。风险也在这里：如果反思器错误判断意图和结果是否对齐，坏经验会进入长期认知。^[inferred]

### GenericAgent

[[wiki/sources/GenericAgent Paper Source Guide]] 记录的是 *GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization*。它的自进化不靠改模型，而靠把验证过的轨迹压缩成 SOP 和 scripts，并通过层级记忆保存 index、fact、SOP、raw-session。

GenericAgent 的主轴是 [[wiki/concepts/Context Information Density]]：长期 agent 的表现不取决于 nominal context window 有多大，而取决于有限 active context 中有多少 decision-relevant information。它报告在重复 HuggingFace dataset-download 任务中，token use 从约 200k 降到约 100k，因为经验被蒸馏成可复用 memory。

### Voyager

Voyager 在当前 wiki 中不是独立 source guide，而是作为 agent memory survey 中的代表系统出现。[[wiki/sources/Memory for Autonomous LLM Agents Source Guide]] 把它放在 procedural skill library 路线：Minecraft agent 把成功经验沉淀为技能库，报告 3.3x more unique items 和 15.3x faster tech-tree progression；没有 skill library 时速度下降 15.3x。

Voyager 说明早期自进化 agent 的关键不是写更多上下文，而是把可复用行为折成技能。它的治理、评估和跨域泛化仍弱于后来的 SkillOS、Skills-Coach 或 Hermes 路线。^[inferred]

### Reflexion

Reflexion 用 verbal self-critiques as episodic memory。失败后写自然语言反思，后续尝试读取这些反思。[[wiki/sources/Memory for Autonomous LLM Agents Source Guide]] 记录其 HumanEval pass@1 报告为 91%，GPT-4 baseline 为 80%。

Reflexion 是轻量自进化原型：它证明自然语言反思能改进后续尝试，但它缺少更强的验证、回滚、版本治理和共享资产机制。^[inferred]

### Memory-as-a-Tool

[[wiki/sources/Memory-as-a-Tool Paper River Source Guide]] 记录的是 feedback guideline memory 路线：Self-Refine 和 Reflexion 证明批评与反思有效，但常常只服务当前任务；Memory-as-a-Tool 把 rubric feedback 抽象成可读、可编辑、可检索的文件原则，让后续任务直接读取这份工作手册。

它位于运行时反思记忆和 skill/harness ratchet 之间：更新对象不是模型权重，也不是完整 skill，而是从 feedback 中蒸馏出的 guideline 文件。关键风险是坏反馈被固化、文件碎片化、检索扩展性，以及多 agent 共享时的 provenance 和 rollback。^[inferred]

## Skill 层自进化

### Skills-Coach

[[wiki/sources/Skills-Coach Paper Source Guide]] 是当前 wiki 中最明确的单 skill 自进化系统。它把一个 [[wiki/concepts/Agent Skill]] 当成可评估组件：从 `Skill.md` / `Readme.md` 解析命令、参数、约束、例子和失败模式，生成 standard / advanced / boundary tasks，再用 training-free GRPO 优化 instruction 或 code，并通过 comparative execution 与 traceable evaluation 决定保留。

报告结果包括：Skill-X 48 个 skills，平均分从 0.378 到 0.84，pass rate 从 33.59% 到 88.02%。这些数值应留在 source 层，直到有独立复现或代码检查。

Skills-Coach 的稳定贡献是 [[wiki/concepts/Skill Self-Evolution]]：skill 质量不只看说明文件是否完整，而要看它在边界任务上的行为覆盖。

### Hermes Agent Self-Evolution

Hermes Agent Self-Evolution 在 [[wiki/sources/GEPA Paper River Source Guide]] 中作为 GEPA 工程化延伸出现。它把 DSPy + GEPA 用到 `SKILL.md`、tool descriptions、system prompts、workflow/code artifacts 上，并通过 tests、size limits、semantic preservation、cache compatibility 和 PR review 加护栏。

Hermes 的重要性不在“agent 会自我进化”这个口号，而在它把自我改进变成软件工程流程：生成候选，跑评估，过约束，开 PR，人审。它适合共享 skill / prompt / tool-description 生态，因为共享控制资产一旦写坏会污染许多未来运行。^[inferred]

### GEPA as optimizer

GEPA 本身不是完整 agent，但可以作为自进化引擎。[[wiki/sources/GEPA Paper River Source Guide]] 把它概括为：从 execution trace、evaluation trace 和文字反馈中反思失败，生成 prompt/artifact 变体，再用 Pareto selection 保留多种局部赢家。

GEPA 适合被 Hermes、DSPy pipeline、Skills-Coach 类系统用于优化文本化控制资产。

### SkillOpt

[[wiki/sources/SkillOpt Paper River Source Guide]] 记录的是 skill change governance 的问题线。它把 ReAct、Reflexion、OPRO/DSPy、TextGrad、GEPA、Trace2Skill/EvoSkill 这条线收束到一个更具体的问题：当可优化对象是共享 agent skill 时，系统不能只生成一个新版本，还要判断失败是否来自 skill、候选修改是否修对了病因、改完是否真的优于旧版本。

[[wiki/sources/SkillOpt Paper Source Guide]] 保存原论文层：SkillOpt 把 skill document 当成冻结目标模型外部的可训练状态，用 scored rollouts 生成 add/delete/replace edits，再通过 textual learning-rate budget、held-out validation gate、rejected-edit buffer 和 epoch-wise slow/meta update 训练 compact `best_skill.md`。报告结果包括 52/52 evaluated cells best or tied-best、GPT-5.5 direct chat 平均 +23.5 points、Codex loop +24.8、Claude Code loop +19.1，以及 Codex-trained SpreadsheetBench skill 迁移到 Claude Code 的 +59.7 gain。

SkillOpt 的稳定价值是把 [[wiki/concepts/Skill Self-Evolution]] 推向类似 CI 的治理流程：root-cause analysis、pairwise selection 和 before/after validation。它与 Skills-Coach 的边界任务评估互补；前者更强调变更决策链，后者更强调自动生成任务和比较执行。^[inferred]

### Raw Experience to Skill Consumption

[[wiki/sources/Raw Experience to Skill Consumption Paper Source Guide]] 不是一个新的 skill optimizer，而是把 model-generated agent skill 的生命周期拆成 experience generation、skill extraction 和 skill consumption 三段来测。它报告 skills 在 75% 组合中提升，但 25% 组合出现负迁移；文本裁判无法可靠选出真正高效 skill，在高差距 pair 上只 15.8% 选中高效版本。

这篇的价值是给 skill 自进化系统补诊断尺：抽取或优化 skill 之前，先确认 rubric 是否和下游 utility 对齐。它筛出的三维 utility rubric 是：写出具体失败机制、给出领域动作级补救、列出高风险动作警告。^[inferred]

## Skill Repository 层自进化

### SkillOS

[[wiki/sources/SkillOS Paper Source Guide]] 是 repository-level self-evolution 的主要入口。SkillOS 冻结 task-solving executor，把 skill curation 设为可训练组件：executor 使用持久 SkillRepo，curator 观察轨迹后对 Markdown skills 做 insert、update、delete。

SkillOS 的难点是 delayed downstream reward：一个 skill 写得好不好，可能要到后续相关任务中 executor 检索并使用它时才显现。它通过 grouped task rollouts 和 GRPO 训练 curator，让奖励绑定到整个 repository path，而不是当前一步。

报告结果包括：ALFWorld 上 Qwen3-8B executor 的平均成功率提高到 61.2，强 baseline ReasoningBank 为 55.7；Qwen3-32B executor 到 68.6；Gemini-2.5-Pro executor 到 80.2。SkillOS 的稳定贡献是把 procedural memory 从“经验条目集合”推进成“可训练的仓库维护策略”。^[inferred]

## Harness 层自进化

### Meta-Harness

[[wiki/sources/Meta-Harness Paper Source Guide]] 讲的是 harness code 自进化。它让 coding-agent proposer 读取现有 harness code、任务分数、raw execution traces 和 evaluation traces，然后提出新的 executable harness code。

Meta-Harness 把 [[wiki/topics/AI Harness]] 从 runtime plumbing 变成 search space：prompt construction、retrieval、memory updates、state transitions、tool calls、evaluation traces 都可能被改写。报告结果包括 online text classification 比 ACE 高 7.7 points 且约 4x fewer context tokens；retrieval-augmented math reasoning 在 5 个 held-out models 上平均 +4.7 accuracy；full raw traces 明显优于 scores-only 或 scores+summary。

它的风险也最大：自动搜索 harness code 容易触及 security、authorization、governance 和 benchmark overfitting，需要强 human review 和外部评估。^[inferred]

## Memory Baselines and Earlier Patterns

### ReasoningBank and MemP

[[wiki/sources/SkillOS Paper Source Guide]] 把 ReasoningBank 和 MemP 作为 SkillOS baseline。ReasoningBank 保存 reusable reasoning insights；MemP 是 procedural memory，包含手写 consolidation、forgetting 和 re-indexing。

它们已经有“经验变记忆”的方向，但不如 SkillOS 那样把 repository curation policy 训练出来。^[inferred]

### MemGPT

MemGPT 更像 memory architecture，而不是严格意义上的自进化 agent。[[wiki/sources/Memory for Autonomous LLM Agents Source Guide]] 把它描述为 OS-inspired paging：main context 像 RAM，recall storage 像 disk，archival storage 像 cold vector-indexed storage。

MemGPT 解决“记忆如何存放和分页”，但不直接解决“从失败中改写技能或 harness”。^[inferred]

## 选型判断

如果目标是做一个能自进化的 agent 系统，先判断学习层级：

| 目标 | 优先看 |
|---|---|
| 运行中少踩工具/同伴/动作链的坑 | AutoAgent, GenericAgent |
| 从轨迹中沉淀 procedural skills | Voyager, GenericAgent |
| 自动优化单个 skill | Skills-Coach, Hermes |
| 管理一整个 skill 仓库 | SkillOS |
| 自动搜索 agent 外壳代码 | Meta-Harness |
| 做最小反思原型 | Reflexion |
| 做 memory substrate | MemGPT, ReasoningBank, MemP |

成熟度上，SkillOS 和 Skills-Coach 的评估闭环最清楚；Meta-Harness 最有野心但风险高；GenericAgent 更偏 token-efficient harness；AutoAgent 的运行时适应覆盖面最广但反思可靠性是关键弱点；Hermes 是工程化方向很对的 GEPA 延伸，但当前 wiki 还没有独立论文级 source guide。^[inferred]

## Related

- [[wiki/concepts/Continual Learning for AI Agents]]
- [[wiki/concepts/Skill Self-Evolution]]
- [[wiki/concepts/Meta-Harness]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Context Information Density]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/AI Memory]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/sources/GenericAgent Paper Source Guide]]
- [[wiki/sources/Skills-Coach Paper Source Guide]]
- [[wiki/sources/SkillOS Paper Source Guide]]
- [[wiki/sources/Meta-Harness Paper Source Guide]]
- [[wiki/sources/GEPA Paper River Source Guide]]
- [[wiki/sources/SkillOpt Paper River Source Guide]]
- [[wiki/sources/Raw Experience to Skill Consumption Paper Source Guide]]
- [[wiki/sources/Memory for Autonomous LLM Agents Source Guide]]
- [[wiki/sources/Memory-as-a-Tool Paper River Source Guide]]
