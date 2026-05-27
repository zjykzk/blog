---
title: >-
  Fallacies of Distributed Computing Source Guide
category: sources
tags: [book, distributed-systems, architecture, systems, software-engineering]
sources:
  - conversation:2026-05-27
created: 2026-05-27T00:49:30+0800
updated: 2026-05-27T00:49:30+0800
summary: >-
  Source guide preserving the eight Fallacies of Distributed Computing as a checklist of mistaken network assumptions and the defensive design they require.
provenance:
  extracted: 0.91
  inferred: 0.08
  ambiguous: 0.01
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-27
type: source
status: draft
aliases:
  - Fallacies of Distributed Computing
  - Eight Fallacies of Distributed Computing
  - Distributed Computing Fallacies
---
# Fallacies of Distributed Computing Source Guide

> Source: Pasted chapter excerpt, "Fallacies of Distributed Computing," from *Laws of Software Engineering* material.

## Capture Policy

This page preserves the pasted chapter as source-level material. It keeps the chapter's checklist, origin story, examples, Amazon SimpleDB incident, related concepts, and figure reference rather than promoting the fallacies into a standalone stable concept page yet.

## What It Covers

The Fallacies of Distributed Computing are eight false assumptions often made when designing or operating distributed systems. They matter because engineers used to local computing can unconsciously treat remote calls, network paths, and shared infrastructure as if they behaved like in-process calls.

The source belongs in the CS and distributed-systems cluster because it names the baseline non-ideal properties of real networks: dropped messages, latency, finite bandwidth, security risk, changing topology, multiple administrators, transport cost, and heterogeneous infrastructure. It should be read alongside [[wiki/sources/CAP Theorem Source Guide]], [[wiki/topics/Circuit Breaker]], [[wiki/sources/Law of Leaky Abstractions Source Guide]], and [[wiki/concepts/System]].

## Preserved Content

### Key Takeaways

Real networks drop messages, introduce delays, have finite throughput, expose security risks, and change shape over time. A distributed system should therefore use defensive design: retries, timeouts, authentication, encryption, redundancy, caching, dynamic discovery, topology-aware routing, and explicit handling of partial failure.

The fallacies often appear as subtle bugs rather than obvious design mistakes. For example, assuming latency is zero can lead to chatty remote calls that work locally but become painfully slow across an actual network.

Accounting for the fallacies up front changes the architecture. Caches become necessary because bandwidth and latency are not ideal; redundancy becomes necessary because networks and nodes fail; dynamic membership handling becomes necessary because topology changes.

### Overview: The Eight Fallacies

The source presents the fallacies as a checklist of what not to assume:

1. The network is reliable.
2. Latency is zero.
3. Bandwidth is infinite.
4. The network is secure.
5. Topology doesn't change.
6. There is one administrator.
7. Transport cost is zero.
8. The network is homogeneous.

All eight spring from the same root mistake: treating a distributed system like a local one. Remote service calls are not local function calls. They can fail independently, become slow, consume bandwidth, cross trust boundaries, and change behavior as machines, routes, ownership, and platforms change.

The chapter frames the fallacies as a mindset correction. The network should be expected to fail and behave non-ideally; the system must be designed to tolerate that reality.

### Origins

The concept is credited primarily to L. Peter Deutsch around 1994 at Sun Microsystems, with others including James Gosling contributing to the list. The original list contained seven fallacies; Gosling later added the eighth: "The network is homogeneous."

Deutsch observed that engineers accustomed to local computing would subconsciously assume that the network simply worked. Turning those assumptions into a named checklist helped teams remember to address each one during distributed-system design.

Over time, the fallacies became widely taught in distributed-computing courses.

### Amazon SimpleDB Outage Example

The source describes a June 13, 2014 Amazon SimpleDB outage where a power failure in one Amazon data center took down SimpleDB across all regions for two hours.

The system was designed to handle node failures, but simultaneous power loss across multiple storage nodes overwhelmed the lock service with de-registration requests. Healthy nodes then tried to verify their own status, ran into timeout walls caused by increased latency, and removed themselves from the cluster because they believed they had lost connectivity.

The source uses this as a case where several fallacies appeared together:

- the architecture assumed reliable network behavior under stress;
- it underestimated latency during failure handling;
- it assumed network paths and failure-detection behavior would remain uniform;
- a localized hardware problem cascaded because the failure-detection mechanism became a bottleneck.

