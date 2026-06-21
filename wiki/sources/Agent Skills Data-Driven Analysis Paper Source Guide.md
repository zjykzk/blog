---
title: >-
  Agent Skills Data-Driven Analysis Paper Source Guide
category: sources
type: source
status: draft
tags:
  - paper
  - arxiv
  - agents
  - skills
  - software-engineering
aliases:
  - Agent Skills: A Data-Driven Analysis of Claude Skills for Extending Large Language Model Functionality
  - arXiv:2602.08004
sources:
  - https://arxiv.org/abs/2602.08004v1
  - https://arxiv.org/pdf/2602.08004v1
  - conversation:2026-05-12
created: 2026-05-12T11:05:11+08:00
updated: 2026-05-12T11:05:11+08:00
summary: >-
  Direct paper guide for a 40,285-skill marketplace measurement study covering growth bursts, length, redundancy, functional demand, and safety risks in Claude-style agent skills.
provenance:
  extracted: 0.91
  inferred: 0.07
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-05-12
---
# Agent Skills Data-Driven Analysis Paper Source Guide

> Source: Agent Skills: A Data-Driven Analysis of Claude Skills for Extending Large Language Model Functionality, arXiv:2602.08004v1, submitted 2026-02-08.

## Capture Policy

This page preserves the source-level structure of the arXiv paper itself. It should be used for paper-grounded claims about the public agent-skill marketplace snapshot, especially quantitative claims about growth, length, redundancy, category supply/demand, and safety-risk distribution.

This page complements [[wiki/concepts/Agent Skill]], [[wiki/topics/AI Skills Workflow]], [[wiki/sources/Claude Code Skills Source Guide]], [[wiki/sources/Skills-Coach Paper Source Guide]], and [[wiki/sources/SkillOS Paper Source Guide]]. Those pages focus on skill definition, workflow design, skill optimization, or repository-level curation; this paper contributes an ecosystem measurement layer.

## What It Covers

The paper studies publicly listed Claude-style agent skills as an emerging infrastructure layer for LLM agents. It asks what kinds of skills exist, how users adopt them, how much redundancy the ecosystem contains, whether skill length fits prompt budgets, and what safety risks appear when skills package reusable procedures and tool interactions.

The empirical base is a crawl of 40,285 publicly listed skills from `skills.sh`, finalized on 2026-02-05. For each skill, the authors collect metadata such as skill name, repository, first-seen date, and per-platform install counts. The paper then combines descriptive statistics, LLM-based classification, embedding/name-based redundancy analysis, and LLM-based risk auditing.

The paper's central thesis is not that skills are merely prompt snippets. It treats skills as reusable, program-like modules that can define triggering conditions, procedural logic, resources, and tool interactions. At ecosystem scale, this makes skills a measurable layer of agent capability distribution, reuse, and risk.

## Preserved Content

### Abstract-Level Claim

Agent skills extend LLM agents with reusable modules that specify when a skill should be used and how a subtask should be carried out. As public skill marketplaces grow, their contents, adoption patterns, and risks become important empirical questions.

The paper reports five main findings:

1. Skill publication grows rapidly and in bursts that track shifts in community attention.
2. Skill content is highly concentrated in software-engineering workflows.
3. Information retrieval and content creation receive substantial adoption relative to their supply.
4. Skill length is heavy-tailed, but most skills remain within typical prompt budgets.
5. The ecosystem is homogeneous and redundant, while a non-trivial share of skills enables state-changing or system-level actions.

### 1. Introduction: Why Skills Need Ecosystem Measurement

LLM agents increasingly handle complex multi-step tasks by reasoning, using tools, and interacting with external environments. As agents scale, they repeatedly encounter recurring behaviors: data retrieval, information extraction, code modification, environment setup, document editing, and workflow automation.

Without explicit skill abstractions, these recurring behaviors are repeatedly specified through prompts or ad hoc control logic. This increases prompt overhead, makes behavior brittle under context changes, and complicates maintenance of shared procedures.

The paper defines an agent skill as a reusable, plug-and-play module that specifies both applicability and execution. In practical implementations, a skill combines:

- lightweight metadata for discovery and selection;
- executable or procedural instructions;
- supporting resources such as files, scripts, and tool configurations.

A common runtime pattern is progressive disclosure: the agent first sees a compact skill index with names and descriptions, then loads the full skill specification only after selecting a relevant skill. This connects directly to [[wiki/topics/Tool Routing]] and [[wiki/topics/Context Management]] because skill metadata becomes a routing surface and full skill bodies become conditional context.

### 2. Skill Data and Growth Trends

#### Dataset Construction

The dataset is built by crawling agent skills listed on `skills.sh`. Each record includes:

```json
{
  "name": "[SKILL NAME]",
  "repository": "[REPOSITORY LINK]",
  "first_seen": "[DD/MM/YY]",
  "installed_on": [
    {"platform": "claude-code", "installs": "[NUMBER OF INSTALL]"},
    {"platform": "codex", "installs": "[NUMBER OF INSTALL]"}
  ]
}
```

The final snapshot contains 40,285 skill metadata records. The authors state that measurements use publicly accessible content and report aggregate results rather than sensitive attributions about individual creators.

#### Rapid and Bursty Growth

The marketplace grows from 2,179 skills on 2026-01-16 to 40,285 skills on 2026-02-05. That is a net increase of 38,106 skills in 20 days, or about 18.5x growth.

The average inflow is 1,918 skills per day, but arrivals are not smooth. The largest spike occurs on 2026-01-25, when 8,857 skills are added in a single day. That one day accounts for 23.2% of all new skills in the measurement window. The week centered on 2026-01-25 contributes 19,259 skills, or 47.8% of the full snapshot.

#### Growth Aligns With OpenClaw Attention

The paper tracks OpenClaw GitHub stars as a parallel signal of community attention. Daily new stars rise from hundreds in mid-January to 10,543 on 2026-01-25 and peak at 25,432 on 2026-01-26. The synchronized marketplace and GitHub-star spikes suggest a shared attention wave.

GitHub stars are only an imperfect usage proxy, but the paper treats the synchronization as evidence that rapid skill publication coincides with broader community interest in skill-based tooling.

### 3. Skill Length and Redundancy

#### Length Measurement

The authors tokenize each `SKILL.md` with `tiktoken` using the `o200k_base` encoding. Token count is used as a proxy for prompt budget and inference cost.

The distribution is heavy-tailed but centrally compact:

- median: 1,414 tokens;
- mean: 1,895 tokens;
- 80% are within 2,955 tokens;
- 90% are within 3,935 tokens;
- 95% are within 5,077 tokens;
- 99% are within 9,253 tokens;
- maximum: 116,239 tokens.

The paper's interpretation is that most skills can be loaded directly into context, but the top tail behaves more like libraries. Very long skills often include multiple components, extended documentation, large code blocks, or template collections. Such skills may benefit from modularization or retrieval-based partial loading.

This finding is important for [[wiki/topics/AI Skills Workflow]] because it suggests a practical split between ordinary prompt-sized skills and library-like skill bundles that require progressive or selective disclosure.

#### Intent-Level Redundancy

The paper measures redundancy with two signals:

1. exact name-based matching after lowercasing and removing special characters;
2. semantic matching by embedding `Name:[NAME] + Description:[DESCRIPTION]` with `BAAI/bge-m3` and inspecting nearest neighbors plus t-SNE.

Because marketplace descriptions are often short, noisy, and template-derived, the paper uses strict name matching for main quantitative results and treats embeddings as a complementary view.

The name-based result is that 53.7% of skills appear once, while 46.3% share a normalized name with at least one other listing. Duplication is concentrated:

- 2x groups contribute 18.7% of the corpus;
- 5x to 9x groups contribute 14.3%;
- 10x to 49x groups contribute 8.8%;
- a small number of names appear more than 100 times.

The paper interprets this as evidence of repeated reposting, template-driven publication, and superficial repackaging. High redundancy increases search costs, fragments adoption signals, and makes it harder for high-quality implementations to become defaults.

### 4. Skill Usage Patterns: Taxonomy, Supply, and Demand

#### Functional Taxonomy

