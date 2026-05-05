---
title: Testing Strategy
type: topic
status: seed
category: topics
summary: Testing Strategy combines test layering, test purpose, and AI-era quality gates to increase confidence in software changes.
sources:
  - https://martinfowler.com/articles/reduce-friction-ai/
  - https://martinfowler.com/articles/reduce-friction-ai/design-first-collaboration.html
  - https://martinfowler.com/articles/reduce-friction-ai/encoding-team-standards.html
  - https://martinfowler.com/articles/reduce-friction-ai/feedback-flywheel.html
created: 2026-04-21
base_confidence: 0.53
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.80
  inferred: 0.20
  ambiguous: 0.0
source_count: 6
updated: 2026-05-05T17:55:00+08:00
aliases:
  - 测试模型
tags:
  - testing
  - quality
  - software-engineering
---

# Testing Strategy

测试策略至少有两个互补视角：

- 从投入层次看：Test Pyramid
- 从测试目的看：Test Quadrants

## Test Pyramid

强调测试层次与自动化投入比例：

- 单元测试最多
- 集成测试居中
- 端到端测试最少

目标是提高自动化效率，降低高层测试维护成本。

## Test Quadrants

强调测试活动的目的与受众：

- Q1：技术导向，支持开发
- Q2：业务导向，支持开发
- Q3：业务导向，评估产品
- Q4：技术导向，评估产品

目标是避免只做某一类测试，而忽略产品质量的其他维度。

## Practical takeaway

- 用四象限规划“要覆盖什么”
- 用金字塔决定“自动化资源怎么配”

## AI-assisted development metrics

[[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]] adds a useful testing-adjacent point: generation speed is a weak quality metric for AI coding.

Better signals are closer to review and delivery outcomes:

- first-pass acceptance rate
- iteration cycles per task
- post-merge rework required
- review burden compared to manual writing

These metrics treat AI output as something that must survive team standards and downstream change, not just compile once. ^[inferred]

[[wiki/concepts/Design-First Collaboration]] adds a more operational testing bridge: after capabilities, components, and interactions are agreed, the contracts level can define interfaces, types, and schemas before implementation.

Those contracts can be turned into tests before the assistant writes code. This makes AI-assisted TDD more natural because the test target is an agreed design artifact rather than an inferred implementation. ^[inferred]

[[wiki/concepts/Encoding Team Standards]] extends testing strategy from tests to quality gates. A security instruction, review instruction, or test-quality instruction can encode what the team treats as blockers, must-fix issues, and advisories.

This is not a replacement for automated tests. It is a way to make review and security checks more consistent across developers and AI sessions, especially when the relevant standard is architectural judgment or threat-model knowledge rather than a simple assertion. ^[inferred]

[[wiki/concepts/Feedback Flywheel]] adds the measurement loop: accepted output, repeated review comments, regeneration cycles, and post-merge rework should decide which tests, review instructions, standards, or guardrails need to change next.

## Peer topics

- [[wiki/topics/Testing Purpose]]
- [[wiki/topics/Spec-Driven Development]]
- [[wiki/concepts/AI Collaboration Scaffolding]]
- [[wiki/concepts/Design-First Collaboration]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]]

## Navigation

- [[wiki/maps/CS Map]]

## Source notes

- `pages/测试模型.md`
