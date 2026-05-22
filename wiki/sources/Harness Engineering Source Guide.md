---
title: Harness Engineering Source Guide
type: source
status: growing
category: sources
summary: Source guide for Birgitta Böckeler's Martin Fowler article on user-owned harness engineering for coding agents, combining guides, sensors, timing, regulation categories, templates, and human judgment.
sources:
  - https://martinfowler.com/articles/harness-engineering.html
created: 2026-05-06T22:24:21+08:00
updated: 2026-05-23T01:52:00+08:00
base_confidence: 0.48
lifecycle: draft
lifecycle_changed: 2026-05-06
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.0
aliases:
  - Harness engineering for coding agent users
  - Martin Fowler harness engineering
  - Birgitta Böckeler harness engineering
  - coding agent harness engineering source guide
tags:
  - article
  - agents
  - harness
  - ai-coding
---
# Harness Engineering Source Guide

> Source: Birgitta Böckeler, “Harness engineering for coding agent users,” Martin Fowler, 2026-04-02, https://martinfowler.com/articles/harness-engineering.html

## Capture Policy

This page preserves the Martin Fowler article as source-level material for the AI / agent engineering cluster. It keeps the article's control vocabulary, diagrams, examples, regulation categories, and open questions distinct from broader wiki syntheses about [[wiki/topics/AI Harness]] and [[wiki/syntheses/AI Engineering Workflow]].

## What It Covers

The article argues that coding-agent users should not treat an agent as a sealed black box. A practical coding-agent setup includes an outer user-owned harness: prompts, rules, tools, tests, linters, review agents, knowledge sources, workflow integrations, and continuous signals that steer and inspect the agent's work.

The article narrows the broader “model plus harness” framing. The model and vendor-built coding-agent harness already exist inside the tool. The user's leverage sits in the outer harness that the team builds around that agent: repository conventions, instructions, executable checks, feedback loops, and templates that make generated work more trustworthy.

For this wiki, the source's durable contribution is a concrete control model for [[wiki/concepts/Coding Agent User Harness]]: harness engineering combines feedforward guidance, feedback sensing, deterministic checks, inferential review, lifecycle timing, regulation categories, reusable templates, and human accountability.

## Preserved Content

### Core model: guides and sensors

The article uses a steering-loop model:

- **Guides / feedforward controls** shape the agent before it acts. Examples include coding conventions, bootstrap instructions, architecture documentation, testing how-tos, API reference docs, knowledge-management access through MCP, codemods, and LSP/code-intelligence inputs.
- **Sensors / feedback controls** inspect results after the agent acts. Examples include code-review agents, linters, static analysis, structural tests, coverage checks, mutation testing, browser checks, logs, runtime SLO monitoring, dead-code analysis, dependency scanning, response-quality sampling, and log-anomaly review.
- The human steers both sides: they choose what guidance to encode, what sensors to add, when to trust agent self-correction, and when to intervene.

The source warns against one-sided control. Feedback without guidance can create repeated avoidable errors. Guidance without feedback leaves the team unable to tell whether the agent followed the guidance. The useful harness combines both.

This maps directly to [[wiki/concepts/Feedforward and Feedback Controls]]: feedforward narrows the action before generation; feedback makes deviations visible after generation and can enter the agent's self-correction loop.

### Computational and inferential controls

The article separates control mechanisms by execution type:

- **Computational controls** are deterministic, fast, and cheap enough to run frequently. Examples include tests, type checkers, linters, structural analysis, static analysis, architecture boundary checks, and scripts.
- **Inferential controls** rely on semantic judgment by LLMs or people. Examples include AI review agents, LLM-as-judge, design review, over-engineering detection, redundant-test detection, and review rubrics.

The article prefers computational checks when the quality criterion can be made executable. They are cheaper, more repeatable, and better suited for frequent feedback close to the coding activity. Inferential checks remain useful when the criterion involves meaning, taste, trade-off, architectural intent, or organizational context.

