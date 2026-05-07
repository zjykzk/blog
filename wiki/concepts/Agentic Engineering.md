---
title: Agentic Engineering
type: concept
status: seed
category: concepts
summary: Agentic engineering is production AI coding where humans shape harnesses, checks, skills, and attention allocation instead of merely prompting or approving diffs.
sources:
  - https://www.chrismdp.com/coding-with-ai/
created: 2026-05-07T22:03:56+08:00
updated: 2026-05-07T22:03:56+08:00
base_confidence: 0.44
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
  - ai
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

## Control Surface

Agentic engineering treats [[wiki/topics/AI Harness|harness]] design as part of software engineering practice.

A productive harness includes standing instructions, skill files, a [[wiki/concepts/Verification Loop]], and a [[wiki/concepts/Feedback Flywheel]]. When an agent gets stuck on a recurring issue, the failure should be treated as missing context or missing harness structure before it is treated as a prompt wording problem.

This makes agentic engineering a close cousin of [[wiki/concepts/AI Collaboration Scaffolding]]: both externalize tacit collaboration knowledge into durable artifacts that future agent sessions can reuse. ^[inferred]

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
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/topics/Context Management]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/sources/Coding with AI Source Guide]]
