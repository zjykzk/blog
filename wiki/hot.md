---
title: Hot Cache
category: meta
summary: Recent wiki activity sharpened prompt caching as an agent harness and context-management design constraint.
tags: []
sources: []
created: 2026-05-04
base_confidence: 0.30
lifecycle: draft
lifecycle_changed: 2026-05-05
updated: 2026-05-05T13:58:10+08:00
---

## Recent Activity

- Ingested Thariq's Claude Code prompt-caching article: added stable mode tools, deferred tool loading, cache-safe compaction, and cache-hit monitoring to the prompt-caching cluster.
- Ingested a Claude Code prompt-caching case study: added [[wiki/concepts/Prompt Caching]] and [[wiki/concepts/KV Cache]], then connected cache stability to [[wiki/topics/Context Management]] and [[wiki/topics/AI Harness]].
- Added synthesis pages for [[wiki/syntheses/Business Analysis to Software Design]] and [[wiki/syntheses/React UI Organization Model]].

## Active Threads

- Software methodology is converging around the handoff from business modeling to analysis, DDD, and executable design.
- Frontend knowledge is forming around React as a coordination model for declarative rendering, component boundaries, and state.
- AI / Agent systems are being organized around harness, context management, tool design, memory, permissions, and reusable operational knowledge.
- Prompt and context design now includes an explicit runtime-economics layer: stable prefixes can be reused, while prefix mutation creates cold-cache sessions.
- Tool availability can be made cache-stable by exposing stable stubs and deferring full schema loading until search/select time.

## Key Takeaways

- Structural wiki health is currently clean across frontmatter, summaries, links, index coverage, tag cohesion, and synthesis-gap checks.
- Long-horizon agent performance should be judged by decision-relevant information preserved under finite context, not by how much history is visible.
- Tool minimality, hierarchical memory, and self-evolution can be read as density-preserving harness mechanisms.
- Prompt caching turns context order, tool schema stability, and model continuity into concrete harness responsibilities.
- Cache-hit rate is a production health signal for long-running agents, because low hit rates can reveal accidental prompt or tool-prefix churn.

## Flagged Contradictions