This is the source layer behind [[wiki/concepts/Computational and Inferential Controls]]. It explains why tests and linters are not “just QA”; inside an AI coding workflow, they are harness sensors that let the agent or human correct work earlier.

### The steering loop

The article's harness overview diagram places the coding agent inside a loop where guides feed into the agent, sensors observe generated results, and feedback can be routed back into self-correction. The human remains outside the loop as the designer and accountable operator of the harness.

The practical loop is:

1. encode expectations through rules, docs, skills, conventions, tools, and project instructions;
2. let the coding agent work inside that guided environment;
3. inspect results through sensors;
4. feed results back into agent correction or human review;
5. improve the harness when failures repeat.

This turns repeated agent mistakes into harness improvements rather than one-off prompt fixes. A recurring error can become a new rule, a deterministic sensor, a refined guide, a linter, a codemod, a test, a checklist, or a template change. That is the operational link to [[wiki/concepts/Harness Ratchet]].

### Timing: keep quality left

The article distributes guides and sensors across the change lifecycle. The main recommendation is to move fast feedback as close as possible to the moment of coding:

- before human review;
- before integration;
- in pre-commit hooks;
- in the agent loop;
- in CI/CD;
- after integration through continuous drift and runtime monitoring.

Fast deterministic checks belong early. More expensive or slower checks can run later. Some sensors should run continuously rather than only on individual changes, especially when they watch for accumulating drift: dead code, dependency risk, weak coverage, architecture erosion, runtime anomalies, SLO degradation, or response-quality changes.

The source's timing claim strengthens the wiki's AI coding quality model: verification is not a terminal stage after generation; it is a runtime placement problem. The same check has different value depending on whether it runs before generation, inside the agent loop, before review, before merge, or after production drift appears. ^[inferred]

### Regulation categories

The article groups harness controls into three regulation categories.

#### Maintainability harness

A maintainability harness governs internal code quality. Many maintainability issues can be caught through deterministic tooling:

- duplication;
- complexity;
- missing coverage;
- style violations;
- static-analysis warnings;
- architecture drift;
- dependency risk;
- dead code.

LLM-based review may help with semantic maintainability concerns such as over-engineering or weak test value, but the article treats those as less deterministic than executable checks.

#### Architecture fitness harness

An architecture fitness harness governs whether the system continues to satisfy architectural characteristics and constraints. Examples include:

- performance requirements;
- observability conventions;
- logging standards;
- dependency boundaries;
- architecture fitness functions;
- ArchUnit tests;
- dep-cruiser checks;
- performance tests;
- structural tests;
- runtime SLO monitoring.

This category connects harness engineering to architecture governance. The harness is not only a local coding convenience; it can encode architectural boundaries and make drift visible before it becomes system-wide erosion.

#### Behaviour harness

A behaviour harness governs whether the application does the right thing functionally. The article treats this as the least solved area. Current approaches include specifications, AI-generated tests, coverage tools, mutation testing, approved fixtures, manual testing, browser-based feedback, logs, and response-quality sampling, but the article does not claim these fully solve functional confidence.

This matters because AI-generated code can satisfy syntactic or structural checks while still solving the wrong behavior. Behaviour harnesses need better specification, example, test, and observation structures before teams can delegate more confidently.

### Harnessability

The article introduces harnessability as the quality of a codebase, task, or workflow that makes it easier to surround with useful controls. A more harnessable environment has:

- strong types;
- clear boundaries;
- standard frameworks;
- explicit conventions;
- tractable structure;
- runnable tests;
- accessible tooling;
- codified architectural constraints;
- examples and templates that agents can follow.

This source grounds [[wiki/concepts/Harnessability]]. Harnessability is not the same as agent intelligence. It is a property of the work environment: whether the codebase exposes enough structure for guides and sensors to be effective.

### Harness templates

The article extends the ordinary service-template idea. A template should not only instantiate starter code; it can also instantiate a guide-and-sensor bundle. Example service topologies include:

