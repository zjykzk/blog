---
title: Modern Software Engineering
type: topic
status: seed
category: topics
summary: >-
  Modern Software Engineering treats development as evidence-driven problem solving and shared design knowledge, under change, feedback, AI collaboration, and unintended consequences.

sources:
  - https://www.sei.cmu.edu/documents/1010/1990_005_001_299270.pdf
  - https://martinfowler.com/articles/reduce-friction-ai/
  - https://martinfowler.com/articles/reduce-friction-ai/encoding-team-standards.html
  - https://martinfowler.com/articles/reduce-friction-ai/feedback-flywheel.html
  - inline:laws-of-software-engineering-unintended-consequences-2026-06-09
  - https://dora.dev/guides/dora-metrics/
  - wiki/sources/Vibe 时代的软件工程.md
  - conversation:2026-09-29
created: 2026-04-21
base_confidence: 0.55
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.82
  inferred: 0.18
  ambiguous: 0.00
source_count: 5
updated: 2026-10-05T05:49:32+08:00
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

## Engineering as shared design knowledge

[[wiki/sources/Prospects for an Engineering Discipline of Software Source Guide|Mary Shaw 的 1990 年报告]]补充了职业层面的判准：管理流程使商业生产稳定，而工程学科还要把成熟科学与实践经验组织成可分析、可选择、可复用的设计知识，让普通专业者能够可靠地完成常规设计。报告以土木工程、化学工程和软件中的算法、数据结构、编译器构造作比较；其“尚未普遍工程化”判断属于当时的历史语境。

这为本页的经验主义增加一个检验问题：反馈是否只帮助当前项目过关，还是更新了下一位工程师能够使用的知识？观察、假设和修正若能沉淀为有适用条件的参考资料、设计规则和工具，个人经验才有机会变成职业的共同能力。^[inferred]

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

## Change as empirical intervention

[[wiki/concepts/Law of Unintended Consequences]] strengthens the empirical reading of software engineering: a change is not only an implementation step, but an intervention in a complex socio-technical system.

A feature, fix, logging change, security policy, or UI simplification can produce unexpected benefits, side effects, or perverse results. That means mature engineering practice needs release discipline, rollback paths, observability, and post-change learning, not only pre-change design confidence. ^[inferred]

## Software delivery performance

[[wiki/concepts/DORA Metrics]] adds an application-level measurement layer to the empirical view of software engineering. The five metrics split delivery performance into throughput — change lead time, deployment frequency, and failed deployment recovery time — and instability — change fail rate and deployment rework rate.

The important methodological point is that DORA Metrics are not local productivity counters. They measure whether the whole delivery system can move changes safely and recover from failure, so they belong next to feedback, observability, retrospectives, and improvement loops. ^[inferred]

DORA also warns that metrics should not become goals or cross-team competitions. For [[wiki/topics/Modern Software Engineering]], that makes measurement a problem-framing device: use metrics to expose constraints and learn, not to replace judgment. ^[inferred]

## Vibe-era bottleneck shift

[[wiki/sources/Vibe 时代的软件工程]] adds a compact AI-era restatement of the empirical view: when [[wiki/concepts/Vibe Coding]] makes code generation cheap, software engineering does not disappear; it becomes more visibly about problem understanding, complexity control, and verification.

The source names [[wiki/concepts/Verification Gap]] as the new center of gravity: generated code can arrive at machine speed, but intent clarification, risk judgment, behavior validation, and maintainability review still move through human and institutional feedback loops.

This strengthens the page's core thesis: modern software engineering should be judged by the quality of its evidence loops and recovery structures, not by local implementation throughput. ^[inferred]

[[wiki/concepts/Judgment Externalization]] names the organizational move needed to keep those evidence loops from becoming a new manual bottleneck. The team externalizes standards, evidence, execution, and governance so programs and model judges can run most decisions at machine speed, while people design the rules, audit samples, and adjudicate exceptions. ^[inferred]

## Navigation

- [[wiki/topics/面向对象分析与设计]]
- [[wiki/maps/CS Map]]
- [[wiki/maps/Reading Map]]
- [[wiki/sources/Modern Software Engineering Notes]]
- [[wiki/concepts/AI Collaboration Scaffolding]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/concepts/Vibe Coding]]
- [[wiki/concepts/Verification Gap]]
- [[wiki/concepts/Judgment Externalization]]
- [[wiki/sources/Software Engineering 3.0 Judgment Shift Source Guide]]
- [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]]
- [[wiki/sources/Vibe 时代的软件工程]]
- `pages/软件工程.md`
