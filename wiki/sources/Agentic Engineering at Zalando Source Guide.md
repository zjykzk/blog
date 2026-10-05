---
title: >-
  Agentic Engineering at Zalando Source Guide
category: sources
type: source
status: draft
tags: [article, agents, ai-coding, software-engineering, organization]
aliases:
  - "Agentic Engineering at Zalando: A Snapshot"
  - Zalando Agentic Engineering
  - Zalando 智能体工程实践
sources:
  - https://engineering.zalando.com/posts/2026/08/agentic-engineering-at-zalando-a-snapshot.html
  - conversation:2026-09-21
source_url: https://engineering.zalando.com/posts/2026/08/agentic-engineering-at-zalando-a-snapshot.html
published: 2026-08
created: 2026-09-21T23:22:10+0800
updated: 2026-09-21T23:22:10+0800
summary: >-
  Zalando 的 2.5 年实践表明，Agentic Engineering 是统一基础设施、分布式实验、数据反馈、风险治理与组织学习共同组成的社会—技术闭环。
provenance:
  extracted: 0.70
  inferred: 0.28
  ambiguous: 0.02
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-09-21
tier: supporting
relationships:
  - target: "[[wiki/concepts/Agentic Engineering]]"
    type: related_to
  - target: "[[wiki/topics/AI Harness]]"
    type: uses
  - target: "[[wiki/concepts/Agent Skill]]"
    type: uses
  - target: "[[wiki/concepts/Verification Loop]]"
    type: uses
---

# Agentic Engineering at Zalando Source Guide

