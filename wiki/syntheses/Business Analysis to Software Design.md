---
title: Business Analysis to Software Design
category: syntheses
tags:
  - software-methodology
  - analysis
  - design
sources:
  - wiki/maps/Software Analysis Map.md
  - wiki/maps/Software Design Map.md
  - wiki/concepts/Software Analysis Three Generators.md
  - wiki/concepts/Software Design Three Generators.md
  - wiki/concepts/Domain-Driven Design.md
  - wiki/concepts/Business Modeling in Software.md
  - wiki/topics/Software Methodology.md
  - wiki/sources/Business Modeling and DDD NotebookLM Practice Map Source Guide.md
created: 2026-05-05
updated: 2026-10-28T15:24:26+08:00
summary: Business modeling narrows organizational reality into system responsibilities, domain models, executable design boundaries, and problem-matched practices.
provenance:
  extracted: 0.55
  inferred: 0.40
  ambiguous: 0.05
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-05
---
# Business Analysis to Software Design

## The Connection

[[wiki/concepts/Business Modeling in Software]], [[wiki/concepts/Software Analysis Three Generators]], [[wiki/concepts/Domain-Driven Design]], and [[wiki/concepts/Software Design Three Generators]] describe one pipeline at different resolutions.

Business modeling asks how the target organization produces results. Software analysis turns that organizational reality into system responsibilities and boundaries. Domain-driven design compresses the selected business reality into a shared model. Software design then makes that model executable through boundaries, protocols, and runtime flow. ^[inferred]

## Where They Co-occur

These concepts co-occur in [[wiki/maps/Software Analysis Map]], [[wiki/maps/Software Design Map]], [[wiki/topics/Software Methodology]], and the concept pages for software analysis, software design, DDD, and business modeling.

The repeated pattern is a handoff problem: a business improvement target must become a system boundary, then a domain model, then executable software structure.

## Cross-cutting Insight

The crucial transition is not "requirements become code". It is "organizational exchange becomes modeled responsibility". ^[inferred]

If analysis skips business modeling, the system may optimize a function without knowing which organizational result it improves. If design skips domain modeling, the code may implement screens and data tables without preserving the business distinctions that made the requirement meaningful. ^[inferred]

DDD sits between analysis and design because it forces the same model to satisfy two pressures at once: it must still explain the business, and it must be precise enough to guide implementation. ^[inferred]

The handoff can be read as a sequence of narrowing boundaries: business modeling fixes the target organization and improvement reason; software analysis fixes what the to-be-built system must take responsibility for; software design fixes internal partitions, connections, and state flow. DDD is the hinge where business language becomes a model that can survive implementation pressure. ^[inferred]

The pipeline is incomplete if the resulting code only preserves machine behavior. [[wiki/concepts/Code Expression for Human Understanding]] adds the maintenance-facing handoff: implementation should keep intent, responsibility, constraints, state change, and failure modes legible to the humans who must verify and evolve the model. ^[inferred]

## Choose Practices by Problem Layer

The pipeline also provides a way to choose practices. [[wiki/sources/Business Modeling and DDD NotebookLM Practice Map Source Guide]] groups 36 practices by the problem layer they primarily address:

| Problem layer | Diagnostic question | Practice families |
|---|---|---|
| Business modeling and requirements | Do we understand the organizational result, external actor, and system promise? | Business/system use cases, sea-level use cases, story mapping, 3C, business sequence diagrams |
| Strategic DDD | Do business and technology share meanings, and is each model's boundary explicit? | Ubiquitous language, bounded context, context mapping, ACL, shared kernel, OHS/PL |
| Tactical DDD | Does code preserve business rules, invariants, and aggregate boundaries? | Rich domain model, small aggregates, identity references, domain events, domain services, factories |
| Architecture and integration | Can the core evolve without being trapped by infrastructure, synchronous chains, or legacy replacement risk? | Strangler, hexagonal architecture, CQRS, event-driven architecture, pipes and filters, DSL |
| Organization and delivery | Do team boundaries and feedback loops support the intended system boundaries? | Inverse Conway, TDD, event storming, Q1/Q2 linkage, LLM pairing with tests |
| Object design | Are local responsibilities, algorithms, states, and extensions separated at the code level? | SRP, DIP, Strategy, State, Decorator, Observer, Role Object |

This is not a maturity ladder and not a checklist. A project should start from the observed failure layer and introduce the smallest practice that changes the causal structure there. Adding a tactical pattern cannot repair an undefined business boundary; adding a workshop cannot repair an implementation that continually violates an already-understood boundary. ^[inferred]

Several practices cross layers. Domain events belong to the domain model but may drive system integration; an anticorruption layer expresses a strategic model boundary through architectural code; event storming is a collaboration practice that discovers strategic boundaries. The grouping therefore indicates the first problem to inspect, not exclusive ownership. ^[inferred]

## Tensions and Trade-offs

- Business modeling wants to preserve organizational context, while software design needs sharper boundaries and smaller mechanisms. ^[inferred]
- Software analysis can overfit to existing work practice; software design can overfit to technical convenience. DDD is useful when it keeps both pressures visible. ^[inferred]
- The same boundary word appears at multiple layers: organization boundary, system boundary, bounded context, module boundary, and transaction boundary. Confusing these layers is a common cause of analysis/design drift. ^[inferred]
- The wiki still needs more examples showing when the pipeline should be lightweight versus formal. ^[ambiguous]

## Open Questions

- When should a project stop at user stories, and when does it need explicit business modeling?
- Which artifacts best preserve the handoff from organizational exchange to object responsibility?
- How should this pipeline change for brownfield systems where the current code already encodes an implicit domain model?

## Related

- [[wiki/concepts/Business Modeling in Software]]
- [[wiki/concepts/Software Analysis Three Generators]]
- [[wiki/concepts/Domain-Driven Design]]
- [[wiki/concepts/Software Design Three Generators]]
- [[wiki/concepts/Code Expression for Human Understanding]]
- [[wiki/topics/Software Methodology]]
- [[wiki/syntheses/From User Story to Architecture]]
- [[wiki/sources/Business Modeling and DDD NotebookLM Practice Map Source Guide]]