- a data dashboard in Node;
- a CRUD business service on the JVM;
- an event processor in Golang.

A harness template can package coding conventions, architecture documentation, tests, static checks, CI defaults, review agents, observability expectations, and recommended workflows. This turns recurring application shapes into reusable agent-governance setups.

The article mentions related industry examples such as OpenAI's harness engineering write-up, Stripe's “minions,” service templates, MCP servers, AGENTS.md, skills, LSPs, CLIs, scripts, codemods, OpenRewrite recipes, ArchUnit tests, pre-commit hooks, ESLint, Semgrep, coverage tooling, mutation testing, Dependabot, Spring, and continuous delivery.

### Sidebars and supporting frames

The article includes several framing sidebars:

- **Metaphors only go so far** cautions that harness metaphors help organize thinking but should not be treated as exact system descriptions.
- **How does harness engineering relate to context engineering?** places context work inside the broader harness. Context engineering controls what the agent sees; harness engineering also controls tools, checks, workflows, and feedback.
- **Ambient affordances** points to environmental cues and defaults that guide action without a direct command.
- **Ashby's Law** suggests that a regulator needs enough variety to handle the variety in the system being regulated. For AI coding, a harness needs enough guide and sensor variety to govern the range of agent failure modes.

### Role of the human

The article keeps the human in the loop, but not as an all-purpose manual reviewer. Humans supply judgment, taste, accountability, organizational context, and trade-off awareness. Harnesses can externalize some of this knowledge into rules, tests, templates, and sensors, but they cannot remove all human judgment.

The goal is to focus human attention where it matters most: ambiguous trade-offs, product intent, accountability, architectural judgment, and decisions that cannot be reduced to deterministic checks.

### Starting point and open questions

The article closes by positioning harness engineering as an emerging practice rather than a finished discipline. Open questions include:

- how to keep guides and sensors consistent as the harness grows;
- how agents should resolve conflicting instructions and conflicting feedback;
- how teams should evaluate harness coverage and quality;
- how tooling can configure, synchronize, and reason about controls across the delivery lifecycle;
- how to improve behaviour harnesses, because functional correctness remains the hardest category to govern.

## Integration Decisions

This page should remain a source guide, not a general harness concept page. The broad abstraction lives in [[wiki/topics/AI Harness]], while this page preserves Böckeler's article-specific vocabulary: guides/sensors, computational/inferential controls, lifecycle timing, regulation categories, harnessability, harness templates, and the human role.

The source strengthens four existing wiki concepts:

- [[wiki/concepts/Coding Agent User Harness]] — developer-owned harnesses around existing coding agents.
- [[wiki/concepts/Feedforward and Feedback Controls]] — guides before action and sensors after action.
- [[wiki/concepts/Computational and Inferential Controls]] — deterministic executable checks versus semantic judgment controls.
- [[wiki/concepts/Harnessability]] — the task/codebase quality that makes useful harnessing easier.

It also supports [[wiki/concepts/Harness Ratchet]]: repeated agent failures should update durable control surfaces rather than remain prompt-by-prompt corrections.

The article's maintainability / architecture fitness / behaviour categories are source-level terms for now. They may later support a synthesis with [[wiki/topics/Testing Strategy]], [[wiki/topics/AI Harness]], [[wiki/syntheses/Quality Engineering Three Generators]], and [[wiki/syntheses/AI Engineering Workflow]].

## Open Questions

- How should teams measure harness coverage without creating a false sense of safety?
- Which behaviour-harness techniques reliably catch “wrong thing built” failures rather than only code-shape failures?
- When does a harness template become too rigid for product-specific judgment?
- How should conflicting guides and conflicting sensor outputs be prioritized inside an agent loop?

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/syntheses/Quality Engineering Three Generators]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/concepts/Feedforward and Feedback Controls]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/concepts/Harnessability]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/sources/Agent Harness Engineering Source Guide]]
