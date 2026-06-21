---
title: Dive into Claude Code Source Guide
type: source
status: growing
category: sources
summary: >-
  Direct arXiv source guide for Dive into Claude Code, preserving its Claude Code architecture analysis, design principles, OpenClaw comparison, and future agent-system directions.
sources:
  - https://arxiv.org/abs/2604.14228
created: 2026-04-22T00:00:00+08:00
updated: 2026-05-22T21:13:00+08:00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-05-05
source_count: 1
provenance:
  extracted: 0.86
  inferred: 0.12
  ambiguous: 0.02
aliases:
  - 2604.14228 source guide
  - Dive into Claude Code
  - Claude Code paper
  - Claude Code design space paper
tags:
  - paper
  - arxiv
  - agents
  - harness
  - ai-coding
---
# Dive into Claude Code Source Guide

> Source: *Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems*, arXiv:2604.14228, https://arxiv.org/abs/2604.14228

## Capture Policy

This page preserves the arXiv paper as a source-level artifact. It keeps the paper's architecture vocabulary, section structure, implementation references, and comparative claims separate from stable wiki syntheses, so paper-grounded claims can be traced back to this source.

## What It Covers

The paper analyzes Claude Code as a production coding-agent system whose visible agent behavior comes from a small reactive model-tool loop surrounded by a large operational harness. Its central contribution is a design-space reading of agent systems: values, principles, permissions, context management, extensibility, subagents, persistence, recovery, and execution boundaries matter as much as the core model call.

Source metadata:

- Title: *Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems*
- Authors: Jiacheng Liu, Xiaohan Zhao, Xinyi Shang, Zhiqiang Shen
- arXiv ID: `2604.14228v1`
- Date: 2026-04-14
- Category: `cs.SE`; also listed under `cs.AI`, `cs.CL`, and `cs.LG`
- Comment: Tech report
- DOI: `10.48550/arXiv.2604.14228`
- License: Creative Commons Attribution-NonCommercial-ShareAlike 4.0
- Evidence base: public TypeScript source analysis of Claude Code v2.1.88, supplemented by documentation, community analysis, and comparison with OpenClaw.

## Preserved Content

### Central thesis

Claude Code is presented as a concrete production point in the design space of AI agent systems. The paper argues that the core agent loop is relatively simple, while the surrounding harness carries most of the system's real complexity: authorization, context shaping, tool orchestration, recovery, extensibility, delegation, state persistence, and user control.

The paper rejects the thin picture of `agent = model + tools`. Its system picture is closer to: agent = model reasoning loop + governed execution harness + context economy + extension surfaces + delegation boundaries + persistent audit trail.

### 1. Introduction

The introduction situates Claude Code in the shift from autocomplete and IDE assistants toward agentic coding systems. Claude Code can plan, inspect, act, call tools, run shell commands, edit files, and continue from environment feedback. This creates new architectural pressure around safety, context, extensibility, delegation, persistence, and user control.

The paper's motivating running example is: “Fix the failing test in `auth.test.ts`.” This example traces how a user request passes through query loop execution, permission checks, tool use, context selection, iterative repair, subagent delegation, and session persistence.

The paper is organized into three major moves:

1. A design-space analysis of Claude Code.
2. A comparison with OpenClaw.
3. A set of future directions for agent systems.

### 2. Values, philosophies, and design principles

The paper identifies five motivating values:

1. **Human Decision Authority** — humans retain final authority over goals and actions; they can observe, approve, reject, interrupt, and audit.
2. **Safety, Security, and Privacy** — the system should protect code, data, infrastructure, and users even when users are inattentive.
3. **Reliable Execution** — the agent should understand intent, preserve coherence, use environment feedback, and verify progress.
4. **Capability Amplification** — the system should increase what users can accomplish, with Claude Code framed more like a Unix utility than a closed product.
5. **Contextual Adaptability** — the system should adapt to projects, conventions, tools, workflows, and user trust levels.

These values map to thirteen design principles:

1. **Deny-first with human escalation** — unknown or risky actions are blocked or escalated instead of silently allowed.
2. **Graduated trust spectrum** — autonomy is not binary; users move across permission modes.
3. **Defense in depth with layered mechanisms** — safety comes from several independent controls.
4. **Externalized programmable policy** — settings, rules, hooks, and files expose policy rather than hiding it in product internals.
5. **Context as scarce resource with progressive management** — context window pressure is a primary systems constraint.
6. **Append-only durable state** — transcripts favor auditability over opaque mutable state.
7. **Minimal scaffolding, maximal operational harness** — the model reasons; the harness executes, validates, records, and bounds.
8. **Values over rules** — contextual model judgment is used, but bounded by deterministic controls.
9. **Composable multi-mechanism extensibility** — no single extension API carries every purpose.
10. **Reversibility-weighted risk assessment** — read-only or reversible actions are treated differently from destructive ones.
11. **Transparent file-based configuration and memory** — user-visible files are preferred over opaque storage.
12. **Isolated subagent boundaries** — subagents run with separated context and permission boundaries.
13. **Graceful recovery and resilience** — the system tries recovery paths before surfacing failure.

