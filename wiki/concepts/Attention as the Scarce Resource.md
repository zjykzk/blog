---
title: Attention as the Scarce Resource
type: concept
status: seed
category: concepts
summary: >-
  AI makes code generation cheap, shifting the bottleneck to human attention: developers coordinate agents, judge results, and protect energy with clearer workflows.
sources:
  - https://martinfowler.com/rachels-ramblings/conductor-developer.html
  - conversation:2026-09-12
created: 2026-09-12T00:00:00+0800
updated: 2026-10-11T17:50:30+08:00
base_confidence: 0.40
lifecycle: draft
lifecycle_changed: 2026-09-12
provenance:
  extracted: 0.55
  inferred: 0.45
  ambiguous: 0.0
aliases:
  - Conductor Developer
  - 指挥家开发者
  - 注意力瓶颈
  - attention bottleneck
  - human attention bottleneck
tags:
  - agents
  - ai-coding
  - attention
  - judgment
---
# Attention as the Scarce Resource

When AI makes code generation cheap and fast, the binding constraint in software development stops being any single delivery phase and becomes human attention.

## What It Is

Rachel Laycock's central claim is that AI did not change what great software looks like — it changed *what is scarce*. For years the industry framed AI as a productivity tool and assumed the bottleneck would migrate down the delivery lifecycle: from coding to design and specification, then architecture, then verification. That migration model is wrong. The next bottleneck is not a phase at all; it is the developer's attention. ^[extracted]

The practical signature of this shift is that the best developers no longer spend the day in a single protected block of flow. They spend it **orchestrating agents** — deciding which agent takes which problem, supplying context, evaluating what comes back, catching subtle mistakes, and judging what deserves another iteration versus what is ready to ship.

This reframes the developer's role from soloist to **conductor**. A conductor is first and foremost a capable musician who *could* play the instruments; that is not why they stand on the podium. Their value is holding the whole score — the whole system — in their head. In this metaphor the AI agents are the musicians and the developer is the conductor. ^[extracted]

## How It Works

The scarcity shows up as a hard ceiling on parallel agents. Engineers report running eight AI agents in parallel — sometimes ten or twelve — and beyond that *they themselves* become the bottleneck. The number is not a tooling limit; it is an attention limit. Laycock notes it matches the shape of executive work: many simultaneous streams, none arriving neatly packaged, progressing only where a human decides to place attention. ^[extracted]

Three mechanisms explain why attention, not hours, is the constraint: ^[inferred]

- **Attention residue** (Leroy, 2009): switching from task A to task B leaves part of attention stuck on A, especially when A was left unfinished. Every glance at an agent's output adds residue, so high-frequency polling of many agents degrades all of them. ^[inferred]
- **Decision fatigue** (Baumeister's ego-depletion line): decisions draw on a limited resource. A conductor makes hundreds of micro-decisions a day ("good enough? / iterate? / which agent?"), so *decision density*, not clock time, is what exhausts. ^[inferred]
- **Loss of protected flow**: the old world optimized around long uninterrupted focus; the new world trades that for high-frequency shallow switching, so the old "find a quiet block" tactic no longer covers the cost. ^[inferred]

## When to Use

The concept applies whenever a person is steering multiple AI workstreams rather than executing one. The response Laycock points to is the executive skill set — **protect attention, manage energy, reduce unnecessary decisions, and build systems that help the brain rather than the calendar** — applied to engineering for the first time. ^[extracted]

Concrete moves that operationalize each principle: ^[inferred]

- **Batch, don't interrupt** — set fixed inspection windows (e.g. every 25–45 min) to review all agents at once instead of reacting to each return, collapsing N random switches into one planned one. ^[inferred]
- **Leave a ready-to-resume marker** — before switching away, write the acceptance criterion and what you'll check on return; Leroy's remedy for residue is a clear stopping point. ^[inferred]
- **Sequence by energy, not time** (Loehr & Schwartz, *The Power of Full Engagement*): put high-judgment decisions (architecture, "is this agent off-track?", rip-and-redo) in your peak window; put low-cognition inspection in the trough. ^[inferred]
- **Turn repeat judgments into rules** (Gollwitzer's implementation intentions): encode recurring micro-decisions as if-then policies and raise the agent's own Definition of Done so you only spend a decision when it hits the line. ^[inferred]
- **Externalize state** (GTD, David Allen: the mind is for having ideas, not holding them): track each agent's status on a board (in-progress / awaiting review / shipped / blocked) so attention is not stolen by "did I miss one?" The conductor holds the *structure* of the system in their head, but the system's live state lives on the score. ^[inferred]

The one-line frame: **replace willpower with structure.**

## Boundary and Open Questions

- Laycock argues developers are not becoming managers and AI is not replacing engineering; rather, engineering expertise is being applied in a different place, far more often, because execution got cheap. She suspects developers are simply the first knowledge workers to feel this. This "first-mover among knowledge workers" claim is a single-author observation. ^[ambiguous]
- The named attention/energy theories (residue, decision fatigue, energy management, implementation intentions, GTD) are imported into this frame here; the article itself only states the four executive principles without citing them. ^[inferred]
- Open: how should engineering *careers* be redesigned when attention is the scarce resource — the question Laycock leaves unanswered.

## Related

- [[wiki/concepts/Agentic Engineering]]
- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Loop Engineering]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/concepts/Verification Gap]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Agent Loop Human Judgment Positions]]
- [[wiki/syntheses/From Senior Engineer to Tech Leader]]
- [[wiki/topics/Technical Management]]
- [[wiki/sources/The Conductor Developer Source Guide]]
</content>
</invoke>
