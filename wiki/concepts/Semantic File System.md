---
title: Semantic File System
type: concept
status: seed
category: concepts
summary: A semantic file system is a memory layer where artifact relationships, ownership, provenance, freshness, and permissions matter as much as text.
sources:
  - https://open.substack.com/pub/nanothoughts/p/company-brain-part-2-factual-memory?utm_campaign=post&utm_medium=web
  - https://nanothoughts.substack.com/p/memory-is-state-not-a-service
created: 2026-05-08T20:38:05+08:00
updated: 2026-05-11T10:27:21+08:00
base_confidence: 0.61
lifecycle: draft
lifecycle_changed: 2026-05-08
provenance:
  extracted: 0.70
  inferred: 0.27
  ambiguous: 0.03
aliases:
  - company semantic file system
  - semantic memory layer
  - relationship-aware file system
tags:
  - memory
  - knowledge-graph
  - organization
---
# Semantic File System

A semantic file system is the source's name for a company memory layer where artifacts are not just blobs of text. The relationships, entities, facts, state changes, provenance, ownership, freshness, and permissions around each artifact matter as much as the artifact itself.

## Core Idea

The article contrasts durable [[wiki/concepts/Factual Memory]] with simple RAG across enterprise data. RAG can retrieve fragments, but company memory needs provenance, permissions, ownership, freshness, source-of-truth boundaries, and relationships between artifacts.

In a semantic file system, a customer call can connect to an account, the account to open issues, issues to tickets, tickets to product areas, product areas to owners, and owners to decisions. The later state-substrate article adds that the durable memory is often the state change caused by an artifact: what became true, who owns it, which commitment was created, what action followed, and whether the company learned from the outcome.

## Difference from a Knowledge Graph

The source says this is more than a knowledge graph pasted on top of documents and more than markdown with metadata. The quality of the relationships determines the quality of the memory.

A [[wiki/concepts/Context Graph]] can be treated as the reasoning-facing side of this layer: it turns relationship-rich facts into usable context for decisions and actions. ^[inferred]

## Interface Implication

A semantic file system may include chat, but cannot only be chat. It should be mutable, appear inside work, surface facts based on what someone is doing, and respect the boundary between assistance and surveillance.

The goal is to help the company remember without making people feel watched.

## Open Questions

- Which relationships should be explicit schema, and which should remain inferred at query time? ^[inferred]
- How can the layer preserve source-of-truth boundaries without forcing every team into one central repository? ^[inferred]
- How can proactive surfacing avoid becoming surveillance or notification spam? ^[inferred]

## Related

- [[wiki/concepts/Factual Memory]]
- [[wiki/concepts/Company Brain]]
- [[wiki/concepts/Context Graph]]
- [[wiki/concepts/Organizational Memory]]
- [[wiki/topics/AI Memory]]
- [[wiki/sources/Company Brain Source Guide]]
- [[wiki/sources/Memory Is State Not a Service Source Guide]]