The paper defines a two-level taxonomy with 6 major categories and 20 sub-categories. Marketplace tags are sparse and inconsistent, so the authors use Qwen2.5-32B-Instruct to assign each skill to exactly one sub-category from name and description.

The six major categories are:

1. Software Engineering
2. Information Retrieval
3. Productivity Tools
4. Data & Analytics
5. Content Creation
6. Utilities & Other

The sub-category table reports size, corpus percentage, average tokens, and average downloads/installs. Key entries include:

| Major Category | Sub-Category | # Skills | % of Total | Avg Tokens | Avg Downloads |
|---|---:|---:|---:|---:|---:|
| Software Engineering | Code Generation | 5,743 | 14.3% | 2004 | 235 |
| Software Engineering | Debug & Analysis | 5,319 | 13.2% | 1772 | 103 |
| Software Engineering | Version Control | 1,275 | 3.2% | 1403 | 71 |
| Software Engineering | Infrastructure | 9,664 | 24.0% | 1995 | 114 |
| Information Retrieval | Web Search | 567 | 1.4% | 1517 | 1268 |
| Information Retrieval | Academic Search | 1,083 | 2.7% | 2100 | 73 |
| Information Retrieval | Live Data Streams | 277 | 0.7% | 1514 | 48 |
| Productivity Tools | Team Communication | 698 | 1.7% | 1458 | 196 |
| Productivity Tools | Document Systems | 1,579 | 3.9% | 1981 | 125 |
| Productivity Tools | Task Management | 2,275 | 5.6% | 1656 | 106 |
| Data & Analytics | Data Processing | 3,179 | 7.9% | 2134 | 93 |
| Data & Analytics | Math & Calculation | 368 | 0.9% | 2028 | 147 |
| Data & Analytics | Data Visualization | 736 | 1.8% | 2322 | 108 |
| Content Creation | Image Generation | 1,201 | 3.0% | 2145 | 214 |
| Content Creation | Text Generation | 2,212 | 5.5% | 1977 | 178 |
| Content Creation | Audio & Video | 1,466 | 3.6% | 1744 | 266 |
| Utilities & Other | Local File Control | 255 | 0.6% | 1420 | 42 |
| Utilities & Other | Command Execution | 337 | 0.8% | 1541 | 70 |
| Utilities & Other | Memory & Cognition | 929 | 2.3% | 1475 | 54 |
| Utilities & Other | Other Utilities | 1,125 | 2.8% | 1684 | 135 |

#### Software Engineering Dominates Supply

Software Engineering accounts for 54.7% of the corpus. Infrastructure is the single largest sub-category with 9,664 skills, or 24.0% of all listings. The paper interprets this as evidence that developers frequently publish skills for environment setup, DevOps automation, tool configuration, and deployment.

This reinforces [[wiki/concepts/Agentic Engineering]]: AI coding work is not only about generating code but also about encoding repository routines, environment procedures, and operational checks into reusable agent-facing structures.

#### Adoption Concentrates Differently Than Publication

Adoption does not mirror supply. Web Search has the highest mean downloads at 1,268 while representing only 1.4% of listings. Content creation also has high mean installs: Audio & Video at 266 and Image Generation at 214. Code Generation remains highly adopted at 235.

Utility-focused skills show lower mean installs: Local File Control at 42 and Memory & Cognition at 54. The paper suggests this may reflect narrower use cases, higher perceived risk, or overlap with built-in agent capabilities.

#### Supply-Demand Gaps

After de-duplicating skills, the paper compares supply as number of de-duplicated skills and demand as average installs per skill.

It identifies three systematic gaps:

1. Content creation is demand-heavy: writing and media workflows are repeatedly reused even when listings are modest.
2. Software engineering is supply-heavy: coding, testing, and repository routines are easy to publish, so overlap is high and installs spread across close substitutes.
3. Information retrieval is demand-heavy despite limited supply: reliable retrieval connectors are widely useful but costly to build and maintain because they need stable connectors, query design, and adaptation to external rate limits and interface changes.

This is one of the paper's most useful ecosystem-level findings: the hardest skills to maintain may be the ones users reuse most, while the easiest skills to publish may create redundant supply.

### 5. Risk and Safety Assessment