The paper contrasts this design family with graph orchestrators such as LangGraph, container-isolated agents such as SWE-Agent and OpenHands, and version-control-centered safety in tools such as Aider.

### 2.4. Long-term capability preservation

The paper adds long-term human capability as an evaluative lens. Short-term agent amplification may create overreliance or weaken developer comprehension. The important architectural question is not only “can the agent complete the task?” but also “does the system help the human understand, supervise, and improve over time?”

This claim should remain source-level until more independent sources support the same framing.

### 3. Architecture overview

The architecture section asks four recurring design questions:

1. **Where does reasoning live?** Reasoning lives mostly in the model; enforcement, execution, validation, and persistence live in the harness. The model emits `tool_use` requests, while the harness checks and executes them.
2. **How many execution engines?** A shared `queryLoop()` supports interactive terminal, headless CLI, Agent SDK, and IDE integration.
3. **What is the default safety posture?** The default is deny-first with escalation. Deny rules override ask rules, which override allow rules.
4. **What is the binding resource constraint?** Context is the limiting resource. The paper describes multiple context-reduction strategies before model calls.

The paper describes seven high-level components:

1. **User** — provides prompts, approvals, review, and interrupts.
2. **Interfaces** — interactive CLI, headless CLI, Agent SDK, IDE, desktop, and browser integrations.
3. **Agent loop** — implemented as `queryLoop()` in `query.ts`.
4. **Permission system** — deny-first rules, auto-mode classifier, and hook interception.
5. **Tools** — up to 54 built-in tools, with 19 unconditional and 35 conditional; MCP tools are merged into the pool.
6. **State and persistence** — mostly append-only JSONL transcripts, prompt history, and sidechain files.
7. **Execution environment** — shell execution, optional sandboxing, filesystem operations, web fetching, MCP connections, and remote execution.

Layered subsystem decomposition:

- **Surface layer** — `src/entrypoints/`, `src/screens/`, `src/components/`; terminal UI, SDK events, IDE surfaces, and Ink components.
- **Core layer** — `queryLoop()` plus compaction pipeline.
- **Safety/action layer** — permissions, auto-mode classifier, hooks, tool assembly, sandboxing, and subagents.
- **State layer** — context loading, runtime state, transcript persistence, CLAUDE.md hierarchy, recovery, and prompt history.
- **Backend layer** — Bash and PowerShell tools, remote execution, MCP client, transports, and concrete tools.

The paper clarifies that `QueryEngine` is not the core execution engine. It is a conversation wrapper for non-interactive use; the shared execution path is `query()` and `queryLoop()`.

### 3.5. Permission and safety layers

The paper identifies seven safety layers:

1. Tool pre-filtering.
2. Deny-first rule evaluation.
3. Permission mode constraints.
4. Auto-mode classifier.
5. Shell sandboxing.
6. Not restoring permissions on resume.
7. Hook-based interception.

This is one of the paper's clearest examples of defense in depth: permission approval, rule evaluation, classifier judgment, sandboxing, and hooks are distinct surfaces rather than one unified gate.

### 3.6. Context as bottleneck

The paper treats context as a runtime systems bottleneck rather than a prompt-length inconvenience. It names several context-saving mechanisms:

- CLAUDE.md lazy loading.
- Deferred tool schemas with ToolSearch.
- Subagent summary-only return.
- Per-tool-result budget.
- Budget reduction, snip, microcompact, context collapse, and auto-compact.

This connects directly to [[wiki/topics/Context Management]] and [[wiki/concepts/Context Information Density]].

### 4. Turn execution and the agentic query loop

The query pipeline is described as:

1. Settings resolution.
2. Mutable state initialization.
3. Context assembly.
4. Pre-model context shaping.
5. Model call.
6. Tool-use dispatch.
7. Permission gate.
8. Tool execution and result collection.
9. Stop condition.

`queryLoop()` is an `AsyncGenerator` that yields stream events, request-start events, messages, tombstone messages, and tool-use summaries. The model call streams through `deps.callModel()`. The paper compares this to ReAct while contrasting it with graph-routing and tree-search methods.

Tool dispatch has two execution paths:

- `StreamingToolExecutor`.
- `runTools()` in `toolOrchestration.ts`.

