---
title: CS Map
type: map
status: growing
category: maps
summary: 这页聚合当前 vault 中更偏计算机科学与软件架构的长期知识页。
sources: []
created: 2026-04-21
base_confidence: 0.70
lifecycle: draft
lifecycle_changed: 2026-05-05
source_count: 8
updated: 2026-05-27T00:43:06+0800
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

## Go

- [[wiki/topics/Go Memory Model]]

## Performance and systems

- [[wiki/topics/High Concurrency]]
- [[wiki/topics/Circuit Breaker]]
- [[wiki/topics/Go Memory Model]]
- [[wiki/sources/Principles of Mechanical Sympathy Source Guide]] — hardware-aware performance principles: predictable memory access, cache-line contention, single-writer ownership, and batching.
- [[wiki/sources/Law of Leaky Abstractions Source Guide]] — abstraction-boundary principle: useful high-level models eventually expose lower-layer behavior at edge cases.
- [[wiki/sources/Hyrums Law Source Guide|Hyrum's Law Source Guide]] — API-evolution principle: observable behavior becomes de facto contract once enough users depend on it.
- [[wiki/sources/Galls Law Source Guide]] — software-systems growth principle: complex working systems should evolve from simple working systems.

## Databases

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

## Source layer

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
- `content/posts/cs/arch/arch.md`
- `content/posts/cs/dist/circuit-breaker.md`
- `content/posts/cs/golang/go-memory-model.md`
- `content/posts/cs/db/bolt.md`
