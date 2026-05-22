---
title: Memory in the Age of AI Agents Paper Source Guide
type: source
status: seed
category: sources
summary: Source guide for arXiv 2512.13564 on agent memory forms, functions, dynamics, resources, and future frontiers.
sources:
  - https://arxiv.org/abs/2512.13564
  - https://arxiv.org/pdf/2512.13564
created: 2026-05-21T14:52:00+08:00
updated: 2026-05-21T14:52:00+08:00
base_confidence: 0.83
lifecycle: draft
lifecycle_changed: 2026-05-21
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
aliases:
  - Memory in the Age of AI Agents
  - arXiv 2512.13564
  - Forms Functions and Dynamics
  - Agent Memory Forms Functions Dynamics
source_count: 2
tags:
  - paper
  - arxiv
  - agents
  - memory
  - survey
---
# Memory in the Age of AI Agents Paper Source Guide

> Source: Yuyang Hu et al., “Memory in the Age of AI Agents: A Survey — Forms, Functions and Dynamics,” arXiv:2512.13564v2.

## Capture Policy

This page preserves the primary arXiv paper as source-level material. It should be used for paper-grounded claims about the paper's forms–functions–dynamics taxonomy, while [[wiki/sources/Memory for Autonomous LLM Agents Source Guide]] and [[wiki/sources/AI Memory Survey Source Guide]] remain companion guides for adjacent surveys.

The PDF was retrieved locally from `https://arxiv.org/pdf/2512.13564`; local extraction reported 107 pages and SHA-256 `10de3c050903bfa1113c9a954380e2786f42d25a9ea24478bf6cc69fef2e2b42`.

## What It Covers

The paper surveys memory in foundation-model-based agents and argues that agent memory has become fragmented enough to require a new taxonomy. Its organizing triangle is:

- **Forms**: what carries memory.
- **Functions**: why agents need memory.
- **Dynamics**: how memory forms, changes, and gets retrieved over time.

The paper explicitly distinguishes agent memory from LLM memory, RAG, and context engineering, then compiles benchmarks, open-source frameworks, and future research frontiers.

## Preserved Content

### Source identity

- Title: “Memory in the Age of AI Agents: A Survey — Forms, Functions and Dynamics.”
- arXiv: `2512.13564v2`, submitted 15 Dec 2025, revised 13 Jan 2026.
- Categories: `cs.CL`, `cs.AI`.
- Project list: `https://github.com/Shichun-Liu/Agent-Memory-Paper-List`.
- Main contact emails are listed on the first page of the paper.

### Motivation

The paper starts from the claim that memory turns static LLMs into adaptive agents. Without memory, an LLM-based system can generate from the current context, but it cannot reliably accumulate user preferences, environment facts, plans, failures, or reusable skills across interactions.

The authors argue that earlier long-term/short-term memory taxonomies are too coarse for current agent systems. Recent work includes tool-distilling memories, test-time scaling memories, memory graphs, latent memories, RL-controlled memory operations, multimodal memories, and shared multi-agent memories. A taxonomy based only on duration hides these differences.

The survey's guiding questions are:

1. What is agent memory, and how does it relate to LLM memory, RAG, and context engineering?
2. What architectural or representational forms can memory take?
3. What roles or purposes does memory serve?
4. How does memory operate, adapt, and evolve over time?
5. What frontiers are most promising for future agent-memory research?

### Formal agent-memory framing

The paper formalizes LLM agents as policies operating over observations, tasks, memory-derived signals, and heterogeneous action spaces. Actions may include natural-language generation, tool calls, planning outputs, environment-control operations, or communication with other agents.

Agent memory is modeled as a persistent state coupled to the agent loop. Three operations recur:

- **Memory formation** extracts future-useful candidates from artifacts such as tool outputs, reasoning traces, plans, self-evaluations, and environment feedback.
- **Memory evolution** integrates candidates into the existing memory base through consolidation, updating, forgetting, conflict resolution, and restructuring.
- **Memory retrieval** constructs a context-dependent memory signal for the policy at action time.

The paper emphasizes that short-term and long-term memory effects do not necessarily correspond to separate modules. They can emerge from different invocation patterns of formation, evolution, and retrieval inside or across tasks.

### Distinctions from adjacent concepts

#### Agent memory vs. LLM memory

