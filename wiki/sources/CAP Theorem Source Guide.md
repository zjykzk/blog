---
title: >-
  CAP Theorem Source Guide
category: sources
tags: [book, distributed-systems, database, systems, architecture]
sources:
  - conversation:2026-05-22
created: 2026-05-22T01:47:51+08:00
updated: 2026-05-22T01:47:51+08:00
summary: >-
  Source guide preserving a CAP theorem chapter on consistency, availability, partition tolerance, database examples, and Kleppmann's critique of CAP as a design heuristic.
provenance:
  extracted: 0.91
  inferred: 0.07
  ambiguous: 0.02
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-22
type: source
status: draft
aliases:
  - CAP Theorem
  - Brewer's theorem
  - Consistency Availability Partition Tolerance
---

# CAP Theorem Source Guide

> Source: *Laws of Software Engineering*, Chapter 4, “The CAP Theorem” pasted excerpt.

## Capture Policy

This page preserves the pasted chapter as source-level material. It keeps the chapter's teaching sequence, examples, and critique without promoting CAP into a standalone stable concept page yet.

## What It Covers

The chapter introduces the CAP theorem as a distributed-systems trade-off among Consistency, Availability, and Partition Tolerance. It explains why network partitions force systems to choose between consistency and availability, gives DNS, relational replication, MongoDB, and Cassandra examples, and then qualifies the usual “choose two” framing through Martin Kleppmann's critique.

This source belongs in the CS and distributed-systems cluster because it connects database replication, network failure, consistency models, latency, and system-design trade-offs. It should be read alongside [[wiki/topics/Circuit Breaker]], which handles failure containment, and [[wiki/concepts/System]], which frames distributed behavior as relations, boundaries, feedback, and time rather than isolated components.

## Preserved Content

### Key Takeaways

A distributed system can meet at most two of three guarantees: Consistency, Availability, and Partition Tolerance. In an ideal network, consistency and availability can coexist; under a network partition, the system must give up one of them.

The theorem's practical trade-off appears during partition: the system can remain consistent by refusing or delaying operations, or remain available by responding even when replicas may diverge. It cannot be fully consistent and fully available while communication between nodes is unreliable.

Distributed databases often lean toward one side of the partition-time trade-off. MongoDB is presented as favoring consistency: during partition, writes may be blocked or refused so replicas do not diverge. Cassandra is presented as favoring availability: it keeps answering queries even if some replicas temporarily differ until consistency is repaired.

### Overview: C, A, and P

The CAP theorem is a core concept in distributed systems and databases. It names three desirable properties:

1. **Consistency** means all nodes see the same data at the same time. If one node observes a change, the other nodes should also observe that change immediately.
2. **Availability** means every request receives a response, though that response is not guaranteed to include the latest write. The system keeps operating even when part of it is down or unable to communicate.
3. **Partition Tolerance** means the system continues operating despite unreliable communication among nodes, including lost or delayed messages.

The theorem matters because it turns distributed design into an explicit trade-off. If a system promises that every read returns the most recent write and also needs to tolerate communication failure, then some clients or operations may lose availability during partition.

Because real-world networks can partition, distributed systems generally must treat partition tolerance as non-negotiable. That leaves a common design question: under partition, should the system behave more like CP, sacrificing availability to preserve consistency, or more like AP, sacrificing immediate consistency to keep responding?

### Origins

Eric Brewer proposed the theorem in 2000 in the context of web services. Seth Gilbert and Nancy Lynch later formalized it in 2002.

Brewer's original concern came from large-scale systems that had to keep data consistent across nodes, keep services up, and survive network unreliability. The formal proof sharpened the point: in a distributed system with shared data, a partition forces a sacrifice between consistency and availability.

CAP then became a central design frame in the NoSQL movement and in distributed-database architecture during the 2000s.

### DNS as an AP Example

The Domain Name System is presented as an availability-and-partition-tolerance example. If some name servers cannot communicate, they can still answer queries. Their answers may be slightly outdated until zones synchronize, but the system continues to serve clients.

DNS therefore illustrates the AP posture: availability is preserved even when strict, immediate consistency is not guaranteed.

### Relational Replication and MongoDB as CP Examples

A traditional relational database with replication often chooses a CP posture during network splits. Some replicas may refuse writes or become read-only so the system does not accept conflicting changes.

MongoDB is used as an example of a database that favors consistency during partition. If nodes cannot coordinate safely, it may block or refuse writes rather than allow divergent state to become accepted as valid.

This preserves a consistent system view, but some clients experience reduced availability until communication recovers.

### Cassandra as an AP Example

Apache Cassandra is presented as a database designed to favor availability and partition tolerance over immediate consistency.

In a Cassandra cluster replicated across multiple data centers, a partition can separate data center A from data center B. If data center A updates a user's balance while data center B reads the same user's balance before the update propagates, data center B may return the old value. The system stays available, but different replicas can temporarily disagree.

