---
title: Harness Engineering Source Guide
type: source
status: seed
category: sources
summary: Source guide for Martin Fowler's harness engineering article, focused on user-owned harnesses for coding agents and their control loops.
sources:
  - https://martinfowler.com/articles/harness-engineering.html
created: 2026-05-06T22:24:21+08:00
updated: 2026-05-06T22:24:21+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-06
provenance:
  extracted: 0.86
  inferred: 0.14
  ambiguous: 0.0
aliases:
  - Martin Fowler harness engineering
  - coding agent harness engineering source guide
tags:
  - agents
  - harness
  - ai-coding
---
# Harness Engineering Source Guide

This page tracks Martin Fowler's article "Harness Engineering" as a source for the AI / agent engineering cluster.

The article is about how software developers can shape the environment around coding agents instead of treating the agent as a self-contained black box. For this wiki, its durable value is that it moves [[wiki/topics/AI Harness]] from agent-builder architecture toward user-owned workbench design.

## Core Claims

- The practical unit of AI coding is not just "model plus vendor UI"; it is the model plus the user's surrounding harness.
- A harness includes the context, tools, rules, affordances, templates, review loops, and execution environment that make coding-agent behavior more useful.
- Users can improve agent outcomes by engineering the harness, even when they cannot change the underlying model.
- Harness engineering relies on both feedforward controls that shape inputs before generation and feedback controls that inspect and correct outputs after generation.
- Some harness controls are computational, such as tests and scripts, while others are inferential, such as reviewer judgment or agent-readable checklists.

## Promotions

### [[wiki/concepts/Coding Agent User Harness]]

The article's main contribution is a user-side harness frame: developers can deliberately organize prompts, repo rules, test surfaces, template workspaces, and review paths around a coding agent.

### [[wiki/concepts/Feedforward and Feedback Controls]]

The source separates controls that steer the agent before work from controls that evaluate or correct the work afterward.

### [[wiki/concepts/Computational and Inferential Controls]]

The source also distinguishes executable controls from judgment-bearing controls. This helps explain why tests alone do not cover the whole harness, and why checklists alone are weaker than executable checks when executable truth is available. ^[inferred]

### [[wiki/concepts/Harnessability]]

The article introduces harnessability as a design quality: a task, codebase, or workflow is easier to use with coding agents when it exposes stable context, clear constraints, testable boundaries, and repeatable templates.

## Relation to Existing Pages

This source strengthens [[wiki/topics/AI Harness]] by shifting attention from vendor-side agent architecture to the developer's surrounding environment.

It strengthens [[wiki/syntheses/AI Engineering Workflow]] because user harnessing is a practical bridge between collaboration scaffolding, standards, verification, and repeatable agent workflows.

It also gives [[wiki/concepts/Harness Ratchet]] a broader control vocabulary: the ratchet can add feedforward controls, feedback controls, computational checks, or inferential review artifacts depending on the failure.

## Open Questions

- How much of a coding-agent harness should be shared at repository/team level versus personalized for one developer?
- When does a harness template become a skill, and when should it remain a lightweight prompt or document? ^[inferred]
- How should teams measure harnessability before and after refactoring workflow or codebase structure?

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/concepts/Feedforward and Feedback Controls]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/concepts/Harnessability]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/sources/Agent Engineering Source Guide]]
