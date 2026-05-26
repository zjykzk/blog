---
title: Bayes-Consistent Agentic Orchestration Paper River Source Guide
type: source
status: draft
summary: Preserves a paper-river reading of arXiv 2605.00742v2, tracing agent orchestration from tool action toward Bayesian cost-aware control.
category: sources
sources:
  - conversation:2026-05-26
  - https://arxiv.org/pdf/2605.00742v2
created: 2026-05-26T14:03:46+08:00
updated: 2026-05-26T14:03:46+08:00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-26
provenance:
  extracted: 0.74
  inferred: 0.22
  ambiguous: 0.04
aliases:
  - Agentic AI Orchestration Should Be Bayes-Consistent Paper River
  - Bayes-consistent orchestration paper river
  - arXiv 2605.00742v2 paper river
tags:
  - paper
  - arxiv
  - agents
  - harness
  - probability
---
# Bayes-Consistent Agentic Orchestration Paper River Source Guide

> Source: `ljg-paper-river` reading of `https://arxiv.org/pdf/2605.00742v2`, generated from the current conversation.

## Capture Policy

This page preserves the generated paper-river artifact, not a verbatim chat transcript. It should be read as a source-level guide to one constructed intellectual lineage around *Position: agentic AI orchestration should be Bayes-consistent*, while paper-grounded claims about the target paper itself should still be checked against the primary arXiv source.

The lineage is partly confirmed and partly synthetic. The target paper directly invokes agent action, tool use, model routing, uncertainty estimation, Bayesian decision theory, and cost-aware orchestration. The exact single-chain sequence below is an interpretive organization of the problem's evolution rather than a claim that every later paper explicitly criticizes the immediately previous one. ^[inferred]

## What It Covers

The captured paper river frames the core question as: when an agent can call tools, ask humans, route to another model, continue searching, stop, or escalate, what principle should decide the next action?

The central answer is that agentic systems should separate prediction from decision. LLMs and tools provide evidence; an external orchestration layer maintains task-level belief, utility, cost, and value of information. This positions Bayesian consistency as a property of the control layer rather than a requirement that the LLM's internal weights behave as a full Bayesian learner.

This belongs in the wiki because it connects [[wiki/topics/AI Harness]], [[wiki/concepts/Agentic Control Loop]], [[wiki/topics/Tool Routing]], [[wiki/topics/Probability]], and [[wiki/syntheses/不确定性下的判断]] into one agent-system control problem.

## Preserved Content

### Problem River

The paper river begins from a shift in agent research: the hard question is no longer only whether an LLM can reason or call a tool, but whether the surrounding system can decide *which* action is worth taking under uncertainty and cost.

Early LLM agents make models act: they can think, call tools, observe results, and continue. Real deployments expose a second-order problem: each action has a price. More search costs latency and money; more model calls can amplify correlated mistakes; more questions can burden users; premature stopping can leave important evidence unseen.

The target paper's architectural claim is therefore pragmatic: do not force the LLM itself to be the full Bayesian agent. Treat the LLM as a black-box predictor or evidence source, and put Bayesian belief state, utility, and value-of-information logic in the orchestration layer.

### Source Map

```text
[1965/1966] Value of information
  |
  | Problem: information is not free; more evidence must justify its cost.
  | Move: buy information only when expected decision improvement exceeds cost.
  v
[1985/2010] Bayesian decision theory
  |
  | Problem: probability alone does not select actions.
  | Move: connect posterior belief to expected utility.
  v
[2022/2023] ReAct
  |
  | Problem: LLMs can answer but cannot reliably revise through environment feedback.
  | Move: interleave reasoning, action, and observation.
  v
[2023] Toolformer
  |
  | Problem: tool use cannot depend only on hand-written prompting patterns.
  | Move: let the model learn when and how to call APIs.
  v
[2024/2025] DeLLMa / RouteLLM
  |
  | Problem: decision quality and model choice both carry cost.
  | Move: structure decisions and route between models by quality-cost tradeoff.
  v
[2025/2026] Structured uncertainty / Bayesian orchestration
  |
  | Problem: ambiguous tasks require deciding what to ask, whom to trust, and when to stop.
  | Move: use uncertainty, EVPI, Bayes updates, and cost-aware multi-LLM orchestration.
  v
[2026] Bayes-consistent agentic orchestration
  |
  | Problem: local tricks have not become an agent architecture principle.
  | Move: put Bayesian consistency in the control layer around LLMs and tools.
```

