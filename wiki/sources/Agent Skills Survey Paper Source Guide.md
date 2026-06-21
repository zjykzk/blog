---
title: >-
  Agent Skills Survey Paper Source Guide
category: sources
type: source
status: draft
tags:
  - paper
  - arxiv
  - survey
  - agents
  - skills
aliases:
  - A Comprehensive Survey on Agent Skills
  - A Comprehensive Survey on Agent Skills: Taxonomy, Techniques, and Applications
  - arXiv:2605.07358
sources:
  - https://arxiv.org/abs/2605.07358v1
  - https://arxiv.org/pdf/2605.07358v1
created: 2026-05-18T15:01:48+08:00
updated: 2026-05-18T15:01:48+08:00
summary: >-
  Direct paper guide for the agent-skills survey, preserving its lifecycle taxonomy, resource taxonomy, retrieval/selection framing, evolution risks, and research agenda.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-05-18
---
# Agent Skills Survey Paper Source Guide

> Source: "A Comprehensive Survey on Agent Skills: Taxonomy, Techniques, and Applications", arXiv:2605.07358v1, submitted 2026-05-08.

## Capture Policy

This page preserves the arXiv paper as a primary source. It should be used for paper-grounded claims about the agent-skills lifecycle, taxonomy, retrieval/selection problem, evolution problem, and research agenda.

This page complements [[wiki/concepts/Agent Skill]], [[wiki/topics/AI Skills Workflow]], [[wiki/concepts/Skill Self-Evolution]], [[wiki/sources/Agent Skills Data-Driven Analysis Paper Source Guide]], [[wiki/sources/Skills-Coach Paper Source Guide]], and [[wiki/sources/SkillOS Paper Source Guide]]. Those pages cover concrete implementations, ecosystem measurements, optimization systems, or repository curation; this survey contributes the organizing map across the field.

## Source Identity

- Title: A Comprehensive Survey on Agent Skills: Taxonomy, Techniques, and Applications
- Authors: Yingli Zhou, Shu Wang, Yaodong Su, Wenchuan Du, Yixiang Fang, Xuemin Lin
- arXiv: 2605.07358v1, cs.IR, submitted 2026-05-08
- URL: https://arxiv.org/abs/2605.07358v1
- PDF: https://arxiv.org/pdf/2605.07358v1
- Companion resources: https://github.com/JayLZhou/Awesome-Agent-Skills

## Extraction Notes

The arXiv HTML and PDF were both accessible. The wiki extraction used arXiv HTML for readable text and the PDF bytes for the manifest content hash.

## What It Covers

The survey frames agent skills as the operational layer that lets LLM-based agents move from passive response generation and raw tool access toward reusable, composable, maintainable action. Its central problem is the "procedural gap": tools expose what can be done, but not when to invoke them, how to compose them, how to recover from failures, or how to validate results.

The paper organizes the field around four lifecycle stages:

1. **Skill representation**: how skills are packaged as instruction documents plus optional resources and trigger/applicability conditions.
2. **Skill acquisition**: how skills are created from human expertise, experience traces, current tasks, or external corpora.
3. **Skill retrieval and selection**: how agents find, rank, compose, and choose skills under context, state, latency, safety, and utility constraints.
4. **Skill evolution**: how skills are revised, validated, governed, versioned, deprecated, and trusted after deployment.

## Preserved Content

### Procedural Gap

The paper distinguishes active procedural knowledge from passive parametric knowledge. LLMs may have general reasoning priors, and tools may expose external capabilities, but neither layer by itself supplies stable procedures for coordinating capabilities in a concrete task.

Skills fill this gap by externalizing task-focused know-how. A skill specifies not only an operation, but also scope, applicability, sequencing, failure handling, and completion criteria. This makes skills closer to reusable workflow artifacts than to standalone tool APIs.

### Agent Skill Definition

The survey defines an agent skill as a reusable procedural artifact with bounded scope. Formally, it models a skill as a tuple whose key parts are:

- a root instruction document that the agent can load and follow;
- auxiliary resources such as reference documents, templates, scripts, or domain artifacts;
- applicability conditions that govern when the skill should be retrieved and used.

This formalization supports the local wiki definition of [[wiki/concepts/Agent Skill]] as a capability bundle, while adding a clearer lifecycle and retrieval boundary.

### Representation Taxonomy

The paper classifies skills by resource configuration:

- **Text-backed skills** use textual resources such as instructions, examples, rubrics, schemas, references, and checklists. They improve grounding and reuse without adding executable dependencies.
- **Code-backed skills** include executable resources such as scripts, helper functions, notebooks, or command wrappers. They can improve determinism and repeatability, but introduce software maintenance problems.
- **Hybrid-resource skills** combine textual and executable resources. They preserve human-readable procedure while adding deterministic support, but require consistency across instructions, code, references, and bindings.

This taxonomy explains why skill quality is not only prompt quality. At ecosystem scale, skill maintenance includes packaging, dependency management, schema consistency, security review, evaluation, and retirement. ^[inferred]

