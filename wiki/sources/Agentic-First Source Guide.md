---
title: Agentic-First Source Guide
category: sources
tags:
  - article
  - agents
  - harness
  - ai-coding
  - context
sources:
  - https://james-pritchard.com/blog/agentic-first
created: 2026-05-20T04:11:49+08:00
updated: 2026-05-20T04:11:49+08:00
summary: >-
  Source guide for James Pritchard's Agentic-First article, focused on designing workflows, context, platforms, and validation around agent operation.
provenance:
  extracted: 0.86
  inferred: 0.11
  ambiguous: 0.03
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-20
type: source
status: draft
aliases:
  - Agentic-First
  - Designing Systems for AI From Day One
  - Agentic-First Designing Systems for AI From Day One
---
# Agentic-First Source Guide

> Source: [Agentic-First: Designing Systems for AI From Day One](https://james-pritchard.com/blog/agentic-first)

## Capture Policy

This page preserves James Pritchard's article as source-level material. Its migration economics, platform comparison, and workflow claims should remain attributed to the source until corroborated by other production reports.

## What It Covers

The article argues that many AI workflow failures come from placing agents inside systems designed for human operators. The proposed remedy is an “agentic-first” design stance: start from the outcome, give the agent a navigable environment, compile relevant context, and put human oversight and validation at the system boundaries rather than inside every reasoning step.

The central case is a website migration system that moves from a WordPress/Oxygen, checkpoint-heavy workflow toward an Astro, file-oriented workflow that agents can inspect, edit, diff, and validate.

## Preserved Content

### Why traditional development instincts break AI systems

The article opens by rejecting the default diagnosis that agentic systems stall because the model is weak, prompts are bad, or review is insufficient. In the author's migration work, “the AI was never the bottleneck”; the bottleneck was the workflow architecture around it.

The original migration tool crawled a client site, extracted content with AI, mapped pages into templates, and deployed to WordPress. Traditional instincts inserted human control points throughout the process:

- humans selected templates before page processing;
- pages were reviewed one by one;
- deployment remained manual;
- later editing happened inside a page builder;
- the UI expanded to manage all these review and routing steps.

These controls looked like precision but often forced premature decisions. A human had to pick a template before the system had analyzed the page deeply enough. Review comments and edits happened outside the AI's awareness, so they did not improve the agent's next decisions. Narrow prompts split decisions that should have been made with the page, site structure, components, and design system in view together.

The source's core criticism is that each checkpoint can add complexity without adding quality when it interrupts the agent before it has enough context to act well.

### Design the system for the agent

The article reframes the design question from “how do we supervise this AI helper?” to “what environment lets the agent complete the task without interruption while still respecting boundaries?”

This does not remove human oversight. It moves oversight to boundary decisions: defining scope, setting constraints, approving final outputs, and reviewing generated pull requests. Inside the work loop, the system should avoid asking humans to make decisions the agent can make better with fuller context.

The article names three practical design principles.

#### Pick a platform the agent can navigate

The replacement system targets Astro instead of WordPress/Oxygen. The reason is not only developer preference; it is agent navigability.

Astro gives the agent a file-oriented environment:

- routes map to files;
- content can live in YAML;
- layouts are explicit imports;
- page assembly is visible rather than hidden inside a database and page builder;
- review can happen through small diffs.

The broader claim is that platform architecture becomes an AI performance decision. A system with inspectable files, explicit relationships, and deterministic checks gives agents better control surfaces than a system whose state is hidden behind UI operations and database-driven composition.

#### Give the agent the right context

The source treats context as working memory. The agent should receive the information needed for the current mode, not every instruction the organization has ever written.

Instead of one giant instruction file, the author uses modular documentation compiled into task-specific context. Migration mode and maintenance mode get different instructions, hooks, skills, and agent definitions.

This mode-aware context design keeps irrelevant constraints out of the active prompt and gives the agent the source content, component library, design tokens, and site structure needed for holistic decisions.

#### Guardrails at edit time, not after the fact

The article emphasizes validation while the agent edits, so failure becomes immediate feedback rather than late review debt.

Edit-time validation includes:

- YAML schema checks;
- component rules;
- structural constraints;
- design token enforcement.

A second layer blocks commits unless builds, links, components, and page patterns pass. Shared resources can be locked when a task should not modify them. The agent should also be prevented from editing its own instructions or configuration; instruction changes should flow through source docs, rebuild steps, and human installation.

This makes guardrails part of the agent's operating environment rather than a post-hoc QA ritual.

### Automate the process, not the steps

The article's most reusable distinction is “automate the process, not the steps.” The old system automated pieces of a human workflow: choose a template, fill slots, review a page, deploy manually, edit in a builder. The new system starts from the desired result: migrate the site.

From that perspective, the design target is not preserving existing handoffs. It is letting the agent do the full initial build with enough context and validation, then using humans and agents for QA, design refinement, content changes, and client-specific adjustment afterward.

The source reports a business comparison from the author's migration work:

- old process: 30–120 developer hours per site;
- old throughput: about two sites per month;
- old bottleneck: production capacity;
- old delivery time: weeks;
- new test migrations: about $20 compute per migration;
- new bottleneck: sales capacity rather than production capacity;
- new delivery time: days.

These numbers are source-reported operating claims, not general benchmarks. They should be used as an example of workflow redesign economics, not as universal estimates.

### Bigger point

The article ends with a general claim: AI integration should not mean adding AI to legacy human workflows. Teams should redesign workflows around agent capabilities, because architecture, context, and constraints often matter more than prompt tweaks or model upgrades.

The source's memorable formulation is: “Architecture is an AI performance decision.”

## Integration Decisions

This source belongs in the agent engineering and harness cluster because it contributes a concrete production-design pattern: make the target environment agent-navigable, keep context mode-specific, and make validation immediate.

The article reinforces [[wiki/concepts/Agentic Engineering]] by shifting engineering work from prompt supervision to environment design. It reinforces [[wiki/concepts/Harnessability]] by showing that Astro's explicit file structure is more harnessable than a hidden page-builder workflow. It also reinforces [[wiki/concepts/Verification Loop]] because edit-time validation turns mistakes into agent-readable feedback.

The article should not be collapsed into a stable concept page yet. “Agentic-first” is a useful phrase, but the strongest evidence is still a single author's website migration experience. The promotable concept is broader: platform and workflow design can raise or lower the ceiling of agent performance. ^[inferred]

## Open Questions

- Which parts of the reported productivity gain come from AI delegation, and which come from replacing WordPress/Oxygen with a simpler file-oriented architecture?
- How much edit-time validation is required before an agent can safely run the full migration loop without human checkpoints?
- Does the agentic-first pattern transfer to domains where the best representation is not file-based code and content?

## Related

- [[wiki/concepts/Agentic Engineering]]
- [[wiki/concepts/Harnessability]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/sources/Agent Engineering Source Guide]]
- [[wiki/sources/Harness Engineering Source Guide]]
- [[wiki/sources/Coding with AI Source Guide]]
