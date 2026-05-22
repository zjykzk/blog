---
title: Agent Skill Design Patterns
type: concept
status: seed
category: concepts
summary: Agent Skill Design Patterns classify SKILL.md content by the control problem it solves: knowledge, structure, review, questioning, or workflow gates.
sources:
  - https://x.com/GoogleCloudTech/article/2033953579824758855
  - https://lavinigam.com/posts/adk-skill-design-patterns/
created: 2026-05-07T12:44:36+08:00
updated: 2026-05-07T12:44:36+08:00
base_confidence: 0.53
lifecycle: draft
lifecycle_changed: 2026-05-07
provenance:
  extracted: 0.76
  inferred: 0.24
  ambiguous: 0.0
aliases:
  - SKILL.md design patterns
  - ADK skill design patterns
  - skill patterns
tags:
  - agents
  - skills
  - workflow
---
# Agent Skill Design Patterns

Agent skill design patterns are reusable structural templates for organizing `SKILL.md` content. The article's core claim is that the SKILL.md packaging problem is mostly solved by the shared format, while the harder problem is how to structure the logic inside the skill.

The useful design axis is not “what files does a skill contain?” but “what control problem does this skill solve for the agent?” ^[inferred]

## Five Patterns

| Pattern      | Control problem                                                  | Typical resources                                  | Use when                                                                               |
| ------------ | ---------------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Tool Wrapper | Put domain conventions behind an on-demand context surface       | `references/`                                      | The agent must apply a library, SDK, internal system, or team convention consistently. |
| Generator    | Make output shape repeatable                                     | `assets/` plus `references/`                       | The output must follow a fixed template, style guide, or document structure.           |
| Reviewer     | Separate evaluation criteria from review protocol                | `references/`                                      | Code, content, or artifacts need checklist-based scoring and severity grouping.        |
| Inversion    | Prevent premature generation by making the agent interview first | often `assets/`                                    | The agent needs missing user context before useful action is possible.                 |
| Pipeline     | Preserve ordered execution with explicit gates                   | `references/`, `assets/`, and sometimes `scripts/` | The workflow has dependent stages where skipping validation would corrupt the result.  |

## Pattern Logic

Tool Wrapper skills treat knowledge as on-demand operational context. The skill description should contain the actual trigger vocabulary users type, and the detailed rules should live in references that load only after activation.

Generator skills treat output structure as an external artifact. The instructions coordinate template loading, style-guide loading, missing-input collection, and final template filling.

Reviewer skills treat judgment as a rubric. The checklist holds what to check; the top-level skill defines how to read the artifact, classify severity, explain the issue, and propose fixes.

Inversion skills treat the user's missing context as the bottleneck. Their key mechanism is a non-negotiable gate that forbids building or synthesizing until the interview phases are complete.

Pipeline skills treat order as part of correctness. Their instructions define stage boundaries, failure conditions, validation points, and handoffs between references, assets, scripts, and user confirmations.

## Composition

The source explicitly says the patterns compose: a Pipeline can include a Reviewer step, a Generator can use Inversion to gather inputs, and a Tool Wrapper can be embedded as a reference inside a larger workflow.

This makes the five patterns closer to “workflow operators” than mutually exclusive categories. A mature skill may combine several operators, but it should still have one dominant control problem so the trigger, resources, and success criteria stay legible. ^[inferred]

## Design Heuristics

- Start with Tool Wrapper when the skill's main job is to teach the agent a bounded domain.
- Use Generator when consistency of output shape matters more than creativity.
- Use Reviewer when the value is stable judgment against a checklist.
- Use Inversion when the main failure mode is assumption-driven action.
- Use Pipeline when the main failure mode is skipped steps or missing checkpoints.
- Treat the `description` field as the routing API: vague descriptions make the agent fail to load the skill at the right time.
- Evaluate a skill by comparing task pass rate with and without the skill, not by whether the skill looks well structured.

## Relationship to Existing Wiki

This page refines [[wiki/concepts/Agent Skill]] by separating the skill container from the internal content architecture.

It also strengthens [[wiki/topics/AI Skills Workflow]]: a workflow skill is not merely a checklist, but a context-and-control structure that decides what the agent knows, asks, reviews, generates, and validates at each stage. ^[inferred]

## Open Questions

- Which pattern combinations produce the best reliability/cost tradeoff for personal engineering workflows? ^[inferred]
- How should a skill author decide when a Pipeline has become too large and should split into multiple skills? ^[inferred]

## Related

- [[wiki/concepts/Agent Skill]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/Tool Routing]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/sources/ADK Skill Design Patterns Source Guide]]
