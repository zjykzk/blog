---
title: Tag Taxonomy
category: meta
tags: []
sources: []
created: 2026-05-10T16:02:23+08:00
updated: 2026-05-22T01:47:51+08:00
summary: Controlled tag vocabulary and lint policy for the structured wiki.
base_confidence: 0.30
lifecycle: draft
lifecycle_changed: 2026-05-10
---

# Tag Taxonomy

This file defines tag policy for the structured wiki.

## Rules

- Use at most 5 content tags per page.
- Prefer specific cluster tags over umbrella tags.
- Category already encodes page type, so avoid redundant type tags when possible.
- Reserved sensitivity tags are system tags and are managed outside this taxonomy.

## Retired / ignored umbrella tags

These tags are intentionally not used as ordinary content tags because they create low-cohesion graph clusters:

- `ai` — too broad; use `agents`, `llm`, `harness`, `memory`, `inference`, `ai-coding`, `training`, `context`, `tools`, or another specific tag.
- `source` — redundant with `category: sources`; use concrete source-kind tags such as `paper`, `article`, `blog`, `arxiv`, or the topical tags.

## Common AI cluster tags

- `agents` — agent concepts, tools, harnesses, and runtime behavior.
- `llm` — language model internals and usage.
- `harness` — agent runtime scaffolding, permissions, checks, loops, and orchestration.
- `memory` — persistent memory, context retrieval, organizational memory, and state.
- `context` — context-window, placement, density, anchoring, and context-management issues.
- `feedback` — signals, loops, controls, and evaluation data that steer agent, system, or learning behavior.
- `inference` — model serving, decoding, KV cache, batching, and latency/throughput systems.
- `ai-coding` — coding assistants, agentic engineering, AI development workflow.
- `training` — pretraining, SFT, RL, data, and alignment stages.
- `tools` — agent tool surfaces, routing, selection, and action space.
- `skills` — reusable agent skill/workflow bundles.
- `llm-wiki` — LLM-maintained Markdown wiki architecture, source capture, index/log/hot workflows, and durable knowledge compilation.
- `workflow` — ordered work procedures, reusable process designs, gates, and operational loops.

## Source-kind tags

These tags describe source genre rather than semantic neighborhood, so low graph cohesion is expected and should not trigger automatic cross-linking.

- `roundtable`
- `paper`
- `article`
- `blog`
- `arxiv`
- `survey`
- `book`

## Broad non-AI domains currently used

These tags are coarse routing labels. If cohesion lint flags a large cluster here, prefer splitting into more specific tags or linking through maps/syntheses rather than adding weak page-to-page links.

- `software-engineering`
- `distributed-systems`
- `database`
- `architecture`
- `systems`
- `thinking`
- `learning`
- `cognition`
- `education`
- `management`
- `organization`
- `judgment`
- `reasoning`
- `mechanism`
- `frontend`
- `requirements`
- `testing`
- `wealth`
- `probability`

## Cohesion lint exclusions

- Source-kind tags such as `paper`, `article`, and `arxiv` are genre labels, not topical clusters.
- Broad domain tags with more than 15 pages should be reviewed through taxonomy or map pages before any cross-linking pass.
- Automatic fixes should only add links for small topical clusters where the relationship is semantically specific.

## Alias mappings

- `agent` → `agents`
- `papers` → `paper`
- `sources` → remove; use `category: sources` plus concrete source-kind tags
- `ai` → remove; use a specific AI cluster tag
