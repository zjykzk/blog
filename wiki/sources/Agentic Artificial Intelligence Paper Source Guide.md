---
title: Agentic Artificial Intelligence Paper Source Guide
type: source
status: seed
summary: Source guide for arXiv 2601.12560v1 on agentic AI architectures, taxonomy, control loops, multi-agent orchestration, evaluation, safety, and open challenges.
category: sources
sources:
  - https://arxiv.org/abs/2601.12560v1
created: 2026-05-13T10:37:07+08:00
updated: 2026-05-13T10:37:07+08:00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: "2026-05-13"
provenance:
  extracted: 0.92
  inferred: 0.07
  ambiguous: 0.01
aliases:
  - Agentic Artificial Intelligence AI paper
  - arXiv 2601.12560v1 source guide
tags:
  - paper
  - arxiv
  - agents
  - architecture
---
# Agentic Artificial Intelligence Paper Source Guide

## Source Identity

- Source: https://arxiv.org/abs/2601.12560v1
- User supplied URL: `https://arxiv.org/html/2601.12560v1`
- Title: Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents
- Authors: Arunkumar V, Gangadharan G.R., Rajkumar Buyya
- Submitted: 18 Jan 2026
- arXiv version: 2601.12560v1
- Subjects: Artificial Intelligence (cs.AI); Multiagent Systems (cs.MA)
- Comments: 28 pages, 4 figures, 5 tables
- Extraction representation: arXiv experimental HTML was used for readable paper text.
- Manifest hash representation: PDF bytes from `https://arxiv.org/pdf/2601.12560v1` were hashed.
- PDF bytes observed through browser fetch: 1,681,154 bytes; Last-Modified `Wed, 21 Jan 2026 02:15:23 GMT`; SHA-256 `afd746da626d5615691aeeb4248675269b00074cbdc58e2fcbc815d803fe0056`.

## What This Paper Is About

The paper is an architecture- and engineering-focused survey of Agentic AI. Its central claim is that AI is shifting from passive text generation toward systems that perceive, reason, plan, act, use tools, maintain memory, and receive feedback from environments.

The paper proposes a unified taxonomy with six dimensions: Core Components, Cognitive Architecture, Learning, Multi Agent Systems, Environments and Domains, and Evaluation and Safety.

## Contributions Claimed by the Paper

The paper positions itself against prior surveys that focus on broad LLM-agent overviews, application catalogs, or methodology lists. Its claimed contribution is an architecture-first view:

- a POMDP-based formal control loop for LLM agents
- a six-dimensional taxonomy of agentic AI systems
- an engineering view of memory backends, retention policies, agent-computer interfaces, code-as-action, MCP, typed state, and controllable orchestration
- a multi-agent comparison across chain, star, mesh, hierarchy, and workflow-graph patterns
- an evaluation and safety lens using cost, latency, accuracy, security, and stability

## Formal Agentic Control Loop

The paper models an LLM-based agent as a tuple `A = <S, O, M, T, π>`:

- `S`: environment state space
- `O`: observation space
- `M`: internal memory space
- `T`: action or tool space
- `π`: policy

At each discrete step, the agent receives partial observations through a perception function, updates memory from observation, prior reasoning trace, and prior execution feedback, generates a reasoning trace or plan, chooses an action from the tool space, and receives environment feedback.

This is the source basis for [[wiki/concepts/Agentic Control Loop]].

## Architecture Taxonomy

The paper's taxonomy organizes the field into six dimensions:

1. **Core Components**: perception, memory, action/tools, profiling.
2. **Cognitive Architecture**: planning, reflection, hierarchical reasoning, tree search, self-correction.
3. **Learning**: in-context methods, fine-tuning, RLHF/RLAIF, agent-specific learning.
4. **Multi Agent Systems**: adversarial debate, role playing, SOP-based workflows, chains, stars, meshes, swarms.
5. **Environments and Domains**: web, OS, software engineering, robotics, games, healthcare, science, finance.
6. **Evaluation and Safety**: cost, latency, accuracy, security, stability, prompt injection, benchmarks.

This is the source basis for [[wiki/concepts/Agentic AI Architecture Taxonomy]].

## Core Components and Notable Source-Level Details

The paper treats modern agent architecture as a pipeline from perception to action through a central decision process. It writes core components as `A = <Φ, M, T, P>`: perception, memory, tools/actions, and profiling.

