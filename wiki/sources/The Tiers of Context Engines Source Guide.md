---
title: >-
  The Tiers of Context Engines Source Guide
type: source
status: draft
category: sources
tags: [article, agents, context, architecture]
aliases:
  - The Delegation Gradient
  - Context Engine Tiers
sources:
  - https://denis2054.github.io/Context-Engineering-for-Multi-Agent-Systems/media/three_tier_context_engines.html
created: 2026-09-09T21:39:46+0800
updated: 2026-09-09T21:39:46+0800
summary: >-
  这张架构图按上下文规划由谁运行，把 Context Engine 分成人工、产品内嵌、平台配置和自建工程四种形态，并以控制、杠杆和集成引力解释选择。
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-09-09
tier: supporting
relationships:
  - target: "[[wiki/syntheses/Agent Knowledge Architecture]]"
    type: related_to
  - target: "[[wiki/syntheses/Agent System Design Space]]"
    type: related_to
---

# The Tiers of Context Engines Source Guide

> Source: [The Tiers of Context Engines](https://denis2054.github.io/Context-Engineering-for-Multi-Agent-Systems/media/three_tier_context_engines.html)

## What It Covers

这张图用“委托梯度”解释 Context Engine：同一种上下文规划能力，可以运行在人脑、通用 AI 产品、企业 Agent 平台或自建工程系统中。差别不主要在模型聪明程度，而在谁负责选择资料、保持记忆、规划工具调用、验证结果和记录执行过程。

图中的标题与文件名使用“三层”表述，但正文实际列出 Tier 3、Tier 2、Tier 1.5 和 Tier 1 四张卡片；Tier 1.5 是介于成品 AI 产品和完全自建系统之间的中间形态。

## Key Points

### Context Engine 的四种运行位置

- **Tier 3 — Human Context Engine**：用户在脑中和浏览器标签页之间完成规划，手工粘贴资料、重述记忆并验证结果。它提供最高的直接控制，但杠杆和规模最低。
- **Tier 2 — Embedded Context Engine**：Claude、ChatGPT、Gemini、Copilot 等产品通过 Projects、Memory、Skills、Connectors、文件摄取和工具循环接管一部分规划。用户仍拥有资料、指令和最终判断。
- **Tier 1.5 — Platform Context Engine**：供应商提供预制的 orchestrator、托管 RAG、连接器、治理、审计和低代码工作流；企业负责数据源、Agent 配置和流程定义。
- **Tier 1 — Engineered Context Engine**：工程团队自建 Planner、Executor、Tracer、Agent Registry、dual RAG、MCP、审核防御和审计链路，把上下文做成类型化 packet、schema 和 trace。

### 从 Prompt 到编译器

原图用一句话压缩了层级跃迁：

> Prompts are sentences. Contexts are documents. Engines are compilers.

Prompt 表达一次要求，Context 汇集完成任务所需的信息环境，Engine 则动态选择、组合和编译知识、规则、工具与状态，使它们进入一次可执行过程。^[inferred]

### “Build or buy” 为什么不够

传统企业软件把选择压成“自己开发还是购买成品”。Tier 1.5 使这条边界变得连续：企业可以买供应商的运行时和治理设施，同时自己配置 Agent、连接内部数据并定义业务工作流。

因此原图把问题改写为：**哪个平台最符合组织已经拥有的 integration gravity？** AWS、Microsoft、Salesforce、ServiceNow、UiPath 或 n8n 等既有生态，会通过身份、权限、数据、流程和审计体系降低某个平台的接入摩擦。

更准确的决策不是一次性选择 build 或 buy，而是逐层决定模型、编排、检索、工具、治理和业务责任分别由谁拥有。^[inferred]

### 为什么列出 dual RAG

Tier 1 的能力清单明确包含 `dual RAG (procedural + factual)`：

- factual knowledge 为 Agent 提供任务世界中的对象、属性、事件和证据；
- procedural knowledge 为 Agent 提供完成任务的步骤、分支、前置条件和验证方式。

原图只列出了这组二分，没有进一步论证它为何足够，也没有声称这是完备的知识分类。将其理解为 Agent 执行所需的最小闭环——“知道当前世界怎样”加“知道接下来怎样做”——属于基于架构语境的解释。^[inferred]

## Open Questions

- 原图的 control rail 从 Tier 3 的 maximum 指向 Tier 1 的 minimum。这里更可能指用户在单次执行中亲自控制每一步的程度；若讨论组织对基础设施的所有权，自建 Tier 1 反而拥有更强的架构控制。^[inferred]
- `dual RAG` 是否应继续拆出因果、规范、目标、能力、元知识与运行时状态，取决于系统是否只回答问题，还是要承担高风险、可审计的现实行动。^[inferred]
- 平台适配不能只比较功能表，还要比较数据边界、权限体系、可迁移性、审计要求和供应商锁定成本。^[inferred]

## Related

- [[wiki/syntheses/Agent Knowledge Architecture]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Agent Skill]]