> Source: Zalando Engineering, [Agentic Engineering at Zalando: A Snapshot](https://engineering.zalando.com/posts/2026/08/agentic-engineering-at-zalando-a-snapshot.html), 2026-08

## What It Covers

这篇文章回顾 Zalando 在 250 多个工程团队中推进 Agentic Engineering 的 2.5 年实践。它不是某个 Coding Agent 的使用教程，而是一份组织级现场报告：怎样让不同团队低摩擦地试验模型和工具，同时保持成本、安全、质量和责任链可见；又怎样从真实使用数据中识别有效实践，再把它们沉淀成规则、Skill、培训和平台能力。

文章覆盖的实践包括统一 LLM Proxy、Chat UI 与 CLI、MCP 认证、供应商独立、PR 与代码复杂度观测、风险型 PR 审批、Agent Session 分析、Skill 集合、Tech Radar、Guild、Hackathon、Labs、仓库 AI readiness，以及面向 Agent 平台的 Identity Broker。

## Central Thesis

Agentic Engineering 不是“给工程师安装 Coding Agent”，而是把组织改造成一个能够安全试错、观察结果、修正行为并把经验制度化的社会—技术系统。^[inferred]

```text
统一基础设施
    ↓
降低实验门槛
    ↓
允许团队多路线探索
    ↓
采集使用、交付与代码数据
    ↓
识别收益、风险和有效实践
    ↓
沉淀为规则、Skill、培训和平台
    ↓
在保留选择权的前提下扩大采用
    └──────────────────────↺
```

这个闭环同时避免两个极端：过早指定唯一工具会锁死尚未成熟的方向；完全放任则会失去安全边界、成本控制、经验复用和责任追踪。^[inferred]

## Core Concepts

### 统一访问层：LLM Proxy

Zalando 的 ML 平台团队在 2024 年 1 月部署了基于 LiteLLM 的 API Proxy，为 OpenAI、AWS Bedrock 和 Google Vertex 等模型提供统一入口。这个 Proxy 同时承担：

- 通过 MAU、WAU、模型和 User-Agent 观察采用情况；
- 通过 post-call hooks 匿名追踪成本；
- 通过 pre-call hooks 和 User-Agent 强制客户端升级；
- 关闭退役模型，处理长期不更新配置的用户；
- 自动注入 Prompt Cache 检查点，降低自定义 Agent 的调用成本；
- 用 `--max_requests_before_restart` 每 2 万次请求重启，缓解稳定性和内存泄漏问题。

文章报告：六个小型 Pod（每个 2 CPU、4 GB 内存）即可服务约 2,000 MAU。

Proxy 因而不只是流量转发层，而是组织的 Agent 控制面：用户保留模型和工具选择权，平台保留认证、策略、成本与行为可见性。^[inferred]

### 安全的工具与 MCP 接入

统一 API 之外，Zalando 还提供 Chat UI、自研 CLI、本地认证代理和 MCP 适配。CLI 从 2024 年 8 月 Hackathon 的维护脚本演化为社区共同维护的工具，逐步加入多轮对话、文件上下文、Agent 模式、MCP、Bearer Token 自动注入、HTTP-to-stdio MCP Proxy 和多种 Coding Agent 的安全配置安装。

这套设计针对两个常见缺口：

1. 工具使用通用 User-Agent，平台无法识别真实客户端、来源仓库和版本；
2. 工具只支持静态凭证或环境变量，Token 过期后需要人工刷新和重启应用。

本地代理与插件把短期凭证注入运行时，避免将秘密硬编码到配置文件。内部 MCP Server 还受到默认 Ingress OAuth Filter 保护。这一点随着用户群从工程师扩展到安全直觉不同的非工程角色而更重要。

### 供应商独立与延迟收敛

Zalando 没有集中规定唯一 Coding Agent，而是通过 Proxy 接入多模型，并为不同 Agent 维护参考配置和模型提供方插件。工程师可以依据模型、IDE/CLI 偏好和任务切换工具。

文章同时观察到：工具能力相近、技术切换成本较低，并不意味着人会轻易切换。用户会依恋熟悉的交互和特定模型的表达风格。供应商独立因此既是协议和配置问题，也是心理迁移问题。^[inferred]

组织采用的治理姿态是延迟收敛：在生态高速变化期，优先建立透明度、交换机制和安全边界；等实践反复证明有效后，再进入标准配置、Skill、Tech Radar 和正式培训。^[inferred]

### Agent 可观测性

Zalando 同时观察 Agent 的输入侧过程和输出侧结果：

| 观察面 | 例子 | 能回答的问题 |
|---|---|---|
| 接入 | MAU、WAU、User-Agent、版本、模型 | 谁在用什么，旧客户端是否仍存在 |
| 经济性 | Token、成本、Prompt Cache 读写 | 调用是否浪费，缓存是否有效 |
| Session | Prompt 模式、任务类型、非必要调用 | 人与 Agent 的协作过程怎样失效 |
| 交付 | PR 大小、Lead Time、风险等级 | AI 是否改变交付行为 |
| 代码 | 圈复杂度、重构拐点 | AI 是否加快复杂度形成或消解 |
| 元数据 | Commit Message 长度与内容 | 自动生成是否污染工程记录 |

文章举出一个 Session 诊断案例：某位 OpenCode 用户的 Cache Hit Ratio 低于 30%，而预期通常高于 80%；团队通过跨 Session 解析器定位后，确认它不是全体用户的系统性缺陷。

Git 记录最终产物，Agent Session 则暴露产物的形成过程。Session 数据因此成为新的工程过程数据。^[inferred]

### AI 是工程系统的放大器

Zalando 在 PR 数据中观察到 `[100,500)` 行 PR 持续增加，Sonnet 4 于 2025 年第二季度发布后，`[500,1k)` 与 `[1k,2k)` 等更大区间也开始增长。不同团队对此采用不同约束：有的内部约定固定 PR 上限，有的接受较大 PR，转而使用 GitHub 语义分组或 Linear Reviews。

四个 Java/Go 代码库的 Commit 级复杂度分析显示，Coding Agent 进入后，总圈复杂度出现可辨认的拐点；从一开始就充分采用 Agent 的新 Go 项目，复杂度快速累积后增速趋缓。作者没有把这一走势直接解释为好或坏，而是等待时间验证它是否代表“有界微服务被更快建成”。

文章据此反复强调，AI 会同时放大好实践和坏实践。可以把它整理成一个启发式关系：

```text
AI 产出效果 ≈ Agent 能力 × 工程系统质量
```

这个公式是对文章案例的综合，不是作者给出的正式度量。^[inferred]

### 风险型 PR 审批

Zalando 在 PR 创建时根据发布风险将变更分为低、中、高三档。规则来自生产事故和常见中断原因，并针对本地技术栈、部署清单和配置文件制定：

- 文档变更属于低风险；
- 破坏向后兼容属于中风险，需要另一位人类判断业务理由；
- 可能破坏配置的拼写错误属于高风险。

文章报告约 33% 的 PR 属于低风险并由 Bot 自动批准；这些 PR 相比全部 PR 的 Lead Time 降低约 20%–40%。

更重要的二阶效果是，审批差异改变了作者行为：工程师开始把向后兼容、可快速发布的变更拆成低风险 PR，把删除旧字段等中风险清理留到后续。治理工具不只裁决 PR，还通过反馈重塑 PR 的组织方式。^[inferred]

### Agent Skill 作为可执行组织知识

Zalando 将中央 Agent Skill 集合按 Plugin 分组，覆盖数据、工程、前端、SRE、语言和基础设施迁移等场景。组织鼓励团队贡献被实践证明有用的 Skill；中央集合又反过来成为其他团队的参考实现，传播 Plugin CI 校验、Skill 与脚本的职责分离、OAuth Token 应放在哪一层等经验。

传统知识传播依赖“专家写文档、其他人阅读并人工执行”；Skill 将经验推进成 Agent 可以按需加载和执行的工作规范。^[inferred] 这与 [[wiki/concepts/Agent Skill]] 和 [[wiki/topics/AI Skills Workflow]] 的知识复用模型直接相连。

### 引导式实验与知识成熟流水线

Zalando 使用多种知识交换载体，分别适配不同成熟度：

- LLM Guild：每周一小时，适合早期采用者交换最新实验和行业变化；
- Guided Hackathon：预设约十个主题，每题给出目标、考虑项、排除项和潜在协同，4–6 人团队用 2–3 天并行探索；
- GenAI Labs：约 20 人、1–4 小时、双人练习的现场实验课；
- Monthly Training：把反复有效的 Lab 转成标准课程，由往期参与者扩展讲师池；
- Tech Radar 与开发者门户：为已经形成共识的实践、工具和政策提供组织入口。

这形成一条知识成熟流水线：

```text
个人或团队实验
  -> Guild 交换
  -> Hackathon / Lab 对照验证
  -> Skill / 参考配置
  -> 固定培训
  -> 平台默认能力
```

这是从全文实践抽出的组织学习结构。^[inferred]

Hackathon 还承担反向诊断平台的功能。例如，一组构建 MCP Server，另一组被明确要求绕开 MCP、从 API 定义目录搜索并生成调用；后一路线暴露了 API Spec 缺少 hostname 等质量问题，使机器无法生成可运行调用。

### AI Readiness

Zalando 下一步计划扫描每个仓库的 AI readiness，并把它与交付状态和代码库健康度关联。由于公司主要采用微服务多仓库，而非少数高杠杆 Monorepo，Agent 能否稳定工作更依赖每个仓库是否暴露清晰上下文、自动验证、可操作结构和及时反馈。^[inferred]

文章认为 AI readiness 评估还有一个副作用：过去因为 ROI 不明显而被推迟的工程最佳实践，现在会因为 Agent 能重复消费它们而获得新收益。

### Identity Broker 与委托链

Zalando 正在构建 Agent Platform，使团队无需自行处理沙箱即可定义和部署 Agent。平台采用包括 kagent 在内的 OSS 组件，并建设 Identity Broker：

- 记录 on-behalf-of 调用的委托链；
- 在不同 OAuth2 基础设施之间进行中介；
- 提供 Token Vault；
- 位于 Agent 与 MCP Server、Agent 与 Agent 的调用路径中。

当 Agent 从个人辅助工具变成能调用内部系统的行动主体时，系统必须能回答最初发起者、当前代理对象、权限传递路径、Token 适用目标和责任追溯问题。^[inferred] 这说明规模化 Agentic Engineering 的深水区不是代码生成，而是身份、授权、沙箱和责任边界。^[inferred]

## Concept Structure

全文可以整理成五层结构：

```text
5. 规模化治理
   风险审批 / 法律审查 / AI 使用发现 / Agent Platform / Identity Broker
                              ↑
4. 组织学习
   Guild / Hackathon / Lab / Training / Skills / Tech Radar
                              ↑
3. 反馈系统
   使用率 / 成本 / Cache / Session / PR / 复杂度 / Lead Time
                              ↑
2. 选择权
   多模型 / 多工具 / 参考配置 / 供应商独立 / 延迟收敛
                              ↑
1. 基础设施
   LLM Proxy / CLI / Chat UI / MCP / Auth Proxy / Token Injection
```

五层不是相互独立的功能清单，而是一条依赖链：没有基础设施就难以普及；没有选择权就难以探索；没有观测就无法判断探索结果；没有组织学习就无法把局部经验放大；没有治理就无法把 Agent 的行动范围扩展到高风险系统。^[inferred]

## Four Productive Tensions

| 张力 | Zalando 的处理方式 |
|---|---|
| 自由探索 vs 中心治理 | 工具与模型自由选择，但统一接入、认证、配置入口和可观测性 |
| 交付速度 vs 代码质量 | 不统一压慢所有 PR，而是按发布风险分配审批强度 |
| 快速变化 vs 知识标准化 | Guild/Hackathon 保持探索，成熟后再转为 Skill、Radar 和培训 |
| 本地自主 vs 组织复用 | 团队自由创造，中央集合传播反复有效的实践 |

这些张力没有被一次性消除，而是通过反馈机制持续调节。可以概括为：对变化快的部分保持可替换，对风险高的部分建立中心控制，对已经验证的部分进行标准化。^[inferred]

## Reasoning Flow

文章的推理不是从抽象理论向下演绎，而是从 2.5 年组织实践中向上归纳：

1. **确认高度不确定。** 模型、工具和实践快速变化，250 多个团队处在不同采用阶段，因此中央团队无法提前指定唯一最优方案。
2. **建立低摩擦且可观测的底座。** LLM Proxy、CLI、认证代理和 MCP 接入让广泛实验成为可能，又避免组织失去使用、成本和版本可见性。
3. **允许多路线并行探索。** 多模型、多工具、Guild 和 Guided Hackathon 增加局部实验数量，让方案通过真实使用竞争。
4. **从数据识别实际影响。** 观察从“有没有人用”递进到“怎样用”“工程行为如何变化”“代码与交付结果如何变化”。
5. **承认双向放大。** PR 变大、复杂度拐点和元数据污染说明 AI 不自动带来成熟度；平台、预览环境和验证能力也会被 AI 放大。
6. **把发现转换成约束。** 风险审批、客户端版本门禁、模型淘汰、Cache 注入、安全 MCP 认证和 Commit 限制把经验写进系统，而不只依赖个人自觉。
7. **把成熟做法转换成组织资产。** 有效实践从实验和分享进入 Skill、参考配置、培训、Radar 与平台默认值。
8. **寻找新的规模瓶颈。** 当代码生成与工具采用扩大后，问题转移到仓库 readiness、批量变换、云端沙箱、身份委托和多 Agent 授权。

推理的终点是：下一阶段的差异化能力不只来自更强的模型，而来自让 Agent 可以安全行动、被持续观察、承担清晰责任并从组织反馈中进化的运行环境。^[inferred]

## Evidence and Boundaries

文章提供的是单个大型技术组织的实践快照，不是对 Agentic Engineering 效果的控制实验。应区分三类证据：

- **直接运行数据**：约 2,000 MAU、六个小型 Pod、33% PR 自动批准、低风险 PR Lead Time 降低 20%–40%、PR 大小分布和代码复杂度曲线；
- **行为观察**：工程师会为争取低风险等级主动拆 PR，用户对工具和模型形成心理依赖，培训参与者会用 Agent 绕过本应亲自练习的新技能；
- **未来计划**：仓库 AI readiness Scanner、面向非工程师的原型发布入口、Agent Platform、Identity Broker、Local Sandboxing 与自动模型路由。

这些数字主要来自 Zalando 内部数据，文章没有公开完整样本定义、混杂变量控制或因果识别方法。PR 变大、复杂度变化与 Agent 采用存在时间相关性，但不等于 Agent 是唯一原因。^[ambiguous]

文章还给出一个重要学习边界：当培训目标是让人掌握底层概念或手工技能时，应明确哪些练习必须手写，因为 Coding Agent 虽能加快结果生成，却可能抑制学习。

## Open Questions

- 仓库 AI readiness 应由哪些可复现指标组成，怎样避免把“易被 Agent 修改”误当成“软件质量高”？
- 风险审批 Bot 的误判率、漏判率和事故结果如何长期校准？
- 当 Agent Session 成为工程过程数据时，怎样同时处理隐私、员工评估误用和安全审计？
- 中央 Skill 集合如何处理版本、所有权、失效、供应链安全和团队特例？
- Identity Broker 如何表达多级委托中的最小权限、撤销、审计和责任归属？
- 当开放模型与开放工具成熟后，模型自动路由应依据成本、质量、数据边界还是任务风险？

## Related

- [[wiki/concepts/Agentic Engineering]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/concepts/Harnessability]]
- [[wiki/concepts/Attention as the Scarce Resource]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/sources/The AI-Native SDLC Playbook Source Guide]]
- [[wiki/sources/Coding with AI Source Guide]]
