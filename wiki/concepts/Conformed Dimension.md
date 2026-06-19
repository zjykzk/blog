---
title: Conformed Dimension
type: concept
status: draft
category: concepts
summary: A conformed dimension is shared consistently across fact tables so separate business processes can be compared or drilled across.
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
  - target: "[[wiki/concepts/Data Warehouse Bus Matrix]]"
    type: related_to
  - target: "[[wiki/concepts/Dimension Table]]"
    type: related_to
---

# Conformed Dimension

A conformed dimension is a dimension used consistently across fact tables so measures from different business processes can be compared, combined, or drilled across.

Kimball treats conformed dimensions as the integration mechanism of the enterprise data warehouse bus architecture. They let independently implemented business-process stars participate in one analytic system.

## Drilling across

Drilling across means querying separate fact tables and then merging the answer sets on shared row-header attributes from conformed dimensions. This avoids invalid fact-to-fact joins while still allowing cross-process analysis.

## Shrunken rollup dimensions

A shrunken rollup dimension is a conformed dimension subset that removes lower-level rows and/or attributes. It is useful when an aggregate fact table operates at a higher grain than the atomic star.

## Related

- [[wiki/concepts/Data Warehouse Bus Matrix]]
- [[wiki/concepts/Fact Table]]
- [[wiki/sources/Kimball Dimensional Modeling Techniques Source Guide]]
