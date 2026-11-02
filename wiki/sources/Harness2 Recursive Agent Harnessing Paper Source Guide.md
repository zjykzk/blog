---
title: >-
  Harness2 Recursive Agent Harnessing Paper Source Guide
type: source
status: draft
category: sources
tags: [paper, arxiv, agents, harness, optimization]
sources:
  - https://arxiv.org/abs/2610.14224
  - /Users/zenk/Context/20261020T000245--paper-harness2-recursive-agent-harnessing__paper.md
  - conversation:2026-11-03
created: 2026-10-21T20:55:33+0800
updated: 2026-11-03T00:49:22+0800
summary: >-
  Harness² 论文指南：解释编辑者分工、同题行为对照与预算停止，并区分任务内 harness 顺序迭代和跨任务经验库递归。
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-21
aliases:
  - Harness²
  - Harness² Paper Source Guide
  - Recursive Agent Harnessing
relationships:
  - target: "[[wiki/topics/AI Harness]]"
    type: extends
  - target: "[[wiki/maps/Self-Evolving Agents Map]]"
    type: related_to
  - target: "[[wiki/concepts/Harness Ratchet]]"
    type: implements
  - target: "[[wiki/concepts/Verification Loop]]"
    type: related_to
---

# Harness2 Recursive Agent Harnessing Paper Source Guide

> Source: Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu, Bhavana Dalvi Mishra, Yifei Ming, Han Yu, Rujun Han, Chen-Yu Lee, and Tomas Pfister, *Harness²: Recursive Agent Harnessing for an Open World*, arXiv 2610.14224v1, 2026.

## What It Covers

Harness² 研究固定模型如何在没有 ground-truth answer、测试或可见 rubric 的新任务上改进自己的 [[wiki/topics/AI Harness|harness]]，并让改 harness 的能力随任务积累。

论文把问题拆成两层递归：

1. **任务内 harnessing**：在当前任务上运行原 harness，提出候选修改，在相同条件下试跑，再依据行为差异组合新 harness。
2. **任务间 harnessing**：任务结束后，把采用的 harness、适用条件和试跑证据提炼为经验，供后续任务提出和组合修改时检索。

这里的 harness 不只是 system prompt。它可以包含全局指令、领域手册、长期记忆、skills、scripts、工具说明、subagent delegation 和 hooks。模型参数、改进流程与选择规则保持不变，变化的是任务所用 harness 以及跨任务经验库。

## The Open-World Problem

已有 harness optimizer 常在一组带评分器的开发任务上搜索一个全局 harness，再把它部署到测试任务。真实工作却经常同时缺少三样东西：熟悉任务、标准答案和稳定 verifier。

这使两种直觉方案都不可靠：

- 每项任务现场修改、完成后丢弃，不能复用已经付费获得的诊断和试验；
- 直接把上一项任务的 harness 继承给下一项任务，会把任务特有规则和错误假设带入新环境。

Harness² 的回答不是永久继承上一版 harness，而是让每个新任务仍从基础 harness 开始，只把过去有证据支持的 harness 片段、脚本和经验作为编辑材料。它保留“为什么这样改”的证据链，而不把历史产物自动当成默认规则。

## Task-Level Loop: Propose–Probe–Compose

### 1. Establish a behavioral reference

系统先用当前 harness 执行任务，保留文件访问、工具调用、中间状态和最终产出的 trace。参考 trace 说明 agent 实际怎样工作，但不证明结果正确。

### 2. Propose complementary edits

两个编辑者从不同方向提出候选：

- generalist editor 处理规划、工具使用、信息管理、委派和复查等跨领域模式；
- domain editor 处理当前领域的知识、流程、约束和数据格式。

这种分工让候选集同时覆盖通用执行习惯与任务特有做法，而不是让多个编辑者生成近似建议。

分工依据是关注的问题，而非两个互斥的部件。领域手册本身属于 harness；两位编辑者各自交付一整份候选 harness，一份候选可以包含多处修改。

