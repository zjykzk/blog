---
title: Anti-Patterns in Software Blogging Source Guide
category: sources
type: source
status: draft
tags: [article, software-engineering, cognition, frontend]
sources:
  - https://refactoringenglish.com/blog/anti-patterns-software-blogging/
  - conversation:2026-10-08
created: 2026-10-08T23:17:28+0800
updated: 2026-10-08T23:17:28+0800
summary: >-
  Michael Lynch 用六类软件博客反模式说明：技术文章应尽快承诺价值、控制知识依赖、保持页内自足，并把语言与网页呈现都纳入读者体验。
relationships:
  - target: "[[wiki/concepts/Logic Tree and Pyramid Principle]]"
    type: related_to
  - target: "[[wiki/concepts/Cognitive Load Theory]]"
    type: related_to
  - target: "[[wiki/topics/Frontend Development]]"
    type: related_to
provenance:
  extracted: 0.72
  inferred: 0.25
  ambiguous: 0.03
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-08
tier: supporting
aliases:
  - 软件博客反模式
  - Technical Blogging Anti-Patterns
author: Michael Lynch
published: 2026-10-07
source_url: https://refactoringenglish.com/blog/anti-patterns-software-blogging/
---

# Anti-Patterns in Software Blogging

> Source: [Michael Lynch, “Anti-Patterns in Software Blogging”](https://refactoringenglish.com/blog/anti-patterns-software-blogging/), 2026-10-07

## What It Covers

Michael Lynch 把软件工程中的“反模式”概念迁移到技术写作，用六类反复损害阅读体验的做法说明初学者常见的软件博客问题：开头绕远、错误估计读者知识、依赖链接解释、要求补读前文、过度正式，以及忽略移动端与可读性。

文章不是一套完整的写作理论，而是一份以读者体验为判据的失败模式清单。每一类问题都通过坏例子、读者代价和替代写法展开，最后收束成发布前检查项。^[inferred]

## Core Question

文章表面追问“软件开发者写博客时最常犯什么错误”。更深一层，它处理的是作者与读者之间的工作分配：为了理解文章，哪些上下文组织、术语解释和阅读障碍应该由作者预先消化，而不该转嫁给读者。^[inferred]

这一问题可以压成一条判断：技术内容即使正确，只要读者不知道为什么值得读、必须不断补背景或无法顺畅阅读，它就没有完成交付。^[inferred]

## Concept Structure

六类反模式可以按读者完成阅读所经过的三个关口重新组织：^[inferred]

```text
                    读者能否从文章中获得价值
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
          愿意开始读         能够连续理解        能够舒服地读完
             │                 │                 │
        明确价值承诺         控制知识依赖         降低表达与界面摩擦
             │                 │                 │
      ┌──────┴──────┐   ┌─────┼─────┐      ┌────┼────┐
      │             │   │     │     │      │         │
   标题与前三句   删除前奏  背景假设 链接依赖 前文依赖 语言风格   HTML呈现
      │             │   │     │     │      │         │
   给出收益       不绕路  建桥  页内解释 文章自足  像人说话  移动端/对比度
```

### 注意力预算

读者一开始会迅速判断两件事：文章是不是写给自己，以及阅读能带来什么收益。作者建议用标题和前三句话回答这两个问题。副标题、作者简介、图片、名言和背景故事不是绝对不能出现，但都会消耗促使读者继续阅读的有限预算。

### 文章自足性

文章应包含目标读者理解核心论点所需的最小上下文。链接可以支持深入探索，却不能代替当前页面必须给出的解释；系列文章可以互相引用，却不能假设读者记得前一篇。文章用 Docker、cgroups、BSD jails 和防火墙文档说明，作者熟悉的术语与资料可能给读者制造巨大的隐形前置工作。

### 阅读摩擦

阅读摩擦可以同时从语言和载体两层观察。^[inferred] 过度正式会制造距离并抹掉作者声音；在 AI 让文字趋同的环境里，个人语气反而更珍贵。移动端横向溢出、低对比度字体和难读字形则会直接阻断阅读。作者称该页面约 25% 的访问来自手机，他的个人博客约为 35%。

## Six Anti-Patterns

| 反模式 | 转嫁给读者的工作 | 作者给出的修正 |
|---|---|---|
| 开头绕远 | 等待作者终于说明主题与收益 | 在标题和前三句话中说明目标读者与回报 |
| “读者除了这一点外什么都懂” | 自行补齐作者默认的术语和经验 | 选择一个真实参考读者，逐项检查其可能不认识的词 |
| 依赖链接解释 | 中断当前阅读，进入另一篇可能很长的资料 | 在页内给最低充分解释，把链接降为可选深入材料 |
| 续篇注入 | 为了开始当前文章先补读整个系列 | 摘要重述当前所需背景，让大多数续篇可以独立阅读 |
| 过度正式 | 穿过冗长、僵硬语言寻找实际意思 | 使用接近日常说话的自然语言，保留作者人格 |
| 忽视 HTML 呈现 | 对抗横向滚动、低对比度和难读字体 | 用浏览器移动预览与无障碍工具检查页面 |

作者用 FreeBSD 防火墙章节举例：给术语挂上一个约两万词的链接，并没有完成解释，只是把大量工作交给读者。对于确实需要拆成系列的复杂项目，也应在每篇文章中重述当前论证必需的背景。

在呈现层，作者建议检查图片和代码块是否导致移动端溢出，并使用浏览器工具检测低对比度文本；若没有字体选择偏好，可考虑 Braille Institute 发布的 Atkinson Hyperlegible 字体。

## Reasoning Flow

下面的顺序是对各节之间推进关系的重建，而不是作者显式列出的论证提纲。^[inferred]

1. 从软件工程借用反模式：把反复导致坏结果的结构从代码迁移到博客写作。
2. 从最常见的开头绕远切入，把视角从“作者想交代什么”切换到“读者为什么继续读”。
3. 从注意力推进到理解，指出作者往往错误估计读者的背景知识。
4. 用链接依赖与续篇依赖说明，外部资料不能替代当前文章的最低充分上下文。
5. 把摩擦推进到语言风格，主张自然、个性化的声音比人为正式更可信、更可读。
6. 最后把写作责任延伸到浏览器中的真实页面，说明内容、语言和渲染共同构成阅读体验。

这条推理不是从一个公理严格演绎，而是从作者观察到的高频失败出发，反复使用“坏例子 → 读者代价 → 替代写法”，最后归纳出读者中心原则。^[inferred]

## Synthesis

文章的六类反模式可以统一理解为“读者负担过高”：^[inferred]

```text
继续阅读的意愿
≈ 可预期收益
− 理解成本
− 跳转成本
− 前置阅读成本
− 语言与界面摩擦
```

这个公式不是原文给出的模型，而是对各节共同结构的压缩。它把好文章的责任说得更直接：作者要提前完成那些本可避免的上下文压缩、信息组织和页面检查，让读者把注意力花在思想本身。^[inferred]

这也扩展了 [[wiki/concepts/Logic Tree and Pyramid Principle|金字塔原理]] 的读者模型：先给结论、再给理由只能解决信息顺序；技术文章还要处理价值承诺、背景知识、页内自足、自然语言和最终渲染。^[inferred]

## Evidence Boundaries

作者称这些是自己最常见于初学者博客的问题，但没有提供系统抽样、错误频率或对照实验，因此“最常见”的排序应视为个人编辑与阅读经验，而不是已验证的普遍分布。^[ambiguous]

“像说话一样写”也不是逐字记录口语。原文反对的是为了显得专业而制造的僵硬表达；一篇技术文章仍然需要书面结构、删改和事实核验。^[inferred]

## Open Questions

- 页内自足与文章长度之间怎样取得平衡，尤其是面对高级读者时？
- 不同读者群的最低充分背景如何通过测试而非作者想象来确定？
- 除了点击和停留时间，什么信号能判断读者真正理解了文章？

## Related

- [[wiki/concepts/Logic Tree and Pyramid Principle]]
- [[wiki/concepts/Cognitive Load Theory]]
- [[wiki/concepts/Code Expression for Human Understanding]]
- [[wiki/topics/Frontend Development]]
- [[wiki/maps/CS Map]]

