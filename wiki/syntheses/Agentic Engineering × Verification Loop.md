---
title: Agentic Engineering × Verification Loop
category: syntheses
type: synthesis
status: draft
tags: [agents, ai-coding, testing, software-engineering]
sources:
  - wiki/concepts/Agentic Engineering
  - wiki/concepts/Verification Loop
  - wiki/concepts/Coding Agent User Harness
  - wiki/sources/Coding with AI Source Guide
  - wiki/sources/Compounding Engineering Source Guide
  - wiki/sources/Agentic-First Source Guide
created: 2026-05-23T02:28:40+08:00
updated: 2026-05-23T02:28:40+08:00
summary: Agentic engineering shifts engineering effort from generating code to designing verification loops that make generated work safe to accept.
provenance:
  extracted: 0.22
  inferred: 0.70
  ambiguous: 0.08
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-23
---
# Agentic Engineering × Verification Loop

## The Connection

[[wiki/concepts/Agentic Engineering]] is production AI coding where humans shape harnesses, checks, skills, and attention allocation. [[wiki/concepts/Verification Loop]] is the feedback cycle that catches errors before they compound.

Their connection is the AI-era bottleneck shift: when generation becomes cheap, engineering leverage moves to verification design. ^[inferred]

## Where They Co-occur

This pair appears in pages and sources about production AI coding:

- [[wiki/concepts/Coding Agent User Harness]] defines the developer-owned environment around the coding agent.
- [[wiki/sources/Coding with AI Source Guide]] argues that senior developers become harness trainers.
- [[wiki/sources/Compounding Engineering Source Guide]] treats reviews, failures, tests, and workflow lessons as durable control-surface updates.
- [[wiki/sources/Agentic-First Source Guide]] moves human oversight toward boundaries and validation placement.
- [[wiki/topics/Testing Strategy]] reframes tests as executable acceptance for AI-generated work.

## Cross-cutting Insight

Agentic engineering is not “AI writes code and humans review more.” It is the discipline of deciding which parts of verification can be made executable, which need semantic review, and where each signal enters the workflow. ^[inferred]

A team becomes agentic when its verification loops are strong enough that generated work can be accepted, rejected, repaired, or escalated without relying on heroic human inspection of every diff. ^[inferred]

## Tensions and Trade-offs

- **Generation speed vs. acceptance speed**: faster code generation can increase queue pressure if verification does not improve.
- **Human attention vs. automated gates**: humans should focus on ambiguous trade-offs, but must first make enough checks executable to avoid drowning in routine review.
- **Local task success vs. harness learning**: a fix that passes once is less valuable than a repeated failure that becomes a new durable check.
- **Evaluator agents vs. independent truth**: AI review can help, but must be grounded in tests, traces, requirements, or human judgment.

## Open Questions

- What fraction of a team's review comments can become executable or semi-executable harness checks?
- Which verification failures should update tests, which should update skills, and which should update requirements?
- How should teams measure agentic engineering maturity without counting generated lines?

## Related

- [[wiki/concepts/Agentic Engineering]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/topics/AI Harness]]
