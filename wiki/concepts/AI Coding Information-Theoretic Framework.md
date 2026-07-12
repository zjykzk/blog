---
title: AI Coding Information-Theoretic Framework
type: concept
status: growing
category: concepts
summary: 用覆盖层与填补层区分 AI Coding 的两类失败：上下文还留下多少猜测空间，以及模型是否用符合私有业务的方向填补这些空白。
sources:
  - inline:ai-coding-information-theory-cheer-2026-07-12
provenance:
  extracted: 0.82
  inferred: 0.18
  ambiguous: 0.00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-07-12
tier: supporting
created: 2026-07-12T23:19:18+0800
updated: 2026-07-12T23:19:18+0800
aliases:
  - AI Coding 信息论框架
  - 覆盖层与填补层
relationships:
  - target: "[[wiki/concepts/Context Information Density]]"
    type: uses
  - target: "[[wiki/topics/Context Management]]"
    type: related_to
  - target: "[[wiki/topics/AI Harness]]"
    type: related_to
  - target: "[[wiki/topics/AI Memory]]"
    type: related_to
tags:
  - ai-coding
  - context
  - harness
  - memory
  - mechanism
---
# AI Coding Information-Theoretic Framework

AI Coding 的失败不能只用“上下文不够”解释。一个更有区分力的框架，是把问题拆成两个独立维度：模型还要猜多少，以及它会朝哪个方向猜。

## 两层框架

### 覆盖层：剩余猜测空间有多大

$$H(Y)=I(X;Y)+H(Y\mid X)$$

- $Y$ 是目标代码，$X$ 是模型可见上下文。
- $H(Y)$ 是任务的可能性空间，可通过缩小边界和拆分任务降低。
- $I(X;Y)$ 是上下文排除的错误可能性。
- $H(Y\mid X)$ 是模型看完上下文后仍需猜测的部分。

覆盖层失败时，输出往往含糊、摇摆或前后不一致。Rules、示例、验收标准、代码检索、RAG 和任务拆解的价值，取决于它们能否提高与目标输出的互信息，而不是增加多少 token。

因此覆盖层的工程指标不是上下文总量，而是：

$$\text{有效信息密度}\approx \frac{I(X;Y)}{|Context|}$$

这个指标无法在真实工程中被直接精确测量，但可以作为判断原则：一段上下文是否排除了真实的错误方向？^[inferred]

### 填补层：猜测方向是否贴合真实业务

模型会用训练先验 $P$ 填补 $H(Y\mid X)$，而项目真实约束属于业务分布 $Q$。低熵只表示模型在 $P$ 下很自信，不表示结果符合 $Q$。

填补层失败时，输出通常稳定、流畅、内部一致，却调用不存在的 API、破坏历史兼容、违反状态机或忽略团队约定。问题不是模型发散，而是模型自信地遵循了另一个世界的规则。

历史系统难以使用 AI，核心不只在代码多，而在私有约束不可见且 $P/Q$ 错配更大：字段命名、旧客户端兼容、错误码、执行顺序、灰度逻辑和架构审美常没有进入文档或测试。

## 为什么两层不能混为一谈

继续堆任务上下文，可能缩小 $H(Y\mid X)$，却不必然校准剩余空白的填补方向。反过来，项目规则即使准确，如果本次任务没有检索到相关部分，也无法形成足够互信息。

因此两层需要不同资产：

| 维度 | 主要问题 | 典型资产 | 失败形态 |
|---|---|---|---|
| 覆盖层 | 这次任务还留下多少猜测空间 | 任务边界、示例、验收标准、相关代码、精准 RAG | 含糊、摇摆、不一致 |
| 填补层 | 剩余空白会被哪套规则填补 | 项目 Rules、架构决策、业务约定、测试、review | 稳定、自信但业务错误 |

任务级信息通常每次不同；项目级规则可以被沉淀并复用。^[inferred]

## 上下文的负收益

理想信息论中，增加相关变量不会提高条件熵，但真实模型有有限注意力、位置偏差和检索误差。因此：

- 低密度上下文会偷走注意力。
- 错误或过期上下文会把填补方向推向旧规则。
- 冲突约束会迫使模型做概率折中。
- Agent 擅自扩大任务边界会直接扩大 $H(Y)$。

这使 [[wiki/concepts/Context Information Density]] 不只是压缩问题，也包含正确性、时效性、无冲突性和位置可用性。^[inferred]

## Harness 的信息论角色

[[wiki/topics/AI Harness]] 通过计划分解、状态管理、工具编排、验证门控、反馈、回退和人机交接，把静态上下文问题改造成多轮校准问题。

测试、lint、类型检查、运行日志和 review 会把真实世界的约束转成下一轮输入：它们既能缩小剩余猜测空间，也能纠正模型先验的方向。Harness 的价值不只是“给模型更多信息”，而是让现实反复进入生成循环。^[inferred]

但 Harness 有边界：从未表达、没有编码进代码/文档/测试的业务意图，无法通过自动化链路凭空恢复。系统应识别信息缺口并在价值判断、兼容取舍和不可逆决策处升级给人。

## 记忆的设计判据

[[wiki/topics/AI Memory]] 的价值不在存得多，而在能否召回少量高密度、相关、未过期的项目约束。

- 犯错记录、架构决策、业务约定和偏好边界可校准未来任务。
- 流水账会降低密度。
- 过期 API 和废弃模式会污染填补方向。
- 遗忘和版本治理因此是正确性机制，不只是存储优化。^[inferred]

## 工程判断清单

评估 Prompt、RAG、Memory、Skill、SDD 或 Harness 优化时，依次问：

1. 它是否缩小了目标任务本身的边界？
2. 它提供的信息是否真能排除错误方向？
3. 单位上下文里的有效信息是否提高？
4. 它暴露的是本次任务信息，还是长期项目规则？
5. 信息是否过期、错误、矛盾或位置上难以使用？
6. 有哪些空白仍会被模型公开先验填补？
7. 哪些缺口能由检索、执行和验证获得？
8. 哪些缺口属于未表达意图，必须交还给人？

## 边界

这是工程解释框架，而不是对具体代码任务的严格概率建模。真实任务中的 $X$、$Y$、意图和环境通常无法构造成可计算的联合分布；交叉熵也更适合作为“模型先验与业务真实约束错配”的类比，而非可直接测量的项目指标。

## Related

- [[wiki/sources/AI Coding 信息论框架 Source Guide]]
- [[wiki/concepts/Context Information Density]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Memory]]
- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/concepts/Executable Specification]]
- [[wiki/concepts/Verification Loop]]
