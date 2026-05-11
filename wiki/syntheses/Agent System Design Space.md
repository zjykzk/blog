---
title: Agent System Design Space
type: synthesis
status: seed
summary: Agent System Design Space compares agent architectures by values, context, tools, permissions, memory, delegation, recovery, cache economics, and harness evolution.
category: syntheses
sources:
  - https://baijia.online/homepage/survey/Survey%20on%20AI%20Memory.pdf
  - https://arxiv.org/abs/2307.03172
  - https://addyosmani.com/blog/agent-harness-engineering/
  - https://x.com/_avichawla/article/2044670188998803855
  - https://x.com/trq212/status/2024574133011673516
  - https://x.com/akshay_pachaar/status/2041146899319971922
  - https://x.com/hwchase17/status/2040467997022884194
  - https://arxiv.org/abs/2603.28052
  - https://arxiv.org/abs/2604.27488
created: 2026-05-04
base_confidence: 0.80
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.89
  inferred: 0.10
  ambiguous: 0.01
source_count: 8
updated: 2026-05-11T12:08:45+08:00
aliases:
  - Agent architecture design space
  - AI agent system design space
tags:
  - synthesis
  - agents
  - architecture
---
# Agent System Design Space

这页把 `AI Harness`、`Context Management`、`AI Skills Workflow` 串起来，不把 agent system 看成固定架构，而把它看成一个 design-space 问题：不同系统面对的是相似约束，但会因为价值排序和部署环境不同，长出不同答案。

## 1. Start from values, not mechanisms

很多关于 agent 的讨论，容易从机制出发：有没有 tool use、有没有 memory、有没有 multi-agent、有没有 workflow。

但如果只从机制看，容易把实现误当成问题本身。

更稳的起点是先问：这个系统到底想保护和放大什么。

从当前材料往上抽，可以先看到几类更基础的目标：

- 人类是否还保有关键决策权
- 系统是否在安全边界内工作
- 执行是否可靠、可恢复、可连续
- 外部接口是否真的在放大能力，而不是只在堆功能
- 上下文受限时，系统是否还能维持有效工作

机制是答案，价值排序才是题目。

## 2. The core loop is not the whole system

表面上看，很多 agent system 都可以被压成一个很简单的 loop：读上下文、调用模型、决定动作、执行动作、再继续下一轮。

但真正决定系统性质的，往往不是这个 loop 本身，而是 loop 外围的运行秩序。

也就是说：

- loop 决定系统怎样继续运转
- harness 决定系统在什么边界内运转

因此两个系统即使共享相似的 loop，只要外围的权限、压缩、隔离、恢复机制不同，最后的系统性质也会明显不同。

## 3. The main design surfaces

如果把 agent 当成一个系统而不是一个提示词技巧，那么至少有几块设计面必须被单独看待。

### Permission and approval boundary

系统需要决定：

- 哪些动作可以自动执行
- 哪些动作必须回到人类确认
- 哪些动作要在更严格的边界里运行

这不是一个附属开关，而是 agent 是否可控的核心结构。

### Verification and recovery

Akshay Pachaar's harness overview makes verification a first-class design surface rather than a final QA step.

The design question is:

- which failures should be retried automatically
- which failures should become observations for the model to repair
- which failures need user intervention
- which outputs can be checked by deterministic tests, visual inspection, or evaluator models

This is where [[wiki/concepts/Verification Loop]] connects to state management and error handling: feedback only improves an agent if the harness can route it back into the loop in a usable form.

Addy Osmani's harness-engineering article adds the ratchet angle: verification should not only catch this run's mistakes, but also expose which harness rule, hook, tool boundary, or workflow split should change so the same failure is less likely next time.

### Context compression and reconstruction

上下文永远不是无限的，所以系统要决定：

- 什么该被保留
- 什么该被压缩
- 什么该在下一轮被恢复出来

因此 context management 不是 token 工程小技巧，而是 system design 的核心组件。

[[wiki/sources/GenericAgent Paper Source Guide]] 给这块补了一个更精确的评价词：[[wiki/concepts/Context Information Density]]。也就是说，比较 agent architecture 时，不能只问它能不能恢复历史，还要问恢复出来的历史是否真的提高下一步决策的信息密度。

[[wiki/sources/Prompt Caching Claude Code Case Study Source Guide]] 又补了另一个评价面：上下文是否 cache-stable。一个 agent 可能语义上保留了正确历史，但如果每一轮都重写 system prompt、重排 tool schema 或改变 model，它会在 runtime economics 上退化成冷缓存系统。

