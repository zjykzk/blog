---
title: Dimensional Design Grain
type: concept
status: draft
category: concepts
summary: Grain is the binding declaration of what one fact-table row represents, and it constrains every dimension and fact that can legally appear.
tags:
  - database
  - data-warehouse
  - modeling
sources:
  - https://www.kimballgroup.com/wp-content/uploads/2013/08/2013.09-Kimball-Dimensional-Modeling-Techniques11.pdf
created: 2026-06-19T10:40:26+0800
updated: 2026-06-19T10:40:26+0800
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-06-19
tier: supporting
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
relationships:
  - target: "[[wiki/topics/Dimensional Modeling]]"
    type: related_to
  - target: "[[wiki/concepts/Fact Table]]"
    type: related_to
---

# Dimensional Design Grain

Grain is the declaration of exactly what a single [[wiki/concepts/Fact Table|fact table]] row represents. Kimball calls it the pivotal design step because dimensions and facts must be chosen only after the grain is explicit.

## Binding contract

A grain declaration is a binding contract on the design:

- every candidate [[wiki/concepts/Dimension Table|dimension]] must be single-valued and meaningful at that grain;
- every candidate fact must measure something at that grain;
- different grains should not be mixed in the same fact table.

## Atomic grain first

Kimball strongly recommends starting from atomic-grained data, the lowest level at which the business process captures data. Summary grains are useful for performance tuning, but they pre-suppose common questions; atomic grain survives unpredictable query patterns better.

## Design consequence

Grain is the dimensional-modeling version of a system boundary: once it is declared, it decides what can be attached without corrupting the model.^[inferred]

## Related

- [[wiki/topics/Dimensional Modeling]]
- [[wiki/concepts/Fact Table]]
- [[wiki/sources/Kimball Dimensional Modeling Techniques Source Guide]]
