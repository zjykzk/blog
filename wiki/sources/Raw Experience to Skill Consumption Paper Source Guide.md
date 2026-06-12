---
title: >-
  Raw Experience to Skill Consumption Paper Source Guide
category: sources
type: source
status: draft
tags: [paper, arxiv, agents, skills, feedback]
sources:
  - https://arxiv.org/html/2605.23899v1
  - https://arxiv.org/abs/2605.23899
  - conversation:2026-06-11
created: 2026-06-11T21:58:46+0800
updated: 2026-06-11T22:36:02+0800
summary: >-
  Primary-paper guide for a lifecycle study of model-generated agent skills, covering experience generation, extraction, consumption, negative transfer, utility rubrics, and meta-skill guidance.
provenance:
  extracted: 0.84
  inferred: 0.14
  ambiguous: 0.02
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-06-11
aliases:
  - From Raw Experience to Skill Consumption
  - Model-Generated Agent Skills lifecycle study
  - arXiv:2605.23899
---

# Raw Experience to Skill Consumption Paper Source Guide

> Source: *From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills*, arXiv:2605.23899v1, submitted 2026-05-22.

## Capture Policy

This page preserves the primary-paper layer for the agent-skill lifecycle study. It should be used for paper-grounded claims about the study design, reported negative-transfer rates, experience-pool findings, skill-quality diagnostics, consumption behavior, and meta-skill-guided extraction.

This guide is distinct from the separate Denote reading note generated during the conversation. The Denote note is a personal reading artifact; this wiki page is the reusable source guide that integrates the paper into the structured wiki.

## What It Covers

The paper studies whether model-generated, domain-level agent skills actually help when extracted from prior execution traces and fed back to agents on new tasks. It evaluates the full trajectory-to-skill lifecycle across three stages:

```text
experience generation
  -> skill extraction
  -> skill consumption
  -> downstream utility
```

The core contribution is not a new skill optimizer. It is a measurement and diagnosis framework for when generated skills help, when they hurt, and what textual properties predict actual utility. This makes it directly relevant to [[wiki/concepts/Agent Skill]], [[wiki/topics/AI Skills Workflow]], [[wiki/concepts/Skill Self-Evolution]], and [[wiki/maps/Self-Evolving Agents Map]].

## Preserved Content

### Problem Statement

Agent skills are structured procedural artifacts distilled from past experience. The paper focuses on domain-level, model-generated skills because they are promising for fast adaptation: instead of hand-writing a skill for every domain, an extractor model can summarize a target model's past successes and failures into reusable guidance.

The open question is whether this pipeline is dependable. A skill can look plausible while doing nothing useful, or worse, pushing a model into negative transfer. The paper therefore asks three lifecycle questions:

- What kind of experience pool produces useful skills?
- What makes an extracted skill useful rather than merely readable?
- Why does the same skill help one consuming model and hurt another?

### Study Design

The evaluation fixes a deployment-like single-step evolution loop:

1. A target model runs training tasks in a domain and produces trajectories with outcomes.
2. An extractor model processes the trajectories and produces a domain-level skill.
3. The same target model consumes the skill on held-out tasks.
4. Skill utility is measured as the downstream performance difference between baseline and skill-augmented runs.

This design keeps the target model fixed while varying the extractor. It grounds the skill source in the target model's own behavior and failure modes, rather than in generic human-written advice.

The study spans five agentic task domains:

- ALFWorld
- SpreadsheetBench
- SWE-bench-Verified
- SEAL-0
- BFCL

The models include GPT, Gemini, and Qwen variants used both as extractors and consumers.

### Extraction Pipeline

The extraction pipeline has a map-reduce shape:

```text
single trajectory
  -> success patterns / failure patterns
  -> grouped consolidation
  -> domain-level skill
```

Each trajectory is analyzed independently. The extractor captures success patterns as reusable strategies and failure patterns as pitfalls or anti-patterns. The pattern sets are then hierarchically consolidated into a skill containing both what to do and what to avoid.

This matters because the paper does not treat a skill as generic advice. A skill should encode behavioral regularities observed in traces: procedures that led to completion and traps that caused failure.

### Main Result: Skills Help on Average but Often Hurt

The main experiment reports that model-generated skills improve downstream performance in 75% of evaluated extractor-target entries. However, 25% of entries show negative transfer, meaning the extracted skill makes the target model worse.

The negative-transfer rate depends strongly on domain:

- SpreadsheetBench and SWE-bench-Verified have the lowest negative rates, about 13%.
- ALFWorld is the most fragile domain, with a 47% negative rate.

The stable finding is that average improvement hides a serious deployment risk. Model-generated skills cannot be treated as universally beneficial simply because the mean gain is positive.

### Extractor Strength Does Not Equal Extraction Quality

The paper reports that an extractor model's own task-solving capability does not reliably predict the usefulness of the skills it extracts. A model can be strong as an extractor but weak as a consumer, or the reverse.

This separates three roles that are easy to conflate:

- task solver: can solve the benchmark task;
- extractor: can turn traces into useful skill text;
- consumer: can read and apply a skill effectively.

For wiki integration, this is an important distinction inside [[wiki/concepts/Agent Skill]] and [[wiki/topics/AI Skills Workflow]]: skill quality is not only a property of the text; it is a property of the text interacting with a consuming model and task domain. ^[inferred]

### Experience Generation: Success and Failure Teach Different Things