Important source-level details that should mostly stay in this guide:

- Perception examples include WebVoyager, AppAgent, SeeAct, Magma, AudioGPT, and 3D-LLM.
- Memory examples compare natural-language streams, hierarchical clusters, SQL tables, memory graphs, and virtual context / paging approaches.
- Action and tool evolution includes fixed APIs, code-as-action, direct UI / computer-use actions, and standardized connector layers such as MCP.
- Profiling refers to system prompts, dynamic roles, and identity/persona shaping.

These examples are useful as evidence but should not all become global pages unless future sources make them central.

## Multi-Agent and Workflow Graphs

The paper distinguishes multi-agent coordination patterns:

- **Chain / waterfall**: fixed sequence of agents and handoffs, as in MetaGPT or ChatDev-style workflows.
- **Star / hub-and-spoke**: controller coordinates specialized workers, common in AutoGen-like patterns.
- **Mesh / swarm**: decentralized interaction, debate, simulation, or social dynamics.
- **Hierarchical verification**: supervisor/worker or verifier patterns for higher reliability tasks.
- **Workflow graph**: developer-defined state machine where nodes are tool calls or LLM calls and edges are permissible transitions.

The paper presents graph-based orchestration / flow engineering as a practical shift away from open-ended chat loops: developers specify state, transitions, checkpoints, guards, approvals, and cycles; the LLM handles local reasoning inside that structure.

This is the source basis for [[wiki/concepts/Workflow Graph Orchestration]].

## Evaluation and Safety

The paper adopts CLASSic: Cost, Latency, Accuracy, Security, Stability.

Source-level points:

- Hierarchical reasoning can improve proficiency but increase token cost and latency.
- Real-world latency includes asynchronous waiting and time awareness, not only model response time.
- Accuracy for agents must include tool use, state tracking, long-horizon recovery, and failure severity.
- Security becomes central once agents have file I/O, code execution, enterprise APIs, MCP connectors, or computer-use capabilities.
- Stability includes infinite loops, paralysis, repetitive retries, and failure to ask for human help.

This is the source basis for [[wiki/concepts/Agent Evaluation CLASSic Framework]].

## Open Challenges

The paper highlights several open challenges:

- **Hallucination in action**: a wrong action can call a nonexistent API, mutate the wrong file, or cause irreversible failure.
- **Error propagation**: early mistakes in ReAct-like loops can cascade through later steps.
- **Infinite loops and paralysis**: agents can retry failed actions without strategic change.
- **Latency and computational cost**: debate, tree search, and multi-agent patterns are expensive.
- **Human-agent alignment and social norms**: task success alone can create harmful behavior.
- **Open-ended learning**: current agents often do not improve their core competence after deployment.
- **Theoretical limits and optimization**: intrinsic motivation, introspection, and active retrieval remain underdeveloped.

## What Was Promoted

- [[wiki/concepts/Agentic Control Loop]] — formal control-loop model.
- [[wiki/concepts/Agentic AI Architecture Taxonomy]] — six-dimensional architecture taxonomy.
- [[wiki/concepts/Agent Evaluation CLASSic Framework]] — evaluation and safety lens.
- [[wiki/concepts/Workflow Graph Orchestration]] — graph/state-machine orchestration pattern.
- [[wiki/concepts/Agent]] — updated from a thin concept seed toward a control-loop definition.
- [[wiki/topics/AI Harness]] and [[wiki/syntheses/Agent System Design Space]] — updated to connect taxonomy, workflow graphs, CLASSic evaluation, and harness governance.

## What Should Stay Source-Level

- Exact table rows and model/framework comparisons.
- The paper's specific examples of WebVoyager, AppAgent, SeeAct, Magma, AudioGPT, 3D-LLM, CAMEL, AutoGen, MetaGPT, ChatDev, DyLAN, LangGraph, Swarm, TradingAgents, and MAKER.
- Single-paper claims about model families and benchmark statuses, especially where the survey references 2026-era model versions and benchmarks that may change quickly.

## Related

- [[wiki/sources/Agent Systems Papers Source Guide]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/AI Memory]]
- [[wiki/concepts/Agentic Control Loop]]
- [[wiki/concepts/Agentic AI Architecture Taxonomy]]
- [[wiki/concepts/Agent Evaluation CLASSic Framework]]
- [[wiki/concepts/Workflow Graph Orchestration]]
- [[wiki/syntheses/Agent System Design Space]]
