---
title: Agent Action Space
type: concept
status: seed
category: concepts
summary: Agent Action Space is the set of actions an agent can perceive, choose, compose, and execute through tools, skills, subagents, and harness policy.
sources:
  - https://x.com/trq212/status/2027463795355095314
created: 2026-05-06T11:10:34+08:00
updated: 2026-05-06T11:10:34+08:00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-06
provenance:
  extracted: 0.70
  inferred: 0.30
  ambiguous: 0.0
aliases:
  - action space
  - agent tool action space
tags:
  - ai
  - agents
  - tools
  - harness
---

# Agent Action Space

Agent action space is the set of actions a model can perceive, choose, compose, and execute through an [[wiki/topics/AI Harness]]. Thariq Shihipar's Claude Code article frames action-space design as one of the hardest parts of building an agent harness.

The source's core rule is that action space must fit the model's actual capabilities, task, and operating environment. There is no fixed answer such as "one bash tool" or "one tool for every use case."

## Why It Matters

Tools do not only add capability. They also add choices the model has to understand.

Claude Code's design lessons show three recurring failure modes:

- a tool can mix incompatible intentions, such as asking for a plan and questions in the same call
- an output-format convention can look flexible but fail because the model does not reliably follow the exact format
- a tool that helped an earlier model can later constrain a stronger model

This makes action-space design an empirical harness problem: watch model behavior, read outputs, experiment, and revise the surface. ^[inferred]

## Design Lessons

- User elicitation worked better as a dedicated `AskUserQuestion`-style tool than as a side channel inside an exit-plan tool or a markdown output convention.
- Todo lists helped early Claude Code stay on track, but later became constraining when stronger models needed to revise plans and coordinate subagents.
- Task-style coordination is a broader action surface than a private todo list because tasks can include dependencies, updates, deletion, and subagent coordination.
- Search tools changed context building: instead of giving the model preselected RAG context, Claude Code let the model search the codebase and assemble context itself.
- [[wiki/concepts/Agent Skill]] and progressive disclosure expanded the action space without adding a new always-visible tool.
- Specialized subagents can also expand action space by hiding extensive instructions behind a routed capability.

## Evaluation Questions

- Does the model understand when and how to call this action?
- Does the action separate one intention cleanly, or does it combine several decisions?
- Does it reduce user or model friction enough to justify its prompt and choice cost?
- Does it remain useful as the model's capability improves?
- Can the same capability be exposed through progressive disclosure, a skill, or a subagent instead of a new top-level tool?
- Does this action help the agent build better context, or merely add another option? ^[inferred]

## Related

- [[wiki/concepts/Agent Tool]]
- [[wiki/topics/Tool Routing]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/sources/Seeing Like an Agent Source Guide]]