The paper manipulates the success/failure composition of the experience pool. It samples pools with success ratios of 100%, 75%, 50%, 25%, and 0%, then extracts skills from each pool.

The first finding is simple: all-failure pools consistently perform worst. Successful trajectories provide the positive procedural signal that tells an agent how to reach completion, not merely what to avoid.

The second finding is more domain-specific: the best success-failure mix varies by domain. SpreadsheetBench favors more successful trajectories, because successful traces show how to inspect and modify workbook structure. ALFWorld can benefit from more failure-heavy pools, because failures reveal invalid actions, dead-end states, and shallow inspection mistakes.

The resulting principle is:

```text
success traces give routes
failure traces give guardrails
the best mix depends on what the domain teaches through each
```

### Extraction: Textual Plausibility Does Not Predict Utility

The paper asks language models to judge which of two skills is better from text alone. This pairwise judge performs no better than chance.

The most striking number is the high-margin case: when two skills differ by at least 5 percentage points in downstream utility, the judge picks the higher-utility skill only 15.8% of the time. The larger the actual utility gap, the more the text-only judge can invert the real answer.

This is the paper's most important caution. A skill that reads like a good document is not necessarily a skill that changes agent behavior in the right direction.

### SpreadsheetBench Contrast: Concrete Failure Mechanisms Matter

The qualitative SpreadsheetBench comparison explains the gap. A high-utility skill names domain-specific failure mechanisms and gives executable remedies, such as precomputing static values when the host environment does not evaluate formula strings.

A lower-utility skill gives process-level directives such as resolving the contract before coding or editing minimally. These are reasonable instructions, but they are too abstract to prevent the concrete failure modes that dominate SpreadsheetBench.

The distinction is:

```text
low-utility skill:
  "verify results"

high-utility skill:
  "if the grader reads cell values without recalculating formulas,
   compute static values and write those values into the workbook"
```

The second form is more useful because it identifies the failure mechanism, trigger condition, and corrective action.

### Skill Consumption: Same Skill, Different Consumers

The paper also studies how the same skill behaves across different target models. A skill's utility is not fixed across consumers. Some models can turn a skill into better behavior; others may over-follow, misread, or spend extra exploration budget without improving final execution.

This implies that skill evaluation should include consumer behavior, not just skill text. In practical systems, a skill library may need consumer-specific validation or routing policies. ^[inferred]

### Meta-Skill Guided Extraction

The paper turns its diagnostic findings into an intervention. It builds an extraction-quality guidance block, or meta-skill, that instructs the extractor to prioritize properties that actually predict utility.

The raw contrastive analysis identifies seven plausible dimensions, but only three survive utility validation:

1. Name concrete failure mechanisms.
2. Provide executable, domain-grounded remedies.
3. Include high-risk action warnings or anti-patterns.

When this three-dimension utility-validated rubric guides extraction, it improves all nine tested cells and raises average performance by 1.55 points. A broader seven-dimension plausibility rubric hurts on average by 0.59 points.

This result is important because it shows that extraction guidance should be selected by downstream utility, not by surface document quality.

### Relation to Skill Self-Evolution

The paper is adjacent to skill self-evolution work but has a different role. [[wiki/sources/Skills-Coach Paper Source Guide]] probes and improves individual skills through generated boundary tasks. SkillOpt optimizes a persistent skill document through validation-gated text edits. [[wiki/sources/SkillOS Paper Source Guide]] trains repository-level curation policy.

This paper supplies the diagnostic layer underneath those systems: before optimizing or curating skills, one must know which skill properties actually correlate with downstream behavior.

## Integration Decisions

This page should be the primary link for factual claims about arXiv:2605.23899: its lifecycle evaluation design, negative-transfer rates, experience-pool results, text-judge inversion, and meta-skill-guided extraction intervention.

The paper strengthens [[wiki/concepts/Agent Skill]] by showing that skill quality is not equivalent to readability. A useful skill should encode concrete failure mechanisms, domain-specific triggers, and executable remedies.

The paper strengthens [[wiki/concepts/Skill Self-Evolution]] by adding a diagnostic precondition: self-evolution needs a utility-grounded rubric, or the system may optimize toward plausible but harmful skill text. ^[inferred]

The paper also belongs in [[wiki/maps/Self-Evolving Agents Map]] because it connects raw execution traces to skill extraction and skill consumption, even though it is primarily a study rather than a new self-evolving system.

Source-level numerical claims, including 75% improvement entries, 25% negative transfer, ALFWorld's 47% negative rate, the 15.8% high-margin judge accuracy, +1.55 average gain for the validated rubric, and -0.59 for the plausibility rubric, should remain tied to this source until independently replicated.

## Open Questions

- Can a skill library route different versions of the same domain skill to different consumer models based on measured consumption ability?
- How stable are the three validated dimensions across domains beyond the five evaluated benchmarks?
- Can a downstream utility rubric be learned continuously from production traces without letting bad feedback harden into future skill guidance? ^[inferred]
- How should generated skills be tested when the skill changes model attention allocation rather than directly changing the task procedure? ^[inferred]

## Related

- [[wiki/concepts/Agent Skill]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/concepts/Skill Self-Evolution]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/maps/Self-Evolving Agents Map]]
- [[wiki/sources/Skills-Coach Paper Source Guide]]
- [[wiki/sources/SkillOS Paper Source Guide]]
