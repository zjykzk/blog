---
title: Data Warehouse Bus Matrix
type: concept
status: draft
category: concepts
summary: The data warehouse bus matrix maps business processes against shared dimensions to plan an integrated Kimball-style enterprise warehouse.
tags:
  - database
  - data-warehouse
  - architecture
sources:
  - https://www.kimballgroup.com/wp-content/uploads/2013/08/2013.09-Kimball-Dimensional-Modeling-Techniques11.pdf
created: 2026-06-19T10:40:26+0800
updated: 2026-06-19T10:40:26+0800
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-06-19
tier: supporting
provenance:
  extracted: 0.84
  inferred: 0.16
  ambiguous: 0.00
relationships:
  - target: "[[wiki/topics/Dimensional Modeling]]"
    type: related_to
  - target: "[[wiki/concepts/Conformed Dimension]]"
    type: uses
---

# Data Warehouse Bus Matrix

The enterprise data warehouse bus matrix lays out business processes as rows and conformed dimensions as columns. Each business process corresponds to a potential dimensional model and fact table family; shared dimensions mark integration points.

## Role in Kimball architecture

Kimball's bus architecture decomposes the enterprise warehouse into business-process dimensional models that can be delivered incrementally while remaining integrated through [[wiki/concepts/Conformed Dimension|conformed dimensions]].

The matrix is both a planning artifact and an architectural control: it makes visible which processes exist, which dimensions they share, and where consistency must be governed.^[inferred]

## Related matrices

Kimball also mentions the opportunity/stakeholder matrix, which maps potential DW/BI opportunities against organizational stakeholders. Compared with the bus matrix, it is more about prioritization and buy-in than schema integration.^[inferred]

## Related

- [[wiki/topics/Dimensional Modeling]]
- [[wiki/concepts/Conformed Dimension]]
- [[wiki/sources/Kimball Dimensional Modeling Techniques Source Guide]]
