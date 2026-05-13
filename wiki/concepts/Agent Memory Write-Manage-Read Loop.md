---
title: Agent Memory Write-Manage-Read Loop
type: concept
status: seed
category: concepts
summary: Agent Memory Write-Manage-Read Loop models memory as read, update, and management operations coupled to perception, action, feedback, and goals.
sources:
  - https://arxiv.org/abs/2603.07670
created: 2026-05-13T09:59:22+08:00
updated: 2026-05-13T09:59:22+08:00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-05-13
provenance:
  extracted: 0.82
  inferred: 0.18
  ambiguous: 0.0
aliases: [memory loop, write-manage-read loop]
tags:
  - agents
  - memory
---
# Agent Memory Write-Manage-Read Loop

The Agent Memory Write-Manage-Read Loop is the operational model from [[wiki/sources/Memory for Autonomous LLM Agents Source Guide]]: an agent acts by reading relevant memory into the current step, then updates memory from input, action, observation, and reward-like feedback.

## Core Structure

The paper formalizes action selection as a policy over current input, retrieved memory, and active goal. It then formalizes memory update as a function over prior memory, input, action, observation, and feedback.

The important point is that the update function is not simple append. A useful memory system summarizes, deduplicates, scores priority, resolves contradictions, and sometimes deletes.

This makes memory a feedback loop: decisions determine what gets written, and written memory shapes later decisions.

## Why It Is Brittle

A bad write can pollute many downstream decisions because later retrieval makes the wrong record look like system history.

This is why memory quality must be treated as part of [[wiki/topics/AI Harness]] and not only as a storage feature. The harness needs write filters, provenance, contradiction checks, and deletion paths. ^[inferred]

## POMDP Reading

The paper connects agent memory to a partially observable Markov decision process: memory plays the role of a belief state, a sufficient summary of hidden interaction history for selecting better actions.

The useful design question is therefore not "did the database retrieve a similar record?" but "does the maintained memory state help the agent act well under partial observability?"

## Related

- [[wiki/topics/AI Memory]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Agent Memory Mechanism Families]]
- [[wiki/concepts/Agent Memory Evaluation Stack]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/Memory for Autonomous LLM Agents Source Guide]]
