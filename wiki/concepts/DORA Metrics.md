---
title: DORA Metrics
category: concepts
tags: [software-engineering, metrics, feedback, devops]
aliases:
  - DORA 软件交付指标
  - Software Delivery Performance Metrics
sources:
  - https://dora.dev/guides/dora-metrics/
  - https://dora.dev/insights/dora-metrics-history/
summary: DORA Metrics measure software delivery through a historically evolving five-signal model of throughput and instability.
provenance:
  extracted: 0.84
  inferred: 0.16
  ambiguous: 0.00
base_confidence: 0.78
lifecycle: draft
lifecycle_changed: 2026-06-11
created: 2026-06-11T17:49:52+08:00
updated: 2026-06-11T22:29:33+08:00
type: concept
status: draft
---

# DORA Metrics

DORA Metrics are five software delivery performance metrics for assessing how well a team delivers software safely, quickly, and efficiently.

## Key Ideas

DORA frames software delivery performance as a combined view of throughput and instability:

- **Change lead time**: time from version-control commit to production deployment.
- **Deployment frequency**: number of deployments in a period, or time between deployments.
- **Failed deployment recovery time**: time required to recover from a failed deployment that needs immediate intervention.
- **Change fail rate**: ratio of deployments that require immediate intervention, rollback, or hotfix.
- **Deployment rework rate**: ratio of unplanned deployments caused by production incidents.

The metrics are meant to be applied at the application or service level, because different systems have different technology, user, organizational, and compliance contexts.

DORA's guide treats these metrics as both leading indicators for organizational performance and employee well-being, and lagging indicators for software development and delivery practices.

The deeper engineering value is not ranking teams but making the delivery system visible enough to improve: throughput shows how quickly changes move, while instability shows whether that movement is damaging the system. ^[inferred]

## Speed and Stability

A key DORA claim is that speed and stability are not long-term tradeoffs: high performers tend to do well across all five metrics, while low performers tend to do poorly across them.

This connects DORA Metrics to [[wiki/topics/Modern Software Engineering]]: software engineering is empirical problem solving, so delivery performance should be judged by real feedback from the delivery system, not by local activity volume. ^[inferred]

## Anti-Goodhart Boundary

DORA warns against turning metrics into targets. Common failure modes include:

- setting broad metric goals that invite gaming;
- choosing one metric to rule them all;
- comparing very different applications as if context did not matter;
- isolating ownership so development, operations, and release teams optimize against one another;
- measuring instead of improving.

A healthier use is to keep metrics in tension, pair them with delivery-process conversations, and use them to find constraints rather than to declare winners. ^[inferred]

## Improvement Loop

The DORA guide recommends improving the metrics by reducing batch size and running a cross-functional learning loop:

1. set a baseline with DORA Quick Check;
2. discuss friction points and map the delivery process;
3. commit to improving the most significant constraint or bottleneck;
4. turn the commitment into a plan with leading indicators such as code-review duration or test quality;
5. do the work;
6. check progress through metrics, conversations, and retrospectives;
7. repeat.

This makes DORA Metrics a delivery-system feedback loop, not a standalone dashboard. ^[inferred]

## Historical Evolution

DORA's software delivery metrics evolved as the research program refined what it meant to measure technology performance:

- In 2014, DORA began with deployment frequency, lead time for changes, mean time to recover, and change fail rate, but change fail rate did not statistically join the other variables into a single latent construct of IT performance.
- By 2015, the model stabilized into throughput and stability: deployment frequency and lead time for throughput; MTTR and change fail rate for stability.
- In 2018, DORA added availability and renamed the broader frame from IT performance to Software Delivery and Operational performance.
- In 2021, availability expanded into reliability, covering broader operational concerns such as latency, performance, and scalability.
- In 2023, MTTR / time to restore service became **failed deployment recovery time** so the metric specifically measured recovery from production changes that caused impairment, not all operational outages.
- In 2024, DORA added **deployment rework rate** because change fail rate also acted as a proxy for rework burden.

This history matters because the metrics are not merely names on a dashboard. They encode a boundary decision about which failures belong to software delivery performance and which belong to wider operational reliability. ^[inferred]

## Open Questions

- How should teams choose leading indicators that predict DORA improvement without creating local gaming incentives? ^[inferred]
- How should DORA Metrics be interpreted for AI-assisted development, where code generation speed can rise while review burden or rework also rises? ^[inferred]

## Sources

- [[wiki/sources/DORA Metrics Source Guide]] — DORA guide to the current five software delivery performance metrics.
- [[wiki/sources/DORA Metrics History Source Guide]] — DORA article tracing the metrics from IT performance through SDO performance, reliability, failed deployment recovery time, and the 2024 deployment rework rate addition.

## Related

- [[wiki/topics/Modern Software Engineering]]
- [[wiki/syntheses/Quality Engineering Three Generators]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/concepts/Feedback Loops]]
- [[wiki/maps/CS Map]]