### Value of Information: Information Also Has a Price

The value-of-information root says that information is not automatically worth acquiring. A medical test, tool call, search query, human clarification, or model escalation should be judged by whether it is likely to change the final action enough to justify its cost.

For agents, this turns "continue thinking" into an economic decision. The system should not search merely because the model is uncertain; it should search when the expected value of the additional observation exceeds the cost.

This root leaves open how beliefs are represented and updated, which leads into Bayesian decision theory.

### Bayesian Decision Theory: Belief Must Connect to Action

Bayesian decision theory joins three pieces: prior belief, evidence-driven posterior updating, and action selection by posterior expected utility.

The captured explanation stresses that probability alone is incomplete. A 10% chance of recommending the wrong movie and a 10% chance of missing a medical risk imply different actions because the loss functions differ. A useful agent controller therefore needs a task-level ledger: what hypotheses are live, how credible they are, what each action costs, and what happens if the action is wrong.

This is a natural fit for an orchestration layer. It is less natural as a literal description of an LLM's internal token probabilities, because token-level confidence is not the same as task-level uncertainty. ^[inferred]

### ReAct: LLMs Become Actors

ReAct moves LLMs from one-shot answerers toward actors in an environment. It interleaves thought, action, observation, and further thought.

The paper river frames ReAct as solving the access problem: the model can now touch external state and revise from feedback. Its remaining gap is control: the loop has a shape, but stopping, evidence value, tool reliability, and action cost remain mostly outside the formalism.

This makes ReAct a behavior root for [[wiki/concepts/Agentic Control Loop]] and [[wiki/concepts/Workflow Graph Orchestration]].

### Toolformer: Tool Calling Becomes Model Capability

Toolformer pushes tool use inside model behavior. Instead of relying only on hand-written examples and workflows, the model learns when to call APIs, what arguments to pass, and how to incorporate returns.

The paper river treats this as a move from scaffolded tool use toward learned tool use. Its remaining gap is still decision quality under cost. Knowing how to call a tool is not the same as knowing whether this particular call is worth making.

This connects directly to [[wiki/topics/Tool Routing]]: the tool surface is not only an affordance list but a routing and cost-control problem.

### DeLLMa and RouteLLM: Decisions and Routing Become Cost-Sensitive

DeLLMa represents a move from "ask the LLM for a decision" toward structuring decision problems before using the model. It introduces decision-theoretic and utility-theoretic scaffolding around LLM reasoning.

RouteLLM represents a practical cost-quality version of the same control question. A system with a cheap model and an expensive model must decide when the expensive model is worth using. This reframes model choice as a small orchestration problem: route requests by expected quality improvement under cost constraints.

The paper river treats these as neighboring branches, not a strict citation chain. Together they make cost-sensitive orchestration visible, but they do not yet unify tool calls, clarifying questions, stopping, escalation, evidence reliability, and posterior belief into one control layer. ^[inferred]

### Structured Uncertainty and Bayesian Multi-LLM Orchestration

Structured uncertainty work moves uncertainty from a vague scalar into task structure. For tool-calling agents, uncertainty often sits in missing or ambiguous arguments: location, budget, time, entity identity, risk tolerance, or user intent.

The captured SAGE-Agent reading says the useful question is not just "am I uncertain?" but "which parameter is uncertain, and which clarification question has the highest expected value?" This brings value of information directly into tool-calling behavior.

The captured Amin reading gives a more explicit Bayesian orchestration form: treat multiple LLMs as approximate likelihood sources, combine evidence under a prior, update belief with Bayes rule, and choose whether to stop, continue, or consult another model based on expected cost. This becomes the closest engineering ancestor to the target paper's control-layer stance. ^[inferred]

