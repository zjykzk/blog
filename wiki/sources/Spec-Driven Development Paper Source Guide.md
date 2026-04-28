---
title: Spec-Driven Development Paper Source Guide
type: source
status: stable
updated: 2026-04-26
aliases:
  - SDD Paper
  - arxiv 2602.00180
  - Piskala 2026
tags:
  - software-engineering
  - specs
  - ai-coding
  - paper
---

# Spec-Driven Development Paper Source Guide

这篇论文是 Deepak Babu Piskala 投稿 AIWare 2026 的 practitioner guide，把 SDD 这波被 AI coding assistant 重新点燃的旧想法梳理成三档光谱 + 四阶段流水线 + 决策框架。8 页，3 张图，零量化实验。

## 来源

- arxiv：https://arxiv.org/abs/2602.00180
- PDF：https://arxiv.org/pdf/2602.00180
- 作者：Deepak Babu Piskala
- 场所：submitted to AIWare 2026
- 本地精读笔记：`~/Documents/notes/20260426T165313--paper-规约驱动开发__paper.org`

## 核心抓手

### 规约光谱（四档）

从"代码为王"到"规约即源码"的连续光谱，不是开关。规约对代码的权威性逐级递增：

1. **Code-First**：代码是真相，文档事后补，漂移常态。
2. **Spec-First**：开工前写规约指导实现，写完可能弃用。适合一次性功能、AI 起步的新需求。
3. **Spec-Anchored**：规约和代码同步演化，CI 用测试强制两者一致。大多数生产系统的甜点位置。BDD、OpenAPI + 契约测试是典型。
4. **Spec-as-Source**：人只改规约，代码全自动生成。汽车 Simulink、Tessl 属于这档。要求工具链极度成熟。

选档原则：选能撑住的最右，不要一步到位。

### 四阶段流水线

Specify → Plan → Implement → Validate。每阶段产出一个工件，约束下一阶段。这个链条是 AI agent 能跑完复杂任务的关键——上下文窗口装不下全系统，装得下一阶段。

Validate 阶段如果发现代码和规约对不上，要先问"谁错了"——规约不是圣经，但必须是权威。

### AI 催化作用

规约是 LLM 的"超级 prompt"。论文引的研究称人工精修规约能把生成代码错误率降一半。衍生玩法：**self-spec**——让 LLM 先写规约，人审核，再让 agent 实现。把"想清楚"和"动手"显式分成两次 prompt。

### 三个案例押三档

- 金融微服务（Spec-Anchored + OpenAPI + Specmatic）：API 变更周期砍 75%
- 企业软件（Spec-Anchored + Cucumber）：消除 "done" 的定义争议
- 汽车引擎控制（Spec-as-Source + Simulink）：ISO 26262 认证天然满足

### 决策框架

不是所有项目都该上 SDD。论文给了一张决策树：
- 抛弃式原型、solo 短命项目、探索式 coding、明显 CRUD → 不上
- 用 AI + 复杂需求 → 至少 Spec-First
- 长寿 + 多人维护 → Spec-Anchored
- 生成工具成熟可信 → Spec-as-Source

黄金法则：**用能消除歧义的最小规约纪律档位**。

## 和传统设计文档的关系

论文自己承认：SDD 不是革命，是 "BDD with branding"（Finster 语）。HLD/LLD/SRS 从来都存在，但它们是/建议性/的，读完靠人肉翻译。SDD 加的是三件事：**可执行**（测试强制一致）、**CI 集成**（每次提交都验）、**AI 可消费**（结构化供模型生成）。

## 审稿结论（博导视角）

weak accept。作为 industry track 合格，概念框架有教学价值，但：

- 零量化实验，"75%" 这类数字孤零零没出处
- 三个 case study 是叙述，不可复现
- 和传统设计文档的关系处理得太客气，最锋利那刀（Finster 那句）被放在脚注

## 对个人体系的连接

- **规约光谱可迁移到"接-替-想"**：每个生成器都有一条"纪律档位"光谱，从随意到形式化
- **self-spec 双阶段流水线 ≈ 认识-表达对偶**：接收→先产规约→人工校准→再产制品，是通用知识工作模板
- **反转提醒**：SDD 假设"规约比代码更接近意图"，在 brownfield legacy 项目里未必成立——这是 SDD 的隐含前提，不是普适真理

## Related

- [[wiki/topics/Spec-Driven Development]]
- [[wiki/topics/User Stories]]
- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/concepts/Cognition Three Channels]]
- [[wiki/concepts/Expression Three Channels]]
- [[SDD]]（pages/ 下的 source note）
