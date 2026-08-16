---
title: >-
  Code as Agent Harness Paper Source Guide
type: source
status: draft
category: sources
tags: [paper, arxiv, agents, harness, reasoning]
sources:
  - https://arxiv.org/abs/2605.18747
  - /Users/zenk/Documents/notes/20260812T222839--paper-code-as-agent-harness__paper.org
created: 2026-08-12T23:17:18+0800
updated: 2026-08-12T23:17:18+0800
summary: >-
  Source guide for arXiv 2605.18747, framing code as the executable, inspectable, and stateful medium through which agents reason, act, preserve state, verify progress, and coordinate.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.70
lifecycle: draft
lifecycle_changed: 2026-08-12
aliases:
  - Code as Agent Harness
  - 代码作为智能体骨架
  - 代码从答卷变骨架
relationships:
  - target: "[[wiki/topics/AI Harness]]"
    type: related_to
  - target: "[[wiki/concepts/Formalization]]"
    type: implements
  - target: "[[wiki/concepts/Verification Loop]]"
    type: extends
---

# Code as Agent Harness Paper Source Guide

> Source: Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei et al., *Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems*, arXiv 2605.18747v1, 2026.

## What It Covers

这篇综述重新解释代码在 Agent 系统中的位置：代码不只是模型生成的最终产物，也是 Agent 用来推理、行动、表示环境、保存状态、观察反馈和验证进度的运行媒介。

论文采用三层结构梳理相关工作：

1. **Harness interface**：代码如何连接推理、行动和环境建模。
2. **Harness mechanisms**：规划、记忆、工具使用、反馈控制与优化如何支撑长任务。
3. **Scaling the harness**：共享代码物件如何支撑多 Agent 的角色分工、协作和验证。

它是一篇领域地图，而不是报告新 benchmark 结果的实验论文。

## Core Claim

论文的中心命题是：Agent 自主性的瓶颈不只在模型能力，也在把模型输出连接到长时行动和持久状态的系统是否可靠。

Agent harness 指包在模型外面的软件层，包括工具、API、沙箱、记忆、验证器、权限边界、执行循环和反馈通道。它把一次性、无状态的模型调用变成可以持续执行任务的 Agent。

论文进一步把长任务系统拆成三个相互耦合的元素：

- **模型内部能力**：推理、感知、规划、模拟和评价；
- **系统预置的 harness 设施**：工具、API、沙箱、记忆系统、权限、telemetry 和 workflow；
- **Agent 自己创建和演化的代码物件**：回归测试、临时工具、DSL 程序、可执行 workflow、可复用 skill 和中间程序状态。

第三类是论文最有辨识度的观察。代码不只在任务结束时成为补丁或答案；Agent 会在执行途中创建代码物件，再执行、观察、修改、保存和分享它们。这些物件成为推理和协作的外部支架。^[inferred]

## Why Code Can Be a Harness Interface

论文给代码三个关键性质：

- **Executable**：模型提出的过程可以被解释器、运行时或工具真实执行；
- **Inspectable**：变量、控制流、测试结果、trace 和 runtime error 能暴露中间过程；
- **Stateful**：持续变化的 repo、程序状态和执行物件能保存任务进度。

这三个性质使代码能够把模型的瞬时输出接到真实状态变化上：

```text
模型提出过程
-> 代码执行
-> 环境返回 trace / error / test result
-> harness 保存状态并反馈
-> 模型修正下一步
```

这并不意味着推理的每一步都要写成代码。论文明确划定范围：原始感知、物理状态、人类意图和模型内部隐式推理本身不是代码；代码只能选择性地表示、检查或作用于它们。

这一边界与 [[wiki/concepts/Formalization]] 一致：适合交给代码的部分，需要先被表达成对象、状态、规则与判定条件；形式化能保证规则被稳定执行，但不能自动保证规则正确刻画现实。^[inferred]

## Harness Interface

### Code for Reasoning

代码把部分中间推理外部化成可执行计算。模型负责提出程序，解释器、符号求解器或验证器负责执行和反馈。

这类工作包括：

- program-delegated reasoning；
- formal verification and symbolic reasoning；
- iterative code-grounded reasoning。

它解决的主要问题不是“模型完全不会想”，而是模型不擅长忠实执行算术、符号和逻辑步骤，也难以仅靠自然语言暴露可检查的中间状态。

### Code for Acting

