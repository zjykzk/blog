---
title: Harness Ratchet × Feedback Flywheel
category: synthesis
tags:
  - agents
  - harness
  - feedback
  - workflow
sources:
  - wiki/concepts/Harness Ratchet.md
  - wiki/concepts/Feedback Flywheel.md
  - wiki/concepts/Feedforward and Feedback Controls.md
  - wiki/concepts/AI Collaboration Scaffolding.md
  - wiki/sources/Compounding Engineering Source Guide.md
  - wiki/sources/Agent Harness Engineering Survey Source Guide.md
  - wiki/sources/LLM Wiki Source Guide.md
created: 2026-06-09T14:38:22+08:00
updated: 2026-06-09T14:38:22+08:00
summary: Harness ratchets and feedback flywheels are complementary maintenance loops: one hardens the agent runtime, the other updates the broader collaboration system.
provenance:
  extracted: 0.25
  inferred: 0.70
  ambiguous: 0.05
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-06-09
---

# Harness Ratchet × Feedback Flywheel

## The Connection

[[wiki/concepts/Harness Ratchet]] and [[wiki/concepts/Feedback Flywheel]] both convert experience into durable system change, but they act at different boundaries. The ratchet hardens the immediate agent runtime: rules, hooks, checks, tool surfaces, done conditions, and orchestration. The flywheel updates the broader collaboration system: priming docs, team standards, workflow rules, context anchors, review habits, and guardrails. ^[inferred]

## Where They Co-occur

They co-occur in [[wiki/concepts/Feedforward and Feedback Controls]], [[wiki/concepts/AI Collaboration Scaffolding]], and source guides about compounding engineering, LLM Wiki, and agent harness engineering.

The recurring context is maintenance after real AI-assisted work: review comments, failed tests, repeated regeneration, post-merge rework, and agent trace data.

## Cross-cutting Insight

The distinction is blast radius. A harness ratchet changes how the agent acts; a feedback flywheel changes how the team collaborates with AI. ^[inferred]

A mature AI engineering system needs both. If all learning goes into the harness, team norms and product context stay tacit. If all learning stays in collaboration docs, the runtime keeps making avoidable mistakes that could have been prevented by hooks, checks, or tool redesign. ^[inferred]

## Tensions and Trade-offs

- Harness changes can be enforceable but may be too rigid for judgment-heavy work.
- Flywheel updates can preserve judgment but may remain advisory unless translated into executable checks or routed skills.
- Both loops can accumulate stale rules; both need pruning, ownership, and evidence thresholds.

## Open Questions

- What evidence threshold should promote a lesson from flywheel documentation into a harness ratchet? ^[inferred]
- Who owns pruning when a rule appears both in team standards and harness instructions? ^[inferred]
- How can trace systems show whether a change improved agent behavior or merely moved effort to humans? ^[inferred]

## Related

- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/concepts/Feedforward and Feedback Controls]]
- [[wiki/concepts/AI Collaboration Scaffolding]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/syntheses/Verification Loop × Feedback Flywheel]]
