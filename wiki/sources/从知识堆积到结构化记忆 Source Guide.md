---
title: >-
  从知识堆积到结构化记忆 Source Guide
category: sources
type: source
status: draft
tags: [article, agents, memory, skills, harness]
sources:
  - conversation:2026-05-13
created: 2026-05-13T16:50:00+08:00
updated: 2026-05-13T16:50:00+08:00
summary: >-
  这页保存一篇中文文章对 LLM Wiki、Obsidian-Wiki、GBrain 与 Skillify 的比较，重点是 Agent 知识管理从堆积走向结构化记忆。
provenance:
  extracted: 0.86
  inferred: 0.12
  ambiguous: 0.02
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-13
aliases:
  - 从“知识堆积”到“结构化记忆”
  - Agent 知识管理与自进化机制
  - LLM Wiki 与 GBrain 对比
---

# 从知识堆积到结构化记忆 Source Guide

> Source: 从“知识堆积”到“结构化记忆”（用户粘贴的中文文章）

## Capture Policy

这页保存文章的 source-level 内容：文章的论证顺序、关键类比、系统组件、技术路径比较、适用边界和工程判断都保留在来源层。文中的项目描述、指标和案例判断主要来自单篇文章，应先作为 source claims 使用，再视后续材料决定是否提升到稳定概念或综合页。

## What It Covers

这篇文章把 Agent 时代的知识管理问题从“收藏资料”推进到“结构化记忆”。它比较了 Karpathy 的 LLM Wiki、Obsidian-Wiki 和 Garry Tan 的 GBrain，核心问题是：如何让 Agent 把非结构化资料、历史对话、经验规则和事实知识转化为可被渐进式加载、可维护、可复用的长期知识资产。

文章与当前 wiki 中的 [[wiki/topics/AI Memory]]、[[wiki/concepts/Agent Skill]]、[[wiki/topics/AI Skills Workflow]]、[[wiki/topics/AI Harness]]、[[wiki/concepts/Company Brain]] 和 [[wiki/concepts/Context Graph]] 直接相连。它的新增价值不在单独定义 memory 或 skill，而在把知识工程、skill 化、wiki 化、图谱化和混合检索放进同一条 Agent 自进化路径里。

## Preserved Content

### 知识管理的原始痛点

文章从人类知识管理的弱点切入：人类擅长“无脑堆积”知识，例如收藏文章、保存文档、囤积桌面文件；但不擅长长期组织知识。知识要真正可用，需要被分类、关联、更新、去重、验证和迁移，而这些维护工作耗时、无聊、缺乏统一标准，导致个人和组织都会产生大量“落灰”的信息资产。

企业知识库的维护成本更高，文章特别强调两个维度：

- **时效性与动态维护**：知识有生命周期，会随着产品迭代、业务变化而过时。系统必须识别失效知识、剔除旧内容、接入新知识。
- **组织结构复杂性**：知识很难只按产品、问题场景或关键词形成单一树状分类。像“镜像”可能集中在 ECS 和轻量应用服务器，而 OpenClaw 相关知识可能横跨多个产品线。复杂交叉关系使人工维护完美知识图谱几乎不可行。

这为 Agent 知识管理提供了动机：如果 Agent 的上下文不仅来自当前 prompt，还来自外部注入的知识，那么知识质量会直接决定 Agent 能力上限。

### 经验性知识与事实性知识

文章把 Agent 需要的知识分成两类：

- **经验性知识**：完成特定任务所需的策略、步骤、习惯和隐性经验。例如 AI Coding 中的命名规范、注释风格、设计顺序、库选择、测试习惯。这类知识常被封装为 [[wiki/concepts/Agent Skill]]。
- **事实性知识**：概念、术语、机制、FAQ、最佳实践、最新技术博客摘要等，可作为回答问题或执行任务的基础素材。