Read-only or concurrency-safe operations can run in parallel. State-changing operations such as shell commands are serialized. Results are emitted in tool-request order and normalized for the Anthropic API.

Pre-model context shapers include:

1. `applyToolResultBudget()` — caps large tool results and replaces oversized content with references.
2. `snipCompactIfNeeded()` — removes older history segments under a feature gate.
3. Microcompact — time-based and cache-aware paths reduce context pressure.
4. Context collapse — produces a projected read-time history view without mutating full REPL history.
5. `compactConversation()` — runs when lighter methods fail.

Recovery mechanisms include max-output-token escalation, reactive compaction, prompt-too-long handling, streaming fallback, and fallback model. Stop conditions include no tool use, max turns, context overflow, hook intervention, and explicit abort.

### 5. Tool authorization and control boundaries

The paper lists seven permission modes:

1. `plan`
2. `default`
3. `acceptEdits`
4. `auto`
5. `dontAsk`
6. `bypassPermissions`
7. `bubble`

`auto` is feature-gated by `TRANSCRIPT_CLASSIFIER`; `bubble` is internal and used for subagent escalation. Rule matching is deny-first: `toolMatchesRule()` checks deny rules first, and a deny can override a more specific allow. Rules can match tool names, Bash prefixes, and qualified MCP tool names.

The authorization pipeline is:

1. **Pre-filtering** — blanket-denied tools are removed before the model sees them.
2. **PreToolUse hook** — hooks can deny, ask, or update input.
3. **Rule evaluation** — deny-first matching including MCP server-level rules.
4. **Permission handler** — coordinator, swarm worker, speculative classifier, or interactive path.

Denials act as routing feedback: the model can receive a denial reason and attempt a safer path.

The paper also distinguishes hook timing for non-MCP and MCP tools. For non-MCP tools, `tool_result` is emitted before `PostToolUse`; for MCP tools, output can be delayed so hooks can update MCP tool output.

Shell sandboxing applies to Bash and PowerShell commands through `shouldUseSandbox.ts`. It checks global enablement, invocation opt-out, and exclusion patterns. The paper notes a defense-in-depth weakness: very long shell commands with many subcommands can degrade into generic approval prompts when detailed parsing becomes too expensive.

### 6. Extensibility: MCP, plugins, skills, and hooks

Claude Code exposes several extension mechanisms rather than one universal extension model:

1. **MCP servers** add external tools and service integrations.
2. **Plugins** package and distribute bundles of components.
3. **Skills** add domain-specific instructions, often from `.claude/skills/`.
4. **Hooks** intercept lifecycle and tool execution events.

The paper interprets this plurality as a context-cost and control-point trade-off. MCP, plugins, skills, and hooks sit at different points in the agent loop and carry different disclosure and governance costs.

This connects to [[wiki/concepts/Agent Skill]], [[wiki/concepts/Agent Tool]], and [[wiki/topics/AI Skills Workflow]].

### 7. Context construction and memory

The paper's context and memory section covers:

- Context window assembly.
- CLAUDE.md hierarchy and auto memory.
- Compaction pipeline.
- `getSystemContext()` and `getUserContext()`.
- Runtime state and transcript persistence.
- Lazy context loading and context-pressure relief.

It distinguishes runtime context from durable memory. Context is the bounded active workspace for a model call; memory and transcript state persist beyond the current turn and can be reintroduced later.

### 8. Subagent delegation and orchestration

Subagents are spawned through `AgentTool` and `runAgent.ts`. They re-enter `queryLoop()` with isolated context. The parent receives summary text rather than the full subagent history, and sidechain transcripts are stored separately.

This design is presented as a boundary mechanism rather than only a convenience feature. Subagents reduce context pressure and isolate work, but they also create questions about delegation criteria, permission propagation, and summary fidelity.

### 9. Session persistence and recovery

Session transcripts are mostly append-only JSONL. Resume and fork reconstruct session state from transcripts, but session-scoped permissions are not restored on resume or fork. This choice supports auditability and deny-first safety at the cost of convenience.

The paper names `sessionStorage.ts`, `history.ts`, and `conversationRecovery.ts` as relevant implementation locations.

### 10. Comparative analysis: Claude Code and OpenClaw

The paper compares Claude Code with OpenClaw across six dimensions:

1. System scope and deployment model.
2. Trust model and security architecture.
3. Agent runtime and tool orchestration.
4. Extension architecture.
5. Memory, context, and knowledge management.
6. Multi-agent architecture and routing.

