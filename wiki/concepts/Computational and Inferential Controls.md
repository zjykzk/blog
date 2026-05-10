---
title: Computational and Inferential Controls
type: concept
status: seed
category: concepts
summary: Computational controls execute objective checks; inferential controls carry human or model judgment where correctness cannot be fully executable.
sources:
  - https://martinfowler.com/articles/harness-engineering.html
created: 2026-05-06T22:24:21+08:00
updated: 2026-05-06T22:24:21+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-06
provenance:
  extracted: 0.78
  inferred: 0.22
  ambiguous: 0.0
aliases:
  - computational controls
  - inferential controls
  - executable and judgment controls
tags:
  - agents
  - harness
  - testing
---
# Computational and Inferential Controls

Computational and inferential controls describe two kinds of control surfaces in a coding-agent harness.

Computational controls are executable checks. Inferential controls rely on judgment by a person, model, reviewer, or agent-readable rubric.

## Computational Controls

Computational controls include:

- tests
- type checks
- linters
- formatters
- builds
- reproducible scripts
- static or runtime checks

Their strength is that they can return a concrete signal to the [[wiki/concepts/Verification Loop]] without depending on another act of interpretation.

## Inferential Controls

Inferential controls include:

- design checklists
- architecture principles
- review rubrics
- examples of good and bad output
- human review comments
- evaluator-model judgments

They are necessary when correctness depends on fit, maintainability, taste, risk, product intent, or architectural coherence.

## Design Rule

When a property can be checked computationally, executable feedback is usually stronger than a prompt reminder. When a property cannot be fully checked computationally, the harness should make the needed judgment explicit and reusable. ^[inferred]

This links [[wiki/topics/Testing Strategy]] with [[wiki/concepts/Encoding Team Standards]]: tests cover executable truth, while standards and rubrics preserve senior judgment that cannot yet be reduced to a test.

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/concepts/Feedforward and Feedback Controls]]
- [[wiki/sources/Harness Engineering Source Guide]]
