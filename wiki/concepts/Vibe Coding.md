---
title: Vibe Coding
category: concepts
tags: [ai-coding, software-engineering, agents]
aliases:
  - vibe coding
  - 氛围编程
relationships:
  - target: "[[wiki/concepts/Verification Gap]]"
    type: related_to
  - target: "[[wiki/concepts/Agentic Engineering]]"
    type: contradicts
  - target: "[[wiki/topics/Modern Software Engineering]]"
    type: related_to
sources:
  - wiki/sources/Vibe 时代的软件工程.md
summary: Vibe Coding 是一种把意图交给 AI 生成代码、但人对代码理解逐步降低的协作谱系；它释放速度，也放大验证鸿沟。
provenance:
  extracted: 0.82
  inferred: 0.16
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-07-03
tier: supporting
created: 2026-07-03T21:45:37+0800
updated: 2026-07-03T21:45:37+0800
---
# Vibe Coding

[[wiki/sources/Vibe 时代的软件工程]] 把 Vibe Coding 放在一条人机协作谱系里理解：从补全式、结对式、委托式到放飞式，人对代码的逐字符理解逐步下降，生产速度逐步上升。

窄义的 Vibe Coding 指 Karpathy 原始语境中“顺着感觉走、拥抱指数增长、忘记代码本身存在”的放飞式开发；宽义上，它也可以指 AI 让人从亲手打字转向描述意图、接受生成、再决定是否检查的整组协作方式。

## Key Ideas

- Vibe Coding 的核心变化不是“多了一个自动补全工具”，而是代码生成成本快速下降，人的主要工作从写代码转向表达意图、控制委托粒度和验证结果。
- 放飞式 Vibe Coding 合法存在于低风险、易验证的区域；一旦任务高风险或难验证，它就会变成把责任交给自己没有理解的代码。 
- Vibe Coding 与 [[wiki/concepts/Agentic Engineering]] 的关键差别在验证责任：前者容易只看运行效果，后者必须把测试、类型检查、自动门禁或人工评审接进循环。
- 对复杂系统而言，AI 生成的代码越快，越需要 [[wiki/concepts/Verification Gap]] 这类概念来约束“看起来能跑”的诱惑。 ^[inferred]

## Failure Modes

- 巨型一次性委托会制造无法验证的大块产物，让人只能全盘接受或全盘放弃。
- 只看演示效果会掩盖安全漏洞、边界条件、长期可维护性和业务语义错误。
- “以后更强模型会重构烂摊子”的想法忽略了无结构、无文档、无测试代码的理解成本会随时间复利增长。

## Open Questions

- 哪些任务可以明确划入“低风险 × 易验证”的放飞区？
- 团队如何训练新人既能享受 Vibe Coding 的速度，又不失去读代码、设计接口和判断风险的能力？

## Sources

- [[wiki/sources/Vibe 时代的软件工程]] — 本地 PDF 抽取源文档。
