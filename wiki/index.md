---
title: Wiki Home
category: maps
tags:
  - llm-wiki
sources: []
created: 2026-05-04
updated: 2026-05-05T00:00:00+08:00
base_confidence: 0.30
lifecycle: draft
lifecycle_changed: 2026-05-05
type: map
status: draft
summary: Wiki Home is the navigation hub and inventory for the structured knowledge layer under wiki/.
aliases:
  - wiki home
  - wiki/index
---

# Wiki Home

This is the navigation hub and full page inventory for the structured wiki layer.

## Usage Rules

- New durable knowledge belongs under `wiki/`, not legacy note areas.
- Use [[wiki/NAMING]] for naming and placement rules.
- [[wiki/Welcome]] is legacy context, not the homepage.

## Maps
- [[wiki/maps/AI Map|AI Map]] — Entry point for the AI, Agent, and LLM knowledge cluster, linking concepts, topics, syntheses, and source guides. (#ai #agents #llm-wiki)
- [[wiki/maps/Classification Thinking Map|Classification Thinking Map]] — 这一组页面围绕一个核心问题展开： 人如何通过分类把混乱切成结构，以及这种切法的价值、方法与边界是什么。
- [[wiki/maps/CS Map|CS Map]] — 这页聚合当前 vault 中更偏计算机科学与软件架构的长期知识页。 (#cs #map #architecture)
- [[wiki/maps/Learning Map|Learning Map]] — Learning Methodology——七条动作原则
- [[wiki/maps/Management Map|Management Map]] — 这页聚合当前 vault 中与管理、决策、组织协作相关的长期知识页。 (#management #leadership #map)
- [[wiki/maps/Reading Map|Reading Map]] — 这页用于承接读书笔记从 raw/source 进入 wiki 的提升过程。 (#reading #books #map)
- [[wiki/maps/Software Analysis Map|Software Analysis Map]] — 这页把软件分析中的核心概念按层次放在一张图里。它基于 Software Analysis Three Generators 的三根： 组织、交换、边界 。 (#software-analysis #requirements #architecture #map)
- [[wiki/maps/Software Design Map|Software Design Map]] — 这页把软件设计中的核心概念按层次放在一张图里。关键区分是： (#software-design #architecture #map)

## Topics
- [[wiki/topics/AI Harness|AI Harness]] — AI Harness is the runtime order layer that connects model, context, tools, permissions, state, recovery, and cache stability into a controllable agent system. (#ai #agents #harness #runtime)
- [[wiki/topics/AI Skills Workflow|AI Skills Workflow]] — 当前 source notes 里已经出现了一个很清楚的 workflow 雏形： (#ai #skills #workflow)
- [[wiki/topics/BoltDB Internals|BoltDB Internals]] — BoltDB 是一个非常适合入门数据库实现的案例：代码量相对小，但已经覆盖了页式存储、B+ 树、事务、空闲页管理、写时复制等核心机制。 (#database #storage #golang)
- [[wiki/topics/Categorical Thinking|Categorical Thinking]] — 分类思维，是先找一个划分维度，再按这个维度把混乱切成几类，从而让理解、判断和行动变得更清楚。
- [[wiki/topics/Circuit Breaker|Circuit Breaker]] — Circuit Breaker 是分布式系统里的保护机制：当下游服务已经过载或不可用时，不再继续把请求打过去，而是主动快速失败，避免故障扩大。 (#distributed-systems #resilience #architecture)
- [[wiki/topics/Context Management|Context Management]] — Context management designs what enters, stays in, leaves, and stays stable in an AI agent's active context under finite attention and cache constraints. (#ai #agents #context)
- [[wiki/topics/Critical Thinking|Critical Thinking]] — 这页聚合的是《学会提问》这类材料中最稳定、最值得反复使用的批判性思维框架。 (#thinking #reasoning #methods)
- [[wiki/topics/European Antisemitism|European Antisemitism]] — 欧洲反犹主义之所以长期存在，不是因为犹太人有什么共同本质，而是因为他们在很多历史结构里反复处在一种容易被区分、被排斥、被掠夺、被甩锅的位置。它不是一条不变的偏见，而是一套会不断换语言的社会机制：中世纪更多借宗教敌意和制度隔离维持，近代更多借民族主义、经济焦虑和阴谋论升级，到了纳粹主义时期则被推进成国家机器。
- [[wiki/topics/Frontend Development|Frontend Development]] — Frontend development organizes user-interface behavior, state, rendering, and interaction into maintainable software. (#frontend #software #ui)
- [[wiki/topics/Frontend Development Workflow|Frontend Development Workflow]] — Frontend development workflow 不是一条把设计稿翻译成页面的生产线，而是一套持续对齐用户任务、界面行为与系统行为的工作方法。 (#frontend #software-engineering #workflow #ux)
- [[wiki/topics/Go Memory Model|Go Memory Model]] — Go Memory Model 的核心作用，是定义并发场景下内存操作之间的顺序约束，让我们能判断一个 goroutine 读取到的值在什么条件下是确定的。 (#golang #concurrency #memory-model)
- [[wiki/topics/High Concurrency|High Concurrency]] — 当前这篇旧笔记内容还很少，但主题本身值得先占位，因为它很可能会成为系统设计和性能治理的重要母页。 (#cs #concurrency #systems)
- [[wiki/topics/Karpathy Guidelines|Karpathy Guidelines]] — 这组 guideline 的核心目的是降低 LLM 写代码时常见的失误，尤其是：默认假设、过度设计、顺手大改、以及缺少可验证目标。 (#ai #coding #guidelines)
- [[wiki/topics/Learnable Structure in Data|Learnable Structure in Data]] — 评估数据价值时，一个更稳的起点，不是先问“这里有多少信息”，而是先问：对当前模型来说，这里到底有多少结构是可学习的。 (#ai #data #training #topic)
- [[wiki/topics/Learning Methodology|Learning Methodology]] — 一份自己能用、能指导动作的学习方法论。建立在两个概念之上：人是三通道进出系统；知识是网不是塔。
- [[wiki/topics/Limits of Classification|Limits of Classification]] — 它擅长把混乱切开，却不自动提供关系、过程、演化和反馈。很多理解错误，不是因为不会分类，而是因为 把分类工具误当成了世界本身 。
- [[wiki/topics/Mental Models|Mental Models]] — 这页聚合的是一组可以反复调用的思维工具，而不是某个单一学科知识点。 (#thinking #models #decision-making)
- [[wiki/topics/Methods of Classification|Methods of Classification]] — 分类方法的差异，本质上不是“分成几类”，而是 按什么维度切对象 。
- [[wiki/topics/Modern Software Engineering|Modern Software Engineering]] — 这页讨论的不是某一条具体方法流派的历史，而是一个更高层的方法论总纲：如何把软件开发理解为一种经验主义、证据驱动的问题求解活动。 (#software-engineering #methods)
- [[wiki/topics/Probability|Probability]] — 概率不只是一个数学章节名，也是一种处理不确定性的核心框架。 (#thinking #probability #judgment)
- [[wiki/topics/Problem Framing|Problem Framing]] — 这个定义虽然简单，但它迫使我们先把“预期”说清楚，而不是直接跳进解决方案。 (#thinking #problem-solving #methods)
- [[wiki/topics/Prompt Frequency|Prompt Frequency]] — 一个值得单独抽出来的判断是：在语义不变时，越接近训练语料中常见表达的 prompt，模型通常越容易发挥出能力。 (#ai #llm #prompting)
- [[wiki/topics/Requirement to Architecture Mapping|Requirement to Architecture Mapping]] — 这个主题页沉淀的是：如何把用户故事、PRD、free form requirement 先归一化，再稳定映射到分层架构。 (#architecture #requirements #mapping)
- [[wiki/topics/Resource Formula|Resource Formula]] — 当前笔记里的核心想法很短，但值得保留成一个主题种子： (#planning #resources #work)
- [[wiki/topics/Software Development Thought Lineage|Software Development Thought Lineage]] — 这页关心的核心问题，不是某一条具体方法怎么落地，也不是现代软件工程的总定义，而是：不同软件开发思想是如何在历史上一个接一个出现、彼此修正，并逐步形成今天这组主流方法栈的。 (#software-engineering #methodology #history #development)
- [[wiki/topics/Software Methodology|Software Methodology]] — 这里的'软件方法'，特指潘加宇《软件方法》所代表的那条建模与分析主线：不是先列功能，而是先锁定组织改进，再逐步收缩到系统边界，最后把责任落实到对象与代码。
- [[wiki/topics/Spec-Driven Development|Spec-Driven Development]] — Spec Driven Development（SDD）把'代码是真相、文档是附属品'这个长期默认假设倒置： 规约是合同，代码是合同的执行副本 。合同变了，执行副本重新生成；执行副本擅自改了，CI 让构建失败。AI coding assistant 这波新工具把这个老想法重新点燃——因为 LLM 是'擅长模式补全、不会读心'的队友，模糊的上下文被放大成灾难。 (#software-engineering #specs #ai-coding #process)
- [[wiki/topics/Technical Management|Technical Management]] — 这页聚合的是技术管理里比较稳定、可反复使用的判断，而不是具体某次团队事件。 (#management #leadership #engineering)
- [[wiki/topics/Testing Purpose|Testing Purpose]] — 测试的直接目的，不是追求某个表面指标，而是增加对代码正确性的信心。 (#testing #quality #software-engineering)
- [[wiki/topics/Testing Strategy|Testing Strategy]] — 从投入层次看：Test Pyramid 从测试目的看：Test Quadrants (#testing #quality #software-engineering)
- [[wiki/topics/Thinking in Systems|Thinking in Systems]] — 一本关于系统视角的入门书，但真正重要的不是术语，而是一个判断翻转： 问题反复出现，优先怀疑系统结构，而不是个体意志。
- [[wiki/topics/Tool Routing|Tool Routing]] — 当前笔记里关于 router / adapter 的判断，可以进一步抽成一个独立主题：工具路由不是附属细节，而是 agent 系统的核心结构设计。 (#ai #agents #tools)
- [[wiki/topics/UML Diagrams in Software Development|UML Diagrams in Software Development]] — UML 图不是一套必须全画的仪式，而是一组在不同开发环节回答不同问题的建模工具。
- [[wiki/topics/User Stories|User Stories]] — 用户故事的价值，不在于写出一个固定格式，而在于把“谁、想做什么、为什么”表达清楚，并让需求能继续往设计与实现层面流动。 (#product #requirements #software-engineering)
- [[wiki/topics/What Makes a Good Classification|What Makes a Good Classification]] — 好的分类，不是最整齐的分类，也不是看起来最像“标准答案”的分类，而是 最能支持理解、判断和行动的分类 。
- [[wiki/topics/面向对象分析与设计|面向对象分析与设计]] — 把面向对象分析与设计压到最少，背后真正撑住它的不是一长串术语，而是三根独立的力：责任、协作、抗变。

## Concepts
- [[wiki/concepts/Agent|Agent]] — Agent 的核心任务目前可以归纳为三件事： (#ai #agent #concept)
- [[wiki/concepts/Agent Tool|Agent Tool]] — 当前在旧笔记中， Agent tool 这个文件名和其中的内容发生了错位：文件里实际保留的是 think tool 摘录，而 router / adapter 这段内容出现在旧的 llm.md 中。 (#ai #agents #tools)
- [[wiki/concepts/Business Modeling in Software|Business Modeling in Software]] — 软件中的业务建模，不是先讨论'软件怎么做'，而是先回答：目标组织为了产出业务结果，现在是怎么运作的，应该怎么改。
- [[wiki/concepts/Cognition Three Channels|Cognition Three Channels]] — 人认识世界靠三根独立的生成器撑着。关掉任何一根，认识塌一块。
- [[wiki/concepts/Cognitive Engineering|Cognitive Engineering]] — 认知工程学不是单独研究'人怎么想'，而是研究如何设计工具、信息结构与反馈机制，让人更容易想对、做对、协同对。
- [[wiki/concepts/Component-Based Architecture|Component-Based Architecture]] — Component-based architecture organizes an interface or system as composable units with local responsibilities. (#frontend #architecture #modularity)
- [[wiki/concepts/Concept|Concept]] — 概念不是词，而是有限生命面对连续世界时制造的边界。
- [[wiki/concepts/Conceptual Integrity|Conceptual Integrity]] — 软件设计中的概念完整性，不是风格统一，而是一个系统里的所有部分都像从同一个头脑里长出来：用户、程序员、机器面对它时，都能感觉到这里面只有一套世界观。
- [[wiki/concepts/Context Information Density|Context Information Density]] — Context information density treats agent context quality as the ratio of decision-relevant signal to finite active context budget. (#ai #agents #context #memory)
- [[wiki/concepts/Cynefin Framework|Cynefin Framework]] — Cynefin Framework 适合用来判断问题处在哪种上下文里，再决定应该用什么动作模式，而不是先假定所有问题都能靠一种统一方法解决。 (#framework #decision-making #management)
- [[wiki/concepts/Declarative Programming|Declarative Programming]] — Declarative programming describes a target state or relation rather than spelling out each mutation step. (#frontend #programming #abstraction)
- [[wiki/concepts/Domain-Driven Design|Domain-Driven Design]] — DDD 不是一组面向对象技巧，也不是“把数据库表包装成实体类”。它更像一座折算器：先锁定软件要贴合的那段业务现实，再用共享语言和清晰边界，把这段现实压成可演化的软件结构。
- [[wiki/concepts/Economic Bubble|Economic Bubble]] — An economic bubble is not simply an expensive asset. It is a price structure where market value has detached from the real support beneath it, and continues rising mainly because people believe...
- [[wiki/concepts/Epiplexity|Epiplexity]] — Epiplexity 不是在问一份数据“总共有多少信息”，而是在问：对一个算力有限的观察者来说，这份数据里到底有多少结构是可提取、可学习、可压缩的。 (#ai #ml #concept #information-theory)
- [[wiki/concepts/Expression Three Channels|Expression Three Channels]] — 人向外表达，靠三根独立的生成器撑着。关掉任何一根，表达塌一块。
- [[wiki/concepts/Feedback Loops|Feedback Loops]] — 反馈回路是系统里“结果反过来影响原因”的闭环。
- [[wiki/concepts/Knowledge as Network|Knowledge as Network]] — 知识没有全局层级，只有局部的序。看起来像金字塔，其实是张网。
- [[wiki/concepts/KV Cache|KV Cache]] — KV cache stores transformer key/value tensors so repeated prefixes or generated histories do not need full attention recomputation. ( #ai #llm #inference #caching)
- [[wiki/concepts/Leverage Points|Leverage Points]] — 杠杆点是系统里“改一点，结果却变很多”的位置。
- [[wiki/concepts/LLM|LLM]] — 当前旧笔记里与 LLM 相关的两类判断混在了一起： (#ai #llm #concept)
- [[wiki/concepts/Prompt Caching|Prompt Caching]] — Prompt caching reuses stable prompt prefixes so repeated agent turns avoid recomputing the same system, tool, and context tokens. ( #ai #agents #context #caching)
- [[wiki/concepts/React|React]] — React is a frontend UI library centered on components, declarative rendering, and state-driven interface updates.
- [[wiki/concepts/Software Analysis Three Generators|Software Analysis Three Generators]] — 翻书架：需求工程、用例建模、领域驱动设计、事件风暴、用户故事地图、业务流程再造、数据流图、状态机、UML 九种图、C4 模型、ArchiMate、Use Case 2.0、Jobs to be Done……每一派都说自己抓到了本质，每一派都有一套词汇表、一套图、一套流程。新人进来第一个反应是：这些到底是同一件事的不同说法，还是真的在干不同的事？
- [[wiki/concepts/Software Design Three Generators|Software Design Three Generators]] — 软件设计这门学问，名词满天飞：SOLID、设计模式二十三种、DDD、六边形、洋葱、整洁架构、CQRS、事件溯源、依赖注入、分层、微服务、界限上下文、聚合根……但任何一个设计决定，最后都能归到三根独立的生成器里。
- [[wiki/concepts/State Management|State Management]] — State management controls where application state lives, how it changes, and how those changes propagate through the interface. (#frontend #architecture #state)

## Syntheses
- [[wiki/syntheses/Acting Under Complexity|Acting Under Complexity]] — 这页尝试把 Cynefin、决策模式、思考工作流、mental models、critical thinking 串成一个更高层的框架：当问题复杂、不确定、争议大时，关键不是只会分析，而是知道应该如何判断并继续行动。 (#synthesis #complexity #decision-making #thinking)
- [[wiki/syntheses/Agent System Design Space|Agent System Design Space]] — Agent System Design Space compares agent architectures by values, context, tools, permissions, memory, delegation, recovery, and cache economics. (#synthesis #ai #agents #architecture)
- [[wiki/syntheses/AI Engineering Workflow|AI Engineering Workflow]] — AI Engineering Workflow connects agent mental models, workflow control, tool design, coding constraints, and requirement normalization. (#synthesis #ai #agents #workflow)
- [[wiki/syntheses/Business Analysis to Software Design|Business Analysis to Software Design]] — Synthesis of how business modeling and software analysis become software design through domain boundaries and shared models. (#software-methodology #analysis #design)
- [[wiki/syntheses/Decision Modes for Engineering Work|Decision Modes for Engineering Work]] — 这页尝试把管理、问题判断和软件工程方法连成一个更高层的操作框架：面对不同类型的问题，团队不该只换答案，更要换决策模式。 (#synthesis #decision-making #management #engineering)
- [[wiki/syntheses/From User Story to Architecture|From User Story to Architecture]] — 这页综合的不是单一技巧，而是一条完整路径：需求如何从业务表达，一路变成可以实现、可以验证、可以维护的架构决策。 (#synthesis #requirements #architecture #software-engineering)
- [[wiki/syntheses/Learning Methodology Across Sources|Learning Methodology Across Sources]] — 把 wiki 里散落在不同笔记中的学习相关结论，按 Learning Methodology 的七条原则做一次对齐。目的：看清楚哪些原则已经被多个独立来源印证、哪些还只是一家之言、哪些源之间有冲突需要再想。
- [[wiki/syntheses/React UI Organization Model|React UI Organization Model]] — Synthesis of React as a UI organization model combining declarative rendering, components, and state management. (#frontend #react #ui)
- [[wiki/syntheses/Thinking and Judgment Workflow|Thinking and Judgment Workflow]] — 这页把 Mental Models 、 Critical Thinking 、 Problem Framing 串成一条更完整的思考路径：面对复杂问题时，不只是要会想，还要知道先怎么定义问题、再怎么观察、最后怎么判断。 (#synthesis #thinking #reasoning #methods)
- [[wiki/syntheses/不确定性下的判断|不确定性下的判断]] — 这页尝试把 Problem Framing 、 Mental Models 、 Probability 、 Critical Thinking 串成一个更高层的判断框架：很多真正重要的决策，并不是在确定条件下做出的，而是在信息不全、对象不稳、反馈滞后时被迫推进的。 (#synthesis #thinking #judgment #decision-making)

## Sources
- [[wiki/sources/Agent Engineering Source Guide|Agent Engineering Source Guide]] — 这页用于收拢“agent engineering / harness / workflow”这一类更偏工程综述与系统实践的来源材料。 (#source #ai #agents #engineering #harness)
- [[wiki/sources/Agent Harness Qiaomu Article Source Guide|Agent Harness Qiaomu Article Source Guide]] — 这篇文章目前更适合作为一个 source facing note 进入当前仓库，而不是直接升格成稳定 topic 页。 (#article #blog #ai #agents #harness #source)
- [[wiki/sources/Agent Systems Papers Source Guide|Agent Systems Papers Source Guide]] — Source guide collecting agent-system papers and deciding which claims should stay source-level versus move into topics and syntheses. (#papers #agents #ai #source)
- [[wiki/sources/AI Coding Control Limits Source Guide|AI Coding Control Limits Source Guide]] — 这篇文章更适合作为一个 source facing note 进入当前仓库，而不是直接承担稳定 topic 页角色。 (#ai-coding #software-engineering #source #complexity #productivity #security)
- [[wiki/sources/Before the Tool Call Source Guide|Before the Tool Call Source Guide]] — 这篇 arXiv 论文更适合作为单篇 source facing note 进入当前仓库，而不是直接升格成稳定 topic 页。 (#paper #arxiv #agents #authorization #security #source)
- [[wiki/sources/Dive into Claude Code Source Guide|Dive into Claude Code Source Guide]] — 这篇 arXiv 论文更适合作为一个 source facing note 进入当前仓库，而不是直接升格成稳定 wiki 母页。 (#paper #arxiv #agents #ai #harness #source)
- [[wiki/sources/Epiplexity Paper Notes|Epiplexity Paper Notes]] — 这页保留论文 From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence 的阅读笔记，并作为 Epiplexity 的来源层。 (#paper #ai #information-theory #source)
- [[wiki/sources/Frontend Development Workflow Roundtable Source Guide|Frontend Development Workflow Roundtable Source Guide]] — 这份圆桌更适合作为一个 source facing note 进入当前仓库，而不是直接承担前端工程方法论的稳定母页角色。 (#frontend #software-engineering #workflow #ux #source #roundtable)
- [[wiki/sources/GenericAgent Paper Source Guide|GenericAgent Paper Source Guide]] — Source guide for the GenericAgent paper, focused on context information density, hierarchical memory, tool minimality, and self-evolution. (#papers #agents #ai #source)
- [[wiki/sources/Journals|Journals Source Guide]] — journals/ 是当前 vault 的时间流输入层。它们不应直接承担稳定知识页职责，但应该持续为 wiki/ 提供可回溯的来源。 (#journals #raw #source)
- [[wiki/sources/LLM Reasoning Is Latent, Not the Chain of Thought Source Guide|LLM Reasoning Is Latent, Not the Chain of Thought Source Guide]] — 这篇 arXiv 论文更适合作为一个 source facing note 进入当前仓库，而不是直接升格成稳定 wiki 母页。 (#paper #arxiv #reasoning #llm #source)
- [[wiki/sources/Managed Agents Source Guide|Managed Agents Source Guide]] — 这篇 Anthropic engineering article 更适合作为一个 source facing note 进入当前仓库，而不是直接升格成稳定 wiki 母页。 (#agents #ai #harness #source #anthropic)
- [[wiki/sources/Mobu Notes|Mobu Notes Source Guide]] — mobu/ 目前是个人知识与领域素材的大池子，适合作为 raw/domain input 层，而不是直接作为稳定 wiki 层。 (#mobu #raw #source)
- [[wiki/sources/Modern Software Engineering Notes|Modern Software Engineering Notes]] — 这份读书笔记目前以摘录和图片为主，仍更适合作为 source note，而不是直接升格为稳定 wiki 页面。 (#book-notes #software-engineering #source)
- [[wiki/sources/Probability Roundtable Source Guide|Probability Roundtable Source Guide]] — 这份圆桌更适合作为一个 source facing note 进入当前仓库，而不是直接承担概率论的稳定母页角色。 (#probability #thinking #roundtable #source)
- [[wiki/sources/Prompt Caching Claude Code Case Study Source Guide|Prompt Caching Claude Code Case Study Source Guide]] — Source guide for a prompt-caching case study that frames Claude Code cache efficiency as an agent harness design problem. ( #source #ai #agents #caching #claude-code)
- [[wiki/sources/Published Posts|Published Posts Source Guide]] — content/posts/ 是对外发布层，不直接等同于 wiki 本体。 (#hugo #posts #source)
- [[wiki/sources/Qiaomu Best Prompt Source Guide|Qiaomu Best Prompt Source Guide]] — 这篇文章当前更适合作为一个 source facing note 进入当前仓库，而不是直接升格成稳定母页。 (#article #blog #ai #llm #prompting #source)
- [[wiki/sources/React Framework Background and Core Concepts Source Guide|React Framework Background and Core Concepts Source Guide]] — 这篇材料更适合作为 React 入门理解的 source facing note，而不是直接承担前端体系中的稳定概念母页。 (#react #frontend #web #ui #source)
- [[wiki/sources/Software Methodology by Pan Jianyu|Software Methodology by Pan Jianyu]] — 这页收纳《软件方法》相关的阅读入口与当前已经稳定下来的判断。
- [[wiki/sources/Spec-Driven Development Paper Source Guide|Spec-Driven Development Paper Source Guide]] — 这篇论文是 Deepak Babu Piskala 投稿 AIWare 2026 的 practitioner guide，把 SDD 这波被 AI coding assistant 重新点燃的旧想法梳理成三档光谱 + 四阶段流水线 + 决策框架。8 页，3 张图，零量化实验。 (#software-engineering #specs #ai-coding #paper)
- [[wiki/sources/Theory Is All You Need Source Guide|Theory Is All You Need Source Guide]] — 这页保留 Teppo Felin 与 Matthias Holweg 的论文 Theory Is All You Need: AI, Human Cognition, and Causal Reasoning 的阅读导览。 (#paper #ai #cognition #causal-reasoning #source)

## Meta
- [[wiki/hot|Hot Cache]] — Ingested a Claude Code prompt-caching case study: added Prompt Caching and KV Cache concepts and connected cache stability to context and harness design.
- [[wiki/log|LLM Wiki Log]] — 建立 wiki/ 作为稳定知识层入口。 明确目标结构： raw/ 为原始材料层， wiki/ 为复利知识层。 首批试点选择 AI / Agent 知识簇。 保留 pages/ 、 journals/ 、 mobu/ 、 content/posts/ 作为迁移来源。 (#llm-wiki #log)
- [[wiki/NAMING|NAMING]] — 这份文档规定 wiki/ 下笔记的命名和放置规则。
- [[wiki/README|README]] — This directory is the stable knowledge layer of the vault.
- [[wiki/Welcome|Welcome (legacy)]] — 这是历史遗留的 Obsidian 默认欢迎页，不再作为这个仓库的首页使用。
