---
title: Verification Loop × Feedback Flywheel
category: synthesis
tags:
  - agents
  - feedback
  - ai-coding
  - workflow
sources:
  - wiki/concepts/Verification Loop.md
  - wiki/concepts/Feedback Flywheel.md
  - wiki/concepts/Harness Ratchet.md
  - wiki/concepts/Feedforward and Feedback Controls.md
  - wiki/concepts/Agentic Engineering.md
  - wiki/concepts/Coding Agent User Harness.md
  - wiki/sources/Coding with AI Source Guide.md
  - wiki/sources/Compounding Engineering Source Guide.md
  - wiki/sources/Agent Harness Engineering Survey Source Guide.md
created: 2026-06-09T14:38:22+08:00
updated: 2026-10-11T17:54:15+08:00
summary: Verification loops catch local task errors; feedback flywheels convert those signals into durable improvements to context, standards, workflows, and guardrails.
provenance:
  extracted: 0.11
  inferred: 0.89
  ambiguous: 0.00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-06-09
---

# Verification Loop × Feedback Flywheel

## The Connection

[[wiki/concepts/Verification Loop]] and [[wiki/concepts/Feedback Flywheel]] describe two different time scales of feedback in AI-assisted engineering. A verification loop asks whether the current agent output is good enough to continue, repair, or stop. A feedback flywheel asks whether repeated verification, review, and rework signals should change the durable collaboration system. ^[inferred]

The loop catches errors inside a task; the flywheel turns patterns across tasks into updated context, standards, workflows, skills, checks, or guardrails. ^[inferred]

## Where They Co-occur

They co-occur in pages about [[wiki/concepts/Harness Ratchet]], [[wiki/concepts/Feedforward and Feedback Controls]], [[wiki/concepts/Agentic Engineering]], [[wiki/concepts/Coding Agent User Harness]], and sources on compounding engineering and agent harness surveys.

The recurring context is AI coding work where generated output is not trusted by default. Tests, linters, visual checks, evaluator reviews, and human comments provide local truth signals; repeated classes of failure then become inputs to system improvement.

## Cross-cutting Insight

The useful unit is not just a passed test or accepted diff. The useful unit is a feedback event that can either close the current task or update the future system. ^[inferred]

A verification loop without a flywheel can catch the same mistake forever. A flywheel without verification has weak evidence and may update standards based on anecdotes. Together they form a two-level learning architecture: local feedback protects the current change; accumulated feedback improves the next run. ^[inferred]

[[wiki/concepts/Loop Engineering]] makes the two levels operational. An inner grader loop checks the current output against deterministic tests or a semantic rubric and returns repair feedback; an outer trace-analysis loop examines repeated tool calls, grader failures, and human corrections, then proposes changes to prompts, tools, memory, skills, or grader configuration. ^[inferred]

The outer loop must retain diagnostic traces rather than only pass rates. A scalar score says that the system failed; the sequence of actions and feedback indicates which durable surface should change. ^[inferred]

## Independent evidence before durable updates

[[wiki/concepts/Verification Loop]] now separates **independence** from **grounding**: a reviewer can be independent yet weakly grounded, or execute real tests while sharing the generator's wrong specification. Passing a check is evidence about the encoded condition, not proof that the condition represents the real goal. ^[inferred]

[[wiki/concepts/Agentic Engineering]] connects error analysis, automated checks, deployment and product feedback. Use local checks to repair the current result, then assess repeated failures before changing shared rules, skills or harness code. Durable updates need recorded evidence, bounded edit rights and rollback; a convincing self-review alone is insufficient. ^[inferred]

## Tensions and Trade-offs

- Fast verification favors cheap checks, but useful flywheel updates need enough diagnostic detail to identify recurring failure classes. ^[inferred]
- Updating artifacts after every failure creates rule bloat; waiting too long lets the same failures repeat. ^[inferred]
- Deterministic checks are stronger for executable truth conditions, while review comments and evaluator output are necessary for product fit, maintainability, and architecture judgment. ^[inferred]

## Open Questions

- Which verification failures deserve durable workflow changes instead of one-off repair? ^[inferred]
- What is the minimum trace detail needed for a feedback flywheel to make good updates without overwhelming maintainers? ^[inferred]
- How should teams prune flywheel artifacts when models, architecture, or tools change? ^[inferred]

## Related

- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Feedforward and Feedback Controls]]
- [[wiki/concepts/Agentic Engineering]]
- [[wiki/concepts/Loop Engineering]]
- [[wiki/syntheses/Coding Agent User Harness × Verification Loop]]
