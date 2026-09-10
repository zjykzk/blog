---
title: The AI-Native SDLC Playbook Source Guide
type: source
status: draft
category: sources
summary: Anthropic 的阶段式 AI-native SDLC 实施指南，用版本化工件、反馈循环、自动门禁和风险分层的人类判断连接计划、设计、构建、测试、部署与维护。
tags: [article, software-engineering, ai-coding, harness, workflow]
sources:
  - https://claude.com/blog/the-ai-native-sdlc-playbook
source_url: https://claude.com/blog/the-ai-native-sdlc-playbook
published: 2026-08-21
created: 2026-09-10T21:22:11+0800
updated: 2026-09-10T21:22:11+0800
aliases:
  - The AI-Native SDLC Playbook
  - AI-Native SDLC
  - Agentic SDLC Playbook
relationships:
  - target: "[[wiki/syntheses/AI Engineering Workflow]]"
    type: related_to
  - target: "[[wiki/topics/AI Harness]]"
    type: uses
  - target: "[[wiki/concepts/Verification Loop]]"
    type: uses
provenance:
  extracted: 0.91
  inferred: 0.07
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-09-10
tier: supporting
---

# The AI-Native SDLC Playbook Source Guide

> Source: Anthropic, “The AI-Native SDLC Playbook,” 2026-08-21, <https://claude.com/blog/the-ai-native-sdlc-playbook>

## Capture Policy

这篇文章是 Anthropic Applied AI 团队面向企业软件交付的官方实施 playbook。它适合保存为一手厂商实践：文章给出了完整的工件链、控制分层、采用依赖、执行样例与衡量指标，但没有提供对照实验或跨组织统计。因而，本页将流程结构作为来源明确陈述的实践方案保留；效率提升、适用范围及厂商产品能力仍按有条件主张处理。

## Central Thesis

文章的起点是：当 Agent 能把构建阶段压缩到小时级时，软件交付的瓶颈会移向构建左侧和右侧——需求澄清、设计、审核、测试、部署和治理。继续沿用按人类产出速度设计的审批与交接流程，会让代码生成速度变成新的排队压力。

AI-native SDLC 因此不是在传统流水线的 Build 阶段加入代码生成，而是重新设计整个生命周期：

- 每个阶段产出一个人和 Agent 都能读取的版本化工件；
- 被接受的工件触发下一阶段，而不是等待一次人工转述；
- 可计算的控制进入测试、hooks、CI、权限和 sandbox；
- 人类判断集中在意图、风险、冲突、例外与生产授权；
- 生产异常重新写成 `intent.md`，进入下一轮交付。

```text
intent.md
  -> spec.md
  -> plan.md
  -> diff + tests
  -> PR + review findings
  -> deployment / incident record
  -> next intent.md
```

这条链同时是 handoff、状态载体和审计轨迹：每个阶段既消费上游承诺，也留下谁提出、谁修改、谁批准以及依据什么继续推进的记录。

## Six-Stage Shift

| Stage | 传统方式 | 文中建议的 AI-native 方式 | 主要工件或证据 |
|---|---|---|---|
| Plan | 经会议、backlog 和转述形成需求 | 发起人与 Claude 澄清问题、结果、用户、系统、约束和开放问题 | `intent.md` |
| Design | 分析与设计由不同角色顺序交接 | Agent 读取 intent，并在安全、品牌、合规、UX skills 约束下生成需求与设计 | `spec.md`、被标出的冲突 |
| Build | 工程师直接从设计进入代码 | 先在只读 plan mode 中检查文件、顺序、风险和证明方法，再批准实现 | `plan.md`、代码 diff |
| Test | QA 在阶段末验证 | 测试、构建、lint、视觉检查持续回流给实现 Agent；配置变化另跑 eval | 测试输出、截图差异、eval 结果 |
| Deploy | 人类逐行审查并周期性治理 | Agent 做分层 review，hooks 和权限执行门禁，人保留关键批准 | PR、review findings、gate verdict |
| Maintain | 人在告警后重新启动流程 | 确定性监控触发只读诊断或受控行动，把发现写回新的 intent | 指标越界记录、incident、`intent.md` |

