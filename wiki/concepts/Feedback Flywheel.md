---
title: Feedback Flywheel
type: concept
status: seed
category: concepts
summary: Feedback flywheel turns AI collaboration experience into updated context, standards, workflows, and guardrails.
sources:
  - https://martinfowler.com/articles/reduce-friction-ai/feedback-flywheel.html
created: 2026-05-05T17:55:00+08:00
updated: 2026-05-05T17:55:00+08:00
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-05
provenance:
  extracted: 0.84
  inferred: 0.16
  ambiguous: 0.0
aliases:
  - AI feedback flywheel
  - AI collaboration feedback loop
  - continuous improvement loop for AI coding
tags:
  - ai-coding
  - feedback
  - workflow
---
# Feedback Flywheel

Feedback flywheel is the practice of turning AI collaboration experience into updated context, standards, workflows, and guardrails.

Rahul Garg's [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]] frames it as the pattern that prevents the other four patterns from going stale. [[wiki/concepts/Knowledge Priming]], [[wiki/concepts/Context Anchoring]], [[wiki/concepts/Encoding Team Standards]], and design workflows all need maintenance after real use.

## Core Loop

The article describes a continuous loop:

1. Use AI on real development work.
2. Observe failures, successes, friction, and review outcomes.
3. Capture the learning.
4. Update priming documents, context anchors, standards, prompts, commands, and workflow rules.
5. Reuse the improved system on future work.

The important shift is from one-off prompt tuning to system improvement. A bad AI interaction is not only a bad output; it is evidence about what the collaboration system failed to provide.

## What Counts As Feedback

Useful feedback includes more than explicit user ratings.

- Review comments: what humans repeatedly corrected.
- Regeneration cycles: where the assistant needed multiple attempts.
- Accepted output: what worked without major changes.
- Post-merge rework: where AI output created later maintenance cost.
- Prompt edits: what humans keep adding manually.
- Security, test, and architecture findings: where standards were missing or unclear.

These signals should feed back into durable artifacts, not remain private memory in a developer's head.

## Artifact Updates

The flywheel acts on several artifact types:

- update [[wiki/concepts/Knowledge Priming]] when the assistant lacked project vocabulary or examples
- update [[wiki/concepts/Context Anchoring]] when feature decisions or current state were missing
- update [[wiki/concepts/Encoding Team Standards]] when review, security, or refactoring judgment had to be repeated manually
- update design workflows when the assistant skipped design alignment
- update checks, tests, or CI gates when a repeated failure can be made executable

This makes the flywheel a team-level cousin of [[wiki/concepts/Harness Ratchet]]: both turn repeated failures into durable changes around the model. ^[inferred]

## Metrics

The source emphasizes operational metrics rather than generation-speed metrics.

- first-pass acceptance rate
- iteration cycles per task
- post-merge rework
- review burden
- repeated classes of correction

These metrics matter because they reveal whether AI assistance is reducing total collaboration cost or merely producing faster first drafts.

## Maintenance Discipline

A flywheel can decay if it only adds rules. Teams need a pruning path: remove stale instructions, consolidate duplicated guidance, and revisit whether a rule still reflects current architecture or model behavior.

That makes the feedback flywheel a [[wiki/concepts/Feedback Loops]] problem with delay: if the team waits too long to update artifacts, the same failures repeat; if it updates too aggressively after one event, the system can accumulate noisy rules. ^[inferred]

## Lattice Example

The article's Lattice example treats feedback as a workflow capability: teams can capture what worked, what failed, which artifacts should change, and which standards or skills need refinement.

This strengthens [[wiki/topics/AI Skills Workflow]] because a skill system should not only execute a current workflow; it should help preserve lessons that improve the next run. ^[inferred]

## Related

- [[wiki/concepts/AI Collaboration Scaffolding]]
- [[wiki/concepts/Knowledge Priming]]
- [[wiki/concepts/Context Anchoring]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Feedback Loops]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide]]
