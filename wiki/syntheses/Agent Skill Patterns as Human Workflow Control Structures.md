---
title: Agent Skill Patterns as Human Workflow Control Structures
category: synthesis
tags: [ai, agents, workflow, skills, systems]
sources:
  - conversation:2026-05-07
created: 2026-05-07T13:57:16+08:00
updated: 2026-05-07T13:57:16+08:00
summary: Agent skill patterns translate ordinary human work controls—manuals, templates, reviews, interviews, and gates—into executable agent workflows.
provenance:
  extracted: 0.35
  inferred: 0.65
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-07
---

# Agent Skill Patterns as Human Workflow Control Structures

## Context

[[wiki/concepts/Agent Skill Design Patterns]] describes five SKILL.md content patterns: Tool Wrapper, Generator, Reviewer, Inversion, and Pipeline. These patterns are not only AI-specific tricks; they correspond to common control structures in ordinary human work. ^[inferred]

## Finding

Agent skill patterns translate human work routines into agent-readable workflow grammar. Human teams already use manuals, templates, checklists, interviews, and stage gates; skills make those structures explicit, loadable, reusable, and executable by an agent. ^[inferred]

The relationship is therefore deeper than “AI imitates human workflow.” A skill can encode the same control logic that human organizations use to reduce variation, prevent premature action, preserve order, and make judgment repeatable. ^[inferred]

## Pattern Mapping

| Agent skill pattern | Human workflow analogue | Control function |
| --- | --- | --- |
| Tool Wrapper | Expert handbook, team convention, internal operating guide | Make the worker consult the right norms before acting. |
| Generator | PRD template, report template, commit-message format, API-doc template | Keep output structure consistent across runs and authors. |
| Reviewer | Code review checklist, security audit rubric, editorial review standard | Turn judgment into repeatable criteria and severity-ranked findings. |
| Inversion | Requirements interview, diagnostic intake, consultant discovery call | Force context gathering before solution generation. |
| Pipeline | SOP, release process, staged project workflow, approval gate | Preserve sequence and prevent later stages from running before prerequisites are satisfied. |

## Reasoning

Tool Wrapper is the agent equivalent of “look up the team manual before doing the task.” It makes domain conventions available only when needed, similar to how a human specialist consults a standard, style guide, or internal playbook.

Generator is the agent equivalent of “use the approved template.” It reduces structural drift by separating the output frame from the content that fills it.

Reviewer is the agent equivalent of “review against a rubric.” It separates what counts as good from the process of inspecting the artifact, which makes review less dependent on intuition or reviewer mood. ^[inferred]

Inversion is the agent equivalent of “ask before solving.” It protects against the common failure mode where a worker or agent generates a detailed answer from an underdefined problem.

Pipeline is the agent equivalent of “follow the SOP and do not skip gates.” It treats order itself as part of correctness: validation, approval, and handoff points are not optional decoration but quality controls.

## Implications

Skill design can be understood as workflow engineering. The author is not merely writing instructions for a model; the author is deciding which human work control should be made explicit for the agent. ^[inferred]

This reframes skill selection around failure modes:

- If the failure is missing domain knowledge, use Tool Wrapper.
- If the failure is inconsistent output shape, use Generator.
- If the failure is weak judgment, use Reviewer.
- If the failure is premature assumption, use Inversion.
- If the failure is skipped process or missing validation, use Pipeline.

This also connects [[wiki/topics/AI Skills Workflow]] to ordinary organizational practice. A reusable skill is a way to convert tacit workflow knowledge into a durable operational artifact that can be shared, reviewed, improved, and re-run. ^[inferred]

## Related

- [[wiki/concepts/Agent Skill Design Patterns]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/topics/AI Harness]]
