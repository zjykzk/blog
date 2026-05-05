---
title: AI Skills Workflow
type: topic
status: seed
category: topics
summary: AI Skills Workflow treats skills as reusable workflows that gather, order, persist, and reload context for more stable agent behavior.
sources:
  - https://martinfowler.com/articles/reduce-friction-ai/knowledge-priming.html#ThisPatternInLattice
  - https://martinfowler.com/articles/reduce-friction-ai/design-first-collaboration.html
  - https://martinfowler.com/articles/reduce-friction-ai/context-anchoring.html
  - https://martinfowler.com/articles/reduce-friction-ai/encoding-team-standards.html
created: 2026-04-22
base_confidence: 0.70
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.78
  inferred: 0.22
  ambiguous: 0.0
source_count: 7
updated: 2026-05-05T17:45:00+08:00
aliases:
  - skills workflow
  - AI skills
tags:
  - ai
  - skills
  - workflow
---

# AI Skills Workflow

当前 source notes 里已经出现了一个很清楚的 workflow 雏形：

- 任务拆解要足够小
- 先对齐需求和现有代码口径，再做设计
- 写 skill 时，可以先和 AI 讨论出解决方案
- 再让 AI 把方案整理成可复用的方法论
- 最后再输出成 skill

## Why it matters

这说明 skill 不是“把 prompt 存起来”，而是把一次有效协作抽成稳定工作流。

[[wiki/concepts/Knowledge Priming]] adds a concrete example from Lattice: a `knowledge-priming` atom plus a `knowledge-priming-refiner` can interview the user, capture project identity, write it to a versioned file, and let other skills read that context automatically.

This reinforces the local view that skill design is partly context architecture: a skill can decide how project context is gathered, compressed, persisted, and reintroduced before later actions. ^[inferred]

[[wiki/concepts/Design-First Collaboration]] adds a second Lattice example: a `design-first` atom can encode a staged collaboration method, while a `design-blueprint` molecule can load context, walk the design levels, and persist the approved blueprint.

That makes a skill more than an invocation shortcut. It can preserve sequencing discipline, especially when deadline pressure would otherwise collapse design and implementation into one prompt. ^[inferred]

[[wiki/concepts/Context Anchoring]] adds a third Lattice example: a `context-anchoring` atom can create or enrich a living feature document across sessions, so the workflow's decisions and current state survive the chat boundary.

This makes durable intermediate artifacts part of skill design. A skill can decide what should be kept outside the active context and reloaded later, not only what prompt should run now. ^[inferred]

[[wiki/concepts/Encoding Team Standards]] adds a fourth Lattice example: atoms such as `clean-code`, `architecture`, `secure-coding`, and `test-quality` can carry team standards with self-validation checklists, while refiners customize them through guided interviews.

That makes skills a vehicle for executable governance: they can apply shared team judgment consistently instead of relying on whoever happens to know the best prompt. ^[inferred]

## Practical pattern

1. 先把任务拆小
2. 对齐需求与现有实现约束
3. 和 AI 讨论方案
4. 把方案压缩成方法论
5. 再固化成 skill

这里还有一个容易被忽略的点：workflow 的价值不只是把步骤写出来，而是在构造一个更容易产生稳定 reasoning 的执行顺序。

也就是说，skill / workflow 不是单纯的 prompt 展开器，而是在安排：

- 哪些信息先进入上下文
- 哪些判断先做
- 哪些动作要被隔离出去
- 哪些中间结果要被压缩后再回流

## Reasoning implication

如果把 reasoning 看成 latent-state trajectory 的形成，那么 workflow 设计的意义就不只是“可复用”，而是“可稳定触发”。

同样一组能力：

- 顺序不同
- 边界不同
- 压缩点不同
- 子任务隔离方式不同

最后形成的系统质量会明显不同。

所以 workflow 设计其实在回答一个更深的问题：我们是在怎样安排一个 agent 的思考条件，而不只是安排它的执行步骤。

## Upstream topics

- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/topics/Karpathy Guidelines]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Knowledge Priming]]
- [[wiki/concepts/Design-First Collaboration]]
- [[wiki/concepts/Context Anchoring]]
- [[wiki/concepts/Encoding Team Standards]]

## Peer topics

- [[wiki/topics/Tool Routing]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Prompt Frequency]]

## Downstream synthesis

- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/syntheses/Agent System Design Space]]

## Navigation

- [[wiki/maps/AI Map]]

## Source notes

- `pages/项目___AI___skills.md`
- `journals/2026_04_01.md`
- [[wiki/sources/LLM Reasoning Is Latent, Not the Chain of Thought Source Guide]]
- [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]]
