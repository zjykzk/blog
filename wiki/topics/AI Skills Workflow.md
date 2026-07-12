---
title: AI Skills Workflow
type: topic
status: seed
category: topics
summary: AI Skills Workflow treats skills as reusable workflows that gather, order, persist, and reload context for more stable agent behavior.
sources:
  - https://x.com/trq212/status/2033949937936085378
  - https://martinfowler.com/articles/reduce-friction-ai/knowledge-priming.html#ThisPatternInLattice
  - https://martinfowler.com/articles/reduce-friction-ai/design-first-collaboration.html
  - https://martinfowler.com/articles/reduce-friction-ai/context-anchoring.html
  - https://martinfowler.com/articles/reduce-friction-ai/encoding-team-standards.html
  - https://martinfowler.com/articles/reduce-friction-ai/feedback-flywheel.html
  - https://x.com/GoogleCloudTech/article/2033953579824758855
  - https://lavinigam.com/posts/adk-skill-design-patterns/
  - https://arxiv.org/abs/2604.27488
  - https://x.com/neural_avb/article/2053873358853591435
  - https://arxiv.org/abs/2605.07358v1
  - https://research.perplexity.ai/articles/designing-refining-and-maintaining-agent-skills-at-perplexity
  - https://engineering.block.xyz/blog/3-principles-for-designing-agent-skills
  - https://x.com/trq212/article/2073100352921215386
created: 2026-04-22
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.81
  inferred: 0.18
  ambiguous: 0.01
source_count: 17
updated: 2026-07-04T16:59:13+0800
aliases:
  - skills workflow
  - AI skills
tags:
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

[[wiki/sources/Claude Code Skills Source Guide]] adds a lower-level implementation view from Claude Code practice: a skill can be a folder containing references, scripts, assets, templates, data, configuration, memory, and on-demand hooks, not only a top-level instruction file.

That turns [[wiki/concepts/Agent Skill]] into a context-engineering surface. The skill can keep the always-loaded layer small, then disclose deeper material only when the current task needs it. ^[inferred]

[[wiki/concepts/Knowledge Priming]] adds a concrete example from Lattice: a `knowledge-priming` atom plus a `knowledge-priming-refiner` can interview the user, capture project identity, write it to a versioned file, and let other skills read that context automatically.

This reinforces the local view that skill design is partly context architecture: a skill can decide how project context is gathered, compressed, persisted, and reintroduced before later actions. ^[inferred]

[[wiki/concepts/Design-First Collaboration]] adds a second Lattice example: a `design-first` atom can encode a staged collaboration method, while a `design-blueprint` molecule can load context, walk the design levels, and persist the approved blueprint.

That makes a skill more than an invocation shortcut. It can preserve sequencing discipline, especially when deadline pressure would otherwise collapse design and implementation into one prompt. ^[inferred]

[[wiki/concepts/Context Anchoring]] adds a third Lattice example: a `context-anchoring` atom can create or enrich a living feature document across sessions, so the workflow's decisions and current state survive the chat boundary.

This makes durable intermediate artifacts part of skill design. A skill can decide what should be kept outside the active context and reloaded later, not only what prompt should run now. ^[inferred]

[[wiki/concepts/Encoding Team Standards]] adds a fourth Lattice example: atoms such as `clean-code`, `architecture`, `secure-coding`, and `test-quality` can carry team standards with self-validation checklists, while refiners customize them through guided interviews.

That makes skills a vehicle for executable governance: they can apply shared team judgment consistently instead of relying on whoever happens to know the best prompt. ^[inferred]

[[wiki/concepts/Feedback Flywheel]] adds the fifth Lattice example: skills should help capture observed failures, accepted outputs, review comments, and artifact updates so the next run starts from improved context and standards.

That turns skill design into a maintenance loop. A reusable workflow is not complete if it only executes; it should also make it easy to improve the workflow after real use. ^[inferred]

## Practical pattern

1. 先把任务拆小
2. 对齐需求与现有实现约束
3. 和 AI 讨论方案
4. 把方案压缩成方法论
5. 再固化成 skill

这里还有一个容易被忽略的点：workflow 的价值不只是把步骤写出来，而是在构造一个更容易产生稳定 reasoning 的执行顺序。

这说明 skill / workflow 不是单纯的 prompt 展开器，而是在安排：

- 哪些信息先进入上下文
- 哪些判断先做
- 哪些动作要被隔离出去
- 哪些中间结果要被压缩后再回流
- 哪些 references / scripts / assets 该按需展开，而不是一开始全塞进上下文

[[wiki/concepts/Agent Skill Design Patterns]] adds five concrete workflow shapes for this arrangement: Tool Wrapper controls when domain knowledge enters context, Generator controls output structure, Reviewer controls evaluation, Inversion controls when the agent is allowed to ask versus act, and Pipeline controls ordered stages with gates.

This turns “write a skill” into a design choice about failure mode: missing domain knowledge, unstable output, weak review, premature assumptions, or skipped process steps each calls for a different skill shape. ^[inferred]

## Evaluation-driven maintenance

[[wiki/concepts/Skill Self-Evolution]] adds an explicit maintenance loop to this workflow. After a skill is written, the next question is not only whether it is reusable, but whether its capability boundaries have been probed with standard, advanced, and edge-case tasks.

The Skills-Coach paper suggests a workflow where generated tasks, comparative execution, and traceable scoring decide which instruction or code changes are retained. That turns skill maintenance into a measured feedback loop rather than ad hoc prompt polishing. ^[inferred]