`intent.md`、`spec.md` 和 `plan.md` 分别承诺不同东西：

- `intent.md` 承诺为什么要改变、想得到什么结果、受什么约束；
- `spec.md` 承诺系统应表现出什么行为，如何处理状态、接口、政策和未决冲突；
- `plan.md` 承诺如何实现，涉及哪些文件、按什么顺序、主要风险是什么、用什么证据证明完成。

它们是职责拆分，不是对 PRD 的简单替代。组织可以继续让 Jira、ServiceNow、Figma 或监管需求系统作为权威记录；最低要求是为每类工件声明唯一 source of truth，并让副本通过记录 ID 与 commit SHA 双向链接。

## The Control Stack

文章把治理从“所有规则都写成提示词”拆成不同强度的控制：

| Layer | 适合承载 | 强制性 |
|---|---|---|
| `CLAUDE.md` | 仓库命令、架构、惯例、常见错误 | 常驻上下文，仍属模型可解释的指导 |
| Skills | 安全标准、API 规范、品牌与合规流程 | 按任务触发的建议性政策 |
| Hooks / tests / CI | 受保护路径、格式、测试、发布批准 | 确定性 allow / ask / block |
| Permissions / sandbox / managed settings | 工具、凭证、网络、插件和 MCP 边界 | Agent 无权绕过的运行时能力边界 |
| Human approval | 产品意图、政策冲突、高风险变更、生产发布 | 最终责任与例外裁决 |

文章明确指出，Skill 只是 advisory control。必须始终成立的政策要有测试、hook、权限或独立 review 作为确定性后盾。这与 [[wiki/concepts/Computational and Inferential Controls]] 的边界一致：能计算的约束应交给机器裁决，不能完全计算的适配性、架构、风险和产品判断要显式交给人或独立 evaluator。^[inferred]

## Three Feedback Horizons

文章实际区分了三种不同时间尺度的反馈：

1. **任务内反馈**：实现 Agent 反复运行测试、构建或截图比较，直到当前修改满足可执行检查。
2. **配置级回归**：当 `CLAUDE.md`、Skill、Hook、模型或 prompt 改变时，用一组真实历史任务运行 continuous eval，避免 Agent 配置退化。
3. **生产回流**：指标越过控制带、事故或安全发现触发诊断；修复后把这一类事故加入 eval，并把较大的问题写成新 `intent.md`。

这使 [[wiki/concepts/Verification Loop]] 不只是“交付前跑测试”，而是连接当前任务、Agent 配置和生产演化的多尺度反馈系统。^[inferred]

## Adoption Dependencies

文章没有要求按 Plan 到 Maintain 线性改造。依赖图把实践分成可独立起步项和后续组合项。

可独立起步的基础包括：

- Capture intent；
- 建立简短、版本化的 `CLAUDE.md`；
- 为当前任务提供本地 feedback loop；
- 建立 hooks；
- 默认先使用 plan mode。

在此之上，再逐步增加：

- Skills 依赖可维护的机构知识和明确 policy owner；
- Subagents 依赖共享上下文、可隔离工具与可重复任务；
- Evals 依赖反馈循环和可重放的真实任务；
- PR review 依赖审查政策、执行证据和职责分离；
- CI/CD 自动行动依赖 PR 门禁、sandbox、短期凭证和可演练 rollback；
- Closing the loop 依赖稳定的生产信号、前述门禁和可重新进入 Plan 的 `intent.md` 格式。

核心顺序不是“先自动化所有阶段”，而是先建立可验证、可阻断、可回滚的边界，再扩大自主行动范围。^[inferred]

## Human Judgment and Risk

