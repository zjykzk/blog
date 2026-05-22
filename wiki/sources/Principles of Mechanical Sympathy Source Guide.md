---
title: Principles of Mechanical Sympathy Source Guide
type: source
status: seed
category: sources
tags:
  - article
  - software-engineering
  - systems
  - architecture
  - inference
sources:
  - https://martinfowler.com/articles/mechanical-sympathy-principles.html
  - conversation:2026-05-17
created: 2026-05-17T23:35:07+08:00
updated: 2026-05-17T23:35:07+08:00
summary: Source guide for Caer Sanders' Martin Fowler article on mechanical sympathy: predictable memory access, cache lines, single writers, batching, and observability.
provenance:
  extracted: 0.91
  inferred: 0.09
  ambiguous: 0.0
base_confidence: 0.60
lifecycle: draft
lifecycle_changed: 2026-05-17
aliases:
  - Mechanical Sympathy Principles
  - Martin Fowler mechanical sympathy principles
  - Caer Sanders mechanical sympathy
---

# Principles of Mechanical Sympathy Source Guide

> Source: Caer Sanders, "Principles of Mechanical Sympathy", Martin Fowler, https://martinfowler.com/articles/mechanical-sympathy-principles.html

## Capture Policy

This page preserves the source-level content of the article rather than promoting mechanical sympathy directly into a broad concept page. Its claims should stay tied to the article until they are cross-checked with other performance, concurrency, and hardware-aware systems sources.

## What It Covers

The article explains mechanical sympathy as software design that respects the hardware it runs on. The practical point is not micro-optimization by default; it is choosing data structures, ownership models, and batching strategies that fit CPU memory hierarchy, cache behavior, and runtime contention.

For this wiki, the source belongs in the CS and software architecture layer because it connects low-level performance behavior to higher-level design choices already tracked in [[wiki/topics/High Concurrency]], [[wiki/topics/LLM Inference Systems]], [[wiki/topics/Go Memory Model]], and [[wiki/syntheses/信息流与状态流转设计原则]].

## Preserved Content

### Mechanical Sympathy as a Design Posture

The source opens from a mismatch: hardware has become extremely fast, but ordinary software can remain slow because it ignores how hardware actually behaves. Mechanical sympathy names the practice of making software fit the machine rather than assuming all memory access, synchronization, and batching strategies are equivalent.

Caer Sanders attributes the phrase's software popularization to Martin Thompson and grounds the article in Thompson's work around high-performance systems such as LMAX. The article's everyday principles are:

- predictable memory access
- cache-line awareness
- single-writer ownership
- natural batching

The article explicitly applies these ideas beyond low-level libraries. It says the same principles can matter in AI inference servers, data platforms, ETL pipelines, IO-heavy services, and CQRS-style architectures.

### Not-So-Random Memory Access

The first principle starts with CPU memory hierarchy:

- CPU cores have very fast but tiny registers and buffers.
- Each core usually has its own L1 and L2 caches.
- Multiple cores share a larger but slower L3 cache.
- Main memory is much slower than the cache hierarchy.

The article's operational model is that CPUs make locality bets. Recently accessed memory is likely to be accessed again; nearby memory is likely to be accessed soon; and access patterns are likely to continue. Sequential access therefore lets the CPU prefetch and reuse data more effectively, while random page-crossing access defeats those bets.

The practical design rule is to prefer algorithms and data structures that enable predictable sequential access. The source's ETL example says a pipeline may be faster scanning a source sequentially and filtering out irrelevant keys than repeatedly querying one key at a time. That is a hardware-aware inversion of a common "only fetch what I need" intuition: fewer logical records is not automatically less physical work.

### Cache Lines and False Sharing

The second principle is cache-line awareness. CPU caches move memory in contiguous cache-line chunks, often 64 bytes. This creates a concurrency trap: two variables can be logically independent but physically adjacent inside the same cache line.

When two CPU cores write different variables in the same cache line, the cores still have to coordinate ownership of that cache line. The source calls this false sharing: the software thinks the variables are separate, while the hardware treats the surrounding memory line as the coherence unit.

The article emphasizes three implications:

- False sharing appears around writes, not ordinary reads, because written cache lines require synchronization between core-local copies.
- Atomic variables are common victims because they are designed to be safely modified across threads, so they often sit exactly where high write contention happens.
- Padding can isolate hot writable variables so a cache line effectively contains only one frequently written variable.

The source keeps this as a late-stage performance concern. It is relevant when chasing the final performance limit in a multithreaded application, especially where a data structure is written by multiple threads and latency grows as threads are added.