文章的关键判断是：Prompt Engineering 主要教模型“完成什么任务”，Knowledge Engineering 则教模型“应该知道什么，以及如何运用已知信息”。Agent 的长期效果不只依赖 prompt、context 或 harness，也依赖知识和 skill 能否持续沉淀。

### LLM Wiki 的核心突破

Karpathy 的 LLM Wiki 被文章解释为一种突破传统 RAG 的方法。传统 RAG 在每次查询时重新从原始文档中检索和拼接答案；LLM Wiki 则让 LLM 渐进式维护一个持久 Markdown Wiki，把原始资料“编译”为带交叉引用、矛盾标注和综合页面的知识体。

文章用“编译型语言 vs 解释型语言”来描述差异：

| 对比项 | 传统 RAG | LLM Wiki |
|---|---|---|
| 知识检索 | 每次查询重新检索原始文档 | 知识提前编译到 Wiki 中 |
| 交叉引用 | 运行时重新发现 | 交叉引用已经建立 |
| 知识矛盾 | 每次重新发现 | 矛盾已经被标记 |
| 综合分析 | 每次重新推导 | 随来源添加持续丰富 |

LLM Wiki 的价值是让知识成为持续累积、可审查、可修改的活体，而不是每次临场搜索的片段集合。人类负责策划来源、提问题、判断意义；LLM 负责摘要、归档、交叉引用、记账和维护。

### LLM Wiki 的三层架构

文章保留了 LLM Wiki 的三层结构：

1. **Raw Sources 原始资料层**：只读存档区，保存文章、论文、图片、数据文件等原始输入。LLM 读取它们，但不修改它们。
2. **The Wiki 知识层**：LLM 生成和维护的 Markdown 页面集合，包括摘要页、实体页、概念页、比较页、综合页等。
3. **The Schema 索引/规则层**：例如 CLAUDE.md 或 AGENTS.md，规定 Wiki 结构、命名约定、摄入流程、查询流程和维护规则，使 LLM 成为有纪律的 wiki maintainer。

文章将这个结构解释为“高质量整理知识”，而不是“大规模摄入知识”。LLM Wiki 不只是问答工具，而是一套自我维护的知识管理体系。

### LLM Wiki 的三种操作

文章把 LLM Wiki 的工作流分为三类：

- **Ingest 摄入**：添加新来源时，LLM 阅读原始材料，提取关键要点，生成摘要页，更新 index，回填相关实体和概念页，并记录 log。一个来源可能联动 10–15 个页面。
- **Query 查询**：用户向 wiki 提问时，LLM 先定位相关页面，再综合带引用的答案。高质量答案还可以归档为新页面，使探索本身也能复利。
- **Lint 维护**：周期性检查矛盾、过时声明、孤儿页面、缺失交叉引用和数据缺口，类似代码静态检查。

这三种操作共同形成知识闭环：来源进入 wiki，查询生成新的知识，维护保持系统健康。

### index.md 与 log.md

文章强调两个导航文件：

- **index.md**：面向内容，是 wiki 页面目录和导航入口。LLM 查询时先读 index，再深入具体页面。在中小规模知识库中，这可以替代复杂 RAG 基础设施。
- **log.md**：面向时间，是 append-only 的演化记录。它保存 ingests、queries、lint passes 等操作，让 wiki 有可追踪的时间线。

这个设计与当前仓库的 [[wiki/index]] 和 [[wiki/log]] 一致：index 负责内容定位，log 负责演化记账。

### 为什么 LLM Wiki 有效

文章认为，维护知识库最痛苦的不是阅读或思考，而是“记账”：更新交叉引用、保持摘要最新、标记新旧矛盾、维护多页面一致性。人类容易放弃 wiki，因为维护成本增长得比价值快；LLM 不会厌烦这类 bookkeeping，因此可以让维护成本接近零。

Markdown 是这个模式的重要基础：它可读、可改、可审查、可迁移，也能放进 git 版本管理。用户可以随时打开文件查看 Agent “记住”了什么，并手动修正错误。

