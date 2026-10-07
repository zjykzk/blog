---
title: Building and Deploying AI Applications Source Guide
type: source
status: draft
category: sources
tags: [article, llm, agents, feedback, software-engineering]
aliases:
  - AI Engineering Skills Map Building and Deploying AI Applications
  - 构建与部署 AI 应用技能地图
  - Andrew Ng Building and Deploying AI Applications
sources:
  - https://x.com/AndrewYNg/article/2090840747738374568
  - conversation:2026-10-06
source_url: https://x.com/AndrewYNg/article/2090840747738374568
created: 2026-10-06T23:40:38+0800
updated: 2026-10-06T23:40:38+0800
summary: >-
  Andrew Ng 将构建与部署 AI 应用拆成 LLM/ML 基础、数据 grounding、agentic systems、evaluation-driven development 与生产运营，并把不确定输出转化为证据驱动的迭代闭环。
provenance:
  extracted: 0.72
  inferred: 0.26
  ambiguous: 0.02
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-06
tier: supporting
relationships:
  - target: "[[wiki/sources/AI Engineering Skills Map Source Guide]]"
    type: derived_from
  - target: "[[wiki/concepts/Evaluation]]"
    type: related_to
  - target: "[[wiki/syntheses/AI Engineering Workflow]]"
    type: related_to
  - target: "[[wiki/topics/AI Harness]]"
    type: related_to
---

# Building and Deploying AI Applications Source Guide