文中并未主张取消人类审核，而是改变审核对象。人不需要把同等注意力投入每一行机械改动，而应检查：

- intent 是否值得实现；
- spec 是否忠实于 intent 并解决开放问题；
- plan 是否控制了 blast radius；
- diff 是否符合 plan；
- 证据是否真的证明了行为；
- Auth、PII、Money、合规和生产发布等高风险区域是否获得明确授权。

这种风险分层只有在三个条件成立时才可靠：机器检查覆盖了可执行属性，Agent 不能批准自己的输出，不可逆动作存在独立门禁。否则“把人从逐行 review 中移开”只是在减少可见监督。^[inferred]

## Measurement Model

每项 play 都给出 leading 与 lagging indicator。可归纳为四类：

- **交接速度**：首次对话到 `intent.md`、intent 到 spec、plan 批准到合并、首次 review 时间；
- **返工与一致性**：构建开始后的 spec 修改、实现轮次、diff 与 plan 的偏离；
- **验证质量**：first-pass CI、eval pass rate、生产事故转为 eval 的时间；
- **运行结果**：DORA 指标、逃逸缺陷、重复事故、门禁违规、有效发现转为已合并修复的比例。

这些指标是评估框架，不是文章已经证明的效果。真正采用时应先记录现状基线，再判断 AI-native 改造是否只是移动成本，还是同时改善了吞吐、质量和风险。^[inferred]

## Evidence and Applicability Limits

- “Code is no longer the bottleneck” 是条件性前提。对高不确定研究、遗留集成、复杂迁移或验证成本远高于生成成本的系统，Build 仍可能是约束。
- 文章来自 Claude 产品提供方，示例和控制面高度依赖 Claude Code、Claude Security、Claude Tag 及其 managed settings。通用原则可以迁移，具体命令和能力必须按当前产品文档验证。
- 效率与质量指标主要说明“应该测什么”，没有提供跨团队对照数据。
- Agent 生成的测试可能与代码共享同一误解；高风险验收需要独立于生成器的证据、职责分离和 rollback。
- 版本化 Markdown 提高可读性与审计性，但不会自动成为组织的法定或业务 source of truth。
- 自动闭环依赖低噪声信号、可逆动作、明确 ownership 和分级权限；这些条件不成立时，自动化会放大错误或告警噪声。

## Integration Decisions

本来源不再派生一组新的 `AI-Native SDLC` 子概念页，因为相关稳定概念已由现有页面承载：

- [[wiki/syntheses/AI Engineering Workflow]] 吸收版本化工件链与阶段触发；
- [[wiki/topics/AI Harness]] 吸收指导、建议性政策、确定性门禁和人类批准的控制分层；
- [[wiki/concepts/Verification Loop]] 吸收任务、配置、生产三个反馈时间尺度；
- [[wiki/concepts/Executable Specification]] 保持独立：文中的 `spec.md` 可以包含可执行规格，但两者不是同义词；
- [[wiki/sources/Humans and Agents in Software Engineering Loops Source Guide]] 提供互补视角：人从逐件修补产物转向设计和治理循环。

## Open Questions

- 什么条件足以证明某个团队的主要瓶颈已经从 Build 转移到 Plan、Review 或 Deploy？
- `intent.md`、PRD、Jira 与监管记录并存时，如何避免双重 source of truth？
- 哪些 review 判断可以稳定编码成检查或 rubric，哪些必须长期保留人工责任？
- continuous eval 应怎样抽样真实任务，才能避免只优化历史分布？
- 生产信号写回 `intent.md` 前需要怎样的去噪、聚类和责任归属？

## Related

- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Executable Specification]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/concepts/Feedforward and Feedback Controls]]
- [[wiki/sources/Humans and Agents in Software Engineering Loops Source Guide]]
- [[wiki/sources/Harness Engineering Source Guide]]
- [[wiki/sources/Structured-Prompt-Driven Development Source Guide]]