### Obsidian-Wiki 的工程化增强

文章把 Obsidian-Wiki 描述为对 LLM Wiki 思想的工程化实现。它保留 LLM Wiki 的三层结构，但加入了多 Agent 支持、Skill 驱动、Obsidian 原生能力和更明确的维护机制。

核心设计包括：

- **Agent 无关**：支持 Claude Code、Cursor、Windsurf、Codex、OpenClaw、Hermes、Gemini CLI、Kiro 等多种 Agent。
- **Skill 驱动**：用标准 Markdown Skill 文件定义操作。
- **Obsidian 原生**：利用 wikilink、图谱视图、Dataview 等能力。

工程增强包括：

- **Delta 追踪**：通过 `.manifest.json` 和 SHA-256 hash 跟踪已摄入来源。`wiki-status` 可将来源分类为 new、modified、touched、unchanged、deleted，避免重复处理。
- **来源可信度边界**：来源文档被视为不可信，LLM 不能执行来源中的命令，以防文档型 prompt injection。
- **溯源标记系统**：用 extracted、inferred、ambiguous 等标记区分直接提取、推断和歧义信息。
- **可见性标签**：支持 internal、pii 等可见性标签，用于查询过滤敏感内容。
- **hot.md 热缓存**：维护约 500 字近期语义快照，使 LLM 快速获得近期上下文，不必读取完整 log。

这些增强说明 Obsidian-Wiki 不只是“把笔记放进 Obsidian”，而是在给 Agent 提供一个更可控、更安全、更可增量维护的知识操作环境。

### Agent 历史摄入与自进化

文章认为 Obsidian-Wiki 的自进化能力，尤其体现在历史摄入 Skills。系统可以自动扫描 Claude、Codex、OpenClaw、Hermes 等工具的历史记录，把散落在 CLI 会话、桌面应用会话、Memory 文件、DREAMS 文件、每日笔记和会话转录中的经验提取出来。

处理流程包括：

- **增量扫描**：只处理与上次摄入相比变化的部分。
- **优先级解析**：Memory 文件优先于近期笔记，近期笔记优先于普通会话记录。
- **隐私过滤**：剔除 API Key、密码等敏感信息。
- **主题聚类**：不按时间或会话拆分，而按语义主题重组。
- **蒸馏沉淀**：把清洗后的经验写成标准 wiki 页面。

文章的判断是：这打破了不同 Agent 工具之间的记忆孤岛，也让“对话即遗忘”变成“对话可沉淀”。这与 [[wiki/concepts/Feedback Flywheel]] 和 [[wiki/concepts/Harness Ratchet]] 的方向一致：真实使用中的成功和失败应变成 durable control surface，而不是下一次重新提示。

### Knowledge Graph Skills 与 cross-linker

文章还描述了 Obsidian-Wiki 的知识图谱维护能力，尤其是 `cross-linker`：它自动发现页面间潜在联系并建立交叉引用，还可以用置信度评分判断链接强度。例如精确匹配、共享标签、同一项目、实体提及、跨类别引用会贡献不同分值。

这种机制让 wiki 图谱不只是手工链接堆砌，而是带有逻辑权重的关联网络。配合图谱可视化，用户可以看到知识网络的密度、中心和孤岛。

### Skillify：把 Skill 泛化为知识组织形态

文章提出的核心词是 **Skillify**：不把 skill 限定为固定的 `SKILL.md` 指令文件，而是把它泛化为一种知识组织方式。

在这种范式下，任何 Markdown 文件、文档片段、笔记、历史记录都可能成为 skill-like knowledge。关键是通过元数据、schema 或触发规则说明：

- 什么场景下应该加载哪些文件；
- 哪些知识应该先披露，哪些应该按需披露；
- 哪些经验应该沉淀成可复用流程；
- 哪些事实应该保存在结构化知识库中。