| 编辑者 | 诊断视角 | 制片任务中的候选修改 |
|---|---|---|
| 通用编辑者 | 跨领域执行习惯 | 加入清点输入、追溯数字的守则；加入重新打开产出的复查脚本 |
| 领域编辑者 | 行业知识、流程、约束和格式 | 加入日程、场地、人工与预算的核对手册；加入金额先去符号与逗号再计算的工具提示 |

这一例是两份候选、四处修改。最终采用多少处由 composer 依据 probe 决定；两位编辑者不分别拥有“通用 harness”和“领域手册”两块固定编辑区域。

### 3. Probe under matched conditions

每个候选 harness 在同一任务、同一模型与同一运行环境中重跑。系统比较候选 trace 与参考 trace，观察原问题是否消失、修改是否无效、是否产生新失败。

Probe 提供的是干预后的行为证据。它比“看起来应该有用”的静态编辑更可靠，但仍受执行随机性、共同盲点和单次样本影响。

### Runtime comparison and research evaluation

任务内优化与论文中的效果评测采用不同的反馈：

| 场景 | 比较对象 | 能看到的信号 | 用途 |
|---|---|---|---|
| 当前任务的 probe | 原 harness 与候选 harness 对同一任务的执行 | 文件访问、工具调用、中间状态与产出；看不到 benchmark 的 rubric 和分数 | 判断修改是否改变了目标行为、是否出现新问题 |
| 论文实验的事后评测 | 各方法在相同 benchmark 测试任务上的结果 | 评分器依据 rubric 得出的分数 | 衡量方法平均是否改善表现 |

因此运行时做的是同题对照试跑，并非拿一套可见评分的评测集反复选优。原执行没有核对跨文件数字，候选执行实际进行了核对，这是行为证据；数字是否真正正确仍需额外验证。

### 4. Compose evidence-backed changes

Composer 阅读原 harness、候选差异、参考 trace 和 probe traces，然后合并、修改、舍弃候选或保留原样。每一项采用都应对应可观察差异。

其原则可以压缩为：**只把有行为对比支持的修改带入新 harness。** 这与 [[wiki/concepts/Harness Ratchet]] 一致：失败只有改变了持久控制面，才会成为系统学习；Harness² 又增加一道要求——进入控制面的改变应先经过现场试跑。

## Harnessing-Level Recursion

任务结束后，reflection agent 回看整个改进过程，抽取“什么修改在什么情形下解决了什么问题，以及证据是什么”。只有 probe 支持的经验才进入库；某份最终结果被 selector 选中，并不能单独证明对应修改可迁移。

经验记录包含：

- 被采用的完整 harness；
- 可执行 scripts 和领域手册；
- 适用情形、观察到的问题与改动后果；
- 指向 probe 对比的支持证据；
- 用于后续检索的目录信息。

下一项任务的 proposer 和 composer 可以检索经验库，但新任务仍从基础 harness 起步。这种设计把“上一项任务的局部最优配置”与“可供下一项任务重新检验的经验”分开。

### Sequential iteration and second-level recursion

把 composer 产出的新 harness 接回下一轮 Propose–Probe–Compose，是第一层内部的 sequential scaling。第二层在任务结束后更新经验库，再让后续任务查阅它。

| 维度 | 第一层内部的顺序迭代 | 第二层递归 |
|---|---|---|
| 发生范围 | 同一个任务内部 | 不同任务之间 |
| 传递内容 | 新 harness 和本任务累积的改进记录 | 采用的 harness、脚本、适用条件与支持证据组成的经验库 |
| 下一次起点 | 本任务上一轮的新 harness | 新任务仍从基础 harness 起步 |
| 更新对象 | 当前任务的执行配置 | 后续 proposer、composer 可参考的经验 |

```text
第一层内，任务 A 的顺序迭代：
H_base → 提出/试跑/组合 → H_A1 → 提出/试跑/组合 → H_A2

第二层，跨任务的经验积累：
任务 A：H_base + 经验库 R_t → 第一层优化 → H_A 与改进记录
                                               ↓
                                      反思、提炼有证据的经验
                                               ↓
                                        更新经验库 R_(t+1)
                                               ↓
任务 B：H_base + 更新后的经验库 → 提出/试跑/组合 → H_B
```

