---
title: Temporal Memory Validity
type: concept
status: seed
category: concepts
summary: Temporal memory validity distinguishes when a fact was recorded from when it was true, so agents can reconstruct current state without erasing history or mixing stale facts with live ones.
sources:
  - inline:ai-agent-three-paradoxes-2026-07-20
provenance:
  extracted: 0.56
  inferred: 0.39
  ambiguous: 0.05
base_confidence: 0.32
lifecycle: draft
lifecycle_changed: 2026-07-20
tier: supporting
created: 2026-07-20T04:29:25+0800
updated: 2026-07-20T04:29:25+0800
aliases:
  - 记忆时间有效性
  - 幽灵记忆
  - Ghost Memory
relationships:
  - target: "[[wiki/topics/AI Memory]]"
    type: related_to
  - target: "[[wiki/concepts/Agent Memory Write-Manage-Read Loop]]"
    type: extends
  - target: "[[wiki/concepts/Slowly Changing Dimension]]"
    type: related_to
tags:
  - agents
  - memory
  - context
  - data
---
# Temporal Memory Validity

Temporal memory validity is the rule that a memory record must carry not only **what** it claims, but also **when the claim was true**, **when it was observed or recorded**, and **whether a later record superseded it**.

Without this distinction, a memory store can correctly retain every historical statement and still give the agent a false present.

## Ghost Memory Failure

The source calls the failure **ghost memory**:

- the user lived in New York;
- the user moved to London;
- the user now lives in London;
- retrieval returns all three records because they are semantically similar;
- the model receives history, transition, and current state without enough temporal structure to tell them apart.

This is not only a retrieval-ranking problem. The records may all be relevant to the query and individually true, yet jointly unusable because their validity intervals and state-transition roles are missing. ^[inferred]

## Two Clocks

A durable memory should separate at least two clocks:

- **valid time**: when the fact held in the represented world;
- **record time**: when the system learned, wrote, or changed the record.

This is closely related to [[wiki/concepts/Slowly Changing Dimension]] and bitemporal data design. The memory system needs to answer both “what is true now?” and “what did the system believe at an earlier time?” ^[inferred]

Useful metadata can include:

- `valid_from` and `valid_to`;
- `observed_at` or `asserted_at`;
- `supersedes` / `superseded_by`;
- source and confidence;
- record role: state, event, correction, transition, or hypothesis.

## State, Event, and Transition

Temporal memory should not flatten different record types:

- **State**: “The user lives in London.”
- **Event**: “The user signed a London lease on June 1.”
- **Transition**: “The user is moving from New York to London.”
- **Correction**: “The earlier New York address is no longer current.”

An event can remain permanently true as history while the state it produced later changes. Deleting all old records loses provenance; returning all old records as equally current destroys usability. ^[inferred]

The target is therefore **historical retention plus current-state reconstruction**, not either append-only recall or destructive overwrite. ^[inferred]

## Read Protocol

For a current-state question, the read path should:

1. identify the entity and attribute being asked about;
2. select the relevant validity interval;
3. resolve supersession and corrections;
4. prefer evidence valid at the requested time;
5. package earlier states as history only when they help answer the question;
6. expose unresolved overlap as ambiguity rather than silently merging it.

For a historical question, the same store may intentionally return old states and transitions. Retrieval policy must therefore depend on the query's temporal intent, not on similarity alone. ^[inferred]

## Place in the Memory Loop

Temporal validity changes every stage of [[wiki/concepts/Agent Memory Write-Manage-Read Loop]]:

- **Write** records valid time, record time, source, and record role.
- **Manage** detects overlap, contradiction, correction, and supersession.
- **Read** reconstructs the state appropriate to the requested time.
- **Evaluate** tests current-state accuracy, historical reconstruction, and conflict handling separately.

This strengthens [[wiki/topics/AI Memory]]: forgetting is not always deletion. Sometimes the correct operation is to remove a record from current-state retrieval while preserving it as historical evidence. ^[inferred]

## Open Questions

- How should an agent infer validity intervals when users only say “I moved recently”? ^[inferred]
- When two sources disagree about current state, should the system preserve both, ask for clarification, or choose by authority and freshness? ^[inferred]
- Which memories deserve full temporal versioning, and which can safely use last-write-wins? ^[inferred]
- The A-TMA framework and reported “nearly sixfold” improvement in the source require primary-paper verification. ^[ambiguous]

## Related

- [[wiki/topics/AI Memory]]
- [[wiki/concepts/Agent Memory Write-Manage-Read Loop]]
- [[wiki/concepts/Factual Memory]]
- [[wiki/concepts/Slowly Changing Dimension]]
- [[wiki/concepts/Context Information Density]]
- [[wiki/sources/AI Agent 三重悖论 Source Guide]]