### The Single Writer Principle

The source's most reusable design principle is single-writer ownership. If an application writes to a data item or resource, all writes should be made by one thread. The point is not merely speed; it also reduces race conditions, context switching, and mutex overhead.

The article's worked example is an HTTP embedding service. In the naive design, multiple request threads call into an AI model runtime protected by a mutex. Because many model runtimes can execute only one inference call at a time, concurrent requests queue behind the lock and can suffer head-of-line blocking.

The single-writer refactor wraps model access in a dedicated actor thread:

- request threads submit asynchronous messages to the actor;
- the actor owns calls into the model runtime;
- the actor can collect independent requests into a batch inference call;
- results are returned asynchronously to the original request paths.

This matters for [[wiki/topics/LLM Inference Systems]] because model serving is often a scheduling, ownership, batching, and memory-management problem, not just a neural-network problem. ^[inferred]

The article's design rule is to avoid protecting writable resources with a mutex when ownership can be restructured. A dedicated actor owns writes, while other threads communicate by message.

### Natural Batching

Natural batching builds on the single writer. Once a single actor owns a resource, it can form batches from its queue.

The source contrasts three approaches:

- waiting for a predetermined batch size can block indefinitely under low traffic;
- fixed-interval batching bounds waiting time but adds artificial delay;
- natural batching starts as soon as work is available and closes the batch when the queue is empty or the maximum batch size is reached.

The article uses Martin Thompson's batching example to show why this can reduce latency. With a fixed batch processing time, timeout-based batching pays both processing time and waiting time even when all requests are already present. Natural batching can send immediately when the queue already contains enough work, while still capturing bursts that arrive naturally.

The reusable rule is greedy queue draining: when a single writer handles batches, begin when data is available, then continue until either the queue is empty or the batch is full.

### Scaling the Principles

The source explicitly scales the principles from local code to whole systems:

- predictable access applies to data lakes and ETL paths, not only arrays;
- single-writer ownership can improve IO-intensive applications;
- single-writer thinking can support CQRS-style write ownership;
- batching applies to inference, reads, writes, and other queued operations.

This makes the article a useful bridge between hardware-level performance and architecture-level constraints. It supports the broader wiki thread that software design has a runtime dimension: state, data flow, control flow, concurrency, consistency, and failure behavior are part of design, not after-the-fact tuning. ^[inferred]

### Observability Before Optimization

The closing warning is that optimization should follow measurement. Before applying mechanical-sympathy principles, the team should define the relevant SLIs, SLOs, and SLAs so it knows where performance matters and when to stop.

This connects the source to [[wiki/syntheses/Quality Engineering Three Generators]]: optimization should be tied to a clear promise, visible deviation, and correction loop. Mechanical sympathy without observability can become premature optimization; observability without mechanical sympathy can show a performance problem without giving a structural way to fix it. ^[inferred]

## Integration Decisions

Mechanical sympathy should remain source-level for now. The wiki already has several connected destinations, but not yet enough cross-source grounding for a stable concept page.

The most immediate integration points are:

- [[wiki/topics/High Concurrency]]: add hardware-aware contention, batching, and resource ownership as performance dimensions.
- [[wiki/topics/LLM Inference Systems]]: connect actor ownership and natural batching to inference-serving pressure.
- [[wiki/topics/Go Memory Model]]: keep correctness-ordering and hardware/cache sympathy related but distinct.
- [[wiki/syntheses/信息流与状态流转设计原则]]: treat single-writer ownership as one way to keep mutation paths explicit.
- [[wiki/syntheses/Quality Engineering Three Generators]]: keep observability as the constraint that makes performance work accountable.

The source's detailed claims about cache lines, false sharing, and actor batching should not be generalized to all systems without profiling. They are strong design lenses, not universal mandates.

## Open Questions

- Which parts of the article should later become a stable Mechanical Sympathy concept page after more sources are captured? ^[inferred]
- How should natural batching be compared with continuous batching in modern LLM serving systems? ^[inferred]
- When does single-writer ownership simplify correctness, and when does it create an overloaded actor bottleneck? ^[inferred]

## Related

- [[wiki/topics/High Concurrency]]
- [[wiki/topics/LLM Inference Systems]]
- [[wiki/topics/Go Memory Model]]
- [[wiki/syntheses/信息流与状态流转设计原则]]
- [[wiki/syntheses/Quality Engineering Three Generators]]
- [[wiki/maps/CS Map]]
