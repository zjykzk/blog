---
title: Dimension Table
type: concept
status: draft
category: concepts
summary: A dimension table supplies descriptive context, labels, filters, and groupings for facts in a dimensional model.
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
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.00
relationships:
  - target: "[[wiki/topics/Dimensional Modeling]]"
    type: related_to
  - target: "[[wiki/concepts/Slowly Changing Dimension]]"
    type: related_to
---

# Dimension Table

A dimension table provides the descriptive context around a business process event: who, what, where, when, why, and how. Dimension attributes are used for filtering, grouping, row labels, and user-facing BI navigation.

Kimball says dimension tables are sometimes the “soul” of the data warehouse because they are the entry points and labels through which business users experience the warehouse.

## Shape

Dimension tables are usually wide, flat, denormalized tables with many low-cardinality text attributes. Operational codes and indicators can appear as attributes, but verbose descriptions are usually more useful for BI users.

## Keys

Kimball recommends surrogate integer primary keys for almost all dimensions because natural keys are controlled by operational systems, may be incompatible across sources, and may change. The date dimension is the main exception because it is stable and predictable enough to use a meaningful primary key.

Natural keys, durable keys, and surrogate keys play different roles: a durable key identifies the same business entity across time, while multiple surrogate keys may represent different historical profiles of that entity.

## Modeling tendencies

- Prefer denormalized flattened dimensions for fixed-depth hierarchies.
- Use role-playing dimensions when the same dimension appears in different roles, such as order date and ship date.
- Use junk dimensions for unrelated low-cardinality flags rather than producing many small dimensions.
- Avoid abstract generic dimensions such as one universal person or location dimension when different business roles have different attributes.

## Related

- [[wiki/concepts/Fact Table]]
- [[wiki/concepts/Slowly Changing Dimension]]
- [[wiki/sources/Kimball Dimensional Modeling Techniques Source Guide]]
