---
title: >-
  SkillOS Paper Source Guide
category: sources
type: source
status: draft
tags:
  - paper
  - arxiv
  - agents
  - skills
  - training
aliases:
  - SkillOS paper
  - SkillOS: Learning Skill Curation for Self-Evolving Agents
  - arXiv:2605.06614
sources:
  - https://arxiv.org/abs/2605.06614
  - https://arxiv.org/html/2605.06614v1
  - conversation:2026-05-12
created: 2026-05-12T10:45:54+08:00
updated: 2026-05-12T10:45:54+08:00
summary: >-
  Direct paper guide for SkillOS, preserving its formal problem setting, grouped-task GRPO training recipe, benchmark results, analyses, limitations, and future directions.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-12
---
# SkillOS Paper Source Guide

> Source: SkillOS: Learning Skill Curation for Self-Evolving Agents, arXiv:2605.06614v1, submitted 2026-05-07.

## Capture Policy

This page preserves the source-level structure of the arXiv paper itself. It complements [[wiki/sources/SkillOS Source Guide]], which captured an explanatory article about the paper, by grounding the mechanism, equations, tables, appendix details, limitations, and future directions in the direct paper source.

## What It Covers

SkillOS studies how an LLM agent can improve across streaming tasks without retraining the task-solving executor. The paper treats reusable skills as procedural memory stored in Markdown files and makes skill curation the trainable component: a frozen executor retrieves and applies skills, while a learned curator inserts, updates, and deletes skills in an external SkillRepo.

The paper belongs in the [[wiki/topics/AI Skills Workflow]] and [[wiki/topics/AI Memory]] cluster because it reframes memory not as raw trajectories or opaque vector retrieval, but as a repository of actionable procedural files whose usefulness is evaluated by later related tasks.

## Preserved Content

### Abstract-Level Claim

LLM agents in streaming settings often act as one-off solvers. SkillOS argues that self-evolving agents need reusable skills distilled from past interactions, but that the bottleneck is high-quality skill curation. Existing approaches rely on manual curation, heuristic memory operations, or short-horizon skill adaptation, and therefore struggle with complex repository management under indirect delayed feedback.

SkillOS proposes an experience-driven RL training recipe. It pairs:

1. a frozen Agent Executor that retrieves and applies skills;
2. a trainable Skill Curator that updates an external SkillRepo from accumulated experience;
3. grouped task streams that make earlier curation decisions observable through later related tasks;
4. composite rewards that combine task outcomes, valid function calls, skill quality, and compression.

The reported outcome is that SkillOS improves effectiveness and efficiency across multi-turn agentic tasks and single-turn reasoning tasks, generalizes across executor backbones and task domains, and produces more structured Markdown skills over time.

### 1. Introduction: Why Skill Curation Is the Bottleneck

The paper starts from streaming deployment: tasks arrive sequentially, and an agent should not restart from scratch on each new task. Self-evolution requires accumulating, refining, and reusing experience.

The key memory substrate is procedural memory in the form of reusable skills. In a skill-based self-evolving loop, an agent selects relevant skills for a new task, uses them during execution, and updates its skill collection from the resulting trajectory. This makes skill curation the central bottleneck.

The paper distinguishes SkillOS from three weaker patterns:

- Manual skill repositories scale poorly because they require expert human curation.
- Prompted or heuristic memory operations lack downstream performance feedback and cannot adapt to the executor's actual needs.
- Existing RL work often teaches agents to use skills or optimizes short-horizon operations, which gives sparse evidence for update and deletion decisions.

SkillOS represents skills as Markdown files similar to Anthropic-style `SKILL.md` artifacts, but simplifies each skill to a single file with YAML frontmatter and Markdown instructions. The repository is manipulated through file-like operations, making the system resemble an operating-system layer over agent procedural memory.

### 2. Related Work: SkillOS in the Memory and RL Landscape

The paper positions SkillOS against two related literatures.

#### Memory for Self-Evolving Agents

One line stores experience in concrete forms such as raw trajectories or query-response pairs. These representations preserve detail but can be inefficient and less composable.

Another line abstracts experience into higher-level knowledge such as workflows, distilled insights, recurring patterns, or skills. Skills are agent-native because they are modular, customizable, editable, and orchestrable. SkillOS follows this direction, but treats the curation policy itself as a learned object.

#### RL for Memory and Skill Curation

Prior RL work includes long-context compaction, memory tool-call learning, memory retrieval policy training, and skill-use training. SkillOS's distinction is that it formulates skill curation as a long-horizon executor-grounded learning problem: the curator is rewarded for repository edits that later help the executor solve related tasks.

