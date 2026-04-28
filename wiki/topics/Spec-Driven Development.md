---
title: Spec-Driven Development
type: topic
status: draft
source_count: 2
updated: 2026-04-26
aliases:
  - SDD
tags:
  - software-engineering
  - specs
  - ai-coding
  - process
---

# Spec-Driven Development

Spec-Driven Development（SDD）把"代码是真相、文档是附属品"这个长期默认假设倒置：**规约是合同，代码是合同的执行副本**。合同变了，执行副本重新生成；执行副本擅自改了，CI 让构建失败。AI coding assistant 这波新工具把这个老想法重新点燃——因为 LLM 是"擅长模式补全、不会读心"的队友，模糊的上下文被放大成灾难。

## Core idea

- 代码是规约的实现细节，不是反过来
- 规约权威性不是开关，是连续光谱
- 在 AI 协作场景下，规约质量直接决定产出质量

## 规约光谱（四档）

| 档位 | 谁是真相 | 漂移控制 | 典型场景 |
|------|----------|----------|----------|
| Code-First | 代码 | 无 | 默认的旧世界 |
| Spec-First | 初期是规约，之后是代码 | 不强制 | 一次性功能、原型、AI 启动新需求 |
| Spec-Anchored | 规约和代码同步 | 测试强制 | 多数生产系统的甜点位置 |
| Spec-as-Source | 只有规约是真相 | 重新生成 | 汽车 Simulink、certified embedded、Tessl |

**选档原则**：用能消除歧义的最小规约纪律档位。不要一步到位选最右。

## 四阶段流水线

Specify → Plan → Implement → Validate

每阶段产出一个工件，约束下一阶段。这条链是 AI agent 能跑完复杂任务的关键——上下文窗口装不下全系统，装得下一阶段。Validate 发现不一致时，先问"谁错了"：规约错就改规约，代码错就改代码，但规约必须保持权威。

## 决策框架

论文给了一张决策树，归纳起来：

- **不上 SDD**：抛弃式原型、solo 短命项目、探索式 coding、简单 CRUD
- **Spec-First**：用 AI 起步新需求，或需求复杂到容易被误读
- **Spec-Anchored**：长寿系统 + 多人维护 + 集成密集
- **Spec-as-Source**：代码生成工具链已经被充分信任的领域

## 与既有实践的关系

- **TDD** 是单元级 SDD，先写测试就是写微规约
- **BDD** 是最直接的祖先，Gherkin 场景就是可执行规约
- **API-First / OpenAPI** 在 Web 领域已经是标配的 Spec-Anchored
- **Design by Contract**（Meyer）是 Spec-as-Source 的理论根
- Finster 的尖锐一刀："SDD is not a revolution, it's just BDD with branding"——但 branding 本身也在做工作：它提醒规约应该是/权威的/而非/建议的/

## AI coding 语境下的新价值

1. **规约 = 超级 prompt**：消除 LLM 必须瞎猜的默认值
2. **并行**：规约边界清楚了，多个 agent 可以同时做互不重叠的模块
3. **self-spec**：LLM 先写规约、人审核、再让 agent 实现，把"想清楚"和"动手"显式分两次 prompt
4. **非决定性缓释**：property-based testing 从规约抽不变式，规避每次生成的随机波动

## Open questions

- 从 legacy code 反向抽规约时，规约未必比代码更接近意图——这是 brownfield 的特殊挑战
- 规约本身也会被错写。SDD 不消除歧义，只把歧义从"代码 vs 意图"转移到"规约 vs 意图"
- "每行代码可追溯到规约"的认证成本是否值得，取决于领域容错度

## Navigation

- [[wiki/sources/Spec-Driven Development Paper Source Guide]]（arxiv 2602.00180 精读）
- [[SDD]]（pages/ source note，含 GitHub spec-kit）
- [[wiki/topics/User Stories]]
- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/syntheses/From User Story to Architecture]]
