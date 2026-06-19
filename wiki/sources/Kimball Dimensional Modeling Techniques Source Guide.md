---
title: Kimball Dimensional Modeling Techniques Source Guide
type: source
status: draft
category: sources
summary: Source guide for Kimball Group's 2013 technique catalog covering dimensional modeling concepts, fact tables, dimensions, conformance, SCD, hierarchies, and special schemas.
tags:
  - database
  - data-warehouse
  - modeling
sources:
  - https://www.kimballgroup.com/wp-content/uploads/2013/08/2013.09-Kimball-Dimensional-Modeling-Techniques11.pdf
source_url: https://www.kimballgroup.com/wp-content/uploads/2013/08/2013.09-Kimball-Dimensional-Modeling-Techniques11.pdf
created: 2026-06-19T10:40:26+0800
updated: 2026-06-19T10:40:26+0800
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-06-19
tier: supporting
provenance:
  extracted: 0.92
  inferred: 0.08
  ambiguous: 0.00
relationships:
  - target: "[[wiki/topics/Dimensional Modeling]]"
    type: related_to
  - target: "[[wiki/concepts/Fact Table]]"
    type: related_to
  - target: "[[wiki/concepts/Dimension Table]]"
    type: related_to
---

# Kimball Dimensional Modeling Techniques Source Guide

This source guide preserves the structure of Kimball Group's 2013 “Kimball Dimensional Modeling Techniques” PDF, drawn from *The Data Warehouse Toolkit, Third Edition* by Ralph Kimball and Margy Ross.

## Source identity

- Source: Kimball Group, “Kimball Dimensional Modeling Techniques,” September 2013.
- URL: https://www.kimballgroup.com/wp-content/uploads/2013/08/2013.09-Kimball-Dimensional-Modeling-Techniques11.pdf
- Length: 24 PDF pages; 21 numbered content pages after title and table of contents.

## Central frame

The document is a compact catalog of official Kimball dimensional modeling techniques. Its backbone is the four-step dimensional design process:

1. select the business process;
2. declare the [[wiki/concepts/Dimensional Design Grain|grain]];
3. identify the [[wiki/concepts/Dimension Table|dimensions]];
4. identify the [[wiki/concepts/Fact Table|facts]].

The catalog repeatedly returns to one principle: dimensional models should be governed by business process measurement events and consistent descriptive context, not by one-off report layouts.

## Fundamental concepts

- Business requirements and data realities must be gathered together: business representatives explain objectives, KPIs, decision processes, and analytic needs, while source-system experts and profiling reveal feasibility.
- Collaborative dimensional modeling workshops are required because dimensional models should not be designed in isolation from subject matter experts and data governance representatives.
- A business process is an operational activity, such as taking an order or snapshotting an account, that generates performance metrics for a fact table.
- The grain establishes exactly what one fact row represents and must be declared before dimensions or facts are chosen.
- Dimensions provide “who, what, where, when, why, and how” context; facts provide numeric measurements from a business process event.
- Star schemas implement dimensional structures in relational databases; OLAP cubes implement or derive dimensional structures in multidimensional databases.
- Graceful extensions include adding grain-consistent facts, adding non-grain-changing dimensions, adding dimension attributes, and restating a fact table at a lower grain while preserving existing names.

## Fact table techniques

- Fact tables contain numeric measures and foreign keys to associated dimensions; their design is based on physical measurement events, not eventual reports.
- Additive facts can be summed across all dimensions; semi-additive facts can be summed across only some dimensions; non-additive facts such as ratios are often better stored as additive components and calculated later.
- Null numeric facts are acceptable because aggregate functions handle them, but null foreign keys should be avoided by using default dimension rows for unknown or not-applicable conditions.
- Conformed facts must have identical technical definitions and names if they are to be compared or computed together.
- Transaction fact tables capture point-in-time events; periodic snapshots summarize activity over standard periods; accumulating snapshots update rows as a workflow passes milestones.
- Factless fact tables record dimensional combinations without numeric facts and can also support “what did not happen” analysis by comparing coverage and activity tables.
- Aggregate fact tables or cubes are performance structures that should behave like indexes and be chosen transparently by the BI layer.
- Consolidated fact tables combine cross-process facts when they share the same grain, trading ETL burden for easier analytics.
- BI applications should avoid direct fact-to-fact joins; multipass SQL and drilling across are the correct pattern.

