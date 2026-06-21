---
title: Human-LLM Collaborative Planning Paper Source Guide
type: source
tags:
  - paper
  - arxiv
  - agents
  - orchestration
  - human-in-the-loop
category: sources
sources:
  - https://arxiv.org/abs/2605.23023
summary: Direct paper guide for AMBIPOM and human-LLM co-planning, preserving its mode-scope-level design space, user-study findings, benchmark, limitations, and harness implications.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: "2026-06-09"
created: 2026-06-09T14:38:26+08:00
updated: 2026-06-09T14:38:26+08:00
aliases:
  - AMBIPOM paper
  - How to Steer Your Multi-Agent System
---
# Human-LLM Collaborative Planning Paper Source Guide

## Source Identity

- Source: https://arxiv.org/abs/2605.23023
- Title: How to Steer Your Multi-Agent System: Human-LLM Collaborative Planning
- Authors: Zeyu He, Hannah Kim, Dan Zhang, Estevam Hruschka
- Venue note: ACM Conference on AI and Agentic Systems (CAIS) 2026
- Related DOI: https://doi.org/10.1145/3786335.3813144
- Artifact: https://github.com/megagonlabs/ambipom
- Extraction representation: the arXiv HTML and PDF were both accessible. The wiki extraction used arXiv HTML for readable text and the PDF bytes for the manifest content hash.
- Hashed representation: PDF bytes from https://arxiv.org/pdf/2605.23023

## What the paper is about

The paper studies how humans can steer orchestrated multi-agent systems by supervising the plan process rather than only checking final outputs.

Its core problem statement is that orchestrated MAS often use an LLM planner to decompose a high-level task into subtasks for specialized agents, but generated plans may misalign with human intent, miss domain constraints, or hallucinate. Existing outcome-level supervision leaves intermediate states opaque, making failures hard to diagnose and local corrections hard to apply.

The paper represents multi-agent plans as directed acyclic graphs: nodes are agent-executable subtasks, and edges encode data dependencies. This turns the plan into a first-class object that can be inspected, modified, executed, and debugged before and during execution.

## Core contribution: three-axis co-planning space

The paper formalizes [[wiki/concepts/Human-LLM Co-Planning Interaction Space]] along three axes:

- Mode: structural direct manipulation of the graph vs. semantic natural-language feedback.
- Scope: global feedback over the full plan vs. targeted feedback conditioned on a selected subgraph.
- Level: low-level graph edits vs. high-level operations such as merge, split, or replan.

This framing extends earlier process-level supervision systems that exposed only mode-level differences. By making scope and level first-class, the paper makes human-LLM planning interactions comparable rather than treating every intervention as generic chat feedback.

## AMBIPOM prototype

AMBIPOM stands for Agent-aware Mixed-initiative Block-level Interactive Planning for Orchestrated Multi-agent systems.

The prototype includes:

- An LLM planner for initial plan generation and revisions.
- Four execution agents specialized in code, math, search, and commonsense tasks.
- A dual-panel interface: a chat panel for semantic interactions and a plan panel for graph-based structural interactions.
- Node cards showing subtask description, assigned agent, inputs/outputs, status, and execution logs.
- Direct manipulation operations: add/delete/duplicate/reposition nodes, link/remove edges, edit task descriptions, agent assignments, I/O variables, and agent configuration.
- High-level structural operations: merge selected interface-closed subgraphs and split nodes, with both manual and LLM-assisted variants.

Targeted feedback replans only a selected subgraph and reintegrates it with the unchanged plan. The system intentionally provides the planner only the selected subgraph and boundary I/O specification, rather than full history and full plan, to reduce irrelevant context and format violations.

## User study findings

The user study involved 13 participants and compared AMBIPOM to a baseline system.

Important findings:

