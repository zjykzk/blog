---
title: Agent Harness Engineering Source Guide
type: source
status: seed
category: sources
summary: Source guide for Addy Osmani's Agent Harness Engineering article, focused on harnesses as configurable runtimes, failure ratchets, and service APIs.
sources:
  - https://addyosmani.com/blog/agent-harness-engineering/
created: 2026-05-05T15:10:00+08:00
updated: 2026-05-06T22:45:47+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.84
  inferred: 0.16
  ambiguous: 0.0
aliases:
  - Addy Osmani agent harness engineering
  - Agent Harness Engineering article
tags:
  - agents
  - harness
  - engineering
---
# Agent Harness Engineering Source Guide

This page tracks Addy Osmani's April 19, 2026 article "Agent Harness Engineering" as a source for the AI / agent engineering cluster.

## Source Role

The article is a synthesis-oriented engineering essay rather than a paper. Its main value is that it connects several existing source threads in the vault:

- Viv Trivedy's "agent = model + harness" framing
- HumanLayer's "skill issue" / configuration framing
- Anthropic's long-running agent harness lessons
- user-facing agent workflow and coding-agent product examples

For this wiki, the article mainly strengthens [[wiki/topics/AI Harness]], [[wiki/topics/Context Management]], [[wiki/concepts/Verification Loop]], [[wiki/concepts/Agent Tool]], and [[wiki/syntheses/Agent System Design Space]].

## Extracted Claims

- A coding agent should be understood as the model plus the harness around it.
- The harness includes prompts, tools, context policy, hooks, sandboxes, subagents, feedback loops, observability, and recovery paths.
- Agent failures are often actionable harness failures rather than only model failures.
- Filesystem and Git provide durable state, coordination surface, progress tracking, rollback, and experiment branching.
- Bash and code execution act as general-purpose tools, but they need sandbox boundaries and good default tooling.
- Context rot makes compaction, tool-output offloading, skills, and full context resets central harness mechanisms.
- Long-horizon agent work needs planning, continuation loops, verification, and often separate generator/evaluator roles.
- Hooks enforce constraints at lifecycle points such as before tool calls, after edits, before commits, or at session start.
- Short `AGENTS.md`-style rulebooks are high-leverage only when each line has earned its place through a real failure or hard constraint.
- Harness components encode assumptions about what the model cannot yet do by itself; as models change, some scaffolding should be removed and new scaffolding may become necessary.
- Agent products are increasingly trained with harnesses in the loop, which can make models especially fluent with particular filesystem, shell, planning, or subagent primitives.
- Harness-as-a-Service shifts agent building from raw completion APIs toward configurable runtimes with loops, tools, context management, hooks, and sandbox primitives.
- Harness patterns converge across coding agents even when the underlying models differ.

## Promoted Knowledge

### [[wiki/concepts/Harness Ratchet]]

The article's most durable new concept is the ratchet: every recurring mistake should become a rule, hook, check, workflow split, or other harness change.

### [[wiki/topics/AI Harness]]

The article reinforces that harnesses are product behavior surfaces, not interchangeable wrappers. Different tool schemas, state policies, execution environments, and verification loops can make the same model behave differently.

### [[wiki/topics/Context Management]]

The article contributes the phrase "context rot" and maps it to concrete harness mechanisms: compaction, offloading large tool output, progressive skill disclosure, and full reset from a structured handoff file.

### [[wiki/concepts/Verification Loop]]

The article makes verification more operational by tying it to hooks, test suites, done conditions, generator/evaluator separation, and sprint contracts.

### [[wiki/concepts/Agent Tool]]

The article frames tools as a context and security surface: each tool schema competes for model attention, and external MCP/tool descriptions are trusted prompt text.

### [[wiki/syntheses/Agent System Design Space]]

The article strengthens the view that harness design is a moving design space. Better models can make old scaffolding redundant, but they also open new task surfaces that need memory policy, multi-agent coordination, evaluator roles, and just-in-time tool/context assembly.

The Harness-as-a-Service framing also moves harnesses from application glue into an API layer: developers increasingly configure a runtime rather than building every loop, approval flow, sandbox, and context policy from scratch.

## Open Questions

- When should a harness remove old rules because the current model no longer needs them?
- How should teams measure whether a harness rule is still useful or has become context noise?
- Can agents analyze their own traces well enough to propose high-quality harness changes? ^[inferred]
- What parts of harness assembly should become just-in-time and compiler-like rather than preconfigured at startup? ^[inferred]
- How much model behavior is portable across harnesses when post-training has optimized the model around specific harness primitives? ^[inferred]

## Related

- [[wiki/sources/Agent Engineering Source Guide]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Agent Tool]]
- [[wiki/syntheses/Agent System Design Space]]