文章用“巨大的结构化 Skill 包”来比喻个人知识库：它可以包含事实知识、经验知识、长期记忆、个人偏好和过往经历。用户负责投喂资料，Agent 负责整理、索引、持久化和按需加载。

这与 [[wiki/topics/AI Skills Workflow]] 里“skill 是上下文、流程、工具、记忆和验证的组合面”一致。文章进一步强调：Skillify 的目标是让 Agent 下次遇到相似问题时直接读取已内化的知识，而不是重新搜索。

### 智能客服知识体系的三阶段演进

文章用阿里云智能客服作为类比，把知识体系演进分成三阶段：

1. **传统智能知识库时代（2016–2022）**：知识面向搜索引擎，由人工严格分类、打标和归档，形成树状或标签体系。检索依赖关键词匹配，维护成本高，灵活性差，长尾问题效果弱。
2. **RAG 时代（2023 起）**：采用“前置小模型检索 + 后置大模型生成”。RAG 解决海量知识存储和召回，但有模型能力断层、搜索独立性和知识未沉淀问题。
3. **Agent 时代**：知识组织转向 LLM Wiki / GBrain 这类持久知识系统。知识被结构化后成为 Agent 内部资产，下次相似问题可直接使用，形成“一次学习，永久可用”的飞轮。

文章指出，Agentic RAG 可以通过反复优化搜索关键词提升召回，但本质仍可能是在用昂贵推理弥补检索不足，并没有解决知识未沉淀问题。

### LLM Wiki / Obsidian-Wiki 的适用场景

文章列出这类轻量知识系统适合的场景：

- **个人深度研究**：长期跟踪主题，像写书一样持续修正章节。
- **结构化读书笔记**：为书籍建立伴侣 wiki，拆解概念、人物、观点和关联。
- **项目知识管理**：跟踪 ADR、架构演变、经验教训和 postmortem。
- **AI Agent 记忆固化**：从 Claude、Hermes、OpenClaw 等交互历史中提取隐性知识。
- **小团队内部 Wiki**：比 Confluence 或 Notion 更轻量、更可控。

### LLM Wiki / Obsidian-Wiki 的能力边界

文章也明确了局限：

1. **无数据库依赖**：纯 Markdown 主要依赖 index、grep 或 QMD，复杂查询能力有限。
2. **规模天花板明显**：数百到低千页面时 index 驱动效果较好，但目录膨胀后模型定位困难。
3. **无内建自动化调度**：摄入和 lint 通常需要用户手动触发或外部脚本调用。
4. **弱结构化图谱**：wikilink 缺乏 typed edges，不能直接表达“投资了”“任职于”等语义关系。
5. **非实时实体检测**：cross-linker 等维护技能需要手动触发，不是 always-on。

文章把这个问题类比为 Skill 爆炸：当 skill 或知识页面过多时，检索和调用效率会下降，需要更工程化的检索、索引或图数据库支持。

### GBrain 的工程化路线

文章把 GBrain 描述为比 LLM Wiki 更厚重的工程化实践：它保留文件系统存储和渐进式披露，但加入混合检索和实体关系图谱，解决规模化后的定位和推理问题。

GBrain 的架构哲学被概括为 **Thin Harness, Fat Skills**：Harness 尽量薄，把主要能力放在丰富 skills 上。这与很多把重点放在 Harness Engineering 的路径不同。文章认为它的核心洞察是：

- 让 LLM 决定“做什么”；
- 让代码保证“在哪里”和“如何做”。

### 潜在空间 vs 确定性

GBrain 用 **Latent Space** 和 **Deterministic** 区分任务边界：

| 对比 | 潜在空间（Latent Space） | 确定性（Deterministic） |
|---|---|---|
| 特点 | 智能：阅读、解释、决策 | 信任：相同输入总是产生相同输出 |
| 适合场景 | 判断、分析、综合 | SQL、计算、链接构建 |
| 执行者 | LLM | 代码 |

