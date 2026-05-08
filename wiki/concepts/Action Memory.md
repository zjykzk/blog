---
title: Action Memory
type: concept
status: seed
category: concepts
summary: Action memory remembers when company work should wake up, which path should run, what guardrails apply, and what happened afterward.
sources:
  - https://nanothoughts.substack.com/p/company-brain-part-4-action-memory
created: 2026-05-08T22:24:16+08:00
updated: 2026-05-08T22:24:16+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-08
provenance:
  extracted: 0.84
  inferred: 0.14
  ambiguous: 0.02
aliases:
  - company action memory
  - organizational action memory
  - operational memory
tags:
  - ai
  - memory
  - organization
  - workflow
---

# Action Memory

Action memory is the third layer of a [[wiki/concepts/Company Brain]]. It remembers how the company moves: when a workflow should wake up, when it should stay still, which path should run, what guardrails apply, and what happened after action.

The source explicitly distinguishes action memory from ordinary workflow memory. It is not only the memory of a process; it is the memory of when a process becomes relevant and what should happen at every step in between.

## Why It Matters

Companies forget how work actually gets done, especially across people, systems, approvals, and time. A pricing exception may look like one workflow, but a small change in discount percentage can trigger finance approval, legal review, CRM updates, customer communication, and a different closing timeline.

This makes action memory the operational continuity layer between [[wiki/concepts/Interaction Memory]] and [[wiki/concepts/Governed Action]]. Interaction memory explains what people meant and promised; action memory knows what should happen next, whether it should happen now, and who or what should act.

## Four Parts

The source splits action memory into four parts:

- **Procedural memory**: how a process is supposed to work, such as onboarding, refunds, pricing approvals, incidents, or security reviews.
- **Trigger memory**: when something should happen, such as a churn-risk signal, unresolved ticket age, discount threshold, approaching renewal, late commitment, changed metric, meeting promise, or agent action needing review.
- **Execution memory**: what actually happened in a specific case, including approvers, delays, workarounds, agents involved, corrections, handoff failures, and confusing systems.
- **Outcome memory**: what happened after action, such as renewal, technical debt, risk reduction, human correction, or recurrence of the same issue.

These parts prevent action from becoming surface automation. The company should not treat every completed workflow as a successful workflow.

## First-Class Inaction

The article's strongest action-design claim is that doing nothing must be a first-class action. A useful company brain acts because context says it should, and stays still when context says it should not.

Valid next moves can include waiting, asking for approval, notifying someone without mutating a system, stopping because the action is organizationally wrong, or deliberately doing nothing.

For agents, this means action memory is not just a tool-selection layer. It is a policy-and-context layer that decides whether a tool call should exist at all. ^[inferred]

## Guardrail Role

Action memory should function as guardrails. A refund, customer email, pricing exception, and production change have different risk shapes even if an agent can technically perform all of them.

The system must remember the difference between routine actions and actions that only look routine. Some actions are safe to execute; some require approval; some affect money or production; some differ from precedent in one detail that changes risk.

## Loop Back into Memory

The loop closes when actions become memory. If an agent drafts an email, creates a ticket, updates Salesforce, escalates a risk, requests approval, or notifies an owner, the system should remember what happened.

A successful action becomes precedent. A failed action becomes risk memory. A human correction becomes a signal. A workflow change becomes part of how the company operates next time.

This links action memory to [[wiki/topics/AI Memory]]: downstream execution must feed back into persistent memory rather than remaining an isolated tool trace. ^[inferred]

## Role-Specific Questions

The source emphasizes that roles see action memory differently:

- An IC needs the next step and enough context to do it well.
- A manager needs to see where handoffs fail and commitments are stuck.
- A CEO needs to know where the company repeatedly fails to turn decisions into action.

For the CEO, action memory makes momentum loss pointable: it maps where strategy silently translates into nothing.

## Open Questions

- How should action memory distinguish official process from the actual path without rewarding unhealthy process bypasses? ^[inferred]
- What action traces should become durable precedent, and what should expire as one-off exceptions? ^[inferred]
- How should approval thresholds be represented so agents can detect small details that change risk?

## Related

- [[wiki/concepts/Company Brain]]
- [[wiki/concepts/Factual Memory]]
- [[wiki/concepts/Interaction Memory]]
- [[wiki/concepts/Governed Action]]
- [[wiki/concepts/Context Graph]]
- [[wiki/concepts/Organizational Memory]]
- [[wiki/topics/AI Memory]]
- [[wiki/topics/AI Harness]]
- [[wiki/sources/Company Brain Source Guide]]
