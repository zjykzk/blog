---
title: AI Harness
type: topic
status: growing
summary: AI Harness is the runtime order layer that connects model, context, tools, permissions, state, recovery, and cache stability into a controllable agent system.
category: topics
sources:
  - https://x.com/_avichawla/article/2044670188998803855
  - https://x.com/trq212/status/2024574133011673516
  - https://x.com/akshay_pachaar/status/2041146899319971922
created: 2026-05-04
base_confidence: 0.70
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.93
  inferred: 0.07
  ambiguous: 0.0
source_count: 8
updated: 2026-05-05T14:03:13+08:00
aliases:
  - harness
tags:
  - ai
  - agents
  - harness
  - runtime
---

# AI Harness

AI Harness 不是模型本身，也不是某一个工具本身。它更像 agent system 的运行层：把模型、上下文、工具、权限、委派和状态接起来，并给这些东西规定边界。

## Core idea

如果只看表面的 agent loop，很容易把系统理解成“模型调用 + 工具调用”的重复循环。

但从当前材料看，真正更决定系统性质的，往往不是 loop 本身，而是 loop 外围的秩序设计。

换句话说：

- 模型调用只是中心动作之一
- harness 决定这个动作发生在什么边界内
- 同样的模型，放在不同 harness 里，会得到不同的稳定性、可控性与安全性

所以 harness 更适合被理解为 runtime order layer，而不是外围工程杂项。

## What a harness actually governs

一个 harness 至少在治理几类关键问题：

- orchestration loop 如何组装输入、调用模型、执行工具并判断停止
- 上下文如何被组织、压缩和恢复
- 工具如何被暴露、路由和限制
- 输出如何被解析成最终回答、工具调用或 handoff
- 权限边界如何被设置，并在何时交还给人类决策
- 错误如何被分类成可重试、可由模型修正、需要用户介入或直接暴露
- verification loop 如何把测试、视觉检查或 evaluator 的反馈送回系统
- 子任务是否应该被委派，以及如何隔离执行环境
- 状态如何被记录、持久化和重建

把这些放在一起看，harness 的职责就不只是“把模型接到工具上”，而是在塑造 agent 的可运行秩序。

这里还需要补一个经常被低估的点：harness 不只是在提供 capability surface，也是在决定 action 是否可以真正落地。

也就是说，系统设计里至少存在两层不同问题：

- 模型或 router 觉得“下一步应该调用哪个工具”
- 系统是否允许这个动作在当前策略边界内真正发生

前者更接近 capability selection，后者更接近 pre-action authorization。

如果这两层没有被明确分开，很多所谓的 agent safety 就会退化成“希望模型自己别做错事”。

## Why harness complexity matters

这也解释了为什么很多 agent 系统的复杂度，不在核心 loop 本身，而在 loop 外面的约束结构。

真正影响系统质量的，常常是这些外围机制是否成立：

- 能不能把上下文压到足够小但不丢掉任务边界
- 能不能让工具在正确边界内被调用
- 能不能把高风险动作重新交给人判断
- 能不能用 [[wiki/concepts/Verification Loop]] 在错误扩散前获得外部反馈
- 能不能在需要时隔离子任务与执行环境
- 能不能在会话中断之后恢复足够连续的状态

因此当我们评估一个 agent system 时，不能只问“模型强不强”，还要问：

- 这个 harness 在放大什么
- 它在约束什么
- 它在保护什么
- 它在失败之后如何恢复

## Reasoning implication

如果把 reasoning 优先理解为 latent-state trajectory 的形成，而不是表面 chain-of-thought 的展开，那么 harness 的位置会变得更关键。

因为真正决定 agent 是否稳定工作的，往往不是模型单次“想得好不好”，而是外围秩序是否把 reasoning 的形成条件塑好了，例如：

- 上下文如何被组织与压缩
- 工具如何被暴露与路由
- 权限边界如何被逐步控制
- 状态如何被记录、恢复与重建

从这个角度看，harness 不是外围工程细节，而是塑造 reasoning、稳定性与可控性的运行层。

## Design dimensions

从当前材料往上抽，可以把 harness 看成几个设计维度的交点：

- boundary design：系统如何决定什么能做、什么要停下来问人
- contextual adaptability：系统如何在上下文受限时继续工作
- capability amplification：系统如何通过 skill / hook / plugin / MCP 等接口放大能力
- pre-action authorization：系统如何在动作执行前用独立于模型输出的策略层做 allow / deny 判定，并保留可审计记录
- execution reliability：系统如何把动作做成可恢复、可隔离、可连续的执行过程
- human decision authority：系统如何保留人类在关键节点上的最终判断权
- information density preservation：系统如何用工具最小化、分层记忆和压缩机制，把有限上下文留给真正影响下一步决策的信息
- cache stability：系统如何让静态 prompt 前缀、tool schema、project context 和 model choice 在会话中保持稳定，从而复用 [[wiki/concepts/Prompt Caching]]

