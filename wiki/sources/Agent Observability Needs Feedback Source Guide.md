---
title: Agent Observability Needs Feedback Source Guide
category: sources
tags:
  - article
  - agents
  - harness
  - feedback
  - context
aliases:
  - Agent observability needs feedback to power learning
  - Harrison Chase Agent Observability Feedback Source Guide
sources:
  - https://x.com/hwchase17/status/2051708710859501807
  - conversation:2026-05-12
created: 2026-05-12T12:20:47+08:00
updated: 2026-05-12T12:20:47+08:00
summary: Source guide for Harrison Chase's X article arguing that agent observability must store traces and feedback together to power model, harness, and context learning.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-12
---
# Agent Observability Needs Feedback Source Guide

> Source: Harrison Chase, “Agent observability needs feedback to power learning”, https://x.com/hwchase17/status/2051708710859501807

## Capture Policy

This page preserves the source-level content of Harrison Chase's X article rather than reducing it to a short observability takeaway. It keeps the article's argument flow, diagram structure, feedback taxonomy, platform requirements, and product examples so later wiki pages can distinguish source claims from promoted synthesis.

The stable conceptual implications belong in [[wiki/topics/AI Harness]], [[wiki/topics/AI Memory]], [[wiki/concepts/Feedforward and Feedback Controls]], and [[wiki/concepts/Continual Learning for AI Agents]]. This page remains the source-facing artifact for what the article itself says.

## What It Covers

The article argues that agent observability is too narrow if treated only as debugging. Traces show what happened, but they do not by themselves say whether the agent's behavior was useful, accepted, rejected, inefficient, risky, or wrong. For agent systems, observability must connect traces with feedback so production behavior can become learning material.

The article positions this as a difference between traditional software observability and agent observability. In traditional software systems, user feedback can be separated from observability more safely. In agent systems, the author argues that traces and feedback need to be linked closely because improving an agent depends on knowing not only what happened, but what that behavior meant.

## Preserved Content

### Opening Thesis

Most teams first treat agent observability as a debugging tool: something went wrong, so a developer opens the trace, inspects the steps, and identifies where the agent made a bad decision. The article says this is useful but too narrow.

The deeper role of agent observability is to power learning. Traces alone do not create that loop. A learning loop also needs feedback: signals about whether the agent behavior was useful, accepted, rejected, inefficient, risky, or wrong.

The article's strongest claim is:

> With software, it is somewhat acceptable for user feedback to be separate from observability. With agents, feedback and observability need to be closely linked.

This claim is not limited to model training. It applies across the whole agent system:

- what the model should do;
- how the harness should guide the model;
- what context the agent needs;
- which failure modes recur;
- which behaviors actually work for users.

Traces are not merely records of what happened, and feedback is not merely a rating at the end. Together, they are raw material for improving the system.

### Diagram: Agent Observability Powers Learning Loops

The source includes a diagram titled:

```text
Agent observability powers learning loops
```

Subtitle:

```text
Traces show what happened. Feedback says what it meant. Together, they drive changes to the agent system.
```

The diagram forms a four-step loop:

```text
Traces
  Model calls, tool calls, context, outputs, errors, and intermediate state.
    -> Feedback
       User ratings, behavioral signals, LLM judges, rules, and regex checks.
         -> Learning
            Identify what failed, what worked, and which improvements are worth making.
              -> Changes
                 Update prompts, tools, memory, routing, eval datasets, or model behavior.
                   -> back to Traces
```

The diagram's bottom note says:

```text
The loop only works when traces and feedback are stored together. Otherwise, traces remain raw trajectories instead of learning signals.
```

This is the source's core mechanism: observability becomes learning only when trajectories and meaning-bearing signals are joined.

### Learning Happens at Multiple Levels

The article links back to Harrison Chase's earlier article on [[wiki/sources/Continual Learning for AI Agents Source Guide|continual learning for AI agents]]. The earlier framework separates learning into model, harness, and context layers. This article applies that framework to observability and feedback.