### Acquisition Taxonomy

The survey groups skill acquisition into four families:

- **Human-derived acquisition**: experts write reusable procedures, encode tacit judgment, and attach constraints or supporting material.
- **Experience-derived acquisition**: systems build skills from trajectories, demonstrations, execution traces, exemplars, or observed failures.
- **Task-derived acquisition**: skills are constructed on demand from the current task or requirement.
- **Corpus-derived acquisition**: skills are extracted from documents, repositories, interface traces, or other textual and structured corpora.

The important distinction is the direct source of procedural knowledge. Human-authored skills tend to be precise but slow to scale; experience- and corpus-derived skills promise scale but create quality-control, redundancy, and governance problems.

### Retrieval and Selection

The paper separates skill retrieval from skill selection. Retrieval finds candidates from a potentially large and heterogeneous library; selection decides which candidate or composition should actually run under current constraints.

Retrieval methods include dense embedding retrieval, sparse/keyword retrieval, generative retrieval, and structure-aware retrieval. Selection adds a harder decision problem: a skill may be semantically relevant but still wrong under the current state, budget, safety level, user preference, or execution context.

The survey highlights several design dimensions:

- representation quality from the retrieval perspective;
- state and applicability constraints;
- granularity and composition;
- objectives, feedback, and evaluation.

This strengthens [[wiki/topics/Tool Routing]] and [[wiki/topics/AI Skills Workflow]]: skill activation is not just search. It is runtime control over context, tools, cost, risk, and recovery. ^[inferred]

### Skill Evolution

The survey treats skills as lifecycle-managed artifacts, not static prompts. Evolution includes revision, validation, policy coupling, repository evolution, and runtime governance.

The strongest warning is asymmetry: systems are better at adding skills than safely rewriting, merging, deprecating, or retiring them. Once a skill library is writable and shareable, governance questions become unavoidable: who can publish, who is trusted, how provenance is tracked, how poisoned or stale skills are detected, and how responsibility is assigned when a skill causes harm.

The survey also warns that reported gains can be confounded. Improved performance may come from stronger judges, better task synthesis, more compute, richer grounding, or benchmark scale rather than from a better skill artifact. This matters for [[wiki/concepts/Skill Self-Evolution]] because evaluation must isolate whether the evolved artifact itself caused the improvement. ^[inferred]

### Open Challenges

The paper groups open challenges around acquisition, retrieval, and evolution:

- acquisition still lacks robust quality control, scalable validation, and clean ways to convert heterogeneous source material into usable skills;
- retrieval and selection need multi-objective decision protocols that combine success, cost, latency, safety, risk, user preference, and execution outcome;
- evolution needs causal evaluation, lineage, rollback, cleanup, trust, and repository-scale governance.

The future research directions are:

- **Unified skill schema** for scope, triggers, dependencies, versioning, and safety constraints;
- **resource-aware joint optimization** across retrieval, planning, execution, latency, token cost, and tool risk;
- **skill library evolution under non-stationarity**, including drift detection, compatibility checks, safe online updates, and rollback;
- **multimodal and domain-specific benchmarks** beyond text-centric settings;
- **causality-driven skill diagnosis** that attributes failures to retrieval mismatch, policy mis-selection, tool malfunction, or unsafe composition.

### Application Scenarios

The survey lists software engineering, web/GUI tasks, embodied domains, medical agents, education, retrieval, data analysis, and other application settings as places where skills package recurring procedural behavior.

For this wiki, the most relevant scenario is software engineering: skills package code generation, debugging, repository-aware refactoring, review, and operational routines so agents can reuse verified procedures rather than solve every issue from scratch.

## Integration Decisions

- Promote the lifecycle frame into [[wiki/topics/AI Skills Workflow]]: representation, acquisition, retrieval/selection, and evolution are the stable organizing dimensions.
- Keep exact platform counts, table entries, and per-paper benchmark comparisons source-level until independently cross-checked.
- Use the survey to connect [[wiki/concepts/Agent Skill]] with [[wiki/concepts/Skill Self-Evolution]], [[wiki/topics/Tool Routing]], and [[wiki/topics/AI Harness]].
- Treat the paper's research agenda as a checklist for future skill-system design: schema, resource-aware routing, drift handling, multimodal/domain benchmarks, and causal diagnosis.

## Open Questions

- How should a local skill registry expose enough metadata for retrieval without increasing always-on context cost? ^[inferred]
- What is the right validation gate before a skill is promoted into a shared repository? ^[inferred]
- How should cleanup, merge, and retirement be made as routine as skill creation? ^[inferred]

## Related

- [[wiki/concepts/Agent Skill]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/Tool Routing]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Skill Self-Evolution]]
- [[wiki/sources/Agent Skills Data-Driven Analysis Paper Source Guide]]
- [[wiki/sources/Skills-Coach Paper Source Guide]]
- [[wiki/sources/SkillOS Paper Source Guide]]
