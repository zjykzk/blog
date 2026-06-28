---
title: CS Map
type: map
status: growing
category: maps
summary: 这页聚合当前 vault 中更偏计算机科学与软件架构的长期知识页。
provenance:
  extracted: 0.95
  inferred: 0.05
  ambiguous: 0.00
sources: []
created: 2026-04-21
base_confidence: 0.70
lifecycle: draft
lifecycle_changed: 2026-05-05
source_count: 8
updated: 2026-06-19T10:40:26+0800
aliases:
  - Computer Science Map
tags:
  - cs
  - map
  - architecture
---

# CS Map

这页聚合当前 vault 中更偏计算机科学与软件架构的长期知识页。

## Distributed systems

- [[wiki/topics/Circuit Breaker]]
- [[wiki/sources/CAP Theorem Source Guide|CAP Theorem Source Guide]] — CAP theorem source guide：在网络分区下，一致性和可用性不能同时获得强保证；实际设计要看操作级一致性、延迟和失败模式。
- [[wiki/sources/Fallacies of Distributed Computing Source Guide]] — distributed-systems checklist：不要假设网络可靠、零延迟、无限带宽、安全、拓扑静态、单一管理员、传输免费或同构。

## Go

- [[wiki/topics/Go Memory Model]]

## Performance and systems

- [[wiki/topics/High Concurrency]]
- [[wiki/topics/Circuit Breaker]]
- [[wiki/topics/Go Memory Model]]
- [[wiki/sources/Principles of Mechanical Sympathy Source Guide]] — hardware-aware performance principles: predictable memory access, cache-line contention, single-writer ownership, and batching.
- [[wiki/sources/Law of Leaky Abstractions Source Guide]] — abstraction-boundary principle: useful high-level models eventually expose lower-layer behavior at edge cases.
- [[wiki/sources/Hyrums Law Source Guide|Hyrum's Law Source Guide]] — API-evolution principle: observable behavior becomes de facto contract once enough users depend on it.
- [[wiki/concepts/Law of Unintended Consequences]] — change principle: interventions in complex software and social systems can produce benefits, side effects, or perverse results beyond the original plan.
- [[wiki/sources/Galls Law Source Guide]] — software-systems growth principle: complex working systems should evolve from simple working systems.

## Databases

- [[wiki/topics/Dimensional Modeling]] — Kimball-style analytic data modeling starts from business process, grain, dimensions, and facts, then integrates marts through conformed dimensions and a bus matrix.
- [[wiki/concepts/Fact Table]] — fact tables store process measurements at a declared grain and must not be joined directly to other fact tables.
- [[wiki/concepts/Dimension Table]] — dimension tables provide descriptive context and user-facing labels for analytic queries.
- [[wiki/concepts/Data Warehouse Bus Matrix]] — bus matrix plans business processes against conformed dimensions for incremental enterprise integration.
- [[wiki/topics/BoltDB Internals]]
- [[wiki/sources/CAP Theorem Source Guide|CAP Theorem Source Guide]] — distributed database trade-off source guide：网络分区下强一致与强可用不能同时保证，数据库选择应回到延迟、失败模式和操作级一致性。
- [[wiki/sources/Doris 写入与 Routine Load Source Guide|Doris 写入与 Routine Load Source Guide]] — Doris 写入路径 source guide：从 Stream/Broker/Routine Load 选择，下钻到 Routine Load Task、Kafka offset、Rowset、事务和 publish version。

## Architecture and methods

- [[wiki/maps/Software Analysis Map]]
- [[wiki/maps/Software Design Map]]
- [[wiki/concepts/Software Design Three Generators]]
- [[wiki/topics/Software Methodology]]
- [[wiki/topics/面向对象分析与设计]]
- [[wiki/topics/UML Diagrams in Software Development]]
- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/topics/User Stories]]
- [[wiki/topics/Frontend Development Workflow]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/syntheses/Quality Engineering Three Generators]]
- [[wiki/concepts/DORA Metrics]] — software delivery performance metrics that pair throughput with instability so teams can improve delivery systems without treating speed and stability as tradeoffs; the history source shows how the boundary evolved from IT performance through reliability and recovery definitions.
- [[wiki/sources/软件工程中的稳定性治理的秩 Source Guide]] — 稳定性治理 source guide：把运行期可靠性压成变化入口、故障传染和回拉能力三根生成器。
- [[wiki/syntheses/信息流与状态流转设计原则]]
- [[wiki/topics/Testing Purpose]]
- [[wiki/topics/Problem Framing]]
- [[wiki/topics/Spec-Driven Development]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/topics/Software Development Thought Lineage]]
- [[wiki/concepts/重构层次]]
- [[wiki/concepts/架构一致性]]
- [[wiki/topics/架构落地方法]]
- [[wiki/concepts/架构知识模型]]
- [[wiki/concepts/架构认知框架]]

