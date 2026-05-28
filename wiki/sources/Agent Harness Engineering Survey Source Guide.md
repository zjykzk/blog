---
title: >-
  Agent Harness Engineering Survey Source Guide
category: sources
type: source
status: draft
tags: [paper, agents, harness, architecture, systems]
sources:
  - https://picrew.github.io/LLM-Harness/main.pdf
created: 2026-05-28T19:37:07+0800
updated: 2026-05-28T19:37:07+0800
summary: >-
  Source guide for the Agent Harness Engineering survey, preserving its binding-constraint thesis, ETCLOVG taxonomy, project mapping, tradeoffs, and open research agenda.
provenance:
  extracted: 0.91
  inferred: 0.08
  ambiguous: 0.01
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-28
aliases:
  - Agent Harness Engineering: A Survey
  - LLM Harness Survey
  - ETCLOVG Survey
  - Awesome-Agent-Harness
---

# Agent Harness Engineering Survey Source Guide

> Source: Junjie Li et al., "Agent Harness Engineering: A Survey", under review as submission to TMLR, PDF at https://picrew.github.io/LLM-Harness/main.pdf

## Capture Policy

This page preserves the primary PDF source layer for the survey. It should not replace the broader [[wiki/topics/AI Harness]] topic or the article-level guides such as [[wiki/sources/Harness Engineering Source Guide]]; it records the paper's own claims, taxonomy, evidence mapping, tradeoffs, and caveats so later syntheses can ground harness claims in the primary survey.

## What It Covers

The survey argues that production LLM-agent reliability is often constrained less by model capability than by the execution harness around the model. The harness is treated as an independent engineering layer that manages execution environments, tools, context, lifecycle/orchestration, observability, verification, and governance.

Its main contribution is a seven-layer taxonomy called ETCLOVG:

```text
E - Execution environment and sandbox
T - Tool interface and protocol
C - Context and memory management
L - Lifecycle and orchestration
O - Observability and operations
V - Verification and evaluation
G - Governance and security
```

The paper also maps a large public corpus of agent-harness projects onto the taxonomy. The abstract says 170+ projects, while later claim and conclusion text sometimes says 148+ projects; this page preserves that inconsistency as a source-level ambiguity rather than smoothing it away.

## Preserved Content

### Bibliographic Metadata

- Title: Agent Harness Engineering: A Survey
- Authors include Junjie Li, Xi Xiao, Yunbei Zhang, Chen Liu, Lin Zhao, Xiaoying Liao, Yingrui Ji, Janet Wang, Jianyang Gu, Yingqiang Ge, Weijie Xu, Xi Fang, Xiang Xu, Tianchen Zhao, Youngeun Kim, Tianyang Wang, Jihun Hamm, Smita Krishnaswamy, Jun Huan, and Chandan K. Reddy.
- Affiliations include CMU, Yale, JHU, NEU, Tulane, UAB, OSU, Virginia Tech, and Amazon.
- Status: under review as submission to TMLR.
- Project page label in PDF: Awesome-Agent-Harness.

### Central Thesis: Harness Over Model

The paper frames agent reliability through a "binding constraint" thesis: for long-horizon tasks across comparable frontier models, measured performance can be driven as much by the execution harness as by the model itself.

The source supports this thesis with three kinds of harness-only evidence:

- tool and surrounding harness changes that reportedly produce up to 10x gains on coding benchmarks across 15 models;
- a fixed GPT-5.2-Codex agent improving from 52.8% to 66.5% on Terminal-Bench 2.0 through prompt restructuring, middleware context injection, and self-verification hooks;
- [[wiki/sources/Meta-Harness Paper Source Guide]] reporting 76.4% on Terminal-Bench-2 through automated harness optimization without changing model weights.

The point is not that models stop mattering. The stronger claim is that model behavior is measured inside a controller. Context policy, tool schemas, sandbox behavior, feedback hooks, verification, and governance all change what the same model can reliably do.

