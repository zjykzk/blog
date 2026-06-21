---
title: AI Harness × Testing Strategy
category: syntheses
type: synthesis
status: draft
tags: [agents, harness, testing, software-engineering]
sources:
  - wiki/topics/AI Harness
  - wiki/topics/Testing Strategy
  - wiki/concepts/Agentic Engineering
  - wiki/concepts/Computational and Inferential Controls
  - wiki/concepts/Harnessability
  - wiki/concepts/Verification Loop
  - wiki/sources/Coding with AI Source Guide
created: 2026-05-23T02:28:40+08:00
updated: 2026-06-09T10:56:14+08:00
summary: In AI coding, testing strategy becomes harness design: tests are runtime feedback surfaces, not only post-implementation QA.
provenance:
  extracted: 0.22
  inferred: 0.70
  ambiguous: 0.08
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-23
---
# AI Harness × Testing Strategy

## The Connection

[[wiki/topics/AI Harness]] governs the runtime order around an agent: context, tools, permissions, memory, feedback, and recovery. [[wiki/topics/Testing Strategy]] decides which truth signals should exist for software quality.

In AI-assisted development, these are no longer separate concerns. Tests become part of the harness because they decide whether the agent can correct itself before human review. ^[inferred]

## Where They Co-occur

This pair appears in the AI coding and quality cluster:

- [[wiki/concepts/Verification Loop]] treats tests, visual checks, and evaluators as feedback surfaces inside the harness.
- [[wiki/concepts/Computational and Inferential Controls]] separates executable checks from semantic review.
- [[wiki/concepts/Harnessability]] treats runnable tests and explicit conventions as properties that make a workflow easier to harness.
- [[wiki/concepts/Agentic Engineering]] frames senior engineers as trainers of harnesses rather than approvers of every diff.
- [[wiki/sources/Coding with AI Source Guide]] names verification speed as the bottleneck after generation becomes cheap.
- [[wiki/sources/Team AI Coding Harness Seminar Source Guide]] frames TDD as a team-level AI coding loop.

## Cross-cutting Insight

Testing strategy becomes more valuable when it moves from a coverage artifact to a control interface. ^[inferred]

In human-only coding, tests mainly increase confidence in changes. In AI coding, tests also shape the agent's next action. A failing test can become a repair prompt; a missing test becomes missing feedback; an ambiguous acceptance condition becomes a harness blind spot. ^[inferred]

Therefore the AI-era testing question is not only “what should be tested?” but “where should this test signal enter the agent loop?” Unit tests, contract tests, visual checks, mutation tests, lint rules, and review rubrics have different value depending on whether they run during generation, pre-commit, CI, or periodic drift review. ^[inferred]

## Tensions and Trade-offs

- **Executable truth vs. product judgment**: tests can assert behavior but may not reveal whether the right problem was solved.
- **Early feedback vs. maintenance burden**: moving checks earlier improves repair loops but increases local harness complexity.
- **Agent-generated tests vs. independent verification**: agents can create tests quickly, but tests generated from the same misunderstanding may certify the wrong behavior.
- **Coverage vs. confidence**: AI-generated code can increase lines and tests without increasing real assurance.

## Open Questions

- Which testing layers should be mandatory before an AI agent is allowed to modify production code?
- How should teams separate tests that guide generation from tests that independently verify acceptance?
- Can test failures be mined automatically into better prompts, rules, or harness sensors without overfitting?

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/concepts/Harnessability]]
- [[wiki/syntheses/Quality Engineering Three Generators]]