#### Model-Level Learning

Learning can happen at the model level when traces show recurring model failures, such as:

- consistently misclassifying a request;
- choosing the wrong tool;
- failing to follow a policy.

Those traces can be used to update model weights through supervised fine-tuning or reinforcement learning.

#### Harness-Level Learning

Learning can happen at the harness level. The harness includes everything around the model:

- prompts;
- tool schemas;
- permission checks;
- control flow;
- memory update logic;
- routing;
- retries;
- guardrails.

A trace may show that the model had the capability to solve the task, but the scaffolding around it was wrong. The article gives examples:

- the tool description was ambiguous;
- the agent needed a read-before-write constraint;
- the system prompt made the wrong tradeoff.

This positions traces as evidence for improving [[wiki/topics/AI Harness|AI Harness]] design rather than only evaluating the base model. ^[inferred]

#### Context-Level Learning

Learning can also happen at the context level. Agents are sensitive to the information they receive:

- retrieved documents;
- memory;
- user preferences;
- tool results;
- prior turns;
- environment state.

A trace can show that the model made a reasonable decision given bad or missing context. In that case, the learning loop should improve what context is retrieved, stored, compressed, or discarded. The article notes that this is commonly called memory.

The important point is that all of these learning loops require traces. Without knowing what the agent saw, what it did, and what happened next, a team cannot reliably know what to improve.

### Diagram: Agents Learn at Three Levels

The source includes a second diagram titled:

```text
Agents learn at three levels
```

Subtitle:

```text
The fix for a bad trace is not always a better model. Sometimes the system needs to learn elsewhere.
```

The diagram shows:

```text
Traces + feedback
  What happened, whether it worked, and which behavior should change.
    -> Model
       Improve reasoning, classification, tool choice, policy following, or task completion behavior.
    -> Harness
       Improve prompts, tool schemas, permissions, routing, memory writes, retries, and control flow.
    -> Context
       Improve retrieved docs, user/session state, memory, tool results, compression, and context selection.
```

Footer:

```text
A trace shows which layer had enough information to act correctly, and feedback tells you whether that action was actually useful.
```

This diagram gives a routing test for improvement work: determine whether the failure belongs to the model, harness, or context layer before deciding what to change. ^[inferred]

### Learning Can Be Automated or Hand-Driven

The article distinguishes hand-driven learning from automated learning.

Hand-driven learning includes cases where:

- a developer looks at a trace, notices that the agent called the wrong tool, and updates a prompt or tool schema;
- a product manager reviews failed conversations and realizes the product needs a new workflow;
- an annotator labels traces so the team can build a better evaluation dataset.

The source emphasizes that this is still learning even with a human in the loop.

Automated learning includes systems that:

- sample production traces;
- run online evaluations;
- detect known failure patterns;
- add examples to a dataset;
- trigger review queues when something looks wrong.

The article clarifies that the agent does not need to improve itself automatically for the learning loop to be automated. Automation can simply identify which traces deserve attention and turn them into structured feedback.

For a single low-volume agent, manual review may be enough. For many agents or high-volume production traffic, this becomes an infrastructure problem: capture traces, filter them, score them, route them, and preserve the traces that matter.

### Traces Are Necessary but Not Sufficient

A trace tells what happened. It does not tell whether what happened was good.

The article gives examples:

- An agent can complete a task in 40 steps, but perhaps the same task should have taken 6.
- An agent can produce a confident answer, but perhaps the user rejected it.
- An agent can avoid throwing an error, but still fail the user's intent.
- An agent can call the right tool with subtly wrong arguments.

Feedback turns observability from a passive record into a training signal, debugging signal, product signal, or evaluation signal.

With feedback, teams can ask:

- Which traces represent success?
- Which traces represent failure?
- Which failures are caused by the model, harness, or context?
- Which failures are worth turning into evals?
- Which behaviors are improving over time?

The article's core requirement is to store feedback with agent observability data.

### Feedback Comes from Many Places

The source says feedback does not require a human to manually grade every trace. Useful feedback has several forms.

