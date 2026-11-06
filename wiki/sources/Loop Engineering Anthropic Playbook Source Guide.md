---
title: "Loop Engineering: The Anthropic Playbook Source Guide"
category: sources
tags:
  - agents
  - harness
  - workflow
  - ai-coding
  - verification
aliases:
  - Loop Engineering Anthropic Playbook
  - Loop Engineering IEEE Working Note
relationships:
  - target: "[[wiki/concepts/Loop Engineering]]"
    type: explains
  - target: "[[wiki/concepts/Agent Loop Human Judgment Positions]]"
    type: supports
  - target: "[[wiki/concepts/Verification Loop]]"
    type: supports
sources:
  - https://drive.google.com/file/d/1qzKI4DKnyHRpXK1J3ATPqwaqLc0iNu-M/view
source_url: https://drive.google.com/file/d/1qzKI4DKnyHRpXK1J3ATPqwaqLc0iNu-M/view
created: 2026-11-07T01:51:41+0800
updated: 2026-11-07T01:51:41+0800
summary: >-
  实践型工作笔记：把 Loop Engineering 拆成五个运行动作与六类实现部件，并以独立评价器、持久状态、预算上限和人工检查点约束无人值守 Agent。
provenance:
  extracted: 0.76
  inferred: 0.22
  ambiguous: 0.02
base_confidence: 0.58
lifecycle: draft
lifecycle_changed: 2026-11-07
tier: supporting
---

# Loop Engineering: The Anthropic Playbook Source Guide

