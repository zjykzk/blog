---
title: Agentic Engineering
type: concept
status: seed
category: concepts
summary: Agentic engineering is production AI coding where humans shape harnesses, checks, skills, and attention allocation instead of merely prompting or approving diffs.
sources:
  - https://www.chrismdp.com/coding-with-ai/
  - https://mp.weixin.qq.com/s/64e7occeVSutUJzZAWVutg
  - https://x.com/odysseus0z/status/2030416758138634583?s=46&t=GqNFmk6Xi41yVO4sAJf36g
  - wiki/sources/Vibe 时代的软件工程.md
  - https://x.com/trq212/article/2073100352921215386
  - https://www.langchain.com/blog/the-art-of-loop-engineering
  - https://engineering.zalando.com/posts/2026/08/agentic-engineering-at-zalando-a-snapshot.html
  - https://x.com/AndrewYNg/article/2088302050706686198
created: 2026-05-07T22:03:56+08:00
updated: 2026-10-06T16:39:47+0800
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-07
provenance:
  extracted: 0.78
  inferred: 0.22
  ambiguous: 0.0
aliases:
  - agentic coding
  - agentic engineering practice
  - AI coding trainer role
tags:
  - agents
  - ai-coding
  - software-engineering
---
# Agentic Engineering

Agentic engineering is the production practice of using coding agents with explicit verification, harness design, and human judgment allocation.

Chris Parsons contrasts it with vibe coding: vibe coding looks at generated output without seriously checking it, while agentic engineering makes a measured call about which diffs need human eyes and which can be checked by tests, type checkers, automated gates, or other review surfaces.

[[wiki/sources/Vibe 时代的软件工程]] sharpens that contrast by placing [[wiki/concepts/Vibe Coding]] on a spectrum from completion to pair work, delegation, and hands-off acceptance. Agentic engineering starts where that spectrum needs responsibility: someone must decide the acceptable delegation grain, the verification path, and the rollback boundary.

## Core Shift

The senior engineer's role moves from being the final approver of every diff to training the [[wiki/concepts/Coding Agent User Harness]] that produces future diffs.

This training work includes:

- noticing agent drift before it becomes obvious in the diff
- extracting repeated lessons into repository rules, [[wiki/concepts/Agent Skill|skill files]], or reusable standards
- choosing which risks need human judgment and which can move into computational checks
- teaching teammates the reset, context, and verification instincts needed for agent work

In this view, architectural taste still matters, but it compounds into markdown, skills, tests, and harness rules rather than staying only inside one senior engineer's head. ^[inferred]

The cybernetics framing sharpens this into calibration work: the engineer designs the sensor, actuator, target, and feedback path that let the system steer code changes without constant manual intervention. ^[inferred]

## Control Surface

Agentic engineering treats [[wiki/topics/AI Harness|harness]] design as part of software engineering practice.

A productive harness includes standing instructions, skill files, a [[wiki/concepts/Verification Loop]], and a [[wiki/concepts/Feedback Flywheel]]. When an agent gets stuck on a recurring issue, the failure should be treated as missing context or missing harness structure before it is treated as a prompt wording problem.

[[wiki/sources/The Art of Loop Engineering Source Guide]] names this harness work [[wiki/concepts/Loop Engineering]]: stack the basic agent loop with verification, event-driven triggers, and trace-driven improvement so production value comes from the loops around the model, not only from model capability.

This makes agentic engineering a close cousin of [[wiki/concepts/AI Collaboration Scaffolding]]: both externalize tacit collaboration knowledge into durable artifacts that future agent sessions can reuse. ^[inferred]


## Human-side harness

[[wiki/sources/Team AI Coding Harness Seminar Source Guide]] reinforces the human side of agentic engineering. The source argues that prompt rules can often constrain AI output, while getting people to clarify requirements, write tests, self-test rigorously, and review consistently is the harder organizational problem.

This reframes the engineer's responsibility: the team is not only evaluating generated code, but designing the work environment that makes generated code reviewable and repairable. ^[inferred]

