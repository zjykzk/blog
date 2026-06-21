---
title: Agent Skill × Context Management
category: syntheses
type: synthesis
status: draft
tags: [agents, skills, context, workflow]
sources:
  - wiki/concepts/Agent Skill
  - wiki/topics/Context Management
  - wiki/concepts/Agent Action Space
  - wiki/concepts/Agentic Engineering
  - wiki/concepts/Continual Learning for AI Agents
  - wiki/sources/Claude Code Skills Source Guide
  - wiki/sources/Agent Skills Survey Paper Source Guide
created: 2026-05-23T02:28:40+08:00
updated: 2026-06-09T10:56:14+08:00
summary: Skills are context-routing devices: they add capability by making task-specific context loadable only when the workflow needs it.
provenance:
  extracted: 0.20
  inferred: 0.72
  ambiguous: 0.08
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-23
---
# Agent Skill × Context Management

## The Connection

[[wiki/concepts/Agent Skill]] and [[wiki/topics/Context Management]] meet at progressive disclosure. A skill is not merely reusable instruction; it is a context boundary that decides when instructions, references, examples, scripts, assets, memory, or hooks should enter the active context. ^[inferred]

This makes skill design a context-management problem. A good skill gives the agent more capability without making every capability permanently visible. A bad skill turns durable knowledge into always-on context noise. ^[inferred]

## Where They Co-occur

The pair appears across the AI and agent cluster:

- [[wiki/concepts/Agent Action Space]] treats skills as a way to enlarge action space without exposing every top-level tool.
- [[wiki/concepts/Agentic Engineering]] frames production AI coding as shaping harnesses, checks, skills, and attention allocation.
- [[wiki/concepts/Continual Learning for AI Agents]] separates durable learning into model, harness, and context/memory layers.
- [[wiki/sources/Claude Code Skills Source Guide]] treats skills as folder-shaped capability bundles with progressive disclosure.
- [[wiki/sources/Agent Skills Survey Paper Source Guide]] adds a lifecycle frame: representation, acquisition, retrieval/selection, and evolution.
- [[wiki/topics/AI Skills Workflow]] treats skills as reusable workflows that gather, order, persist, and reload context.

## Cross-cutting Insight

A skill should be judged by its **activation boundary**, not only by its contents. The question is not “does this skill contain useful knowledge?” but “does the agent reliably load this knowledge exactly when it improves the next decision?” ^[inferred]

This reframes the `description` field, folder structure, reference files, and scripts as routing machinery. The skill body carries capability, but the skill boundary protects context density. In mature agent systems, the boundary may matter more than the body because an excellent skill loaded at the wrong time becomes distractor context. ^[inferred]

## Tensions and Trade-offs

- **Capability vs. context density**: richer skills can help difficult tasks, but every always-loaded instruction competes with task-specific evidence.
- **Progressive disclosure vs. discoverability**: deeply nested references keep context small, but the agent must know when and how to fetch them.
- **General skill vs. narrow skill**: broad skills reduce routing burden but mix failure modes; narrow skills route cleanly but increase catalog and selection complexity.
- **Static authoring vs. self-evolution**: automatically revised skills can adapt from traces, but shared teams still need review before new rules enter durable context.

## Open Questions

- What metrics show that a skill improved context density rather than merely increasing available instructions?
- How should teams test skill activation boundaries against false positives and false negatives?
- When should related skills be composed, and when should they remain separate to protect routing clarity?

## Related

- [[wiki/concepts/Agent Skill]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/concepts/Agent Action Space]]
- [[wiki/topics/Tool Routing]]
- [[wiki/concepts/Skill Self-Evolution]]
