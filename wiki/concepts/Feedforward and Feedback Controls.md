---
title: Feedforward and Feedback Controls
type: concept
status: seed
category: concepts
summary: Feedforward controls shape an agent before action; feedback controls inspect results after action and steer correction or future harness changes.
sources:
  - https://martinfowler.com/articles/harness-engineering.html
created: 2026-05-06T22:24:21+08:00
updated: 2026-05-06T22:24:21+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-06
provenance:
  extracted: 0.84
  inferred: 0.16
  ambiguous: 0.0
aliases:
  - feedforward controls
  - feedback controls
  - agent control loops
tags:
  - agents
  - harness
  - feedback
---
# Feedforward and Feedback Controls

Feedforward and feedback controls are two complementary ways to steer a coding agent inside a [[wiki/topics/AI Harness]].

Feedforward controls shape the agent's behavior before it acts. Feedback controls inspect what happened after it acts and provide correction, acceptance, or learning signals.

## Feedforward Controls

Feedforward controls include:

- project context and architecture descriptions
- task framing and constraints
- examples of desired output
- repository instructions
- checklists and templates
- tool affordances that make the right action easy

These controls try to make a good next action more likely before generation begins.

## Feedback Controls

Feedback controls include:

- test, typecheck, lint, build, or preview results
- reviewer comments
- evaluator output
- failure traces and logs
- post-merge rework signals

These controls catch error after action and decide whether to retry, repair, escalate, or update the harness.

## Why the Split Matters

The split prevents a common AI-coding mistake: trying to solve every quality problem by adding more prompt context.

Some problems need better feedforward context. Others need stronger feedback checks because the correct answer cannot be guaranteed from instructions alone. ^[inferred]

For [[wiki/concepts/Harness Ratchet]], the design question is: should a recurring failure become a feedforward rule, a feedback check, or both?

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/sources/Harness Engineering Source Guide]]