例如，让 LLM 判断“这条信息是否应该属于某个人的页面”属于潜在空间；用代码构建交叉验证链接、验证引用格式属于确定性。这与 [[wiki/topics/AI Harness]] 的边界设计直接相关：模型负责语义判断，harness 负责可重复、可审计、可恢复的控制流程。

### GBrain 的混合检索：向量过滤 + 文件披露

文章强调，GBrain 引入向量数据库并不等于回到传统 RAG。传统 RAG 把知识完全托管给搜索引擎；GBrain 的知识本体仍存在 Markdown 文件中，向量索引只是用来解决规模膨胀后的候选过滤问题。

检索流程是“Chunk 确认 → 整页加载 → 分层呈现”：

1. **混合搜索**：结合关键词和语义向量相似度，从海量内容中筛选相关 chunk，通常约 2KB。
2. **完整页面加载**：一旦 chunk 证明某页相关，就调用 `get_page()` 加载整页 Markdown，保留上下文完整性。
3. **分层喂给模型**：先给“编译真相”，即当前综合摘要或结论；再给“时间线证据”，即历史记录、原始来源和演化过程。

文章认为这种“向量粗筛 + 文件精读”比纯 RAG 更能保留语义完整性，也比纯文件遍历更高效。它把渐进式披露延伸到检索环节：先用低成本确认相关性，再把高价值内容完整交给模型阅读。

### 图谱加权与 benchmark claim

文章引用 GBrain 在 240 页富文本语料库 benchmark 上的结果：

| 指标 | GBrain（带图谱） | 仅混合搜索（无图谱） | 差距 |
|---|---:|---:|---:|
| P@5 | 49.1% | 17.7% | +31.4 pp |
| R@5 | 97.9% | — | — |

文章认为主要增益来自图谱加权的 backlink boost：连接良好的实体在搜索排名中更高。

这些数字应保持 source-level：它们来自文章对 GBrain benchmark 的转述，当前页不把它们提升为通用结论。

### GBrain 的图谱构建 Pipeline

文章把 GBrain 的图谱构建描述为四步流水线：

1. **实体抽取**：用正则、Markdown link、wikilink 和关键词模式识别人名、公司、会议等实体。它不是传统 NER，而是面向已有文本和链接格式的规则抽取。
2. **页面生成**：为识别出的实体生成 `people/xxx.md`、`companies/xxx.md` 等页面，作为图谱节点。
3. **关系分类**：用关键词匹配判断关系类型，例如 `works_at`、`founded`、`invested_in`、`advises`。
4. **反向链接强制化**：如果 A 提到 B，系统自动在 B 页面添加指向 A 的 backlink，保证图谱连通性。

文章强调 GBrain 不只是 Markdown 交叉引用。它有完整图结构：

- **Nodes**：实体页面；
- **Edges**：`links` 表中的 `(Source, Relation_Type, Target)`；
- **Relation Types**：有类型的语义关系；
- **Graph Traversal**：可用 `graph-query <slug> --depth N` 做多跳查询。

它没有采用 RDF 三元组等学术标准，但满足“节点 + 有类型边 + 可遍历性”的知识图谱定义。文章认为，这使 Agent 能从文档检索进一步走向结构化关系推理。

### 多模态与知识运营闭环

文章还指出，GBrain 支持视频、音频、PDF、截图等多模态输入，通过自动转录、OCR 和实体抽取转成结构化文字，再进入知识图谱和索引系统。

它的完整闭环是：

1. 信息入口收集；
2. 摘要、转录、实体抽取；
3. 归档到文件系统；
4. 构建向量索引；
5. 查询时做语义/关键词混合检索；
6. 大模型驱动渐进式阅读；
7. 修复引用和关系；
8. 继续沉淀为下一轮知识资产。

文章把它与早期简单 Memory 堆砌对比：无脑堆积会让记忆越来越慢、越来越乱；GBrain 通过清洗、组织、索引和维护实现“自进化”而不是“自混乱”。

