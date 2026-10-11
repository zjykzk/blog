---
title: Feedback Impact Levels
type: concept
status: draft
category: concepts
summary: 同伴反馈按累积影响区分内容、模式与关系：单次问题讨论具体工作，重复发生讨论规律，持续不变讨论信任和协作代价；关系层无效时可能需要管理介入。
aliases: ["反馈影响层级", "Content Pattern Relationship", "CPR", "内容—模式—关系"]
tags: ["management", "organization", "feedback"]
sources:
  - https://martinfowler.com/articles/healthy-peer-feedback.html
source_id: martinfowler.com/anuja-karnik-sumeet-gayathri-moghe
created: 2026-10-11T23:28:02+08:00
updated: 2026-10-11T23:28:02+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-10-11
tier: supporting
provenance:
  extracted: 0.72
  inferred: 0.28
  ambiguous: 0.0
relationships:
  - target: "[[wiki/topics/Peer Feedback]]"
    type: related_to
  - target: "[[wiki/concepts/Context-Situation-Behaviour-Impact]]"
    type: related_to
---

# Feedback Impact Levels

反馈影响层级区分内容（content）、模式（pattern）和关系（relationship）。[[wiki/sources/Healthy Peer Feedback Source Guide]] 用反复写不清楚的 commit message 说明：问题持续重复时，谈话焦点要随实际影响变化，不能一直停留在某条提交记录上。

## 三个尺度

| 层级 | 对象 | 文章中的提交信息例子 | 谈话重点 |
|---|---|---|---|
| 内容 | 一个具体事件或作品 | 某次 commit message 没有说明意图或结果 | 指出这条信息缺什么，示范团队标准 |
| 模式 | 多次类似事件 | 上次谈过后，新的信息仍过于笼统 | 回溯已有反馈，指出重复观察和影响 |
| 关系 | 反复不变对合作的影响 | 给予者不再依赖历史记录，需要更细地审查改动 | 说清信任与合作负担怎样变化，邀请共同解决 |

第一次发现问题通常可以在工作流中讨论内容。若已经提出反馈而问题持续，应承认它成为模式。若模式持续影响双方合作，应讨论关系。文章并未提供“第几次必须升级”的硬阈值；关键是实际影响。^[inferred]

## 怎样讨论关系而不攻击人格

关系层的例子包含具体历史：先前指出过“update code”缺少意图，后来又看见“fix tests”“address review comments”“update validation”之类缺少上下文的信息。

给予者接着表达自己的担忧：反馈似乎没有被落实、双方可能没有共享同一标准；自己开始更细地检查对方的改动，合作因此更费力。最后询问怎样帮助对方遵循团队标准。

这仍是观察与影响的对话，而不是把对方定性成不可靠的人。应结合 [[wiki/concepts/Context-Situation-Behaviour-Impact|CSBI]] 询问是否存在能力、资源或标准理解方面的障碍；文章没有完整列出这些障碍，它们是应用时需要检验的其他解释。^[inferred]

## 与惩罚升级的区别

CPR 首先改变的是谈话主题：从某次作品转向重复规律，再转向合作关系的后果。它不等于内容层口头批评、模式层警告、关系层惩罚的制度流程。^[inferred]

作者承认，若关系层反馈仍不奏效，可能需要经理或 HR 介入，尤其是建立团队规范时。同伴反馈有边界；职权介入需要围绕已有约定与实际证据，而不能把个人偏好偷换成共同规范。后一句是推论。^[inferred]

## 表扬也有层级

文章明确说这一层级同样适用于表扬。下面是按模型生成的例子。^[inferred]

- **内容**：这次把背景与取舍写进提交信息，让我快速理解了改动。
- **模式**：最近几次你都把意图写清楚了，评审反复打开 diff 补上下文的次数减少。
- **关系**：持续清楚地沟通变化，让我更愿意把协作交接给你，也更信任我们的共同标准。

## 使用前判断

1. 有具体观察吗，还是只有印象？
2. 这是单次事件，还是能够指出多次证据的模式？
3. 前一次反馈是否说清楚、得到理解？
4. 不变的模式怎样改变了合作、审查负担或信任？
5. 正在讨论共同标准，还是个人偏好？

这些问题是根据文章原则整理的应用检查，不是作者给出的量表。^[inferred]

## Sources

- [[wiki/sources/Healthy Peer Feedback Source Guide]] — “Match feedback to the level of impact”“Catch someone doing something right”。

## Related

- [[wiki/topics/Peer Feedback]]
- [[wiki/concepts/Context-Situation-Behaviour-Impact]]
- [[wiki/topics/Technical Management]]
- [[wiki/concepts/Feedback Loops]]
- [[wiki/maps/Management Map]]
