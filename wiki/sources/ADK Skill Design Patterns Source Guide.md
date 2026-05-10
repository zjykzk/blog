---
title: ADK Skill Design Patterns Source Guide
type: source
status: seed
category: sources
summary: Source guide for Google Cloud Tech and Lavi Nigam's article on five practical SKILL.md content patterns for ADK agents.
sources:
  - https://x.com/GoogleCloudTech/article/2033953579824758855
  - https://lavinigam.com/posts/adk-skill-design-patterns/
created: 2026-05-07T12:44:36+08:00
updated: 2026-05-07T12:44:36+08:00
base_confidence: 0.53
lifecycle: draft
lifecycle_changed: 2026-05-07
provenance:
  extracted: 0.86
  inferred: 0.14
  ambiguous: 0.0
aliases:
  - 5 Agent Skill Design Patterns Source Guide
  - Google Cloud Tech ADK skill patterns
tags:
  - agents
  - skills
  - adk
---
# ADK Skill Design Patterns Source Guide

This source guide covers Google Cloud Tech's X article and Lavi Nigam's expanded post, "5 Agent Skill Design Patterns Every ADK Developer Should Know." The source argues that SKILL.md's shared packaging format is no longer the hard part; the hard part is content design.

## Source Identity

- Original user-provided source: https://x.com/GoogleCloudTech/article/2033953579824758855
- Accessible expanded article used for extraction: https://lavinigam.com/posts/adk-skill-design-patterns/
- Mirror confirming the X article framing: https://en.rattibha.com/thread/2033953579824758855
- Companion repository: https://github.com/lavinigam-gcp/build-with-adk/tree/main/adk-skill-design-patterns

The X article was behind the logged-out X wall during ingest, so the extraction used the accessible expanded article and a thread mirror while preserving the original X URL as the source requested by the user.

## Core Claim

The article distinguishes the SKILL.md container from SKILL.md content design. The container is standardized across many coding-agent tools; the content still needs patterns that tell the agent whether it should load conventions, fill a template, run a rubric, interview the user, or execute a gated workflow.

This source is therefore primarily relevant to [[wiki/concepts/Agent Skill Design Patterns]], [[wiki/concepts/Agent Skill]], and [[wiki/topics/AI Skills Workflow]].

## Five Practical Patterns

1. Tool Wrapper packages library, SDK, framework, or internal-system conventions into on-demand references.
2. Generator produces consistently structured outputs by combining a template in `assets/` with style or quality rules in `references/`.
3. Reviewer evaluates submitted code, content, or artifacts against a checklist and groups findings by severity.
4. Inversion makes the agent ask phased questions before acting, using explicit gates to prevent premature synthesis.
5. Pipeline defines ordered multi-step workflows with validation gates between stages.

## What This Adds to the Wiki

- It gives [[wiki/concepts/Agent Skill]] a more precise taxonomy of internal skill shapes.
- It gives [[wiki/topics/AI Skills Workflow]] a vocabulary for the different control problems a skill can encode.
- It adds a strong bridge between [[wiki/topics/Tool Routing]] and skill authoring: the skill `description` field is effectively a routing surface for agent activation.
- It reinforces [[wiki/concepts/Verification Loop]] because Reviewer and Pipeline patterns make evaluation and gate-checking explicit parts of the skill, not afterthoughts. ^[inferred]

## Promoted Pages

- [[wiki/concepts/Agent Skill Design Patterns]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/sources/Agent Engineering Source Guide]]

## Open Questions

- The article says patterns compose, but it leaves open when composition becomes too large for a single skill. ^[ambiguous]
- ADK's current pip release did not support script execution from `scripts/` at the time of the article, while the broader Agent Skills spec discusses scripts as a supported directory; the operational boundary may change by version. ^[ambiguous]

## Related

- [[wiki/maps/AI Map]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Tool Routing]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/sources/Claude Code Skills Source Guide]]
- [[wiki/sources/Seeing Like an Agent Source Guide]]
