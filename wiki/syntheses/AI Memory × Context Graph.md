---
title: AI Memory × Context Graph
category: syntheses
type: synthesis
status: draft
tags: [agents, memory, organization]
sources:
  - wiki/topics/AI Memory
  - wiki/concepts/Context Graph
  - wiki/concepts/Company Brain
  - wiki/concepts/Factual Memory
  - wiki/concepts/Interaction Memory
  - wiki/concepts/Organizational Memory
  - wiki/concepts/Semantic File System
created: 2026-05-23T02:28:40+08:00
updated: 2026-05-23T02:28:40+08:00
summary: AI memory becomes organizationally useful when remembered items are placed in a context graph of owners, evidence, freshness, and permissions.
provenance:
  extracted: 0.22
  inferred: 0.70
  ambiguous: 0.08
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-23
---
# AI Memory × Context Graph

## The Connection

[[wiki/topics/AI Memory]] describes persistent state outside the active context window. [[wiki/concepts/Context Graph]] describes relationships among artifacts, owners, decisions, commitments, evidence, freshness, and permissions.

Their connection is that memory without graph structure is recall, while graph-shaped memory can become governed organizational reasoning. ^[inferred]

## Where They Co-occur

The pair appears in the company-brain cluster:

- [[wiki/concepts/Company Brain]] treats organizational memory as a permissioned substrate for agents.
- [[wiki/concepts/Factual Memory]] asks what exists, what happened, where evidence lives, who owns it, and when it changed.
- [[wiki/concepts/Interaction Memory]] preserves what people meant, debated, promised, assumed, and left unresolved.
- [[wiki/concepts/Organizational Memory]] explains how personal work becomes shared institutional memory.
- [[wiki/concepts/Semantic File System]] treats relationships, ownership, provenance, freshness, and permissions as first-class file-system facts.
- [[wiki/sources/Company Brain Source Guide]] and [[wiki/sources/Memory Is State Not a Service Source Guide]] provide source-layer grounding.

## Cross-cutting Insight

The important question for organizational AI memory is not “can the system remember this?” but “can the system remember this **in relation to the organization**?” ^[inferred]

A remembered statement needs edges: source, owner, artifact, decision, commitment, permission, freshness, contradiction, and downstream action. Without those edges, memory can increase confidence while weakening accountability. With those edges, memory can support governed action: ask, wait, escalate, cite, update, delete, or execute. ^[inferred]

This makes the context graph a memory-quality layer. It turns memory from stored text into navigable institutional state. ^[inferred]

## Tensions and Trade-offs

- **Recall vs. governance**: raw memory can retrieve relevant text, but governed memory must know who can see it and whether it is still valid.
- **Completeness vs. freshness**: remembering everything can preserve history while obscuring what is current.
- **Local tool memory vs. shared state**: isolated tools can remember their own truth, while the organization needs one inspectable, correctable substrate.
- **Automation vs. accountability**: graph memory can enable action, but action requires ownership, approval, and audit trails.

## Open Questions

- Which graph edge types are essential before an AI memory can safely drive organizational action?
- How should stale or contradicted memories be surfaced without overwhelming users?
- When should memory retrieval return text, a graph path, or an explicit uncertainty/permission warning?

## Related

- [[wiki/topics/AI Memory]]
- [[wiki/concepts/Context Graph]]
- [[wiki/concepts/Company Brain]]
- [[wiki/concepts/Factual Memory]]
- [[wiki/concepts/Interaction Memory]]
- [[wiki/concepts/Organizational Memory]]
- [[wiki/concepts/Semantic File System]]
