---
title: >-
  Designing, Refining, and Maintaining Agent Skills at Perplexity Source Guide
category: sources
type: source
status: draft
tags: [article, agents, skills, workflow, context]
sources:
  - https://research.perplexity.ai/articles/designing-refining-and-maintaining-agent-skills-at-perplexity
created: 2026-05-18T14:34:14+08:00
updated: 2026-06-24T12:01:01+0800
summary: >-
  Perplexity's guide treats agent skills as costly, progressively loaded context packages that balance deterministic scripts with LLM judgment and turn workflows into action arcs.
provenance:
  extracted: 0.88
  inferred: 0.11
  ambiguous: 0.01
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-05-18
aliases:
  - Designing, Refining, and Maintaining Agent Skills at Perplexity
  - Perplexity agent skills guide
---
# Designing, Refining, and Maintaining Agent Skills at Perplexity Source Guide

> Source: Designing, Refining, and Maintaining Agent Skills at Perplexity — https://research.perplexity.ai/articles/designing-refining-and-maintaining-agent-skills-at-perplexity

## Capture Policy

This page preserves the Perplexity Agents team's source-level guidance on agent skill design. It keeps the article's practical method, examples, budgets, warnings, and maintenance loop as a source guide rather than collapsing them into a new general concept page.

## What It Covers

The article frames skills as curated context packages for agent systems. A skill is not ordinary documentation and not merely a software module: it is an activation surface, a compressed instruction body, and a progressively disclosed directory of files that shape what an agent can notice, load, and do.

The source belongs in the AI / Agent skills cluster because it adds a production-practice layer to [[wiki/concepts/Agent Skill]], [[wiki/topics/AI Skills Workflow]], and [[wiki/topics/Tool Routing]]: skill authoring is partly a routing problem, partly a context-budget problem, and partly a maintenance/evaluation problem.

## Preserved Content

### What a skill is

Perplexity defines a skill through four complementary properties.

#### A skill is a directory

A skill is a folder-shaped package. The root `SKILL.md` carries frontmatter and high-signal guidance, while supporting files can live in accessory directories:

- `scripts/` for deterministic helper code
- `references/` for large or conditional documentation
- `assets/` for templates, schemas, examples, or reusable artifacts
- `config.json` for setup or persistent user configuration

The directory shape matters because the agent does not need every byte at once. A skill can expose a small trigger and body first, then let deeper resources load only when the task requires them.

#### A skill is a format

The root skill file needs at least a name and description. The source treats the description as the most important routing field: it should tell the agent when to load the skill, not merely summarize the skill for a human reader.

The recommended shape is closer to `Load when...` than to a README abstract. The name should align with the directory name, typically in lowercase hyphenated form.

Optional metadata can include dependencies, review/eval support, or system-specific fields. Perplexity notes that some system-specific metadata may be stored separately so it does not consume unnecessary model context.

#### A skill is invocable

A skill is not always fully present. The agent decides whether to activate it. In Perplexity Computer, activation involves a `load_skill` path that can copy the skill directory into a sandbox, load dependencies, strip frontmatter, and expose relevant files.

Different agent systems expose file trees differently. Perplexity Computer generally avoids putting full directory listings into the model's context unless configured to do so, because directory visibility itself has context cost.

#### A skill is progressive

The article's core cost model has three tiers:

| Tier | Content | Cost pattern |
| --- | --- | --- |
| Index | Skill names and descriptions | Paid in every session |
| Load | Main `SKILL.md` body | Paid only after activation |
| Runtime | Scripts, references, assets, subfiles | Paid only if read or used |

Perplexity gives rough budgets: the always-present index should be short, around 100 tokens per skill; the loaded body should ideally stay under about 5,000 tokens; runtime files may be much larger because they are accessed conditionally.

This progressive model makes [[wiki/topics/Context Management]] part of skill design. Every skill adds always-on routing text, and many real sessions may load three to five skills. A skill therefore has to justify both its own body and its interference with neighboring skills.

### When a skill is needed

A skill is valuable when the model needs special context, stable judgment, local conventions, non-obvious procedures, or consistent behavior that is not reliably supplied by model weights alone.

The article gives design-related skills as an example: design taste, font choices, visual tone, and qualitative preferences can encode expert judgment that the model may not infer from general training data.

A skill is not needed when the model already handles the task well, when the instruction applies to nearly every request and belongs in global context, or when the source material changes so quickly that a static skill will become stale.

### Every skill is a tax

Perplexity emphasizes that each skill creates cost:

