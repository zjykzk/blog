---
title: Agent Harness Anatomy Source Guide
type: source
status: seed
category: sources
summary: Source guide for Akshay Pachaar's agent harness thread, focused on the 12-component harness model and architecture decisions.
sources:
  - https://x.com/akshay_pachaar/status/2041146899319971922
created: 2026-05-05T14:03:13+08:00
updated: 2026-05-05T14:03:13+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.0
aliases:
  - The Anatomy of an Agent Harness
  - Akshay Pachaar agent harness thread
tags:
  - agents
  - harness
  - architecture
---
# Agent Harness Anatomy Source Guide

This page tracks Akshay Pachaar's thread "The Anatomy of an Agent Harness" as a source for the AI / agent engineering cluster.

## Source role

The thread is a broad engineering explainer. It defines the agent harness as the software infrastructure around a model: orchestration loop, tools, memory, context management, state persistence, error handling, guardrails, verification, and subagent orchestration.

It should be used as a source-level overview, not as final authority for every framework detail. The durable value is the component map and the design-decision frame.

## Main claims to promote

- A production agent is better understood as model plus harness, not model plus prompt.
- The orchestration loop is simple in shape, but the hard engineering sits in context, tools, state, recovery, permissions, and verification.
- Tool schemas, memory layers, state checkpoints, error handling, and guardrails are part of the agent's behavior surface.
- Verification loops turn agent work from open-ended generation into feedback-driven execution.
- Multi-agent systems should usually be justified by tool overload, domain separation, or isolation needs, not by novelty. ^[inferred]
- Harness design is a product differentiator because the same model can behave differently under different infrastructure.

## Component map

The source's component inventory maps cleanly onto existing wiki pages:

- orchestration loop and lifecycle: [[wiki/topics/AI Harness]]
- tools and tool schemas: [[wiki/concepts/Agent Tool]]
- context and memory: [[wiki/topics/Context Management]]
- error handling and recovery: [[wiki/syntheses/Agent System Design Space]]
- verification: [[wiki/concepts/Verification Loop]]
- design decisions: [[wiki/syntheses/Agent System Design Space]]

## What should stay source-level

- Specific ranking claims about TerminalBench should stay here unless corroborated by primary benchmark sources.
- Framework-by-framework implementation details should be verified against official documentation before becoming strong claims.
- The scaffolding and operating-system metaphors are useful explanatory aids, but should not become architectural proof by themselves.

## Related

- [[wiki/sources/Agent Engineering Source Guide]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Agent Tool]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/syntheses/Agent System Design Space]]
