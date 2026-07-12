---
title: Agentic Coding Unknowns
category: concepts
tags:
  - agents
  - ai-coding
  - workflow
  - context
sources:
  - https://x.com/trq212/article/2073100352921215386
relationships:
  - target: "[[wiki/topics/AI Skills Workflow]]"
    type: related_to
  - target: "[[wiki/concepts/Agentic Engineering]]"
    type: related_to
  - target: "[[wiki/concepts/Coding Agent User Harness]]"
    type: related_to
created: 2026-07-04T16:59:13+0800
updated: 2026-07-04T16:59:13+0800
summary: Agentic coding unknowns are the gaps between a user's prompt-map and the real codebase-territory that an agent must either clarify or guess through.
provenance:
  extracted: 0.76
  inferred: 0.24
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-07-04
tier: supporting
---
# Agentic Coding Unknowns

Agentic coding unknowns are the gaps between the map a user gives an agent and the territory where the work actually happens. The map is prompts, skills, context, plans, specs, and reference artifacts. The territory is the codebase, product, domain, users, runtime constraints, and real-world feedback.

When an agent reaches one of these gaps, it must either ask, inspect the territory, or guess. Thariq Shihipar's Fable article argues that stronger long-horizon models make this gap more visible: the bottleneck moves from raw model capability toward the user's ability to surface and clarify unknowns.

## Four Classes

- **Known knowns** are the things already stated in the prompt: the explicit request, constraints, and desired outcome.
- **Known unknowns** are the questions the user already knows are unresolved.
- **Unknown knowns** are tacit preferences or criteria the user can recognize when shown a prototype but cannot easily specify in advance.
- **Unknown unknowns** are missing considerations the user has not yet imagined, such as hidden codebase constraints, domain standards, or quality bars.

This taxonomy matters because each unknown type calls for a different discovery artifact, not just a longer prompt. ^[inferred]

## Discovery Artifacts

A blind spot pass asks the agent to inspect a domain or codebase and explain what the user is likely missing. It is especially useful when unknown unknowns dominate.

Brainstorms and prototypes expose unknown knowns by giving the user concrete alternatives to react to before implementation cost accumulates.

Interviews surface known unknowns by asking one question at a time, especially questions where the answer would change architecture, data models, or user-facing behavior.

References reduce ambiguity when language is too weak. Source code is often the strongest reference because it carries behavior, structure, edge cases, and implementation semantics.

Implementation plans should lead with decisions likely to change, while burying mechanical refactors the user already trusts the agent to perform.

Implementation notes preserve deviations, conservative choices, and edge cases discovered mid-run so the next attempt starts with a better map.

Post-implementation explainers and quizzes make the final territory understandable to reviewers and maintainers, not only to the agent that performed the change.

## Relation to Agentic Engineering

[[wiki/concepts/Agentic Engineering]] usually emphasizes verification loops, harness design, and human judgment allocation. Agentic coding unknowns add an earlier and more continuous responsibility: the human-agent pair must actively discover where the prompt-map is under-specified before a model's plausible guess becomes code.

This also connects to [[wiki/concepts/Coding Agent User Harness]]. Unknown-discovery artifacts are harness components: they shape what the agent sees, when it may proceed, when it should ask, and how lessons from one attempt become context for the next attempt. ^[inferred]

## Failure Modes

- Over-specific instructions can trap the agent on a path even when implementation evidence suggests a pivot.
- Vague instructions can cause the agent to substitute generic industry practice for local project fit.
- Planning-only workflows miss unknowns that appear only after the agent reads code, runs checks, or hits edge cases.
- Diff-only review gives the user weak understanding when behavior depends on existing hidden code paths.

## Related

- [[wiki/sources/Agentic Coding Unknowns Source Guide]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/concepts/Agentic Engineering]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/concepts/Context Anchoring]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/syntheses/AI Engineering Workflow]]
