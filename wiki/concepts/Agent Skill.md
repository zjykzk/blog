---
title: Agent Skill
type: concept
status: seed
category: concepts
summary: Agent Skill is a reusable capability bundle that can combine instructions, references, scripts, assets, memory, and hooks for agent work.
sources:
  - https://x.com/trq212/status/2033949937936085378
created: 2026-05-06T10:51:47+08:00
updated: 2026-05-06T10:51:47+08:00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-06
provenance:
  extracted: 0.72
  inferred: 0.28
  ambiguous: 0.0
aliases:
  - agent skills
  - AI skill
tags:
  - ai
  - agents
  - skills
  - workflow
---

# Agent Skill

An agent skill is not just a saved prompt. Thariq Shihipar's Claude Code article frames skills as folders that can contain instructions, reference files, scripts, assets, data, configuration, memory, and hooks that the agent can discover and use.

That makes a skill a reusable capability bundle: it can shape context, provide executable helpers, preserve local knowledge, and activate workflow-specific guardrails. ^[inferred]

## Durable Skill Shapes

The source groups useful Claude Code skills into recurring categories:

- library and API reference skills that capture internal SDKs, CLIs, examples, and gotchas
- product verification skills that drive the running product and assert behavior
- data and analysis skills that encode table names, dashboard IDs, query patterns, and metrics workflows
- business automation skills that turn multi-tool team routines into repeatable commands
- scaffolding and template skills that generate framework-correct boilerplate
- code quality and review skills that encode review, testing, and style methodology
- CI/CD and deployment skills that monitor, retry, deploy, smoke test, or roll back
- incident runbook skills that map symptoms to investigation paths
- infrastructure operation skills that guide cleanup, dependency, and cost workflows

The article's practical rule is that durable skills tend to fit cleanly into one category. Skills that straddle several categories are more likely to be confusing.

## Design Principles

- Do not spend skill context on defaults the model already knows.
- Put the highest-signal warnings in a gotchas section, and grow that section from repeated failures.
- Use progressive disclosure: the top-level skill should route to references, scripts, examples, templates, or assets only when needed.
- Avoid over-prescribing every shell step; specify intent and constraints so the agent can adapt to local state.
- Write the description field as trigger guidance for the model, not as a human-facing abstract.
- Cache setup answers when a skill needs stable user or environment configuration.
- Store durable plugin data outside the skill directory when the data should survive upgrades.
- Give the skill code when a deterministic helper can replace repeated reconstruction.
- Use on-demand hooks for session-scoped guardrails that should only apply during a specific workflow.

These principles connect directly to [[wiki/topics/AI Skills Workflow]]: a strong skill is a small operating surface for context, tools, memory, verification, and guardrails, not merely a paragraph of advice. ^[inferred]

## Marketplace Implication

Skills become team infrastructure when they are shared through repositories or plugin marketplaces. The article warns that scale creates a curation problem: teams need a way to notice useful skills, move them into shared distribution, and prevent redundant or low-quality skills from accumulating.

This connects to [[wiki/concepts/Encoding Team Standards]] because shared skills can carry team judgment in a reviewable, reusable form. ^[inferred]

## Open Questions

- Which skill categories are most valuable for solo knowledge work versus team software engineering? ^[inferred]
- How should a team measure whether a skill is improving outcomes rather than merely increasing context and tool surface? ^[inferred]

## Related

- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/sources/Claude Code Skills Source Guide]]
