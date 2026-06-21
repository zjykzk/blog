---
title: >-
  SkillOS Source Guide
category: sources
type: source
status: draft
tags:
  - article
  - agents
  - skills
  - memory
  - training
aliases:
  - SkillOS
  - Google's SkillOS paper
  - Experiences to Memories to Skills
sources:
  - https://x.com/neural_avb/article/2053873358853591435
  - https://arxiv.org/abs/2605.06614
  - conversation:2026-05-12
created: 2026-05-12T10:35:38+08:00
updated: 2026-05-12T10:35:38+08:00
summary: >-
  Source guide for AVB's SkillOS article: experiences become reusable skills through a trainable curator, grouped task rollouts, and delayed RL rewards.
provenance:
  extracted: 0.86
  inferred: 0.12
  ambiguous: 0.02
base_confidence: 0.44
lifecycle: draft
lifecycle_changed: 2026-05-12
---
# SkillOS Source Guide

> Source: https://x.com/neural_avb/article/2053873358853591435

## Capture Policy

This page preserves the source-level structure of AVB's article about Google's SkillOS paper. It keeps the article's operational model, training loop, reward design, and result claims as source material rather than promoting them directly into a stable general theory.

## What It Covers

SkillOS is presented as a framework for making LLM agents evolve by turning task execution experiences into reusable skill files. Its central move is to separate a frozen task-solving executor from a trainable skill curator: the executor uses a persistent SkillRepo, while the curator observes trajectories and edits that repository.

The article belongs in the AI / Agent skills cluster because it extends [[wiki/concepts/Skill Self-Evolution]] from evaluation-driven improvement of individual skills toward repository-level learning: experiences become memory-like artifacts, and memory is operationalized as structured Markdown skills that future agents can retrieve.

## Preserved Content

### Core Claim: Experiences Become Memories Become Skills

The source frames SkillOS as an operating-system-like layer for agent skill management. The SkillRepo is treated as persistent memory, but the memory is not an opaque vector store or unstructured trace log. It is a file repository of reusable skills.

The compressed slogan is:

```text
Experiences -> Memories -> Skills
```

This makes the paper relevant to both [[wiki/topics/AI Memory]] and [[wiki/topics/AI Skills Workflow]]: memory becomes useful to the executor only after it is distilled into an actionable artifact that can be retrieved and applied.

### Three Main Components

#### Agent Executor

The Agent Executor is a frozen actor LLM. It retrieves skills from the SkillRepo and uses them while solving tasks. Its weights are not updated during training. Performance improvement comes from better skill availability rather than model-weight adaptation.

The article explicitly says there is no central contribution in the executor itself: it behaves like an ordinary harnessed agent that receives available skill headers, chooses relevant skills, reads their full content, and acts in the environment.

#### Skill Curator

The Skill Curator is a trainable LLM that observes executor trajectories and decides how to update the SkillRepo. It can insert, update, or delete skills. The curator is the paper's main locus of learning.

The curator's role is quoted as converting past experiences of agent task execution into reusable, general skills so they can benefit and inspire future tasks.

#### SkillRepo

The SkillRepo stores skills as structured Markdown files. Each skill includes a name, description, content, and potentially code snippets or usage guidelines in the article's description. The retrieval mechanism depends heavily on the YAML description because BM25 keyword matching uses descriptions to find relevant skills.

The source notes that Google's SkillOS work focuses on text/prose portions of skills. Anthropic's broader skill architecture also includes resource files and executable code, but SkillOS does not primarily learn those in this paper.

### Skill Format

The source presents skills as lazily loaded prompts stored in files. A minimal skill contains YAML frontmatter and a Markdown body:

```markdown
---
name: frontend-design
description: techniques and instructions to write good UI code
---

instructions: <an essay about frontend patterns>
```

In a harness such as Claude Code or Codex, the agent sees a list of available skill headers in the system prompt. When a task matches a skill, the agent reads the full skill file and loads its instructions into context.

SkillOS targets the skill creation and maintenance phase: generating clear, actionable instructions that improve future agent performance.

### Stage 1: Executor Runs

Before any new skill is created, the frozen executor attempts a task.

The execution stage has four source-described steps:

1. Retrieve the top-k relevant existing skills from the SkillRepo using BM25 keyword matching over YAML descriptions.
2. Run a multi-step interaction with the environment.
3. Produce a trajectory: a sequence of observations and actions.
4. Use a separate LLM-as-a-judge, described as Qwen3-32B, to determine whether the task was completed successfully.