### Target Paper: Bayesian Consistency Belongs in the Orchestrator

The target paper's strongest architectural move is the separation between prediction and decision.

LLMs and tools provide observations or likelihood-like signals. The orchestrator maintains task-relevant latent variables, belief state, utility, and action costs. It then chooses actions by posterior expected utility or value of information: answer, ask, search, call a tool, route to another model, escalate to a human, or stop.

This avoids treating the LLM's next-token probability as equivalent to task confidence. A model can be fluent while wrong, hesitant while correct, or confident about wording while uncertain about the world. The control layer must therefore manage evidence at the task level.

The paper river's compact slogan is: the LLM is not the judge; it is a witness. The orchestrator is responsible for combining testimony, accounting for reliability and dependence, and deciding what action is worth taking. ^[inferred]

### Remaining Technical Gaps

The paper river identifies several hard problems that remain after accepting the target paper's stance:

- learning or specifying observation models for free-form LLM outputs and tool traces
- translating natural-language evidence into likelihood-like updates
- avoiding overconfidence when multiple LLMs share training data, prompts, tools, or prior mistakes
- defining utility functions without hiding human judgment behind numeric theater
- deciding when conservative updating, recalibration, abstention, or human escalation should override automatic action

These gaps are source-level research directions, not settled wiki conclusions.

### Frontier Extension

At capture time, no confirmed later paper in this conversation directly cites and improves the target paper. The target paper's arXiv v2 date is May 2026, so the paper river treats it as current frontier rather than a midstream node.

The likely next step is "Bayesian-ish agent runtime" rather than fully Bayesian LLM weights: framework-level belief state, utility-aware routers, value-of-information query selection, calibrated evidence models, and dependence-aware evidence pooling. ^[inferred]

### Compressed Overview

```text
time        1965       1985        2023          2024/25          2026
            |          |           |             |                |
problem     info cost  belief->act action loop   cost routing     control layer
            |          |           |             |                |
idea        VOI        Bayes DT    ReAct/Tools   DeLLMa/Route     Bayes-consistent
                                                            orchestration

what moved  "ask?"     "act?"      "can act?"    "which/when?"    "what governs
                                                                    action choice?"

unit        evidence   utility     tool step     model/query      belief state
of control                                     selection          plus utility
```

## Integration Decisions

This source guide should strengthen the agent-control side of [[wiki/topics/AI Harness]]. It adds a sharper rule: orchestration is not only graph traversal, retries, tools, and permissions; it is also the cost-sensitive management of belief and action under uncertainty.

It should not replace [[wiki/topics/Probability]] or [[wiki/syntheses/不确定性下的判断]]. Those pages are broader human and conceptual frames. This guide adds the AI-agent engineering instantiation: uncertainty is operationalized as belief state, observation value, stopping policy, routing, and escalation.

It also connects to [[wiki/concepts/Governed Action]]: governed action in agents should eventually include not only permission and workflow policy but also belief, utility, and expected information value. ^[inferred]

The phrase "Bayes-consistent orchestration" is promotable as a future concept page if more sources accumulate. For now it remains source-level because this capture is based on one position paper plus an interpretive paper-river chain.

## Open Questions

- How should an agent framework represent task-level belief state without making developers write full probabilistic programs for every workflow?
- Can LLM outputs be calibrated into observation models robustly enough for high-stakes action selection?
- How should orchestrators handle evidence dependence when several LLMs likely share training data or repeat each other's reasoning?
- What developer interface makes utility and action cost explicit without creating fake precision?
- Should value-of-information gates become default primitives in agent frameworks, or remain application-specific policy?

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Agentic Control Loop]]
- [[wiki/topics/Tool Routing]]
- [[wiki/concepts/Workflow Graph Orchestration]]
- [[wiki/topics/Probability]]
- [[wiki/syntheses/不确定性下的判断]]
- [[wiki/concepts/Governed Action]]
- [[wiki/sources/Agentic Artificial Intelligence Paper Source Guide]]
