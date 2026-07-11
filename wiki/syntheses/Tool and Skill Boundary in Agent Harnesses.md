---
title: Tool and Skill Boundary in Agent Harnesses
category: syntheses
type: synthesis
status: draft
tags: [agents, harness, tools, skills, workflow]
sources:
  - conversation:2026-05-29
created: 2026-05-29T17:04:21+0800
updated: 2026-07-12T00:07:31+0800
summary: Agent harnesses separate executable tool capabilities from skill-level business SOPs; both are selected through descriptions, but they operate at different layers.
provenance:
  extracted: 0.77
  inferred: 0.23
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-29
aliases:
  - harness tool skill boundary
  - tool 与 skill 的边界
---
# Tool and Skill Boundary in Agent Harnesses

## Context

Agent harnesses often expose both tools and skills to an LLM-facing agent. They can look similar from the outside because both have names, descriptions, and activation rules, and the model uses those descriptions to decide what to use next.

The important distinction is not whether the model saw a description. The distinction is what layer of the agent system the described object controls. ^[inferred]

## Finding / Decision

In an agent harness, a tool is an executable capability at the boundary between the agent and the external environment. A skill is a business-semantic workflow or SOP that teaches the agent how to complete a class of tasks.

Tools answer: what can the agent do to the world?

Skills answer: how should the agent perform this kind of work?

This makes the clean boundary: ^[inferred]

| Layer | Tool | Skill |
|---|---|---|
| Primary abstraction | Capability / actuator / IO boundary | Policy / playbook / SOP / task schema |
| Main question | What external action is available? | What workflow should govern this task? |
| Invocation effect | Executes an operation or queries an external system | Loads instructions, references, scripts, templates, and constraints into the agent's working context |
| Business semantics | Usually thin and interface-level | Usually central |
| Example | run a shell command, read a file, open a browser, search web, generate image | capture a conversation into wiki, review a PR, ingest a source, build a travel research brief |

## Reasoning

The LLM may use descriptions for both layers, but the descriptions play different roles.

A tool description decides whether the model should make a direct tool call and how to fill the tool's schema. The tool then performs an externally visible operation, such as reading files, executing commands, fetching a page, or creating an image.

A skill description decides whether the agent should load a task-specific method. After loading, the skill changes the agent's operating procedure: what to inspect first, what output structure to produce, which references or scripts to prefer, what risks to avoid, and how to verify success.

So a typical flow is: ^[inferred]

```text
user request
  -> skill routing decides whether a task SOP should enter context
  -> the loaded skill shapes the plan, constraints, and success criteria
  -> tool routing decides which executable capabilities to call
  -> tools perform the external actions
```

This also explains why skill is not just a saved prompt. A useful skill packages domain meaning, sequence, validation, and local conventions. It can include scripts and templates, but the skill's main value is the business workflow that chooses when and how those assets matter. ^[inferred]

Tools can still carry some domain semantics. A finance lookup tool, weather tool, ticket-creation MCP tool, or image-generation tool is not a completely neutral primitive. But that semantics remains interface semantics: the tool defines a bounded operation the agent can execute. It does not usually define the full business SOP for a task. ^[inferred]

## Implications

Harness design should avoid mixing the layers. ^[inferred]

If a behavior is mostly about external action, authorization, and IO, it belongs closer to the tool layer. Its design questions are schema, permission, sandboxing, reliability, observability, and error handling. ^[inferred]

If a behavior is mostly about task judgment, ordering, domain conventions, output shape, and verification criteria, it belongs closer to the skill layer. Its design questions are activation boundary, workflow sequence, reference loading, examples, failure modes, and maintenance. ^[inferred]

This distinction also clarifies evaluation: ^[inferred]

- tool quality is judged by whether the operation is safe, clear, bounded, reliable, and easy for the model to call correctly; ^[inferred]
- skill quality is judged by whether the right workflow activates at the right time and improves task outcomes without polluting context. ^[inferred]

For mature harnesses, both layers interact. A skill can instruct the agent to use certain tools, and a tool can expose a capability that makes a skill practical. But collapsing them into one concept hides the most important design choice: whether the agent needs a new action surface or a better procedure for using existing surfaces. ^[inferred]

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/concepts/Agent Tool]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Agent Action Space]]
- [[wiki/topics/Tool Routing]]
- [[wiki/syntheses/Agent Skill × Context Management]]