The trajectory, correctness signal, and previously retrieved skills are then handed to the curator.

### Stage 2: Curator Input

The curator receives a structured prompt containing:

- Task description: what the agent was trying to accomplish.
- Past skills: names and contents of previously retrieved relevant skills.
- Agent trajectory: the full step-by-step trace of what happened.
- Result: whether the executor succeeded or failed.

This input structure is important because it makes curation trace-grounded. The curator is not supposed to invent generic advice detached from observed behavior.

### Stage 3: Curator Output

The curator emits structured function calls in a ReAct-style loop.

#### `new_skill_insert`

Creates a new skill when a trajectory reveals a generalizable strategy that is not yet represented in the SkillRepo. This is especially useful early in training when the repository is empty.

Inputs include:

- `skill_name`
- `content`

#### `skill_update`

Modifies an existing skill. This is used when an existing skill should be refined, renamed, or rewritten.

Inputs include:

- `skill_name`
- `new_name`
- `new_content`

The exact skill name must match the existing repository entry.

#### `skill_delete`

Removes an existing skill by name. The article frames deletion as useful when a skill is redundant, misleading, or superseded.

### Skill Writing Rules

The curator is instructed to follow several rules:

- No specifics: remove specific numbers and names, replacing them with variables or concepts when generalization is needed.
- No hallucination: include only facts supported by the trajectory.
- Atomic and modular: each skill should be self-contained and reusable in isolation.
- Actionable: the body should provide concrete guidance, not vague advice.

These rules make SkillOS a compression-and-generalization system rather than a raw trace archive.

### The Hard RL Problem

The article highlights the technical challenge of delayed feedback in curation. A curator's decision may only reveal its value through later tasks that use the curated skill.

The source states the challenge as indirect and delayed feedback: curation decisions are evaluated through future relevant task performance, not immediate reward.

This differs from standard RL settings where an action's effect is usually observable quickly. In SkillOS, a bad skill created at task `t` may not reveal itself until a later task fails because the executor retrieved and followed it.

### Phase 1: Grouped Training Instance Construction

The most important training design is grouped task construction. The dataset is preprocessed into groups of related tasks so that skills curated from early tasks can be tested on later tasks in the same group.

The article describes two preprocessing stages:

1. Latent Attribute Annotation: Gemini-2.5-Pro annotates tasks by type.
2. Group Construction: annotated tasks are grouped, with difficulty ranking creating a natural curriculum inside each group.

Reported group sizes:

- ALFWorld and WebShop: group size 10.
- Reasoning tasks such as Math and GPQA: random group size between 5 and 12.

The article identifies task grouping as the core mechanism that turns delayed curation effects into a trainable signal.

### Phase 2: Skill Creation Loop

For each training step, SkillOS samples a task group, initializes an empty SkillRepo, and then runs the executor-curator loop across the group.

The loop is:

1. Executor retrieves top-5 skills using BM25.
2. Executor attempts the task and produces a trajectory.
3. Judge emits a correctness signal.
4. Curator reads the trajectory and updates the SkillRepo.
5. Later tasks in the same group test whether earlier curation helped.

This makes the SkillRepo itself part of the evolving state of a rollout.

### Phase 3: Composite Reward

After a full group rollout, SkillOS computes a composite reward with four components.

#### Task Outcome Reward

This is the main downstream signal: did skills curated from earlier tasks help later tasks succeed?

The first task begins with an empty SkillRepo, so its performance cannot be credited to prior curation. Later task outcomes become evidence about whether earlier skill insertions, updates, or deletions were useful.

#### Function Call Reward

This measures the fraction of generated function calls that are syntactically valid and successfully execute against the SkillRepo.

It prevents the curator from producing malformed JSON, updating nonexistent skills, or otherwise failing at the repository operation layer.

#### Compression Reward

This penalizes verbatim trajectory copying and rewards genuine distilled knowledge. Without compression pressure, the curator could learn to dump raw traces into the repository.

The compression reward is structurally important because SkillOS treats skills as reusable memory, not as an ever-growing log.

#### Content Quality Reward

Qwen3-32B acts as a judge over the curated skills, scoring whether they are:

- semantically meaningful;
- likely useful for future tasks;
- faithful;
- actionable.