> Source: [Loop Engineering: The Anthropic Playbook for Designing Systems That Prompt Your Agents](https://drive.google.com/file/d/1qzKI4DKnyHRpXK1J3ATPqwaqLc0iNu-M/view)

这份 2026 年工作笔记把 Loop Engineering 定义为：不再逐次提示 Agent，而是设计一个能自动发现任务、执行、检查、保存状态并再次启动的系统。文档是 HuaShu 对 Addy Osmani 开放指南的独立会议论文式重排，不是 Anthropic 官方论文或对照实验。

## Problem

文档处理的核心问题不是怎样让 Agent 多生成代码，而是怎样让无人值守的多轮执行保持可停止、可验证和可治理。

具体问题包括：

- 人从逐轮执行位置退出后，应当保留哪些判断位置？
- 一次 Agent 运行怎样变成能跨轮次积累进展的循环？
- 同一系统既生成又自评时，如何避免持续自我认可？
- 自动化如何同时放大产出、错误、认知债务与 Token 成本？

## Assumptions

文档的论证依赖以下前提：

- Coding Agent 已能在无人值守时完成部分非平凡任务。
- 调度能力和单次运行成本已越过实用阈值。
- 生成者自评存在系统性宽松偏差。
- 独立评价器比自我批评的生成器更容易校准。
- 跨轮状态写入外部介质后，循环才能累积进展。
- 当生成接近廉价时，工程判断会成为更稀缺的资源。

前五项可通过成功率、缺陷检出率、重复劳动率和成本对照检验。最后一项是文档的经济与职业判断，现有案例不足以单独证成。

## Core Concepts

### Four engineering layers

1. Prompt Engineering 管一次表达：告诉模型什么。
2. Context Engineering 管一次窗口：让模型此刻看到什么。
3. Harness Engineering 管一次运行：工具、动作和完成条件。
4. Loop Engineering 管跨轮系统：自动再次运行并把前一轮结果带入下一轮。

### Five operational moves

| 动作 | 回答的问题 | 缺失后的失败模式 |
| --- | --- | --- |
| Discovery | 本轮做什么？ | Blind loop：仍由人每天挑任务 |
| Handoff | 任务交给谁，怎样隔离？ | Tangled loop：并行修改彼此冲突 |
| Verification | 做对了吗，谁能否决？ | Nodding loop：生成者持续认可自己 |
| Persistence | 下一轮怎样记得？ | Amnesiac loop：重复发现或重复执行 |
| Scheduling | 何时再次运行？ | Manual loop：仍靠人记得启动 |

这五项构成文档选定粒度下的功能循环。它们分别承担选择、执行边界、评价、记忆和再次触发。

### Six implementation parts

| 部件 | 主要职责 | 对应动作 |
| --- | --- | --- |
| Automations | 定时或事件触发 | Scheduling |
| Worktrees | 隔离并行工作目录 | Handoff |
| Skills | 固化项目知识，减少重复解释 | Discovery |
| Connectors | 连接 issue tracker、Slack、API 等外部系统 | Discovery / Persistence |
| Sub-agents | 分开生成者与评价者 | Verification |
| Memory | 保存上下文窗口之外的状态 | Persistence |

五个动作与六个部件不是一一映射。Discovery 同时使用 Skills 和 Connectors；Connectors 又跨越发现与持久化，所以实现清单比功能动作多一项。

## Reasoning Chain

文档的主推理链可以压缩为：

1. 单次 Agent 运行已经足够可靠且便宜。
2. 调度移除每轮等待人的停顿，单次运行因此变成多轮自治。
3. 多轮自治会让错误进入持久状态，并在后续轮次成为既定事实。
4. 错误损失随存活轮次和扩散范围增长。^[inferred]
5. 系统因此需要独立评价器、可执行门禁和显式停止条件。
6. 生成供给激增后，工程价值转向方向选择、证据判断与否决权。

可以用一个近似式表达第 4 步：^[inferred]

$$
\text{错误损失} \approx \text{单轮影响} \times \text{错误存活轮次} \times \text{扩散范围}
$$

## Change Mechanisms

### Generator–evaluator separation

生成者刚完成输出时，其上下文包含支持当前方案的整条理由链。文档认为，这种“自我说服”使同一 Agent 难以严格否决自己。独立评价器应当：

- 默认怀疑结果，而不是默认通过；
- 执行测试、点击界面和检查真实行为，而不只阅读代码；
- 在可能时使用不同模型，减少共享盲点；
- 根据显式完成条件给出 PASS 或 REJECT；
- 把拒绝理由反馈给下一轮执行。

结构分离不自动等于认知独立。若生成者和评价器共享模型、训练偏差、数据盲区或错误规格，两者仍可能共同通过错误结果。^[inferred]

### Deterministic gates around probabilistic work

Stripe Minions 案例把规则明确的步骤留给确定性程序：编排器收集上下文，LLM 写代码，linter 作为不可跳过的门禁，硬编码步骤完成提交，最后由人审核 PR。文档据此主张，可靠性更依赖约束质量，而不是只依赖模型规模。

### Two reinforcing paths

安全路径从小循环开始：先让一个任务端到端运行，再证明评价器能抓到真实错误，最后扩大任务发现范围和并行度。

失控路径由四项成本相互强化：

1. 未验证输出累积为 verification debt。
2. 人的心智模型落后于代码，形成 comprehension rot。
3. 理解下降使人更容易放弃独立判断，形成 cognitive surrender。
4. 无人看守和无限重试造成 token blowout，并生成更多待验证输出。

## Why Five Moves but Not Exactly Six Parts

五动作具有较强的“删除测试”：删掉任何一项，都会出现文档明确命名的失败模式。因此它可视为软件 Agent 场景中的近似最小操作集。^[inferred]

但它不是形式化证明出的唯一最小基：

- Handoff 把任务交接、隔离和执行揉在一起。
- Scheduling 可以被视为状态转换条件，而不是独立动作。
- Observe、Plan、Escalate、Recover、Budget 和 Learn 都可以在更细粒度模型中单列。
- 如果任务由外部队列指定，Discovery 不一定由循环自身承担。

六部件更明显是经验性参考架构：

- Worktree 只适用于需要 Git 并行隔离的场景。
- Connector 对纯本地任务不是必要部件。
- Skill 可由策略服务、数据库或配置替代。
- Sub-agent 可由确定性检查器、模拟器或人工 reviewer 替代。
- Automation 可以是 cron、事件总线、队列消费者或状态机。

文档后面的首个循环检查表又加入 Token cap 和 Human review。这反向说明，六部件只覆盖运行骨架，没有覆盖全部治理。^[inferred]

更抽象的功能模型可以压成四类：Perceive and Select、Act、Evaluate、Update State；Trigger 作为状态转移条件把下一轮接回来。^[inferred] 五动作更适合工程搭建，四类模型更接近跨工具形式抽象。

## Predictions

这套论证导出以下可观察预测：

- 团队时间会从编写转向审核、评测和评价器设计。
- 强约束的较弱模型可能胜过弱约束的较强模型。
- 缺少独立评价器的长期循环会出现异常低的拒绝率。
- 自治轮次增加而门禁不增强时，错误爆炸半径会扩大。
- 成熟系统会组合本地快循环与云端慢循环。^[inferred]
- 工程师差距会更多由判断质量决定，而不是机械实现速度。
- 人工检查点不会因循环变可靠而自然失去价值；它是维持可靠性的结构。

最直接的检验是比较“强生成器 + 弱评价器”与“普通生成器 + 强评价器”的缺陷逃逸率、返工率和成本。^[inferred]

## Evidence Boundary

> [!warning] 实践证据，不是因果证明
> 文档主要使用从业者观察、架构案例与规范性推理。Stripe 每周合并 1,300 多个机器生成 PR 的案例能证明系统可以规模化运行，但不能单独证明五动作是唯一完备集，也不能证明独立评价器在所有任务上优于自评。

仍缺少四类数据：

- 自评与独立评价的缺陷检出对照；
- 不同门禁组合的消融实验；
- 人工审核成本与吞吐变化；
- 长期使用后工程师代码理解度的变化。

## Related

- [[wiki/concepts/Loop Engineering]]
- [[wiki/concepts/Agent Loop Human Judgment Positions]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Event-Driven Agent Loop]]
- [[wiki/concepts/Cognitive Debt]]
- [[wiki/concepts/Attention as the Scarce Resource]]
- [[wiki/topics/AI Harness]]
- [[wiki/sources/The Art of Loop Engineering Source Guide]]
