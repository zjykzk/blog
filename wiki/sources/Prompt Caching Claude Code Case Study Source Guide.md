---
title: Prompt Caching Claude Code Case Study Source Guide
type: source
status: seed
summary: Source guide for prompt-caching case studies that frame Claude Code cache efficiency as an agent harness design problem.
category: sources
sources:
  - https://x.com/_avichawla/article/2044670188998803855
  - https://x.com/trq212/status/2024574133011673516
source: https://x.com/_avichawla/article/2044670188998803855
created: 2026-05-05T00:00:00+08:00
updated: 2026-05-05T13:58:10+08:00
base_confidence: 0.61
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.9
  inferred: 0.08
  ambiguous: 0.02
aliases:
  - Claude Code prompt caching case study
  - Claude cache hit-rate case study
  - Lessons from Building Claude Code
tags:
  - source
  - ai
  - agents
  - caching
  - claude-code
---

# Prompt Caching Claude Code Case Study Source Guide

## Current role

These sources are best treated as engineering explainers and case studies, not as canonical provider specifications.

Their durable value is that they connect prompt caching mechanics to agent architecture: cache efficiency depends on how the harness orders, stabilizes, and mutates context across long-running sessions.

## Source metadata

- Title: *A case study on how Claude achieves 92% cache hit-rate*
- Author handle: `_avichawla`
- URL: https://x.com/_avichawla/article/2044670188998803855
- Type: engineering article / social article
- Ingested: 2026-05-05
- Title: *Lessons from Building Claude Code: Prompt Caching Is Everything*
- Author handle: `trq212` / Thariq
- URL: https://x.com/trq212/status/2024574133011673516
- Type: engineering article / social article
- Ingested: 2026-05-05
- Parent source guide: [[wiki/sources/Agent Engineering Source Guide]]

## Why ingest this

- It gives a crisp static-prefix / dynamic-suffix model for long-running agent requests.
- It explains prompt caching through transformer prefill, decode, and [[wiki/concepts/KV Cache]] reuse.
- It turns cache fragility into concrete engineering rules: do not mutate the prefix, reorder tools, inject timestamps, or switch models casually.
- It frames cache efficiency as a metric to monitor, not a feature to assume is working.
- It adds a cost dimension to [[wiki/topics/Context Management]] and [[wiki/topics/AI Harness]].
- It gives production harness patterns: stable plan-mode tools, deferred tool loading, and cache-safe compaction/forking.

## Distilled claims

- Agent requests often resend system instructions, tool definitions, project context, and prior conversation on every turn.
- The repeated foundation should be treated as a static prefix, while user messages, assistant turns, tool output, and observations form the dynamic suffix.
- Transformer inference first performs a prefill over the input prompt, then decodes output tokens one at a time.
- During prefill, attention computes key and value tensors that can be reused when the exact same token prefix appears again.
- Provider prompt caching stores reusable prefix state and serves later matching prefixes from cache.
- Cache reads are much cheaper than uncached input processing in the pricing model described by the source.
- Claude Code is presented as a production example of keeping a large static foundation warm across a long coding session.
- The source claims a 92% cache-hit rate and 81% cost reduction for the illustrated Claude Code session; treat those numbers as workload-specific unless corroborated elsewhere. ^[ambiguous]
- Thariq's article says Claude Code is built around prompt caching and treats low cache-hit rate as a production incident signal.
- Prompt caching works by prefix matching, so request ordering matters: static content first, dynamic content last.
- Claude Code's stable ordering is described as global system prompt and tools, then project-level `Claude.md`, then session context.
- Stable tools can represent mode changes, so entering plan mode does not require rewriting the cached prefix.
- Deferred tool loading preserves prefix stability by sending stable lightweight tool stubs and loading full schemas through tool search only when needed.
- Cache-safe compaction and forking should keep the parent prefix and append compaction instructions at the end.

## Candidate wiki destinations

### [[wiki/concepts/Prompt Caching]]

Primary destination. The stable concept is not "Claude Code is cheap"; it is the architectural discipline of making reusable prompt prefixes stable.

### [[wiki/concepts/KV Cache]]

Primary mechanism page. This source gives enough explanation to create a lightweight concept page connecting attention state to prompt caching.

### [[wiki/topics/Context Management]]

Prompt caching adds a new context-management dimension: context order and mutability affect cost and latency, not only answer quality.

### [[wiki/topics/AI Harness]]

Harnesses should protect cache stability by keeping tools, system prompts, model choice, and retrieved context stable across a session when possible.

### [[wiki/syntheses/Agent System Design Space]]

Cache discipline belongs in the broader design space as an economics and runtime-efficiency surface alongside memory, permissions, tools, and recovery.

## What should stay source-only

- Exact pricing numbers unless tied to a dated provider pricing page.
- The specific Claude Code billing example as a universal benchmark.
- Any claim that one provider's auto-caching semantics generalize to every LLM API.
- Screenshots and visual examples from the article.
- Operational severity language, unless the page is specifically about production SLO design.

## Open questions

- How do current provider APIs differ in cache breakpoint control, TTL, diagnostics, and pricing?
- What cache-hit threshold is enough to justify larger static prefixes in production agents?
- How should teams balance cache stability against the need to update tools or policies during a live session?

## Related

- [[wiki/sources/Agent Engineering Source Guide]]
- [[wiki/sources/Dive into Claude Code Source Guide]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/Agent System Design Space]]