这些维度并不是 Claude Code 独有的实现细节，而更像 agent system design 的一组通用观察面。

## Density-preserving harness

[[wiki/sources/GenericAgent Paper Source Guide]] 补强了 harness 的另一个面向：harness 不只是把模型接到工具和权限系统上，也是在塑造模型每一轮能看到的信息环境。

GenericAgent 的做法是把四件事放在同一个设计原则下：

- 用 minimal atomic tool set 降低工具 schema 常驻上下文的成本
- 用 hierarchical on-demand memory 让深层事实和 SOP 需要时再进入上下文
- 把成功轨迹压缩成 SOP 和可执行代码，而不是复放原始历史
- 用 truncation、compression、message eviction 和 working-memory anchor 控制长任务中的历史膨胀

这说明 harness 的质量可以用一个新问题来追问：它是在提高 [[wiki/concepts/Context Information Density]]，还是只是在堆更多可见能力？ ^[inferred]

## Cache-stable harness

[[wiki/sources/Prompt Caching Claude Code Case Study Source Guide]] 给 harness 增加了一个更偏 runtime economics 的维度：长时 agent 不只要管理上下文质量，还要管理哪些上下文能作为稳定前缀被复用。

这会把一些看似无害的实现细节变成系统约束：

- system prompt 里注入时间戳，会让每一轮都变成不同前缀
- tool schema 序列化顺序不稳定，会破坏缓存命中
- 会话中途添加、删除或修改 tool definition，会让后续 token 重新计费和重算
- 中途切换 model，会失去 model-specific cache

因此 harness 不能只问“这一轮需要什么信息”，还要问“哪些信息应该稳定地留在前缀，哪些变化应该追加到 suffix”。

一个更稳的做法是：把状态更新、提醒和压缩请求追加成新的消息，而不是改写 system prompt 或工具定义。这样可以同时保留 [[wiki/topics/Context Management]] 的语义连续性和 [[wiki/concepts/KV Cache]] 的可复用性。

Thariq's Claude Code article adds two concrete harness patterns:

- Treat mode transitions as stable tool calls, such as plan-mode entry and exit, instead of mutating the upstream prompt.
- Use deferred tool loading: keep stable lightweight tool stubs in the prefix, then let a tool-search mechanism load full schemas only when needed.

这两个模式背后的同一条原则是：capability surface 可以按需展开，但 prefix shape 应该尽量稳定。

## Design consequence

这也意味着，不存在一个脱离部署环境的唯一正确 harness。

本地 CLI agent、托管式 agent、企业内部受控系统、带强沙箱约束的 workflow runner，都会把这些维度组合成不同答案。

所以讨论 harness 时，不能只问“它有哪些功能”，还要问“它在什么环境里工作”。

## Harness as product surface

[[wiki/sources/Agent Harness Anatomy Source Guide]] adds a useful framing: the harness is not a commodity wrapper around the model. It is part of the product behavior surface.

The same base model can behave differently when the surrounding harness changes:

- different tool schemas alter the action space
- different memory and context policies alter what the model can use
- different error handling policies determine whether failures become recoverable observations
- different guardrails and permissions determine whether proposed actions can actually execute
- different verification loops determine whether work is checked before it compounds

This makes harness design an architectural bet, not just application plumbing. ^[inferred]

## Governance implication

从 `Before the Tool Call` 这类材料往上抽，一个更稳定的判断是：harness 的安全边界不应只寄托在 prompt、模型自觉或人工事后复盘上。

更强的系统会把一部分关键控制前移到执行前：

- 在动作真正发生前检查是否满足 policy
- 把 capability routing 和 permission gating 区分开
- 让高风险动作有独立于模型文本输出的拦截层
- 在需要时留下可验证、可回溯的审计记录

这不意味着所有 agent 都必须采用重型 policy engine，而是说明：只要系统开始拥有真实工具能力，harness 就不能只被理解为“接线层”，还必须被理解为 governance layer。

## Upstream concepts and topics

- [[wiki/concepts/Agent]]
- [[wiki/concepts/Agent Tool]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/Tool Routing]]

## Peer topics

- [[wiki/topics/AI Skills Workflow]]

## Downstream synthesis

- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/syntheses/Agent System Design Space]]

## Source notes

- [[wiki/sources/LLM Reasoning Is Latent, Not the Chain of Thought Source Guide]]
- [[wiki/sources/Dive into Claude Code Source Guide]]
- [[wiki/sources/Before the Tool Call Source Guide]]
- [[wiki/sources/Agent Harness Qiaomu Article Source Guide]]
- [[wiki/sources/Managed Agents Source Guide]]
- [[wiki/sources/GenericAgent Paper Source Guide]]
- [[wiki/sources/Prompt Caching Claude Code Case Study Source Guide]]
- [[wiki/sources/Agent Harness Anatomy Source Guide]]

## Navigation

- [[wiki/maps/AI Map]]