- the index description competes for attention in every session;
- the description can accidentally route too broadly or too narrowly;
- the body consumes context after loading;
- accessory files can distract if the hierarchy is unclear;
- new skills can degrade unrelated skills through routing interference.

The article therefore treats skill creation as a reliability tradeoff rather than an automatic good. A skill should be added only when the value of reusable context or procedure exceeds the routing and context burden.

### How to build a skill

#### Step 0: write the evals

The source recommends writing evaluation cases before the skill. Useful eval sources include real user requests, known agent failures, and boundary cases near neighboring skills.

Both positive and negative cases matter. Negative and forbidden-load cases are especially valuable because they test whether the skill avoids activating when another skill, global instruction, or ordinary model capability should handle the request.

This connects directly to [[wiki/concepts/Verification Loop]]: skill quality should be judged by behavior under tasks, not by whether `SKILL.md` looks clear to a human.

#### Step 1: optimize the description

The description is the routing API. Perplexity recommends keeping it short, ideally around 50 words or fewer, and making it reflect real user intent.

A poor description summarizes the workflow. A strong description names the situation in which the skill should load. For a pull-request monitoring skill, the description should match user intents such as wanting someone to watch CI or make sure a change lands, rather than listing internal monitoring steps.

Small wording changes can meaningfully affect activation precision and recall. After merge, description changes require eval support because they alter routing behavior.

#### Step 2: write the body

The body should not be a full human README. It should spend tokens only on information that improves agent behavior:

- domain-specific judgment;
- failure modes;
- constraints;
- non-obvious procedures;
- gotchas;
- exact steps only when exact steps matter.

The article warns against listing routine commands when the model already knows the command family. A git workflow skill, for example, should usually specify the desired outcome and constraints—such as applying a commit cleanly and preserving intent—rather than enumerate standard `git` commands.

#### Step 3: use the hierarchy

Bulky, conditional, or branching material belongs in accessory files. `scripts/` should hold deterministic helpers, `references/` should hold larger supporting material, and `assets/` should hold templates or schemas.

The U.S. income-tax example shows why hierarchy matters. Perplexity reports that a tax skill with all 1,945 sections of the U.S. Internal Revenue Code in a flat folder performed worse than not loading the skill. Organizing the material into topical subdivisions improved read precision, though it required curated navigation aids.

The lesson is not merely “split files.” The hierarchy has to mirror the agent's retrieval and decision path. A large skill without navigable structure can lower performance by increasing search burden and distracting the model.

#### Step 4: iterate

The article recommends developing the skill and eval set together before sending a consolidated review. Iteration should test routing, body usefulness, accessory-file disclosure, boundary cases, and end-to-end task success.

#### Step 5: ship

A skill is ready to ship when its routing description, main body, hierarchy, dependencies, and eval cases jointly support the intended behavior.

### How to maintain a skill

#### The gotchas flywheel

Perplexity treats post-launch skill maintenance as mostly append-oriented. The gotchas section grows as real failures surface:

- if the agent fails in a known way, add a targeted gotcha;
- if the skill activates too broadly, refine the description and add negative evals;
- if the skill fails to activate, add targeted keywords and positive evals;
- if global prompts change, check whether the skill now duplicates or conflicts with global context.

This turns skill maintenance into a feedback flywheel: failures become concise, high-signal context that prevents the same failure from recurring.

#### Eval suites

The article names several evaluation types:

- skill-loading tests for activation precision and recall;
- forbidden-load tests for boundary protection;
- progressive-loading tests to ensure accessory files are read when needed;
- end-to-end task tests judged by rubrics;
- cross-model checks across GPT, Claude Opus, and Claude Sonnet.

Different model families may route or use skills differently, so a skill that works for one model is not automatically reliable for another.

### Practical warnings

Perplexity's warnings cluster around context economics and routing interference:

- Do not create a skill for knowledge the model already has.
- Put broadly relevant instructions in global context, not conditional skills.
- Avoid skills for fast-changing APIs unless there is a maintenance path.
- Treat every sentence as a context cost.
- Avoid LLM-generated skills that merely restate generic model knowledge.
- Watch for cross-skill interference whenever adding or changing skills.
- Use evals before changing a description after merge.

The article's reliability framing is high-end: skill authoring should move systems beyond rough 80/20 behavior toward far more reliable 99.9% or 99.99% task performance where the workflow needs it.

## Integration Decisions

This guide should remain source-level because several claims are specific to Perplexity's runtime and production experience, especially `load_skill`, Perplexity Computer's directory exposure choices, and the reported U.S. tax-skill example.

