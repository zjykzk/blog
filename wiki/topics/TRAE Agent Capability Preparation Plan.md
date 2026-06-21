---
title: TRAE Agent Capability Preparation Plan
type: topic
status: draft
category: topics
summary: TRAE Agent 能力准备计划围绕 AI Coding Agent 的架构、上下文、模型路由、验证闭环、指标和实验体系组织面试准备。
sources: []
created: 2026-05-30
updated: 2026-06-09T10:56:14+08:00
base_confidence: 0.30
lifecycle: draft
lifecycle_changed: 2026-06-09
aliases:
  - TRAE Agent 能力准备计划
  - TRAE AI Coding Agent 面试准备
tags:
  - ai-coding
  - agents
  - context-engineering
  - career
---
# TRAE Agent Capability Preparation Plan

这份计划面向 TRAE Agent 能力优化与架构设计岗位，目标是围绕 AI Coding Agent 的端到端效果，准备架构、模型、上下文、指标和实验能力。

## 核心能力地图

这个岗位本质是：AI Coding Agent 的端到端效果负责人。

需要准备五条主线。

## Agent 架构与调度

关键主题：

- 单 Agent 与多 Agent 的取舍
- Planner、Executor、Critic、Tool Agent、Context Agent 的职责划分
- 任务分解、状态机、重试、回滚、验证闭环
- ReAct、Plan-and-Execute、Reflection、Tree/Graph of Thoughts、SWE-agent 类工作流

核心问题：

- 复杂任务如何拆？
- 什么时候调用工具？
- 失败后如何恢复？
- 多 Agent 什么时候真的带来收益？

## Code Agent 工程能力

关键主题：

- repo 理解
- 代码搜索
- 依赖图
- AST
- LSP
- 测试运行
- diff 生成
- IDE、DevTools、CI/CD 工作流

常见编码任务类型：

- bug fix
- feature implementation
- refactor
- test generation
- migration
- code review

核心问题：

- Agent 如何像真实工程师一样工作，而不是只生成代码？
- 如何让 Agent 探索代码、验证修改、收敛到可合并 diff？

## Context Engineering

关键主题：

- 多源上下文：代码、README、docs、issue、PR、日志、终端输出、历史对话
- 召回：关键词、embedding、AST/LSP、调用图、文件变更历史
- 排序：query-file relevance、dependency distance、recentness、symbol importance
- 压缩：文件摘要、函数级摘要、diff-aware context、long task memory
- 注入：system、developer、user、tool result、scratchpad、memory 分层

核心问题：

- 如何让模型用对信息，而不是塞满 token？
- 长上下文为什么不等于高质量上下文？
- Context Builder 如何在复杂长链路任务中持续更新？

## 模型适配与推理策略

关键主题：

- 不同模型在规划、代码生成、长上下文、工具调用、指令遵循、修复能力上的差异
- Prompt 体系：角色、约束、工具协议、输出格式、失败处理、代码风格
- Pipeline：小模型检索/分类，大模型规划/生成，强模型修复/验证
- 策略：temperature、top-p、parallel sampling、self-consistency、rerank、fallback

核心问题：

- 不同任务该用什么模型？
- 什么任务需要强推理模型？
- 什么任务更适合低延迟模型？
- 如何设计 model router 与 fallback？

## 效果评估与实验分析

核心指标：

- task success rate
- compile/test pass rate
- issue resolved rate
- edit accuracy
- regression rate
- tool-call efficiency
- user intervention rate
- time-to-solution

评测体系：

- SWE-bench、RepoBench、HumanEval、MBPP、自建真实任务集
- 离线 replay 与在线 A/B
- 分任务类型归因：检索失败、规划失败、工具失败、代码生成失败、验证失败

核心问题：

- Agent 失败了，如何判断是模型问题、上下文问题还是调度问题？
- 如何把用户真实任务转化成可回放、可评估、可归因的数据闭环？

## 两周准备版

目标：两周内形成完整知识框架，能在面试里讲出系统设计、指标、实验和 tradeoff。

## 第 1-2 天：理解 AI Coding Agent 全链路

重点准备：

