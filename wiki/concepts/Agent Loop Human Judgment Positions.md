---
title: Agent Loop Human Judgment Positions
category: concepts
tags: [agents, harness, judgment, ai-coding, software-engineering]
sources:
  - conversation:2026-06-30
  - /Users/zenk/Documents/notes/20260630T181051--paper-loop-engineering__paper.org
created: 2026-06-30T18:22:54+0800
updated: 2026-07-12T00:07:31+0800
summary: >-
  Agent loop human judgment positions are the structural points where humans define value, boundaries, veto power, state, gates, and loop repair instead of operating every agent turn.
provenance:
  extracted: 0.50
  inferred: 0.50
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-06-30
tier: supporting
aliases:
  - 人在智能体循环中的位置
  - human positions in agent loops
  - humans on agent loops
---

# Agent Loop Human Judgment Positions

Agent loop human judgment positions are the structural points where humans remain responsible in an autonomous or semi-autonomous agent loop. ^[inferred]

The core distinction is not whether humans are still “inside” every operation. It is whether humans still occupy the places where value, responsibility, evidence, stopping, and correction are defined. ^[inferred]

In a mature loop, machines turn; humans define direction, gates, doors, and repair mechanisms. ^[inferred]

## What It Is

In an agent loop, a human should move away from routine operation and toward high-leverage judgment points. ^[inferred]

A loop may discover work, spawn agents, run checks, persist state, and schedule the next turn. That does not remove human responsibility. It relocates it from per-step execution into the structure that determines what the loop is allowed to do, how it knows it is right, and where it must stop. ^[inferred]

This extends [[wiki/sources/Humans and Agents in Software Engineering Loops Source Guide|humans on the loop]]: the human is not merely approving final output or hand-driving every turn, but maintaining the loop that produces future outputs. ^[inferred]

## How It Works

A human-owned loop needs at least eight judgment positions. ^[inferred]

1. Value definition: humans define what is worth doing. The loop can read CI failures, issues, commits, and feedback, but it does not know which items are noise, blockers, today-work, or never-automate work unless those criteria are encoded. ^[inferred]

2. Task-boundary cutting: humans define what can safely be handed off. Agent work becomes more reviewable when vague goals are cut into bounded tasks with clear risk levels, acceptance criteria, and escalation paths. ^[inferred]

3. Veto design: humans design who or what can say no. A [[wiki/concepts/Verification Loop]] is strong only when the reviewer, evaluator, or test surface has permission to reject outputs without being overridden by the generator. ^[inferred]

4. Hard gates: humans decide which properties must be executable constraints. Tests, lint, budgets, retry caps, migration safeguards, and no-auto-merge rules should not depend only on model judgment when they can be enforced computationally. ^[inferred]

5. Persistent state design: humans define what survives across turns and how it can be corrected. State files, boards, inboxes, and PR records must carry evidence, status, source, confidence, and next action rather than merely saying `done`. ^[inferred]

6. Human doors: humans reserve at least one non-bypassable entry point into the loop. Final merge, high-risk approval, release sampling, budget overflow, repeated evaluator rejection, and ambiguous requirements are common doors. ^[inferred]

7. Understanding calibration: humans sample outputs to keep their mental model current. The goal is not to read every generated line, but to remain able to explain representative changes and notice comprehension rot. ^[inferred]

8. Loop-level retrospection: humans review the loop itself. Discovery quality, evaluator rejection rate, inbox accumulation, repeated escaped defects, token cost, state-file decay, and skipped gates reveal whether the system remains trustworthy. ^[inferred]

These positions map onto the loop moves: ^[inferred]

- Discovery: define what counts as worth finding. ^[inferred]
- Handoff: define task boundaries and risk classes. ^[inferred]
- Verification: define who can say no and what evidence counts. ^[inferred]
- Persistence: define state schema, provenance, and correction paths. ^[inferred]
- Scheduling: define when the loop may run automatically and when it must stop. ^[inferred]

## Why It Matters

The dangerous failure is not that humans leave mechanical work. The dangerous failure is that humans leave judgment positions while believing they have only left operation positions. ^[inferred]

When an agent loop makes generation cheap, it also makes mistakes cheap to repeat. If the human no longer defines value, cuts responsibility, designs vetoes, reads samples, or repairs the loop, the system can accumulate verification debt, comprehension rot, cognitive surrender, and budget blowout. ^[inferred]

This is why [[wiki/concepts/Agentic Engineering]] treats senior engineering work as harness training rather than diff approval alone. The engineer's leverage comes from turning judgment into checks, skills, rules, state schemas, and review surfaces that improve future agent runs. ^[inferred]

## When to Use

Use this concept when designing or reviewing any recurring agent workflow: ^[inferred]

- coding-agent triage loops
- automated issue repair loops
- wiki maintenance loops
- CI or release-monitoring loops
- multi-agent planning and review systems
- any scheduled automation that can act without a human pressing the next button ^[inferred]

A quick review question is: ^[inferred]

> If this loop runs while no one is watching, where can a human still define value, say no, enter the system, and repair the loop? ^[inferred]

If the answer is unclear, the loop may be automated but not governed. ^[inferred]

## Related

- [[wiki/concepts/Agentic Engineering]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/concepts/Workflow Graph Orchestration]]
- [[wiki/sources/Humans and Agents in Software Engineering Loops Source Guide]]
