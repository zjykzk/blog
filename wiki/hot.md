---
title: Hot Cache
category: meta
summary: Recent wiki activity added an understanding-as-cloud model linking concepts, learning, mental models, similarity, and abstraction.
tags: []
sources: []
created: 2026-05-04
base_confidence: 0.30
lifecycle: draft
lifecycle_changed: 2026-05-05
updated: 2026-05-06T19:18:40+08:00
---

## Recent Activity

- Ingested an inline essay on “理解”: added [[wiki/concepts/Understanding]] and connected it to [[wiki/concepts/Concept]], [[wiki/concepts/Knowledge as Network]], [[wiki/topics/Learning Methodology]], and [[wiki/topics/Mental Models]].
- Ingested Aleksa Gordic's vLLM article: added [[wiki/topics/LLM Inference Systems]], [[wiki/concepts/Paged Attention]], [[wiki/concepts/Continuous Batching]], [[wiki/concepts/Prefill Decode Split]], [[wiki/concepts/Speculative Decoding]], and [[wiki/concepts/LLM Inference Benchmarking]].
- Ingested Thariq Shihipar's "Seeing like an Agent" article: added [[wiki/concepts/Agent Action Space]] and [[wiki/sources/Seeing Like an Agent Source Guide]], connecting tool design to elicitation, task coordination, search, skills, and subagents.

## Active Threads

- Software methodology is converging around the handoff from business modeling to analysis, DDD, and executable design.
- Frontend knowledge is forming around React as a coordination model for declarative rendering, component boundaries, and state.
- AI / Agent systems are being organized around harness, context management, tool design, memory, permissions, and reusable operational knowledge.
- Prompt and context design now includes an explicit runtime-economics layer: stable prefixes can be reused, while prefix mutation creates cold-cache sessions.
- Tool availability can be made cache-stable by exposing stable stubs and deferring full schema loading until search/select time.
- Agent harness architecture now has an explicit verification thread: tests, visual checks, and evaluator loops are part of runtime behavior, not just final QA.
- AI-assisted learning is strongest when it maps expert mental models, disagreements, and diagnostic questions before trying to accelerate content consumption.
- Wealth creation is now represented as a system model: own scalable assets, build specific knowledge, accept accountability, use permissionless leverage, and improve judgment because leverage amplifies decisions.
- Harness engineering is now represented as a feedback discipline: repeated agent mistakes should become durable rules, hooks, checks, done conditions, tool-surface changes, or workflow splits.
- Long-context quality now has a positional robustness thread: the right information must be present and placed where the model can actually use it.
- AI memory is now split from context: memory persists and gets retrieved into the active window; context is the bounded runtime workspace for the current inference step.
- AI coding workflow now has an explicit collaboration-scaffolding layer: onboarding context, design alignment, team standards, anchored decisions, and feedback loops.
- Knowledge priming is now represented as context infrastructure: compact project identity should be versioned, reviewed, and reused by skills instead of pasted ad hoc.
- Design-first collaboration is now represented as a staged AI pairing workflow: capabilities, components, interactions, contracts, then implementation.
- Context anchoring is now represented as feature-level external memory: decisions, reasons, rejected alternatives, open questions, and state should survive outside the chat transcript.
- Encoding team standards is now represented as executable governance: senior judgment about generation, refactoring, security, and review can live as versioned shared instructions.
- Feedback flywheel is now represented as the maintenance loop for AI collaboration: real review, regeneration, acceptance, and rework signals should update context, standards, workflows, checks, and guardrails.
- Agent skills are now represented as folder-shaped capability bundles: references, scripts, assets, memory, configuration, and on-demand hooks can be disclosed only when the workflow needs them.
- Agent action space is now represented as an empirical harness design problem: add, remove, or reshape tools based on whether the model can actually use them.
- LLM inference systems are now represented as a stack: scheduler, KV-cache allocator, model executor, advanced decoding features, distributed serving layer, and benchmark loop.
- Prefill/decode separation is now a key inference-design thread: compute-heavy prompt processing and latency-sensitive decoding need different scheduling and scaling choices.
- Understanding is now represented as a cloud-shaped cognitive structure: horizontal similarity gives breadth, vertical abstraction gives depth, and teaching/rebuilding tests whether the cloud can move.

## Key Takeaways

- Structural wiki health is currently clean across frontmatter, summaries, links, index coverage, tag cohesion, and synthesis-gap checks.
- Long-horizon agent performance should be judged by decision-relevant information preserved under finite context, not by how much history is visible.
- Tool minimality, hierarchical memory, and self-evolution can be read as density-preserving harness mechanisms.
- Prompt caching turns context order, tool schema stability, and model continuity into concrete harness responsibilities.
- Cache-hit rate is a production health signal for long-running agents, because low hit rates can reveal accidental prompt or tool-prefix churn.
- Harness quality should be judged by how it manages context, tools, state, permissions, errors, and verification around the same underlying model.
- AI tutor workflows should preserve the learner's responsibility to answer, fail, and repair understanding; otherwise the tool becomes a summary machine rather than a learning loop.
- Permissionless leverage connects the reading and management clusters: code and media change the replication structure of work, but they amplify judgment rather than replacing it.
- Context rot reframes long-context work as an active harness problem: compaction, offloading, progressive disclosure, and full reset from a handoff file are runtime design choices.
- More retrieved context is not automatically better; reader performance can saturate before retriever recall, so reranking and truncation can be accuracy tools, not just latency optimizations.
- Memory architecture should be compared by lifecycle, content type, storage representation, and modality before debating implementation details.
- AI coding productivity should be measured by acceptance, iteration cycles, rework, and review burden, not by time to first output or generated lines.
- Reusable AI skills can be context architecture, not just command wrappers: they can collect, compress, persist, and reintroduce project context before action.
- Contracts are the hinge between AI design conversation and testing: once interfaces are agreed, tests can be generated before implementation.
- Durable feature documents are a practical reset mechanism: they let teams close long AI chats and restart from a compact, decision-rich artifact.
- AI standards should move from personal prompting skill into repository infrastructure when output quality varies by who is asking.
- Failed AI interactions are useful evidence only if they change a durable artifact; otherwise the same collaboration failure returns as a new prompt problem.
- Inference benchmarking should be read through SLO-aware goodput, not just raw tokens per second, because latency and throughput can optimize against each other.
- A concept can be known as a label without being understood as a movable cloud; durable learning should change the cloud's examples, abstractions, and links.

## Flagged Contradictions
