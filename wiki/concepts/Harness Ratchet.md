---
title: Harness Ratchet
type: concept
status: seed
category: concepts
summary: A harness ratchet turns repeated agent failures into durable rules, hooks, checks, or workflow changes instead of treating them as one-off bad runs.
sources:
  - https://addyosmani.com/blog/agent-harness-engineering/
  - https://martinfowler.com/articles/reduce-friction-ai/feedback-flywheel.html
  - https://martinfowler.com/articles/harness-engineering.html
  - https://arxiv.org/abs/2603.28052
created: 2026-05-05T15:10:00+08:00
updated: 2026-05-09T22:42:07+08:00
base_confidence: 0.83
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.76
  inferred: 0.24
  ambiguous: 0.0
aliases:
  - agent harness ratchet
  - failure-to-rule loop
tags:
  - agents
  - harness
  - feedback
---
# Harness Ratchet

A harness ratchet is the discipline of treating an agent mistake as a permanent signal for improving the [[wiki/topics/AI Harness]].

The core move is simple: when an agent fails in a repeatable way, the team changes the harness so that failure becomes less likely next time.

## What Gets Ratcheted

Addy Osmani's article gives concrete examples of failures becoming harness changes:

- missing repository conventions become shorter, sharper `AGENTS.md` rules
- unsafe shell behavior becomes a blocking hook or approval gate
- premature task completion becomes a continuation loop or clearer done condition
- broken generated code becomes typecheck, lint, test, or reviewer feedback inside the loop
- noisy tool choice becomes a smaller and more focused tool surface

The ratchet is strongest when every rule traces back to a real failure, not a speculative style preference.

[[wiki/concepts/Feedback Flywheel]] adds the human-team version of the same loop: review comments, regeneration cycles, accepted outputs, and post-merge rework should become updates to priming documents, standards, workflows, or checks.

The useful distinction is scope. Harness ratchet focuses on the runtime around an agent; feedback flywheel focuses on the collaboration system around AI-assisted development. ^[inferred]

[[wiki/sources/Harness Engineering Source Guide]] gives the ratchet a control vocabulary. A repeated failure can be absorbed as a [[wiki/concepts/Feedforward and Feedback Controls|feedforward control]], a feedback control, a computational check, or an inferential rubric.

That means the ratchet should not default to "add another instruction." Sometimes the stronger move is to add an executable test, expose a better template, or make review criteria visible to the agent and the human reviewer. ^[inferred]

## Why It Matters

This turns agent engineering from prompt tweaking into feedback-driven system design.

The model may improve over time, but the local harness still has to encode project-specific constraints, failure history, permissions, verification surfaces, and workflow defaults.

That makes the harness ratchet a learning loop for the system around the model, not for the model weights themselves. ^[inferred]

## Design Implication

A good ratchet has two sides:

- add constraints when real failures reveal missing structure
- remove constraints when stronger models or better primitives make them redundant

If only the first side exists, the harness can accumulate stale rules and context overhead. If only the second side exists, the system forgets the failures that shaped its reliability. ^[inferred]

## Automated Ratchet Variant

[[wiki/sources/Meta-Harness Paper Source Guide]] adds an automated variant of the ratchet. Meta-Harness stores candidate harness code, scores, and execution traces, then uses a coding-agent proposer to inspect prior failures and write a new harness candidate.

The difference from a manual ratchet is not the learning target but the actor. The durable artifact is still harness code, context policy, retrieval logic, memory update behavior, or orchestration logic; the outer loop delegates more diagnosis and proposal work to an agent. ^[inferred]

The paper's ablation is a warning for ratchet design: if failure history is compressed into scalar scores or short summaries, the proposer loses diagnostic signal. A useful ratchet needs raw enough traces for credit assignment, plus cheap validation before expensive evaluation.

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Agent Tool]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/concepts/Feedforward and Feedback Controls]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/Agent Harness Engineering Source Guide]]
- [[wiki/sources/Harness Engineering Source Guide]]
