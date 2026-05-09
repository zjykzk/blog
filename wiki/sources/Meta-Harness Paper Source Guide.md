---
title: Meta-Harness Paper Source Guide
type: source
status: seed
category: sources
summary: Source guide for the Meta-Harness paper, focused on automated search over executable model harnesses using full filesystem access to code, scores, and traces.
sources:
  - https://arxiv.org/abs/2603.28052
provenance:
  extracted: 0.86
  inferred: 0.12
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-05-09
created: 2026-05-09T22:42:07+08:00
updated: 2026-05-09T22:42:07+08:00
aliases:
  - Meta-Harness paper
  - Meta-Harness source guide
tags:
  - paper
  - arxiv
  - ai
  - agents
  - harness
---

# Meta-Harness Paper Source Guide

## Source Identity

- Title: Meta-Harness: End-to-End Optimization of Model Harnesses
- Authors: Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn
- arXiv: 2603.28052v1, cs.AI, 30 Mar 2026
- URL: https://arxiv.org/abs/2603.28052
- Project page: https://yoonholee.com/meta-harness/
- Optimized harness artifact: https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact

## Extraction Notes

The arXiv HTML and PDF were both accessible. The wiki extraction used arXiv HTML for readable text and the PDF bytes for the manifest content hash.

## Central Contribution

The paper introduces [[wiki/concepts/Meta-Harness]], an outer-loop system that searches over executable harness code around a fixed LLM.

Its central claim is that harness engineering needs richer feedback than scalar scores or short summaries because failures may depend on long-horizon interactions among prompt construction, retrieval, memory updates, state transitions, tool calls, and evaluation traces.

## What Should Be Promoted

- The stable concept of [[wiki/concepts/Meta-Harness]] as trace-driven program search over harness code.
- The distinction between optimizing model weights and optimizing the executable [[wiki/topics/AI Harness]] around the model.
- The claim that raw execution traces can contain diagnostic signal that summaries erase.
- The practical engineering pattern: write a skill, log everything, make logs queryable, validate cheaply, and run evaluation outside the proposer.

## What Should Stay Source-Level

- Exact per-dataset table values beyond the headline comparisons.
- The detailed TerminalBench-2 leaderboard ranking, because the benchmark is public and search/evaluation use the same task set.
- Claims about the irreproducibility of other leaderboard systems unless corroborated by those systems' own source materials.
- Implementation details of the artifact repository until inspected directly.

## Key Results

- Online text classification: Meta-Harness improves over ACE by 7.7 points while using roughly 4x fewer context tokens.
- Retrieval-augmented math reasoning: one discovered retrieval harness improves average accuracy by 4.7 points across five held-out models on 200 IMO-level problems.
- Agentic coding: discovered harnesses surpass Terminus-KIRA and rank highly on TerminalBench-2 under the paper's reported evaluation.
- Ablation: full access to raw traces substantially outperforms scores-only and scores-plus-summary interfaces.

## Relationship to Existing Wiki Threads

This paper strengthens several existing threads:

- [[wiki/topics/AI Harness]]: harness is not just runtime plumbing; it is a search space.
- [[wiki/concepts/Harness Ratchet]]: repeated failures can become durable harness changes, and Meta-Harness automates part of that ratchet.
- [[wiki/concepts/Continual Learning for AI Agents]]: harness-level learning can improve systems without weight updates.
- [[wiki/topics/Context Management]]: context policies can themselves be optimized as code, not only hand-designed.
- [[wiki/syntheses/Agent System Design Space]]: the design space now includes who or what performs harness evolution.

## Open Questions Raised

- How much does the method depend on frontier coding-agent quality?
- How should benchmark-specific search be separated from benchmark overfitting?
- Can the same outer loop safely optimize security-, authorization-, or governance-sensitive harness components?
- What is the right interface between automated harness search and human review? ^[inferred]

## Related

- [[wiki/concepts/Meta-Harness]]
- [[wiki/sources/Agent Systems Papers Source Guide]]
- [[wiki/sources/GenericAgent Paper Source Guide]]
- [[wiki/sources/Continual Learning for AI Agents Source Guide]]
- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/Agent System Design Space]]
