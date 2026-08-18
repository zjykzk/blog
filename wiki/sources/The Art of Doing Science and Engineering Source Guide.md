---
title: The Art of Doing Science and Engineering Source Guide
type: source
status: draft
category: sources
summary: 汉明把 Learning to Learn 定义为面向未来的元教育：在知识过时、问题变化和系统演化中，持续选择重要问题、学习基础结构并修正自己的思维风格。
tags:
  - book-notes
  - learning
  - engineering
  - leadership
sources:
  - /Users/zenk/Downloads/The Art of Doing Science and Engineering - Learning to Learn.pdf
  - conversation:2026-08-16
created: 2026-08-16T17:13:51+0800
updated: 2026-08-16T17:13:51+0800
provenance:
  extracted: 0.82
  inferred: 0.17
  ambiguous: 0.01
base_confidence: 0.69
lifecycle: draft
lifecycle_changed: 2026-08-16
aliases:
  - 科学与工程的艺术
  - Learning to Learn
  - Richard Hamming Learning to Learn
---

# The Art of Doing Science and Engineering Source Guide

> Source: Richard W. Hamming, *The Art of Doing Science and Engineering: Learning to Learn*

## What It Covers

这本书表面上讲计算机史、编码、信息论、数字滤波、模拟、光纤、创造力、专家、数据、系统工程和研究工作，真正主题却是科学与工程中的 *style of thinking*。技术章节是汉明展示思维动作的材料，不是课程本身。

副标题 *Learning to Learn* 不是“提高学习效率”，而是面向长期技术生涯的元教育：技术会过时，问题会重写，连一个时代有效的思维风格也可能在下一个时代失效。工程师必须学会选择知识、进入新领域、定义问题、观察反馈，并改造自己的工作方式。

## Why Learning to Learn

### 知识增长快于职业教育

汉明估计，相关知识大约每 17 年翻一倍，工程技术细节的半衰期约为 15 年。一个人的职业生涯远长于学校知识的有效期，而且他贡献最大时所需的知识往往在毕业后才出现。

由此得到的答案不是无边界地持续输入，而是：

- 优先掌握能生成大量细节的基础结构；
- 在新领域出现时，快速学习足够解决当前问题的部分；
- 不把职业身份绑定在短命工具上；
- 定期判断现在所学是否仍对应未来的问题。

这与 [[wiki/topics/Learning Methodology]] 的“从问题进、just-in-time、抓结构层”直接相连，但汉明更强调职业方向与重要问题。

### 教育不同于训练

汉明用一句话区分两者：

> Education is what, when, and why to do things; Training is how to do it.

训练回答“怎么做”，教育回答“做什么、何时做、为什么做”。二者缺一不可。只训练会产生擅长解决给定题目的人，却不保证他能发现题目是否重要、边界是否正确、方法是否过时。

汉明把这门课称为 *meta-education*：它不是再教一批答案，而是让学习者审查教育本身，学会选择题目、方法与方向。

### 学习对象包括自己的思维风格

思维风格是面对未知时稳定出现的判断动作，包括：

- 先做 *back-of-the-envelope calculation*，用数量级排除荒唐方向；
- 长期保留十到二十个重要且尚无答案的问题；
- 定期留出 “great thoughts” 时间，抬头检查领域与组织的方向；
- 卡住时反转问题，而不是只增加资源；
- 用类比连接远距离知识，并检查类比的失效点；
- 对专家口中的“不可能”追问隐藏假设；
- 保持 *open door*，防止专业化把问题越做越窄；
- 同时相信工作值得做，又怀疑当前方法仍可改进。

风格不是固定人格。汉明明确提醒，一个时代成功的风格未必适合下一个时代。Learning to Learn 因而包含修改“学习算法”本身的能力。^[inferred]

## Systems Engineering as Learning

系统工程章把 Learning to Learn 从个人学习扩展成系统学习。

### 局部优化可能毁掉整体

汉明的第一条系统工程规则是：