[[wiki/sources/Lost in the Middle Paper Source Guide]] adds a third evaluation surface: positional robustness. A system can include the right evidence and still fail if that evidence lands where the model is least likely to use it.

所以 context design 至少有三层问题：

- what should be visible for the next decision
- what should be compressed or retrieved later
- what must remain stable enough for [[wiki/concepts/Prompt Caching]] to work
- where decision-critical evidence should be placed so it remains usable

### Extension surfaces

skill、hook、plugin、MCP 这些看起来分散的接口，实际上都在回答同一个问题：系统如何扩展自己的能力边界。

重点不只是“能不能接更多东西”，而是这些扩展是否让系统更稳定、更清楚、更可复用。

GenericAgent 的 minimal atomic tool set 提供了一个相反方向的设计样本：有时更少的工具反而能降低 prompt overhead 和 action-space ambiguity，让能力通过组合产生，而不是通过枚举接口产生。

The harness-engineering source adds a trust-boundary warning: tool and MCP descriptions are injected into the model's prompt surface, so extension is not only capability expansion. It is also prompt-surface expansion and should be treated as a security and context-design decision.

### Delegation and isolation

当任务变复杂时，系统是否能把局部问题隔离出去单独处理，会直接影响整体稳定性。

委派不是为了制造 multi-agent 的表面热闹，而是为了：

- 把任务边界切清楚
- 降低上下文污染
- 控制执行环境
- 让结果能够回流而不是把噪音一起带回来

### Persistence and recovery

一个 agent system 不能只考虑当前回合，还要考虑：

- 状态如何留下来
- 中断之后如何恢复
- 历史如何继续成为后续动作的依据

如果没有这一层，很多“会做事”的 agent 只能停留在短时演示，而很难变成连续工作的系统。

GenericAgent 把 persistence 进一步拆成层级记忆：常驻索引、事实层、SOP 层和原始会话归档层。这个分层的关键不是“记得更多”，而是让更深层知识可检索但默认不污染当前上下文。

The same design surface includes full context resets: for long jobs, a harness may deliberately tear down a saturated session and rebuild from a compact handoff file. That is recovery by reconstruction, not merely summarization.

[[wiki/sources/AI Memory Survey Source Guide]] broadens this surface into memory architecture: lifecycle, content type, storage representation, modality, consolidation policy, and sharing policy all change what the agent can preserve and reuse.

In multi-agent systems, memory also becomes a coordination substrate: agents may communicate through shared natural-language summaries, structured schemas, latent state, shared task-level experience, or step-level routing.

### Learning layer and learning scope

[[wiki/sources/Continual Learning for AI Agents Source Guide]] adds a learning-layer axis to the design space. An agent system can improve by updating model weights, harness code and always-on instructions, or configurable context and memory.

The same axis has a scope dimension: an update may apply to the whole agent, a single user, a team, an organization, or a tenant. This makes continual learning a boundary-design problem, not only an optimization problem. ^[inferred]


### Cache economics

Agent architecture also has an inference-economics surface: how much repeated work the system forces the model provider to redo.

For long sessions, a large static foundation can be cheap after the first turn if it remains an identical prefix. The same foundation can be expensive on every turn if the harness mutates anything upstream of the cache breakpoint.

This makes cache discipline a sibling of memory, tool design, and recovery rather than a billing afterthought. ^[inferred]

Thariq's Claude Code article makes this design surface operational: cache-hit rate is important enough to alert on, and cache misses can come from harness choices that look semantically harmless, such as timestamp injection, nondeterministic tool ordering, model switching, or changing a tool parameter upstream of the cache breakpoint.

### Harness lifecycle and runtime APIs

Addy Osmani's Agent Harness Engineering article adds a moving-surface view: every harness component encodes an assumption about what the model cannot yet do alone. When models improve, some scaffolding should be retired; when models unlock larger tasks, new scaffolding appears around memory policy, multi-agent coordination, evaluators, and dynamic tool/context assembly.

The same source frames Harness-as-a-Service as a shift from model-completion APIs toward configurable agent runtimes. The loop, tools, context management, hooks, sandboxing, and subagent primitives become platform surfaces, while domain work moves into prompt, tool, memory, and verification configuration.

That means agent architecture should be compared not only by mechanisms it contains, but by which mechanisms are vendor runtime defaults, which are locally configured, and which remain application-specific code. ^[inferred]

## 4. Why environment changes the architecture

同一类 agent 设计问题，在不同环境里并不会得到同一个最优解。

例如：

