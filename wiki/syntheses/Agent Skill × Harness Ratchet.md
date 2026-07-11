---
title: Agent Skill × Harness Ratchet
category: synthesis
tags:
  - agents
  - skills
  - harness
  - feedback
sources:
  - wiki/concepts/Agent Skill.md
  - wiki/concepts/Harness Ratchet.md
  - wiki/concepts/Skill Self-Evolution.md
  - wiki/concepts/Continual Learning for AI Agents.md
  - wiki/sources/Skills-Coach Paper Source Guide.md
  - wiki/sources/Continual Learning for AI Agents Source Guide.md
  - wiki/sources/Agent Engineering Source Guide.md
  - wiki/sources/GEPA Paper River Source Guide.md
created: 2026-06-09T14:38:22+08:00
updated: 2026-07-12T00:07:31+0800
summary: Skills become ratchet surfaces when repeated agent failures are converted into revised instructions, examples, constraints, scripts, or evaluable helper code.
provenance:
  extracted: 0.59
  inferred: 0.41
  ambiguous: 0.00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-06-09
---

# Agent Skill × Harness Ratchet

## The Connection

[[wiki/concepts/Agent Skill]] is a reusable capability bundle; [[wiki/concepts/Harness Ratchet]] is the discipline of turning repeated failures into durable changes around an agent. Their intersection is the skill as a ratchet surface: failures can become revised instructions, sharper gotchas, better examples, templates, scripts, or executable helpers. ^[inferred]

This makes a skill more than documentation. It becomes one of the places where an agent system remembers how it has failed and what it learned from those failures. ^[inferred]

## Where They Co-occur

They co-occur in [[wiki/concepts/Skill Self-Evolution]], [[wiki/concepts/Continual Learning for AI Agents]], and source guides about Skills-Coach, GEPA, LLM Wiki, agent engineering, and structured memory.

The common situation is a workflow that repeatedly needs the same operational judgment: when to use a tool, how to format an output, what edge cases to check, when to ask for clarification, or how to recover from failure. ^[inferred]

## Cross-cutting Insight

A harness ratchet does not always need to modify harness code. If the failure is task-specific, domain-specific, or workflow-specific, the right durable artifact may be a skill. ^[inferred]

That creates a useful placement rule: put universal runtime constraints into the harness; put reusable workflow judgment into skills; put project-local facts into repository context or memory. ^[inferred]

The skill itself should preserve a second boundary: repeated calculations, fixed scoring, formatting constraints, and mandatory gates move into scripts or checkers, while interpretation, exception handling, and synthesis remain model work. This prevents a ratchet from hardening probabilistic judgment into an unreliable instruction while still making reproducible parts executable. ^[inferred]

“Design for the arc” extends the ratchet beyond one invocation: a diagnostic result becomes repair context, a failed check becomes a plan input, and a recurring failure becomes a candidate gotcha, test, script, or harness change. The skill is therefore both an execution surface and a routing point into the next improvement loop. ^[inferred]

## Tensions and Trade-offs

- Skills are easier to update than harness code, but they add routing and context overhead. ^[inferred]
- A skill can preserve learned judgment, but if it accumulates every failure as another warning, it becomes noisy and harder to route. ^[inferred]
- Automated skill evolution can propose improvements, but those changes still need a [[wiki/concepts/Verification Loop]] before entering shared use. ^[inferred]

## Open Questions

- When should a repeated failure become a skill update rather than a hook, test, or harness-code patch? ^[inferred]
- How should skill repositories merge duplicate ratchets that encode the same lesson in different words? ^[inferred]
- What tests prove that a skill update improved behavior instead of merely increasing instruction length? ^[inferred]

## Related

- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Skill Self-Evolution]]
- [[wiki/concepts/Continual Learning for AI Agents]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/syntheses/Agent Skill × Context Management]]