A practical implication for wiki skill authoring is that a strong skill should make its own evaluation surface visible: expected inputs, outputs, failure modes, examples, constraints, and verification checks should be concrete enough for future tests to be generated. ^[inferred]

## Lifecycle Architecture

[[wiki/sources/Agent Skills Survey Paper Source Guide]] turns the workflow view into a full lifecycle:

1. **Representation**: a skill is packaged as a root instruction document, optional auxiliary resources, and trigger or applicability conditions.
2. **Acquisition**: skills can come from expert writing, execution traces, current task requirements, or external corpora.
3. **Retrieval and selection**: the system must find candidate skills, then decide which one or which composition should run under current state, cost, latency, safety, and user constraints.
4. **Evolution**: deployed skills need revision, validation, policy coupling, repository governance, drift handling, rollback, and retirement.

This adds a useful test for workflow design: a strong skill is not finished when it first works. It should expose enough metadata to be found, enough boundaries to be selected safely, enough evidence to be evaluated, and enough versioning context to be changed or retired later. ^[inferred]

[[wiki/sources/COLLEAGUE.SKILL Paper Source Guide]] adds a person-grounded lifecycle layer. When a skill is distilled from human traces, the workflow must separate capability from bounded behavior, expose provenance and source limits, allow natural-language correction, preserve rollback points, and support deletion or controlled distribution.

This makes governance part of skill workflow design. A human-trace skill is not mature merely because it sounds like the source person; it must make the extracted craft inspectable, editable, and bounded against identity replacement. ^[inferred]

## Reasoning implication

如果把 reasoning 看成 latent-state trajectory 的形成，那么 workflow 设计的意义就不只是“可复用”，而是“可稳定触发”。

同样一组能力：

- 顺序不同
- 边界不同
- 压缩点不同
- 子任务隔离方式不同

最后形成的系统质量会明显不同。

所以 workflow 设计其实在回答一个更深的问题：我们是在怎样安排一个 agent 的思考条件，而不只是安排它的执行步骤。

## Workflow Catalyst Arc

[[wiki/sources/Designing Refining and Maintaining Agent Skills at Perplexity Source Guide]] adds a useful distinction between one-shot tools and workflow catalysts.

[[wiki/sources/Block Agent Skills Design Principles Source Guide]] independently names this as "design for the arc." Block's Repo Readiness example starts with a deterministic score, but the skill is valuable because the score becomes conversational context for explanation, AGENTS.md drafting, remediation, and re-running the check.

A one-shot tool creates a process breakpoint: it emits a report, JSON payload, check result, or draft, then leaves the human to bridge the next step. A workflow-catalyst skill turns that output into the agent's next context input. Diagnosis can feed repair planning; readiness checks can feed `AGENTS.md` drafting; repeated review failures can feed new gotchas, tests, scripts, or guardrails.

This changes the design target from “can the agent run the helper?” to “does the helper create the next action arc?” A strong skill therefore designs the handoff between deterministic execution and LLM interpretation: scripts provide stable observations, while the model explains what those observations imply and chooses the next bounded action. ^[inferred]

The practical workflow arc is:

1. trigger the skill from a real task situation;
2. load the smallest useful context;
3. run deterministic scripts or mandatory checks where sameness matters;
4. let the LLM interpret results under the skill's constraints;
5. produce the next artifact, plan, code change, question, or verification step;
6. feed the outcome back into gotchas, evals, references, or harness rules when it reveals a reusable pattern. ^[inferred]

## Unknown Discovery Workflow

[[wiki/sources/Agentic Coding Unknowns Source Guide]] adds a user-side workflow for finding the gap between a prompt-map and the real codebase-territory. The source frames this gap as [[wiki/concepts/Agentic Coding Unknowns]]: known knowns, known unknowns, unknown knowns, and unknown unknowns.

The workflow implication is that skillful agentic coding is not only giving clearer instructions. It is choosing the cheapest artifact that can expose the current uncertainty class: blind spot passes for unknown unknowns, brainstorms and prototypes for unknown knowns, interviews for architecture-changing ambiguities, references when language is too weak, implementation notes for mid-run deviations, and quizzes or explainers for post-run understanding.

This turns many “prompting techniques” into a staged discovery system. A skill or session brief can explicitly ask the agent to inspect the territory, surface blind spots, prototype alternatives, interview the user, log deviations, and package what was learned so the next run starts from a better map. ^[inferred]

## Upstream topics

- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/topics/Karpathy Guidelines]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Knowledge Priming]]
- [[wiki/concepts/Design-First Collaboration]]
- [[wiki/concepts/Context Anchoring]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Agent Skill Design Patterns]]
- [[wiki/concepts/Skill Self-Evolution]]
- [[wiki/concepts/Computational and Inferential Controls]]

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
- [[wiki/sources/Claude Code Skills Source Guide]]
- [[wiki/sources/COLLEAGUE.SKILL Paper Source Guide]]
- [[wiki/sources/ADK Skill Design Patterns Source Guide]]
- [[wiki/sources/Skills-Coach Paper Source Guide]]
- [[wiki/sources/SkillOS Source Guide]]
- [[wiki/sources/Designing Refining and Maintaining Agent Skills at Perplexity Source Guide]]
- [[wiki/sources/Block Agent Skills Design Principles Source Guide]]
- [[wiki/sources/Agentic Coding Unknowns Source Guide]]
