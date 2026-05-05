---
title: Verification Loop
type: concept
status: seed
category: concepts
summary: A verification loop gives an agent external feedback, such as tests, visual checks, or evaluators, so errors are caught before they compound.
sources:
  - https://x.com/akshay_pachaar/status/2041146899319971922
created: 2026-05-05T14:03:13+08:00
updated: 2026-05-05T14:03:13+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.82
  inferred: 0.18
  ambiguous: 0.0
aliases:
  - evaluation loop
  - agent verification loop
tags:
  - ai
  - agents
  - verification
---

# Verification Loop

A verification loop is the part of an agent harness that gives the system feedback about whether its work is actually correct.

## Core idea

The Akshay Pachaar thread treats verification as one of the main differences between toy agents and production agents.

The basic pattern is:

- the agent acts
- an external check evaluates the result
- the result is fed back into the harness
- the agent or system corrects course

This matters because multi-step agent work compounds error: even high per-step reliability can still produce poor end-to-end reliability when many steps are chained.

## Verification surfaces

The source names three broad verification surfaces:

- deterministic checks, such as tests, linters, type checkers, or executable validation
- visual checks, such as Playwright screenshots for UI work
- evaluator checks, such as a separate model or subagent judging semantic quality

These surfaces differ in strength. Deterministic checks are usually better when a task has clear executable truth conditions; evaluator checks are useful when correctness is semantic but add latency and another model failure mode. ^[inferred]

## Relation to harness design

Verification should be treated as part of [[wiki/topics/AI Harness]], not as a post-hoc quality ritual. It affects:

- when an orchestration loop can stop
- whether a failed tool call becomes recoverable feedback
- whether a long task should continue, retry, ask the user, or abort
- how much confidence the system should have in its own output

For [[wiki/syntheses/Agent System Design Space]], the key design question is not "does this agent have verification?" but "what kind of truth signal does the task allow, and where does that signal enter the loop?" ^[inferred]

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Agent Tool]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/Agent Harness Anatomy Source Guide]]
