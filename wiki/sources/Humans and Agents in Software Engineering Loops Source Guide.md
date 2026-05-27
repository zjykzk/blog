---
title: >-
  Humans and Agents in Software Engineering Loops Source Guide
category: sources
tags: [article, agents, harness, ai-coding, software-engineering]
sources:
  - https://www.martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html
created: 2026-05-27T23:47:19+0800
updated: 2026-05-27T23:47:19+0800
summary: >-
  Source guide for Kief Morris's Martin Fowler article on humans outside, in, and on agentic software engineering loops.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.48
lifecycle: draft
lifecycle_changed: 2026-05-27
aliases:
  - Humans and Agents in Software Engineering Loops
  - humans on the loop
  - agentic flywheel
---
# Humans and Agents in Software Engineering Loops Source Guide

> Source: Kief Morris, “Humans and Agents in Software Engineering Loops,” Martin Fowler, 2026-03-04, https://www.martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html

## Capture Policy

This page preserves the article as source-level material for the AI coding and harness-engineering cluster. It keeps Morris's loop vocabulary, human-role distinctions, and agentic-flywheel argument distinct from broader syntheses such as [[wiki/topics/AI Harness]] and [[wiki/syntheses/AI Engineering Workflow]].

## What It Covers

The article argues that software teams should not choose only between delegating implementation to agents and manually inspecting every generated line. The more durable role is for humans to work **on the loop**: they shape the specifications, workflow, checks, guidance, and harnesses that let agents produce better software over time.

Its central distinction separates the **why loop** from the **how loop**:

- The **why loop** connects an idea, need, or desired outcome to working software and then back through learning from results.
- The **how loop** produces and revises intermediate artifacts such as specifications, task breakdowns, code, tests, infrastructure, design records, and operational checks.
- Agentic engineering becomes a nested-loop problem: some loops decide why a change matters, while other loops decide how artifacts should be generated, validated, and improved.

## Preserved Content

### Opening frame: beyond full delegation versus manual inspection

Morris opens from a tension in agentic software development. One extreme says humans can stay out of implementation and use agents to produce running software from intent. Another extreme says experienced developers must remain close to the code because internal quality still determines maintainability, cost, reliability, and safe change.

The article proposes a third position: humans should manage and improve the loops that transform goals into outcomes. This does not mean abandoning technical responsibility. It means moving responsibility from line-by-line intervention toward system-level steering.

### Why loop and how loop

The article models software development as nested feedback loops.

The **why loop** starts from a human or business reason: an idea, goal, problem, or desired user outcome. Working software is valuable because it feeds learning back into that loop. The loop is not complete when code exists; it is complete when the team learns whether the software produced the intended effect.

The **how loop** contains the artifacts and activities that turn intent into software. Morris describes this as layered:

- outer loops specify and deliver working software;
- middle loops decompose work into smaller items;
- inner loops generate, test, and revise code.

The important shift is that agents can participate in the how loop at many levels, not only at the final code-generation step. They can help draft specifications, split work, produce tests, generate implementation, inspect results, and recommend process changes.

### Humans outside the loop

The “outside the loop” position treats agentic coding as a way for humans to specify outcomes while agents handle implementation. Morris connects this to vibe coding and some interpretations of spec-driven development.

The attraction is real: users and stakeholders care about outcomes more than implementation details. If an agent can create software that satisfies the need, humans may not want to inspect every intermediate artifact.

The article does not dismiss this position, but it limits it. Internal quality still matters whenever structure affects delivery speed, future modification, operational behavior, security, compliance, cost, or reliability. Messy generated systems may work initially, but they can become more expensive for both humans and agents to understand and change. Clean structure remains useful because it gives agents a better substrate for future work.

### Humans in the loop

The “in the loop” position keeps humans directly involved in low-level production and review. Experienced developers can often notice design errors, untangle agent mistakes, and fix problems faster than an agent can spiral through trial and error.

Morris acknowledges this value but warns about bottlenecks. If every generated artifact requires human inspection, the human becomes the scarce review gate. The article compares this to older quality-assurance patterns where defects were caught late by separate inspection rather than prevented earlier in the process.

