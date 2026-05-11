---
title: Skills-Coach Paper Source Guide
category: sources
tags:
  - paper
  - arxiv
  - agents
  - skills
aliases:
  - Skills-Coach paper
  - Skills-Coach source guide
sources:
  - https://arxiv.org/abs/2604.27488
summary: Source guide for the Skills-Coach paper, focused on automated skill boundary probing, training-free GRPO optimization, comparative execution, and Skill-X evaluation.
provenance:
  extracted: 0.84
  inferred: 0.14
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: "2026-05-11"
created: 2026-05-11T12:08:45+08:00
updated: 2026-05-11T12:08:45+08:00
---
# Skills-Coach Paper Source Guide

## Source Identity

- Title: Skills-Coach: A Self-Evolving Skill Optimizer via Training-Free GRPO
- Authors: Yu Tian, Jiawei Chen, Lifan Zheng, Mingxiang Tao, Xinyi Zeng, Zhaoxia Yin, Hang Su, Xian Sun
- arXiv: 2604.27488v1, cs.CL, submitted 30 Apr 2026
- URL: https://arxiv.org/abs/2604.27488
- DOI: https://doi.org/10.48550/arXiv.2604.27488
- Code: https://github.com/T1aNS1R/Skills-Coach
- Clawhub: https://clawhub.ai/t1ans1r/skills-coach

## Extraction Notes

The arXiv HTML and PDF were both accessible. The wiki extraction used arXiv HTML for readable text and the PDF bytes for the manifest content hash.

## Central Contribution

The paper introduces Skills-Coach, an automated framework for [[wiki/concepts/Skill Self-Evolution]]. It targets a specific [[wiki/concepts/Agent Skill]], explores its capability boundaries, generates improved versions, compares original and optimized execution, and emits structured reports.

The source frames skills as modular capability extensions composed of instructions, scripts, and resources. Its motivating problem is that large skill ecosystems can have high volume but fragmented coverage, so individual skills may fail on complex or edge-case tasks.

## Framework Structure

Skills-Coach contains four modules:

1. **Diverse Task Generation Module**: parses skill files such as `Skill.md` and `Readme.md`, extracts commands, parameters, constraints, examples, I/O formats, and failure cases, then creates standard, advanced, and boundary tasks.
2. **Lightweight Optimization Module**: uses training-free GRPO to generate and select instruction variants, while code-inclusive skills can also receive caching, validation, error-handling, command optimization, and auto-fixes.
3. **Comparative Execution Module**: runs original and optimized skills on the same tasks in isolated workspaces, capturing outputs, errors, return codes, generated files, and logs.
4. **Traceable Evaluation Module**: scores execution artifacts against explicit criteria, computes metrics, compares versions, and makes retain-or-discard decisions.

The system supports a virtual mode that estimates success from instruction text and deterministic hashing, and a real mode that evaluates actual outputs, logs, and files.

## Benchmark Claims to Preserve

The paper introduces Skill-X, a benchmark of 48 skills sourced from Anthropic, Clawhub, Vercel Labs, and SkillSh. It includes 29 instruction-only skills and 19 code-inclusive skills.

Headline reported results on Skill-X:

- All skills: average score improves from 0.378 to 0.84; pass rate improves from 33.59% to 88.02%.
- Instruction-only skills: average score improves from 0.388 to 0.839; pass rate improves from 37.93% to 91.38%.
- Code-inclusive skills: average score improves from 0.343 to 0.842; pass rate improves from 26.97% to 82.89%.
- Standard-task score improves from 43.00% to 87.43% overall.
- Advanced-task score improves from 32.71% to 81.61% overall.

These figures should remain source-level claims unless corroborated by independent replications or inspections of the released code and benchmark. ^[ambiguous]

## What Should Be Promoted

- [[wiki/concepts/Skill Self-Evolution]] as a distinct loop for improving skills through generated tests, optimization, execution, and evaluation.
- The idea that skill quality includes behavioral coverage over boundary tasks, not only instruction-file completeness.
- The connection between skill optimization and [[wiki/concepts/Continual Learning for AI Agents]]: skills are an inspectable update surface between raw context and full harness code.
- The warning that large skill marketplaces create a coverage and quality-control problem, not merely an abundance of reusable capabilities. ^[inferred]

## What Should Stay Source-Level

- Exact Skill-X table values for every individual skill.
- The implementation details of the released repository until directly inspected.
- Claims that training-free GRPO generally outperforms other optimization strategies outside the Skill-X setup.
- Virtual-mode scoring behavior as an engineering shortcut rather than a stable evaluation principle.

## Relationship to Existing Wiki Threads

- [[wiki/concepts/Agent Skill]]: adds a capability-boundary and optimization lens to existing skill authoring principles.
- [[wiki/topics/AI Skills Workflow]]: turns skill maintenance into an evaluation-driven workflow rather than one-off prompt polishing.
- [[wiki/concepts/Harness Ratchet]]: failed skill executions can become durable instruction, example, or code updates.
- [[wiki/concepts/Verification Loop]]: optimized skills should be admitted only after external task evaluation.
- [[wiki/syntheses/Agent System Design Space]]: adds a skill-evolution surface beside model learning, harness learning, context learning, and harness-code search.
- [[wiki/sources/Meta-Harness Paper Source Guide]]: adjacent paper for outer-loop optimization, but Meta-Harness optimizes executable harnesses while Skills-Coach optimizes skills.

## Open Questions Raised

- How should automatic skill changes be reviewed before being shared across teams? ^[inferred]
- Does Skill-X reward genuinely better skill behavior, or mainly reward documentation structures that match its criteria? ^[ambiguous]
- Can real-mode evaluation be made safe for skills with destructive, networked, or credential-sensitive actions? ^[inferred]
- How should skill optimization handle conflicts among skills in the same ecosystem? ^[inferred]

## Related

- [[wiki/concepts/Skill Self-Evolution]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/concepts/Continual Learning for AI Agents]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/sources/Agent Systems Papers Source Guide]]
- [[wiki/sources/Meta-Harness Paper Source Guide]]