The key lesson is that failure-handling paths are themselves distributed systems. If those paths assume reliable, low-latency communication, they can amplify the original fault instead of containing it. ^[inferred]

### Chatty Remote Cache Example

A developer building a distributed cache might assume that network latency is effectively zero and fetch data from a remote node for every small lookup.

This may appear acceptable in a local environment or ideal model, but in production it creates many round trips. The design then suffers from high latency and poor throughput. The practical correction is to minimize round trips, use batching or local caching where appropriate, and make network boundaries visible in the design.

### Insecure Network Example

Assuming that the network is secure can lead a system to send sensitive data unencrypted or fail to validate inputs from other services.

The source treats this as a direct path to breach if the network is compromised. Distributed systems should authenticate remote callers, encrypt sensitive traffic where needed, validate inputs at service boundaries, and avoid trusting traffic simply because it is "internal."

### Multiple Administrators Example

Assuming that there is one administrator hides the fact that subsystems may be owned by different teams, automated processes, cloud providers, deployment controllers, or external services.

Those parties can make conflicting changes. Distributed designs therefore need explicit ownership, change coordination, versioning, observability, and rollback paths rather than assuming a single coherent control point. ^[inferred]

### Changing Topology Example

The chapter notes that systems break when they assume topology does not change. Machines can be added, removed, restarted, rescheduled, partitioned, or moved across zones and regions.

Distributed systems therefore need service discovery, membership protocols, health checks, load balancing, and failure-aware routing. A fixed mental picture of the network becomes wrong as soon as deployment, scaling, or recovery changes the topology.

### Figure Preserved from the Source

The source includes a figure titled "Fallacies of Distributed Computing." The pasted image URL is local-only: `http://127.0.0.1:8123/read/Laws%20of%20Software%20Engineering_data/images/image4.png`.

The durable wiki should preserve the figure title and role, but not depend on that local URL being available later. ^[inferred]

### Related Concepts from the Source

The source explicitly relates the Fallacies of Distributed Computing to:

- **The CAP Theorem**: CAP focuses on consistency, availability, and partition tolerance under distributed failure; the fallacies provide the broader checklist of network assumptions that make such trade-offs unavoidable.
- **Murphy's Law**: if something can go wrong in a distributed system, it should be assumed possible and designed for rather than dismissed as an edge case.

### Further Reading Preserved from the Source

- Fallacies of distributed computing. (n.d.). *Wikipedia*. https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing
- Rotem-Gal-Oz, A. (n.d.). *Fallacies of distributed computing explained*. https://arnon.me/wp-content/uploads/Files/fallacies.pdf

## Integration Decisions

This page should remain source-level because it preserves a chapter excerpt with examples and references. A later concept page could promote the minimal model: distributed design begins by rejecting local-call assumptions and making failure, latency, bandwidth, trust, topology, administration, transport cost, and heterogeneity explicit design dimensions.

The source complements [[wiki/sources/CAP Theorem Source Guide]]. CAP describes a formal partition-time trade-off around consistency and availability; the Fallacies of Distributed Computing describe the broader operational assumptions that lead engineers to underbuild for real network behavior. ^[inferred]

It also connects to [[wiki/topics/Circuit Breaker]] because circuit breakers operationalize one response to unreliable or slow networks: stop sending work to an unhealthy dependency long enough to prevent cascading failure. ^[inferred]

The SimpleDB outage example should stay source-level unless later verified from independent incident reports. It is useful as an illustration of how latency, reliability, topology, and failure detection can interact, but the exact incident narrative comes from the pasted chapter. ^[inferred]

## Open Questions

- Should the wiki promote the eight fallacies into a stable concept page, or wait until PACELC, consistency models, and failure-detection material are also captured?
- Which current cloud-native patterns map most directly to each fallacy: retries, timeouts, circuit breakers, bulkheads, service discovery, mTLS, observability, rate limiting, and topology-aware routing?
- How should the wiki distinguish network fallacies from broader distributed-systems laws such as CAP, PACELC, Hyrum's Law, and Murphy's Law?

## Related

- [[wiki/maps/CS Map]]
- [[wiki/topics/Circuit Breaker]]
- [[wiki/sources/CAP Theorem Source Guide]]
- [[wiki/sources/Law of Leaky Abstractions Source Guide]]
- [[wiki/sources/Hyrums Law Source Guide|Hyrum's Law Source Guide]]
- [[wiki/concepts/System]]
