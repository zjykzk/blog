---
title: >-
  Structured-Prompt-Driven Development Source Guide
type: source
status: draft
category: sources
tags:
  - article
  - software-engineering
  - ai-coding
  - architecture
  - testing
sources:
  - https://martinfowler.com/articles/structured-prompt-driven/
  - conversation:2026-05-17
created: 2026-05-17T22:18:34+08:00
updated: 2026-05-17T22:18:34+08:00
summary: >-
  Source guide for Thoughtworks' SPDD article, preserving REASONS Canvas, prompt/code sync workflow, billing example, fit boundaries, and Q&A caveats.
provenance:
  extracted: 0.86
  inferred: 0.12
  ambiguous: 0.02
base_confidence: 0.55
lifecycle: draft
lifecycle_changed: 2026-05-17
aliases:
  - SPDD Source Guide
  - Structured Prompt-Driven Development
---

# Structured-Prompt-Driven Development Source Guide

> Source: [Structured-Prompt-Driven Development (SPDD)](https://martinfowler.com/articles/structured-prompt-driven/), Wei Zhang and Jessie Jie Xia, MartinFowler.com, 2026-04-28; Q&A added 2026-05-04.

## Capture Policy

This page preserves the article as a source-layer artifact. SPDD's claimed outcomes, fit ratings, tool behavior, and roadmap remain source-reported unless later corroborated by independent practice or promoted into [[wiki/topics/Spec-Driven Development]].

## What It Covers

The article presents Structured-Prompt-Driven Development as a team-level AI coding workflow from Thoughtworks internal IT. Its central move is to treat structured prompts as maintained delivery artifacts that travel with the code in version control, so AI-assisted changes become reviewable, reusable, auditable, and less dependent on scattered chat history.

The article belongs in the wiki because it extends the existing [[wiki/topics/Spec-Driven Development]] cluster with a concrete prompt-as-spec workflow, a named canvas, CLI commands, a billing-engine example, and a candid Q&A about variance, hotfixes, model drift, human review, asset verification, and decision memory.

## Preserved Content

### Problem frame: individual speed is not system throughput

The opening distinguishes local developer speed from delivery-system speed. AI coding assistants can help one developer draft, modify, and refactor code faster, but the full lifecycle still suffers when requirements are ambiguous, reviews must process larger diffs, generated output is inconsistent, and production risk becomes harder to reason about.

SPDD answers a governance question rather than a code-generation question: how can teams make AI-generated changes governable, reviewable, and reusable without losing quality?

### SPDD definition

Structured-Prompt-Driven Development treats prompts as first-class delivery artifacts. A structured prompt is not a disposable chat instruction; it is an asset that captures requirements, domain language, design intent, constraints, task breakdown, norms, and safeguards.

This makes the prompt a boundary object between business intent, software design, LLM execution, review, and future iteration. In the article's framing, SPDD shifts AI assistance from personal productivity toward organization-level delivery capability.

### REASONS Canvas

The REASONS Canvas is the article's main structured-prompt template. It moves from intent and design, through execution, into governance:

| Letter | Dimension | Function |
|---|---|---|
| R | Requirements | Problem, value, scope, acceptance criteria, and definition of done. |
| E | Entities | Domain entities, relationships, language, and core business concepts. |
| A | Approach | Implementation strategy and design direction. |
| S | Structure | Where the change fits in the system, including components and dependencies. |
| O | Operations | Concrete, testable implementation tasks and sequencing. |
| N | Norms | Cross-cutting engineering standards such as naming, observability, and defensive coding. |
| S | Safeguards | Non-negotiable boundaries such as invariants, performance limits, and security constraints. |

The article's key claim is that the Canvas lets reviewers reason about a single structured artifact before reviewing code. This reduces reliance on implicit team memory and narrows the variance of free-form prompting. It does not eliminate human judgment.

### Workflow rule: fix the prompt first when behavior changes

SPDD brings prompt artifacts into the same discipline as code: version control, review, and quality gates. Its central workflow rule is:

- Logic or business behavior changes flow requirements -> prompt -> code.
- Refactoring or internal structure changes flow code -> prompt.

This creates two-way sync instead of a one-way handoff. If reality diverges from the prompt, the prompt is corrected before code is regenerated or updated. If code is refactored without changing observable behavior, the code can move first and the prompt is synchronized afterward.

This distinction is important because it keeps the prompt as the current intent record rather than an obsolete plan.

### openspdd command surface

The article describes `openspdd` as the CLI/tooling layer that implements repeatable SPDD steps:

| Command | Role |
|---|---|
| `/spdd-story` | Optional splitting or standardization of larger requirements into deliverable user stories. |
| `/spdd-analysis` | Extracts domain terms, scans relevant code, identifies concepts, rules, risks, and design direction. |
| `/spdd-reasons-canvas` | Produces the full REASONS Canvas from business context and codebase state. |
| `/spdd-generate` | Generates code task by task according to Operations, Norms, and Safeguards. |
| `/spdd-api-test` | Optional functional API test generation with normal, boundary, and error cases. |
| `/spdd-prompt-update` | Updates the Canvas when requirements, architecture, or constraints change. |
| `/spdd-sync` | Synchronizes code-side refactors or fixes back into the Canvas. |
| `/spdd-code-review` | In Q&A, described as comparing the Canvas and code diff for alignment. |

The command vocabulary is important because SPDD is not just a prompt template. It is a workflow harness around prompt assets, code generation, tests, review, and synchronization. ^[inferred]

### Billing-engine walkthrough

The tutorial example enhances a simple LLM billing engine. The existing system calculates bills from token usage. The enhancement introduces model-aware pricing and multi-plan billing:

- The API receives a required `modelId`.
- Standard-plan overage keeps the existing quota model but changes overage pricing by model.
- Premium-plan billing has no quota and charges prompt/completion tokens separately by model.
- The design should isolate formulas through an extensible routing pattern such as Strategy or Factory.

The workflow starts by turning the enhancement idea into a simplified user story with business value, scope, exclusions, and Given/When/Then acceptance criteria. The example deliberately keeps scope boundaries tight: calculate the current bill only; do not build customer CRUD, historical billing queries, subscription management, model management, or invoice generation.

### Analysis before generation

Before implementation, `/spdd-analysis` turns the clarified story into strategic analysis grounded in the codebase. The article emphasizes that this stage should stay at the "what and why" level:

- Existing and new domain concepts.
- Business rules and relationships.
- Strategic design direction.
- Risks, ambiguities, edge cases, and acceptance-criteria coverage.

Human review at this stage checks alignment with architecture and business intent. In the example, review focuses on whether the Strategy Pattern is appropriate, whether OOP principles such as ISP and SRP are respected, whether the field-addition strategy is valid, and whether unanticipated risks appear.

The authors accept the analysis when the strategic direction is aligned, even though granular implementation details are not yet fully known. The next stage asks the AI to simulate implementation details inside the agreed frame, making hidden issues easier to inspect.

### Structured prompt before code

`/spdd-reasons-canvas` translates the accepted analysis into a REASONS Canvas. The article treats this as a deeper intent-alignment checkpoint: reviewers inspect how the model carries strategy into abstractions, structures, concrete operations, norms, and safeguards.

When the structured prompt needs changes, the article discourages manual editing of the prompt file. The intended loop is:

1. Identify the missing or wrong intent.
2. Provide the correction in conversation.
3. Let the AI update only the affected sections of the prompt artifact.

This keeps the prompt history and structure inside the workflow rather than turning it into a hand-edited document with unclear provenance.

### Code generation and review

`/spdd-generate` reads the Canvas and generates implementation tasks in the order defined by Operations. The article's review focus is:

- Whether the code follows the intended architecture.
- Whether service-layer business logic matches the original intent.
- Whether the change stays inside the structured prompt's boundary.

The article reports that the example generated code largely met expectations, with remaining issues such as magic numbers deferred until after core functional validation.

### Functional tests before deeper code review

The walkthrough generates a cURL-based API test script using `/spdd-api-test`, runs it, and reports that functional tests passed. This sequence intentionally validates observable behavior before investing heavily in code review.

In Q&A, the authors explain that this is not a rejection of TDD's purposes. SPDD distributes those purposes differently:

- API tests validate the system boundary before expensive human review.
- Code review then focuses on architecture, trade-offs, logic, and non-functional concerns.
- Unit tests come later as a regression safety net after implementation stabilizes.

This is one of SPDD's sharper departures from classic test-first workflows and should remain source-level until compared against real team practice. ^[ambiguous]

### Final adjustments: behavior changes vs refactoring

The article separates final adjustments into two classes:

- **Logic corrections:** behavior-changing fixes update the prompt first, then regenerate or update code. Example: deciding that historical missing `modelId` should default to `fast-model`.
- **Refactoring:** behavior-preserving structure or style cleanup changes code first, then syncs the prompt back to the current implementation. Example: extracting magic numbers into constants.

This distinction maps to an intent/implementation split: business truth is captured in the prompt before code moves; internal cleanup can start in code so long as the prompt is synchronized after.

### Unit-test generation

The article treats unit tests as the final sign-off for core logic. At the time of writing, SPDD did not yet have finalized dedicated unit-test commands, so the example uses a template-driven test prompt:

1. Combine implementation details with a testing template.
2. Generate a structured test prompt.
3. Deduplicate against existing tests.
4. Generate unit-test code from the refined prompt.
5. Run the full test suite.

The reported outcome for the example includes high intent alignment, implementation transparency, a synchronized prompt asset, and accumulated developer expertise. These are source claims, not independent measurements.

### Three core developer skills

The article identifies three human skills required for effective SPDD:

- **Abstraction first:** define objects, collaborations, boundaries, and design before code generation.
- **Alignment:** make scope, non-scope, standards, and hard constraints explicit before implementation.
- **Iterative review:** treat AI output as a controlled engineering loop, not a one-shot draft.

The human role shifts from typing code toward modelling, framing, reviewing intent, and maintaining the workflow.

### Fit assessment

The article rates SPDD as strongest for:

- Scaled, standardized delivery.
- Logic-heavy business workflows.
- Compliance-heavy or hard-constraint environments.
- Team collaboration and auditability.
- Cross-cutting consistency work across services or languages.

It rates SPDD as weak for:

- Emergency hotfixes during active incident response.
- Exploratory spikes.
- Disposable one-off scripts.
- Poorly bounded domains with unclear business rules.
- Taste-driven creative or visual work.

The core boundary is not model intelligence alone. SPDD works when the problem can be bounded, decomposed, modelled, and verified.

### Trade-offs and adoption barriers

The article frames SPDD as an engineering investment. Its expected benefits are determinism, traceability, faster reviews, explainability, and safer evolution. Its costs are mindset shift, senior expertise up front, and automation tooling.

This matters because SPDD can look like an expert-only method. The authors' stated direction is to move more of the burden into organization-level assets, reusable commands, asset verification, and decision memory.

### Q&A caveats

The Q&A section is unusually important because it states SPDD's current limits:

- Global rules and hooks do not replace SPDD because they operate at a broader level; SPDD makes the generation plan itself inspectable.
- Compared with progressive-disclosure instructions, SPDD's distinctive artifact is a maintained structured prompt file with fixed shape, intent-first workflow, operations breakdown, and two-way prompt/code sync.
- SPDD does not yet close an autonomous AI learning loop. The loop is closed by workflow and artifacts, with humans still gatekeeping core decisions.
- The Canvas narrows variance but does not remove it. A weak Canvas can still be structurally complete and substantively under-specified.
- The scaling ceiling often comes from problem boundary clarity and accumulated decision assets, not raw model capability.
- SPDD is intended to be model-agnostic, but stronger reasoning models produce better analysis and canvases. Teams should consciously decide whether the artifact is just prompt-as-spec or prompt plus model configuration.
- Additional prompt engineering is needed when behavior mismatches acceptance criteria, generated logic is overcomplicated, or instructions/norms/safeguards are violated.
- Six workflow steps distribute cognitive load so reviewers can engage with narrower decisions.
- Hotfix governance is deferred rather than skipped: during incidents recovery comes first; after recovery, failures should be fed back into existing prompts or documented as new assets.
- Agent review can check Canvas/code alignment, but humans still catch whether the Canvas matches real business intent and learn from the model's choices.

### Roadmap

The article names four future directions:

- Capture more recurring workflows as commands.
- Add automated verification at the asset layer for analysis, Canvas, and prompt artifacts.
- Raise the automation ratio only where reliability is proven.
- Build decision memory so historical canvases, trade-offs, and accepted patterns can be retrieved as persistent context.

This roadmap connects SPDD directly to [[wiki/concepts/Context Anchoring]], [[wiki/concepts/Agentic Engineering]], and [[wiki/topics/AI Memory]]: the durable asset is not only code but also the reasoning structure that constrains future code generation. ^[inferred]

## Integration Decisions

This source should strengthen [[wiki/topics/Spec-Driven Development]] with a concrete "prompt-as-maintained-spec" variant. It is narrower than full spec-as-source and more operational than generic design-first collaboration.

SPDD should not be collapsed into [[wiki/syntheses/AI Engineering Workflow]] yet. The source adds a workflow and artifact family, but its claims about 99% intent alignment, review speed, and quality improvement are single-source practitioner claims.

The REASONS Canvas can later become a concept page if multiple sources or local practice validate it. For now it remains source-level to avoid making one organization's template look like a universal method.

SPDD adds a useful contrast to [[wiki/sources/Spec-Driven Development Paper Source Guide]]: the paper provides a broader SDD discipline spectrum; the Thoughtworks article gives a concrete prompt-driven workflow with CLI commands, prompt/code synchronization, and decision-memory ambitions.

It also connects to [[wiki/syntheses/Use Cases as AI Coding Traceability Anchors]] because SPDD starts from user stories and acceptance criteria, then carries that intent through analysis, Canvas, generated code, API tests, review, and unit tests.

## Open Questions

- Can asset-layer verification reliably judge whether a REASONS Canvas is substantively sufficient, not merely well-structured?
- How much of SPDD's benefit comes from the Canvas structure versus the surrounding review discipline and CLI workflow?
- Does functional-test-first sequencing improve human review leverage in real teams, or does it weaken design feedback compared with earlier unit-test generation?
- How portable are SPDD prompt assets across model families, provider updates, and local/offline execution?
- What decision-memory architecture is needed so past canvases and trade-offs become useful context without freezing obsolete assumptions?

## Related

- [[wiki/topics/Spec-Driven Development]]
- [[wiki/sources/Spec-Driven Development Paper Source Guide]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/concepts/AI Collaboration Scaffolding]]
- [[wiki/concepts/Design-First Collaboration]]
- [[wiki/concepts/Context Anchoring]]
- [[wiki/concepts/Agentic Engineering]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/syntheses/Use Cases as AI Coding Traceability Anchors]]
- [[wiki/topics/AI Memory]]
