---
title: DORA Metrics Source Guide
category: sources
tags: [article, software-engineering, metrics, devops, feedback]
aliases:
  - DORA’s software delivery performance metrics
  - DORA Metrics Guide
sources:
  - https://dora.dev/guides/dora-metrics/
summary: Source guide for DORA's guide to five software delivery performance metrics, their throughput/instability split, pitfalls, and improvement loop.
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-06-11
created: 2026-06-11T17:49:52+08:00
updated: 2026-06-11T17:49:52+08:00
type: source
status: draft
---

# DORA Metrics Source Guide

## Source Identity

- Source: DORA, “DORA’s software delivery performance metrics”
- URL: https://dora.dev/guides/dora-metrics/
- Last updated by source page: January 5, 2026
- Extraction representation: readable Markdown extracted through `https://r.jina.ai/http://https://dora.dev/guides/dora-metrics/`; manifest hash uses the original HTML bytes fetched from the canonical URL.
- Source byte hash: `sha256:00f7a12f296db54df7006f19badcfe668819c30fc50d386c471fe55531bcdff1`

## What the Source Says

DORA argues that technology-driven teams need ways to measure performance so they can assess current state, prioritize improvements, and validate progress. The guide presents five software delivery performance metrics as a way to measure outcomes of the software delivery process.

The guide says DORA research shows these performance metrics predict better organizational performance and team-member well-being. It also notes that the metrics have evolved from the original four-key model to the current five-metric model, including the shift from MTTR to Failed Deployment Recovery Time.

## Leading and Lagging Indicator Frame

The source says these metrics can be read in two directions:

- as leading indicators for organizational performance and employee well-being;
- as lagging indicators for software development and delivery practices.

This matters because the metrics are not just retrospective reports. They can orient improvement conversations when paired with the real delivery process. ^[inferred]

## Throughput and Instability

DORA groups the metrics into two factors.

### Throughput

Throughput is how many changes can move through the delivery system over time. Higher throughput means the system can move more changes into production.

DORA uses three metrics for throughput:

- **Change lead time**: the time from committing a change to version control to deploying it in production.
- **Deployment frequency**: number of deployments in a given period, or time between deployments.
- **Failed deployment recovery time**: the time needed to recover from a deployment failure requiring immediate intervention.

### Instability

Instability is how well deployments go. When deployments go well, teams can confidently push more changes, and users are less likely to experience immediate post-deployment issues.

DORA uses two metrics for instability:

- **Change fail rate**: the ratio of deployments requiring immediate intervention, rollback, or hotfix.
- **Deployment rework rate**: the ratio of unplanned deployments that happen because of a production incident.

Together, throughput and instability provide a high-level view of delivery performance across applications or services, independent of technology stack, deployment-process complexity, or end-user type.

## Key Insights Preserved

- DORA's research repeatedly finds that speed and stability are not tradeoffs over long periods.
- Top performers tend to do well across all five metrics; low performers tend to do poorly across them.
- The metrics can apply to different technologies, including LLM systems, banking applications, mobile ordering apps, and mainframe travel systems.
- The metrics are best applied one application or service at a time.
- Context matters: blending metrics across many teams or whole organizations can be problematic when applications differ in users, context, and constraints.
- The guide quotes Dave Farley: “the real trade-off, over long periods of time, is between better software faster and worse software slower.”

## Pitfalls

The source warns against several adoption pitfalls:

- **Setting metrics as a goal**: broad targets can create Goodhart-style gaming.
- **Having one metric to rule them all**: complex systems need multiple metrics with healthy tension.
- **Using industry as a shield against improving**: regulated context can become an excuse for no change.
- **Making disparate comparisons**: comparing very different applications can mislead.
- **Having siloed ownership**: isolating metrics by dev, ops, or release teams can produce friction and blame.
- **Competing**: the goal is team improvement over time, not competition between teams or organizations.
- **Focusing on measurement at the expense of improvement**: exact integrations may not be worth the initial investment; conversations, Quick Check, and lightweight tools may be better starting points.

## Improvement Process

The guide's recommended first improvement lever is reducing batch size. Smaller changes are easier to understand, move through delivery, and recover from when they fail.

The guide proposes a repeated improvement loop:

1. set a baseline for the application using DORA Quick Check;
2. discuss friction points in the delivery process;
3. map the delivery process when useful;
4. commit as a cross-functional team to improving the main constraint or bottleneck;
5. turn that commitment into a plan with possible leading indicators, such as code-review duration or test quality;
6. do the work;
7. check progress through DORA Quick Check, conversations, and retrospectives;
8. repeat the process for continuous learning and improvement.

## Distillation into the Wiki

This source created [[wiki/concepts/DORA Metrics]]. It also strengthens [[wiki/topics/Modern Software Engineering]] by making empirical software engineering measurable at the delivery-system level, and [[wiki/syntheses/Quality Engineering Three Generators]] by adding a concrete metric set for throughput, instability, batch size, and improvement loops. ^[inferred]

## Open Questions

- How can organizations report DORA Metrics upward without turning them into cross-team ranking targets? ^[inferred]
- How should deployment rework rate be operationalized in teams whose incident response is spread across several systems or repositories? ^[inferred]
- Which leading indicators best predict DORA improvement in AI-assisted delivery workflows? ^[inferred]

## Related

- [[wiki/concepts/DORA Metrics]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/syntheses/Quality Engineering Three Generators]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/concepts/Feedback Loops]]