### Three Engineering Phases

The paper organizes the 2022-2026 period as a shift in marginal engineering effort:

1. Prompt engineering, roughly 2022-2024: optimization centers on instruction text, few-shot examples, and reasoning templates for a single model call.
2. Context engineering, around 2025: the key question becomes what information the model should see at each step, including retrieval, memory compression, tool results, and context-window saturation.
3. Harness engineering, around 2026: reliability depends on the wrapper that maintains state, mediates tools, injects feedback, enforces constraints, verifies progress, and governs execution.

The source is careful that these phases overlap. Harness engineering includes context engineering, which includes prompt engineering. The phases mark where extra engineering effort goes, not clean replacement boundaries.

### ETCLOVG Taxonomy

The seven layers split the harness into a structural core and a control plane.

Structural core:

- Execution determines where agent actions run and what sandbox constraints bound them.
- Tooling defines how capabilities are described, discovered, selected, and invoked.
- Context controls what the model sees across active-window, session, and persistent-memory horizons.
- Lifecycle organizes control flow, orchestration, state, retries, subagents, handoffs, and task pipelines.

Control plane:

- Observability records traces, cost, failures, reliability signals, and operational state.
- Verification converts tasks and traces into evaluation, failure attribution, and regression feedback.
- Governance constrains behavior through permissions, identity, policy, hardening, audit, and human oversight.

Two taxonomy choices matter. First, observability is promoted to its own layer because production tracing, cost attribution, and anomaly detection have their own tool stack and ownership. Second, governance is promoted to its own layer because permissions, identity, policy, audit, and compliance are not just lifecycle hooks.

### Corpus and Mapping Method

The paper defines agent harness narrowly: not all software around an LLM, but the engineered wrapper that turns model calls into bounded, stateful, tool-mediated task execution.

Included artifacts must be publicly documented, implement or specify a concrete harness-level mechanism, and provide enough evidence to assign at least one ETCLOVG layer. The paper includes agent frameworks, executable benchmarks, sandboxes, memory systems, observability tools, evaluation systems, and governance systems when they operate over agent state, traces, actions, or policies.

Excluded artifacts include simple chatbot demos, prompt packs, thin model-client wrappers, static datasets or leaderboards without runtime behavior, generic infrastructure not adapted to agents, and product pages without inspectable technical behavior.

The coding protocol is multi-label: each project receives a primary layer plus secondary layers when the public documentation exposes independent capabilities. The paper uses a single-primary-coder protocol with author audit, not a formal multi-coder agreement study. That makes the mapping useful as an ecosystem map, but not a fully reproducible inter-annotator study.

Corpus limitations:

- biased toward English-language and GitHub-visible projects;
- biased toward open-source artifacts and public documentation;
- commercial production systems are underrepresented unless blog posts, SDKs, or docs expose mechanisms;
- coding-agent infrastructure is overrepresented because it leaves rich public traces;
- absence from a layer means "not publicly evidenced", not "not implemented".

### Aggregate Ecosystem Pattern

The visible ecosystem is broad but uneven.

Dense areas:

- execution environments and sandboxes;
- tool interfaces and protocols;
- lifecycle orchestration;
- verification and evaluation.

Thinner areas:

- observability in open-source form, because much of it lives in commercial platforms;
- governance, because permissions, identity, policy, and audit often remain product-specific or under-documented.

The source's key ecosystem claim is that complete systems increasingly span multiple layers. Sandboxing, tool protocols, orchestration, tracing, evaluation, and permission controls are becoming coupled parts of one control system, not isolated add-ons.

### Execution Environment and Sandbox

Execution is the physical substrate of the harness. The source gives sandboxing three agent-era purposes:

- security: untrusted or prompt-injected agent actions need containment;
- reproducibility: evaluation and training need cheap reset to known state;
- liveness: agents need a bounded region where they can act without asking humans for every file write, package install, or network call.

The paper groups execution substrates into seven categories:

- general-purpose managed sandboxes such as Daytona, E2B, Modal, Northflank, OpenSandbox, and Docker Sandboxes;
- computer-use agent infrastructure such as Anthropic Computer Use, CUA, and OSWorld;
- code-specialized sandboxes such as Judge0, OpenAI Code Interpreter, sandboxed.sh, and langchain-sandbox;
- framework-integrated runtimes such as OpenHands, agent-infra sandbox, and smolagents executors;
- browser evaluation environments such as WebArena, VisualWebArena, BrowserGym, and WorkArena;
- OS-level permission sandboxes such as Anthropic sandbox-runtime, Claude Code sandboxing, IsolateGPT, and transactional sandboxing;
- sandbox abstraction layers such as SWE-ReX, smolagents executor interfaces, and Kubernetes agent sandbox CRDs.

The layer is governed by workload fidelity, threat model, and operational mode. MicroVMs and managed clouds fit high-risk workloads; OS-level permission sandboxes fit local workflows where the threat is prompt injection rather than fully adversarial code; fast resettable substrates matter for large-scale training and evaluation.

### Tool Interface and Protocol Layer

The tool layer defines how agents discover, represent, select, and execute external capabilities. The source emphasizes a core tension: exposing more tools increases capability coverage but also increases prompt footprint, selection error, and attack surface.

The paper distinguishes standards by the boundary they cross:

- model to function: function calling and JSON-schema style invocation;
- agent to capability: MCP, OpenAPI, and runtime tool protocols;
- agent to agent: A2A, ACP, and ANP-style delegation;
- agent to repository or environment: AGENTS.md / AGENT.md and version-controlled policy files.

The tool-selection lesson is "fewer but better tools". Large static tool menus do not scale to evolving repositories or multi-tenant enterprise deployments. Useful systems need retrieval-aware tool registries, dynamic candidate pruning, and tool descriptions that are precise enough for both selection and safe invocation.

The source also connects tool competence to three levels:

- model training or fine-tuning for tool use;
- schema and interface quality;
- runtime selection, routing, and session policy.

### Context and Memory Management

The context layer controls what information the model sees at each step and how state persists across active, session, and long-term horizons.

The source argues that larger context windows do not solve memory. Context is expensive because attention has quadratic cost, and it is fragile because relevant information can be present but poorly placed. The paper cites lost-in-the-middle effects and context rot as reasons that context management must be active rather than passive accumulation.

The source organizes context by time horizon:

- short-term active context: system prompt, tool definitions, current history, tool results, retrieved documents, dynamic working state;
- mid-term session state: notes files, planning files, task artifacts, cross-run injection, and summary handoffs;
- long-term persistent memory: indexed memory stores, hybrid vector/graph/key-value memory, reflection, forgetting, shared memory, and multi-agent collective memory.

Long-horizon techniques include compaction, tool-result clearing, subagent context isolation, checkpoint/resume, and automatic consolidation hooks. The important claim is that context management should be handled by the harness infrastructure, not left entirely to the model's own reasoning.

The unresolved issue is context drift: over long trajectories, summaries, retrievals, and accumulated assumptions can diverge from the real task state. Context engineering alone cannot solve this; it needs verification loops, strategic human checkpoints, observability, and governance.

### Lifecycle and Orchestration

Lifecycle and orchestration governs how an agent carries a task across model calls, tool calls, failures, revisions, subtasks, and handoffs.

The source groups orchestration into three levels:

- single-agent inner loop: one agent observes, reasons, acts, receives feedback, and continues;
- multi-agent orchestration: specialized agents or subagents coordinate through hierarchy, teams, workflows, fan-out, or graph composition;
- full lifecycle pipeline: the task moves from issue/specification through planning, implementation, validation, review, and delivery.

It also distinguishes execution state:

- stateless replay reconstructs the run from recorded interaction history;
- stateful execution stores operational state in files, repositories, databases, task graphs, or services;
- hybrid designs combine replayable histories with persistent artifacts.