#### Risk Auditing Protocol

The paper audits each skill with Qwen2.5-32B-Instruct. The model receives skill name, description, and full `SKILL.md` content, then assigns exactly one risk level under a worst-case interpretation:

- L0: safe, read-only public operations;
- L1: privacy risk, read-sensitive operations;
- L2: moderate risk, restricted write/action;
- L3: critical risk, high-impact or destructive operations such as arbitrary command execution, credential handling, authentication changes, financial operations, or irreversible deletion.

The required output is strict JSON:

```json
{"skill_name": "{{SKILL_NAME}}", "risk_level": "L0|L1|L2|L3", "reasoning": "..."}
```

#### Overall Risk Distribution

The paper reports:

- 54% L0;
- 5% L1;
- 30% L2;
- 9% L3.

The paper's interpretation is that low-risk skills dominate, but nearly two-fifths of the marketplace can access sensitive context or perform writes/actions, and a nontrivial share exposes critical capabilities.

#### Category-Level Risk Patterns

Risk concentrates where skills connect the model to external systems:

- Content Creation is safest: 75% L0 and only a small L3 share.
- Information Retrieval is mostly read-oriented: 68% L0, but it has the largest L1 share at 11%, often because connectors use private tokens or private sources.
- Productivity Tools are dominated by L2 at 46%, reflecting email, messaging, calendar, and document actions.
- Software Engineering has the highest L3 fraction at 14%, consistent with repository manipulation, command execution, environment management, and system configuration.
- Utilities & Other has elevated L1 at 10% and L3 at 11%, driven by local file operations and command execution utilities.
- Data & Analytics sits between the extremes, with 59% L0 and 23% L2, consistent with ETL-style pipelines that may write intermediate outputs.

The paper's core safety conclusion is that the most severe cases are less about generating content and more about enabling external side effects.

### 6. Potential Directions

The paper proposes four directions for the agent-skill ecosystem.

#### Reduce Redundancy and Improve Quality Signals

Rapid community contribution creates volume, but long-term value depends on high-quality, non-redundant skills. Future platforms should pair semantic de-duplication with quality signals such as documentation, execution reliability, maintenance, and usage.

The practical target is convergence toward a small set of canonical skills per intent, so developers extend capabilities instead of repackaging the same workflows.

#### Modularize and Selectively Load Long Skills

Because length is heavy-tailed, a small fraction of skills can dominate prompt budgets. Systems should support selective loading, modularization, retrieval of relevant steps, pruning of unused branches, and instruction compression.

This supports the broader [[wiki/topics/Context Management]] principle that reusable knowledge should be exposed in stages rather than dumped into every context window.

#### Use Demand Signals to Guide Skill Authoring

Supply-demand gaps show that publication effort does not always track adoption. Information retrieval attracts high usage but is costly to build and maintain, while many software engineering skills compete as close substitutes.

Future platforms can use demand signals to guide authoring tools, incentives, review effort, and demand-driven synthesis of existing skills into new domains or connectors.

#### Add Proactive Security Protocols

The paper argues for standardized sandboxing and least-privilege protocols because many skills enable state-changing actions. Fine-grained control over reads, writes, command execution, and system-level operations is treated as a necessary condition for safe skill ecosystems.

### 7. Conclusion

The paper positions agent skills as a measurable infrastructure layer for LLM agents. Across 40,285 public skills, the ecosystem is expanding quickly but unevenly: software engineering dominates supply, redundancy is pervasive, adoption concentrates around information retrieval and content creation, and a nontrivial subset of skills enables state-changing or system-level actions.

The durable contribution is an ecosystem-level measurement frame. Instead of asking only whether an individual skill works, the paper asks whether the marketplace as a whole has discoverability, diversity, adoption alignment, prompt-budget discipline, and safety governance.

### Appendix Material Preserved

#### Skill Structure and Integration

The appendix formalizes skills as:

```text
Skill = {Metadata, Instructions, Resources}
```

Metadata specifies applicability conditions. Instructions define procedural steps. Resources link to tools, scripts, APIs, or auxiliary artifacts.