### 3. Methodology

#### 3.1 Streaming Skill Curation

The formal setting is a sequence of tasks:

```text
D = {x1, x2, ..., xT}
```

At timestamp `t`, the executor must solve the current task before seeing future tasks and produces a trajectory of observations and actions:

```text
ξt = {o1, a1, ..., on, an}
```

The system maintains an external skill repository `S_t`, a set of reusable skills at time `t`. Each skill is a Markdown file with:

- YAML frontmatter specifying the skill name and natural-language description of when to use it;
- Markdown instructions containing executable knowledge, workflows, constraints, and reusable heuristics.

The frozen executor retrieves a subset of skills with BM25 and samples actions conditioned on the task, current observation, and retrieved skills. The curator observes the trajectory, a correctness signal, and related skills, then emits structured curation operations:

```text
insert_skill
update_skill
delete_skill
```

Applying those operations transforms `S_t` into `S_{t+1}`, which is then available for later tasks. This creates a closed loop between execution and skill evolution.

#### 3.2 Learning Skill Curation with RL

SkillOS keeps the executor frozen and optimizes only the curator. The central difficulty is that curation decisions receive indirect delayed feedback: a skill written now may only prove useful or harmful on later tasks.

The paper addresses this with two designs:

1. grouped training instances, where related tasks are solved sequentially so early skills can affect later outcomes;
2. composite reward, where downstream task outcome is supplemented by operation validity, content quality, and compression signals.

##### Training Instance Construction

Each training instance is a group of related tasks. For reasoning tasks, the paper annotates each task with skill-relevant attributes using Gemini-2.5-Pro. Attributes include topic, required skills, concepts/theorems, heuristic strategies, and common pitfalls. Tasks are then grouped by phrase-level semantic similarity and difficulty progression.

For multi-turn agentic tasks, the paper uses default task-type annotations. ALFWorld and WebShop use group size 10; reasoning tasks use random group size between 5 and 12.

The important structural idea is that task grouping creates a local stream where a skill extracted from task `i` has a plausible chance to help task `i+1 ... n`. This turns delayed repository-level effects into a trainable signal.

##### Training Loop

For each training step:

1. sample a related task group;
2. initialize an empty SkillRepo;
3. for each task in the group, retrieve top-k skills with BM25;
4. run the frozen executor;
5. sample curator operations from the curator policy;
6. apply insert/update/delete operations to the SkillRepo;
7. compute reward after the group rollout;
8. update the curator using GRPO.

The rollout unit is not a single answer; it is the entire repository evolution path across the group.

##### Composite Reward

The reward combines four signals:

```text
r = r_task + λ_f r_fc + λ_u r_cnt + λ_c r_comp
```

- Task outcome reward: average success over all tasks except the first one, because the first task starts with an empty repository and cannot benefit from prior curation.
- Function call reward: fraction of generated curation function calls that are valid and successfully executed.
- Content quality reward: an external Qwen3-32B judge scores whether generated skills are semantically meaningful and likely to help future tasks.
- Compression reward: rewards concise repository updates by penalizing the ratio between repository token length and curator input context length, discouraging raw trajectory dumping.

##### GRPO Optimization

For each task group, SkillOS samples multiple independent rollouts. Each rollout traverses the same task group but creates a different repository history because the curator samples different edit decisions. GRPO compares the composite rewards across rollouts and reinforces higher-reward curation sequences.

The paper assigns the same rollout advantage to all tokens in the curation sequence and discards the KL term from standard GRPO to encourage policy exploration.

### 4. Experiments

#### Benchmarks

SkillOS is evaluated on:

- ALFWorld: text-based household interaction tasks with six task types.
- WebShop: simulated e-commerce navigation and purchase tasks.
- AIME24 and AIME25: mathematical reasoning benchmarks.
- GPQA-Diamond: graduate-level science multiple-choice questions.

Effectiveness metrics are success rate or accuracy. Efficiency metrics are environment steps for agentic tasks and tokens for reasoning tasks.

#### Baselines

The paper compares against:

- No Memory: independent task solving without external memory.
- ReasoningBank: stores reusable reasoning insights as searchable memory.
- MemP: procedural memory with hand-designed consolidation, forgetting, and re-indexing.
- SkillOS-base: same curator backbone without RL fine-tuning.
- SkillOS-gemini: Gemini-2.5-Pro directly performs curation without RL training.

All baselines share the same frozen executor, retrieval budget, and decoding settings within each backbone block.

#### Implementation Details

