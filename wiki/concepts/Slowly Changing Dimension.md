---
title: Slowly Changing Dimension
type: concept
status: draft
category: concepts
summary: Slowly changing dimension techniques decide how a dimension preserves, overwrites, or exposes historical and current attribute values.
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
  - target: "[[wiki/concepts/Dimension Table]]"
    type: related_to
  - target: "[[wiki/concepts/Fact Table]]"
    type: related_to
---

# Slowly Changing Dimension

Slowly changing dimension (SCD) techniques handle dimension attributes that change over time. The design choice is not just technical storage; it decides whether BI users see the original value, the current value, the historically effective value, or multiple perspectives at once.^[inferred]

## Kimball SCD types

- Type 0: retain the original value.
- Type 1: overwrite the old value with the new value, destroying history.
- Type 2: add a new dimension row with a new surrogate key and effective/expiration dates plus a current-row indicator.
- Type 3: add a new attribute to preserve an old value while the main attribute is overwritten.
- Type 4: split rapidly changing attributes into a mini-dimension.
- Type 5: combine a mini-dimension with a current Type 1 outrigger so historical values and current mini-dimension values can both be accessed.
- Type 6: add current Type 1 attributes into a Type 2 dimension row so facts can be grouped by historical or current values.
- Type 7: place both durable key and surrogate key in the fact table so the same dimension supports Type 1 current and Type 2 historical views.

## Design pressure

SCD is a reporting-reality problem: business users often need both “as-was” and “as-is” views. Hybrid types exist because neither pure overwrite nor pure history is enough for many analytic questions.^[inferred]

## Related

- [[wiki/concepts/Dimension Table]]
- [[wiki/topics/Dimensional Modeling]]
- [[wiki/sources/Kimball Dimensional Modeling Techniques Source Guide]]