## Dimension table techniques

- Dimension tables usually have one primary key, many descriptive low-cardinality text attributes, and are deliberately wide, flat, and denormalized.
- Surrogate dimension keys are recommended because natural keys are controlled by source systems, may change, may be incompatible, or may be poorly administered.
- Durable keys identify the same business entity across time even when multiple surrogate keys represent changing profiles.
- Drilling down means adding a dimension attribute to the row headers / SQL `GROUP BY`; it does not require predetermined drill paths.
- Degenerate dimensions occur when a dimension key, such as an invoice number, remains in the fact table without an associated dimension table.
- Role-playing dimensions reuse the same physical dimension in multiple semantic roles.
- Junk dimensions collect unrelated low-cardinality flags and indicators.
- Snowflaking and outriggers are possible but should be used carefully because dimensional modeling prefers query simplicity and speed.
- Abstract generic dimensions should be avoided when different business roles carry different attributes.

## Integration through conformance

- [[wiki/concepts/Conformed Dimension|Conformed dimensions]] integrate separate fact tables by giving them shared, consistent descriptive context.
- Shrunken rollup dimensions are conformed subsets used with aggregate fact tables at higher grains.
- Drilling across merges separate query result sets on conformed row-header attributes.
- A value chain can be represented as a set of business processes that each become rows in the enterprise bus matrix.
- The [[wiki/concepts/Data Warehouse Bus Matrix|enterprise data warehouse bus matrix]] maps business processes to conformed dimensions.

## Slowly changing dimensions

Kimball lists SCD Type 0 through Type 7:

- Type 0 retains original values.
- Type 1 overwrites values and destroys history.
- Type 2 adds a new row with a new surrogate key and effective/expiration metadata.
- Type 3 adds an attribute for an alternate reality.
- Type 4 splits rapidly changing attributes into a mini-dimension.
- Type 5 adds a current Type 1 outrigger to the mini-dimension pattern.
- Type 6 embeds current Type 1 attributes in Type 2 rows.
- Type 7 supports dual Type 1 and Type 2 perspectives through durable and surrogate keys.

## Hierarchies and advanced patterns

- Fixed-depth many-to-one hierarchies should be flattened into positional dimension attributes.
- Slightly ragged hierarchies can sometimes be force-fit into fixed-depth positional designs using business rules.
- Deep ragged hierarchies can be modeled with bridge tables containing every possible path, or with pathstring attributes when substitution and shared ownership are not required.
- Centipede fact tables should be avoided; many fixed-depth hierarchy keys should usually collapse back to the lowest-grain dimension.
- Numeric values can be facts, dimension attributes, or both depending on whether they are used for calculation or filtering/grouping.
- Header-level facts should often be allocated down to line-level grain so they can be sliced by all dimensions.
- Multiple currencies and units of measure require standard values, true values, and conversion factors governed by ETL rules.
- Late-arriving facts require looking up dimension keys effective at the time of the measurement event.
- Late-arriving dimensions can be represented by placeholder dimension rows and later updated with Type 1 overwrites.

## Special-purpose schemas

- Supertype/subtype schemas handle heterogeneous products by placing shared facts and attributes in a core structure and subtype-specific facts and dimensions in custom structures.
- Real-time fact tables require update strategies such as hot partitions, deferred updating, or DBMS/OLAP-specific support.
- Error event schemas capture data quality screen failures in a dimensional schema available to the ETL back room.

## Reading lens

The document can be read as a structural control manual for analytic data: declare the unit of measurement, attach descriptive context consistently, preserve history intentionally, and integrate processes through conformed dimensions rather than ad hoc joins.^[inferred]

## Related

- [[wiki/topics/Dimensional Modeling]]
- [[wiki/concepts/Dimensional Design Grain]]
- [[wiki/concepts/Fact Table]]
- [[wiki/concepts/Dimension Table]]
- [[wiki/concepts/Slowly Changing Dimension]]
- [[wiki/concepts/Conformed Dimension]]
- [[wiki/concepts/Data Warehouse Bus Matrix]]
- [[wiki/maps/CS Map]]