The paper argues that agent memory largely subsumes much of what earlier work called LLM memory. Systems such as MemoryBank and MemGPT were often described as LLM memory, but under a modern agent framing they are better understood as early agent-memory systems because they track preferences, dialogue state, and cross-turn experience.

The exception is genuinely LLM-internal memory: KV cache reuse, architectural recurrence, model weights, or hidden-state mechanisms that operate inside the model rather than as an agent-level persistent state.

#### Agent memory vs. RAG

Agent memory and RAG share engineering components such as vector indexes, semantic search, knowledge graphs, and context expansion. Their historical goals differ:

- Classical RAG grounds generation in static or externally curated knowledge sources.
- Agent memory maintains a persistent, evolving record of an agent's own interactions, actions, environment feedback, and experience.

As agentic RAG becomes more dynamic, the boundary blurs, but the paper treats agent memory as defined by ongoing self-evolving cognitive state rather than one-shot retrieval from a static corpus.

#### Agent memory vs. context engineering

Context engineering optimizes what enters the context window. It treats context as a constrained computational resource. Agent memory overlaps with context engineering when memories are selected, compressed, and injected into context, but the two are not hierarchical synonyms.

The paper's distinction is operational: context engineering manages transient runtime payloads; agent memory maintains persistent, self-evolving state that can outlive the current context window.

### Forms: what carries memory

The paper's first major taxonomy asks what representational substrate carries memory.

#### Token-level memory

Token-level memory stores information as explicit, discrete, externally inspectable units. “Token” is broad here: it can include text snippets, visual tokens, audio frames, structured records, or any discrete element that can be written, retrieved, reorganized, and revised outside model parameters.

Its advantages are transparency, editability, debuggability, and compatibility with retrieval, routing, conflict handling, and coordination. It is the most common current form.

The paper further distinguishes token-level organization:

- **Flat memory (1D)**: lists, logs, snippets, summaries, vector chunks, dialogue records.
- **Planar memory (2D)**: graph, table, profile, or structured memory where relationships matter.
- **Hierarchical memory (3D)**: multi-level organization such as episodic entries, summaries, abstractions, and skill libraries.

#### Parametric memory

Parametric memory stores information in model parameters. Information is accessed implicitly during forward computation rather than retrieved as an external object.

The paper separates:

- **Internal parametric memory**: knowledge stored in the base model or fine-tuned weights.
- **External parametric memory**: adapters, side networks, memory modules, or learned components coupled to the model.

Parametric memory integrates smoothly with inference, but is less inspectable, harder to update selectively, harder to delete from, and harder to govern than explicit memory.

#### Latent memory

Latent memory lives in hidden states, continuous representations, or evolving latent structures. It sits between explicit token-level data and fixed model weights.

The paper frames latent memory as high-density and efficient but less interpretable. Its useful scenarios include multimodal agents, on-device or edge deployments, cloud-serving environments, and privacy-sensitive domains where low readability can be a feature as well as a debugging liability.

#### Adaptation across forms

The forms are not mutually exclusive. An agent can use explicit records for auditability, latent memories for compact inference, and parametric adaptation for model-native behaviors. The key design question is which layer should carry which kind of memory under constraints of update speed, trust, latency, privacy, and interpretability.

### Functions: why agents need memory

The paper's second taxonomy asks what role memory serves in agent behavior.

#### Factual memory

Factual memory is the agent's declarative knowledge base. It answers: “What does the agent know?”

It stores user preferences, user goals, environment facts, dialogue state, object locations, routines, and verifiable constraints. The paper separates user factual memory from environment factual memory. User factual memory supports personalization and coherence; environment factual memory supports situated action and world-state tracking.

Examples include systems that transform dialogue into user profiles, preserve goal constraints, or convert multimodal observations into text-addressable facts.

#### Experiential memory

Experiential memory is the agent's procedural and strategic knowledge. It answers: “How does the agent improve?”

It abstracts from task trajectories, successes, failures, plans, corrective signals, and reusable strategies. The paper breaks this area into:

- **Case-based memory**: storing solutions or trajectories.
- **Strategy-based memory**: extracting planning principles and failure reflections.
- **Skill-based memory**: preserving workflows, functions, code, or reusable procedures.
- **Hybrid memory**: combining cases, strategies, and skills.

Representative examples include ExpeL-style trajectory comparison, Voyager-style skill libraries, and systems that distill workflows or codebase-level experience.

#### Working memory

