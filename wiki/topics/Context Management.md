---
title: Context Management
type: topic
status: seed
summary: Context management designs what enters, stays in, leaves, and gets optimized in an AI agent's active context under finite attention, memory, and cache constraints.
category: topics
sources:
  - https://baijia.online/homepage/survey/Survey%20on%20AI%20Memory.pdf
  - https://arxiv.org/abs/2307.03172
  - https://addyosmani.com/blog/agent-harness-engineering/
  - https://x.com/_avichawla/article/2044670188998803855
  - https://x.com/trq212/status/2024574133011673516
  - https://x.com/akshay_pachaar/status/2041146899319971922
  - https://martinfowler.com/articles/reduce-friction-ai/context-anchoring.html
  - https://x.com/trq212/status/2027463795355095314
  - https://www.chrismdp.com/coding-with-ai/
  - https://arxiv.org/abs/2603.28052
  - https://arxiv.org/abs/2603.07670
created: 2026-05-04
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.0
source_count: 11
updated: 2026-05-13T09:59:22+08:00
aliases:
  - 上下文管理
tags:
  - agents
  - context
---
# Context Management

在当前 AI / Agent 知识簇里，上下文管理已经被明确视为 agent 的核心任务之一，而不是实现细节。

## Why it matters

如果上下文组织不好，会直接带来几个问题：

- 模型不知道当前任务的边界
- 有价值信息被淹没在杂音里
- 任务拆分和工具调用失去依据

所以很多 agent 质量问题，本质上不是模型能力不够，而是上下文没有被设计好。

这也是为什么在 production agent 里，上下文管理应该被看成高频失败点，而不是 token 层的小优化。

Akshay Pachaar's harness overview sharpens this point: context management is one of the components that turns a stateless model call into a stateful agent. The model does not carry durable working state by itself; the harness decides which memory, transcript, tool results, and current task state are visible on each turn.

[[wiki/sources/AI Memory Survey Source Guide]] clarifies the boundary: context is the bounded runtime workspace for the current inference step, while [[wiki/topics/AI Memory]] is persistent state outside that step. They form a loop: encode interaction traces into memory, retrieve selected memory into context, act, then update memory from the result.

## Practical role

在工作流里，上下文管理至少承担三件事：

- 保留完成任务所需的最小必要信息
- 让任务拆分和下一步决策有依据
- 让工具调用发生在正确边界内
- 在工具结果、错误反馈和 verification output 之间维持可用的工作状态

它还有一个更容易被忽略的角色：上下文管理并不只是“往窗口里塞信息”，而是在塑造模型内部形成判断的条件。

换句话说，当前可见的 prompt / memory / transcript 更像 reasoning 的输入约束，而不是 reasoning 本身的完整展开图。

## Context information density

[[wiki/sources/GenericAgent Paper Source Guide]] 把这个问题进一步压成一个更硬的原则：agent 的长期表现不主要取决于 nominal context window 有多大，而取决于有限上下文里保留了多少 decision-relevant information。

它把上下文质量拆成两个主要求：

- completeness：当前决策需要的信息必须在场
- conciseness：无关、过期、重复的信息必须被排除

这解释了为什么“多塞一点上下文”不总是更安全。上下文越长，position bias、无关信息稀释和 effective context length 收缩会一起把关键信息挤出可用注意力范围。

因此，更稳定的目标不是最大化可见历史，而是最大化 [[wiki/concepts/Context Information Density]]。

## Positional robustness

[[wiki/sources/Lost in the Middle Paper Source Guide]] gives the context-management cluster a concrete empirical failure mode: [[wiki/concepts/Lost in the Middle Effect]].

The paper shows that long-context models may use information well when it appears at the beginning or end of the input, but perform substantially worse when the same information appears in the middle.

This means context management has to govern ordering, not just inclusion:

- decision-critical evidence should not be buried in the middle of a long prompt
- retrieved documents may need reranking or truncation instead of simple top-k accumulation
- long-context claims should be evaluated by moving relevant evidence across context positions
- bigger context windows do not automatically imply better context use

For agent systems, this makes evidence placement part of runtime design. A harness that preserves the right fact but places it where the model is unlikely to use it has not really preserved usable context. ^[inferred]

## Context rot and resets

[[wiki/sources/Agent Harness Engineering Source Guide]] adds the practical failure name "context rot": long contexts can make an agent worse at reasoning and task completion as the window fills with stale, redundant, or low-signal material.

The article maps this to several harness mechanisms:

- compaction before the window overflows
- offloading large tool outputs to the filesystem while keeping only useful head/tail context inline
- progressive disclosure through skills instead of loading every instruction and tool at startup
- full context resets that rebuild a fresh session from a compact handoff file when compaction alone is not enough

This strengthens the current density view: context management is not only preserving history, but deciding when old history should leave the active reasoning surface and become retrievable state.

[[wiki/sources/Seeing Like an Agent Source Guide]] adds a second progressive-disclosure path from Claude Code practice: instead of preloading RAG context, give the agent search tools so it can build context itself. As models improved, Claude Code moved from handing Claude retrieved snippets toward letting Claude search the codebase, follow skill references, and recursively discover relevant material.

This reframes context management as supervised exploration, not just context selection. The harness designs which search and disclosure paths exist, while the model performs some of the context assembly. ^[inferred]

## Externalized decision context

[[wiki/concepts/Context Anchoring]] adds a collaboration-level answer to context rot: do not keep feature decisions only in the chat transcript.

