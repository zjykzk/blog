---
title: Verification Loop
type: concept
status: seed
category: concepts
summary: A verification loop gives an agent external feedback, such as tests, visual checks, or evaluators, so errors are caught before they compound.
sources:
  - https://addyosmani.com/blog/agent-harness-engineering/
  - https://x.com/akshay_pachaar/status/2041146899319971922
  - https://martinfowler.com/articles/harness-engineering.html
created: 2026-05-05T14:03:13+08:00
updated: 2026-05-06T22:24:21+08:00
base_confidence: 0.61
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.8
  inferred: 0.2
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

## Hooks and evaluator splits

[[wiki/sources/Agent Harness Engineering Source Guide]] makes the loop more concrete: hooks can run checks at lifecycle points and return only failures to the agent, keeping successful verification silent and failed verification verbose.

For coding agents, that usually means test suites, typecheckers, linters, formatters, visual checks, and pre-commit checks feeding errors back into the loop.

The same source also distinguishes self-verification from generator/evaluator separation. Self-checks are cheap and useful, but separate evaluator roles can catch quality failures that a generator is likely to grade too optimistically.

This connects verification to [[wiki/concepts/Harness Ratchet]]: every repeated verification failure is evidence for a new rule, hook, done condition, or workflow split.

[[wiki/sources/Harness Engineering Source Guide]] sharpens the distinction between computational and inferential verification. Tests, typechecks, and scripts give computational signals; review rubrics, examples, and evaluator judgments give inferential signals when correctness cannot be fully executed.

The stronger harness uses computational checks for properties that can be made executable, then reserves inferential controls for fit, maintainability, architecture, and product judgment. ^[inferred]

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Agent Tool]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/concepts/Feedforward and Feedback Controls]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/Agent Harness Anatomy Source Guide]]
- [[wiki/sources/Agent Harness Engineering Source Guide]]
- [[wiki/sources/Harness Engineering Source Guide]]
