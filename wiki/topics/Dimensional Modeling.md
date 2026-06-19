---
title: Dimensional Modeling
type: topic
status: growing
category: topics
summary: Dimensional modeling organizes analytic data around business processes, declared grain, dimensions, and facts so BI queries stay understandable and performant.
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
  - target: "[[wiki/concepts/Fact Table]]"
    type: uses
  - target: "[[wiki/concepts/Dimension Table]]"
    type: uses
  - target: "[[wiki/concepts/Data Warehouse Bus Matrix]]"
    type: uses
---

# Dimensional Modeling

Dimensional modeling is Kimball's design approach for DW/BI systems: choose a business process, declare the grain, identify dimensions, and identify facts. The model is not driven by a single report, but by measurement events from business processes and the descriptive context needed to analyze them.

## Core design loop

1. Select the [[wiki/topics/Dimensional Modeling|business process]] being measured, such as taking an order, processing a claim, or snapshotting an account each month.
2. Declare the [[wiki/concepts/Dimensional Design Grain|grain]] before choosing dimensions or facts.
3. Identify [[wiki/concepts/Dimension Table|dimensions]] that provide the who, what, where, when, why, and how context.
4. Identify [[wiki/concepts/Fact Table|facts]] that measure the process at the declared grain.

The order matters: grain acts as the contract that decides which dimensions and facts are legal.

## Why the model is business-first

Kimball frames dimensional design as a collaborative workshop with business subject matter experts, data governance representatives, data modelers, source-system experts, and profiling evidence. Requirements and source-data reality have to meet in the same design process.

This makes dimensional modeling a requirements-to-data-architecture bridge: it starts from business processes and KPIs, but it ends in physical schema choices such as star schemas, OLAP cubes, aggregate tables, and ETL rules.^[inferred]

## Stability and extension

Kimball emphasizes graceful extensions: add facts consistent with the current grain, add fact-table foreign keys for new dimensions if they do not alter the grain, add dimension attributes, or restate a fact table at a more atomic grain while preserving existing names.

The structural rule is: extend the model without breaking existing BI queries or changing previous query results.

## Related

- [[wiki/sources/Kimball Dimensional Modeling Techniques Source Guide]] — source-level guide to the 2013 Kimball technique catalog.
- [[wiki/concepts/Data Warehouse Bus Matrix]] — enterprise integration tool for arranging business processes and conformed dimensions.
- [[wiki/maps/CS Map]] — database and systems entry point.
