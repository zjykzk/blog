---
title: Block Agent Skills Design Principles Source Guide
category: sources
tags:
  - article
  - agents
  - skills
  - workflow
  - ai-coding
sources:
  - https://engineering.block.xyz/blog/3-principles-for-designing-agent-skills
source_url: https://engineering.block.xyz/blog/3-principles-for-designing-agent-skills
author: Angie Jones
created: 2026-07-04T13:49:20+0800
updated: 2026-07-04T13:49:20+0800
summary: Block's engineering post frames good agent skills as executable tribal knowledge with deterministic scripts, agent judgment zones, constitutional constraints, and action arcs.
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
base_confidence: 0.45
lifecycle: draft
lifecycle_changed: 2026-07-04
---
# Block Agent Skills Design Principles Source Guide

## Source Role

This source guide preserves Angie Jones's Block Engineering post on designing agent skills. It belongs in the [[wiki/sources/Agent Engineering Source Guide]] cluster because it turns agent skill design into a concrete engineering boundary problem: what must be deterministic, what should remain model-mediated, and how the skill output should become the next action context.

## Core Takeaways

- Agent skills package team-specific tribal knowledge so agents can use it on demand, rather than leaving it in scattered docs or individual memory.
- Block treats skills as version-controlled repository artifacts: skills can be reviewed, updated, bundled for teams, and distributed through an internal marketplace.
- The first design principle is to remove from the model any decision that must be reproducible across runs or teams. Scoring, fixed commands, SQL query structure, naming formats, and style-guide gates should live in scripts, templates, or hard rules.
- The second design principle is to preserve the model's strengths where context interpretation, generation, prioritization, conversation, or exception handling are required.
- The third design principle is to write `SKILL.md` as a constitution, not a suggestion: explicit constraints prevent the agent from being helpfully inconsistent, softening deterministic results, skipping steps, or adding unapproved checks.
- The bonus principle is to design for the arc: diagnostic or investigation skills should turn script output into agent context so the next likely user action can happen in the same session.

## Promoted Claims

- [[wiki/concepts/Agent Skill]] should be understood as a versioned execution surface for team knowledge, not merely a reusable prompt.
- [[wiki/concepts/Computational and Inferential Controls]] maps directly onto skill design: deterministic scripts and templates handle same-input/same-output surfaces, while the agent handles explanation, creation, and conversation.
- [[wiki/topics/AI Skills Workflow]] gains a sharper action-arc test: after the first output, ask what the user will want to do next, and ensure the skill gives the agent enough context and permission boundaries to help.
- [[wiki/concepts/Encoding Team Standards]] is strengthened by Block's marketplace framing: style guides, oncall runbooks, feature-flag procedures, and API rules become executable, reviewed, version-controlled team infrastructure.

## Design Frame

Block's three principles can be compressed into one control question:

> A skill designer is deciding which parts of work need invariance, which parts need intelligence, and which rules must constrain helpfulness.

This makes skill authoring closer to workflow architecture than prompt writing. The skill is responsible for locating the deterministic/inferential boundary, naming the agent's allowed discretion, and creating the handoff from evidence to next action. ^[inferred]

## Open Questions

- How should teams evaluate whether an internal skill marketplace is reducing tribal-knowledge loss versus creating redundant or stale skills? ^[inferred]
- When should a deterministic scoring script use binary checks rather than graded checks, and how should teams handle cases where partial credit reflects real maturity? ^[inferred]
- How should constitutional skill rules be tested so they do not over-constrain legitimate exception handling? ^[inferred]

## Related

- [[wiki/concepts/Agent Skill]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/syntheses/Agent Skill Patterns as Human Workflow Control Structures]]
- [[wiki/sources/Designing Refining and Maintaining Agent Skills at Perplexity Source Guide]]

## Preserved Content