The contrast is not framed as winner-takes-all. Claude Code is a coding-agent CLI/product architecture centered on a single loop, per-action safety evaluation, context-window extension, and layered harness policy. OpenClaw is described as a multi-channel personal assistant gateway, where perimeter-level access control, gateway-wide capability registration, and gateway control-plane behavior matter more.

The design-space lesson is that the same agent questions produce different architecture answers under different deployment boundaries.

### 11. Discussion

The paper's discussion sections include:

- Design philosophy.
- Value tensions.
- Architectural trade-offs.
- Empirical predictions and early signals.
- Limitations.
- Emerging directions.
- Recurring design choices.

Named trade-offs include:

- Safety vs. autonomy.
- Permission model under adversarial conditions.
- Context efficiency vs. transparency.
- Simplicity vs. extensibility.

Recurring design choices include:

- Graduated layering over monolithic mechanisms.
- Append-only designs that favor auditability over query power.
- Model judgment within a deterministic harness.

The limitations should remain source-level:

- Long-term human capability is not necessarily a primary architectural value.
- Context compaction improves feasibility but may reduce transparency.
- Permission prompts can become weak if users approve habitually.
- Defense-in-depth layers can share operational constraints.
- The architecture does not impose explicit planning graphs.
- The system does not use a single unified extension model.
- Some trust-related session state is intentionally not restored.

### 12. Future directions

The paper names six future directions:

1. **Silent Failure and the Observability–Evaluation Gap** — agents need better visibility into failures that do not surface as crashes.
2. **Persistence: Memory and Longitudinal Colleague Relationships** — agents may need durable state that supports ongoing collaboration.
3. **Harness Boundary Evolution** — where, when, what, and with whom an agent acts may change as systems mature.
4. **Horizon Scaling** — future agents may move from session-scale tasks toward program-scale or scientific-program-scale work.
5. **Governance and Oversight at Scale** — agent autonomy creates oversight questions beyond single-user approval.
6. **Long-Term Human Capability** — systems should be evaluated for whether they preserve or improve human capability, not only immediate output.

### 13–16. Related work, conclusion, package structure, and methodology

The paper situates Claude Code among coding agents and agent architecture patterns, naming systems and concepts such as GitHub Copilot, Cursor, Devin, LangGraph, SWE-Agent, OpenHands, Aider, ReAct, tree-search methods, PASTE, and MCP.

Its package-structure appendix maps directories and files to responsibilities, including:

- `src/entrypoints/` for startup paths.
- `src/screens/` and `src/components/` for UI.
- `src/state/` for runtime state.
- `src/tools/` for concrete tool implementations.
- `src/remote/` for remote execution.
- `services/mcp/client.ts` for MCP connections.

Its methodology section emphasizes source-code analysis, documentation, community analysis, and design-space tracing from values to implementation files.

## Integration Decisions

This source is already partially promoted into [[wiki/syntheses/Agent System Design Space]], [[wiki/topics/AI Harness]], and [[wiki/topics/Context Management]]. The expanded source guide should remain the paper-grounded layer for:

- Claude Code-specific implementation details.
- File and function names mentioned by the paper.
- The exact five values and thirteen design principles.
- The OpenClaw comparison.
- The future-directions list.
- Claims about Claude Code v2.1.88 source structure.

Stable wiki pages should absorb only the reusable abstractions:

- [[wiki/topics/AI Harness]] should keep using the paper as evidence that harness design is the main runtime control layer around a model.
- [[wiki/syntheses/Agent System Design Space]] should use the values/principles/boundaries framing without treating Claude Code as the universal architecture.
- [[wiki/topics/Context Management]] should use the paper as evidence that context management is a runtime systems problem, not only a prompt-writing concern.
- [[wiki/concepts/Coding Agent User Harness]] and [[wiki/concepts/Harnessability]] can use the paper's architecture as one concrete instance of user-side harness design.

Do not promote source-specific conclusions such as “Claude Code's architecture is the best architecture” or detailed claims about current internal implementation without checking against the live code or current documentation.

## Open Questions

- Which of the thirteen design principles deserve standalone concept pages rather than remaining inside [[wiki/syntheses/Agent System Design Space]]?
- Should [[wiki/topics/AI Harness]] be split into permission, context, delegation, persistence, and recovery subtopics?
- How should long-term human capability be operationalized as an agent-system evaluation dimension?
- Which claims in this paper remain stable as Claude Code evolves beyond the analyzed v2.1.88 source?

## Related

- [[wiki/sources/Agent Systems Papers Source Guide]]
- [[wiki/sources/Agent Engineering Source Guide]]
- [[wiki/sources/Before the Tool Call Source Guide]]
- [[wiki/sources/GenericAgent Paper Source Guide]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/concepts/Coding Agent User Harness]]
