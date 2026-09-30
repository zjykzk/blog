---
title: Discovery Replay Simulator
type: concept
status: draft
category: concepts
tags: [agents, harness, optimization, memory, feedback]
aliases:
  - 发现历史回放器
  - 发现树回放模拟器
  - Discovery History as a Replay Simulator
sources:
  - https://github.com/zhengkid/Dream-RSI/blob/c67937fa0452fbda3fad92107d1f30699380da39/papers/Dream-RSI.pdf
  - /Users/zenk/Context/20260926T232318--paper-dream-rsi__paper.md
  - conversation:2026-09-26
created: 2026-10-01T01:10:38+0800
updated: 2026-10-01T01:10:38+0800
summary: >-
  发现历史回放器把已执行搜索的版本、评分和错误按前缀逐步揭示，用固定结果比较探索调度；它降低策略试验成本，但不能评价未记录结果或保证线上泛化。
provenance:
  extracted: 0.75
  inferred: 0.25
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-01
tier: supporting
---

# Discovery Replay Simulator

发现历史回放器将真实搜索留下的版本关系和执行结果组织成可逐步交互的环境，让新探索策略通过访问旧结果接受评价，无须为每套策略重新执行完整发现过程。

这一机制来自 [[wiki/sources/Dream-RSI Paper Source Guide|Dream-RSI]]。其学习对象是“下一次尝试分给哪条路线”的调度代码，属于 [[wiki/concepts/Continual Learning for AI Agents|agent 持续学习]] 的外部代码层。

## 它怎样工作

真实探索先记录每次尝试的起始版本、文件快照、生成产物、评测分数和失败诊断。一次回放从初始状态开始，当前策略只看已经揭示的记录；选择沿一条路线继续，才返回其历史后继。

Dream-RSI 正文中，初始分支按历史创建顺序打开，已开路线按父子关系前进。策略可以改变哪些尝试被访问、何时访问、怎样并行以及何时停止；记录本身和节点结果保持固定。

```text
已经保存的历史：
初始状态 --+--> A1 --> A2 --> A3
           +--> B1 --> B2（失败）--> B3（改善）

回放甲：打开 A、B，见到 B2 后停止继续 B
回放乙：打开 A、B，见到 B2 后再尝试一步，才见到 B3
```

这是虚构示例。箭头表示版本继承，两个回放说明不同停止规则会访问不同子集。策略乙必须依据 B2 之前的观察判断是否值得继续，不能先知道 B3 会改善，也不能绕过 B2 直接取 B3。

回放之后，策略开发代理依据成绩和工作量改写规则，在同一批历史中比较候选；选中的规则再投入真实探索，新经历扩充回放池。候选包含旧规则时，取历史分数最大者只能保证同池分数不下降。

## 与相邻概念的区别

| 概念 | 历史怎样被使用 | 直接改变什么 |
|---|---|---|
| 历史摘要或方向建议 | 作为模型读取的内容 | 后续推理的上下文和答案方向 |
| 技能蒸馏 | 抽取可复用步骤或代码 | 执行某类任务的方法 |
| 发现历史回放器 | 作为逐步揭示结果的策略试验环境 | 分配尝试机会的规则 |
| 生成式世界模型 | 学习环境变化，并预测新动作的后果 | 可模拟的状态转移和结果 |

上表是对经验复用方式的概念区分，并非四种方法的全面效果排名。它们可以组合；回放器本身不能预测原记录之外的程序成绩。^[inferred]

它与 [[wiki/concepts/Meta-Harness]] 的共同点是优化固定模型外部的代码；独特之处在于把历史变成候选策略的评价环境，而不只把日志交给代码修改者阅读。^[inferred]

## 判断它是否适用

以下是从 Dream-RSI 机制推导的工程判断条件，不是论文已经跨领域验证的普遍定律。^[inferred]

- **真实尝试昂贵、记录可复用。** 保存过程与结果的成本，应低于反复运行整轮发现的成本。
- **优化对象适合重排。** 新规则主要改变选择、并行和停止；若它改变了任务定义、评测器或候选生成方式，旧结果的可比性可能不足。
- **记录有足够覆盖。** 少数浅层轨迹不足以判断长期投入；记录外的动作仍需要在线探索。
- **过程信息足够。** 只有最终分数难以区分方向无望与实现错误，版本继承和诊断更有价值。
- **评价同时计质量与投入。** 回放虽只读记录，也要计算它代表的真实工作量，不能默认全部翻完就是好策略。

## 三条不可省略的边界

**支持域边界：** 历史没有走过的分支，回放就没有答案。更多次回放可以更充分比较已有机会，不能凭空扩展已观察空间。

**因果边界：** 真实代理受随机性与全局上下文影响；改变访问顺序，可能改变它实际生成的程序。固定结果回放因此是经验近似，不能当作严格反事实证明。^[inferred]

**泛化边界：** 遮住未来分数能防止运行时偷看，但不能排除反复对同一历史池调策略造成的过拟合。[[wiki/concepts/Verification Loop|验证闭环]] 仍需下一轮真实结果，并区分历史筛选分数、发现质量和端到端费用。^[inferred]

这一机制把 [[wiki/concepts/Search and Learning as Meta-Methods|搜索与学习]] 接在一起：真实搜索产生经验，策略搜索复用经验，再改变后续探索。能否持续改进，还取决于历史覆盖和反馈是否有用。^[inferred]

## Related

- [[wiki/sources/Dream-RSI Paper Source Guide]]
- [[wiki/concepts/Meta-Harness]]
- [[wiki/concepts/Continual Learning for AI Agents]]
- [[wiki/concepts/Search and Learning as Meta-Methods]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/topics/AI Memory]]
- [[wiki/maps/Self-Evolving Agents Map]]
