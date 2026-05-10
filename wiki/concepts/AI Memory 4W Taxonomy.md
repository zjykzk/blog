---
title: AI Memory 4W Taxonomy
type: concept
status: seed
category: concepts
summary: The AI Memory 4W Taxonomy classifies memory by when it persists, what it stores, how it is represented, and which modalities it handles.
sources:
  - https://baijia.online/homepage/survey/Survey%20on%20AI%20Memory.pdf
created: 2026-05-05T16:25:00+08:00
updated: 2026-05-05T16:25:00+08:00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.86
  inferred: 0.14
  ambiguous: 0.0
aliases:
  - 4W Memory Taxonomy
  - When What How Which memory taxonomy
tags:
  - memory
  - taxonomy
  - agents
---
# AI Memory 4W Taxonomy

The AI Memory 4W Taxonomy is a classification scheme from [[wiki/sources/AI Memory Survey Source Guide]] for comparing AI memory systems across four dimensions: When, What, How, and Which.

## The Four Dimensions

**When: lifecycle.** This asks how long memory persists and where it remains accessible.

- transient memory: immediate input buffers or runtime traces
- session memory: information preserved within a task or conversation
- persistent memory: cross-session storage for long-term continuity

**What: content type.** This asks what kind of information the memory captures.

- procedural memory: skills, plans, tool-use routines, workflows
- declarative memory: facts, entities, relations, user details
- metacognitive memory: reflections, self-critiques, strategy notes
- personalized memory: preferences, profiles, identity, interaction patterns

**How: storage.** This asks how memory is represented and retrieved.

- parametric memory inside model weights
- text logs, summaries, or files
- vector stores and embeddings
- structured representations such as graphs, schemas, and databases
- latent representations or compressed internal states

**Which: modality.** This asks what information format the memory handles.

- single-modal memory, usually text
- multimodal memory over images, audio, video, embodied state, or mixed traces

## Why It Matters

The taxonomy prevents "memory" from becoming a single vague bucket.

For [[wiki/topics/AI Memory]], the 4W scheme makes design tradeoffs explicit: a persistent graph of user facts, a session-bound scratchpad, a KV cache, and a skill library are all memory-like, but they differ in lifespan, content, representation, and modality.

For [[wiki/syntheses/Agent System Design Space]], the taxonomy gives a practical checklist for comparing memory architectures. ^[inferred]

## Related

- [[wiki/topics/AI Memory]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Context Information Density]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/AI Memory Survey Source Guide]]
