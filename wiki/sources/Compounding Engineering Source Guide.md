---
title: >-
  Compounding Engineering Source Guide
category: sources
tags:
  - article
  - ai-coding
  - agents
  - harness
  - feedback
sources:
  - conversation:2026-05-12
created: 2026-05-12T21:05:21+08:00
updated: 2026-05-12T21:05:21+08:00
summary: >-
  Source guide for an Every article on compounding engineering: self-improving AI development systems where code reviews, failures, tests, and workflow lessons update durable context and agent defaults.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-12
---

# Compounding Engineering Source Guide

> Source: Every article, “Compounding Engineering” by Kieran Klaassen, pasted into conversation on 2026-05-12.

## Capture Policy

This page preserves the source-level argument of the article rather than turning it directly into a stable concept page. The article is useful as a practitioner source for [[wiki/concepts/Agentic Engineering]], [[wiki/concepts/Harness Ratchet]], [[wiki/concepts/Feedback Flywheel]], [[wiki/topics/AI Harness]], and [[wiki/topics/Testing Strategy]], but its metric claims and Cora-specific examples should remain source-layer until corroborated by additional sources.

## What It Covers

The article argues for “compounding engineering”: building self-improving development systems where every review, failure, test, prompt iteration, and architectural decision becomes reusable system memory. It contrasts ordinary AI-assisted coding, which gives short-term speedups, with an AI engineering workflow where the surrounding context, rules, tests, agents, and review systems become more capable over time.

The central shift is from “AI as an extra set of hands” to “AI as a development system that learns from work.” The engineer’s leverage moves from typing code to designing the systems that design, validate, review, and improve code.

## Preserved Content

### Opening example: code review before the engineer arrives

The article begins with a GitHub review scene. The author expects to review a pull request manually: flag poor variable names, cut excessive tests, and suggest simpler error handling. Instead, Claude Code has already left comments that reference prior pull requests:

- variable naming changed to match a pattern from PR #234;
- excessive test coverage removed based on feedback from PR #219;
- error handling added similar to the approved approach in PR #241.

The point is not that Claude generated code once. The point is that the system appears to have absorbed three months of code-review taste and applied it with references. The source frames this as compounding rather than cheating: every fix, review, and avoidable failure teaches the system.

This example is close to [[wiki/concepts/Encoding Team Standards]] and [[wiki/concepts/Feedback Flywheel]]: a review comment only compounds if it changes durable defaults instead of disappearing into a closed pull request.

### Definition of compounding engineering

The article defines compounding engineering as building self-improving development systems where each iteration makes the next one faster, safer, and better.

It contrasts two modes:

| Mode | Short description | Long-term effect |
|---|---|---|
| Typical AI engineering | Prompt, code, ship, then start over | Faster today, but lessons often remain local to the session |
| Compounding engineering | Prompt, code, ship, then update memory, tests, rules, and workflows | Faster tomorrow because the system carries lessons forward |

The article’s slogan is that AI engineering makes the team faster today, while compounding engineering makes the team faster tomorrow and every day after that.

The deeper behavioral change is that a developer stops seeing a bug fix as complete when the immediate bug disappears. A bug fix is only complete when its category is less likely to recur. Likewise, a code review is partly wasted if it does not produce extractable lessons that future agents can apply.

### The 10-minute investment: prompt testing as a self-improving loop

The article’s main worked example is a “frustration detector” for Cora, Every’s AI-enabled email assistant. The detector should notice when users are annoyed with the app’s behavior and automatically file improvement reports.

A traditional workflow would be:

1. write the detector;
2. test manually;
3. tweak detection logic;
4. repeat.

The compounding workflow starts with a sample conversation where a user expresses frustration, such as repeatedly asking the same question with increasingly terse language. The engineer gives Claude a prompt: “This conversation shows frustration. Write a test that checks if our tool catches it.”

The loop then follows a TDD-like structure:

1. Claude writes the test.
2. The test fails.
3. Claude writes detection logic.
4. The detector still misses cases.
5. Claude iterates on the frustration-detection prompt until the test passes.
6. Claude runs the test multiple times because LLM outputs are nondeterministic.
7. When the detector catches frustration only four times out of ten, Claude studies failed runs and their reasoning traces.
8. Claude notices that it misses hedged frustration, such as “Hmm, not quite,” when paired with repeated requests.
9. Claude updates the prompt to look for polite-but-frustrated language.
10. The detector reaches nine out of ten successful identifications and is considered good enough to ship.

