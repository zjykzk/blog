---
title: Formalization
type: concept
status: growing
category: concepts
tags: [thinking, reasoning, formal-language, software-engineering, verification]
sources:
  - conversation:2026-08-12
  - https://arxiv.org/abs/2605.18747
created: 2026-08-12T23:17:18+0800
updated: 2026-08-12T23:17:18+0800
summary: >-
  形式化把依赖背景、直觉和临场理解的问题，改写成对象、表示、规则与判定标准明确的结构，使推理能够被稳定委托、执行和检查。
provenance:
  extracted: 0.76
  inferred: 0.22
  ambiguous: 0.02
base_confidence: 0.68
lifecycle: draft
lifecycle_changed: 2026-08-12
aliases:
  - 形式化
  - Formalization
relationships:
  - target: "[[wiki/concepts/Knowledge Formalization Gradient]]"
    type: related_to
  - target: "[[wiki/concepts/Executable Specification]]"
    type: related_to
  - target: "[[wiki/concepts/Verification Loop]]"
    type: related_to
---

# Formalization

形式化是把依赖背景、直觉和临场理解的问题，改写成一套对象明确、表示明确、规则明确、结果可判定的结构。

## What It Is

形式化不是单纯把话说得更详细，也不等于直接写代码。它至少完成四件事：

1. 指定讨论什么对象。
2. 规定对象如何被表示。
3. 规定对象之间允许怎样判断或变换。
4. 规定什么结果算成立、成功或失败。

例如，“找出金额比较大的可疑订单”仍需要执行者临场猜测“比较大”和“可疑”的含义。形式化后可以写成：

```text
对象：订单
属性：金额、账户、下单时间、状态
大额：金额 > 5000 元
可疑：金额 > 5000 元，并且同一账户 10 分钟内下单不少于 5 次
缺失值：金额或账户为空时转人工审核
```

从原话到这组对象、条件和异常规则，是形式化；把它进一步写成程序，是编码与执行。

## Why It Is Needed

形式化的根本作用，是减少委托过程中的自由解释。

人面对含糊任务时，会调用背景知识、语境和常识补全缺口；机器、陌生执行者和跨时间协作无法稳定共享这些隐含判断。要让任务能够被重复执行，必须提前外显执行时需要的区别：

```text
现实与人的意图
-> 选择哪些区别重要
-> 固定对象、表示、规则和判定条件
-> 执行者按规则改变状态
```

因此，形式化可以被理解为“从意义到机械因果的翻译层”。它把“理解后酌情处理”压成“满足条件便行动”，让执行不再完全依赖执行者当下的领会。^[inferred]

这也是为什么形式化是可靠委托的代价。自己临场处理时，大量规则可以留在脑中；把任务交给程序、组织、另一个 Agent 或未来的自己时，隐含判断必须逐步外显：

```text
口头意图
-> 术语定义
-> 操作清单
-> 明确规则
-> 形式规格
-> 可执行程序
-> 可机器验证的证明
```

越往后，解释空间越小，一致性和自动化程度越高；表达成本也越高。

## How It Works

形式化通常经过三个动作。

### 选择和表示

现实包含无限细节，形式系统不能复制整个现实。它先根据目的选择需要保留的变量，再把对象压成符号、数据结构或状态。

例如，一笔真实订单涉及买卖双方、物流、税务、情绪和历史，但风控规则可能只保留金额、账户、时间和状态。形式化从一开始就是有目的的抽象，不是现实本身。^[inferred]

### 固定边界与规则

形式化把连续、含糊的意义切成可区分状态，并固定状态之间的关系：

```text
金额 <= 5000 | 金额 > 5000
最近 = 过去 10 分钟
多次 = 不少于 5 次
条件 A 且条件 B -> 标记为可疑
```

机器不需要理解“可疑”的全部社会意义，只需要执行已经固定的区别和变换。

### 建立判定条件

执行和验证都需要形式化。若“正确”没有被改写成可判定条件，程序只能运行，无法知道是否完成了目标。

