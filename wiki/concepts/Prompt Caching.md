---
title: Prompt Caching
type: concept
status: seed
summary: Prompt caching reuses stable prompt prefixes so repeated agent turns avoid recomputing the same system, tool, and context tokens.
category: concepts
sources:
  - https://x.com/_avichawla/article/2044670188998803855
  - https://x.com/trq212/status/2024574133011673516
created: 2026-05-05T00:00:00+08:00
updated: 2026-05-05T13:58:10+08:00
base_confidence: 0.61
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.84
  inferred: 0.16
  ambiguous: 0.0
aliases:
  - prompt cache
  - prompt prefix caching
tags:
  - agents
  - context
  - caching
---
# Prompt Caching

Prompt caching is an inference optimization and agent architecture constraint: put stable prompt material at the beginning of the request so later turns can reuse the already-computed state for that prefix.

## Core idea

Long-running agents resend the same foundation on many turns: system instructions, tool definitions, project context, behavioral rules, and reference documents.

Prompt caching treats that repeated foundation as a stable prefix and the conversation as a growing dynamic suffix:

- static prefix: system prompt, tool definitions, project context, reference documents
- dynamic suffix: user turns, assistant turns, tool results, terminal observations

When later requests share the same token prefix, the inference service can reuse cached [[wiki/concepts/KV Cache]] state rather than rerunning the full prefill computation for those tokens.

## Why agents care

For short chats, caching is mostly a pricing optimization. For agent systems, it becomes a harness design rule because the expensive repeated prefix can dominate total input-token cost across long tasks.

The source uses Claude Code as a case study: a long coding session can pay once for a large static foundation, then repeatedly read that foundation from cache while only the dynamic tail keeps changing.

This makes prompt caching part of [[wiki/topics/Context Management]], not just billing plumbing. The context has to be ordered so reusable material stays stable and early, while volatile state accumulates later.

## Cache fragility

Prompt caches are hash-sensitive. The cache key depends on the exact token sequence from the beginning of the request, so semantically equivalent reorderings can miss the cache.

The source lists three practical cache breakers:

- injecting timestamps into the static prompt
- serializing tool schemas in unstable order
- changing tool definitions during a session
- switching models inside an already-warm session

That makes cache stability a concrete [[wiki/topics/AI Harness]] responsibility. A harness that mutates its prefix to store state can silently turn every future turn into a cold-cache request.

## Design rules

The article's operational rules can be distilled into a stable agent design checklist:

- Keep system instructions and behavioral rules first.
- Load tool definitions upfront and do not change them mid-session.
- Put retrieved documents and project context before conversation history when they should remain stable.
- Let user messages, assistant turns, tool output, and observations grow at the bottom.
- Append reminders or state changes as new messages instead of editing the static prefix.
- Avoid model switching inside one session because caches are model-specific.
- Represent mode switches as stable tools or messages rather than by rewriting the system prompt.
- Defer-load large or rarely used tool schemas behind stable lightweight stubs instead of adding and removing tools mid-conversation.

These rules are not only cost optimizations; they also make the prompt boundary explicit, which helps preserve [[wiki/concepts/Context Information Density]]. ^[inferred]

## Cache-safe compaction

When a session nears the context limit, the source recommends cache-safe forking: keep the existing system prompt, tools, and conversation prefix intact, then append the compaction instruction as a new message.

The important point is that compaction should not rewrite the reusable prefix. It should introduce new work at the end of the sequence so the cache can still match the already-stable part.

Thariq's Claude Code article adds that forking and compaction should reuse the parent prefix wherever possible: keep the same system prompt, tool definitions, project context, and session context, then append the compaction instruction at the end.

## Metrics

The source names three response fields to monitor:

- `cache_creation_input_tokens`: tokens written into cache
- `cache_read_input_tokens`: tokens served from cache
- `input_tokens`: tokens processed without a cache read

It defines cache efficiency as `cache_read_input_tokens / (cache_read_input_tokens + cache_creation_input_tokens)`.

The Claude Code article treats cache hit rate as production health, not just local optimization: a low hit rate can mean the harness is silently rewriting supposedly stable prefix material.

## Open Questions

- How portable are the quoted Claude Code cache-hit and cost-reduction numbers across different workloads, models, and provider cache policies? ^[ambiguous]
- When should an agent deliberately break cache stability to update safety, policy, or tool definitions mid-session? ^[inferred]

## Sources

- [[wiki/sources/Prompt Caching Claude Code Case Study Source Guide]]

## Related

- [[wiki/concepts/KV Cache]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/Agent System Design Space]]
