---
title: Coding Is Not Solved Source Guide
type: source
status: draft
category: sources
tags: [article, ai-coding, software-engineering, reliability, responsibility]
aliases:
  - Coding is NOT solved
  - 编码尚未被解决
  - 可问责的软件工程尚未被解决
relationships:
  - target: "[[wiki/concepts/Cognitive Debt]]"
    type: related_to
  - target: "[[wiki/concepts/Verification Gap]]"
    type: related_to
  - target: "[[wiki/concepts/Accountability]]"
    type: related_to
  - target: "[[wiki/concepts/Attention as the Scarce Resource]]"
    type: related_to
sources:
  - https://blog.alexewerlof.com/p/coding-is-not-solved
  - conversation:2026-10-17
created: 2026-10-17T00:41:23+0800
updated: 2026-10-17T00:41:23+0800
summary: >-
  Alex Ewerlöf 论证 AI 已降低代码生成成本，却尚未解决理解、验证、非功能保证、持续演化与人类问责；软件价值因此从产量迁移到可验证的责任系统。
provenance:
  extracted: 0.78
  inferred: 0.18
  ambiguous: 0.04
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-17
tier: supporting
---

# Coding Is Not Solved Source Guide

> Source: Alex Ewerlöf, [Coding is NOT solved](https://blog.alexewerlof.com/p/coding-is-not-solved)

## What It Covers

这篇文章反驳“coding is solved，工程师今后只需要品味”的流行叙事。作者不否认 AI 已经能快速生成可运行代码，也不否认 harness、测试、Skills、Agent、MCP、状态机和记忆技术取得的进展；他的核心区分是：**生成代码的成本下降，不等于理解、验证、维护、恢复和承担后果的成本消失。**

文章最强的命题可以改写为：AI 已经部分解决狭义代码合成，但尚未解决可问责的软件工程。^[inferred]

## Assumptions

文章依赖以下假设：

1. 软件的大部分长期成本来自维护、可靠性、安全、扩展、合规和故障响应，而不是第一次生成代码。
2. 代码仍是系统实际行为最准确的事实来源；模型对代码的解释不能替代人对系统的理解。
3. 问责要求理解：如果一个人无法解释系统为何这样工作，也无法在失败时定位和修复，就不能形成完整所有权。
4. 当前 LLM 的核心仍是概率生成；compiler、tests、linters、tools、memory 和 harness 能筛错，却不会把模型本身变成确定性逻辑机。
5. 是否需要逐步理解和审查代码取决于风险容忍度，而风险容忍度又受规模、韧性、故障隔离和可观测性影响。
6. 模型能力与可用上下文不会必然线性增长；不能把“明年再强百倍”当作工程规划前提。
7. 当生成速度快于人类理解与验证速度时，更多代码会扩大 [[wiki/concepts/Verification Gap|验证鸿沟]]、安全攻击面与 [[wiki/concepts/Cognitive Debt|认知债务]]。

作者进一步判断，完全不再阅读代码至少还缺两类突破：模型能够在真实工作中稳定实时学习，以及能够可靠进行抽象、符号和逻辑推理。这个“两次革命”判断是技术预测，而不是文章已经证明的结论。^[ambiguous]

## Core Problem

表面问题是“AI 能否写出代码”，深层问题则是：

> 当代码生成成本趋近于零时，谁来理解系统、验证系统、处理异常，并为结果承担责任？

这个问题包含四层：

| 层次 | 要回答的问题 |
|---|---|
| 能力 | AI 能否产出能运行的代码？ |
| 可靠性 | 产物能否持续满足功能需求与非功能需求？ |
| 认知 | 负责系统的人是否仍然理解它？ |
| 制度 | 系统失效时，谁拥有决策权并承担后果？ |

“coding is solved”通常只回答第一层，而专业软件的成本与风险主要集中在后三层。

## Conceptual Structure

文章可以压缩为五个相互连接的层次：

| 层次 | 核心张力 | 作者的判断 |
|---|---|---|
| 生成 | 人写代码 vs AI 生成代码 | AI 已显著降低生成成本 |
| 认识 | 理解系统 vs 接受 AI 解释 | 解释不能替代人的系统模型 |
| 工程 | 功能可用 vs 长期可靠 | Demo 通过不代表安全、可维护、可扩展 |
| 组织 | 委派任务 vs 转移问责 | 可以委派生成，不能把后果转给 AI |
| 经济 | 低成本产出 vs 高保证服务 | 软件价格会分化，质量与 SLA 构成溢价 |

作者把软件所有权拆成三个支柱：

1. **Knowledge**：知道要解决什么问题、系统怎样工作、能力与限制在哪里。
2. **Mandate**：拥有做决定的授权，不必为每一步寻找外部许可。
3. **Accountability**：失败时由自己值班、解释并承担后果。

三者缺一，所有权都会断裂。AI 可以执行任务，却不能承担法律、职业和社会后果；因此它不能成为问责链的终点。

## Reasoning Flow

1. **先承认 AI 的真实能力。** 当前 AI 擅长语言与代码映射、生成、归约、抽取、分类、搜索和多模态转换。
2. **再区分生成与生命周期。** 生成一段代码不等于承担维护、安全、可靠性、扩展和故障恢复。
3. **用风险容忍度划边界。** 个人软件、POC、一次性自动化可以接受更高风险；医疗、金融、航空、制造等领域需要更强保证。作者还列出“武器化 AI”这一特殊情况：不是风险不存在，而是使用者主动把风险指向他人。
4. **解释 AI 为何看起来会写代码。** 模型输出经过编译、测试、lint、工具调用和多轮反馈，最终能力来自随机生成器与确定性筛选器的组合。
5. **把技术问题推进到问责。** AI 不会被罚款、坐牢、解雇或值班；产物出问题时，责任仍回到人和组织。
6. **反驳常见叙事。** 完整规格无法总在事前写出；自然语言含糊冲突；代码量和 PR 数不是进步；管理 Agent 不等于管理可问责的人；“品味”也不足以成为职业护城河。
7. **转向软件经济学。** 即使 AI 产物质量较低，只要足够便宜、快速，在低风险场景中仍然合理；高风险场景则必须为验证、保障和恢复付费。
8. **推出市场与职业变化。** 普通代码生产价格下跌，高质量、可问责且带 SLA 的服务获得溢价，工程师的价值从制造代码迁移到形成理解与保证运行结果。

## Change Mechanisms

### 生成与理解的速度失配

```text
代码生成成本下降
-> 代码数量和变更速度上升
-> 审查能力与理解速度没有同比上升
-> 技术债、认知债和攻击面扩大
-> 故障时缺少系统模型
-> 恢复更慢、责任更模糊、总拥有成本上升
```

这不是“使用 AI 必然降低质量”，而是吞吐量扩大后，验证与理解没有同步扩容的结果。^[inferred]

### 显性错误转为隐性债务

编译错误容易暴露；更危险的是局部能运行、UAT 能通过，但权限过宽、失败路径缺失、外部依赖隐蔽或团队不能解释系统行为。这些风险往往在规模化或事故时才显现。

### 组织激励放大技术缺陷

当管理层用 token、代码行数、PR 数和功能数衡量生产率，团队会最大化生成而不是用户价值与服务水平。模型的随机性经过错误激励后，会变成系统性的质量退化。^[inferred]

### 软件市场两极分化

作者提出两条商业路径：

1. 接受价格坍缩，用更多 AI 提供便宜但保证较弱的软件。
2. 保持较高价格，用经验丰富的人类、验证体系和 SLA 提供可问责的质量。

因此 SaaS 的长期价值可能从“拥有一套代码”迁移到“持续承担可用性、恢复与责任”。^[inferred]

### 人机反馈形成两种循环

```text
良性：理解问题 -> AI 加速实现 -> 人验证 -> 更新系统模型 -> 更有效地使用 AI
恶性：跳过理解 -> AI 大量生成 -> 无力审查 -> 依赖 AI 解释 -> 更不理解系统
```

决定长期结果的不是是否使用 AI，而是使用后人的理解与否决能力增强还是萎缩。^[inferred]

## Where AI Fits and Does Not Fit

作者认为当前 AI 适合：

- 自然语言、代码和结构化数据之间的映射与转换；
- 文本、图像、视频、音乐的生成、扩写与整合；
- 总结、抽取、分类与异常发现；
- 语义搜索、探索式研究、检测与切块。

不适合或需要额外谨慎的场景包括：

- 把法律问责隐含地交给 AI；
- 低功耗嵌入式场景中没有经济必要的 AI；
- 涉及 PII、知识产权或高权限操作的云端处理；
- 把大量上下文一次性扔给模型的 kitchen-sink 用法；
- 已有 regexp、SQL 或普通函数能更快、更便宜、更可预测完成的任务；
- 需要明确伦理榜样与数据权利边界的场景。

作者并非主张永远逐行阅读所有代码：理解与审查投入应随风险、规模、隔离、韧性和可观测性变化。

## Impacted Fields

| 领域 | 当前影响 |
|---|---|
| 软件工程与代码审查 | 从语法和风格转向需求一致性、边界、失败模式、权限与认知负担 |
| SRE 与平台工程 | 可观测性、隔离、灰度、回滚、限流和 SLO/SLA 成为 AI 生成吞吐的承接结构 |
| 工程管理 | 需要明确谁批准、谁理解、谁值班、谁承担事故；“使用 AI”不能本身成为目标 |
| SaaS 定价与采购 | 客户购买的重点从功能表转向保证、责任、数据可迁移性与退出成本 |
| Coding Agent 产品 | 竞争从生成量迁移到范围控制、证据链、回滚、权限、成本和理解支持 |
| 安全与隐私 | 依赖引入、Skill/MCP 供应链、云端上下文和高权限自动化风险扩大 |
| 法律与 AI 治理 | 问责链必须落到具体的人或组织，人类在环需要避免沦为审批疲劳下的合规表演 |
| 工程教育与职业 | 基础编码从主要生产手段转成理解与校验手段，AI 部署、质量、可靠性和技术产品角色增加 |

作者预测部分工程师会转向技术产品经理、AI managers、AI deployment engineers 和 AI quality engineers。共同变化是：价值不再来自比 AI 写得更快，而来自定义问题、设计约束、判断结果和承担后果。

## Boundaries and Open Questions

- 文章大量使用事故、社交媒体言论和个人经验，足以表明风险存在，却不能单独证明整个行业的净生产率没有提高。
- “人类犯错更一致”是有用对比，但人也会疲劳、遗忘并受组织激励影响；传统分布式软件也不总是严格确定。更稳的区别是传统代码通常更可复现、可定位，也更容易建立形式约束。^[inferred]
- 标题依赖对 coding 的定义。若 coding 只指明确规格下的代码合成，AI 已解决相当大一部分；若它指持续把不明确问题变成可靠系统，作者的反驳更成立。^[inferred]
- “两次革命”与软件价格必然坍缩都是方向性预测，仍需要长期数据检验。^[ambiguous]
- AI 生成的解释能否帮助偿还认知债，还是只会增加一层未经验证的表示？
- 如何在事故发生前度量团队的理解能力、验证吞吐与问责完整性？

## Related

- [[wiki/concepts/Cognitive Debt]]
- [[wiki/concepts/Verification Gap]]
- [[wiki/concepts/Accountability]]
- [[wiki/concepts/Attention as the Scarce Resource]]
- [[wiki/concepts/Agentic Engineering]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/syntheses/Agentic Engineering × Verification Loop]]
- [[wiki/sources/Coding with AI Source Guide]]
- [[wiki/sources/Skills for the Future Software Profession Paper Source Guide]]