### 最终技术选型判断

文章的总结不是 LLM Wiki 与 GBrain 二选一，而是混合架构：

- LLM Wiki 追求轻量、透明、可控，适合个人和小团队。
- GBrain 追求工程化、稳健、可扩展，适合复杂数据和较大规模。
- 两者共同目标是让 Agent 高效管理、使用和持续迭代内部知识，形成长期记忆和自我进化。

文章也指出代价：渐进式披露通常比传统 RAG 慢，因为它增加工具调用和文档读取时间。在企业生产环境中，延迟可能不可接受。因此实践上更适合混合：用向量检索、关键词索引快速初筛，解决“找得快”；用大模型深度阅读、离线 wiki 维护和图谱更新解决“答得准”和“记得牢”。

### 与 Agent 工程主线的关系

文章把知识管理放到 Agent 架构主线中：过去讨论较多的是 Context Engineering、Harness Engineering、Prompt Engineering 和模型调优，但真正让 Agent 从“一次次试错探索”进化为“持久化学习更新”的分水岭，是 Skill 与知识的动态维护体系。

知识与 Skill 不是孤立的：

- Skill 是执行能力的封装；
- 知识是决策的依据；
- Skillify 是把非结构化知识转为可调用结构化资产的过程；
- 自进化 Agent 需要从交互中抽取经验、修正认知、沉淀知识。

## Integration Decisions

这篇文章应作为 AI / Agent 知识管理 source guide 保存，而不是直接拆成多个概念页。原因是它同时混合了 LLM Wiki、Obsidian-Wiki、GBrain、企业智能客服、Skillify、图谱检索、RAG 对比和个人经验判断，source-level 保留更利于后续再综合。

可提升方向：

- **Skillify** 可能值得后续提升为概念页：它描述“把知识像 skill 一样组织和加载”的方式，但需要更多来源确认命名和边界。
- **Compiled Knowledge / 知识编译** 可作为 [[wiki/topics/AI Memory]] 或 [[wiki/topics/Context Management]] 的补充视角：知识不只是检索片段，而是被离线整理成可复用结构。
- **Hybrid retrieval plus progressive disclosure** 可补充 [[wiki/topics/AI Harness]] 与 [[wiki/concepts/Context Information Density]]：向量检索用于候选过滤，整页阅读用于语义完整性。
- **Typed graph memory** 可连接 [[wiki/concepts/Context Graph]] 和 [[wiki/concepts/Semantic File System]]：Markdown wikilink 足够透明，但 typed edges 更适合复杂关系推理。

需要谨慎保留在 source 层的内容：

- GBrain benchmark 指标；
- 对 Obsidian-Wiki 支持 Agent 数量和具体 skill 数量的描述；
- “Thin Harness, Fat Skills” 是否代表 GBrain 的正式设计哲学；
- Skillify / Skillfully 的命名来源与论文出处。

## Open Questions

- Skillify 是否应该成为独立概念，还是归入 [[wiki/concepts/Agent Skill]] 与 [[wiki/topics/AI Skills Workflow]] 的子模式？
- 当前 wiki 是否需要引入 typed edge 或轻量 graph table，还是继续依赖 Obsidian wikilink 与 cross-linker？
- 当 wiki 页面超过低千规模时，最自然的检索升级路径是 QMD、SQLite FTS、向量库、还是图数据库？
- Agent 历史摄入如何在隐私、权限、去重和错误记忆删除之间建立治理规则？

## Related

- [[wiki/topics/AI Memory]]
- [[wiki/concepts/Agent Skill]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/AI Harness]]
- [[wiki/topics/Context Management]]
- [[wiki/concepts/Context Information Density]]
- [[wiki/concepts/Company Brain]]
- [[wiki/concepts/Context Graph]]
- [[wiki/concepts/Semantic File System]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Feedback Flywheel]]
- [[wiki/syntheses/Agent System Design Space]]
