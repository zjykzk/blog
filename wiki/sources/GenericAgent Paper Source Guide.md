---
title: GenericAgent Paper Source Guide
type: source
status: seed
summary: Source guide for the GenericAgent paper, focused on context information density, hierarchical memory, tool minimality, and self-evolution.
provenance:
  extracted: 0.86
  inferred: 0.14
  ambiguous: 0.0
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-05-04
source_count: 1
updated: 2026-05-04
aliases:
  - GenericAgent
  - GenericAgent paper
  - arXiv 2604.17091
tags:
  - papers
  - agents
  - ai
  - source
---

# GenericAgent Paper Source Guide

This page tracks the paper *GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)*.

## Source identity

- Title: *GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)*
- arXiv: `2604.17091v1`
- Submitted: 2026-04-18
- Authors: Jiaqing Liang, Jinyi Han, Weijia Li, Xinyi Wang, Zhoujia Zhang, Zishang Jiang, Ying Liao, Tingyun Li, Ying Huang, Hao Shen, Hanyu Wu, Fang Guo, Keyi Wang, Zhonghua Hong, Zhiyu Lu, Lipeng Ma, Sihang Jiang, Yanghua Xiao
- Project: `https://github.com/lsdefine/GenericAgent`
- DOI: `10.48550/arXiv.2604.17091`

## Why this source matters

The paper gives the current AI / Agent cluster a crisp systems principle: long-horizon agent quality depends on [[wiki/concepts/Context Information Density]], not simply on larger context windows.

Its main value is not the specific GenericAgent implementation alone. The reusable contribution is a way to evaluate agent systems by how they preserve decision-relevant information across tools, memory, compression, and repeated tasks. ^[inferred]

## Main claims to promote

### [[wiki/concepts/Context Information Density]]

- Long-horizon LLM agents face context explosion as tool definitions, memories, observations, and intermediate feedback accumulate.
- More visible context can reduce reasoning quality when irrelevant or stale material displaces decision-critical evidence.
- Context quality is framed as a balance between completeness and conciseness, with naturalness as a representational constraint.

### [[wiki/topics/Context Management]]

- Context management is a structural agent design problem, not a token-saving afterthought.
- GenericAgent targets a compact active budget under roughly 30k tokens and relies on layered compression rather than unbounded accumulation.
- Its trimming strategy combines tool-output truncation, tag-level compression, FIFO message eviction, and a working-memory anchor.

### [[wiki/topics/AI Harness]]

- GenericAgent treats the tool layer, memory layer, and compression layer as parts of one harness that shapes the model's active informational environment. ^[inferred]
- The paper argues for a minimal atomic tool set: fewer prompt-resident tool schemas and a smaller action space can reduce both token overhead and decision ambiguity.
- GenericAgent exposes nine atomic tools across file operations, code execution, web interaction, memory management, and human-in-the-loop control.

### [[wiki/syntheses/Agent System Design Space]]

- The system separates fixed tools from evolving operational knowledge.
- Self-evolution happens by consolidating verified trajectories into reusable SOPs and scripts, not by modifying the base model.
- Hierarchical memory uses an always-on index plus deeper fact, SOP, and raw-session layers, so historical knowledge remains retrievable without being loaded by default.

## Evidence from evaluation

The paper evaluates GenericAgent across task completion, tool-use efficiency, memory effectiveness, self-evolution, and web browsing.

Reported results include:

- On Lifelong AgentBench, GenericAgent reaches 100% accuracy while using far fewer input tokens than Claude Code and OpenClaw.
- On five long-horizon complex tasks, GenericAgent matches Claude Code's 100% success while using 188,829 total tokens versus Claude Code's 537,413.
- In repeated HuggingFace dataset-download tasks, GenericAgent's token use drops from about 200k to about 100k as experience is distilled into reusable memory.
- In one memory ablation, condensed memory matches redundant memory on task success while using fewer tokens.

These numbers should stay source-level until corroborated by independent replications or adjacent papers. ^[inferred]

## What should stay source-level

- Exact benchmark scores and token counts
- The specific nine-tool inventory
- Implementation details such as per-tool character thresholds
- Claims comparing GenericAgent to named systems unless later sources confirm the pattern

## Open questions

- Can context information density be operationalized as a stable metric across unrelated agent systems?
- How much of GenericAgent's reported advantage comes from architecture versus benchmark/task selection?
- Does self-evolution through SOPs remain reliable when tasks are less repetitive or when the environment changes quickly?

## Related

- [[wiki/sources/Agent Systems Papers Source Guide]]
- [[wiki/sources/Agent Engineering Source Guide]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/Agent System Design Space]]
