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
created: 2026-05-05
updated: 2026-05-10T14:24:08+08:00
summary: Business modeling narrows organizational reality into system responsibilities, domain models, and executable design boundaries.
provenance:
  extracted: 0.57
  inferred: 0.38
  ambiguous: 0.05
base_confidence: 0.70
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
- [[wiki/topics/Software Methodology]]
- [[wiki/syntheses/From User Story to Architecture]]