The appendix emphasizes that `SKILL.md` frontmatter supports lightweight discovery, while Markdown body content supports procedural execution after selection. This is the same progressive-disclosure pattern already visible in [[wiki/concepts/Agent Skill]].

The integration model is dynamic rather than a fixed workflow graph. At session start, the agent sees a summarized skill index. Given a request, it reasons about the goal, decomposes it into subgoals, selects a skill, executes the skill, incorporates intermediate outputs into state, and may then choose further skills. Skill transitions are determined by intermediate state updates, not hard-coded orchestration rules.

#### Skill Classification Prompt

The classification prompt asks an expert AI Agent Skill Classifier to map each skill into one of the 6 major categories and 20 sub-categories. It requires exactly one sub-category and strict JSON output with major category id/name, sub-category id/name, and reasoning.

This prompt is source-level evidence for how the taxonomy labels were produced. It should not be treated as a universally validated taxonomy without external replication. ^[ambiguous]

#### Skill Security Audit Prompt

The security-audit prompt asks an LLM to classify each skill into L0-L3 based on what operations it enables, whether it reads or writes data, whether it executes code or commands, whether the data is public or private, and whether dangerous patterns such as `exec`, `eval`, `subprocess`, shell commands, SQL queries, file deletion, API keys, or authentication tokens are present.

The prompt explicitly adopts a worst-case scenario mindset. This makes the risk estimates conservative relative to benign usage, but useful for identifying categories that require least-privilege controls. ^[inferred]

#### High-Risk Examples

The appendix includes representative L3 examples across multiple major categories. The paper redacts identifying skill names and highlights risk-related keywords. Typical L3 patterns include arbitrary command execution, credential handling, privileged access, irreversible deletion, and financial operations.

## Integration Decisions

This page should remain source-level because it is a single empirical snapshot from one public marketplace. Its numerical claims should be cited as measurements of that snapshot, not as timeless laws about all agent skill ecosystems.

The most promotable durable idea is skill ecosystem governance: once skills become a public capability distribution layer, the important questions include redundancy, canonicalization, supply-demand alignment, prompt-budget discipline, and least-privilege safety review. That idea may later become a synthesis page if connected with [[wiki/sources/Skills-Coach Paper Source Guide]], [[wiki/sources/SkillOS Paper Source Guide]], and [[wiki/sources/ADK Skill Design Patterns Source Guide]]. ^[inferred]

Connections to existing pages:

- [[wiki/concepts/Agent Skill]]: the paper gives large-scale empirical evidence for what public skills look like and how they are represented.
- [[wiki/topics/AI Skills Workflow]]: the paper shows that skill workflows are not only local authoring practices but also marketplace-level reuse and maintenance problems.
- [[wiki/topics/Tool Routing]]: the skill name and description fields operate as routing surfaces for selection.
- [[wiki/topics/Context Management]]: the length distribution clarifies when skills fit context directly and when modular loading is necessary.
- [[wiki/concepts/Agentic Engineering]]: the dominance of software-engineering skills shows that agentic engineering knowledge is quickly being encoded as reusable procedures.
- [[wiki/concepts/Verification Loop]]: the paper's risk and classification audits are examples of ecosystem-level evaluators, though they are LLM-judge based and should be interpreted carefully.

## Open Questions

- How stable are the reported supply-demand patterns after community attention shifts away from the initial burst?
- How much public marketplace behavior reflects real production use rather than novelty, social promotion, or template publishing?
- Can platform-level canonicalization reduce redundancy without suppressing useful variants?
- How should skills with L2/L3 capabilities declare permissions, required sandboxing, and human confirmation scopes?
- Are LLM-based taxonomy and risk labels reliable enough for governance, or should they be paired with static analysis and execution traces? ^[inferred]
- What happens when skill ecosystems move from single-file Markdown skills to multi-file skills with scripts, resources, and privileged integrations?

## Related

- [[wiki/maps/AI Map]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/Tool Routing]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Agentic Engineering]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/sources/Claude Code Skills Source Guide]]
- [[wiki/sources/ADK Skill Design Patterns Source Guide]]
- [[wiki/sources/Skills-Coach Paper Source Guide]]
- [[wiki/sources/SkillOS Paper Source Guide]]
