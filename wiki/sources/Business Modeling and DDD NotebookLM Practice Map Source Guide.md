---
title: >-
  Business Modeling and DDD NotebookLM Practice Map Source Guide
type: source
status: draft
category: sources
tags: [software-engineering, requirements, architecture, organization]
sources:
  - https://notebook.google.com/notebook/49bde482-b80a-44b7-8e09-9a5c5a340463
  - conversation:2026-10-27
created: 2026-10-28T15:24:26+08:00
updated: 2026-10-28T15:24:26+08:00
summary: >-
  这页把“业务建模（DDD等）”NotebookLM 资料中的 36 项实践按六个问题层次整理，说明每项实践直接压住什么问题，并保留跨层使用时的边界。
provenance:
  extracted: 0.90
  inferred: 0.05
  ambiguous: 0.05
base_confidence: 0.32
lifecycle: draft
lifecycle_changed: 2026-10-28
tier: supporting
aliases:
  - 业务建模与 DDD 实践问题地图
  - 软件实践解决什么问题
---

# Business Modeling and DDD NotebookLM Practice Map Source Guide

> Source: [业务建模（DDD等）NotebookLM](https://notebook.google.com/notebook/49bde482-b80a-44b7-8e09-9a5c5a340463)

## What It Covers

这份来源导览把 NotebookLM 当前资料集合中出现的实践，按它们直接处理的问题分成六层：业务建模与需求、战略 DDD、战术 DDD、架构与系统集成、组织协作与交付、面向对象设计与设计模式。

它的用途不是给出一份“软件项目必须采用的 36 项清单”，而是建立一个选择入口：**先判断问题发生在哪一层，再寻找针对该问题的实践。** 同一实践可能跨越多层；这里的分组表示它在本次资料盘点中的主要落点，不是唯一归属。^[inferred]

NotebookLM 的回答来自资料集合的二次综合，本次捕获没有逐条回到原始书目核验引用，因此清单适合导航和比较，不应被当作已经逐条验证的规范。^[ambiguous]

## Practice-to-Problem Map

### 业务建模与需求

| 实践 | 直接解决的问题 |
|---|---|
| 业务用例（Business Use Case） | 区分组织业务流程与软件功能，避免把企业内部运作直接写成软件需求。 |
| 系统用例（System Use Case） | 用黑盒方式定义系统对外承诺，避免需求过早陷入内部实现和 UI。 |
| 海平面级用例（Sea-Level Use Case） | 控制用例粒度，避免过粗而无法指导开发，或过细而难以维护。 |
| 用户故事地图（User Story Mapping） | 把一维 Backlog 还原成用户旅程，并支持按价值纵向切片、分批交付。 |
| 用户故事 3C（Card, Conversation, Confirmation） | 防止把故事卡当成替代沟通的静态规格，通过对话和确认建立共识。 |
| 业务序列图（Business Sequence Map） | 展示业务人员、部门和业务实体之间的动态协作与职责传递。 |

### 战略 DDD

| 实践 | 直接解决的问题 |
|---|---|
| 统一语言（Ubiquitous Language） | 消除业务与技术之间的语义鸿沟，让沟通、模型和代码表达同一套业务概念。 |
| 限界上下文（Bounded Context） | 隔离大型领域中同名异义的模型，阻止大一统模型持续膨胀。 |
| 上下文映射（Context Mapping） | 说明上下文、团队和系统之间的上下游、依赖及集成关系。 |
| 防腐层（Anticorruption Layer） | 防止外部或遗留系统的模型侵入并污染本地领域模型。 |
| 共享核（Shared Kernel） | 在多个团队必须共享模型时减少重复定义，但要求共同协调变更。 |
| 开放主机服务 / 发布语言（OHS/PL） | 让上游以稳定协议服务多个下游，避免为每个下游定制接口。 |

### 战术 DDD

| 实践 | 直接解决的问题 |
|---|---|
| 充血领域模型（Rich Domain Model） | 避免数据与行为分离、业务规则散落在服务层的贫血模型。 |
| 小聚合设计（Small Aggregates） | 避免聚合过大带来的锁冲突、加载成本、性能下降和事务复杂度。 |
| 通过唯一标识引用聚合 | 避免聚合之间直接对象引用造成边界模糊、循环加载和查询膨胀。 |
| 领域事件（Domain Event） | 解耦跨聚合或跨上下文协作，并支持异步处理和最终一致性。 |
| 领域服务（Domain Service） | 承载不自然属于某一个实体、但确实属于领域的跨对象业务规则。 |
| 聚合工厂（Factory Pattern in DDD） | 封装复杂聚合的创建过程，保护内部约束，避免构造逻辑泄漏。 |

### 架构与系统集成

| 实践 | 直接解决的问题 |
|---|---|
| 绞杀者模式（Strangler Fig Pattern） | 避免遗留系统大爆炸式重写，通过增量替换降低演进风险。 |
| 六边形架构 / 端口与适配器 | 隔离领域核心与 UI、数据库、框架和第三方 API，使核心可独立测试与迁移。 |
| CQRS | 分开读模型与写模型，使复杂事务写入和高并发查询能够独立优化。 |
| 事件驱动架构 | 降低节点之间的同步调用耦合，减少级联故障并提高吞吐与容错。 |
| 管道与过滤器 | 把多阶段处理拆成可以独立复用、组合、替换和重排的步骤。 |
| 领域专用语言（DSL） | 把频繁变化的复杂业务规则表达为领域语言，减少反复修改主程序代码。 |

### 组织协作与交付

| 实践 | 直接解决的问题 |
|---|---|
| 逆康威操纵（Inverse Conway Maneuver） | 当团队结构阻碍目标架构时，按业务上下文调整组织边界，促进系统解耦。 |
| 测试驱动开发（TDD） | 避免先写实现、后补测试形成不可测代码和过度设计，并建立安全重构网。 |
| 事件风暴（Event Storming） | 让业务、开发和测试快速对齐业务流程、统一语言，并发现上下文边界。 |
| Q1/Q2 测试关联策略 | 连接技术侧组件测试和业务侧验收测试，避免两类验证相互割裂。 |
| AI 结对编程 / LLM Pairing + TDD | 用测试和规则约束 AI 生成代码，降低幻觉、设计缺陷和不可验证输出。 |

### 面向对象设计与设计模式

| 实践 | 直接解决的问题 |
|---|---|
| 单一职责原则（SRP） | 避免一个类承担多个变化原因，导致修改彼此牵连。 |
| 依赖倒置原则（DIP） | 避免高层业务规则依赖底层实现细节，使底层可替换、核心可测试。 |
| 策略模式（Strategy） | 消除大量算法选择分支，使算法可以独立扩展、复用和动态切换。 |
| 状态模式（State） | 把状态相关行为收拢进状态对象，避免状态机散落在条件分支中。 |
| 装饰者模式（Decorator） | 在不制造继承类爆炸的情况下，动态组合附加功能。 |
| 观察者模式（Observer） | 解耦状态发布者与依赖者，使变化可以通知多个对象。 |
| 角色对象模式（Role Object） | 表达同一实体在不同上下文承担的角色，避免所有职责堆成巨型类。 |

## How to Read the Map

这 36 项实践不是平铺的工具箱。它们处理的是不同尺度上的失真：

1. **现实失真**：业务目标和组织交换没有被看见，用业务用例、故事地图和业务序列图重建现实。
2. **语义失真**：同一个词在不同群体里含义不同，用统一语言、限界上下文和上下文映射收敛含义。
3. **模型失真**：业务规则进入代码后散落或失去边界，用聚合、领域服务、工厂和领域事件维持模型。
4. **依赖失真**：核心逻辑被基础设施和同步链路绑住，用六边形、CQRS、事件驱动等重组依赖。
5. **协作失真**：团队、测试和交付方式与目标架构不匹配，用逆康威、事件风暴和 TDD 调整反馈回路。
6. **局部结构失真**：类和对象承担的变化、算法或状态混在一起，用设计原则和模式重新分配责任。

因此，实践选择应从“当前结果由哪一层的问题稳定生成”开始，而不是从“团队最近想引入哪个流行方法”开始。^[inferred]

## Important Distinctions

- **业务用例 / 系统用例**区分研究对象和边界；**白盒 / 黑盒**区分是否展开内部结构，它们不是同一个维度。
- **领域事件**是领域模型表达的业务事实；**事件驱动架构**是系统协作方式。
- **防腐层**保护本地模型不被外部模型污染；**六边形架构**保护领域核心不依赖基础设施。
- **事件风暴**用于共同发现业务结构；**上下文映射**用于表达已识别上下文之间的关系。
- **战略 DDD**主要决定语言和模型边界；**战术 DDD**主要决定边界内部如何用代码承载业务规则。

## Open Questions

- NotebookLM 底层各来源是否对 36 项实践使用了相同定义，仍需逐条回到原始材料核验。
- Q1/Q2 测试分类、角色对象模式和 AI 结对编程在这组资料中的证据范围有多大，当前盘点没有展示来源分布。^[ambiguous]
- 一个具体项目何时只需要轻量用户故事，何时值得引入完整业务建模和 DDD，需要结合复杂度、变化率和协作边界判断。^[inferred]

## Related

- [[wiki/syntheses/Business Analysis to Software Design]]
- [[wiki/maps/Software Analysis Map]]
- [[wiki/maps/Software Design Map]]
- [[wiki/concepts/Domain-Driven Design]]
- [[wiki/concepts/Software Analysis Three Generators]]
- [[wiki/concepts/Software Design Three Generators]]
- [[wiki/topics/Software Methodology]]