任务 B 借用、改造 H_A 的片段或脚本，并在 B 上重新试跑；不会直接以 H_A 作为整个任务的起始 harness。第二层也没有重写 proposer、composer 的指令、模型参数或取舍规则，它通过经验库改变这些组件以后可参考的材料。

论文将两层更新形式化为：

```text
(H', e', ξ) = Φ(q_t, H, E; R_t)
R_{t+1} = Update(R_t, H*_t, D_t)
```

第一式表示当前任务、当前 harness、已有经验与改进记录共同产生修改后的 harness、新经验和执行结果；第二式表示任务完成后，用采用的 harness 与本次改进数据更新递归经验状态。形式化的重点不是符号本身，而是把“改当前执行配置”和“更新未来如何改配置”分成两个状态变化。

## Scaling the Improvement Budget

当预算从一次提高到多次时，论文比较两种扩展：

- **parallel scaling**：同一轮生成多组候选与 composition，得到多个交付结果；
- **sequential scaling**：把上一轮的新 harness 与累积记录交给下一轮继续改。

最终 selector 在不知道候选来自哪个 harness 的情况下，只根据任务要求和输入材料选择一个结果。增加预算通常继续提高分数，但会增加编辑、试跑、组合和选择的模型调用成本。

### Stopping conditions

论文主要用预先设置的预算控制任务内优化长度，并没有以“已证明正确”作为停止条件：

- 单步模式：执行一轮 Propose–Probe–Compose，再运行采用的 harness 交付结果。
- 并行扩展：按预算生成 k 对候选并试跑、组合，产生多份结果后选择一份。
- 顺序扩展：连续执行固定的 k 轮改进，最后选择一份结果。
- composer 可以在缺少支持证据时保留原 harness，reflection 也可以不写新经验；这些保守决定本身不构成正确性证明，也不等同于整个算法的自动收敛判据。

Probe 回答“哪些修改值得留”，预算回答“什么时候停止搜索”。外部 verifier 才可能对已编码的正确性性质提供判定。

真实系统可以补充连续多轮无新增稳定证据、高方差 probe 无法排除随机性、剩余问题只能由外部验证或人工判断处理等停止条件；这些是工程建议，不是论文已经实现或验证的自动停止规则。^[inferred]

## Evidence

论文在 WorkBuddy-Bench、JobBench 和 Legal Agent Benchmark 上测试 Gemini 3.5 Flash 与 GLM-5，并从 OpenCode、Codex 两种起始 harness 出发。Harness² 与原 harness、ReasoningBank、Meta-Harness 和每项任务从零优化的 Harness Scaling 比较，每种设置重复三次。

主要结果包括：

- 单步 Harness² 在两种模型、两种初始 harness 和三套 benchmark 的报告设置中都超过各自起点；
- 最大单步提升分别达到 WorkBuddy-Bench `+11.5`、JobBench `+4.5`、LAB partial pass rate `+11.8` percentage points；
- GLM-5 + OpenCode 在 WorkBuddy-Bench 上从 `64.2` 提高到 `75.7`，超过 Gemini 使用原 harness 的 `72.4`；
- parallel 与 sequential budget scaling 在代码和办公任务上随预算增加继续上升，论文报告的 Harness² 设置位于其成本—提升比较的 Pareto frontier；
- 去掉经验库、编辑者分工或 probe 后的 composition，WorkBuddy-Bench 与 JobBench 都下降；
- 不看参考 trace、不 probe、只凭任务直接改 harness 时，代码任务从 `73.4` 降到 `63.2`。

这些结果支持“execution evidence 是 harness 编辑的重要筛选器”，但不能推出 Harness² 总能找到正确修改。论文规模仍是几十到一百个任务、每种设置三次重复，多数得分来自 AI judge。

## What the Ablations Reveal

消融实验共同指向三条机制：

1. **现场证据比静态直觉可靠**：直接编辑可能明显伤害表现。
2. **候选多样性有价值**：generalist/domain specialist 分工优于同数量的无角色编辑者。
3. **经验库的价值取决于证据密度**：更大预算产生的经验库即使脱离在线 probe 也能带来提升，JobBench 经验迁移到 WorkBuddy-Bench 也有小幅收益。

