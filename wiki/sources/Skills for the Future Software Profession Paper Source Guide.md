---
title: "Skills for the Future Software Profession Paper Source Guide"
type: source
status: draft
category: sources
tags: [paper, arxiv, software-engineering, ai-coding, verification]
aliases:
  - "Skills for the future software profession: beyond agentic AI!"
  - "Future Software Profession Paper"
relationships:
  - target: "[[wiki/concepts/Executable Specification]]"
    type: uses
  - target: "[[wiki/concepts/Cognitive Debt]]"
    type: related_to
  - target: "[[wiki/concepts/Agentic Engineering]]"
    type: related_to
sources:
  - https://arxiv.org/pdf/2606.21894
summary: Position paper arguing that future software engineers shift from code production toward executable specifications, agentic workflow architecture, and stewardship against cognitive debt.
provenance:
  extracted: 0.92
  inferred: 0.08
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-07-12
tier: supporting
created: 2026-07-12T00:30:14+0800
updated: 2026-07-12T00:30:14+0800
---

# Skills for the Future Software Profession: Beyond Agentic AI!

> [!tldr] As coding agents make implementation cheaper, the paper argues that software engineers' defining work moves to executable V&V artifacts, trustworthy agentic pipelines, and preservation of architectural and organizational understanding.

## Source Context

Sungmin Kang, Baishakhi Ray, and Abhik Roychoudhury synthesize two 2026 roundtables on Trustworthy AI for Code, held in Singapore and New York with roughly 30–40 participants each from academia and industry. The paper is a five-page position paper, not a controlled empirical study: its evidence is expert discussion, surveys, and practitioner anecdotes rather than a quantitative benchmark.

## Problem & Motivation

Coding agents now participate across the SDLC: code generation, review, test production, and design advice. The paper asks what remains a defining human competency when agents increasingly automate implementation.

Its core diagnosis is a bottleneck shift. When code generation becomes inexpensive, software assurance—not software production—becomes scarce. Manual review becomes a weak final safeguard when developers accept more generated code with limited scrutiny. Trust therefore has to move upstream into machine-checkable specifications and verification-and-validation artifacts.

## Proposed Workflow

![[wiki/attachments/skills-future-software-profession-fig1.png]]
*Figure 1 (Kang, Ray, and Roychoudhury, 2026): the future engineer distills requirements into V&V artifacts, assembles specialized agent pipelines, and maintains architectural understanding plus non-code artifacts.*

The workflow has three coupled responsibilities:

1. **Distill requirements into V&V artifacts.** Converse with users, then produce or review executable tests and formal specifications that make intended behavior checkable.
2. **Assemble agentic pipelines.** Combine domain requirements, tests, and specifications with coding, verification, and testing agents; evaluate whether the resulting workflow is robust and aligned with organizational constraints.
3. **Maintain understanding and minimize cognitive debt.** Keep humans responsible for architecture and maintain requirements, tests, specifications, code, and agent trajectories as a coherent artifact system.

The paper's deeper move is from “humans write, machines assist” to “agents produce, humans architect, govern, and steward.”

## Executable Specifications and V&V

[[wiki/concepts/Executable Specification|Executable specifications]] translate user intent into machine-checkable artifacts that guide and evaluate generated implementations. The authors distinguish generating a specification from judging its quality: even if agents infer tests or formal properties from documentation, issues, and code, humans still need to assess fidelity to intent, completeness, and assurance level.

The paper argues that formal proof search is becoming increasingly automatable, so the harder problem moves toward inferring the *right* specification. High-level verification may also require localized helper lemmas discovered through program analysis. Code and inferred specifications can drift as either evolves, creating a need for continuous consistency checking.

This makes conflicting evidence a first-class engineering problem: tests, specifications, and implementations may disagree, and passing one artifact does not automatically validate the others.

## Agentic Architecture

The authors use “agentic architecture” for the design of systems composed of specialized agents. The design surface includes task decomposition, communication protocols, coordination, failure localization, recovery, human oversight, security, compliance, and governance.

This is close to [[wiki/concepts/Agentic Engineering]], but the paper emphasizes architecture of the *agent pipeline* rather than only the surrounding coding harness. Engineers increasingly compose coding, verification, and testing agents much as earlier architects composed software components, while managing trust rather than only scale. ^[inferred]

## Cognitive Debt

[[wiki/concepts/Cognitive Debt|Cognitive debt]] arises when developers and organizations lose understanding of the intent, architecture, and rationale behind software generated or maintained by agents. Unlike technical debt, the deficit can exist mainly in human and organizational understanding even when the code still appears healthy.

The proposed countermeasures are structural:

- assign human custodians responsibility regardless of who or what authored the code;
- keep architectural decisions under human ownership;
- preserve requirements, executable specifications, agent instructions, tool policies, design rationale, and trajectories beside implementation;
- develop full-lifecycle engineers who steward AI-assisted systems over time;
- use structured repositories and semantic representations to preserve consistency and institutional knowledge.

## Results and Evidence

The paper reports no benchmark, ablation, statistical analysis, or core equation. Its result is a qualitative agenda distilled from two expert roundtables:

| Proposed competency | Bottleneck it addresses | Primary trust artifact |
|---|---|---|
| Requirements → executable V&V | Cheap code, expensive assurance | Tests and formal specifications |
| Agentic workflow architecture | Fragile multi-agent composition | Protocols, decomposition, oversight, recovery |
| Cognitive-debt management | Loss of intent and system understanding | Architecture, rationale, policies, trajectories |

## Educational Implications

Future curricula should train students to:

- convert business and domain requirements into executable specifications;
- judge whether inferred specifications faithfully capture intent;
- reason across conflicting tests, specifications, and implementations;
- compose agents and subagents into trustworthy pipelines;
- retain architectural responsibility and domain expertise;
- treat governance, security, compliance, and long-term stewardship as part of software construction.

The paper does not require every engineer to become a formal-methods specialist. It argues instead for specification literacy: enough understanding to choose an assurance level, inspect inferred artifacts, and know what evidence is still missing.

## Limitations

- The recommendations come from two invited roundtables; participant selection and discussion synthesis may not represent the wider profession.
- The paper proposes a future workflow but does not measure whether it improves correctness, productivity, or developer understanding.
- “Agentic architecture” remains an agenda rather than a validated discipline with established design laws.
- Human architectural ownership may reduce cognitive debt, but the paper does not specify operational measures for detecting or pricing that debt. ^[inferred]
- The argument assumes continued growth in coding-agent capability and adoption; the pace and distribution of that shift may vary by domain. ^[inferred]

## Related

- [[wiki/concepts/Executable Specification]]
- [[wiki/concepts/Cognitive Debt]]
- [[wiki/concepts/Agentic Engineering]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Verification Gap]]
- [[wiki/topics/Spec-Driven Development]]
- [[wiki/syntheses/AI 时代开发岗位分层与协作]]
- [[wiki/sources/Spec-Driven Development Paper Source Guide]]

## Sources

- <https://arxiv.org/abs/2606.21894>
- <https://arxiv.org/pdf/2606.21894>