生成的程序可以充当策略、工具调用、行为树或可复用 skill，把高层意图变成 GUI、OS、机器人和软件环境中的动作。

在这里，代码不是答案，而是 Agent 对环境施加影响的动作接口。

### Code for Environment Modeling

程序状态、repo、trace、模拟器、测试和日志可以表示环境状态、动态和反馈。

例如，一个修复 GitHub issue 的 Agent 可以把：

- repo 当前 diff 当作任务状态；
- failing test 当作环境反馈；
- stack trace 当作可检视证据；
- regression test 当作 Agent 自己创建的验收物件。

代码因此同时承接思考、行动和观察，而不是只承接最终实现。

## Harness Mechanisms

论文把长任务可靠性拆成四类机制：

- **Planning**：任务分解、结构定位、轨迹搜索和 workflow orchestration；
- **Memory**：工作状态、repo 证据、跨任务经验、长期记忆和多 Agent 共享状态；
- **Tool use**：API、repo、终端、浏览器、沙箱和验证工具的受治理调用；
- **Feedback-driven control**：静态分析、运行时报错、测试和人类反馈推动反复修正。

记忆部分有一条重要的反直觉结论：历史记录不是越多越好。未经治理的经验会带来语义噪声、错误传播和误检索；长期 Agent 需要 write gate、结构化 retrieval key、provenance-preserving compaction 和 state offloading。

这条结论支持 [[wiki/topics/AI Memory]] 的治理视角：记忆不是更大的上下文，而是决定什么留在活跃上下文、什么压缩、什么放进外部持久状态的管理层。^[inferred]

## Scaling to Multiple Agents

多 Agent 系统把代码从个人支架变成共享工作台。

论文从三个维度整理协作：

- 角色：manager、planner、coder、reviewer、tester；
- 方式：programming、repair、debate、red-teaming 和 adversarial interaction；
- 拓扑：centralized、distributed、streaming。

repo、测试、trace 和结构化 workflow 为不同角色提供共同状态。协作不只依靠自然语言对话，也依靠可以被共同执行、检查和修改的代码物件。

## Verification Boundary

代码“可执行”不等于结果“符合真实意图”。

可以分成四层判定：

| 判定 | 主要判断者 | 能说明什么 |
|---|---|---|
| 程序能否运行 | 解释器、运行时 | 语法、类型和运行条件是否成立 |
| 是否满足编码规则 | 测试、断言、静态检查 | 实现是否满足已写下的性质 |
| 结果是否稳健 | 交叉验证、reviewer、held-out evaluation | 是否存在明显遗漏和过拟合 |
| 规格是否对准现实 | 人、领域证据、真实环境反馈 | 意图、口径、价值和风险是否正确 |

因此，论文中的 verification 应与 [[wiki/concepts/Verifier Hierarchy]] 和 [[wiki/concepts/Executable Specification]] 一起理解：执行反馈可以很强，但只对已经形式化的性质负责；规格本身仍需要 validation。

## Open Challenges

论文列出的主要开放问题包括：

- 不只看最终任务成功率，还要评估轨迹、成本、恢复和中间状态；
- 在反馈不完整时验证 Agent 行为；
- 改进 harness 时避免已有能力回归；
- 多 Agent 之间维护一致的共享状态；
- 对高风险动作保留人类监督；
- 把 harness 扩展到多模态和物理环境。

这些问题共同说明：代码让验证变得可操作，却不会自动产生完整的真值函数。真实任务往往没有现成标准答案，环境反馈也可能不完整。

## Critical Reading

论文的优势是提供一个清楚、可迁移的组织框架，把代码推理、工具使用、记忆、反馈和多 Agent 协作放进同一张图。

它的主要局限是实证较弱。论文假设 harness 会持续成为自主性的关键瓶颈，但没有证明模型能力增强不会消解部分 harness 机制。taxonomy 的层次也存在交叠：记忆既是机制，也可能是接口或多 Agent 共享基础设施。

因此，这篇论文更适合作为“如何看 Agent 系统”的概念地图，而不是“harness 一定比模型更重要”的最终证据。^[inferred]

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Formalization]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Verifier Hierarchy]]
- [[wiki/concepts/Executable Specification]]
- [[wiki/concepts/Agentic Control Loop]]
- [[wiki/sources/Agent Harness Engineering Survey Source Guide]]
- [[wiki/sources/Agentic Reasoning for LLMs Paper Source Guide]]
