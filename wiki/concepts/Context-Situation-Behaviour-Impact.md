---
title: Context-Situation-Behaviour-Impact
type: concept
status: draft
category: concepts
summary: CSBI 在情境理解后用具体场景、可观察行为和给予者感知的影响组织反馈；邀请接收者澄清并共同寻找行动，避免把观察直接解释为人格。
aliases: ["CSBI", "SBI", "情境—场景—行为—影响", "情境先行的反馈"]
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
  - target: "[[wiki/concepts/Feedback Impact Levels]]"
    type: related_to
---

# Context-Situation-Behaviour-Impact

CSBI 是把 SBI 反馈结构变成有情境理解的对话：先弄清行为为什么发生，再说明发生的场景、可观察行为和自己感受到的影响。[[wiki/sources/Healthy Peer Feedback Source Guide]] 中，作者认为先询问情境可以减少反馈谈话中的紧张。

## 四个部分

| 部分 | 要回答的问题 | 示例 |
|---|---|---|
| Context：背景情境 | 当时有哪些条件、限制或原因？ | 为什么今天跳过了几页幻灯片？ |
| Situation：具体场景 | 什么时间、哪次工作？ | 今天下午的演讲 |
| Behaviour：可观察行为 | 对方实际做了什么？ | 跳过了几页已经显示在屏幕上的幻灯片 |
| Impact：感受到的影响 | 这件事怎样影响我或工作？ | 我感觉内容像预制演讲；担心听众以为准备不足 |

文章明确区分：场景和行为以具体观察为基础，影响是给予者的感知。“听众都认为你没准备”不能只凭自己的感受认定；更可核验的表达是说明自己观察或感受到的影响。后一判断是对模型的应用推论。^[inferred]

## 情境改变诊断

文章的演讲例子中，跳过幻灯片不一定来自准备不足，也可能是晚开始或意外打断导致时间不足。了解背景以后，反馈仍有价值，但主题从“准备更充分”变为“怎样灵活而自然地略过内容”。

```text
同一观察：跳过幻灯片
        │
        ├─ 未了解背景 → 推断准备不足 → 建议藏掉不相关页面
        │
        └─ 询问背景 → 时间被压缩 → 讨论如何让演讲能灵活缩短
```

图中两种诊断来自文章例子；避免未经检验地把行为归结为个人态度，是这套方法的主要价值。^[inferred]

## 一次可用的对话

1. 确认时机：“我有一个关于今天演讲的观察，大约需要十分钟，现在适合聊吗？”
2. 询问背景：“我注意到你跳过了几页，当时是什么情况？”
3. 说明观察：“在今天的演讲里，我看到几页显示后又被跳过。”
4. 说明感知：“我有些难判断哪些内容是针对这次听众的，也担心这影响演讲连贯性。”
5. 邀请想法：“如果下次时间临时压缩，怎样让演讲仍然连贯？”
6. 留出澄清和跟进：“你怎么看这个影响？我们可以试哪种办法，下次再看效果？”

以上是根据文章方法编写的示范，不是原文逐句翻译；CSBI 是信息结构，不要求对话机械地按四个字母念一遍。^[inferred]

## 表扬也可以使用

文章强调 CSBI 同样适用于表扬。把“做得很好”落到场景、行为和影响，接收者才知道哪些行为值得继续。

例如：“今天评审时，你先复述了两边的方案和分歧，让我们确认彼此理解后再讨论取舍；我觉得这让讨论明显更顺畅，希望下次继续这样做。”这是模型应用示例。^[inferred]

## 边界

- 建议是可选部分。团队规范明确时可以直接建议；多数情况下应邀请接收者提出可实行的办法。
- 背景可能解释行为，但不自动消除影响或责任；接收者提供背景，也不等于防御。需要区分共同诊断与拒绝听取信息。^[inferred]
- 对方不愿谈时，作者建议先处理关系中的其他问题。确认当下时机本身不能保证深层心理安全。^[inferred]
- 单次谈话结构需要配合 [[wiki/concepts/Feedback Impact Levels]]：问题已经重复时，必须说明模式或关系影响。

## Sources

- [[wiki/sources/Healthy Peer Feedback Source Guide]] — “Be hard on the problem, easy on the people”“Seek context to create safety”等章节。

## Related

- [[wiki/topics/Peer Feedback]]
- [[wiki/concepts/Feedback Impact Levels]]
- [[wiki/topics/Technical Management]]
- [[wiki/sources/高难度沟通 Source Guide]]
