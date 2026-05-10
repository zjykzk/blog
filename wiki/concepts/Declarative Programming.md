---
title: Declarative Programming
category: concepts
tags:
  - frontend
  - programming
  - abstraction
sources:
  - wiki/sources/React Framework Background and Core Concepts Source Guide.md
created: 2026-05-05
updated: 2026-05-10T16:08:56+08:00
base_confidence: 0.40
lifecycle: draft
lifecycle_changed: 2026-05-05
type: concept
status: seed
summary: Declarative programming describes a target state or relation rather than spelling out each mutation step.
aliases:
  - declarative style
---

# Declarative Programming

Declarative programming shifts attention from step-by-step update procedures to the desired result or state.

In UI development, this means describing what the interface should look like for a given state, while the framework manages the concrete update path.

Declarative style reduces manual mutation code, but it does not remove the need to model state and transitions carefully. ^[inferred]

## React connection

React is a high-impact frontend example of declarative programming: components describe UI as a function of state, and React coordinates the DOM updates needed to make that description real.

## Related

- [[wiki/concepts/React]]
- [[wiki/concepts/State Management]]
- [[wiki/topics/Frontend Development]]
- [[wiki/syntheses/React UI Organization Model]]
- [[wiki/sources/React Framework Background and Core Concepts Source Guide]]