This source's placement of state management inside Lifecycle is important: operational state is not the same thing as model context or memory. It is the state the harness itself needs to continue execution, recover, retry, coordinate subtasks, and hand work to humans or other agents.

### Observability and Operations

Observability records agent behavior as structured evidence. The source treats traces as trees of spans covering model calls, tool invocations, retrieval steps, context assembly, latency, tokens, cost, errors, retries, and state transitions.

The paper separates:

- tracing and monitoring platforms, such as Langfuse, Opik, Arize Phoenix, MLflow, OpenTelemetry, OpenLLMetry, and OpenInference;
- agent-specific operations platforms, such as AgentOps, RagaAI Catalyst, Laminar, Watson, AgentLens, and reverse-engineering tools;
- cost tracking and optimization tools, such as TensorZero, Helicone, FrugalGPT, GPTCache, QC-Opt, TALE, and routing systems;
- reliability engineering patterns, including checkpoint/resume, failure taxonomies, root-cause isolation, anomaly detection, and managed-agent architectures.

The source's strongest observability point is that seeing what the agent did is not enough. Observability must connect to evaluation and harness revision. Production traces should become regression tests; evaluation failures should become monitoring signals; and cost, latency, and quality should be compared as a frontier rather than isolated metrics.

### Verification and Evaluation

Verification is presented as a task-to-feedback lifecycle, not a final leaderboard score.

The five stages are:

1. Task and benchmark grounding: define task, environment, tools, constraints, termination, and success criteria.
2. Pre-execution readiness validation: check sandbox, dependencies, tool availability, context state, permission policy, budget, and graders.
3. Controlled execution and trace capture: run reproducible rollouts while recording actions, tool calls, state changes, cost, latency, and errors.
4. Multi-level judgement and failure attribution: evaluate outcome, trajectory, and evaluator reliability, then localize failure across harness layers.
5. Continuous regression and deployment feedback: turn evaluation results into tests, monitoring, and future harness revisions.

This reframes evaluation as quality control over a model-harness pair. The final score remains useful, but it does not explain whether the task was specified well, whether the environment was valid, whether the path was safe and efficient, whether the evaluator was reliable, or which harness component should change next.

This aligns directly with [[wiki/concepts/Verification Loop]] and [[wiki/syntheses/AI Harness × Testing Strategy]]: agent tests are not merely post-hoc QA; they are feedback surfaces inside the runtime system.

### Governance and Security

Governance constrains what agents may do and records who bears accountability when constraints fail. The paper treats governance as a distinct ETCLOVG layer because production systems need permission engines, identity, policy languages, lifecycle hooks, hardening, audit, and human oversight.

The governance mechanisms include:

- permission models and identity management: static scopes, contextual per-call policy, authenticated delegation, agent identity, secret vaulting, and web-level manifests;
- lifecycle hooks: input guardrails, pre-invocation action validation, post-execution information-flow control, and human approval gates;
- component hardening: model hardening, runtime classifiers, MCP security, tool signing, protocol-level enforcement, and supply-chain defenses;
- declarative constitutions: training-time constitutions and deployment-time YAML or DSL rules;
- audit infrastructure: structured records of tool calls, arguments, risk category, policy decisions, result, cost, latency, identity, and integrity metadata.

The paper's governance section is important because it avoids treating safety as a model behavior problem alone. Governance lives across model alignment, runtime enforcement, tool integrity, identity, credentials, audit, and organizational accountability.

### Cross-Layer Synthesis

The source condenses harness engineering into several system-level effects.

#### Cost-Quality-Speed Trilemma

Stronger sandboxes, richer context, deeper observability, and more verification can improve reliability, but they add latency, cost, storage, and operational burden. Production harnesses must decide which risks justify synchronous checks, which can run asynchronously, and which telemetry is worth preserving.

#### Capability-Control Tradeoff