Rahul Garg's article argues that developers keep long AI conversations alive because closing the session would lose the only record of decisions, reasons, rejected alternatives, open questions, and current implementation state. That behavior preserves nominal history while making the active context longer and less reliable.

The stronger pattern is to move decision context into a living feature document. This turns old chat history into compact external state that can be loaded into a fresh session, improving [[wiki/concepts/Context Information Density]] and making resets less costly. ^[inferred]

[[wiki/sources/Coding with AI Source Guide]] gives this a practitioner's reset heuristic: output quality follows a curve over context amount. Too little context yields generic output, while too much context drowns the model in stale or irrelevant detail.

When an agent starts looping through useless refactors, repeating wrong assumptions, or leading the human in circles, the recommended move is to stop, discard the polluted conversation, and restart with a cleaner brief and a smaller chunk.

## Long Context Is Not Memory

[[wiki/sources/Memory for Autonomous LLM Agents Source Guide]] adds a sharper boundary: extending context windows can delay memory pressure, but it does not solve persistent cross-session storage, selective retrieval from months of history, structured organization, deletion, or access control.

The paper also names two context-resident memory failure modes. **Summarization drift** gradually drops low-frequency but high-importance facts through repeated compression. **Attentional dilution** means that even when a fact remains inside a long context, the model may fail to focus on it.

This reinforces the existing density view: the goal is not to maximize visible history, but to decide which memory records deserve to become current working context for this step.

## Cache-stable context

[[wiki/sources/Prompt Caching Claude Code Case Study Source Guide]] adds an economic and runtime dimension to context management: the order and mutability of context affect whether repeated prompt tokens can be served from cache.

The useful split is:

- static prefix: system instructions, tool definitions, project context, and stable reference material
- dynamic suffix: user turns, assistant turns, tool output, and observations

If the static prefix remains byte-for-byte stable, provider-side [[wiki/concepts/Prompt Caching]] can reuse the [[wiki/concepts/KV Cache]] state for that prefix. If the harness injects timestamps, reorders tool schemas, changes tools, or rewrites upstream state, the cache can miss even when the semantic content feels equivalent.

This means context management has two simultaneous goals:

- preserve decision-relevant information density
- preserve prefix identity when stable information does not need to change

Those goals can conflict when a system wants to update policies, tools, or durable state mid-session. In that case, cache efficiency is not the only objective; it is one design constraint among correctness, safety, and freshness. ^[inferred]

The Claude Code prompt-caching source sharpens this into an ordering rule: stable system prompt and tools first, project context next, session context after that, and volatile conversation tail last. That ordering lets many sessions share global cache hits while still allowing each session to accumulate its own local context.

## Reasoning implication

如果接受“reasoning 主要发生在 latent-state trajectory，而不是表面 chain-of-thought”这一视角，那么上下文管理的重要性会被重新理解。

它不只是解决 token 不够的问题，而是在决定：

- 哪些信息能进入内部状态形成过程
- 哪些表面痕迹会被模型拿来当作下一步依据
- 哪些噪音会干扰判断
- 系统是否还能在上下文受限时维持连续工作

这意味着很多 agent 质量问题，不能只归因于模型推理能力，也要追问：

- 当前上下文是否把边界说清了
- 我们看到的表面推理文本，是否只是 reasoning 的外显痕迹
- 压缩、裁剪、摘要这些动作，是否改变了 latent-state formation 的条件

## Context policy as optimizable code

[[wiki/sources/Meta-Harness Paper Source Guide]] adds a program-search angle to context management. In its experiments, harness candidates can modify prompting, retrieval, memory, state updates, and orchestration logic; the context policy is therefore not just a hand-written heuristic but part of the executable search space.

This matters because context-management failures often appear only downstream: a retrieval choice, memory update, or prompt-construction rule may affect behavior many steps later. The paper argues that raw execution traces are needed to connect those delayed failures back to earlier harness decisions.

So context management has two layers: design the current information surface, and design the feedback loop that can revise that surface after observing failures. ^[inferred]

## Upstream concepts

- [[wiki/concepts/Agent]]
- [[wiki/concepts/LLM]]

## Peer topics

- [[wiki/topics/Tool Routing]]
- [[wiki/topics/AI Memory]]
- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/Agent Skill × Context Management]] — synthesis
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/concepts/Agentic Engineering]]
- [[wiki/topics/Prompt Frequency]]
- [[wiki/concepts/Prompt Caching]]

## Downstream synthesis

- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/syntheses/Agent System Design Space]]

## Source notes

- `journals/2026_04_04.md`
- [[wiki/sources/LLM Reasoning Is Latent, Not the Chain of Thought Source Guide]]
- [[wiki/sources/Dive into Claude Code Source Guide]]
- [[wiki/sources/Agent Harness Qiaomu Article Source Guide]]
- [[wiki/sources/GenericAgent Paper Source Guide]]
- [[wiki/sources/Prompt Caching Claude Code Case Study Source Guide]]
- [[wiki/sources/Agent Harness Anatomy Source Guide]]
- [[wiki/sources/Agent Harness Engineering Source Guide]]
- [[wiki/sources/Coding with AI Source Guide]]
- [[wiki/sources/Lost in the Middle Paper Source Guide]]
- [[wiki/sources/Memory for Autonomous LLM Agents Source Guide]]

- [[wiki/sources/AI Memory Survey Source Guide]]
- [[wiki/sources/Seeing Like an Agent Source Guide]]