> If you optimize the components you will probably ruin the system performance.

组件变好，不等于系统变好。判断一个部分时必须追问：

- 它属于哪个更大的系统；
- 整体真正要产出什么；
- 它和其他部分怎样相互作用；
- 当前改动会把成本转移给谁；
- 系统超过预期条件后怎样退化。

这与 [[wiki/topics/Thinking in Systems]] 的目标、反馈、延迟和系统边界相连。

### 解决方案会改变问题

汉明为计算中心安排短任务专属时段后，人们把长任务拆成多个短任务，反而增加输入输出负担。规则不是施加在静止对象上的；人会响应规则，解决方案也会改变环境。

因此系统工程没有永远固定的问题，也没有最终完成的答案。每轮方案都应：

1. 缓解当前问题；
2. 观察系统的回应；
3. 增加对真正问题的理解；
4. 为下一轮变化保留弹性。

“一个方案如果没有带来比开始时更深的理解，就很难算好方案”是这章与 Learning to Learn 的直接连接。

### 做正确的问题，哪怕解得不完美

汉明见过许多“把错误的问题正确解决”的方案。系统工程宁可先逼近正确问题，再用可修正的临时方案行动，也不应在错误边界中追求局部完美。

这与 [[wiki/topics/Problem Framing]] 的问题定义、[[wiki/concepts/Law of Unintended Consequences]] 的二阶后果和 [[wiki/topics/Modern Software Engineering]] 的经验主义反馈相连。

## Measurement Changes Behavior

*You Get What You Measure* 说明度量不是中性的观察工具。组织选什么指标，就会诱发人们优化什么。

- 容易精确测量的东西未必与目标最相关；
- 学校容易测训练结果，却难测教育结果；
- 用代码行数衡量产出会鼓励冗长代码；
- 只看短期利润会把组织塑造成短期主义系统。

Learning to Learn 因而还要求观察评价机制怎样改造学习者、团队和问题本身。度量不能只问“准不准”，还要问“相关吗”“会诱发什么行为”。

## Important Work

汉明把卓越工作的概率连接到重要问题：

- 不处理重要问题，很难期待重要成果；
- 重要不等于宏大，还必须有可攻击的入口；
- 长期方向能让许多小步同向积累，否则努力像 *drunken sailor* 相互抵消；
- 重要问题清单让新知识有挂接点，偶然出现时也更容易被识别；
- 勤奋是必要条件，但“正确的问题、正确的时机、正确的做法”比单纯增加工时更关键。

这不是保证人人成为天才，而是把成功从纯粹天赋和运气中移出一部分，转成可以反省、模仿和训练的工作方式。

## Implications for Technical Leadership

对高级工程师和 Tech Leader，这本书把角色成长改写成三次上移：^[inferred]

```text
解决复杂问题
    ↓
让系统更容易应对变化
    ↓
让团队持续发现并解决正确的问题
```

领导力不只是亲自处理最难的技术任务，而是选择值得投入的问题、设计能承受变化的系统、建立不依赖个人英雄的团队判断能力，并用指标和反馈校准技术投资。详见 [[wiki/syntheses/From Senior Engineer to Tech Leader]]。

## Tensions and Limits

- 汉明强调个人主动性，较少讨论权力、资源和组织制度怎样预先限制选题。
- 许多结论来自贝尔实验室和个人经历，故事能展示风格，却不能自动证明普遍因果。
- “重要工作”和“卓越”带有明显的精英取向，不应覆盖维护、照护和稳定交付等同样必要的工作。
- 书中部分技术预测和细节已经过时，但这反而印证了副标题：技术内容会旧，选择、反馈和自我更新仍是长期问题。^[inferred]

## Related

- [[wiki/topics/Learning Methodology]]
- [[wiki/topics/Thinking in Systems]]
- [[wiki/topics/Problem Framing]]
- [[wiki/topics/Technical Management]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/syntheses/From Senior Engineer to Tech Leader]]
- [[wiki/sources/架构师启示录 Source Guide]]
