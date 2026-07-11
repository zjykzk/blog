---
title: Verification Gap
category: concepts
tags: [ai-coding, verification, software-engineering, quality]
aliases:
  - verification gap
  - 验证鸿沟
relationships:
  - target: "[[wiki/concepts/Vibe Coding]]"
    type: related_to
  - target: "[[wiki/topics/Testing Strategy]]"
    type: uses
  - target: "[[wiki/concepts/Verification Loop]]"
    type: related_to
  - target: "[[wiki/topics/Spec-Driven Development]]"
    type: uses
sources:
  - wiki/sources/Vibe 时代的软件工程.md
summary: 验证鸿沟是 AI 代码生成速度与人类理解、验证速度之间扩大的差距；它把软件工程瓶颈从生产转向质量判断。
provenance:
  extracted: 0.80
  inferred: 0.18
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-07-03
tier: supporting
created: 2026-07-03T21:45:37+0800
updated: 2026-07-11T23:53:54+0800
---
# Verification Gap

验证鸿沟（verification gap）指生成代码的速度与验证代码正确性的速度之间日益扩大的差距：代码以机器速度产出，而理解、审查和确认仍然以人的速度进行。

[[wiki/sources/Vibe 时代的软件工程]] 把它定义为 Vibe 时代的软件工程中心矛盾：写代码的边际成本下降后，真正稀缺的不是产量，而是判断这段代码是否正确、可维护、安全、符合意图的能力。

## Key Ideas

- AI 降低的是“生成实现”的成本，不会自动降低“理解实现是否正确”的成本；没有参与书写的代码往往更难验证。
- 单步正确率看似很高时，连续多步不验证仍会快速复合成低整体正确率；因此 AI 协作不能只靠“差不多对”的直觉。
- 缩小验证鸿沟的主要手段包括：更小的委托粒度、明确的意图规格、自动测试、类型检查、静态分析、人工高风险评审和频繁可回滚提交。
- 验证鸿沟把 [[wiki/topics/Testing Strategy]] 从质量保障实践升级为 AI 协作的产能约束：不能验证的生成速度，最终会变成复杂度债务。 ^[inferred]

## Engineering Implications

- 任务委托要按“能否验证”来定粒度，而不是按“模型能否一次写出来”来定粒度。
- [[wiki/topics/Spec-Driven Development]]、可执行验收条件和测试用例可以把部分人工理解压力转成机器可检查门禁。
- [[wiki/concepts/Vibe Coding]] 在高风险或难验证区域会扩大验证鸿沟；在低风险且自动验证充分的区域，放飞式协作才更接近合理选择。

## Open Questions

- 如何度量一个代码库当前的验证吞吐量，而不只度量测试覆盖率？
- 哪些工程实践能把“验证速度”提高到足以承接 AI 生成速度？

## Sources

- [[wiki/sources/Vibe 时代的软件工程]] — 本地 PDF 抽取源文档。
