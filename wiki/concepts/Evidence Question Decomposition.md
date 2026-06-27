---
title: >-
  Evidence Question Decomposition
category: concepts
tags: [thinking, judgment, evaluation, mechanism, feedback]
sources:
  - conversation:2026-06-27
created: 2026-06-27T02:24:07+0800
updated: 2026-06-27T02:24:07+0800
summary: >-
  Evidence question decomposition turns a broad judgment into checkable questions with evidence anchors, answers, failure types, and repair actions.
provenance:
  extracted: 0.74
  inferred: 0.26
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-06-27
tier: supporting
aliases:
  - 证据问题分解
  - 证据拆问
  - 可追责检查点
relationships:
  - target: "[[wiki/concepts/Evaluation]]"
    type: extends
  - target: "[[wiki/concepts/Analysis]]"
    type: uses
  - target: "[[wiki/syntheses/Reality-Refutable Engineering Systems]]"
    type: related_to
---

# Evidence Question Decomposition

Evidence question decomposition is the practice of turning a broad judgment into small questions that can be asked, answered from evidence, and traced to a failure type and repair action.

## What It Is

证据问题分解把“它好不好 / 对不对 / 靠不靠谱”这种总评，拆成一组可检查的小判断。

每个小判断必须同时满足三条：

1. 能问：它能写成一个清楚的问题。
2. 能答：它能根据材料回答“是 / 否 / 不确定”。
3. 能追责：失败后能指出依据、错因、影响和修法。

它的目标不是把问题拆得越细越好，而是把判断拆到“每个问题的答案都会改变总判断”的粒度。

## How It Works

证据问题分解通常按一条责任链推进：

```text
大判断
-> 质量维度
-> 原子问题
-> 证据锚点
-> 是非答案
-> 错因类型
-> 修复动作
```

第一步是把总评拆成维度。比如“这段回答靠不靠谱”可以拆成事实层、理解层、推理层、证据层、边界层和行动层。维度还不是可回答问题，只是先把混在一起的判断分开。

第二步是把维度拆成原子问题。事实层可以继续拆成：是否有未经材料支持的具体事实，是否错归因，是否说错时间、数字、地点，是否把推测说成事实，是否遗漏会改变结论的关键事实。

第三步是给每个问题配证据锚点。问题不能只问“事实质量好吗”，而要问“回答是否声称 X 发生过，但材料中没有对应证据”。证据锚点说明应该比对材料里的哪一处和输出里的哪一处。

第四步是把失败定位到错因类型。失败不应只写“事实不一致”，而应写成“错归因：原文把识别飞机的说法归给俄方，摘要把它归给五角大楼；影响事实一致性；修法是改回主语或删除该句”。

## Grain Test

一个检查点是否到达合适粒度，可以用三问检验：

1. 这个问题的答案会不会改变总判断？
2. 这个问题能不能被材料、执行结果或现实反馈回答？
3. 这个问题失败后能不能导出具体修法？

如果一个问题答了也不影响判断、没有证据能答、失败后也不知道怎么修，它就不是好检查点。

## Examples

需求评审里，“这个需求清楚吗”太整。更好的拆法是：目标是否可观察，用户和验收者是否明确，做与不做的边界是否明确，成功标准是否可测，异常路径是否列出，外部依赖是否暴露。这样“需求不清楚”会变成“异常路径缺失、验收标准不可测、依赖未确认”。

代码评审里，“代码质量好吗”太整。更好的拆法是：主路径是否覆盖，异常路径是否处理，接口契约是否改变，共享状态是否有竞态，错误是否被吞掉，日志是否泄露敏感信息，逻辑是否放在正确层。这样“代码不行”会变成“主路径可用，但异常路径缺少重试边界，错误被统一吞掉，线上失败不可观测”。

LLM 回答评估里，“这回答靠谱吗”太整。更好的拆法是：是否编造事实，是否误解问题，是否偷换概念，是否漏掉关键条件，推理链是否跳步，结论是否有证据，语气是否过度确定。

## When to Use

证据问题分解适合所有总评过黑、改进过虚、责任链过模糊的场景：评估模型回答、做需求评审、做代码评审、做事故复盘、验收交付物、设计测试策略。

它尤其适合和 [[wiki/concepts/Evaluation]]、[[wiki/concepts/Analysis]]、[[wiki/concepts/Verification Loop]] 一起使用：Evaluation 提供尺度，Analysis 负责切开对象，Verification Loop 负责让检查点接上现实反馈。

## Boundaries

证据问题分解不能替代整体判断。架构是否过早抽象、需求方向是否值得做、设计是否保住概念完整性，这类问题可以拆出检查点，但仍需要整体关系判断。

拆得过细也会制造假精确。若把“相关性”“吸引力”“设计感”这类整体性较强的判断拆成过严清单，系统可能把人类允许的简洁、取舍和风格差异误判为缺陷。^[inferred]

## Related

- [[wiki/concepts/Evaluation]]
- [[wiki/concepts/Analysis]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/syntheses/Reality-Refutable Engineering Systems]]
- [[wiki/syntheses/Coding Agent Debugging Skills as Evidence Gates]]