This example preserves three important source claims:

- Prompt behavior can be improved through executable tests rather than only intuition.
- Nondeterminism requires repeated trials, not single-run validation.
- Failure analysis should update the original prompt or harness rule, not only the immediate output.

The article says the whole workflow is codified in `CLAUDE.md` so future emotion or behavior detectors can reuse it. The next task can invoke “the prompt workflow from the frustration detector” instead of reconstructing the method.

This maps directly to [[wiki/concepts/Verification Loop]], [[wiki/concepts/Harness Ratchet]], and [[wiki/topics/Testing Strategy]]. The test is the feedback signal; the `CLAUDE.md` update is the ratchet that prevents the lesson from leaking away.

### From terminal to mission control

The article argues that compounding engineering turns AI from an extra set of hands into an increasingly aligned team. The author lists five patterns used at Cora:

1. Transform production errors into permanent fixes.
   - Agents investigate crashes.
   - Agents reproduce problems from logs.
   - Agents generate both solutions and tests.
   - The goal is to turn every failure into a one-time event.

2. Extract architectural decisions from collaborative work sessions.
   - Design discussions are recorded.
   - Claude documents why approaches were chosen.
   - The resulting standards become reusable onboarding and review material.

3. Build review agents with different expertise.
   - A “Kieran reviewer” captures the author’s style preferences.
   - Specialized reviewers add other lenses, such as Rails best practice or performance optimization.
   - Review becomes a set of codified perspectives rather than one overloaded human pass.

4. Automate visual documentation.
   - An agent detects interface changes.
   - It captures before/after screenshots across screen sizes and themes.
   - It generates visual documentation for reviewers.
   - A thirty-minute manual task becomes an automatic review artifact.

5. Parallelize feedback resolution.
   - Each reviewer comment can receive a dedicated agent.
   - Agents work simultaneously on independent concerns.
   - Ten issues can be resolved in roughly the time one used to take.

The article reports that three months of this workflow on Cora reduced average feature time-to-ship from over a week to one to three days, increased bugs caught before production, and reduced PR review cycles from days to hours. These are source-reported operational claims, not independently verified measurements.

### The playbook: five steps

#### Step 1: Teach through work

Every decision should be captured and codified so the AI does not repeat the same mistake. The article treats `CLAUDE.md` as “taste in plain language”: local preferences such as guard clauses over nested conditionals, naming conventions, or preferred error-handling style.

The article also mentions `llms.txt` as a place for higher-level architectural decisions and system-wide rules that should remain stable even when individual features are restructured.

The principle is not to accumulate generic tips. The durable context should encode local codebase reality and hard-won lessons.

Related wiki layer:

- [[wiki/concepts/Knowledge Priming]] — durable project context before generation.
- [[wiki/concepts/Encoding Team Standards]] — turning tacit engineering judgment into versioned AI instructions.
- [[wiki/concepts/Coding Agent User Harness]] — shaping agent behavior through local context, tools, rules, and checks.

#### Step 2: Turn failures into upgrades

The article says that when something breaks, the failure should become data for the system. Most engineers fix the immediate problem and move on. Compounding engineers also add the test, update the rule, and write the evaluation.

The source example is a user who did not receive a daily email Brief, a critical failure for Cora. The team wrote tests to catch similar delivery lapses, updated monitoring rules to flag missing Briefs, and built evaluations to continuously verify the delivery pipeline.

The article’s pattern is:

```text
failure → reproduction → fix → test → monitoring/evaluation → durable rule
```

Without the last three steps, the failure remains a local incident. With them, it upgrades the system’s future behavior.

This is the same mechanism as [[wiki/concepts/Harness Ratchet]]: repeated or expensive failures should become durable rules, hooks, checks, or workflow changes.

#### Step 3: Orchestrate in parallel

The article emphasizes that AI workers scale on demand. The limiting factors become orchestration skill and compute cost rather than headcount and hiring timelines.

The author describes a three-lane “mission control” setup:

| Lane | Role | Work |
|---|---|---|
| Left lane | Planning | Claude reads issues, researches approaches, and writes detailed implementation plans |
| Middle lane | Delegating | Another agent writes code, creates tests, and implements features |
| Right lane | Reviewing | A third agent reviews output against `CLAUDE.md`, suggests improvements, and catches issues |

