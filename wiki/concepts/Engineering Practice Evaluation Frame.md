---
title: Engineering Practice Evaluation Frame
type: concept
status: draft
category: concepts
summary: 工程实践评估框架用控制目标、作用机制、所需信息、调节动作、新增成本和失效边界六问，判断一项实践是否真正改变系统行为。
tags: [engineering, software-engineering, judgment, mechanism, feedback]
sources:
  - conversation:2026-11-02
relationships:
  - target: "[[wiki/concepts/engineering-thinking]]"
    type: implements
  - target: "[[wiki/concepts/Mechanism Model]]"
    type: uses
  - target: "[[wiki/concepts/Evidence Question Decomposition]]"
    type: extends
  - target: "[[wiki/concepts/Feedforward and Feedback Controls]]"
    type: uses
aliases:
  - 工程实践第一性原理检查表
  - 工程实践评估六问
  - Engineering Practice Checklist
provenance:
  extracted: 0.82
  inferred: 0.18
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-11-02
tier: supporting
created: 2026-11-02T00:22:29+0800
updated: 2026-11-02T00:22:29+0800
---

# Engineering Practice Evaluation Frame

工程实践评估框架用六个问题检查一项实践是否真的改变系统行为，而不是只拥有熟悉的名称、流程或仪式。

## What It Is

一项工程实践可以被看成对系统的干预。评估它时，不应只问“行业是否推荐”或“团队是否执行”，而要还原它试图控制的偏差、作用机制、感知信息、调节动作、附加成本与有效边界。

六问形成一条完整责任链：

| 维度 | 核心问题 | 要暴露的内容 |
|---|---|---|
| 控制目标 | 它试图控制什么？ | 目标状态、风险、不确定性或待压低的偏差 |
| 作用机制 | 它通过什么机制起作用？ | 分解、隔离、约束、验证、自动化、反馈或其他因果路径 |
| 所需信息 | 它需要什么信息？ | 观测数据、上下文、证据、阈值与判断依据 |
| 调节动作 | 它如何产生调节？ | 偏差由谁发现，谁采取什么动作，如何升级或停止 |
| 新增成本 | 它引入什么新成本？ | 复杂度、延迟、资源消耗、认知负担和维护责任 |
| 失效边界 | 什么情况下它会失效？ | 前提条件、适用范围、误用方式、副作用与退出条件 |

## How It Works

六问把工程实践展开为一个控制回路：

```text
目标状态 / 风险容忍度
          ↓
     实践的作用机制
          ↓
传感信息 → 偏差判断 → 调节动作 / 责任人
          ↑                 ↓
          └──── 结果反馈 ────┘

外层约束：新增成本 + 适用边界 + 失效条件
```

缺少任一环节，实践都可能退化：

- 没有控制目标，团队只能检查“做没做”，不能判断“是否有效”。
- 没有机制解释，实践容易变成照搬模板或权威崇拜。
- 没有信息来源，偏差无法被稳定感知。
- 没有调节动作，监控和评审只会生成报告，不会改变系统。
- 没有成本核算，局部可靠性可能以全局速度、认知或维护负担为代价。
- 没有失效边界，局部有效的方法会被误用成万能流程。

## Compact Checklist

```text
1. 它试图控制什么？
   明确它针对的系统状态、风险或不确定性。

2. 它通过什么机制起作用？
   分解、隔离、约束、验证、自动化还是反馈？

3. 它需要什么信息？
   有哪些观测数据、上下文和判断依据？

4. 它如何产生调节？
   发现偏差之后，谁采取什么动作？

5. 它引入什么新成本？
   复杂度、延迟、资源消耗和维护成本。

6. 什么情况下它会失效？
   明确适用边界、前提条件和副作用。
```

## Evaluation Procedure

1. **命名实践与对象。** 先写清被评估的是代码评审、测试金字塔、微服务、持续集成、灰度发布还是其他具体实践。
2. **独立回答六问。** 每个答案都应指向实际系统、工件、数据或责任人，而不是复述方法定义。
3. **检查闭环。** 确认信息能否触发动作，动作能否改变被控制状态，结果能否回流到下一轮判断。
4. **比较替代方案。** 用相同六问比较不同实践，避免只比较口号和功能清单。
5. **记录证据与未知。** 区分已经观察到的效果、合理推断和仍待实验的问题。
6. **设置复审条件。** 当环境、规模、风险或成本结构变化时，重新判断实践是否仍然合适。

## Examples

### Code review

- 控制目标：降低错误进入主干的概率，并维持团队对代码意图的共同理解。
- 作用机制：独立检查、知识传播和责任显性化。
- 所需信息：diff、规格、测试结果、架构约束和历史上下文。
- 调节动作：评论、拒绝、要求补证据、修改后重新审查。
- 新增成本：等待时间、注意力消耗和 reviewer bottleneck。
- 失效边界：评审者缺少上下文、改动过大、只看风格或审批成为橡皮图章。

### Monitoring

- 控制目标：发现运行状态偏离服务目标。
- 作用机制：持续观测并在阈值或模式异常时触发响应。
- 所需信息：日志、指标、trace、服务级目标和用户影响。
- 调节动作：告警、降级、回滚、扩容、修复或调整阈值。
- 新增成本：采集、存储、告警维护与值班负担。
- 失效边界：指标与用户价值脱钩、告警疲劳、数据缺失或响应责任不清。

## Relation to Nearby Models

[[wiki/concepts/engineering-thinking|Engineering Thinking]] 给出工程判断的整体责任结构；本框架把其中一项具体实践拆成可检查的六问。

[[wiki/concepts/Mechanism Model]] 解释系统结果如何由变量、约束、激励、反馈和时间生成；本框架进一步问一项工程干预准备通过什么机制改变该结构。^[inferred]

[[wiki/concepts/Evidence Question Decomposition]] 把模糊总评拆成可回答、可追责的检查点；本框架是它在工程实践选择上的专用问题集。^[inferred]

[[wiki/concepts/Feedforward and Feedback Controls]] 区分行动前塑形与行动后纠偏；六问同时检查控制信息和调节动作是否真正闭环。

## When to Use

这个框架适合：

- 引入新的工程实践或架构模式之前；
- 复盘一项实践为何没有产生预期效果；
- 比较多个候选方法的收益、成本与边界；
- 清理只剩仪式、不能改变系统行为的流程；
- 把专家直觉转成团队可讨论、可验证的判断依据。

对一次性、低风险、边界清楚的动作，不必强制完整填写。检查表本身也会引入认知和流程成本，应按决策后果裁剪。^[inferred]

## Related

- [[wiki/topics/Modern Software Engineering]]
- [[wiki/concepts/engineering-thinking]]
- [[wiki/concepts/Mechanism Model]]
- [[wiki/concepts/Evidence Question Decomposition]]
- [[wiki/concepts/Feedforward and Feedback Controls]]
- [[wiki/concepts/Feedback Loops]]
- [[wiki/concepts/Evaluation]]
- [[wiki/syntheses/Quality Engineering Three Generators]]