Working memory is the dynamically controlled scratchpad for active task context. It answers: “What is the agent thinking about now?”

The paper distinguishes single-turn working memory from multi-turn working memory. It includes input condensation, state consolidation, hierarchical folding, cognitive planning, and session-level workspace management.

Working memory is where retrieved factual and experiential memories become operationally useful. It is not equivalent to persistent memory, but it is the active site where memory affects reasoning and action.

#### Cognitive loop among functions

The paper presents factual, experiential, and working memory as an interconnected cognitive loop:

1. Interaction outcomes are encoded into factual or experiential stores.
2. Working memory processes immediate task context.
3. Retrieval fills working memory with relevant facts, strategies, and skills.
4. New outcomes update long-term stores.

This framing is close to [[wiki/concepts/Agent Memory Write-Manage-Read Loop]], but uses a different lens: factual/experiential/working function rather than write/manage/read operation.

### Dynamics: how memory operates and evolves

The paper's third taxonomy asks how memory changes over time.

#### Memory formation

Memory formation transforms raw experience into information-dense memory units. It is selective rather than archival: the point is not to store every token, but to extract facts, strategies, constraints, abstractions, and latent representations with future utility.

The paper names five formation modes:

- **Semantic summarization**: compress interactions into natural-language memory.
- **Knowledge distillation**: extract reusable knowledge from trajectories or data.
- **Structured construction**: build graphs, profiles, tables, or schemas.
- **Latent representation**: encode memory into compact continuous representations.
- **Parametric internalization**: absorb memory into weights or learned modules.

#### Memory evolution

Memory evolution integrates new memories into the existing memory base. It handles:

- **Consolidation**: merge related entries and abstract repeated patterns.
- **Updating**: revise outdated or contradicted entries.
- **Forgetting**: remove low-utility, stale, sensitive, or misleading memories.

The paper treats evolution as the source of self-evolving memory. A memory system that only appends will eventually become noisy, redundant, stale, and expensive.

#### Memory retrieval

Memory retrieval determines when, where, what, and how to retrieve. It includes retrieval timing, query construction, retrieval strategy, and post-retrieval processing.

Important design choices include whether to retrieve only at task initialization, intermittently, continuously, or only when a trigger fires. Query construction may use the user input, task status, generated subgoals, or a memory-aware reformulation. Post-retrieval processing may rerank, summarize, fuse, filter, or restructure results before they enter working memory.

### Resources and frameworks

The paper compiles memory-oriented benchmarks and broader long-horizon benchmarks. Named examples include MemBench, LoCoMo, WebChoreArena, MT-Mind2Web, PersonaMem, PerLTQA, PrefEval, LOCCO, StoryBench, LongBench, LongBench v2, RULER, BALILong, and multimodal needle-style tests.

It also surveys open-source frameworks and backends such as MemGPT, Mem0, Memobase, MemoryOS, MemOS, Zep, LangMem, SuperMemory, Cognee, Memary, Pinecone, Chroma, Weaviate, Second Me, MemU, MemEngine, Memori, ReMe, AgentMemory, and MineContext.

The paper notes that many frameworks support factual memory through vector or structured stores, while a growing subset represents experiential traces, multimodal memory, graph memory, profile memory, or modular memory spaces. Evaluation coverage remains uneven.

### Positions and frontiers

#### From memory retrieval to memory generation

The paper says the field is shifting from retrieving stored entries toward generating better memory representations. Retrieval assumes the memory base is already well formed. Memory generation actively synthesizes, compresses, reorganizes, and tailors memory for future utility.

This frontier matters because raw memories are often noisy, redundant, or misaligned with the current task. Effective memory use may require abstraction and recomposition, not just nearest-neighbor lookup.

#### Automated memory management

Many existing memory systems rely on hand-crafted rules, thresholds, prompts, or expert-designed update policies. These are interpretable and easy to deploy, but inflexible in dynamic environments.

The paper expects more memory systems to automate clustering, updating, retrieval, and evolution. The central unsolved question is how to keep automated memory management reliable, inspectable, and transferable across tasks.

#### Reinforcement learning meets agent memory

The paper frames RL as a force moving memory from pipeline heuristics toward model-native or policy-governed memory management. RL can learn when to store, retrieve, update, summarize, or forget.

The paper presents this as a plausible dominant direction but not as solved. Long-horizon credit assignment, safety-critical forgetting, distribution shift, and interpretability remain open.

