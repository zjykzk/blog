---
title: >-
  Quality Engineering Three Generators
category: syntheses
tags: [software-engineering, testing, requirements, feedback]
sources:
  - conversation:2026-05-13
created: 2026-05-13T23:20:00+08:00
updated: 2026-05-15T21:33:01+08:00
summary: >-
  质量工程可以压缩为三根生成器：说清承诺、显形偏差、形成修正闭环；软件行业最佳实践分别落在规格契约、测试监控和复盘改进上。
provenance:
  extracted: 0.93
  inferred: 0.07
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-13
type: synthesis
status: draft
aliases:
  - 质量工程三根生成器
  - 质量工程的秩
  - 质量工程最佳实践
---

# Quality Engineering Three Generators

## Context

质量工程常被误解成工具清单：测试、代码审查、CI、监控、灰度、SLO、缺陷复盘、发布门禁、覆盖率和质量报表。更稳的看法是：质量工程处理的是系统承诺和真实运行结果之间的偏离。质量好，不是因为系统没有错误，而是因为承诺清楚、偏差显形、偏差被吃进系统并改变下一次行为。^[inferred]

## Finding

质量工程有三根生成器：

1. **承诺清楚**：把“好”从感觉变成可检查的例子、契约、指标和边界。
2. **偏差显形**：让系统尽早、真实地暴露承诺和现实之间的偏离。
3. **修正闭环**：把每次偏差转化成新的测试、契约、监控、发布约束或组织知识。

这三根不是并列实践，而是质量工程的控制结构。BDD、API 契约、SLO、CI、自动化测试、监控、复盘和错误预算，都是挂在这三根线上的装置。

## Reasoning

### 1. 承诺清楚：规格、例子、契约和 SLO

承诺不清时，团队会陷入争吵：这算不算 bug？这是需求变更还是实现错误？系统应该支持这个边界吗？质量活动会漂，因为没人知道偏离了什么。

软件行业中对应的最佳实践包括：

- **验收标准与 BDD 示例**：用具体场景说明系统应该表现出什么行为。Cucumber 的 Gherkin/BDD 文档强调，场景应该描述业务行为，而不是 UI 操作细节；`Given-When-Then` 的价值在于形成 shared understanding，并让行为示例成为 living documentation。
- **用户故事与验收条件**：用户故事表达“谁、想做什么、为什么”，验收条件则说明这件事如何被确认完成。它连接 [[wiki/topics/User Stories]] 和 [[wiki/topics/Requirement to Architecture Mapping]]。
- **消费者驱动契约测试**：Pact 把消费者真实依赖的 provider 行为写成 contract，并让 provider 持续验证这些 contract。它把服务之间的隐含承诺显性化，减少“接口文档没变但消费者坏了”的集成风险。
- **SLO/SLI/Error Budget**：Google SRE 把可靠性定义为用户关心的服务行为。SLI 是量化服务水平的指标，SLO 是目标值或范围，Error Budget 则定义可接受的不可靠性。它们把“系统要稳定”变成可讨论、可监控、可治理的承诺。
- **架构约束与领域语言**：模块边界、领域不变量、数据所有权、依赖方向和统一语言，都是承诺。它们让质量不只停留在测试阶段，而是进入设计结构。^[inferred]

### 2. 偏差显形：CI、自动化测试、测试金字塔和监控

偏差不显时，团队会陷入侥幸：本地没问题、测试过了、应该不会出事。真正危险的不是红灯，而是假绿灯。红灯至少说明哪里痛；假绿灯会让团队继续加速，直到线上撞墙。

软件行业中对应的最佳实践包括：

- **持续集成**：Martin Fowler 对 CI 的经典描述是，开发者频繁集成到 mainline，自动构建和测试每次集成，并立即修复失败。CI 的核心不是工具，而是把集成问题从后期爆炸提前到每次小变更。
- **测试自动化**：DORA 将测试自动化列为提升软件交付和组织表现的 DevOps 能力。自动化测试让反馈更快、更可重复，也减少手工回归的延迟和随机性。
- **测试金字塔**：Fowler 的 Test Pyramid 建议底部放大量快速、便宜、容易定位问题的单元测试；中间放较少的服务/API/集成测试；顶部只保留少量端到端或 UI 测试。它和 [[wiki/topics/Testing Strategy]]、[[wiki/topics/Testing Purpose]] 相连：测试不是追求数量，而是增加对变化正确性的信心。
- **主干开发和小批量变更**：DORA 将 trunk-based development 和 small batch work 视为减少集成摩擦、缩短 lead time、加快反馈循环的实践。变更越小，偏差越容易定位。
- **监控与可观测性**：Google SRE 的监控章节提出四个黄金信号：latency、traffic、errors、saturation。告警应面向用户症状，并且每个 page 都应该 actionable。DORA 也把 monitoring and observability 视为让团队调试生产系统、给开发者快速反馈的能力。