The curator base model is Qwen3-8B. During training, the executor is also Qwen3-8B and remains frozen. Training uses GRPO with learning rate `1e-6`, batch size 32, group size 8, top-5 skill retrieval, and the verl framework on 16 H100 GPUs.

Reported training time:

- ALFWorld: about 3 days;
- reasoning tasks: about 2.5 days;
- WebShop: about 5 days.

At test time, the curator is paired with Qwen3-8B, Qwen3-32B, Gemini-2.5-Pro, and in appendix analysis Gemini-3.1-Flash-Lite executors.

#### Main Results

On ALFWorld with Qwen3-8B executor, SkillOS raises average success rate from the strongest listed baseline ReasoningBank's 55.7 to 61.2 and reduces average steps to 18.9. With Qwen3-32B executor, SkillOS reaches 68.6 average success rate. With Gemini-2.5-Pro executor, SkillOS reaches 80.2 average success rate and 14.8 steps.

On WebShop and reasoning tasks, SkillOS also improves over memory-free and memory-based baselines. With Gemini-2.5-Pro executor, SkillOS reaches WebShop score 56.0, WebShop success rate 41.3, and average reasoning accuracy 88.6.

The paper emphasizes two result patterns:

1. RL-trained Qwen3-8B curation can outperform direct Gemini-2.5-Pro curation, suggesting that learned executor-grounded curation can matter more than raw curator scale.
2. Gains are larger on multi-turn agentic tasks than on single-turn reasoning tasks, because agentic tasks expose more reusable procedural regularities such as action ordering, recovery behavior, and environment constraints.

### 4.3 Generalization

SkillOS is trained with Qwen3-8B as executor but improves different frozen executors at test time. The paper interprets this as modularity: the learned curator writes skills that are useful across executor capacities and architectures.

The paper also reports cross-task transfer. Curators trained on reasoning tasks transfer well to agentic tasks, likely because reasoning training induces abstract strategies such as decomposition, verification, and adaptive planning. By contrast, skills learned from ALFWorld or WebShop are more environment-specific and transfer less broadly.

### 5. Analysis

#### Ablations

On ALFWorld, the full SkillOS-GRPO model reaches 61.2 average success rate and 18.9 steps. Ablations show:

- without content-quality reward: 58.6 success rate and 20.1 steps;
- without compression reward: 60.0 success rate and 19.3 steps;
- without grouping: 57.3 success rate and 20.6 steps.

The largest drop comes from removing task grouping, supporting the claim that related task streams are the core device for converting delayed feedback into learnable signal.

#### Curator Operation Behavior

At the beginning of training, `insert_skill` dominates because the repository is empty and the curator mainly populates it. As training progresses, `update_skill` becomes increasingly frequent while insertion declines. `delete_skill` remains smaller but grows slightly.

The paper interprets this as a shift from repository expansion to repository refinement and consolidation. Deletion is less common than update, so the main adaptation mode is revising previously acquired skills rather than aggressive pruning.

#### Skill Evolution Dynamics

Early in training, the curator adds generic sections such as tips and recommendations. Later, the added structures become more actionable: failure-handling logic, conditional branches, and explicit deviations from default workflows.

At the repository level, early skills are narrow and task-specific. Later repositories contain more meta-strategy skills such as verification, fallback planning, system search, and strategy adjustment. The paper treats this as evidence that the curator learns higher-level control knowledge, not just a larger collection of local tricks.

#### Skill Usage Attribution

The paper analyzes skill usage rate, successful skill usage rate, skill coverage, and average skills used per example. SkillOS uses skills on all ALFWorld evaluation examples, has higher success among skill-using examples, uses a larger fraction of its skill collection, and uses fewer skills per example. The claimed mechanism is more precise skill selection rather than simply stuffing more skill context into the executor.

### 6. Conclusion

SkillOS presents trained skill curation as a practical path toward self-evolving agents. The executor remains frozen, while the curator learns to manage a skill repository through grouped task streams and executor-grounded rewards. The paper's strongest claim is that repository-level procedural memory can improve without changing model weights, provided the write/update/delete policy is trained against downstream use.

### Appendix Details

#### Prompts

The appendix includes prompt templates for:

- the Skill Curator during training;
- function/tool signatures for curation operations;
- ALFWorld, WebShop, and reasoning executors with retrieved skills;
- external judge reward for generated skill contents;
- LLM-as-judge correctness signals for task trajectories.

The executor prompts explicitly use ReAct for agent execution and CoT for reasoning tasks.

#### Group Construction Details

For reasoning tasks, the grouping pipeline has two stages:

1. latent attribute annotation into five phrase-list dimensions: topics, required skills/capabilities, concepts/theorems, heuristic strategies, and common pitfalls;
2. group construction by retrieving candidate task pairs, filtering them through dependency gates, and ranking by soft-Jaccard similarity plus difficulty bonus.

The dependency gate requires shared concepts and skills, shared reasoning or pitfalls, avoidance of near duplicates, sufficient relatedness, progression through at least one new concept or skill, and a forward curriculum direction.

This grouping procedure matters because it attempts to create task sequences that are related enough for skill reuse but not so redundant that curation degenerates into memorization.

#### Case Studies

The paper gives examples of two curation styles:

- Agentic task skills become procedural and compositional. A failure-recovery skill abstracts a workflow such as exhaustive search, confirm unavailability, identify substitute, and proceed with substitute.
- Reasoning task skills become multi-path frameworks with explicit formulas, prerequisite constraints, and branching solution routes.

A comparison case shows SkillOS-base writing a generic partitioning recipe, while SkillOS writes a concrete counting framework with equations, constraints, and a worked example.

An ALFWorld case shows a retrieved skill helping the executor interpret "look at the CD under the desklamp" by focusing search under or around light sources, rather than exhausting irrelevant containers.

### Limitations

#### Retrieval Mechanism

SkillOS currently uses BM25 keyword retrieval. This isolates curation as the main research object, but denser, hybrid, or learned retrieval could improve relevance. Joint optimization of retrieval and curation remains future work.

#### Simplified Skill Representation

Each skill is simplified to one Markdown file. This omits two affordances of fuller skill systems: supporting scripts/resources and hierarchical organization. Behaviors that would naturally be executable code or sub-skill compositions must be flattened into prose.

#### Frozen Executor

Freezing the executor isolates the contribution of skill curation and enables modular transfer. The cost is that the curator can only change behavior through repository text. Joint or alternating optimization of curator and executor might improve alignment but would be more expensive and less executor-agnostic.

### Future Research Directions

#### Agentic Search over Experiential Memory

The paper identifies retrieval as the next bottleneck. Instead of static top-k BM25, a future system could use agentic search where a curator or retrieval agent issues multiple queries, reformulates them, and decides which skills to surface, cite, or compose.

#### Hierarchical and Compositional Skills

Future SkillRepo versions could support skills that link, invoke, and abstract lower-level sub-skills. This would move the repository from flat entries toward a procedural library.

#### Multi-Agent and Shared Memory

SkillOS currently treats memory as a single agent's private artifact. Multi-agent settings raise conflict resolution, credit assignment, specialization, and cross-agent transfer problems. Shared SkillRepo curation would need governance over competing updates and downstream effects.

## Integration Decisions

This page should remain source-level until its claims are cross-checked with follow-up papers or independent replications. The paper's most promotable durable idea is repository-level skill curation under delayed downstream feedback: learning how to write, revise, and delete procedural memory artifacts by evaluating their later effect on a frozen executor.

The existing [[wiki/sources/SkillOS Source Guide]] should remain as the article-level guide. This page is the paper-level guide and should be used when exact paper claims, experimental setup, appendix details, or limitations matter.

Connections to existing pages:

- [[wiki/concepts/Agent Skill]]: SkillOS operationalizes skills as Markdown files with frontmatter and procedural instructions.
- [[wiki/concepts/Skill Self-Evolution]]: SkillOS is a concrete method for training skill curation from downstream task feedback.
- [[wiki/topics/AI Skills Workflow]]: SkillOS automates a capture-maintain-reuse workflow that manual skill practice performs by review.
- [[wiki/topics/AI Memory]]: SkillOS treats procedural memory as a repository whose contents must be retrieved, compressed, updated, and audited.
- [[wiki/concepts/Verification Loop]]: task judges, content judges, and downstream outcomes provide the feedback loop for curation.

## Open Questions

- Does the simple BM25 retrieval mechanism become the limiting factor as SkillRepo grows larger and more semantically overlapping?
- Can SkillOS safely extend from prose-only Markdown skills to multi-file skills with executable scripts and external resources?
- How should learned deletion be governed when skills represent shared organizational knowledge rather than benchmark-local artifacts?
- Would joint curator-executor training improve performance enough to justify losing modularity across executors? ^[ambiguous]
- How robust are the reported gains under non-simulated streaming distributions where task relatedness is weaker or adversarial? ^[inferred]

## Related

- [[wiki/maps/AI Map]]
- [[wiki/sources/SkillOS Source Guide]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/AI Memory]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Skill Self-Evolution]]
- [[wiki/concepts/Continual Learning for AI Agents]]
- [[wiki/concepts/Verification Loop]]
