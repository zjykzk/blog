---
title: Agentic Engineering
type: concept
status: seed
category: concepts
summary: Agentic engineering is production AI coding where humans shape harnesses, checks, skills, and attention allocation instead of merely prompting or approving diffs.
sources:
  - https://www.chrismdp.com/coding-with-ai/
  - https://mp.weixin.qq.com/s/64e7occeVSutUJzZAWVutg
  - https://x.com/odysseus0z/status/2030416758138634583?s=46&t=GqNFmk6Xi41yVO4sAJf36g
created: 2026-05-07T22:03:56+08:00
updated: 2026-05-09T21:05:00+08:00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-07
provenance:
  extracted: 0.80
  inferred: 0.20
  ambiguous: 0.0
aliases:
  - agentic coding
  - agentic engineering practice
  - AI coding trainer role
tags:
  - agents
  - ai-coding
  - software-engineering
---
# Agentic Engineering

Agentic engineering is the production practice of using coding agents with explicit verification, harness design, and human judgment allocation.

Chris Parsons contrasts it with vibe coding: vibe coding looks at generated output without seriously checking it, while agentic engineering makes a measured call about which diffs need human eyes and which can be checked by tests, type checkers, automated gates, or other review surfaces.

## Core Shift

The senior engineer's role moves from being the final approver of every diff to training the [[wiki/concepts/Coding Agent User Harness]] that produces future diffs.

This training work includes:

- noticing agent drift before it becomes obvious in the diff
- extracting repeated lessons into repository rules, [[wiki/concepts/Agent Skill|skill files]], or reusable standards
- choosing which risks need human judgment and which can move into computational checks
- teaching teammates the reset, context, and verification instincts needed for agent work

In this view, architectural taste still matters, but it compounds into markdown, skills, tests, and harness rules rather than staying only inside one senior engineer's head. ^[inferred]

The cybernetics framing sharpens this into calibration work: the engineer designs the sensor, actuator, target, and feedback path that let the system steer code changes without constant manual intervention. ^[inferred]

## Control Surface

Agentic engineering treats [[wiki/topics/AI Harness|harness]] design as part of software engineering practice.

A productive harness includes standing instructions, skill files, a [[wiki/concepts/Verification Loop]], and a [[wiki/concepts/Feedback Flywheel]]. When an agent gets stuck on a recurring issue, the failure should be treated as missing context or missing harness structure before it is treated as a prompt wording problem.

This makes agentic engineering a close cousin of [[wiki/concepts/AI Collaboration Scaffolding]]: both externalize tacit collaboration knowledge into durable artifacts that future agent sessions can reuse. ^[inferred]


## Human-side harness

[[wiki/sources/Team AI Coding Harness Seminar Source Guide]] reinforces the human side of agentic engineering. The source argues that prompt rules can often constrain AI output, while getting people to clarify requirements, write tests, self-test rigorously, and review consistently is the harder organizational problem.

This reframes the engineer's responsibility: the team is not only evaluating generated code, but designing the work environment that makes generated code reviewable and repairable. ^[inferred]

The source also predicts that AI will compress roles that mainly translate between vague requirements, prototypes, and code. That replacement claim should stay provisional because it is a single-source seminar judgment and likely varies by product complexity, design depth, and quality responsibility. ^[ambiguous]

## Failure Modes

Parsons names several recurring failure modes:

- accidental vibe coding: broad instructions plus weak checks lead to fast but unsafe production changes
- review fatigue: senior engineers become bottlenecks when agent output grows faster than human diff-reading capacity
- invisible dependencies: teams unknowingly rely on model behaviors that may change across upgrades
- premature relief: teams survive one AI tooling wave and underestimate the next wave of cloud agents and autonomous orchestration

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/concepts/Harnessability]]
- [[wiki/concepts/AI Collaboration Scaffolding]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/syntheses/Agentic Engineering × Verification Loop]] — synthesis
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/topics/Context Management]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/sources/Coding with AI Source Guide]]
- [[wiki/sources/Team AI Coding Harness Seminar Source Guide]]
- [[wiki/sources/Harness Engineering Is Cybernetics Source Guide]]