- AI Coding Agent 的典型流程：理解需求、探索 repo、制定计划、修改代码、运行测试、根据错误迭代、生成最终 diff/解释
- 对比 Cursor、Devin、SWE-agent、OpenHands、Aider、Claude Code、Codex CLI 的工作方式

输出物：

- 一张 Code Agent 端到端架构图
- 一段 3 分钟表述：什么是好的 AI Coding Agent？

## 第 3-4 天：多 Agent 架构与任务调度

重点准备：

- Planner、Executor、Reviewer、Context Retriever、Test Runner 的职责
- 多 Agent 的收益：职责清晰、可并行、可复核
- 多 Agent 的成本：上下文同步、冲突、token 成本、延迟
- 调度策略：task classification、dynamic planning、tool routing、retry、fallback、verification loop

输出物：

- 设计一个 TRAE 多 Agent 框架：
  - Planner：拆任务
  - Context Agent：找相关代码和文档
  - Coding Agent：执行修改
  - Validation Agent：跑测试和分析错误
  - Review Agent：检查 diff 风险

## 第 5-6 天：Context Engineering

重点准备：

- 代码仓库上下文召回：lexical search、embedding search、symbol search、dependency graph、recent files、error stack trace mapping
- 上下文排序：与任务 query 的相关度、文件调用距离、最近修改、是否包含目标 symbol
- 上下文压缩：文件级 summary、function-level chunk、call chain summary、error-driven context pack

输出物：

- 一套 Context Pack 构建方案
- 能回答：为什么长上下文不等于好效果？

## 第 7-8 天：模型适配与 Prompt/Pipeline

重点准备：

- 模型选择策略：
  - 简单任务：低成本快模型
  - 复杂规划：强推理模型
  - 大 repo 理解：长上下文模型
  - 代码修复：强代码模型加测试反馈
- Prompt 体系：
  - task intent classification prompt
  - planning prompt
  - code editing prompt
  - review prompt
  - failure recovery prompt
- Pipeline：classify -> retrieve -> plan -> edit -> test -> repair -> review

输出物：

- 一个任务路由表：bug fix、feature、refactor、test、review 分别怎么调模型和工具。

## 第 9-10 天：效果指标与实验设计

重点准备：

- 离线评测：task success rate、pass@1、test pass rate、patch apply rate、average tool calls、average latency/cost
- 在线指标：用户采纳率、中断率、回滚率、二次修改率、session success rate
- 归因框架：context miss、planning error、tool error、model generation error、verification weakness

输出物：

- 一套 Agent 效果 dashboard 指标设计
- 一个 A/B 实验方案：例如引入新的 context reranker 是否提升 bug fix success rate

## 第 11-12 天：准备案例

准备三个可讲案例。

### 复杂 Bug Fix 案例

- 用户给报错日志
- Agent 定位相关文件
- 分析调用链
- 修改代码
- 跑测试
- 根据失败日志二次修复

### 多 Agent 协作案例

- Planner 拆任务
- Retriever 找上下文
- Coder 改代码
- Reviewer 找风险
- Validator 验证

### 效果优化案例

- 发现任务成功率低
- 归因是上下文召回不足
- 加入 symbol-aware retriever
- 实验提升 success rate

## 第 13-14 天：面试表达打磨

高频问题：

- 你怎么设计一个 AI Coding Agent？
- 多 Agent 一定比单 Agent 好吗？
- Code Agent 失败通常是什么原因？
- Context Engineering 和 RAG 有什么区别？
- 如何评估 Agent 端到端效果？
- 如何根据不同任务选择模型？
- 如果工具调用很慢，怎么优化？
- 如果 Agent 修改了无关代码，怎么避免？
- 如果测试不存在，怎么判断任务完成？

最终输出：

- 1 页架构图
- 1 页指标体系
- 1 页 Context Engineering 方案
- 2-3 个项目/方案故事

## 四周深入版

目标：不只是能讲，而是能展示真的懂系统设计、实验和工程落地。

## 第 1 周：AI Coding Agent 基础架构

学习重点：

- SWE-agent、OpenHands、Aider、Claude Code、Codex CLI 的核心设计
- Agent loop：observe、think、act、verify、repair
- 工具系统：file search、read file、edit file、shell、test、browser、git diff

实践任务：