> 来源：[Andrew Ng, “AI Engineering Skills Map: Building and Deploying AI Applications”](https://x.com/AndrewYNg/article/2090840747738374568)

这篇文章是 [[wiki/sources/AI Engineering Skills Map Source Guide|AI Engineering Skills Map]] 的第一篇展开文，专门拆解“构建与部署 AI 应用”所需的内部能力。作者称这张地图来自大量招聘信息、结构化专家访谈和问卷，但没有公开样本、编码方法、权重和学习顺序，因此它是一张实践能力地图，而不是可独立复核的职业标准。^[ambiguous]

## 核心问题

表层问题是：**构建和部署 AI 应用，需要掌握哪些技能？**

作者列出六项：

1. LLM foundations；
2. Grounding models with data；
3. Building agentic systems；
4. Evaluation-driven development；
5. Operating in production；
6. Machine learning foundations。

更深层的问题是：**当模型输出无法在开发前被完全预测时，工程师怎样决定下一步做什么，并把不可靠的 AI 组件组织成可靠系统？**

AI 系统开发因此不是一次性执行预定方案，而是反复构建、观察中间结果、分析错误、选择下一项干预。关键能力不是永远提前知道正确答案，而是在不确定反馈中持续做出更好的下一步决策。^[inferred]

## 概念结构

原图把六项技能画成平行分支；按它们在系统中的职责，可以进一步重组成三层基础与一个控制循环：^[inferred]

| 能力 | 系统职责 | 核心问题 |
|---|---|---|
| LLM foundations | 理解模型边界 | 模型能做什么、何时失效、应如何配置或选择 |
| Machine learning foundations | 理解不确定性 | 怎样分析误差、泛化、偏差、数据和速度取舍 |
| Grounding models with data | 提供任务证据 | 模型此刻应该看到什么，以及怎样保持数据新鲜 |
| Building agentic systems | 组织行动结构 | 模型怎样循环、调用工具、管理记忆并改变外部状态 |
| Evaluation-driven development | 驱动开发方向 | 当前哪里不好，下一项最值得尝试的修改是什么 |
| Operating in production | 关闭现实反馈环 | 真实流量下是否可靠、安全、经济并能应对漂移 |

```text
                 LLM / ML foundations
                 理解能力、失败与误差
                          │
                          ▼
数据与上下文 ──→ agentic 系统结构 ──→ 真实输出与行动
Grounding        workflow / harness       │
    ▲             tools / memory           ▼
    │                                 traces / failures
    │                                        │
    └────── 选择下一项干预 ← eval + 错误分析 ┘
                         │
                         ▼
              生产监控、漂移、安全、成本
                         │
                         └────反馈到下一轮开发
```

LLM 与 ML 基础提供判断语言；grounding 决定系统拥有的证据；agentic architecture 决定系统的行动空间；production 提供现实信号；evaluation-driven development 把它们连接成持续改进的控制环。^[inferred]

因此，eval 在图上虽然是六个并列分支之一，在文章的因果结构中却接近中心：作者明确把严格推动 eval / error-analysis loop 的能力，视为优秀 AI 系统构建者最重要的区别。

## 推理流程

### 1. 用输出不确定性定义 AI 应用的特殊性

LLM 会生成什么文本、监督学习模型面对新样本会作出什么预测，都无法提前完全确定。AI 应用开发因此比传统软件更难预先规划完整过程。

### 2. 把开发重写成自适应决策序列

工程师需要反复构建一部分系统、查看结果，再决定下一步。中间结果会改变后续行动，所以开发路径由反馈塑造，而不只是由初始计划决定。

### 3. 用 LLM 基础判断模型边界

理解 tokenization、生成过程、context window、cache hit、knowledge cutoff、reasoning effort、sampling parameters 和 tool calling，可以帮助工程师：

- 判断何时可以依赖模型、何时容易失败；
- 选择模型或模型组合；
- 决定上下文中应放什么；
- 判断是否需要微调或自托管。

基础知识的作用是缩小干预搜索空间，减少把知识截止、上下文缺失、采样设置和模型能力问题相互混淆的概率。^[inferred]

### 4. 用 grounding 决定模型当前知道什么

RAG 向量检索只是 grounding 的早期形式。工程师还要决定：

- 哪些信息直接放进 prompt，哪些让模型通过工具按需获取；
- 数据应使用向量索引、知识图谱，还是结构化数据上的语义层；
- PDF、HTML、图片等材料如何转换为模型可用输入；
- 数据管道如何保持清洁与新鲜。

模型能力不等于任务信息完整。许多输出失败首先是证据供给问题，而不是模型规模问题。^[inferred]

### 5. 用 agentic architecture 组织行动

Agentic systems 从预定义 LLM 调用序列，到让模型在 harness 中不断决定下一步。工程师需要选择：

- 串行还是并行；
- 使用代码还是 LLM；
- 提供哪些 MCP、CLI 或 sandbox 工具；
- 使用什么记忆架构；
- 长会话如何管理上下文；
- 单 Agent 还是多 Agent；
- 失败时怎样 fallback。

原型进入生产还需要 guardrail、对抗输入防护、数据泄漏控制、安全和治理。

### 6. 用 eval 与错误分析决定开发方向

工程师从 traces 和输出中观察失败，结合产品与业务知识决定测量什么，再选择：

- 确定性的代码评估；
- LLM-as-a-Judge；
- 人工判断。

Eval 本身也需要被评估和持续修改。这样，实验结果才能决定下一项开发工作，使进展从随机尝试变成系统搜索。

### 7. 用生产运营关闭现实反馈环

生产环境带来实验阶段没有充分暴露的漂移、模型失败、prompt injection、成本、延迟和规模效应。团队需要 observability、统计性回归测试、适合 AI 系统的 CI/CD，并根据错误风险调整测试强度。

模型选择、蒸馏、微调和简化 agentic workflow 都可以成为成本与延迟优化手段，尤其是在用户规模扩大之后。

### 8. 用 ML 基础保持跨工具的判断能力

现代 LLM 建立在监督学习和强化学习之上，许多应用也仍需要传统机器学习。Bias/variance、error analysis、训练与评估数据工程，以及准确率、训练速度和推理速度之间的取舍，为处理不确定输出提供了跨项目的稳定心智框架。

## 变化机制

### 从计划驱动转向证据驱动

```text
输出相对可预测
→ 可以较早固定实现方案
→ 主要按计划实现和验收

输出不确定
→ 中间结果携带新信息
→ 下一步依赖观察与评估
→ 开发成为自适应决策序列
```

AI 项目仍需要目标、边界和初始计划，但无法在开始时可靠决定全部干预步骤。^[inferred]

### 可靠性从组件属性转为系统结果

```text
不可靠模型
+ 高质量上下文
+ 有边界的工具与行动空间
+ workflow / harness / fallback
+ eval 与错误分析
+ 生产监控和治理
= 相对可靠的应用系统
```

可靠系统不要求模型永远正确，而要求系统能够发现错误、限制影响、必要时降级或转人工，并把新错误变成下一轮规则和测试。^[inferred]

### Grounding 把模型问题转化为证据供给问题

缺少信息、检索错误、表示不合适、数据过期或证据进入上下文的时机错误，都可能表现为“模型答不好”。改变数据表示、检索路径和上下文供应，有时比更换更大模型更有效。^[inferred]

### 自主性同时扩大行动空间与风险空间

只生成文本时，错误主要停留在答案；能够调用工具、写文件、操作系统和数据库之后，错误会改变外部状态。权限、sandbox、guardrail、回滚和治理因此随自主性一起升级。

### Eval 把随机试错变成定向搜索

```text
观察失败分布
→ 选择高价值问题
→ 提出干预
→ 测量改动
→ 保留有效变化
→ 更新评估标准
```

Eval 的价值不只是产生分数，而是提高“下一项开发工作值得做”的概率。^[inferred]

### 生产反馈把测试集变成风险记忆

真实用户、新输入分布和新攻击会产生未知失败。生产 traces、漂移和事故形成新 failure taxonomy，代表性案例进入回归集，再推动模型、数据、workflow 或产品修复。测试集因而是系统运行历史压缩出的风险记忆。^[inferred]

### 基础知识减少无效搜索

LLM 与 ML 基础不保证一次给出正确答案，但可以帮助工程师排除错误方向：不把数据缺失误判为模型能力不足，不用 LLM Judge 替代可直接执行的确定性检查，也不在 workflow 结构问题上只调整 prompt。^[inferred]

## 边界与开放问题

- 六项能力粒度不同：基础知识、数据供应、系统架构、开发方法和生产运营被放在同一层，更适合作为能力覆盖面，而不是严格分类。^[inferred]
- 文章强调相对于传统软件的不可预测性，但传统分布式系统、人机系统和复杂生产环境同样存在不可预测行为；两者是程度和来源差异，不是绝对二分。^[inferred]
- 文章没有给出从入门到熟练的学习顺序、深度标准和能力验证方法。
- 文章强调 eval 的中心地位，但不同阶段如何配置 eval 投入、何时停止优化、何时转向产品重构，仍需项目级判断。
- 数据治理、隐私、组织职责和用户体验虽被部分触及，但没有展开为独立能力层。

## Related

- [[wiki/sources/AI Engineering Skills Map Source Guide]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/concepts/Evaluation]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/LLM Inference Systems]]
- [[wiki/sources/AI Evals FAQ Source Guide]]
- [[wiki/sources/The Art of Loop Engineering Source Guide]]
- [[wiki/sources/The AI-Native SDLC Playbook Source Guide]]
