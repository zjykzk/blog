---
title: Seeing Like an Agent Source Guide
type: source
status: seed
category: sources
summary: Source guide for Thariq Shihipar's Claude Code article on action-space design, tool iteration, elicitation, task coordination, search, and progressive disclosure.
sources:
  - https://x.com/trq212/status/2027463795355095314
created: 2026-05-06T11:10:34+08:00
updated: 2026-05-06T11:10:34+08:00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-06
provenance:
  extracted: 0.84
  inferred: 0.16
  ambiguous: 0.0
aliases:
  - Lessons from Building Claude Code Seeing like an Agent
  - Seeing like an Agent
  - Claude Code action space article
tags:
  - agents
  - tools
  - claude-code
---
# Seeing Like an Agent Source Guide

This page keeps Thariq Shihipar's *Lessons from Building Claude Code: Seeing like an Agent* as a source-facing note and routes its durable claims into the AI / Agent wiki cluster.

## Source

- Title: *Lessons from Building Claude Code: Seeing like an Agent*
- Author: Thariq Shihipar
- Original URL: https://x.com/trq212/status/2027463795355095314
- Accessible mirror used during ingest: tool.lu mirror of the article content

## Core Contribution

The article's strongest contribution is an action-space design rule: agent tools should be shaped to the model's actual abilities, task, and environment, and those abilities must be inferred from observed behavior rather than assumed.

This strengthens [[wiki/topics/AI Harness]] because tool design is not only capability exposure. It is the design of what actions the model can see, how it can choose them, and how the harness turns those choices into reliable interaction. ^[inferred]

## Claims Promoted

### [[wiki/concepts/Agent Action Space]]

- Building an agent harness requires constructing an action space.
- There is no fixed answer between a single general tool and many narrow use-case tools.
- Tool design should be revised by observing model outputs and behavior.
- Better models may no longer need tools or reminders that helped weaker models.
- Adding a top-level tool has a high bar because each tool becomes another option the model has to consider.

### [[wiki/concepts/Agent Tool]]

- A dedicated question-asking tool worked better than overloading a planning tool or relying on a markdown convention.
- A tool should encode a structured interaction when exact output shape matters.
- A tool only works if the model understands when and how to call it.

### [[wiki/topics/Context Management]]

- Claude Code moved from preselected RAG context toward letting the model search the codebase with tools.
- Progressive disclosure lets the agent discover context incrementally through skills and referenced files.
- The Claude Code Guide subagent is an example of adding capability and context without adding another top-level tool.

## What Should Stay Source-Level

- The specific Claude Code implementation history should remain source-level unless corroborated by other sources.
- The exact replacement of TodoWrite by Task Tool should not be generalized into a universal task-model requirement.
- The article's analogy to math tools is useful as explanation, but the promoted concept should remain action-space fit, not the analogy itself. ^[inferred]

## Related

- [[wiki/concepts/Agent Action Space]]
- [[wiki/concepts/Agent Tool]]
- [[wiki/topics/Tool Routing]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/sources/Agent Engineering Source Guide]]
- [[wiki/maps/AI Map]]