- 搭一个最小 Code Agent 原型：
  - 输入一个 GitHub issue 或自然语言任务
  - 自动搜索文件
  - 生成修改建议
  - 输出 diff
  - 运行测试或静态检查

产出：

- 《Code Agent 基础架构设计文档》
- 一个最小 Demo 或伪代码框架

## 第 2 周：Context Engineering 深入

学习重点：

- repo-level retrieval
- AST/symbol-aware retrieval
- stack trace retrieval
- issue/doc/code 联合召回
- context compression
- memory across long tasks

实践任务：

- 设计一个 Context Builder：
  - 输入：用户任务加当前 repo
  - 输出：context pack
  - 包含相关文件、关键函数、调用链、相关测试、文档片段、风险提示

评估方式：

- 构造 20 个代码任务
- 人工标注需要哪些文件
- 测召回率、精确率、token 成本

产出：

- 《TRAE Context Engineering 方案》
- context ranking 规则表
- 失败案例分析

## 第 3 周：模型策略、Prompt 与多 Agent 调度

学习重点：

- task router
- model router
- tool router
- fallback strategy
- critic/reviewer loop
- parallel candidate generation
- cost/latency/success tradeoff

实践任务：

- 设计任务分类器：
  - bug fix
  - feature implementation
  - refactor
  - test generation
  - code review
  - explanation
- 每类任务配置：
  - 使用哪些工具
  - 需要哪些上下文
  - 用什么模型
  - 是否需要 reviewer
  - 是否需要测试闭环

产出：

- 《多模型与多 Agent 调度策略》
- 一张 task x model x tool 的路由矩阵
- 一个 failure recovery 策略表

## 第 4 周：评测体系与技术影响力沉淀

学习重点：

- SWE-bench 类 benchmark 的局限
- 真实用户任务 replay
- 离线评测与在线指标如何结合
- root cause analysis
- data flywheel：用户任务、agent trace、failure label、eval case、prompt/model/context improvement、再评测

实践任务：

- 设计一套 TRAE Agent Eval 平台：
  - 任务集管理
  - agent trace 采集
  - 工具调用记录
  - 自动判分
  - 人工标注
  - A/B 实验
  - 失败归因

产出：

- 《TRAE Agent 效果评估体系》
- Dashboard 指标草图
- 一篇内部技术分享大纲：从 Context Engineering 到 Agent 成功率提升

## 面试观点

## Agent 效果优化不是单纯换模型，而是系统工程

模型、上下文、工具、调度、验证、数据闭环共同决定成功率。

## Context Engineering 的核心不是塞更多，而是给对信息

高召回、高精度、低 token、可解释，是核心目标。

## 多 Agent 不是越多越好

多 Agent 适合复杂任务、长链路任务、需要复核的任务；简单任务应避免过度编排。

## Code Agent 必须有验证闭环

没有测试、lint、build、diff review 的 Agent，本质上只是代码生成器。

## 评估要从真实开发任务出发

benchmark 有用，但最终要看真实用户任务的完成率、采纳率、回滚率和干预率。

## 推荐沉淀材料

- 《TRAE Code Agent 架构设计》
- 《Context Engineering 方案》
- 《多模型/多 Agent 调度策略》
- 《Agent 效果评估与实验体系》

这四个材料覆盖 JD 的核心：架构、模型、上下文、指标、实验、方法论。

## Related

- [[wiki/concepts/Agent]] — agent 作为感知、规划、工具、反馈构成的控制环。
- [[wiki/concepts/Agentic Engineering]] — AI coding 的工程重心从生成代码转向 harness、检查和验证。
- [[wiki/concepts/Coding Agent User Harness]] — 开发者侧 harness 决定 agent 能否稳定进入真实工程工作流。
- [[wiki/concepts/Context Information Density]] — context engineering 的核心是提高决策相关信息密度，而不是堆 token。
- [[wiki/concepts/Verification Loop]] — code agent 必须通过测试、lint、review 等外部反馈收敛。
- [[wiki/topics/AI Harness]] — agent runtime、工具、权限、状态和反馈回路的总入口。
- [[wiki/topics/Context Management]] — 上下文进入、停留、压缩和退出的设计问题。
- [[wiki/syntheses/AI Engineering Workflow]] — agent 工作流、工具设计、约束和需求归一化的综合框架。