#### Explicit Feedback

Direct user feedback includes:

- thumbs up / thumbs down;
- star ratings;
- written corrections.

This signal is easy to understand but usually sparse because most users do not leave explicit feedback.

#### Behavioral Feedback

Indirect user feedback comes from what the user does after receiving an output. Examples include:

- for a coding agent: lines of code accepted, diffs reverted, tests passed after edits, or whether the user kept the generated change;
- for a support agent: whether the user reopened the ticket;
- for a research agent: whether the user copied the answer or asked the same question again.

Behavioral signals are noisier than explicit ratings but often more plentiful.

#### Generated Feedback

Feedback can be generated by an LLM-as-judge. A judge can score:

- whether an answer was helpful;
- whether an agent followed policy;
- whether a trajectory looks suspicious.

The source frames this as useful because it can run at scale, especially as an online evaluator over production traces. The article notes that it is not perfect and should be calibrated, but it gives teams a way to create structured feedback when human review is too slow.

#### Deterministic Feedback

Feedback can also be deterministic. The article says rules and regexes are underrated. If a team knows a failure pattern, it can encode it.

Examples include:

- check whether an agent calls a destructive command without approval;
- validate that a response contains a required citation;
- detect signs of user frustration.

The source uses the Claude Code leak as an example. Multiple reports found that Claude Code used a regex in `userPromptKeywords.ts` to detect frustration words and phrases in user prompts. The article cites PCWorld's report that the regex looked for terms such as “wtf,” “horrible,” “awful,” and “this sucks.” It also mentions Slashdot's summary and Blake Crosley's analysis, which described the pattern as regex-based frustration detection rather than LLM inference.

The engineering lesson is that not every feedback signal needs a model call. If a cheap rule captures a useful signal, use the cheap rule, while being clear about how that signal is stored and used.

### Diagram: Feedback Signals Come from Many Places

The article includes a diagram titled:

```text
Feedback signals come from many places
```

Subtitle:

```text
Useful feedback can be explicit, behavioral, generated, or deterministic. The best systems combine several signals.
```

The four categories are:

```text
Explicit — Direct user feedback
The user tells you whether the agent helped.
- Thumbs up / thumbs down
- Ratings
- Written corrections

Behavioral — Indirect user feedback
User behavior reveals whether the output was useful.
- Lines of code accepted
- Ticket reopened
- Answer copied or reused

Generated — LLM-as-judge
A model scores traces for quality, policy, or perceived errors.
- Helpfulness score
- Task success judgment
- Trajectory critique

Deterministic — Rules and regexes
Known patterns are captured with cheap, reliable checks.
- Required citation present
- Dangerous command detected
- Frustration keyword matched
```

This diagram provides a compact taxonomy of feedback sources for agent observability.

### What an Observability Platform Needs

If observability powers learning, the article says the platform needs three capabilities.

#### Requirement 1: Store Traces

The platform must capture the full trajectory of agent behavior:

- model calls;
- tool calls;
- inputs and outputs;
- metadata and errors;
- timing;
- intermediate state.

The article says the platform should ideally ingest traces from whatever stack the team uses, not only one framework. It states that LangSmith supports tracing from 30+ frameworks and can ingest traces from OpenTelemetry-compatible applications through OpenTelemetry tracing.

#### Requirement 2: Store Feedback

Feedback should not live in a spreadsheet or analytics system disconnected from the trace. It should attach directly to the run, trace, or thread it evaluates.

This makes it possible to:

- filter by feedback;
- compare good and bad trajectories;
- build datasets from real failures;
- track whether changes improve the behaviors that matter.

The article states that LangSmith supports capturing feedback and associating it with traces.

#### Requirement 3: Generate Feedback

Some feedback will come from users, but much useful feedback should be produced by the system itself. This includes:

- rules;
- evaluators;
- sampling;
- annotation queues;
- alerts;
- backfills over historical traces.

The article states that LangSmith supports automation rules and online evaluations, including LLM-as-judge evaluators that run on production traces.

