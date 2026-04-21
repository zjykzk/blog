---
title: LLM Wiki Index
type: map
status: growing
source_count: 0
updated: 2026-04-20
aliases:
  - Wiki Index
tags:
  - llm-wiki
  - index
---

# LLM Wiki Index

这个 vault 正在从混合式笔记仓库，重构为更接近 Karpathy 风格的 LLM Wiki：

- `raw/`：原始材料、日记、摘录、草稿、领域输入
- `wiki/`：稳定知识页、主题页、概念页、索引页、综合页
- `content/posts/`：对外发布层

## Start here

### Maps

- [[wiki/maps/AI Map]]
- [[wiki/maps/CS Map]]
- [[wiki/maps/Management Map]]
- [[wiki/maps/Reading Map]]

### Core pages

- [[wiki/concepts/Agent]]
- [[wiki/concepts/Agent Tool]]
- [[wiki/concepts/LLM]]
- [[wiki/concepts/Cynefin Framework]]
- [[wiki/topics/Karpathy Guidelines]]
- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/Tool Routing]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Testing Purpose]]
- [[wiki/topics/Problem Framing]]
- [[wiki/topics/Spec-Driven Development]]
- [[wiki/topics/Technical Management]]
- [[wiki/topics/Resource Formula]]
- [[wiki/topics/Circuit Breaker]]
- [[wiki/topics/Go Memory Model]]
- [[wiki/topics/BoltDB Internals]]

### Syntheses

- [[wiki/syntheses/From User Story to Architecture]]
- [[wiki/syntheses/Decision Modes for Engineering Work]]
- [[wiki/syntheses/AI Engineering Workflow]]

### Source guides

- [[wiki/sources/Journals]]
- [[wiki/sources/Mobu Notes]]
- [[wiki/sources/Published Posts]]
- [[wiki/sources/Modern Software Engineering Notes]]
- [[wiki/log]]

## Structure

- `wiki/maps/`：MOC / 主题入口
- `wiki/concepts/`：稳定概念页
- `wiki/topics/`：长期主题页
- `wiki/syntheses/`：综合理解
- `wiki/sources/`：对 raw 或外部材料的结构化导读

## Migration notes

当前仍保留旧目录：
- `pages/`
- `journals/`
- `mobu/`
- `content/posts/`

第一阶段采用“先建索引层，再逐步迁移内容”的方式，避免一次性搬家导致断链。

## Naming and placement

- 目录语义规则见 [[wiki/NAMING]]
- `wiki/index.md` 是当前首页
- `wiki/Welcome.md` 是历史遗留页，不再承担导航职责
- 新增稳定知识优先写入 `wiki/`