- LLM-assisted high-level direct manipulation received the highest ease-of-use rating among AMBIPOM interaction options.
- Targeted replanning reduced conversational turns compared with general chat, while the richer feature set led users to perform more total editing operations.
- Users did not choose a single interaction type; they assembled hybrid workflows per iteration.
- A common refinement loop was: review or execute the current plan, apply targeted or global text feedback, use manual or LLM-assisted direct manipulation for local repair, then re-execute.
- Structural modifications pulled strongly toward LLM-assisted high-level DM, while semantic or ambiguous modifications were more mixed.
- Participants treated direct manipulation as high-control/high-effort, LLM-assisted high-level DM as bounded structural leverage, targeted feedback as bounded semantic leverage, and global feedback as low authoring effort but high verification burden.
- Participants often feared that global replanning could “blow up” the plan.
- Users followed two rhythms: review-first (10/13) and execute-first (3/13). Both converged on broad text edits followed by local structural patches and re-execution.
- Feedback was overwhelmingly prescriptive/instructive: 169 of 178 text feedback messages gave commands such as split, connect, or use output from a node.
- Trust in LLM-assisted high-level DM increased during tasks, but verification effort declined over time, creating a trust-fatigue paradox.

These findings are source-level user-study claims and should not be promoted as universal behavior without more diverse validation.

## Benchmark and controlled experiments

The benchmark contains 200 gold plans and 1,150 broken-plan items built by applying reverse operations to gold plans.

The benchmark spans four subsets:

- Stepwise Math Reasoning
- Multi-Hop Computation
- Listed Retrieval & Aggregation
- Top-K Retrieval & Aggregation

It covers seven operation types:

- add node
- change node description
- change node agent
- merge sequential
- merge parallel
- split sequential
- split parallel

Conditions compared include GF, TF, TF+P, auto-merge/auto-split variants, and GF-to-DM edit-sequence generation.

The paper evaluates graph edit distance, semantic similarity, plan stability, and execution accuracy where applicable. Integration success rates were:

- GF: 1150/1150, success rate 1.000
- TF: 1122/1150, success rate 0.976
- TFsplit: 150/150, success rate 1.000
- TFmerge: 397/400, success rate 0.992
- TF+P: 1134/1150, success rate 0.986
- GF-to-DM: 197/250, success rate 0.788

The main interpretation is that global feedback is robust because it regenerates the whole plan and avoids reintegration failures, while targeted feedback preserves stability but can fail at subgraph boundaries. Full-plan context improves targeted reintegration success. Edit-sequence generation provides an audit trail but is less reliable because operation validity depends on accurately tracking the changing plan state.

## Design suggestions

The discussion argues that richer interaction types shift user effort from authoring to verification and integration. The bottleneck is not only generating edits faster; it is making edits easy to trust, integrate, and verify.

Design suggestions:

- Add verification and integration support: edit previews, boundary compatibility validation, orphan-node detection, I/O mismatch warnings.
- Provide proactive context-aware guidance: recommend targeted prompts or structural operations based on selected nodes and their boundary contracts.
- Surface likely follow-up fixes after replanning: missing bindings, orphan nodes, boundary mismatch, one-click repairs.
- Pair a general DAG planning shell with domain-specific output panels such as code diffs, image previews, table viewers, or long-text comparison panes.

## Limitations

- The co-planning paradigm covers a single user operating on an orchestrated MAS with a fixed set of specialized agents.
- It does not evaluate multi-user collaboration, cooperative/decentralized MAS, or other agent configurations.
- The user study sample is small and drawn from one research lab, with many participants already experienced with LLMs.
- Verification effort declined over time, which may bias plan quality measures.
- The benchmark tasks are constrained and may not capture highly dynamic open-ended planning workflows.
- Main experiment broken plans are synthetically constructed, though the appendix evaluates naturally occurring faulty plans as supplementary evidence.

## Wiki routing decisions

- Promote the three-axis model into [[wiki/concepts/Human-LLM Co-Planning Interaction Space]].
- Update [[wiki/concepts/Workflow Graph Orchestration]] because this paper adds a human steering layer over explicit plan DAGs.
- Update [[wiki/topics/AI Harness]] because plan steering is a harness control surface, not just an interface feature. ^[inferred]
- Update [[wiki/syntheses/Agent System Design Space]] because the paper adds a human-intervention dimension to orchestration design. ^[inferred]

## Related

- [[wiki/concepts/Human-LLM Co-Planning Interaction Space]]
- [[wiki/concepts/Workflow Graph Orchestration]]
- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/maps/AI Map]]
