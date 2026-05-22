---
title: >-
  Hyrum's Law Source Guide
category: sources
tags: [book, software-engineering, architecture, systems]
sources:
  - conversation:2026-05-22
created: 2026-05-22T02:02:00+08:00
updated: 2026-05-22T02:02:00+08:00
summary: >-
  Source guide preserving Hyrum's Law as the claim that every observable behavior of a sufficiently used API becomes somebody's dependency.
provenance:
  extracted: 0.92
  inferred: 0.08
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-22
type: source
status: draft
aliases:
  - Hyrum's Law
  - Hyrums Law
---

# Hyrum's Law Source Guide

> Source: Pasted chapter excerpt, “Hyrum’s Law,” from *Laws of Software Engineering* material.

## Capture Policy

This page preserves the pasted chapter as source-level material. It keeps Hyrum’s Law’s definition, origin, examples, and compatibility implications rather than reducing the source to a short concept note.

## What It Covers

Hyrum’s Law states that with enough users of an API, all observable behaviors of a system become dependencies, regardless of what the official contract promises. The source treats software contracts as broader than documented APIs: users may depend on timing, error messages, output ordering, formatting, memory behavior, UI conventions, bugs, or other side effects.

The source belongs in the wiki’s software and systems cluster because it explains why change is difficult in widely used systems, why backward compatibility requires care, and why implementation details can become public interface through use. It should be read alongside [[wiki/sources/Law of Leaky Abstractions Source Guide]], [[wiki/topics/Modern Software Engineering]], [[wiki/concepts/System]], and [[wiki/maps/CS Map]].

## Preserved Content

### Core Statement

Hyrum’s Law: “With a sufficient number of users of an API, it does not matter what you promise in the contract. All observable behaviors of your system will be depended on by somebody.”

The practical rule is: the real contract of a system is not limited to the documented interface. Once enough users observe and build against the system, every stable-seeming behavior can become part of someone’s workflow.

### Main Takeaways

- As user count grows, everything a system does can become a dependency.
- Unintended side effects, incidental ordering, performance behavior, bugs, and formatting can become de facto features.
- Maintainers should assume that changes may break users who integrated the API in unexpected ways.
- The actual contract includes observed behavior in the wild, not only the official API or specification.
- Informal surfaces, including a familiar UI, can function as contracts when users organize work around them.

### Argument Flow

Hyrum’s Law describes how the boundary between documented interface and implementation detail erodes under real use. A system owner may promise only a narrow API contract, but users interact with the full observable behavior of the system. Over time, some users discover useful patterns outside the intended contract and depend on them.

This means the implementation becomes part of the interface. A specific error message, JSON key order, response timing, memory layout, or UI behavior may be treated as stable by consumers even when the maintainer never intended to support it. The larger the user base, the more likely it is that someone depends on each visible detail.

The result is reduced freedom to change. A maintainer may perform an internal refactor, optimization, or cleanup that appears compatible with the documented API, yet still break real users because their integrations relied on undocumented behavior. In large systems, operating systems, public APIs, browsers, and widely used libraries therefore require careful compatibility management.

### Origins

The law is named after Hyrum Wright, a software engineer who formed the observation while working at Google around 2011–2012. The source says Wright noticed that changes to core Google libraries, even changes that should have been invisible, often broke some project because that project depended on undocumented behavior.

The phrase “Hyrum’s Law” was coined by Titus Winters, Wright’s colleague and a coauthor of *Software Engineering at Google*.

### Example: JSON Key Ordering

Older Google JSON APIs did not promise stable key ordering, but implementations often sorted keys alphabetically by default. Consumers sometimes depended on that incidental behavior. If later optimizations randomized or changed the order for performance, those consumers could break even though the API never promised sorted keys.

The source uses this as an example of an observed non-contractual behavior becoming a dependency. Similar assumptions can appear in analytics dashboards or scripts that assume positional access, and in clients that assume specific sub-second timing for async responses.

### Example: Windows Compatibility and SimCity

The source describes how older Windows programs sometimes depended on behaviors that Microsoft never intended to guarantee. When Windows changed, those programs could break because they relied on undocumented behavior.