- 本地 CLI agent 更强调人机协同、权限确认和本地工具边界
- 托管式 agent 更可能强调控制平面、租户隔离和统一扩展注册
- 企业内部系统更关心审计、权限收敛和可治理性
- 强沙箱 workflow 更关心隔离、恢复和可重复执行

所以 agent architecture 不是静态模板，而是环境约束下的解空间。

## 5. A practical evaluation lens for agent systems

如果不想被具体实现细节牵着走，可以用一组更稳定的问题来评估 agent system：

- 它在放大什么能力
- 它在约束什么风险
- 它把什么决策留给人
- 它如何处理上下文受限的问题
- 它是否能避免 [[wiki/concepts/Lost in the Middle Effect]] 把关键证据埋在低效位置
- 它是否有 verification / evaluation loop 来纠偏自身输出
- 它是否把 repeated failures 转成 [[wiki/concepts/Harness Ratchet]] 层面的规则、hook 或 workflow change
- 它如何隔离复杂任务和执行环境
- 它如何记录状态，并在中断后恢复连续性
- 它的 memory 属于什么生命周期、内容类型、存储形式和模态
- 多 agent 共享 memory 时如何处理 provenance、冲突和访问边界
- 它如何保持静态 prompt / tool / context 前缀稳定，避免不必要的缓存失效
- 它哪些 harness assumptions 应该随模型能力变化而删除、替换或升级
- 它是在 raw model API 上自建 loop，还是在 Harness-as-a-Service runtime 上配置 domain-specific behavior

这样看，agent system 的差异不再只是 feature list 的差异，而是系统秩序设计的差异。

## Why this synthesis matters

如果没有这一层 synthesis，我们很容易把 agent 讨论切碎成很多局部话题：

- 只谈 loop，不谈外围秩序
- 只谈工具，不谈边界设计
- 只谈上下文，不谈恢复与连续性
- 只谈扩展能力，不谈人类决策权

把这些主题重新压到同一张图里之后，agent 才更像一个可比较、可设计、可解释的系统对象。

### Harness evolution and optimizer agency

[[wiki/sources/Meta-Harness Paper Source Guide]] adds another design surface: who or what changes the harness over time.

Before this source, the design space already separated model-level learning, harness-level learning, and context/memory learning. Meta-Harness sharpens the harness-level branch by showing an outer loop where a coding-agent proposer reads previous harness code, scores, and traces, then writes new harness code while evaluation remains external.

This adds two new architecture questions:

- Is harness evolution manual, semi-automated, or delegated to an agentic proposer?
- Does the proposer see raw traces and code, or only scores and compressed summaries?

The second question matters because the paper's ablations suggest that raw execution traces can be the difference between superficial scoring and useful credit assignment. ^[inferred]

### Skill evolution surface

[[wiki/sources/Skills-Coach Paper Source Guide]] adds a narrower but practical evolution surface: skills can be optimized as modular capability packages.

Compared with Meta-Harness, Skills-Coach does not search the whole harness program. It generates boundary-probing tasks from a target skill, optimizes instruction or code variants, runs comparative execution, and admits changes through traceable evaluation. This makes [[wiki/concepts/Skill Self-Evolution]] a middle layer between context updates and harness-code search. ^[inferred]

This adds two more architecture questions:

- Are reusable skills treated as static documentation, or as evaluated components with their own regression suite?
- Does the system optimize skills in virtual/documentation mode, real execution mode, or both?

The second question matters because virtual scoring may reward documentation signals, while real execution can expose file, command, dependency, and side-effect failures. ^[ambiguous]

## Upstream topics

- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Memory]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/concepts/Context Information Density]]
- [[wiki/concepts/AI Memory 4W Taxonomy]]
- [[wiki/concepts/Lost in the Middle Effect]]
- [[wiki/concepts/Prompt Caching]]
- [[wiki/concepts/KV Cache]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Agent Tool]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Meta-Harness]]
- [[wiki/concepts/Skill Self-Evolution]]

## Upstream source notes

- [[wiki/sources/Managed Agents Source Guide]]
- [[wiki/sources/GenericAgent Paper Source Guide]]
- [[wiki/sources/Lost in the Middle Paper Source Guide]]
- [[wiki/sources/AI Memory Survey Source Guide]]
- [[wiki/sources/Prompt Caching Claude Code Case Study Source Guide]]
- [[wiki/sources/Agent Harness Anatomy Source Guide]]
- [[wiki/sources/Agent Harness Engineering Source Guide]]
- [[wiki/sources/Skills-Coach Paper Source Guide]]

## Navigation

- [[wiki/maps/AI Map]]
