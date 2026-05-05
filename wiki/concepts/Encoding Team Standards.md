---
title: Encoding Team Standards
type: concept
status: seed
category: concepts
summary: Encoding team standards turns tacit engineering judgment into versioned AI instructions that execute consistently across the team.
sources:
  - https://martinfowler.com/articles/reduce-friction-ai/encoding-team-standards.html
created: 2026-05-05T17:45:00+08:00
updated: 2026-05-05T17:45:00+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.86
  inferred: 0.14
  ambiguous: 0.0
aliases:
  - executable team standards
  - AI team standards
  - executable governance
tags:
  - ai
  - ai-coding
  - software-engineering
  - workflow
---

# Encoding Team Standards

Encoding team standards is the practice of turning tacit engineering judgment into versioned AI instructions that execute consistently across a team.

Rahul Garg's [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]] frames the problem as inconsistency: two developers can use the same AI, same codebase, and same project context but get materially different results because they prompt with different levels of team judgment.

## Consistency Problem

Senior engineers often carry implicit standards for generation, refactoring, security, and review. They know which error-handling pattern to apply, when an abstraction is premature, which authorization checks are mandatory, and what makes a pull request unacceptable.

Junior developers may ask the same assistant for "create a service" or "check if this is secure" without encoding those quality gates. The resulting gap is not only a training problem; it is a distribution problem. The team already has the knowledge, but it has no reliable vehicle for consistent application.

This pattern is different from [[wiki/concepts/Knowledge Priming]]. Priming tells the assistant how the project works; encoded standards tell the assistant how the team judges work.

## Executable Governance

The article's key move is from documentation to execution. A wiki checklist depends on someone reading, remembering, and applying it. An AI instruction applies the standard as part of the workflow.

Garg compares this to lint rules, CI pipelines, and infrastructure-as-code: the useful artifact is not a page that informs behavior, but configuration that executes behavior.

That makes executable team standards a companion to [[wiki/topics/Karpathy Guidelines]]: local coding rules become shared infrastructure instead of an individual operator's memory. ^[inferred]

## Instruction Anatomy

The article describes four parts of a well-structured instruction:

- Role definition: set the expertise level and perspective.
- Context requirements: specify what project context, code, constraints, or inputs the instruction needs.
- Categorized standards: separate blockers, must-fix issues, preferences, advisories, or other priority levels.
- Output format: make results comparable across developers and runs.

The priority structure matters because it encodes judgment, not just knowledge. A security instruction, for example, should distinguish critical vulnerabilities from important concerns and advisories.

Instructions should stay small and single-purpose. Separate generation, refactoring, security, and review instructions are easier to maintain and compose than one large prompt that tries to govern everything.

## Workflow Placement

Encoded standards can appear at several workflow points:

- Generation time: make new code follow architecture, naming, error handling, and testing expectations from the first pass.
- During development: guide refactoring and security checks with the team's own threat model and refactoring philosophy.
- Review time: apply the team's quality gate consistently.
- CI time: optionally run fast, predictable checks as an automated consistency gate.

Earlier placement has more leverage because it prevents misalignment instead of only catching it at review.

## Shared Infrastructure

A personal prompt is a productivity trick. A prompt or skill in the repository is team infrastructure.

When standards live in the repo, they gain the same operational properties as other shared artifacts: changes are tracked, improvements happen through pull requests, drift is visible, and ownership becomes collective.

The closest connection to [[wiki/concepts/Context Anchoring]] is maintenance: both patterns move important AI collaboration state out of individual chats and into versioned artifacts that can survive session boundaries. ^[inferred]

## Calibration

This pattern is most valuable when AI-assisted output varies noticeably by who is prompting, or when generation and review work routes through a few people because they know how to ask the assistant well.

The costs are real: extraction interviews, drafting, iteration, false positives, over-prescription, and ongoing maintenance. Garg recommends starting with one high-value instruction, usually generation or review, then adding more only after adoption.

## Lattice Example

The article's Lattice sidebar encodes this practice as composable atoms such as `clean-code`, `architecture`, `domain-driven-design`, `secure-coding`, and `test-quality`, each with self-validation checklists.

Refiners let teams customize defaults through guided interviews, producing a versioned standards document that every skill reads. This strengthens [[wiki/topics/AI Skills Workflow]]: a skill can carry team judgment, not just task sequence or project context. ^[inferred]

## Related

- [[wiki/concepts/AI Collaboration Scaffolding]]
- [[wiki/concepts/Knowledge Priming]]
- [[wiki/concepts/Context Anchoring]]
- [[wiki/topics/Karpathy Guidelines]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]]