```python
assert all(order.amount > 5000 for order in result)
assert all(order.account is not None for order in result)
```

这些断言可以检查编码后的性质，却不能证明性质本身选得正确。这正是 [[wiki/concepts/Executable Specification]] 中 validation 与 verification 的分界：

- validation 检查规格是否对准真实意图；
- verification 检查实现是否满足既定规格。

## Formalization and Reasoning

广义问题解决不只有演绎计算。它还包括目标解释、事实获取、问题建模、假设生成、推演、计算、验证、不确定性判断、价值取舍、行动和元推理。

这些内容能被形式化到不同程度：

| 内容 | 适合的形式化方式 | 主要边界 |
|---|---|---|
| 计算与符号推导 | 程序、公式、证明规则 | 输入和规则可能错 |
| 状态维护 | 数据结构、状态机、事件日志 | 表示可能遗漏现实变量 |
| 验证 | 测试、断言、类型、约束 | 只能验证已编码性质 |
| 事实获取 | 查询、传感器协议、证据结构 | 来源可能不完整或失真 |
| 因果推理 | 因果图、实验设计、反事实模型 | 模型假设可能不成立 |
| 不确定性 | 概率、区间、置信度 | 数值可能制造虚假精确 |
| 意图与价值 | 规则、偏好模型、审批边界 | 最终语义和责任不能自动产生 |

所以“是否能形式化”不是在问某件事能不能写成符号，而是在问：

> 当前目的下，能否明确哪些区别重要，并为这些区别给出可重复执行或检查的规则？

## Why Code Fits Formalized Reasoning

代码是形式化的一种特殊载体：它不仅描述规则，还能让规则真实改变机器状态。

代码适合承接部分推理，根本原因不是它比自然语言更有智慧，而是它把形式结构同时变成：

- 可执行的操作；
- 可观察的中间状态；
- 可保存和共享的外部对象；
- 可重复触发的失败与反馈。

这让代码能够把瞬时想法变成一条闭环：

```text
提出规则 -> 执行 -> 观察结果 -> 检查失败 -> 修改规则 -> 再执行
```

[[wiki/sources/Code as Agent Harness Paper Source Guide]] 将这三项能力概括为 executable、inspectable、stateful。代码因此可以成为 Agent 推理、行动和环境建模的接口，但不等于推理的每一步都必须写成代码。

## Limits

形式系统可以内部完全一致，却仍然错误地刻画现实。

```python
adult = age >= 16
```

程序可以百分之百准确地执行这条规则，但它不能自行回答为什么是 16 岁、是否适用于所有法律场景、是否公平。这些问题属于目的、语境、价值与责任。

因此必须区分两种正确：

- **系统内部正确**：是否按既定规则推导或执行；
- **现实对应正确**：对象、变量和规则是否抓住了真实问题。

形式化主要提高前者的稳定性，并通过外显假设帮助人审查后者；它不自动产生真理。

## When to Use

形式化适合用于：

- 把模糊需求变成可检查的规格；
- 把长任务交给程序、Agent、团队或未来的自己；
- 让推理步骤可以复现、审计和反驳；
- 设计测试、状态机、接口协议和权限规则；
- 定位错误来自意图、事实、模型、推导、执行还是验证。

不要把形式化当成：

- 对现实的完整复制；
- 越形式化越高级的价值排序；
- 用明确规则取代人的价值判断；
- 代码运行成功即现实结论正确的保证。

## Related

- [[wiki/concepts/Knowledge Formalization Gradient]] — 形式化在知识表达中的渐进路径。
- [[wiki/concepts/Executable Specification]] — 把意图压成机器可检查承诺。
- [[wiki/concepts/Verification Loop]] — 让执行结果返回推理和行动循环。
- [[wiki/concepts/Verifier Hierarchy]] — 不同判定信号的独立性与现实接地程度。
- [[wiki/concepts/Reasoning as Structure Mapping]] — 推理如何在结构之间建立映射。
- [[wiki/sources/Code as Agent Harness Paper Source Guide]] — 代码作为 Agent 可执行、可检视、有状态的运行媒介。