Cassandra's consistency levels make the trade-off adjustable per operation. The `ALL` consistency level sacrifices availability during partition to ensure consistency. The `ONE` consistency level favors availability, accepting weaker consistency. This makes CAP less like an absolute database label and more like an operational spectrum.

### CAP Is a Spectrum, Not a Simple Product Label

The chapter explicitly warns against treating CAP as an absolute dichotomy. While strong consistency and strong availability cannot both be guaranteed during a partition, systems can expose tunable choices and workload-specific behavior.

A database should not be selected only by asking whether it is “CP” or “AP.” More practical questions include:

- What latency does the application require?
- Which failure modes must the system survive?
- Which operations require strict consistency?
- Which operations can tolerate stale or convergent data?
- How costly is temporary unavailability compared with temporary divergence?

### Kleppmann's Critique

The chapter includes Martin Kleppmann's critique that CAP has serious flaws as a design principle. The definitions used in the theorem can be ambiguous or contradictory, and “availability” in the Gilbert-Lynch formalization differs from how engineers often use the word in practice.

The critique also notes that the proof becomes most clear under an assumption that partitions may last forever. That assumption makes both linearizability and eventual consistency impossible, so it can be too blunt for real system design.

Kleppmann's preferred lens is delay sensitivity: ask how the system's delay changes as the network slows down. In linearizable systems, delay grows with network delay. In causally consistent systems, delay can be independent of network delay. This creates a more useful design frame than arguing about an impossibility slogan.

### Related Concepts Named by the Source

The chapter names PACELC and the Fallacies of Distributed Computing as related ideas. PACELC extends the CAP conversation by asking what a system chooses when there is a partition and what it chooses else, during normal latency conditions. The Fallacies of Distributed Computing capture common mistaken assumptions about network reliability, latency, bandwidth, security, topology, administration, transport cost, and homogeneity. ^[inferred]

### Further Reading Preserved from the Chapter

- Brewer, E. A. (2000). *Towards robust distributed systems* (abstract). Proceedings of the Annual ACM Symposium on Principles of Distributed Computing (PODC). ACM.
- Brewer, E. A. (2012). CAP twelve years later: How the “rules” have changed. *Computer*, 45(2), 23–29. IEEE.
- CAP theorem. (n.d.). *Wikipedia*. https://en.wikipedia.org/wiki/CAP_theorem
- Corbett, J. C., Dean, J., Epstein, M., Fikes, A., Frost, C., Furman, S., Ghemawat, S., Gubarev, A., Heiser, C., Hochschild, P., Hsieh, W., Kanthak, S., Kogan, E., Li, H., Lloyd, A., Melnik, S., Mwaura, J., Nagle, D., Quinlan, S., Rao, R., Rolig, L., Saito, Y., Szymaniak, M., Taylor, W., Wang, R., & Woodford, D. (2012). Spanner: Google's globally-distributed database. Proceedings of OSDI '12, 251–264.
- Gilbert, S., & Lynch, N. (2002). Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services. *ACM SIGACT News*, 33(2), 51–59.
- Kleppmann, M. (2015). *A Critique of the CAP Theorem*. University of Cambridge, Computer Laboratory. https://www.cl.cam.ac.uk/research/dtg/archived/files/publications/public/mk428/cap-critique.pdf
- Kleppmann, M. (2017). *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems*. O'Reilly Media.

## Integration Decisions

The CAP chapter should remain source-level because it mixes introductory explanation, named examples, and critique. A later stable concept page could promote the minimal model: partition tolerance is usually mandatory, so the real design choice is how much consistency, availability, and delay sensitivity each operation needs under failure.

The source should not be reduced to “choose two of three.” Its most reusable insight is the corrected frame: CAP is an impossibility result for partition-time guarantees, but real design depends on operation-level consistency, latency requirements, failure assumptions, and degradation behavior.

The database examples connect to [[wiki/topics/BoltDB Internals]] and [[wiki/sources/Doris 写入与 Routine Load Source Guide|Doris 写入与 Routine Load Source Guide]] as a contrast: single-node storage internals, OLAP ingestion reliability, and distributed consistency each expose different meanings of “reliable data.” ^[inferred]

## Open Questions

- Should CAP be promoted into a stable concept page, or should it remain a source guide until PACELC and consistency-model material are also captured?
- How should the wiki distinguish linearizability, serializability, causal consistency, eventual consistency, and availability in later distributed-systems notes?
- Which database examples should be verified against current product behavior before being used as design guidance?

## Related

- [[wiki/maps/CS Map]]
- [[wiki/topics/Circuit Breaker]]
- [[wiki/concepts/System]]
- [[wiki/topics/BoltDB Internals]]
- [[wiki/sources/Doris 写入与 Routine Load Source Guide|Doris 写入与 Routine Load Source Guide]]