This gives a denser intermediate signal independent of actual downstream task success.

### Phase 4: GRPO Policy Optimization

The curator is trained with GRPO. For each task group, SkillOS samples eight independent rollouts. Each rollout runs through the whole task group from start to finish and produces a different evolving SkillRepo because the curator samples different curation decisions.

GRPO compares relative rewards across the eight rollouts. Higher-reward curation sequences receive positive advantage and are reinforced; lower-reward sequences are suppressed.

The article notes that the KL divergence penalty is discarded from the standard GRPO formulation to encourage policy exploration during skill curation learning.

### Rollout Meaning in SkillOS

In ordinary RL, a rollout is one complete run through a task or sequence. In SkillOS, the rollout unit is the entire related task group.

Each independent rollout over the same task group can produce a different SkillRepo evolution:

```text
Rollout 1: curator decisions c1, c2, ... -> SkillRepo evolves one way
Rollout 2: different curator decisions -> SkillRepo evolves another way
...
Rollout 8: another repository trajectory
```

The training signal attaches not just to one answer, but to the repository path created by the curator across tasks.

### Reported Results

The article reports three high-level result claims.

#### SkillOS Beats Baselines

SkillOS is reported to outperform memory-free baselines and strong memory-based baselines such as ReasoningBank and MemP across multi-turn agentic tasks like ALFWorld and WebShop, and single-turn reasoning tasks such as AIME math.

This remains a source-level claim until checked against the paper's benchmark tables and evaluation details. ^[ambiguous]

#### Curator Generalizes to Unseen Executors

The curator is trained with Qwen3-8B as executor, but is reported to work at test time with different executors:

- Qwen3-8B
- Qwen3-32B
- Gemini-2.5-Pro

The article emphasizes that using Gemini-2.5-Pro directly as the curator underperforms the trained SkillOS curator, especially for weaker executors. The implied interpretation is that stronger raw reasoning is not enough; curation quality depends on learning what is useful for actual executor capacity. ^[inferred]

#### Reward Components Matter

The article reports ablation numbers:

- Full SkillOS: 61.2
- without content-quality reward: 58.6
- without compression reward: 60.0
- without task grouping: 57.3

The largest drop comes from removing task grouping, supporting the article's claim that related sequential tasks are the core training structure.

## Integration Decisions

SkillOS should remain a source guide for now because the capture is based on an explanatory article, not a direct full paper reading. The arXiv paper should be ingested separately if the exact equations, benchmark tables, prompts, and ablations need to become source-grounded wiki claims.

The most promotable concept is not simply "SkillOS" as a brand name, but repository-level skill curation: a trainable agent transforms trajectories into compact, actionable, retrievable skills under delayed downstream reward. That concept can later extend [[wiki/concepts/Skill Self-Evolution]] if the full paper confirms the mechanism.

Connections to existing pages:

- [[wiki/concepts/Agent Skill]]: SkillOS treats skills as Markdown files with descriptions, bodies, and retrieval affordances.
- [[wiki/topics/AI Skills Workflow]]: SkillOS automates the capture-maintain-reuse loop that manual skill workflows currently perform by review and editing.
- [[wiki/concepts/Skill Self-Evolution]]: SkillOS shifts from optimizing a skill against generated tasks to training a curator to manage an evolving repository.
- [[wiki/concepts/Continual Learning for AI Agents]]: SkillOS is harness/context-level learning, not model-weight learning in the executor.
- [[wiki/concepts/Verification Loop]]: LLM-as-judge and downstream task outcomes are the external feedback signals that make curation trainable.

## Open Questions

- How much of SkillOS's reported gain comes from skill retrieval quality versus skill content quality?
- Does BM25 over YAML descriptions remain sufficient as repositories become large and semantically overlapping?
- How should a human team review skill deletion and full replacement when skills encode shared operational knowledge?
- Can the same curator safely manage code-inclusive skills, or does executable skill evolution require stronger sandboxing and verification? ^[inferred]
- Does removing KL improve exploration without increasing unsafe or low-coherence repository edits outside benchmark settings? ^[ambiguous]

## Related

- [[wiki/maps/AI Map]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/AI Memory]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Skill Self-Evolution]]
- [[wiki/concepts/Continual Learning for AI Agents]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/sources/Skills-Coach Paper Source Guide]]