## Syntheses

- [[wiki/syntheses/AI 时代开发岗位分层与协作]] — AI 时代开发岗位会分层为探索闭环、系统 owner 责任和被压缩的执行交付。
- [[wiki/syntheses/From User Story to Architecture]]
- [[wiki/syntheses/类和对象结构图的建模作用]] — OOAD 中类和对象结构图的核心作用是把业务世界压成责任容器及其关系，而不是提前列代码类清单。

## Source layer

- [[wiki/sources/Kimball Dimensional Modeling Techniques Source Guide]] — Kimball Group 2013 technique catalog: four-step design process, grain, fact/dimension patterns, conformed dimensions, SCD types, hierarchy handling, and special schemas.
- [[wiki/sources/Software Methodology by Pan Jianyu]]
- [[wiki/sources/Published Posts]]
- [[wiki/sources/Frontend Development Workflow Roundtable Source Guide]]
- [[wiki/sources/web_chunk|Web Chunk Source Guide]] — 前端构建 source guide：说明 bundler 如何从 module graph 切出 chunk 并输出 asset，同时区分 loadable、dynamic import、module、chunk、asset、bundle。
- [[wiki/sources/架构文档与图示之道 Source Guide]]
- [[wiki/sources/架构师启示录 Source Guide]]
- [[wiki/sources/React Component Lifecycle Source Guide]]
- [[wiki/sources/React Hooks useRef useContext useMemo Source Guide]]
- [[wiki/sources/React Hooks useState useEffect Source Guide]]
- [[wiki/sources/React 状态范围与复杂全局状态 Source Guide]]
- [[wiki/sources/Structured-Prompt-Driven Development Source Guide]]
- [[wiki/sources/SPDD Abstraction First Source Guide]]
- [[wiki/sources/SPDD Alignment Source Guide]]
- [[wiki/sources/SPDD Iterative Review Source Guide]]
- [[wiki/sources/Principles of Mechanical Sympathy Source Guide]]
- [[wiki/sources/Law of Leaky Abstractions Source Guide]]
- [[wiki/sources/Hyrums Law Source Guide|Hyrum's Law Source Guide]]
- [[wiki/sources/Galls Law Source Guide]]
- [[wiki/sources/Second-System Effect Source Guide]]
- [[wiki/sources/Law of Unintended Consequences Source Guide]]
- [[wiki/sources/DORA Metrics Source Guide]]
- [[wiki/sources/DORA Metrics History Source Guide]] — DORA history article source guide: traces the metric model from IT performance to SDO performance, reliability, failed deployment recovery time, and 2024 deployment rework rate.
- [[wiki/sources/Fallacies of Distributed Computing Source Guide]]
- [[wiki/sources/Grokking Simplicity Taming FP Source Guide]] — 函数式编程读书笔记：用 action、calculation、data、timeline、分层和响应式架构治理代码复杂度。
- [[wiki/sources/AI 工程化不是提效 是换主回路 QA Source Guide]] — Q-A 链：把软件工程未彻底工程化、大模型认知引擎、确定性裁判、小闭环和隐性知识蒸馏压成一条可复述的问题路径。
- [[wiki/sources/AI 软件工程问答 Source Guide]] — 中文问答链：从软件工程未彻底工程化出发，推导 AI 中心产线、确定性验证、分治结构和隐性知识蒸馏的落地路径。
- [[wiki/sources/软件工程真正降临 Source Guide]] — 中文长文：从经典工程史和控制论推导软件工程的 AI 中心产线化路径，强调确定性裁判、小闭环、分治单元和产线设计师。
- [[wiki/sources/大模型时代软件工程的本质与演进 Source Guide]] — 中文长文：从需求工程、Naur、DDD、Brooks、Lehman、Woods 到 AI “无理论代码”，论证软件工程是问题定义、知识传递与应用。
- [[wiki/sources/AI 什么都能写与软件价值重心转移 Source Guide]] — 中文长文：把 db9、技术栈迁移、遗留系统重写和企业维护争议串成“代码变便宜，知识与判断变贵”的 AI 软件工程线索。
- `content/posts/cs/arch/arch.md`
- `content/posts/cs/dist/circuit-breaker.md`
- `content/posts/cs/golang/go-memory-model.md`
- `content/posts/cs/db/bolt.md`
