---
title: Coding with AI Source Guide
type: source
status: seed
category: sources
summary: Source guide for Chris Parsons' 2026 Coding with AI article, focused on agentic engineering, trainer roles, harnesses, context resets, and verification bottlenecks.
sources:
  - https://www.chrismdp.com/coding-with-ai/
created: 2026-05-07T22:03:56+08:00
updated: 2026-05-07T22:03:56+08:00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-07
provenance:
  extracted: 0.84
  inferred: 0.16
  ambiguous: 0.0
aliases:
  - How I Use AI to Code
  - Chris Parsons Coding with AI
tags:
  - ai-coding
  - agents
  - harness
---
# Coding with AI Source Guide

This page tracks Chris Parsons' article "How I Use AI to Code" as a source for the AI coding and agent engineering cluster.

## Source Identity

- Source URL: https://www.chrismdp.com/coding-with-ai/
- Extracted with Defuddle from the directly readable HTML page.
- Updated in source: 22 April 2026.
- Earlier version archived by the author at `coding-with-ai-march-2025/`.

## Why This Source Matters

The article argues that coding has become AI's strongest enterprise use case because code is text-dense, precise, and verifiable.

For this wiki, the important contribution is not the tool recommendation itself. It is the role shift: production AI coding should be treated as [[wiki/concepts/Agentic Engineering]], where senior engineers train the harness, encode lessons, choose review surfaces, and improve future agent behavior.

## Main Claims To Promote

### [[wiki/concepts/Agentic Engineering]]

- Vibe coding and agentic engineering are different practices: vibe coding ships without serious checking, while agentic engineering routes checking through tests, type checkers, gates, or human judgment depending on risk.
- The senior skill is deciding where human attention is valuable: Parsons says he skims UI diffs but reads security and database diffs carefully.
- Senior engineers should train the AI and its harness rather than personally reviewing every generated diff.
- A good senior engineer leaves behind markdown, rules, skills, and checks that make the team's AI write better code next week than it did this week.

### [[wiki/concepts/Coding Agent User Harness]]

- The harness around the model matters at least as much as the model: context selection, file chunking, agent loop shape, and privileged rule files compound into different outcomes.
- Practical harness pieces include AGENTS.md or CLAUDE.md, skill files, a portable markdown vault, verification loops, and feedback loops.
- When an agent gets stuck on a trivial issue, Parsons recommends treating it as a context failure rather than a prompt wording failure.

### [[wiki/topics/Context Management]]

- Output quality is described as a curve over context amount: too little context produces generic output, but too much context drowns the model in noise.
- Resetting a drifting conversation with a cleaner brief and smaller chunk is usually cheaper than continuing to correct a polluted context.
- The article cites multi-turn degradation research as support for this reset discipline.

### [[wiki/topics/Testing Strategy]]

- Once generation becomes cheap, verification becomes the bottleneck.
- Tests, type checkers, linting, CI, infrastructure as code, and realistic environments become the surfaces that let agents check their own work before asking humans.
- If verifying AI-generated code takes almost as long as writing it manually, either the output needs a better review surface, verification needs to move into an automated gate, or the task should not have been delegated.

### [[wiki/topics/Spec-Driven Development]]

- Parsons pushes back against specifying the solution upfront for agents, comparing it to a waterfall mistake with a new cover story.
- His alternative is to specify the problem: users, constraints, existing system shape, and success criteria, while leaving solution design open enough for the agent to propose and defend options.
- This creates a useful tension with spec-driven development: the valuable part is explicit problem framing and verification criteria, not premature implementation detail. ^[inferred]

## What Should Stay Source-Level

- Specific vendor recommendations such as installing Claude Code or Codex CLI are time-sensitive and should not become stable wiki claims without more current sources.
- Enterprise adoption statistics and MIT/CTO Craft productivity measurements should stay source-level until corroborated by the cited primary sources.
- The article's prediction about cloud agents and autonomous orchestration is useful trend context but still source-attributed rather than settled.

## Related

- [[wiki/concepts/Agentic Engineering]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/concepts/Harnessability]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/AI Collaboration Scaffolding]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/topics/Spec-Driven Development]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/sources/Agent Engineering Source Guide]]
