---
title: Meta-Harness
type: concept
status: seed
category: concepts
summary: Meta-Harness is an outer-loop system that uses a coding-agent proposer to search over executable LLM harness code using prior code, scores, and traces.
sources:
  - https://arxiv.org/abs/2603.28052
provenance:
  extracted: 0.82
  inferred: 0.16
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-05-09
created: 2026-05-09T22:42:07+08:00
updated: 2026-05-09T22:42:07+08:00
aliases:
  - Meta Harness
  - model harness optimization
tags:
  - agents
  - harness
  - optimization
---
# Meta-Harness

Meta-Harness is an outer-loop system for optimizing [[wiki/topics/AI Harness|AI harnesses]]. It searches over executable harness code around a frozen model rather than updating the model weights.

## Core Idea

The paper defines a harness as the stateful program that wraps a language model and determines what context the model sees at each step.

Meta-Harness repeatedly proposes, evaluates, and logs candidate harnesses. A coding-agent proposer reads a growing filesystem of prior candidate source code, scores, and execution traces, then writes a new harness candidate.

The core distinction from many text optimizers is feedback bandwidth. Instead of conditioning on scalar scores, fixed summaries, or short templates, the proposer can selectively inspect raw prior code and traces with ordinary developer operations such as search and file reads.

This makes harness optimization a kind of trace-driven program search: the system learns by changing the external code that constructs prompts, manages state, retrieves examples, updates memory, or orchestrates tool use. ^[inferred]

## Search Loop

The loop has three steps:

1. A coding-agent proposer inspects a filesystem containing prior harness source code, execution traces, and scores.
2. The proposed harness is evaluated on task instances.
3. Code, reasoning traces, evaluation scores, prompts, tool calls, model outputs, and state updates are written back into a new directory.

The paper reports that a typical run evaluates roughly 60 harnesses over 20 iterations, and that in the TerminalBench-2 run the proposer read a median of 82 files per iteration, with attention split mainly between prior code and execution traces.

Meta-Harness keeps a population and Pareto frontier but deliberately avoids a rigid parent-selection rule: the proposer may inspect any prior harness and trace when proposing the next candidate.

## Why Raw Traces Matter

The paper's ablation argues that raw execution traces are the key ingredient. In online text classification, the full interface reached 50.0 median and 56.7 best search-set accuracy, while scores-only and scores-plus-summary ablations stayed around the mid-30s median.

The interpretation is that summaries compress away the diagnostic details needed for credit assignment across long-horizon harness behavior.

For agent engineering, this connects directly to [[wiki/concepts/Harness Ratchet]]: failure history only becomes useful when the system can inspect it deeply enough to identify what harness artifact should change. ^[inferred]

## Results Reported

The paper evaluates Meta-Harness in three domains:

- Online text classification: the discovered harness reaches 48.6% average accuracy across USPTO, Symptom2Disease, and LawBench, outperforming ACE by 7.7 points while using 11.4K additional context tokens versus ACE's 50.8K.
- Retrieval-augmented math reasoning: one discovered retrieval harness improves pass@1 by 4.7 points on average across five held-out models on 200 IMO-level problems.
- TerminalBench-2: discovered harnesses reach 76.4% with Claude Opus 4.6 and 37.6% with Claude Haiku 4.5; the paper reports these as #2 among Opus-4.6 agents and #1 among Haiku-4.5 agents on that leaderboard.

The TerminalBench-2 result should be read with the paper's own caveat: search and final evaluation use the same public benchmark, although the authors report manual and regex audits for task-specific string leakage. ^[ambiguous]

## Practical Implementation Lessons

Appendix D gives implementation lessons that generalize beyond the specific experiments:

- Write a good skill that defines role, directory layout, commands, output format, forbidden behavior, and objectives.
- Start from a baseline harness and a search set hard enough that the loop has failures to learn from.
- Log code, scores, and execution traces in queryable machine-readable formats.
- Add a small CLI for listing frontiers, showing top candidates, and diffing code/results when the filesystem becomes large.
- Run lightweight validation before expensive evaluations.
- Automate evaluation outside the proposer so the proposer focuses on diagnosis and code changes.

This is notable because it treats skills, logs, CLI affordances, and validation tests as part of the optimization substrate, not just surrounding convenience. ^[inferred]

## Open Questions

- How much of the observed benefit depends on the specific coding-agent proposer used in the paper?
- When does benchmark-specific harness search become overfitting rather than useful discovery?
- How should harness search co-evolve with model fine-tuning rather than keeping the base model frozen?
- What governance is needed when an automated outer loop can modify the harness that controls future agent behavior? ^[inferred]

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Continual Learning for AI Agents]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/Meta-Harness Paper Source Guide]]
