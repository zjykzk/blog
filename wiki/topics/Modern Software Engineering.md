---
title: Modern Software Engineering
type: topic
status: seed
category: topics
summary: 这页讨论的不是某一条具体方法流派的历史，而是一个更高层的方法论总纲：如何把软件开发理解为一种经验主义、证据驱动的问题求解活动。
sources:
  - https://martinfowler.com/articles/reduce-friction-ai/
  - https://martinfowler.com/articles/reduce-friction-ai/encoding-team-standards.html
  - https://martinfowler.com/articles/reduce-friction-ai/feedback-flywheel.html
  - https://dora.dev/guides/dora-metrics/
created: 2026-04-21
base_confidence: 0.55
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.82
  inferred: 0.18
  ambiguous: 0.00
source_count: 6
updated: 2026-06-11T17:49:52+08:00
aliases:
  - 软件工程
  - modern software engineering
tags:
  - software-engineering
  - methods
---
# Modern Software Engineering

这页讨论的不是某一条具体方法流派的历史，而是一个更高层的方法论总纲：如何把软件开发理解为一种经验主义、证据驱动的问题求解活动。

如果要区分它和相邻页面：

- [[wiki/topics/Software Development Thought Lineage]] 关心不同思想如何历史演化、彼此修正
- [[wiki/topics/Software Methodology]] 关心潘加宇《软件方法》那条具体的建模与分析主线
- 本页关心的是统摄这些实践的上位视角

当前已有笔记里，现代软件工程最核心的一句定义种子是：

- 使用经验主义和科学的方法解决软件问题

这一定义值得保留，因为它把软件工程从“纯编程技巧”拉回到更可验证的方法论：

- 观察现实
- 建立假设
- 通过反馈修正
- 用经验与证据而不是纯直觉推动工程决策

## AI-assisted collaboration

[[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]] adds a modern AI-specific expression of the same empirical principle: do not judge AI coding by first output speed or generated lines.

The article proposes measuring collaboration quality instead:

- first-pass acceptance rate
- iteration cycles per task
- post-merge rework
- review burden compared to manual writing

This fits the modern software engineering view because AI-assisted development should still be judged by fit, maintainability, feedback, and downstream rework, not by local generation speed.

[[wiki/concepts/Encoding Team Standards]] adds a second modern software engineering angle: AI collaboration quality should be improved by systems, not only by individual skill. Treating instructions as repository infrastructure makes team standards visible, reviewable, and improvable through the same feedback loops as code, tests, lint rules, and CI pipelines.

[[wiki/concepts/Feedback Flywheel]] makes the empirical loop explicit: AI collaboration should be measured by review burden, iteration cycles, first-pass acceptance, and post-merge rework, then those signals should update the artifacts that guide future AI work.

## Software delivery performance

[[wiki/concepts/DORA Metrics]] adds an application-level measurement layer to the empirical view of software engineering. The five metrics split delivery performance into throughput — change lead time, deployment frequency, and failed deployment recovery time — and instability — change fail rate and deployment rework rate.

The important methodological point is that DORA Metrics are not local productivity counters. They measure whether the whole delivery system can move changes safely and recover from failure, so they belong next to feedback, observability, retrospectives, and improvement loops. ^[inferred]

DORA also warns that metrics should not become goals or cross-team competitions. For [[wiki/topics/Modern Software Engineering]], that makes measurement a problem-framing device: use metrics to expose constraints and learn, not to replace judgment. ^[inferred]

## Navigation

- [[wiki/topics/面向对象分析与设计]]
- [[wiki/maps/CS Map]]
- [[wiki/maps/Reading Map]]
- [[wiki/sources/Modern Software Engineering Notes]]
- [[wiki/concepts/AI Collaboration Scaffolding]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]]
- `pages/软件工程.md`