这说明经验库不是普通的“成功案例记忆”。它的最小单位应是修改、适用条件与行为证据的组合。^[inferred]

## Verification Boundary

Harness² 最重要的边界是：**behavioral contrast is not correctness verification**。

同条件 probe 能说明改动让行为发生了什么变化，却不能证明交付物满足真实意图。几种失败仍然存在：

- selector 可能误判。论文案例中，它在事后分数为 `95, 85, 85, 80, 55` 的候选里选择了 `55` 分结果；
- 多个候选可能共享同一个错误假设，因此相互对比无法暴露共同盲点；
- 单次执行的随机性可能被误认为修改效果；
- AI judge 与 benchmark rubric 只覆盖被表达出来的性质，不能代替真实环境 validation。

因此 Harness² 的 probe 属于 [[wiki/concepts/Verification Loop]] 的一层证据，而不是最终真值函数。高风险任务仍需要独立测试、外部数据、领域专家或真实结果反馈；高方差任务还需要重复 probe。^[inferred]

## Relationship to Adjacent Systems

| System | What changes | Feedback regime | Transfer mechanism |
|---|---|---|---|
| Meta-Harness | executable harness code | scores and raw evaluation traces over optimization tasks | selected global harness |
| Harness Scaling | task-specific harness | same-task execution evidence | none |
| ReasoningBank | retrieved reasoning strategies | distilled prior task experience | strategy memory |
| Harness² | task-local harness plus edit experience | same-task behavioral contrast without visible ground truth | evidence-backed harness and experience library |
| Dream-RSI | search scheduling code | replay over historical discovery trees | updated exploration policy |

Harness² 因而位于 [[wiki/sources/Meta-Harness Paper Source Guide|Meta-Harness]] 与 [[wiki/sources/Dream-RSI Paper Source Guide|Dream-RSI]] 之间：它像前者一样把 harness 视为可优化对象，像后者一样让历史反馈改进未来搜索，但把主要学习信号放在开放任务的现场行为对比，并显式保留跨任务经验。

## Engineering Implications

- harness 变更记录应同时保存 diff、触发问题、试跑 trace、采用理由和适用边界，而不只保存最终 prompt 或 script；
- 任务特有 harness 不应自动成为全局默认值，应先作为带 provenance 的经验供后续检索和复验；
- proposer、composer、selector 和 verifier 是不同责任，尤其不应让提出修改的组件独占最终评估；
- 没有 ground truth 时，可以用 matched execution 缩小不确定性，但必须把“看见变化”与“证明正确”分开；
- budget scaling 应同时报告质量、调用量、token 与 wall-clock cost，不能只报告最好分数。^[inferred]

## Open Questions

- 同一候选需要多少次 probe，才能把真实效果与执行随机性分开？
- 经验库如何检测冲突、过期、领域错配和共享错误前提？
- selector 如何接入更独立的外部信号，避免凭表面完整度挑错结果？
- 长期运行时，经验库是否会膨胀成检索噪声或隐性规则债务？
- 对权限、安全和合规相关 harness 组件，哪些修改必须经过人工批准？

## Algorithm Demonstration

本地演示视频约 3 分 22 秒，以制片任务展示参考运行、提出、试跑、组合、预算选择与经验库更新。

- [观看 MP4](../../artifacts/harness2-algorithm/harness2-algorithm-1080p.mp4)
- [打开带章节跳转的播放器](../../artifacts/harness2-algorithm/preview.html)

视频是机制示意动画；轨迹步骤、probe 对比表与被舍弃的修改作了教学简化，不能视为论文系统的实际执行录屏或复现实验。

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/maps/Self-Evolving Agents Map]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Verifier Hierarchy]]
- [[wiki/sources/Meta-Harness Paper Source Guide]]
- [[wiki/sources/Dream-RSI Paper Source Guide]]
- [[wiki/sources/Continual Learning for AI Agents Source Guide]]
