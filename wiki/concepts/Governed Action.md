---
title: Governed Action
type: concept
status: seed
category: concepts
summary: Governed action is context-aware execution that uses action memory to decide when to move, wait, ask, escalate, stop, or require approval.
sources:
  - https://nanothoughts.substack.com/p/company-brain-why-most-companies
  - https://open.substack.com/pub/nanothoughts/p/company-brain-part-3-interaction?utm_campaign=post&utm_medium=web
  - https://nanothoughts.substack.com/p/company-brain-part-4-action-memory
created: 2026-05-08T15:58:41+08:00
updated: 2026-05-08T22:24:16+08:00
base_confidence: 0.78
lifecycle: draft
lifecycle_changed: 2026-05-08
provenance:
  extracted: 0.80
  inferred: 0.18
  ambiguous: 0.02
aliases:
  - action coordination
  - permissioned action
  - context-aware action
tags:
  - agents
  - governance
  - workflow
---
# Governed Action

Governed action is the execution-governance surface of a [[wiki/concepts/Company Brain]]. It uses [[wiki/concepts/Action Memory]] to decide when to move, wait, ask for help, escalate, stop, require approval, or deliberately do nothing.

## Difference from Automation

The source distinguishes governed action from normal automation:

- Automation executes a known workflow.
- Governed action coordinates action from context.

Examples include drafting a follow-up after a call creates a commitment, creating a ticket after repeated support complaints, warning leadership that teams are making inconsistent assumptions, or deciding that a refund can be processed automatically while a pricing exception needs approval.

## Bridge from Interaction

Part 3 frames [[wiki/concepts/Interaction Memory]] as the bridge between memory and action. Factual memory can tell what exists; interaction memory tells what people meant, debated, promised, and left unresolved.

Governed action is the next requirement: once the company remembers facts and interprets interaction meaning, it still has to coordinate what happens next.


## Action Memory Substrate

Part 4 makes the memory substrate explicit. [[wiki/concepts/Action Memory]] remembers how company work actually moves: procedures, triggers, execution traces, and outcomes. Governed action is the surface that uses that memory to choose and constrain the next move.

This matters because the same action category can hide different risks. A refund, a customer email, a pricing exception, and a production change should not be treated the same way merely because an agent has tools for all of them. A small detail, such as a discount threshold, can change the required approval path.

The source also makes inaction part of governance. Waiting, notifying, asking for approval, and stopping are valid governed actions when the organizational context says execution would be wrong.

## Agent Relevance

For agents, governed action answers:

- what can I safely do?
- what context must I use?
- when should I ask a human?
- when should I deliberately do nothing?
- what prior outcomes or human corrections should change my next action?

This overlaps with [[wiki/topics/AI Harness]] governance: permissions, escalation, approvals, and context lineage must shape whether a proposed action can execute. ^[inferred]

## Incomplete Without Memory

Action without [[wiki/concepts/Context Graph|context]] becomes brittle automation. Reasoning without provenance becomes plausible guessing. A company brain needs both memory and governed action so execution can remain grounded.

## Related

- [[wiki/concepts/Company Brain]]
- [[wiki/concepts/Context Graph]]
- [[wiki/concepts/Action Memory]]
- [[wiki/concepts/Interaction Memory]]
- [[wiki/concepts/Organizational Ontology]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Feedforward and Feedback Controls]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/sources/Company Brain Source Guide]]