The source also predicts that AI will compress roles that mainly translate between vague requirements, prototypes, and code. That replacement claim should stay provisional because it is a single-source seminar judgment and likely varies by product complexity, design depth, and quality responsibility. ^[ambiguous]

## Unknown Discovery

[[wiki/sources/Agentic Coding Unknowns Source Guide]] adds a pre-verification responsibility to agentic engineering. Before a generated diff can be verified, the human-agent pair has to discover where the prompt-map does not match the codebase-territory.

The article names these gaps as [[wiki/concepts/Agentic Coding Unknowns]]. They include explicit requirements, unresolved questions, tacit taste that only appears through prototypes, and hidden constraints the user has not considered. This makes a blind spot pass, prototype, interview, reference, implementation plan, implementation notes file, explainer, or quiz part of engineering control, not merely collaboration style. ^[inferred]

The practical shift is that humans are responsible for steering uncertainty, not only judging output. If instructions are too rigid, the agent may follow a bad path after implementation evidence suggests a pivot. If they are too vague, the agent may replace local fit with generic best practice.

## Failure Modes

Parsons names several recurring failure modes:

- accidental vibe coding: broad instructions plus weak checks lead to fast but unsafe production changes
- review fatigue: senior engineers become bottlenecks when agent output grows faster than human diff-reading capacity
- invisible dependencies: teams unknowingly rely on model behaviors that may change across upgrades
- premature relief: teams survive one AI tooling wave and underestimate the next wave of cloud agents and autonomous orchestration

## Organizational Scale

[[wiki/sources/Agentic Engineering at Zalando Source Guide]] extends the concept from an individual coding discipline to an organization-level operating system. At this scale, agentic engineering depends on five coupled layers: shared access infrastructure, freedom to explore tools and models, observability of sessions and delivery outcomes, mechanisms that spread local learning, and risk/identity controls that bound autonomous action.

The corresponding adoption loop is: lower the cost of experimentation, observe real behavior, identify useful and harmful patterns, encode the lessons into rules/skills/training/platform defaults, then expand adoption while preserving tool choice. ^[inferred]

This also sharpens the amplification principle: coding agents do not independently create engineering maturity. They increase the gain of the surrounding system, so repository quality, verification surfaces, deployment previews, authentication boundaries, and review incentives determine whether faster generation compounds into faster learning or faster disorder. ^[inferred]

## Capability Stack

[[wiki/sources/AI Engineering Skills Map Source Guide]] places coding-agent fluency inside a broader set of AI engineering responsibilities: building and deploying probabilistic AI applications, retaining software-engineering fundamentals, using coding agents effectively, and shaping what should be built.

These capabilities form a responsibility stack rather than four interchangeable techniques: product and business judgment choose the target; software-engineering knowledge exposes constraints and trade-offs; agent skill amplifies execution; evals, error analysis, and deployment controls close the loop around uncertain AI behavior. ^[inferred]

As coding agents improve at delivering against a clear specification, human responsibility moves upstream toward problem selection and specification while remaining downstream at verification, governance, and production-risk boundaries. The engineer becomes accountable for the whole build loop, not merely for producing code. ^[inferred]

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/concepts/Harnessability]]
- [[wiki/concepts/AI Collaboration Scaffolding]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Loop Engineering]]
- [[wiki/concepts/Event-Driven Agent Loop]]
- [[wiki/syntheses/Agentic Engineering × Verification Loop]] — synthesis
- [[wiki/concepts/Vibe Coding]]
- [[wiki/concepts/Verification Gap]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Agentic Coding Unknowns]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/sources/Coding with AI Source Guide]]
- [[wiki/sources/Team AI Coding Harness Seminar Source Guide]]
- [[wiki/sources/Harness Engineering Is Cybernetics Source Guide]]
- [[wiki/sources/Vibe 时代的软件工程]]
- [[wiki/sources/Agentic Coding Unknowns Source Guide]]
- [[wiki/sources/The Art of Loop Engineering Source Guide]]
- [[wiki/sources/Agentic Engineering at Zalando Source Guide]]
- [[wiki/sources/AI Engineering Skills Map Source Guide]]
