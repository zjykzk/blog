---
title: Fact Table
type: concept
status: draft
category: concepts
summary: A fact table stores measurements from a business process event plus the dimensional keys needed to analyze those measurements.
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
  extracted: 0.86
  inferred: 0.14
  ambiguous: 0.00
relationships:
  - target: "[[wiki/concepts/Dimensional Design Grain]]"
    type: uses
  - target: "[[wiki/concepts/Dimension Table]]"
    type: uses
---

# Fact Table

A fact table contains numeric measures produced by a real-world business process event. At the lowest grain, a fact-table row corresponds to one measurement event, plus foreign keys to associated [[wiki/concepts/Dimension Table|dimension tables]].

## Fact categories

Kimball separates numeric facts by additivity:

- Additive facts can be summed across all related dimensions.
- Semi-additive facts can be summed across some dimensions but not all; account balances are common examples because they are not additive across time.
- Non-additive facts, such as ratios, should often be decomposed into additive components and calculated later in the BI layer or OLAP cube.

## Core fact table patterns

- Transaction fact table: one row per measurement event at a point in space and time.
- Periodic snapshot fact table: one row summarizing activity over a standard period.
- Accumulating snapshot fact table: one row tracking predictable process milestones from beginning to end.
- Factless fact table: one row records that dimensional entities came together even when there is no numeric measure.
- Aggregate fact table or cube: a rollup of atomic facts used only for query performance.
- Consolidated fact table: combines facts from multiple processes when they share the same grain.

## Hard rule: avoid fact-to-fact joins

A BI application should not join two fact tables directly across shared foreign keys because cardinality becomes uncontrollable and results become incorrect. Kimball recommends drilling across: create separate answer sets and sort-merge them on common row-header attributes.

## Related

- [[wiki/concepts/Dimensional Design Grain]]
- [[wiki/topics/Dimensional Modeling]]
- [[wiki/sources/Kimball Dimensional Modeling Techniques Source Guide]]
