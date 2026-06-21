---
title: Continual Learning for AI Agents Source Guide
category: sources
tags:
  - article
  - agents
  - memory
  - harness
  - context
aliases:
  - Harrison Chase Continual Learning Source Guide
  - Continual learning for AI agents
sources:
  - https://x.com/hwchase17/status/2040467997022884194
  - conversation:2026-05-12
created: 2026-05-09T22:17:54+08:00
updated: 2026-05-12T11:36:33+08:00
summary: Source guide for Harrison Chase's X article separating agent continual learning into model, harness, and context layers, with the article structure and diagrams preserved.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: "2026-05-09"
---
# Continual Learning for AI Agents Source Guide

> Source: Harrison Chase, “Continual learning for AI agents”, https://x.com/hwchase17/status/2040467997022884194

## Capture Policy

This page preserves the source-level content of Harrison Chase's X article rather than reducing it to a short summary. It keeps the article's layer model, examples, comparison table, diagram logic, update modes, and trace-centered improvement flow so later wiki work can cite the source without reopening X.

The stable conceptual distillation belongs in [[wiki/concepts/Continual Learning for AI Agents]]. This page remains the source-facing artifact for what the article itself says.

## What It Covers

The article argues that continual learning for AI agents should not be collapsed into updating model weights. Agentic systems can learn at three distinct layers:

- the **model**: the model weights themselves;
- the **harness**: the code, always-on instructions, and always-available tools that drive all instances of the agent;
- the **context**: additional configuration outside the harness, such as instructions, skills, tools, and memory.

This distinction matters because each layer has different cost, speed, granularity, inspectability, and impact ceiling. The article's practical design claim is that builders should decide which layer should learn before they design a continual-learning mechanism. ^[inferred]

## Preserved Content

### Opening Thesis

Most discussions of continual learning in AI focus on model-weight updates. For AI agents, learning can happen at three distinct layers: model, harness, and context. Understanding the difference changes how systems that improve over time should be built.

The article names the three main layers of agentic systems as:

- **Model**: the model weights themselves.
- **Harness**: the wrapper around the model that powers all instances of the agent. This includes the code that drives the agent, plus instructions or tools that are always part of the harness.
- **Context**: additional context, including instructions and skills, that lives outside the harness and can configure it.

### Nested Layer Diagram

The first diagram presents a nested structure:

```text
Context
  E.g. AGENTS.md, /skills, mcp.json

  Harness
    E.g. DeepAgents, Claude Code, Pi, Codex, Droid

    Model
      E.g. Sonnet, GLM5, GPT-5.4, Gemini
```

The diagram visually places the model inside the harness, and the harness inside context. The examples make the distinction concrete:

- `AGENTS.md`, `/skills`, and `mcp.json` are context-level configuration surfaces.
- DeepAgents, Claude Code, Pi, Codex, and Droid are harness/runtime examples.
- Sonnet, GLM5, GPT-5.4, and Gemini are model examples.

### Example: Claude Code

For a coding agent such as Claude Code, the mapping is:

- **Model**: `claude-sonnet`, etc.
- **Harness**: Claude Code.
- **User context**: `CLAUDE.md`, `/skills`, `mcp.json`.

This example separates the model provider from the code harness and from user-controlled configuration files. A user can improve agent behavior by editing context without changing Claude Code itself or retraining the model. ^[inferred]

### Example: OpenClaw

For OpenClaw, the mapping is:

- **Model**: many possible models.
- **Harness**: Pi plus other scaffolding.
- **Agent context**: `SOUL.md` and skills from Clawhub.

The article uses OpenClaw as a concrete context-learning example because `SOUL.md` can be updated over time.

### Learning at the Model Layer

The model layer is what most people mean when they talk about continual learning: updating model weights.

The article names common techniques such as:

- supervised fine-tuning (SFT);
- reinforcement learning, including GRPO.

The central challenge is **catastrophic forgetting**: when a model is updated on new data or tasks, it may degrade on things it previously knew. The article treats catastrophic forgetting as an open research problem.

When organizations train models for a specific agentic system, the article says this is mostly done for the agentic system as a whole. OpenAI Codex models can be viewed as models trained for the Codex agent. More granular approaches, such as a LoRA per user, are possible in theory but are not the common practice described in the article.

### Learning at the Harness Layer

The harness layer includes the code that drives the agent plus any instructions or tools that are always part of the harness.

The article connects this layer to recent work on harness optimization, especially **Meta-Harness: End-to-End Optimization of Model Harnesses**. The basic pattern is:

1. Run the agent over a batch of tasks.
2. Evaluate the results.
3. Store logs into a filesystem.
4. Run a coding agent over these traces.
5. Ask the coding agent to suggest changes to the harness code.

Harness learning is usually agent-level, similar to model learning. The article notes that it could theoretically become more granular, such as learning a different code harness per user, but the usual pattern is still agent-wide.

### Harness Optimization Diagram

The harness-optimization diagram shows a loop with three major steps:

```text
Filesystem with all experience
  -> propose harness code
  -> Harness
  -> Harness + LLM
  -> evaluate against tasks
  -> store all logs back to filesystem
```

The stored logs include:

- proposed code;
- reasoning traces;
- evaluation score.

This diagram is important because it makes harness learning trace-driven. The system does not merely remember a conclusion; it saves execution artifacts and evaluation signals so a future coding agent can propose a better harness.

### Learning at the Context Layer

Context sits outside the harness and configures it. The article says context includes things like:

- instructions;
- skills;
- tools;
- memory.