The product shape named by the source is:

```text
store traces, store feedback, generate feedback
```

### Diagram: What Agent Observability Needs to Support Learning

The article includes a platform-requirements diagram titled:

```text
What agent observability needs to support learning
```

Subtitle:

```text
A platform is not complete if it only stores traces. It also needs feedback as first-class data.
```

The three cards are:

```text
Requirement 1 — Store traces
Capture the full trajectory of agent behavior.
- Model calls
- Tool calls
- Inputs and outputs
- Metadata and errors
- OpenTelemetry-compatible ingestion

Requirement 2 — Store feedback
Attach quality signals to the exact run, trace, or thread they evaluate.
- User ratings
- Behavioral signals
- Human annotations
- Judge scores
- Rule outputs

Requirement 3 — Generate feedback
Create signals automatically so teams can scale review and evaluation.
- Automation rules
- Online evaluations
- LLM-as-judge
- Sampling and queues
- Alerts and backfills
```

Bottom note:

```text
LangSmith brings these together: trace ingestion, feedback attached to traces, and generated feedback through rules and online evaluations.
```

### Closing Claim

The article closes with the claim that the point of observability is not merely to look at traces. The point is to learn from them.

Traces tell what happened. Feedback tells what it meant. Together, they let teams improve the model, harness, and context. They support hand-driven debugging and automated evaluation. They turn production behavior into datasets, rules, alerts, and regression tests.

Agent observability without feedback is incomplete. It allows inspection, but not systematic learning. Storing feedback with traces turns agent traces from logs into a learning system.

### Publication Metadata

The browser-rendered X page shows:

- Author/account: Harrison Chase, `@hwchase17`.
- Title: “Agent observability needs feedback to power learning”.
- Displayed timestamp: 1:00 AM · May 6, 2026.
- Visible engagement at capture time: 11 replies, 52 reposts, 209 likes, 314 bookmarks, 57.3K views.

## Integration Decisions

This source belongs in the AI / Agent cluster because it extends the existing continual-learning, harness, memory, and evaluation threads.

Integration routes:

- [[wiki/sources/Continual Learning for AI Agents Source Guide]] supplies the model/harness/context learning-layer frame that this article applies to observability.
- [[wiki/concepts/Continual Learning for AI Agents]] should treat trace-plus-feedback observability as the substrate that decides which learning layer to update.
- [[wiki/topics/AI Harness]] should use this source for the idea that harness improvement requires trace-linked feedback, not just trace inspection.
- [[wiki/topics/AI Memory]] should use this source for context-level learning from traces, especially improving retrieval, compression, storage, and discard rules.
- [[wiki/concepts/Feedforward and Feedback Controls]] should use this source's feedback taxonomy as concrete examples of feedback controls: explicit ratings, behavioral signals, LLM judges, rules, and regexes.
- [[wiki/concepts/Harness Ratchet]] should use this source as a production version of the ratchet: repeated failures become prompts, tools, memory updates, routing changes, eval datasets, rules, alerts, or model updates only when feedback identifies what the trace means. ^[inferred]

Source-level claims about LangSmith, OpenTelemetry integration, PCWorld's Claude Code report, Slashdot's summary, and Blake Crosley's analysis should remain source-level until corroborated through their primary sources. ^[inferred]

## Open Questions

- How should a production agent platform weight sparse explicit feedback against noisy behavioral feedback? ^[inferred]
- Which feedback signals are safe enough to automate into memory or harness changes without human review? ^[inferred]
- How should teams prevent LLM-as-judge feedback from creating self-reinforcing model bias in evaluation loops? ^[inferred]
- What governance should apply when deterministic frustration detection is stored and used as feedback about the user? ^[inferred]

## Related

- [[wiki/sources/Continual Learning for AI Agents Source Guide]]
- [[wiki/concepts/Continual Learning for AI Agents]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/AI Memory]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Feedforward and Feedback Controls]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Feedback Loops]]
- [[wiki/syntheses/Agent System Design Space]]
