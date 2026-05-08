---
title: Governed Action
type: concept
status: seed
category: concepts
summary: Governed action is context-aware execution that knows when to move, wait, ask, escalate, stop, or require approval.
sources:
  - https://nanothoughts.substack.com/p/company-brain-why-most-companies
created: 2026-05-08T15:58:41+08:00
updated: 2026-05-08T15:58:41+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-08
provenance:
  extracted: 0.76
  inferred: 0.22
  ambiguous: 0.02
aliases:
  - action coordination
  - permissioned action
  - context-aware action
tags:
  - ai
  - agents
  - governance
  - workflow
---

# Governed Action

Governed action is the action-coordination layer of a [[wiki/concepts/Company Brain]]. It does not only answer questions; it helps the organization decide when to move, wait, ask for help, escalate, or stop.

## Difference from Automation

The source distinguishes governed action from normal automation:

- Automation executes a known workflow.
- Governed action coordinates action from context.

Examples include drafting a follow-up after a call creates a commitment, creating a ticket after repeated support complaints, warning leadership that teams are making inconsistent assumptions, or deciding that a refund can be processed automatically while a pricing exception needs approval.

## Agent Relevance

For agents, governed action answers:

- what can I safely do?
- what context must I use?
- when should I ask a human?

This overlaps with [[wiki/topics/AI Harness]] governance: permissions, escalation, approvals, and context lineage must shape whether a proposed action can execute. ^[inferred]

## Incomplete Without Memory

Action without [[wiki/concepts/Context Graph|context]] becomes brittle automation. Reasoning without provenance becomes plausible guessing. A company brain needs both memory and governed action so execution can remain grounded.

## Related

- [[wiki/concepts/Company Brain]]
- [[wiki/concepts/Context Graph]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Feedforward and Feedback Controls]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/sources/Company Brain Source Guide]]
