---
title: Agent Transformer
type: concept
status: seed
summary: Agent Transformer models an AI agent as a transformer policy embedded in memory, tools, verifiers, and environment feedback rather than as a standalone text model.
category: concepts
sources:
  - https://arxiv.org/pdf/2601.01743
created: 2026-07-05T12:25:46+0800
updated: 2026-07-05T12:25:46+0800
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: "2026-07-05"
provenance:
  extracted: 0.88
  inferred: 0.11
  ambiguous: 0.01
relationships:
  - target: "[[wiki/concepts/Agentic Control Loop]]"
    type: extends
  - target: "[[wiki/topics/AI Harness]]"
    type: related_to
aliases:
  - agent-transformer abstraction
  - policy-memory-tool-verifier-environment agent
tags:
  - agents
  - architecture
  - harness
---
# Agent Transformer

Agent Transformer 是一种把现代 AI agent 形式化的抽象：agent 不是一个裸 transformer，而是一个 transformer policy 被嵌进 memory、tools、verifiers 和 environment feedback 组成的控制回路。

## Formal Shape

[[wiki/sources/AI Agent Systems Architectures Applications and Evaluation Paper Source Guide]] defines the abstraction as:

$$
A = (\pi_\theta, M, T, V, E)
$$

- `πθ`: transformer policy core.
- `M`: memory subsystem, including retrieval, summaries, and state.
- `T`: tool set, including APIs, search, code execution, databases, or multimodal perception tools.
- `V`: verifiers or critics that validate candidate actions before or after execution.
- `E`: environment that produces observations and changes after tool execution.

## Loop Semantics

At each step, the agent observes the environment, retrieves relevant memory, proposes an action, validates it, executes through tools, and updates both environment and memory.

This matters because the effective policy is not only `πθ`; it is the product of policy, memory selection, available tools, validation rules, permission boundaries, and environment feedback. ^[inferred]

## Why It Matters

The concept makes several agent-system design decisions explicit:

- Memory is not a passive transcript; it changes what the policy can condition on.
- Tools are not just capabilities; their schemas define the agent's action space.
- Verifiers are not post-hoc QA; they determine which proposed actions become real side effects.
- Environment feedback makes the agent a controller over trajectories, not only a generator of messages.

This connects directly to [[wiki/topics/AI Harness]]: the harness is the engineering layer that instantiates `M`, `T`, `V`, permissions, observability, and recovery around the policy core.

## Related

- [[wiki/concepts/Agent]]
- [[wiki/concepts/Agentic Control Loop]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Tool Routing]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/AI Agent Systems Architectures Applications and Evaluation Paper Source Guide]]
