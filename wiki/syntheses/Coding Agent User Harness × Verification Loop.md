---
title: Coding Agent User Harness × Verification Loop
category: syntheses
type: synthesis
status: draft
tags: [agents, harness, ai-coding, testing]
sources:
  - wiki/concepts/Coding Agent User Harness
  - wiki/concepts/Verification Loop
  - wiki/concepts/Agentic Engineering
  - wiki/concepts/Computational and Inferential Controls
  - wiki/concepts/Feedforward and Feedback Controls
  - wiki/concepts/Harness Ratchet
  - wiki/sources/Harness Engineering Source Guide
created: 2026-05-23T02:28:40+08:00
updated: 2026-06-09T10:56:14+08:00
summary: A user harness becomes useful when verification signals enter the loop early enough to steer agents and update durable controls.
provenance:
  extracted: 0.22
  inferred: 0.70
  ambiguous: 0.08
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-23
---
# Coding Agent User Harness × Verification Loop

## The Connection

[[wiki/concepts/Coding Agent User Harness]] is the environment a developer or team shapes around a coding agent. [[wiki/concepts/Verification Loop]] is the feedback path that tells the harness whether the agent's work is correct, acceptable, or risky.

Their connection is operational: a user harness without verification is mostly guidance; verification without a user harness is mostly inspection. Together they become a steering system that can make errors visible while there is still time to correct them. ^[inferred]

## Where They Co-occur

The pair appears in pages about agentic engineering, controls, harness ratchets, and source guides for coding-agent practice:

- [[wiki/concepts/Agentic Engineering]] shifts senior engineers from prompting toward training harnesses.
- [[wiki/concepts/Computational and Inferential Controls]] separates executable checks from semantic judgment.
- [[wiki/concepts/Feedforward and Feedback Controls]] distinguishes guide-before-action from sensor-after-action.
- [[wiki/concepts/Harness Ratchet]] turns repeated failures into durable harness changes.
- [[wiki/sources/Harness Engineering Source Guide]] frames guides and sensors as a user-owned coding-agent control loop.
- [[wiki/sources/Maintainability Sensors for Coding Agents Source Guide]] gives maintainability examples: linting, dependency rules, coupling data, and AI modularity review.

## Cross-cutting Insight

The practical unit of AI coding improvement is not a better prompt; it is a shorter path from generated work to usable truth signal. ^[inferred]

A coding-agent user harness compounds when verification output changes durable control surfaces: rules, tests, hooks, review rubrics, task templates, skill instructions, or done conditions. If verification only catches today's error, the harness remains manual QA. If verification changes next week's default environment, it becomes harness learning. ^[inferred]

## Tensions and Trade-offs

- **Fast checks vs. deep judgment**: tests and linters can run early and often, while product fit, architecture, and maintainability may require slower inferential review.
- **Agent self-correction vs. human authority**: agents can repair failing tests, but humans must still own ambiguous trade-offs and high-risk acceptance.
- **More sensors vs. feedback overload**: too many failing checks can bury the useful signal and push agents into local compliance rather than good design.
- **One-off review vs. harness ratchet**: review comments are cheap in the moment but expensive if they never become reusable controls.

## Open Questions

- Which verification signals should be fed back to the agent automatically, and which should stop for human review?
- How should teams measure whether a verification loop reduces review burden rather than moving it into tool maintenance?
- When does a harness sensor encourage overfitting to local checks instead of improving real quality?

## Related

- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Computational and Inferential Controls]]