This is a human-in-the-loop orchestration pattern. The human is not absent; the human allocates work, designs feedback channels, and verifies through tests, evals, spot checks, and review gates.

This links to [[wiki/topics/AI Harness]] and [[wiki/syntheses/AI Engineering Workflow]]: the output quality depends on the harness around models, not only on the model’s raw coding ability.

#### Step 4: Keep context lean but yours

The article warns against copying “ultimate CLAUDE.md” files from the internet. The source’s rule is that ten specific local rules beat one hundred generic ones.

Context should be:

- codebase-specific;
- pattern-specific;
- grounded in real mistakes and preferences;
- short enough to stay usable;
- actively pruned when rules stop serving the team.

The author says reviewing his `CLAUDE.md`, slash commands, and agent files feels like reading his own software philosophy. This is a strong source image: AI context is not just documentation; it is an executable mirror of local engineering taste.

This overlaps with [[wiki/concepts/Context Information Density]]: the question is not how much context exists, but how much decision-relevant signal survives in the active context budget.

#### Step 5: Trust the process, verify output

The article says the hardest step is to stop micromanaging every line. The recommended stance is to trust the system while verifying through tests, evals, and spot checks.

The source analogy is learning to be a CEO or movie director: one cannot do everything personally, but one can build systems that catch problems before they escalate.

The verification rule is recursive: when an output is wrong, teach the system why it was wrong so the same category of error is less likely next time.

This is not blind trust. It is structured delegation guarded by feedback controls.

### Closing claim: stop coding, start compounding

The article closes with a leverage claim: companies can now buy for hundreds of dollars per month what previously cost hundreds of thousands per year in engineering labor, and one-person startups can compete with funded teams. The source frames the strategic advantage as the ability to teach systems faster than competitors can type.

The suggested starting experiments are concrete:

1. Keep one experiment log.
2. When something fails that should not have, invest the time to prevent the category from recurring.
3. Build the test.
4. Write the rule.
5. Capture the lesson.
6. Open three terminals.
7. Try plan/build/review lanes.
8. Repeat until the workflow compounds.

## Integration Decisions

### Keep as source-level for now

The following should remain source-level until corroborated:

- Cora’s reported time-to-ship reduction from over a week to one to three days.
- Reported increase in bugs caught before production.
- Reported PR review-cycle reduction from days to hours.
- The exact effectiveness of the frustration detector after ten trials.

These claims are useful as practitioner evidence but should not be treated as general law without more cases.

### Promote into existing concepts rather than create a duplicate concept yet

The article’s core idea overlaps strongly with existing pages:

- [[wiki/concepts/Harness Ratchet]] — failures become durable harness improvements.
- [[wiki/concepts/Feedback Flywheel]] — real collaboration signals update standards, context, workflows, and guardrails.
- [[wiki/concepts/Agentic Engineering]] — engineers shape harnesses, checks, skills, and attention allocation instead of merely prompting or approving diffs.
- [[wiki/concepts/Encoding Team Standards]] — tacit preferences become versioned AI instructions.
- [[wiki/concepts/Verification Loop]] — external feedback lets agents correct before human review.

A future stable concept page for “Compounding Engineering” may be useful if more sources use the phrase, but this single article can currently be routed through the existing harness and feedback vocabulary.

### Mechanism shape

The article’s mechanism can be represented as:

```text
work event
  → observable trace / review / failure / test result
  → lesson extraction
  → durable context, rule, test, monitor, eval, or agent role
  → future agent behavior changes
  → new work produces richer traces
  → loop repeats
```

The key distinction is whether a work event updates a durable control surface. If it does not, the team merely used AI. If it does, the team is compounding the engineering system.

## Open Questions

- Which lessons belong in `CLAUDE.md`, which belong in tests, which belong in monitors, and which belong in specialized reviewer agents?
- How should teams prune stale rules so compounding context does not become context rot?
- How should source-reported productivity metrics be measured in a way that accounts for rework, hidden review burden, and risk?
- What organizational process decides whether a human review comment is local preference, team standard, or executable rule?
- How much autonomy is safe for parallel feedback-resolution agents before merge risk outweighs speed?

## Related

- [[wiki/concepts/Agentic Engineering]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Context Information Density]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/sources/Coding with AI Source Guide]]
- [[wiki/sources/Harness Engineering Source Guide]]
- [[wiki/sources/Team AI Coding Harness Seminar Source Guide]]
