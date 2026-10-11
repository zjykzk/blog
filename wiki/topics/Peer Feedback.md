---
title: Peer Feedback
type: topic
status: draft
category: topics
summary: 同伴反馈是在真实协作中交换具体观察与影响，帮助彼此强化有效行为、改善合作；给予、接收、跟进与制度环境共同决定反馈是否可用。
aliases: ["同伴反馈", "同侪反馈", "Peer-to-Peer Feedback", "健康反馈"]
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
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
relationships:
  - target: "[[wiki/concepts/Context-Situation-Behaviour-Impact]]"
    type: uses
  - target: "[[wiki/concepts/Feedback Impact Levels]]"
    type: uses
  - target: "[[wiki/concepts/Feedback Loops]]"
    type: related_to
  - target: "[[wiki/topics/Technical Management]]"
    type: related_to
---

# Peer Feedback

同伴反馈是在共同工作中，把自己看到的行为及其影响告诉对方，并通过对话帮助彼此成长。它包含强化信心的表扬，也包含提升有效性的批评。本文方法来自 [[wiki/sources/Healthy Peer Feedback Source Guide]] 中两位作者的 Thoughtworks 实践经验。

交换反馈时把彼此当作同伴，是一种对话原则，不表示职级和正式责任消失。高级同事尤其需要主动寻求反馈、公开承认自己的错误。

## 目的与态度

Kim Scott 的 Radical Candor 用两个维度区分反馈方式：关心对方，以及直接挑战对方的工作和互动。

| | 直接挑战 | 不直接挑战 |
|---|---|---|
| 关心对方 | Radical Candor：关心个人并直接指出问题 | Ruinous Empathy：出于关心回避问题 |
| 缺少关心 | Obnoxious Aggression：攻击式直言 | Manipulative Insincerity：敷衍或操纵式不真诚 |

“所有反馈都是正向的”是作者对反馈目的的规范：强化信心或提升有效性。不能仅凭反馈者说自己出于善意，就认定内容准确或处理方式合适。^[inferred]

## 如何给予反馈

1. 靠近日常工作提出反馈：结对、设计文档、联合演讲或工作坊都能产生具体观察。
2. 确认接收时机：询问是否适合现在谈，说明较长对话的目的和所需时间；若对方没有准备好，另约时间。
3. 先寻求情境：用 [[wiki/concepts/Context-Situation-Behaviour-Impact|CSBI]] 区分行为、背后条件和自己感受到的影响。
4. 面对问题、尊重人：描述行为，避免把有限观察上升为人格判断。
5. 邀请对方找办法：开放问题让接收者参与行动选择；在明确团队规范的场景，直接建议也可能有效。
6. 按 [[wiki/concepts/Feedback Impact Levels|影响层级]] 区分单次内容、重复模式和关系变化。
7. 同样具体地表扬：指出何时做了什么、带来什么价值，让对方知道哪些行为值得继续。

只在出错时反馈，会让同事把反馈与威胁联系起来；在日常工作中也指出有效行为，可以让反馈成为更完整的协作信号。前半句是对作者“只有批评会伤害关系与士气”的机制解释。^[inferred]

## 如何接收反馈

- **感谢**：让给予者知道你愿意听，包括收到表扬时。
- **澄清**：询问何时发生、观察到什么、有什么影响、原本期待什么；先理解再判断。
- **延迟防御**：澄清是“能给个例子吗”，即时防御是“我这样做还不是因为别人都不做”。背景仍有价值，但需要在理解反馈的对话中提出。后一句是推论。^[inferred]
- **允许反思**：暂时不理解时可以说明需要想一想。
- **关闭回路**：采取行动后告诉对方结果；不采纳时也可以说明反思后的决定，并保持对话。
- **主动、具体地询问**：围绕共同经历或希望改善的技能提问，比向很多人索要泛泛评价更有用。

书面反馈缺少语气和表情。作者建议尝试以友好语气重新阅读，避免把自己的第一反应直接当成对方的意图；这是一种理解练习，并不验证反馈是否准确。后一句是推论。^[inferred]

## 个人偏好与共同规范

作者把非强制反馈比作礼物。对方可以判断礼物是否有用，不必满足给予者的自我。文中的例子是是否让 AI 代写沟通：若没有团队规范，个人不赞成只能是偏好建议。

团队已约定的原则和标准有不同地位。反复不遵守规范并影响协作时，需要讨论具体影响，必要时让经理或 HR 介入。判断关键是：这项反馈依据共同标准，还是依据我个人的工作习惯？^[inferred]

## 制度如何改变反馈动机

作者主张让同伴成长反馈与绩效评审解耦。评审涉及薪酬和晋升，容易让人隐瞒批评；半年或一年后的回忆容易只剩泛泛结论，书面反馈又缺少澄清空间。绩效评审应围绕事先约定的目标，管理者平时持续反馈，使最终评审没有突然出现的新问题。

这不等于证明所有同伴意见都不能成为绩效证据。稳妥的用法是检验信息是否对应约定目标、是否来自足够共同经历、是否已经及时向本人提出，以及奖惩后果是否让信息失真。^[inferred]

| 反模式 | 作者指出的问题 | 更好的做法 |
|---|---|---|
| 只在绩效周期收集 | 后果太重、信息太旧、难以坦诚和具体 | 日常交流；评审围绕约定目标 |
| 表扬—批评—表扬三明治 | 表扬像包装，批评被冲淡，目的不清 | 分开讲清强化信心与改善有效性 |
| 公开 360 | 公开批评威胁地位与安全，导致保留信息 | 个体反馈私下谈；团队回顾讨论共同动态 |
| Speedback | 随机配对缺少共同工作证据，几分钟制造浅层反馈压力 | 围绕真实协作安排有深度的对话 |
| Feedback farming | 为评审货币积攒好评，数量取代有效证据 | 向有共同经历的人询问具体问题 |

这些是文章的实践判断；“没有捷径”的机制是信任由重复互动累积，强制集中活动不能代替具体观察、理解与跟进。^[inferred]

## 与现有知识的连接

[[wiki/sources/高难度沟通 Source Guide]] 的“真实目标—情绪管理—双向推进”可帮助理解为什么反馈不能只剩话术：反馈目标是让行为和合作变好，安全感让对话继续，接收者参与让结论转成行动。这是跨来源综合。^[inferred]

[[wiki/concepts/Feedback Loops]] 的闭环判据也适用：只有信息返回并改变下一次行为或互动，反馈才产生调节作用；送出一段评语只是信号传递。^[inferred]

## Open Questions

- 权力不对等时，怎样让“可以择时谈”和“可以不采纳个人建议”真正可信？^[inferred]
- 当重复问题来自能力不足、资源限制或标准不明确时，怎样避免过早诊断成不愿改变？^[inferred]

## Sources

- [[wiki/sources/Healthy Peer Feedback Source Guide]] — 正文与作者经验边界。

## Related

- [[wiki/concepts/Context-Situation-Behaviour-Impact]]
- [[wiki/concepts/Feedback Impact Levels]]
- [[wiki/topics/Technical Management]]
- [[wiki/sources/高难度沟通 Source Guide]]
- [[wiki/concepts/Feedback Loops]]
- [[wiki/maps/Management Map]]
