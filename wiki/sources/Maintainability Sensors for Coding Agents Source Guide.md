---
title: Maintainability Sensors for Coding Agents Source Guide
type: source
status: growing
category: sources
tags:
  - article
  - agents
  - harness
  - ai-coding
  - software-engineering
sources:
  - https://martinfowler.com/articles/sensors-for-coding-agents.html
created: 2026-05-23T01:59:29+08:00
updated: 2026-05-23T01:59:29+08:00
summary: Source guide for Birgitta Böckeler's Martin Fowler article on maintainability sensors for coding agents, covering linting, dependency rules, coupling data, and AI modularity review.
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.0
base_confidence: 0.48
lifecycle: draft
lifecycle_changed: 2026-05-23
aliases:
  - Maintainability sensors for coding agents
  - Sensors for coding agents
  - Martin Fowler maintainability sensors
  - Birgitta Böckeler maintainability sensors
---
# Maintainability Sensors for Coding Agents Source Guide

> Source: Birgitta Böckeler, “Maintainability sensors for coding agents,” Martin Fowler, 2026-05-20, https://martinfowler.com/articles/sensors-for-coding-agents.html

## Capture Policy

This page preserves a practical follow-up to [[wiki/sources/Harness Engineering Source Guide]], not a duplicate of it. The earlier source guide frames user-owned coding-agent harnesses broadly; this page keeps the follow-up article's maintainability experiments, sensor categories, observations, and limits as source-level material for [[wiki/topics/AI Harness]] and [[wiki/topics/Testing Strategy]].

## What It Covers

The article asks how coding-agent users can sense maintainability problems early enough to correct them. Maintainability means internal code quality that makes future changes easier and safer: small changes should not require broad edits, and new changes should not break existing behavior.

The article's practical claim is that AI-generated code can accumulate technical debt quickly unless the surrounding harness includes maintainability sensors. These sensors do not replace human design judgment, but they make certain maintainability risks visible during coding sessions, in CI, or through periodic review.

## Preserved Content

### The application and experimental setup

The source uses an internal analytics dashboard for community managers as its testbed. The dashboard combines chat activity, engagement, and demographic data from several APIs, using TypeScript, Next.js, and React.

Böckeler rebuilt an existing application from scratch with AI to observe how maintainability sensors behaved when the agent received relatively little explicit quality guidance. This made the experiment sensor-centered: instead of asking whether a strong prompt could prevent problems, it asked what feedback surfaces could reveal and steer problems as the codebase grew.

The work used Cursor, Claude Code, and OpenCode. The article mentions Claude Sonnet for much of the work, Claude Opus for analysis, and Cursor composer-2 for implementation.

### Sensor landscape

The article groups maintainability sensors by timing:

- **During coding sessions**: type checker, ESLint, Semgrep, dependency-cruiser, tests, coverage, incremental mutation testing, and GitLeaks in a pre-commit hook.
- **After integration**: the same computational checks run in CI on clean infrastructure.
- **Repeatedly**: AI-assisted security review, AI-assisted data-handling review, dependency freshness reports, and modularity or coupling reviews.

This timing frame extends the earlier guide/sensor model from [[wiki/sources/Harness Engineering Source Guide]]. The useful question is not only “which check exists,” but where it runs: inside the agent loop, before commit, in CI, after integration, or periodically as drift review. ^[inferred]

### Static code analysis: basic linting

The first sensor family is linting for local code maintainability. The article uses ESLint rules that catch risks common in AI-generated code:

- too many function arguments;
- overlong files;
- overlong functions;
- high cyclomatic complexity.

These rules were not part of the default preset and had to be configured. The source suggests that future presets may become more agent-aware because AI coding changes the cost and failure profile of static analysis.

Böckeler also customized lint messages so they guide self-correction. A bare lint failure tells the agent that something is wrong; a richer message tells it how to reason about the failure. For example, an explicit `any` warning can tell the agent to decide whether to introduce a type or suppress the warning with a reason. Suppression then becomes a reviewable artifact rather than hidden drift.

The article observes several trade-offs:

- Agent-created exceptions became useful code-review entry points.
- The agent sometimes raised cyclomatic-complexity thresholds when the lint message did not strongly guide refactoring.
- Some rules need local interpretation, such as frontend logging versus backend logging.
- Splitting React components to satisfy one rule can create new issues, such as components with excessive props.

The takeaway is that linting becomes more cost-effective with AI because custom rules and scripts are cheaper to create and maintain. But linting can also produce false confidence, feedback overload, or over-refactoring if treated as a complete quality measure.

### Static code analysis: dependency rules

The second sensor family protects cross-file and cross-module structure. The article uses dependency-cruiser to enforce backend layering. One example rule prevents API clients from importing service-layer code. Error messages include architectural guidance about routes, services, clients, and domain code.