The shift-left lesson is that quality should be built into the loop before the final human gate. Tests, reviews, architecture checks, design constraints, and operational signals should become early feedback surfaces, not merely end-stage approval rituals.

### Humans on the loop

The article's main proposal is **humans on the loop**. Instead of correcting individual outputs one by one, humans improve the system that produced those outputs.

In this framing, the agent's harness is the set of controls that guide and evaluate agent work. It can include:

- specifications and acceptance criteria;
- quality checks and test stages;
- workflow guidance;
- design reviews and architectural constraints;
- process rules at different levels of the nested loop;
- evaluations that score generated artifacts;
- templates, patterns, ADRs, and other reusable guidance.

The contrast is operational:

| Human stance | Main action | Failure response |
|---|---|---|
| Outside the loop | Ask for outcomes and let agents build | Re-prompt or accept generated results |
| In the loop | Inspect and fix artifacts directly | Correct the code, test, document, or design |
| On the loop | Improve the harness and workflow | Add or refine checks, specifications, guidance, and loop controls |

This connects directly to [[wiki/sources/Harness Engineering Source Guide|Harness Engineering]]: a team does not only operate an agent; it maintains the system of prompts, rules, tools, tests, sensors, and feedback channels around the agent.

### The agentic flywheel

The article closes by extending the on-the-loop stance into an **agentic flywheel**. Agents should not only produce software inside a static harness; they can also help improve the harness.

Morris suggests feeding agents richer signals, including:

- test results;
- evaluation outcomes;
- pipeline measurements;
- performance data;
- failure-scenario validation;
- production operational data;
- user journey logs;
- commercial results.

With these signals, agents can recommend changes to workflow and harness design. Over time, teams may ask agents to score proposed changes by risk, cost, and benefit. Low-risk improvements may eventually be auto-approved, while high-risk changes still require human judgment.

The flywheel is therefore not “agent writes code faster.” It is “the system learns how to make agent work safer, cheaper, and more aligned.” ^[inferred]

### Named vocabulary and references

The source's reusable vocabulary includes:

- vibe coding;
- spec-driven development / SDD;
- why loop;
- how loop;
- humans outside the loop;
- humans in the loop;
- humans on the loop;
- middle loop;
- agent harness;
- harness engineering;
- agentic flywheel;
- shift left;
- design reviews;
- test stages;
- architectural approaches;
- design patterns;
- microservices;
- CUPID;
- ADRs;
- ralph loop.

## Integration Decisions

This page should stay source-level because its main value is the loop vocabulary and role distinction. The stable concept to promote later is not merely “human in the loop,” but the sharper distinction between **in the loop** and **on the loop** for agentic software engineering.

The article extends three existing wiki clusters:

- [[wiki/topics/AI Harness]] — adds the human role as harness steward rather than artifact inspector.
- [[wiki/concepts/Harness Ratchet]] — gives a broader organizational version of turning failures and signals into durable loop improvements.
- [[wiki/sources/Maintainability Sensors for Coding Agents Source Guide|Maintainability Sensors for Coding Agents]] — supplies concrete sensor examples that can feed the on-the-loop flywheel.
- [[wiki/syntheses/Agentic Engineering × Verification Loop]] — reinforces that verification loops are not just acceptance gates; they are part of the work system agents operate inside.

The article's claims about future auto-approval of low-risk harness changes should remain source-level until grounded by examples or operational criteria. Its durable contribution is the control shift: humans create more leverage by improving the loop than by repeatedly repairing loop outputs.

## Open Questions

- What criteria distinguish a low-risk harness change that can be auto-approved from a high-risk process change that needs explicit human review?
- How should commercial, user-journey, production, and code-quality signals be weighted when agents recommend process changes?
- What organizational roles are responsible for maintaining the agentic flywheel: developers, tech leads, platform teams, QA, product, or a new harness-engineering function?

## Related

- [[wiki/sources/Harness Engineering Source Guide]]
- [[wiki/sources/Maintainability Sensors for Coding Agents Source Guide]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/syntheses/Agentic Engineering × Verification Loop]]