### 3. 修正闭环：复盘、回归测试、错误预算和交付改进

闭环不成时，团队会陷入重复：同类 bug、同类事故、同类发布失败不断出现，每次都像第一次遇到。修正闭环要求偏差不仅被修掉，还要改变系统下一次产生同类偏差的方式。

软件行业中对应的最佳实践包括：

- **无责事故复盘**：Google SRE 的 Postmortem Culture 强调，复盘不是惩罚，而是学习。复盘应记录影响、缓解过程、根因或促成因素，并形成有 owner 和优先级的 follow-up actions。
- **事故知识库与组织学习**：复盘应可搜索、可分享，让其他团队也能学习。否则事故只停留在个体经验里，组织不会长记性。
- **回归测试**：当高层测试或线上事故发现 bug 后，应尽量补一个更低层、更快、更稳定的测试，防止同类问题回来。这把一次偏差变成自动检查。
- **错误预算治理**：Error Budget 不只是可靠性指标，也是闭环控制信号。预算消耗过快时，团队应减少新功能风险，把注意力转向可靠性修复、发布节奏调整或架构约束补强。^[inferred]
- **持续交付改进**：DORA 把 continuous delivery 描述为可靠、低风险、可按需发布的能力。每次失败都应反过来改进流水线、测试、发布策略、回滚机制或架构边界。

## Implications

质量工程的实践可以用三问诊断：

| 根 | 诊断问题 | 典型实践 |
|---|---|---|
| 承诺清楚 | 我们到底承诺了什么？谁能验证？ | BDD 示例、验收标准、API 契约、SLO/SLI、架构边界 |
| 偏差显形 | 偏了以后多久能知道？信号真实吗？ | CI、自动化测试、测试金字塔、主干开发、监控、告警、可观测性 |
| 修正闭环 | 这次问题会不会用同样方式再来？ | 无责复盘、行动项、回归测试、错误预算、持续交付改进 |

它也能解释三种常见质量病灶：

```text
承诺不清  ->  争吵: 这算不算问题
偏差不显  ->  侥幸: 应该不会出事
闭环不成  ->  重复: 同类事故反复来
```

质量工程因此不是“多测一点”或“流程严一点”，而是一套控制偏离的工程能力：先把该发生什么说清楚，再让没发生的部分尽早显形，最后把显形出来的偏差吃进系统，让下一次更难偏。

## Source Anchors

- Google SRE Book: Service Level Objectives — SLI、SLO、Error Budget 把可靠性承诺转化为用户相关、可量化、可治理的目标。
- Google SRE Book: Monitoring Distributed Systems — 四个黄金信号、症状优先、actionable paging 支撑偏差显形。
- Google SRE Book: Postmortem Culture — 无责复盘、follow-up actions、事故知识库支撑修正闭环。
- DORA DevOps Capabilities — 测试自动化、主干开发、持续交付、监控与学习文化支撑高绩效软件交付。
- Martin Fowler: Continuous Integration — 频繁集成、自动构建、自测试构建和快速修复支撑早反馈。
- Martin Fowler: Test Pyramid / Practical Test Pyramid — 分层自动化测试以低成本、快反馈提升信心。
- Cucumber: Better Gherkin — 行为示例和 declarative scenarios 帮助团队形成共同理解。
- Pact Documentation — 消费者驱动契约测试让服务间期望显性化，并提前发现 provider-consumer mismatch。

## Related

- [[wiki/topics/Modern Software Engineering]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/topics/Testing Purpose]]
- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/topics/User Stories]]
- [[wiki/syntheses/Reality-Refutable Engineering Systems]]
- [[wiki/concepts/engineering-thinking|Engineering Thinking]]