The original SimCity for Microsoft Windows 3.x is given as an example. The program used memory after freeing it, which is a use-after-free bug. In DOS and Windows 3.x this did not crash because memory allocated to a program was not immediately returned to the operating system. When Windows 95 beta testing exposed the crash, Microsoft engineers reportedly inspected SimCity, identified the cause, and added special compatibility behavior: if SimCity was running, Windows 95 used a memory allocator mode that did not return memory to the operating system until the program stopped. In effect, Windows deliberately preserved a memory leak to keep the application working.

The example shows Hyrum’s Law at operating-system scale: a bug in an application became a compatibility requirement for the platform because users depended on the application continuing to work.

### Example: Browser Quirks

Browsers also exhibit Hyrum’s Law. If Chrome, Firefox, or another browser implements a quirk and web developers build around it, that quirk can become part of the practical web platform. The browser cannot freely remove or change the behavior without risking breakage across existing websites.

This example matters because the web platform is not only the written specification. It is also the accumulated behavior that web pages assume from real browser implementations.

### Example: Sorted Lists from an Unordered API

A library may document that a function returns an unordered list, while the implementation happens to return a sorted list. Some users may start depending on the sorted order even though the contract explicitly says unordered. If the implementation later changes and returns a truly unordered result, those users’ code may fail.

This is the compact API version of the law: the maintainer’s written contract does not prevent consumers from depending on what they observe.

### Example: Timestamp Formatting

The source gives a user-facing integration example: an API may return a timestamp in a specific format as a helpful side effect. A consumer might parse that exact format. If the API owner later changes the format without realizing consumers depend on it, the integration breaks.

This example shows that de facto contracts can arise from convenience and habit, not only from formal documentation.

### Semantic Versioning and Deprecation

The law is especially relevant to API design and semantic versioning. A change that appears minor to the maintainer can be breaking from a consumer’s perspective because the consumer may depend on undocumented behavior. Maintainers therefore often use long deprecation cycles: a feature may be marked deprecated but supported for a long time because some unknown user likely depends on it.

The source does not say that maintainers can never change behavior. It says they should treat observable behavior as potentially load-bearing and change it through communication, compatibility paths, and deprecation discipline. ^[inferred]

### Relation to Leaky Abstractions

The source lists the Law of Leaky Abstractions as related. The relation is that both laws weaken the idea of a clean interface boundary. Leaky abstractions say lower-layer reality eventually breaks through an abstraction; Hyrum’s Law says consumers eventually depend on observable behavior outside the intended abstraction boundary. ^[inferred]

Together, they imply that software boundaries are social and empirical as well as technical: the real interface is shaped by what lower layers do and by what users learn to rely on. ^[inferred]

### Further Reading Preserved from the Source

- Titus Winters, Tom Manshreck, and Hyrum Wright, *Software Engineering at Google: Lessons Learned from Programming Over Time*, O’Reilly Media, 2020.
- hyrumslaw.com.

## Integration Decisions

This page should remain source-level because the pasted material is a chapter excerpt with origin notes, examples, and compatibility implications. A future concept page could promote the compact law itself, but the examples about JSON ordering, Windows compatibility, browser quirks, unordered lists, and timestamp formats belong here.

Hyrum’s Law should connect to [[wiki/topics/Modern Software Engineering]] because it explains why mature engineering practice treats compatibility, deprecation, and change management as part of software design rather than afterthoughts. It should also connect to [[wiki/sources/Law of Leaky Abstractions Source Guide]] because both sources describe why intended boundaries do not fully control real system behavior.

The source-reported SimCity compatibility story should stay source-level unless later verified against a primary source. Its role here is explanatory: it illustrates how observed behavior can become a compatibility obligation.

## Open Questions

- How should teams decide which undocumented behaviors deserve compatibility preservation and which should be intentionally broken?
- What observability or telemetry can reveal whether users depend on incidental behavior before maintainers change it?
- How should API docs distinguish between guaranteed contract, currently observed behavior, and implementation details that may change?

## Related

- [[wiki/sources/Law of Leaky Abstractions Source Guide]]
- [[wiki/sources/Galls Law Source Guide]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/concepts/System]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/maps/CS Map]]