The same type of material can also exist inside the harness. For example, a harness may have its own base system prompt and built-in skills. The source's distinction is not about whether something is “instruction-like”; it is about whether it is part of the harness itself or part of external configuration.

Context learning can occur at several scopes:

- **agent level**: the agent has persistent memory and updates its own configuration over time;
- **tenant level**: each user, organization, team, or other tenant gets its own context updated over time;
- **mixed scope**: a system can combine agent-level context updates, user-level context updates, and org-level context updates.

Named examples in the source include:

- OpenClaw's `SOUL.md` for agent-level context updates;
- Hex's Context Studio;
- Decagon's Duet;
- Sierra's Explorer.

### Context Update Timing

The source names two timing patterns for context updates.

#### Offline or Background Learning

A system can process traces after the fact in an offline job. The job runs over recent traces, extracts insights, and updates context. OpenClaw calls this “dreaming”.

This pattern keeps the live interaction path fast, but it depends on a reliable background consolidation process. ^[inferred]

#### Hot-Path Learning

A system can update context while the agent is running. This may happen because:

- the agent decides to update memory;
- the user explicitly prompts the agent to remember;
- the harness contains core instructions that cause the agent to remember.

This pattern makes memory immediately available for future turns, but it can add latency and increases the risk of noisy or accidental memory writes. ^[inferred]

### Hot Path vs Background Diagram

The diagram contrasts two memory-update architectures:

```text
In the hot path
  User message
  Update memory
  Respond to user
  User message
  Update memory
  Respond to user

In the background
  Process A:
    User message
    Respond to user
    User message
    Respond to user

  Process B:
    30 minutes later...
    Update memory
```

The diagram's core point is that learning does not always need to be synchronous with user response. Memory can be consolidated later in a separate process.

### Explicit vs Implicit Memory Updates

Another dimension is how explicit the memory update is:

- The user can directly prompt the agent to remember.
- The agent can remember because the harness instructs it to do so.

This creates a governance question: user-requested memories, agent-inferred memories, and background-extracted memories may need different confidence thresholds, provenance, and review rules. ^[inferred]

### Comparison Table

The source compares the three learning layers as follows:

| Dimension | Model | Harness | Context |
|---|---|---|---|
| Form factor | Model weights | Code | Configuration files, such as `agent.md`, skills, and tools |
| Level of granularity | Agent | Agent | Agent, user, org, team, tenant |
| Cost of updating | High | Medium | Low |
| Speed to updating | Slow | Medium | Fast |
| Human inspectable | No | Yes | Yes |
| Ceiling of impact | Highest | High | Medium |
| Update pattern | Batch offline job | Batch offline job | Batch offline job; as agent is running |

This table gives the article its operational value. It turns “continual learning” from a single research problem into an architectural routing problem: choose the cheapest, fastest, most inspectable layer that can actually fix the observed failure. ^[inferred]

### Traces Are the Core

The article's final comparison section says all of the flows are powered by traces: the full execution path of what an agent did.

The article identifies LangSmith as a platform that helps collect traces and then use them in different ways:

- **Model update path**: collect traces and work with an organization such as Prime Intellect to train a custom model.
- **Harness update path**: use LangSmith CLI and LangSmith Skills to give a coding agent access to traces. The article says this pattern improved Deep Agents, an open-source, model-agnostic, general-purpose base harness, on Terminal-Bench.
- **Context update path**: the agent harness must support long-term context learning at agent, user, or org level. The article says Deep Agents supports user-level memory, background learning, and related examples in a production-ready way.

This source therefore treats traces as the shared substrate behind model training data, harness improvement data, and context/memory consolidation.

### Credits and Publication Metadata

The browser-rendered X page shows:

- Author/account: Harrison Chase, `@hwchase17`.
- Title: “Continual learning for AI agents”.
- Displayed timestamp: 12:34 AM · Apr 5, 2026.
- The article thanks `@sydneyrunkle`, `@Vtrivedy10`, and `@nfcampos` for review and feedback.

## Integration Decisions

This source should remain attached to the AI / Agent cluster rather than being promoted into a broad standalone topic page. The article's stable concept is already captured in [[wiki/concepts/Continual Learning for AI Agents]].

The page connects to existing wiki structures in these ways:

- [[wiki/topics/AI Harness]] should use the source for trace-driven harness improvement and harness-code optimization loops.
- [[wiki/topics/AI Memory]] should use the source for hot-path versus background memory updates.
- [[wiki/topics/Context Management]] should use the source for context as configurable material outside the harness.
- [[wiki/concepts/Harness Ratchet]] should use the source as a concrete example of converting traces into durable harness changes.
- [[wiki/syntheses/Agent System Design Space]] should use the source when comparing learning layers, learning scopes, and update costs.

Claims about LangSmith, Deep Agents, Terminal-Bench, Prime Intellect, Hex Context Studio, Decagon Duet, and Sierra Explorer should remain source-level unless independently corroborated by their primary documentation. ^[inferred]

## Open Questions

- When should a repeated failure be converted into a model update, harness-code patch, skill update, or memory write? ^[inferred]
- How should agent systems arbitrate between agent-level, user-level, team-level, org-level, and tenant-level context updates? ^[inferred]
- What governance prevents hot-path memory writes from polluting future behavior with accidental or low-confidence lessons? ^[inferred]
- How should background “dreaming” jobs represent uncertainty and avoid overwriting user-explicit memory with agent-inferred summaries? ^[inferred]

## Related

- [[wiki/concepts/Continual Learning for AI Agents]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/AI Memory]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Skill Self-Evolution]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/Meta-Harness Paper Source Guide]]
- [[wiki/sources/Skills-Coach Paper Source Guide]]