The stable concepts to promote into broader pages are:

- skill descriptions are routing surfaces, strengthening [[wiki/topics/Tool Routing]];
- skills are progressive context packages, strengthening [[wiki/concepts/Agent Skill]] and [[wiki/topics/Context Management]];
- skill maintenance should be eval- and gotcha-driven, strengthening [[wiki/topics/AI Skills Workflow]] and [[wiki/concepts/Verification Loop]];
- accessory-file hierarchy is a context-management mechanism, not just file organization.

The source complements but does not replace [[wiki/sources/Claude Code Skills Source Guide]], which focuses on Claude Code practice, or [[wiki/sources/ADK Skill Design Patterns Source Guide]], which classifies skill content patterns. Perplexity's distinctive contribution is the explicit cost/routing/eval discipline for production skill lifecycle management.

## 2026-06-24 Capture Delta: Determinism, Judgment, and Workflow Arc

这次补充材料把文章中的 skill 设计逻辑进一步压成一条边界原则：好的 agent skill 不是让 LLM 自由发挥，也不是把所有步骤硬编码成脚本，而是明确划分“什么必须确定”和“什么应该留给智能”。

### 明确代理不应决定什么

重复、可计算、硬规则和格式约束不应交给 LLM 临场判断。它们更适合进入 `scripts/`、模板、校验器、固定流程或不可跳过的 gate。

这条原则的价值在于消除同一输入下的波动：如果一件事需要稳定复现，skill 应该把它变成确定性执行面，而不是每次让模型重新解释。它强化了 [[wiki/concepts/Computational and Inferential Controls]] 的分工：computational controls 负责可执行正确性，inferential controls 只处理无法完全形式化的判断。

### 明确代理应当决定什么

复杂语境解释、创作、对话、异常处理、权衡和生成不适合全部写死。skill 应该给出目标、约束、证据标准和上下文资源，让 LLM 在具体环境中选择合适动作。

这条原则把 skill 从“脚本包装器”推进到“智能边界设计”：脚本提供骨架，模型负责把骨架接入当前问题、代码库和用户意图。^[inferred]

### 制定宪法，而非建议

`SKILL.md` 中的关键规则应像宪法一样约束 agent，而不是写成容易被“帮用户省事”绕开的建议。尤其是安全、验证、顺序、询问前置、禁止跳步和成功标准，应写成 mandatory gate。

这不是削弱 agent 的灵活性，而是用硬边界保护灵活性：越能确定哪些地方不可协商，模型就越能在剩余空间内安全地发挥。^[inferred]

### 技能作为工作流弧度的催化剂

补充材料中的 “catalyst for workflow” 强调 skill 的输出不应停在一次性报告。一个强 skill 会把诊断结果、脚本输出、用户回答或中间 artifact 转成 agent 下一步行动的上下文输入。

普通工具形成断点：脚本吐出 JSON、日志或检查项后，人工仍要解释、查资料、写修复方案。workflow catalyst 形成闭环：skill 规定 agent 如何读取这些结果，并把它们接到后续动作，例如生成 `AGENTS.md`、起草修复计划、补测试或更新规则。

因此，skill 的设计对象不是单次命令，而是一条 action arc：触发 → 装载上下文 → 确定性检查 → LLM 解释 → 产出下一步 artifact → 验证或回写经验。^[inferred]

### 信息到生产力的转化

传统 tribal knowledge 只是静态信息；agent skill 把它变成可调用、可执行、可版本化、可维护的生产力表面。

这也是为什么 skill 不等同于文档：文档告诉人如何做，skill 让 agent 能在任务中自动加载这套做法，调用脚本、读取模板、遵守 gate，并把结果继续交给下一步工作流。^[inferred]

## Open Questions

- Which parts of Perplexity's budgets, such as 100-token descriptions and 5,000-token bodies, transfer across other agent harnesses and which are runtime-specific?
- How should a team measure cross-skill interference after adding one new skill?
- When should gotchas remain appended inside a skill, and when should repeated gotchas trigger a split into a new skill, script, or global rule?
- How should a skill author decide which parts belong in deterministic scripts versus LLM judgment without overfitting one current workflow?
- What artifact shape best preserves a workflow arc so a skill's diagnostic output naturally becomes the agent's next action input?

## Related

- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Agent Skill Design Patterns]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/Tool Routing]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/sources/Claude Code Skills Source Guide]]
- [[wiki/sources/ADK Skill Design Patterns Source Guide]]