The source notes that AI made dependency-cruiser setup cheaper despite the tool's configuration complexity. After rules were introduced, agents violated them a few times but then self-corrected. Similar rules were added for frontend React hook structure and for preventing new files from appearing outside the intended folder layout.

The main takeaway is that dependency rules can preserve folder architecture and sometimes substitute for long-form markdown guidance. Their limitation is also clear: they see imports, paths, and file layout, not semantic design intent.

### Static code analysis: coupling data

The third sensor family measures coupling. Instead of adopting an existing tool, Böckeler built a custom TypeScript-based analyzer with AI. It measured incoming and outgoing imports and calls per file, then exposed the results through two surfaces:

- a web UI for human visual analysis;
- a CLI for agent consumption.

For humans, visual coupling tools such as dependency structure matrices remained difficult to interpret. The raw data still required architectural context and experience.

For AI, the author prompted an LLM to run the CLI and produce a modularity report grounded in tool output. The AI identified roughly the same hotspots visible in diagrams, but presented them in a more digestible form. Grounding the report in deterministic data increased confidence compared with a purely speculative scan.

The article also shows the limits of raw coupling data. The LLM misidentified some intentional patterns as problems, including a lightweight dependency-injection factory and a shared Zod schema used as a frontend/backend contract. Legitimate high-coupling hubs need suppression or explanation mechanisms. One useful finding was an `index.ts` barrel file in the domain layer that exposed many domain modules and deserved review.

The takeaway is that coupling metrics are risk signals, not design verdicts. They may be especially useful for code-review triage: changed files with many callers or many dependencies deserve more attention.

### Static code analysis: AI modularity review

The final experiment uses Vlad Khononov's Modularity Skills for an LLM-based design review. This produced stronger results than raw coupling analysis. Running the review with access to coupling data mostly confirmed findings rather than creating a new analysis, while a second independent run surfaced an additional issue.

The AI modularity review found several maintainability concerns:

- duplicate backend route code across three endpoints;
- inconsistent frontend patterns for calling backend code from pages;
- repeated passing of core request parameters, such as chat space and date range, through many layers;
- a partially introduced parameter object that was not used consistently;
- authentication fallback logic placed in a factory where it did not belong;
- high-import hubs interpreted with more context than in the coupling-only review.

The article's key distinction is that modularity is partly semantic. Dependency rules and coupling metrics can expose structure, but they cannot fully decide whether structure is appropriate. AI review can act as periodic design cleanup or maintainability garbage collection, especially when grounded in deterministic data and followed by human judgment.

### Overall takeaways from the source

The article's final position is balanced:

- Dependency rules are useful live guardrails for structural direction.
- Computational sensors are necessary but insufficient for modularity.
- LLM-based review can add semantic interpretation where metrics alone are too shallow.
- Human review remains necessary because some coupling, layering, and modularity decisions depend on context.
- Without maintainability sensors, coding agents can accumulate inadvertent technical debt faster than teams notice.

For this wiki, the source makes maintainability a concrete subcase of [[wiki/concepts/Computational and Inferential Controls]]. Linting, dependency rules, and coupling metrics are computational sensors; AI modularity review is an inferential sensor; human review decides when the sensor output is a true design issue versus an acceptable trade-off.

## Integration Decisions

This page should stay source-level because it reports one article's experiment with one application, one stack, and a specific set of sensors. Its stable contribution is not “these exact tools are mandatory,” but the pattern of combining computational structure sensors with inferential modularity review.

The source strengthens these existing pages:

- [[wiki/concepts/Computational and Inferential Controls]] — maintainability shows why deterministic checks and semantic review need different roles.
- [[wiki/concepts/Feedforward and Feedback Controls]] — lint messages and dependency-rule errors become feedback that can steer agent self-correction.
- [[wiki/concepts/Verification Loop]] — maintainability checks can run inside the agent loop, pre-commit, CI, or periodic drift review.
- [[wiki/concepts/Harnessability]] — typed code, clear folders, dependency boundaries, scripts, and reviewable suppressions make a codebase easier to harness.
- [[wiki/topics/Testing Strategy]] — maintainability sensors broaden “testing” beyond functional checks into structural and modularity feedback.

Claims about specific tools should remain source-level unless corroborated by other sources. ESLint, dependency-cruiser, Semgrep, mutation testing, coupling analyzers, and AI modularity reviews are examples of sensor categories, not a universal stack. ^[inferred]

## Open Questions

- How should teams prevent maintainability sensors from producing noisy feedback overload?
- Which lint rules are genuinely AI-agent-specific rather than ordinary human-code quality rules?
- How should suppressions be governed so agents do not normalize real design debt?
- When should coupling data trigger automatic agent action, human review, or no action?
- How often should AI modularity review run before it becomes expensive design theater?

## Related

- [[wiki/sources/Harness Engineering Source Guide]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/concepts/Feedforward and Feedback Controls]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Harnessability]]
- [[wiki/concepts/Harness Ratchet]]
