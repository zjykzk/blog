---
title: DORA Metrics History Source Guide
category: sources
tags: [article, software-engineering, metrics, devops, feedback]
aliases:
  - A history of DORA’s software delivery metrics
  - DORA Metrics History
sources:
  - https://dora.dev/insights/dora-metrics-history/
created: 2026-06-11T22:29:33+08:00
updated: 2026-06-11T22:29:33+08:00
summary: Source guide preserving DORA's account of how software delivery metrics evolved from IT performance to the 2024 five-metric throughput/instability model.
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-06-11
type: source
status: draft
---

# DORA Metrics History Source Guide

> Source: DORA, “A history of DORA’s software delivery metrics,” January 2, 2026, https://dora.dev/insights/dora-metrics-history/

## Capture Policy

This page preserves the source-level article content pasted into the conversation. It is not a new stable concept page; the stable concept remains [[wiki/concepts/DORA Metrics]], while this guide records DORA’s historical account of how the metrics changed over time.

## What It Covers

The article traces how DORA’s measurement model evolved across more than a decade of research: from an initial quantitative definition of “IT performance,” through the four-key throughput/stability framing, into Software Delivery and Operational performance, reliability, failed deployment recovery time, and finally the 2024 five-metric split between Software Delivery Throughput and Software Delivery Instability.

It belongs in the wiki because it explains why the current metric set has its present shape. The article is especially useful for avoiding a static reading of [[wiki/concepts/DORA Metrics]]: the metrics are research artifacts that changed when DORA’s statistical model, terminology, and operational scope changed.

## Preserved Content

### Center of gravity: delivery metrics as evolving research artifacts

DORA says software delivery performance metrics have acted as the research program’s “center of gravity” for over a decade. Although the metrics became industry standards, the article emphasizes that they have not been static: their names, definitions, and scope changed as the technology landscape and DORA’s own research framing changed.

The important source-level claim is historical rather than merely definitional: DORA Metrics are not a frozen dashboard vocabulary. They are a research-backed measurement model that has been revised when older definitions no longer separated the right phenomena.

### 2014–2015: defining IT performance

In the inaugural 2014 study, DORA wanted to link IT performance to organizational performance. To do that, the researchers first had to define IT performance quantitatively.

The starting variables were:

- deployment frequency;
- lead time for changes;
- mean time to recover (MTTR);
- change fail rate.

The article notes a key statistical detail from 2014: change fail rate did not significantly correlate with the other variables strongly enough to form a single latent construct of IT performance. As a result, the 2014 IT performance definition relied on three metrics:

- deployment frequency;
- lead time for changes;
- mean time to recover.

By 2015, the model had solidified into a speed/stability duality. The article presents this as a debunking of the common belief that speed must trade off against stability. High performers were found to excel at both.

The 2015 framing grouped the metrics as:

- **Throughput measures**: deployment frequency and deployment lead time.
- **Stability measures**: mean time to recover and change fail rate.

### 2016–2018: standardization and operational expansion

Through 2016 and 2017, the four-metric set became an industry benchmark.

In 2018, DORA expanded the scope by adding availability as a measure of operational health. The article frames this as recognition that software delivery is only one part of the lifecycle: teams also need to keep promises about the software they operate.

This produced a terminology shift from broad “IT performance” to the more specific “Software Delivery and Operational (SDO) performance.” The original four metrics remained the core of software delivery, while availability extended the model into operational performance.

### 2021–2023: reliability and failed deployment recovery time

In 2021, DORA expanded “availability” into “reliability.” The article says this shift acknowledged that availability is only one focus of reliability engineering; reliability can also include latency, performance, and scalability.

The source includes a corrective note: the 2021 report inaccurately called reliability the “fifth metric,” while the article argues reliability is better understood as a measure of operational performance rather than a measure of software delivery performance.

In 2023, DORA renamed and redefined the historical “mean time to recover” / “time to restore service” metric as **failed deployment recovery time**.

The reason for the change was scope control. Older recovery definitions did not distinguish between failures caused by a software change and failures caused by external factors such as a data-center outage. The new metric focuses specifically on restoring service after a production change causes an impairment.

This made the metric align more statistically with the other software delivery metrics because it measures recovery from delivery-induced failure rather than general operational recovery.

### 2024: from four keys to five

The article describes 2024 as the most significant structural change to the metrics.

DORA researchers identified that change failure rate could act as a proxy for how much rework a team must perform. To test this, they introduced a fifth metric: **deployment rework rate**.

With this addition, DORA now uses five software delivery performance metrics grouped into two factors.

#### Software Delivery Throughput

- **Change lead time**: time from code commit to successful production deployment.
- **Deployment frequency**: how often application changes are deployed.
- **Failed deployment recovery time**: time to recover from a failed deployment.

#### Software Delivery Instability

- **Change fail rate**: percentage of deployments causing failures in production.
- **Deployment rework rate**: percentage of deployments that are unplanned work to fix bugs.

The article’s closing interpretation is that the evolution from “IT performance” to a five-metric model of “Software Delivery Throughput and Instability” demonstrates DORA’s commitment to learning and improvement. Measuring the factors over time gives teams a high-level view of performance regardless of technology stack.

## Integration Decisions

- Keep this page as a source guide because it preserves one DORA article’s historical account. Do not collapse it into the broader [[wiki/sources/DORA Metrics Source Guide]], which covers the current metric guide and improvement loop.
- Update [[wiki/concepts/DORA Metrics]] with the historical evolution, especially the shift from MTTR to failed deployment recovery time and the 2024 deployment rework rate addition.
- Treat single-article claims about why a definition changed as source-reported unless corroborated by the underlying DORA reports. The stable concept can state the evolution, but detailed statistical rationale should remain linked to this source guide.
- Link this history to [[wiki/topics/Modern Software Engineering]] because it shows a modern empirical-methodology pattern: measurement definitions are refined when research and operational reality expose boundary problems. ^[inferred]
- Link it to [[wiki/syntheses/Quality Engineering Three Generators]] because the progression from throughput/stability to throughput/instability maps onto promise clarity, deviation visibility, and recovery/rework loops. ^[inferred]

## Open Questions

- How should teams preserve historical metric definitions in dashboards so long-term trends remain interpretable after DORA changes terminology or scope? ^[inferred]
- Should reliability be reported beside DORA software delivery performance or kept in a separate operational-health scorecard to avoid mixing delivery and operations constructs? ^[inferred]
- How should deployment rework rate be implemented in organizations where hotfixes, incident response, and planned bug-fix work are not cleanly labeled? ^[inferred]

## Related

- [[wiki/concepts/DORA Metrics]]
- [[wiki/sources/DORA Metrics Source Guide]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/syntheses/Quality Engineering Three Generators]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/maps/CS Map]]