More capable agents need more authority, but every increase in authority expands the control problem. Larger tool menus, persistent memory, and permissive sandboxes increase coverage while also increasing selection error, prompt-injection surface, provenance risk, privacy risk, and blast radius.

#### Harness Coupling Problem

Harness layers are coupled. Tool descriptions consume context budget; execution environments affect evaluation; observability only becomes governance evidence when identity and permission state are captured; evaluation rewards or penalizes orchestration behavior. A local harness improvement can degrade the whole rollout when combined with the rest of the control loop.

This coupling is the paper's most useful bridge to existing wiki material: [[wiki/topics/AI Harness]] should be treated as a system, not as a bag of tools.

#### From Frameworks to Platforms

The ecosystem is moving from local agent frameworks toward managed platforms. Frameworks package agents, tools, memory, and loops; platforms add durable workspaces, managed sandboxes, identity, billing, observability, evaluation, governance, and human handoff across many runs and users.

The core design question shifts from "how do I build an agent?" to "how do I operate a fleet of agents whose actions remain inspectable and reversible over time?"

### Open Problems

The survey's open agenda has five major questions:

- how to harden and scale execution environments across security, portability, cost, reset, and workload fidelity;
- how to maintain reliable state in long-running agents, treating context management as state estimation rather than token packing;
- how to diagnose failures from traces instead of treating pass/fail scores as model-quality labels;
- how to standardize handoffs across agents, tools, sandboxes, evaluators, and humans with intent, constraints, permissions, provenance, risk, and unresolved decisions;
- how to keep harnesses useful as models improve, including removing controls that have become unnecessary and avoiding benchmark-overfit scaffolding.

The final open problem is especially important: harnesses should not monotonically accumulate scaffolding. Every wrapper, reset, verifier, planner, memory rule, and permission gate encodes an assumption about what the model cannot do reliably. As models change, the harness should be re-estimated, simplified, or replaced when the assumption is no longer load-bearing.

## Integration Decisions

This source should connect to the existing harness cluster without replacing it.

- [[wiki/topics/AI Harness]] is the stable topic page for harness as runtime order layer. This survey gives it a more systematic seven-layer vocabulary.
- [[wiki/sources/Harness Engineering Source Guide]] preserves the Martin Fowler article on user-owned coding-agent harnesses. The survey cites that practitioner thread but expands the scope to a research taxonomy and public ecosystem mapping.
- [[wiki/sources/Meta-Harness Paper Source Guide]] grounds automated harness optimization. This survey uses Meta-Harness as one of the key evidence points for the binding-constraint thesis.
- [[wiki/concepts/Coding Agent User Harness]] remains narrower than this survey: it is developer-controlled harnessing around coding agents, while this survey covers agent harness engineering generally.
- [[wiki/syntheses/Agent System Design Space]] can later absorb ETCLOVG as one comparative axis for agent platforms.

Potential promotions:

- ETCLOVG may deserve a dedicated concept page if it becomes a recurring local vocabulary.
- Harness coupling problem may deserve a synthesis with [[wiki/concepts/Feedback Flywheel]], [[wiki/concepts/Harness Ratchet]], and [[wiki/syntheses/AI Harness × Testing Strategy]] if future sources reinforce it.

For now, both should remain source-level terms to avoid overfitting the wiki to one survey.

## Open Questions

- How should the wiki reconcile the paper's 170+ versus 148+ corpus count?
- Which ETCLOVG layers are already well covered in this vault, and which need dedicated concept pages?
- Can the paper's taxonomy be turned into a practical design checklist for this user's own coding-agent harness?
- How should harness evaluations distinguish model improvement from controller/harness improvement in everyday engineering work?

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/maps/AI Map]]
- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Harnessability]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Governed Action]]
- [[wiki/syntheses/AI Harness × Testing Strategy]]
- [[wiki/syntheses/Agent System Design Space]]
- [[wiki/sources/Harness Engineering Source Guide]]
- [[wiki/sources/Meta-Harness Paper Source Guide]]