```text
~/posts/ 3-principles-for-designing-agent-skills...
$ cd ..
Engineering
February 15, 2026
3 Principles for Designing Agent Skills
How Block Engineering codified tribal knowledge for AI
$ git blame
Angie Jones
I lead AI Enablement for Engineering at Block.
$ cat content.md
Traditionally, engineers haven't been the most diligent at writing and maintaining docs. But it seems they're more inspired than ever lately.
Loading tweet...
AI agents have changed the game here. Not because they magically know your codebase or your team's processes; they don't. But because there's now a way to package that knowledge so agents can actually use it: Agent Skills .
This post shares how we think about designing good skills at Block.
What Are Agent Skills?
Skills are an open standard supported by most major AI coding tools: Claude Code, Goose, Cursor, Amp, GitHub Copilot, Gemini CLI, VS Code, and many more.
At their simplest, a skill is a folder with a SKILL.md file with a set of instructions that an agent can discover and load on demand. Think of it like a playbook. When an agent encounters a task that matches a skill's description, it loads those instructions and follows them. Skills can also include supporting files like scripts, templates, MCP servers, and configuration files.
The beauty is in the portability. Write a skill once, and it works for anyone across any agent that supports the format.
Codifying Tribal Knowledge: How We Use Skills at Block
At Block, we built an internal Skills marketplace with over 100 skills and counting, plus curated bundles that package related skills together for specific roles and teams (e.g. frontend , android , iOS , etc).
These skills are deeply specific to how we work:
A skill that knows how to investigate restaurant POS crash patterns specific to our hardware and software
A skill that walks through our exact process for setting up feature flag experiments
A skill that knows our oncall runbook and which dashboards to check, which logs to pull, how to escalate
A skill that enforces our internal API style guide when engineers are designing new services
This is tribal knowledge. The kind of stuff that used to live in one person's head, or in a doc that only three people knew existed. Now it's in a shared, version controlled repository where any Block engineer can install it and any agent can use it.
The key shift is documentation goes from something you read to something your agent can execute. A runbook becomes a workflow. A style guide becomes an enforcer. An onboarding guide becomes an interactive tutor.
And because skills are just files in a repo, they get the same treatment as code: pull requests, reviews, version history. When a process changes, you update the skill and everyone's agent gets the update.
Architecting a Good Skill
Skills are markdown files and executables. Creating them is fairly easy for engineers. Building skills that are actually good is where it gets interesting.
I'll walk through the principles using a skill I designed called Repo Readiness . It evaluates a repository's readiness for AI-assisted development by scoring it across several checks: Does the repo have agent context files? Are there AI workflows configured? Does the CI/CD pipeline incorporate AI tooling? Each check is pass/fail with a fixed point value, and the results roll up into an overall readiness score with a tier rating.
But these principles aren't specific to scoring skills. We've seen them hold up across our entire marketplace... oncall runbooks, commit workflows, code review tools, investigation skills, experiment setup guides. The pattern is the same regardless of what the skill does.
Here's how we think about designing them.
Principle 1: Know What the Agent Should NOT Decide
This might be the most important skill design principle, and it's counterintuitive: the first thing to figure out is what to take away from the agent.
For Repo Readiness, I needed the scoring to be consistent. If you run it on the same repo twice and there have been no changes to that repo, you should get the same score. That sounds obvious, but LLMs don't work that way. Ask an LLM to evaluate a repo and score it out of 100, you'll get different numbers every time. It might feel generous on one run and strict on the next. You can't trend scores over time, you can't compare across teams, and you can't trust the results.
So I moved all scoring into a standalone bash script. Every check is binary - pass or fail, with a fixed point value. No partial credit, no "almost there," no vibes.
bash
1 A3_PASS = false 2 A3_POINTS = 0 3 if [ ${ # A3_FOUND [ @ ] } -gt 0 ] ; then 4 A3_PASS = true 5 A3_POINTS = 20 6 fi
It doesn't matter if you have one AI workflow or fifty, you get the same 20 points. This is intentional. Partial credit would require qualitative judgment ("is three workflows enough?"), and the moment you introduce that, you've reintroduced inconsistency.
The skill's instructions explicitly tell the agent: "The script is the single source of truth for all scores. Never override, adjust, or recalculate any score from the script's output."
In Repo Readiness, the deterministic part is scoring. In other skills, it might be CLI commands, SQL queries, or naming conventions. Our Commit skill locks down the exact git commands to run. Our Experiment Setup skill prescribes the exact CLI invocations and flag naming format. Our Investigation skill hardcodes the SQL query structure so the agent can't improvise something wrong.
The principle is the same everywhere: if it needs to be consistent across runs and across users, don't leave it to the model. Put it in a script, a template, or a hard rule.
Principle 2: Know What the Agent SHOULD Decide
Just as important, what should the agent reason about? If you lock down everything, you've just built an expensive CLI tool with extra steps.
For Repo Readiness, the agent handles:
Interpretation — "Why did I fail the agent context check?" The agent reads the results, understands what agent context files are, and explains it in plain language for that specific user.
Action — "Can you look at my repo and suggest content for an AGENTS.md?" Now the agent reads the actual codebase, understands its structure, and generates a tailored file. No script can do that without an LLM.
Conversation — "What should I prioritize first?" The agent considers the point values, the team's constraints, and gives a recommendation.
Basically, if the task requires understanding context, generating novel content, or having a conversation, that's the agent's job.
This gives you a clean two-zone architecture:
Zone Owner Why
Rules and execution Scripts, templates, hard rules Same input, same output — every time
Interpretation and action The agent Every repo is different; every conversation is different
Play to each system's strengths.
This pattern shows up across all kinds of skills. Our Oncall skill runs a deterministic health check script, but leaves triage and diagnosis to the agent. The Investigation skill hardcodes the SQL query, but the agent interprets the results and decides what to do next. Our Code Review skill locks down the output format and independence rules, but leaves conflict resolution and judgment calls to the agent.
The split looks different for every skill, but the question is always the same: what needs to be consistent, and what needs to be smart?
Principle 3: Write a Constitution, Not a Suggestion
LLMs are people pleasers by nature. They want to be helpful, they want to soften bad news, they want to add caveats. "You scored 30 out of 100, but you're really close on a few checks!" That's nice, but it undermines the whole point of deterministic scoring.
The SKILL.md for Repo Readiness includes explicit rules:
Never override, adjust, or recalculate any score from the script
Never add or remove checks from the report
If the script says a check failed, show it as is
The specific formatting template to follow exactly, not approximately
This is defensive design against the agent's helpfulness. The more specific your SKILL.md , the less the agent has to guess, and the more consistent the experience is for every user who triggers that skill.
This is the most universal of the three principles. Every skill we looked at across our marketplace benefits from constitutional constraints. Without these constraints, agents will find creative ways to be "helpful" that break your workflow. They'll skip steps they think are unnecessary. They'll soften results they think are too harsh. They'll take actions they think you'd want without asking. Constitutional rules are how you channel that helpfulness into something reliable.
Think of the SKILL.md as a contract, not a suggestion. Be precise about the exact steps it should take and how to handle edge cases. Leave room for the agent to reason where reasoning adds value. Lock it down everywhere else.
Bonus: Design for the Arc
The three principles above apply to every skill. This one doesn't, but when it fits, it's the difference between a tool engineers use once and a tool they reach for every week.
The best skills aren't one shot tools. They create a conversation arc.
Here's what that looks like with Repo Readiness. I could have built it as a pure bash tool. It already produces a nicely structured JSON report. I could format that in the terminal with colors and tables and call it a day. But that would mean the workflow stops at the score.
As a skill, the script's output becomes the agent's input. The moment the agent shows you your score, it already has full context: what repo it analyzed, what checks passed and failed, what the specific recommendations are, and access to the repo's actual code.
So when the report says "0 out of 15 on Agent Context — no AGENTS.md found," you don't have to open a browser, Google what that means, read some docs, then come back and write one yourself. You just say:
"What's an AGENTS.md? Why do I need that?"
And then:
"Can you review my repo and take a first pass at drafting one?"
And the agent does it right there in the same session with full context. With their helpful nature, they'll likely even offer it up as a suggestion before you even ask.
Then after collaborating with the agent, you can say "run the check again" and see your score improve in real time.
A script gives you a diagnosis. A skill gives you a diagnosis and a doctor who can treat you on the spot.
That being said, not every skill naturally creates this arc. A Commit skill is mostly one and done. But diagnostic skills, investigation tools, code review workflows, basically anything where results lead to action... these are the ones where designing for the arc pays off. When you're building a skill like that, ask yourself: what will the user want to do after they see the first result? Then make sure the agent has what it needs to help with that too.
Skills aren't complicated. They're markdown files with instructions. But designing them well requires thinking about what should be deterministic versus what should be left for the agent to figure out, how specific your instructions need to be to get consistent results, and what the output enables in terms of next steps.
The principles:
Know what the agent should NOT decide : If it needs to be reproducible, put it in a script
Know what the agent SHOULD decide : Explanation, creation, and conversation are the agent's strengths
Write a constitution : Be explicit about constraints; the agent will thank you by being consistent
Bonus: Design for the arc : The best skills turn output into input, making the agent more useful for whatever comes next
If your team has runbooks, processes, style guides, or any other knowledge that people keep having to re-explain, that's a skill waiting to be written. We're still early, but with 100+ skills, the pattern is clear: the teams that codify their knowledge into skills are the ones whose agents actually work.
$ cat tags
AI
$
```
