---
title: Agent Skill
type: concept
status: seed
category: concepts
summary: Agent Skill is a reusable capability bundle that can combine instructions, references, scripts, assets, memory, and hooks for agent work.
sources:
  - https://x.com/trq212/status/2033949937936085378
  - https://x.com/trq212/status/2027463795355095314
  - https://x.com/GoogleCloudTech/article/2033953579824758855
  - https://lavinigam.com/posts/adk-skill-design-patterns/
  - https://arxiv.org/abs/2604.27488
  - https://arxiv.org/abs/2605.07358v1
  - https://research.perplexity.ai/articles/designing-refining-and-maintaining-agent-skills-at-perplexity
  - https://engineering.block.xyz/blog/3-principles-for-designing-agent-skills
created: 2026-05-06T10:51:47+08:00
updated: 2026-07-04T13:49:20+0800
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-06
provenance:
  extracted: 0.86
  inferred: 0.14
  ambiguous: 0.00
aliases:
  - agent skills
  - AI skill
tags:
  - agents
  - skills
  - workflow
---
# Agent Skill

An agent skill is not just a saved prompt. Thariq Shihipar's Claude Code article frames skills as folders that can contain instructions, reference files, scripts, assets, data, configuration, memory, and hooks that the agent can discover and use.

That makes a skill a reusable capability bundle: it can shape context, provide executable helpers, preserve local knowledge, and activate workflow-specific guardrails.

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

[[wiki/sources/Seeing Like an Agent Source Guide]] adds why skills matter for action-space design: they can add functionality through progressive disclosure without adding another always-visible top-level tool. The model can read a skill file, follow references recursively, and discover task-specific context only when needed.

This makes skills a middle layer between static prompt context and explicit tool calls. They enlarge [[wiki/concepts/Agent Action Space]] while keeping the immediate tool menu smaller. ^[inferred]

## Marketplace Implication

Skills become team infrastructure when they are shared through repositories or plugin marketplaces. The article warns that scale creates a curation problem: teams need a way to notice useful skills, move them into shared distribution, and prevent redundant or low-quality skills from accumulating.

This connects to [[wiki/concepts/Encoding Team Standards]] because shared skills can carry team judgment in a reviewable, reusable form. ^[inferred]

## Content Design Patterns

[[wiki/sources/ADK Skill Design Patterns Source Guide]] adds a content-architecture taxonomy for SKILL.md files. It distinguishes five recurring patterns: Tool Wrapper, Generator, Reviewer, Inversion, and Pipeline.

The important shift is from file format to control problem. A skill may have the same container layout but behave differently depending on whether it is supplying domain conventions, enforcing an output template, applying a rubric, interviewing for missing context, or preserving step order with gates.

## Lifecycle View

[[wiki/sources/Agent Skills Survey Paper Source Guide]] adds a field-level lifecycle frame. A skill is not only a reusable instruction bundle; it is an artifact that must be represented, acquired, retrieved or selected, and later evolved.

The survey's formal view describes a skill as a bounded procedural artifact with a root instruction document, optional auxiliary resources, and applicability conditions. That strengthens the local definition: a skill has both a **body** that tells the agent how to act and a **routing boundary** that decides when the body should enter the workflow.

The lifecycle view also makes cleanup part of the concept. Skill systems can grow by adding new files, but mature skill infrastructure must also validate, revise, merge, deprecate, and retire skills as tasks, APIs, tools, and safety constraints change.

The article also makes the `description` field operationally important: it is the agent's routing surface for whether a skill is loaded at all. That connects skill authoring directly to [[wiki/topics/Tool Routing]]. ^[inferred]

## Determinism and Judgment Boundary

[[wiki/sources/Designing Refining and Maintaining Agent Skills at Perplexity Source Guide]] sharpens a skill's responsibility boundary: a skill should decide which parts of work must be deterministic and which parts should remain inferential.

Hard rules, repeated calculations, formatting constraints, and safety or verification gates belong in scripts, templates, checkers, or mandatory `SKILL.md` steps. Context interpretation, trade-off analysis, conversation, synthesis, exception handling, and generation remain LLM work.

[[wiki/sources/Block Agent Skills Design Principles Source Guide]] makes the same boundary operational through Block's Repo Readiness skill: scoring moved into a bash script with binary checks and fixed point values, while the agent explains failures, drafts tailored follow-up artifacts, and recommends priorities.

Block's formulation is a compact skill-design test: if a decision must be reproducible across runs or teams, remove it from the model; if it requires context interpretation, creation, or conversation, leave it to the agent under explicit constraints.

This makes a skill a boundary object between [[wiki/concepts/Computational and Inferential Controls]]: deterministic components supply the skeleton of repeatability, while model reasoning supplies adaptive fit to the current situation. ^[inferred]

The same source also frames a mature skill as a workflow catalyst rather than a one-shot tool. The skill should make intermediate outputs actionable by the agent: a diagnostic report should become repair context, a check result should become a plan, and a repeated failure should become a candidate gotcha, test, script, or harness update. ^[inferred]

Block calls this "design for the arc": for diagnostic, investigation, review, or readiness skills, the first output should become the agent's next input so the user can ask for explanation, remediation, or re-checking in the same session.

## Capability Boundaries and Self-Evolution

[[wiki/sources/Skills-Coach Paper Source Guide]] adds a behavioral optimization lens. A skill should be tested against generated standard, advanced, and boundary tasks, then improved through revised instructions, examples, constraints, or code helpers.

This shifts skill quality from static readability to task coverage: a skill is not mature merely because its `Skill.md` is well written; it must survive edge cases, anomalous inputs, and real execution artifacts.

The paper's [[wiki/concepts/Skill Self-Evolution]] loop also makes evaluation part of skill design. If repeated failures become revised instructions or code after comparative execution, a skill becomes an inspectable learning surface rather than a frozen prompt bundle.

## Person-Grounded Skills

[[wiki/sources/COLLEAGUE.SKILL Paper Source Guide]] adds the person-grounded case. A skill can be distilled from traces of a person or role, but the useful target is not identity replacement. The artifact should preserve selected capability, mental models, behavior boundaries, correction history, provenance, and lifecycle state.

This strengthens the distinction between craft and persona. In a colleague setting, the highest-value artifact is often the expert's review judgment, escalation thresholds, and decision heuristics; surface style is a separate behavior track that may be invoked, corrected, or withheld independently.

## Open Questions

- Which skill categories are most valuable for solo knowledge work versus team software engineering? ^[inferred]
- How should a team measure whether a skill is improving outcomes rather than merely increasing context and tool surface? ^[inferred]
- When does a composed skill become too broad and need to split into Tool Wrapper, Generator, Reviewer, Inversion, or Pipeline subskills? ^[inferred]
- How should automatically optimized skills be reviewed before they enter shared team infrastructure? ^[inferred]

## Related

- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/syntheses/Agent Skill × Context Management]] — synthesis
- [[wiki/concepts/Agent Action Space]]
- [[wiki/concepts/Agent Skill Design Patterns]]
- [[wiki/concepts/Skill Self-Evolution]]
- [[wiki/topics/Tool Routing]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/sources/Claude Code Skills Source Guide]]
- [[wiki/sources/Seeing Like an Agent Source Guide]]
- [[wiki/sources/Designing Refining and Maintaining Agent Skills at Perplexity Source Guide]]
- [[wiki/sources/Block Agent Skills Design Principles Source Guide]]
- [[wiki/sources/COLLEAGUE.SKILL Paper Source Guide]]
- [[wiki/syntheses/Agent Skill × Harness Ratchet]] — synthesis