#### Multimodal memory

As multimodal agents mature, text-only memory becomes insufficient. Multimodal memory must preserve visual, audio, video, sensor, and embodied information across long horizons.

The paper says images and video have received more attention than audio and other modalities. A future memory system may need both modality-specific representations and unified cross-modal memory operations.

#### Shared memory in multi-agent systems

Multi-agent systems are moving from isolated local memories plus message passing toward shared cognitive substrates. Shared memory can reduce redundancy and support common ground, role handoff, planning, and consensus.

It also introduces clutter, write contention, conflicting memories, and access-control problems. Future shared memory should become agent-aware: read/write privileges and retrieval behavior should depend on role, expertise, trust, and task responsibility.

#### Memory for world models

The paper connects memory to world-model construction. Persistent memory can help agents accumulate stable representations of environment dynamics, object relations, causal patterns, and task state, rather than treating every episode as isolated.

#### Trustworthy memory

Trustworthiness extends RAG concerns into a harder agent setting. Agent memory stores user-specific, persistent, and potentially sensitive material such as preferences, behavioral traces, private facts, and past interactions.

Key concerns include:

- Privacy leakage through indirect prompt attacks.
- Over-retention and memorization.
- Access control.
- Verifiable forgetting.
- Auditable updates.
- Explainability of which memories were retrieved and how they influenced behavior.

This section is directly relevant to [[wiki/concepts/Governed Action]] and [[wiki/topics/AI Memory]].

#### Human-cognitive connections

The paper points back to human cognition as a source of analogies and design hints, but does not reduce agent memory to human memory. The useful connection is architectural: formation, consolidation, retrieval, forgetting, working memory, and shared memory have cognitive analogues that can inspire system design.

### Conclusion

The conclusion restates the three-part contribution:

- **Forms**: token-level, parametric, and latent memory expose different trade-offs in representation, adaptability, and integration with policy.
- **Functions**: factual, experiential, and working memory give a finer-grained alternative to long-term/short-term memory.
- **Dynamics**: formation, evolution, and retrieval explain how memory systems operate over time.

The paper's larger claim is that memory should be treated as a first-class primitive for future agentic intelligence, not as a minor retrieval add-on.

## Integration Decisions

This paper should be routed into the existing AI memory cluster rather than creating a new broad topic page. The wiki already has [[wiki/topics/AI Memory]], [[wiki/concepts/Agent Memory Write-Manage-Read Loop]], [[wiki/concepts/Agent Memory Mechanism Families]], and [[wiki/concepts/Agent Memory Evaluation Stack]].

The paper's most reusable addition is a second axis set for the agent-memory topic:

- Forms: token-level / parametric / latent.
- Functions: factual / experiential / working.
- Dynamics: formation / evolution / retrieval.

These should stay source-level for now until they are compared against the existing [[wiki/sources/Memory for Autonomous LLM Agents Source Guide]] and [[wiki/sources/AI Memory Survey Source Guide]]. If promoted later, they should likely extend [[wiki/concepts/Agent Memory Mechanism Families]] rather than create several near-duplicate concept pages.

Claims about specific systems, benchmark lists, and framework coverage should remain source-level because the paper is a large survey and the ecosystem changes quickly.

## Open Questions

- Should the wiki's existing agent-memory concepts be reorganized around forms/functions/dynamics, or should this taxonomy remain one survey's source-level lens? ^[inferred]
- Can “memory generation” become a stable concept distinct from retrieval, consolidation, and summarization? ^[inferred]
- How should shared multi-agent memory be evaluated when correctness depends on coordination quality, role permission, and write conflict handling? ^[inferred]
- Which parts of memory management are safe to internalize through RL, and which must remain inspectable external controls? ^[inferred]

## Related

- [[wiki/topics/AI Memory]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Agent Memory Write-Manage-Read Loop]]
- [[wiki/concepts/Agent Memory Mechanism Families]]
- [[wiki/concepts/Agent Memory Evaluation Stack]]
- [[wiki/concepts/AI Memory 4W Taxonomy]]
- [[wiki/concepts/Governed Action]]
- [[wiki/sources/Memory for Autonomous LLM Agents Source Guide]]
- [[wiki/sources/AI Memory Survey Source Guide]]
- [[wiki/sources/Agent Systems Papers Source Guide]]
