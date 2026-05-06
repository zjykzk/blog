---
title: Wiki Home
category: maps
tags:
  - llm-wiki
sources: []
created: 2026-05-04
updated: 2026-05-06T21:40:37+08:00
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
- [[wiki/maps/Learning Map|Learning Map]] — Learning Map collects learning methodology, cognition concepts, AI tutor loops, and cross-source synthesis for durable learning practice.
- [[wiki/maps/Management Map|Management Map]] — 这页聚合当前 vault 中与管理、决策、组织协作相关的长期知识页。 (#management #leadership #map)
- [[wiki/maps/Reading Map|Reading Map]] — 这页用于承接读书笔记从 raw/source 进入 wiki 的提升过程。 (#reading #books #map)
- [[wiki/maps/Software Analysis Map|Software Analysis Map]] — 这页把软件分析中的核心概念按层次放在一张图里。它基于 Software Analysis Three Generators 的三根： 组织、交换、边界 。 (#software-analysis #requirements #architecture #map)
- [[wiki/maps/Software Design Map|Software Design Map]] — 这页把软件设计中的核心概念按层次放在一张图里。关键区分是： (#software-design #architecture #map)

## Topics
- [[wiki/topics/AI Harness|AI Harness]] — AI Harness is the runtime order layer that connects model, context, tools, permissions, state, recovery, and cache-stable capability loading into a controllable agent system. (#ai #agents #harness #runtime)
- [[wiki/topics/AI Memory|AI Memory]] — AI Memory is the persistent state layer that lets agents retain, retrieve, update, and consolidate experience beyond a single context window. (#ai #agents #memory #context)
- [[wiki/topics/AI Skills Workflow|AI Skills Workflow]] — AI Skills Workflow treats skills as reusable workflows that gather, order, persist, and reload context for more stable agent behavior. (#ai #skills #workflow)
- [[wiki/topics/BoltDB Internals|BoltDB Internals]] — BoltDB 是一个非常适合入门数据库实现的案例：代码量相对小，但已经覆盖了页式存储、B+ 树、事务、空闲页管理、写时复制等核心机制。 (#database #storage #golang)
- [[wiki/topics/Categorical Thinking|Categorical Thinking]] — 分类思维，是先找一个划分维度，再按这个维度把混乱切成几类，从而让理解、判断和行动变得更清楚。
- [[wiki/topics/Circuit Breaker|Circuit Breaker]] — Circuit Breaker 是分布式系统里的保护机制：当下游服务已经过载或不可用时，不再继续把请求打过去，而是主动快速失败，避免故障扩大。 (#distributed-systems #resilience #architecture)
- [[wiki/topics/Context Management|Context Management]] — Context management designs what enters, stays in, leaves, and stays stable in an AI agent's active context under finite attention, ordering, and cache constraints. (#ai #agents #context)
- [[wiki/topics/Critical Thinking|Critical Thinking]] — 这页聚合的是《学会提问》这类材料中最稳定、最值得反复使用的批判性思维框架。 (#thinking #reasoning #methods)
- [[wiki/topics/European Antisemitism|European Antisemitism]] — 欧洲反犹主义之所以长期存在，不是因为犹太人有什么共同本质，而是因为他们在很多历史结构里反复处在一种容易被区分、被排斥、被掠夺、被甩锅的位置。它不是一条不变的偏见，而是一套会不断换语言的社会机制：中世纪更多借宗教敌意和制度隔离维持，近代更多借民族主义、经济焦虑和阴谋论升级，到了纳粹主义时期则被推进成国家机器。
- [[wiki/topics/Frontend Development|Frontend Development]] — Frontend development organizes user-interface behavior, state, rendering, and interaction into maintainable software. (#frontend #software #ui)
- [[wiki/topics/Frontend Development Workflow|Frontend Development Workflow]] — Frontend development workflow 不是一条把设计稿翻译成页面的生产线，而是一套持续对齐用户任务、界面行为与系统行为的工作方法。 (#frontend #software-engineering #workflow #ux)
- [[wiki/topics/Go Memory Model|Go Memory Model]] — Go Memory Model 的核心作用，是定义并发场景下内存操作之间的顺序约束，让我们能判断一个 goroutine 读取到的值在什么条件下是确定的。 (#golang #concurrency #memory-model)
- [[wiki/topics/High Concurrency|High Concurrency]] — 当前这篇旧笔记内容还很少，但主题本身值得先占位，因为它很可能会成为系统设计和性能治理的重要母页。 (#cs #concurrency #systems)
- [[wiki/topics/Judgment Under Leverage|Judgment Under Leverage]] — Judgment under leverage is the problem of making decisions whose consequences are amplified by capital, labor, code, or media. ( #judgment #leverage #wealth #decision-making)
- [[wiki/topics/Karpathy Guidelines|Karpathy Guidelines]] — Karpathy Guidelines are coding constraints that reduce common LLM mistakes such as hidden assumptions, over-design, broad edits, and missing verification. (#ai #coding #guidelines)
- [[wiki/topics/Learnable Structure in Data|Learnable Structure in Data]] — 评估数据价值时，一个更稳的起点，不是先问“这里有多少信息”，而是先问：对当前模型来说，这里到底有多少结构是可学习的。 (#ai #data #training #topic)
- [[wiki/topics/LLM Inference Systems|LLM Inference Systems]] — LLM inference systems coordinate scheduling, KV cache memory, model execution, serving, scaling, and benchmarking to return tokens efficiently. (#ai #llm #inference #systems)
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
- [[wiki/topics/Spec-Driven Development|Spec-Driven Development]] — Spec-Driven Development treats specs as contracts that guide implementation, validation, and AI coding work before code becomes the default truth. (#software-engineering #specs #ai-coding #process)
- [[wiki/topics/Technical Management|Technical Management]] — 这页聚合的是技术管理里比较稳定、可反复使用的判断，而不是具体某次团队事件。 (#management #leadership #engineering)
- [[wiki/topics/Testing Purpose|Testing Purpose]] — 测试的直接目的，不是追求某个表面指标，而是增加对代码正确性的信心。 (#testing #quality #software-engineering)
- [[wiki/topics/Testing Strategy|Testing Strategy]] — Testing Strategy combines test layering, test purpose, and AI-era quality gates to increase confidence in software changes. (#testing #quality #software-engineering)
- [[wiki/topics/Thinking in Systems|Thinking in Systems]] — 一本关于系统视角的入门书，但真正重要的不是术语，而是一个判断翻转： 问题反复出现，优先怀疑系统结构，而不是个体意志。
- [[wiki/topics/Tool Routing|Tool Routing]] — 当前笔记里关于 router / adapter 的判断，可以进一步抽成一个独立主题：工具路由不是附属细节，而是 agent 系统的核心结构设计。 (#ai #agents #tools)
- [[wiki/topics/UML Diagrams in Software Development|UML Diagrams in Software Development]] — UML 图不是一套必须全画的仪式，而是一组在不同开发环节回答不同问题的建模工具。
- [[wiki/topics/User Stories|User Stories]] — 用户故事的价值，不在于写出一个固定格式，而在于把“谁、想做什么、为什么”表达清楚，并让需求能继续往设计与实现层面流动。 (#product #requirements #software-engineering)
- [[wiki/topics/What Makes a Good Classification|What Makes a Good Classification]] — 好的分类，不是最整齐的分类，也不是看起来最像“标准答案”的分类，而是 最能支持理解、判断和行动的分类 。
- [[wiki/topics/Wealth Creation|Wealth Creation]] — Wealth creation means owning scalable assets that give society what it wants, rather than renting time for money or playing status games. ( #wealth #business #leverage #career)
- [[wiki/topics/面向对象分析与设计|面向对象分析与设计]] — 把面向对象分析与设计压到最少，背后真正撑住它的不是一长串术语，而是三根独立的力：责任、协作、抗变。

## Concepts
- [[wiki/concepts/Accountability|Accountability]] — Accountability means taking public, name-attached risk so society can route responsibility, equity, and leverage toward you. ( #wealth #responsibility #judgment #career)
- [[wiki/concepts/Agent|Agent]] — Agent 的核心任务目前可以归纳为三件事： (#ai #agent #concept)
- [[wiki/concepts/Agent Action Space|Agent Action Space]] — Agent Action Space is the set of actions an agent can perceive, choose, compose, and execute through tools, skills, subagents, and harness policy. (#ai #agents #tools #harness)
- [[wiki/concepts/Agent Skill|Agent Skill]] — Agent Skill is a reusable capability bundle that can combine instructions, references, scripts, assets, memory, and hooks for agent work. (#ai #agents #skills #workflow)
- [[wiki/concepts/Agent Tool|Agent Tool]] — Agent tools are schema-defined action surfaces that let an agent inspect, change, retrieve, or validate external state under harness control. (#ai #agents #tools)
- [[wiki/concepts/AI Collaboration Scaffolding|AI Collaboration Scaffolding]] — AI collaboration scaffolding gives coding assistants onboarding context, design discussion, standards, anchors, and feedback loops so their output fits the team. (#ai #software-engineering #workflow #ai-coding)
- [[wiki/concepts/Application|Application]] — Application is the fit-process that lets abstract knowledge, tools, or methods become effective in a concrete situation. (#thinking #concepts #practice)
- [[wiki/concepts/Knowledge Priming|Knowledge Priming]] — Knowledge priming gives AI coding assistants curated, versioned project context before generation so they fit local architecture and conventions. (#ai #ai-coding #context #workflow)
- [[wiki/concepts/Design-First Collaboration|Design-First Collaboration]] — Design-first collaboration makes AI design decisions explicit through staged alignment before any implementation code is generated. (#ai #ai-coding #software-engineering #workflow)
- [[wiki/concepts/Context Anchoring|Context Anchoring]] — Context anchoring preserves feature-level AI collaboration decisions in a living document outside the chat session. (#ai #ai-coding #context #workflow)
- [[wiki/concepts/Encoding Team Standards|Encoding Team Standards]] — Encoding team standards turns tacit engineering judgment into versioned AI instructions that execute consistently across the team. (#ai #ai-coding #software-engineering #workflow)
- [[wiki/concepts/Feedback Flywheel|Feedback Flywheel]] — Feedback flywheel turns AI collaboration experience into updated context, standards, workflows, and guardrails. (#ai #ai-coding #feedback #workflow)
- [[wiki/concepts/AI Memory 4W Taxonomy|AI Memory 4W Taxonomy]] — The AI Memory 4W Taxonomy classifies memory by when it persists, what it stores, how it is represented, and which modalities it handles. (#ai #memory #taxonomy #agents)
- [[wiki/concepts/AI Learning Tutor Loop|AI Learning Tutor Loop]] — AI Learning Tutor Loop uses a source-grounded AI system to map a field, expose disagreements, test understanding, and repair errors. ( #ai #learning #tutoring #questions)
- [[wiki/concepts/Analogy-Making|Analogy-Making]] — Analogy-making is the cognitive act of understanding a new situation by mapping it onto familiar structures. (#cognition #concepts #thinking)
- [[wiki/concepts/Analysis|Analysis]] — Analysis opens a whole along its own structure, identifies parts and relations, then recomposes them into actionable understanding. (#thinking #concepts #reasoning)
- [[wiki/concepts/Business Modeling in Software|Business Modeling in Software]] — 软件中的业务建模，不是先讨论'软件怎么做'，而是先回答：目标组织为了产出业务结果，现在是怎么运作的，应该怎么改。
- [[wiki/concepts/Cognition Three Channels|Cognition Three Channels]] — 人认识世界靠三根独立的生成器撑着。关掉任何一根，认识塌一块。
- [[wiki/concepts/Cognitive Engineering|Cognitive Engineering]] — 认知工程学不是单独研究'人怎么想'，而是研究如何设计工具、信息结构与反馈机制，让人更容易想对、做对、协同对。
- [[wiki/concepts/Component-Based Architecture|Component-Based Architecture]] — Component-based architecture organizes an interface or system as composable units with local responsibilities. (#frontend #architecture #modularity)
- [[wiki/concepts/Concept|Concept]] — 概念不是词，而是有限生命面对连续世界时制造的边界。
- [[wiki/concepts/Conceptual Integrity|Conceptual Integrity]] — 软件设计中的概念完整性，不是风格统一，而是一个系统里的所有部分都像从同一个头脑里长出来：用户、程序员、机器面对它时，都能感觉到这里面只有一套世界观。
- [[wiki/concepts/Creation|Creation]] — Creation is the act of breaking an old structure and recombining materials into a new order that can be used, understood, or continued. (#thinking #concepts #practice)
- [[wiki/concepts/Continuous Batching|Continuous Batching]] — Continuous batching lets an inference engine mix newly arrived and already-running requests at each generation step. (#ai #llm #inference #scheduling)
- [[wiki/concepts/Context Information Density|Context Information Density]] — Context information density treats agent context quality as the ratio of decision-relevant signal to finite active context budget. (#ai #agents #context #memory)
- [[wiki/concepts/Cynefin Framework|Cynefin Framework]] — Cynefin Framework 适合用来判断问题处在哪种上下文里，再决定应该用什么动作模式，而不是先假定所有问题都能靠一种统一方法解决。 (#framework #decision-making #management)
- [[wiki/concepts/Declarative Programming|Declarative Programming]] — Declarative programming describes a target state or relation rather than spelling out each mutation step. (#frontend #programming #abstraction)
- [[wiki/concepts/Domain-Driven Design|Domain-Driven Design]] — DDD 不是一组面向对象技巧，也不是“把数据库表包装成实体类”。它更像一座折算器：先锁定软件要贴合的那段业务现实，再用共享语言和清晰边界，把这段现实压成可演化的软件结构。
- [[wiki/concepts/Economic Bubble|Economic Bubble]] — An economic bubble is not simply an expensive asset. It is a price structure where market value has detached from the real support beneath it, and continues rising mainly because people believe...
- [[wiki/concepts/Epiplexity|Epiplexity]] — Epiplexity 不是在问一份数据“总共有多少信息”，而是在问：对一个算力有限的观察者来说，这份数据里到底有多少结构是可提取、可学习、可压缩的。 (#ai #ml #concept #information-theory)
- [[wiki/concepts/Evaluation|Evaluation]] — Evaluation is the act of placing an object inside a scale so its value, quality, meaning, or position can appear. (#thinking #concepts #judgment)
- [[wiki/concepts/Expression Three Channels|Expression Three Channels]] — 人向外表达，靠三根独立的生成器撑着。关掉任何一根，表达塌一块。
- [[wiki/concepts/Feedback Loops|Feedback Loops]] — Feedback loops are system structures where results flow back to influence future causes, creating growth, stability, or oscillation.
- [[wiki/concepts/Harness Ratchet|Harness Ratchet]] — A harness ratchet turns repeated agent failures into durable rules, hooks, checks, or workflow changes instead of treating them as one-off bad runs. (#ai #agents #harness #feedback)
- [[wiki/concepts/Knowledge as Network|Knowledge as Network]] — 知识没有全局层级，只有局部的序。看起来像金字塔，其实是张网。
- [[wiki/concepts/Knowledge Types|Knowledge Types]] — 知识类型按知识在人脑和行动中的功能划分；布卢姆分类则描述对知识的掌握深度。 (#cognition #learning #concepts #taxonomy)
- [[wiki/concepts/KV Cache|KV Cache]] — KV cache stores transformer key/value tensors so repeated prefixes or generated histories do not need full attention recomputation. ( #ai #llm #inference #caching)
- [[wiki/concepts/Leverage Points|Leverage Points]] — 杠杆点是系统里“改一点，结果却变很多”的位置。
- [[wiki/concepts/LLM Inference Benchmarking|LLM Inference Benchmarking]] — LLM inference benchmarking compares latency, throughput, and goodput under request shapes and service-level objectives. (#ai #llm #inference #benchmarking)
- [[wiki/concepts/LLM|LLM]] — 当前旧笔记里与 LLM 相关的两类判断混在了一起： (#ai #llm #concept)
- [[wiki/concepts/Lost in the Middle Effect|Lost in the Middle Effect]] — The lost-in-the-middle effect is the long-context failure mode where models use information best at the beginning or end and worse in the middle. (#ai #llm #context #evaluation)
- [[wiki/concepts/Paged Attention|Paged Attention]] — Paged attention stores KV cache in fixed-size blocks so inference servers can allocate, reuse, and evict attention state efficiently. (#ai #llm #inference #memory)
- [[wiki/concepts/Prefill Decode Split|Prefill Decode Split]] — The prefill/decode split separates full-prompt processing from token-by-token generation because they stress GPU systems differently. (#ai #llm #inference #serving)
- [[wiki/concepts/Prompt Caching|Prompt Caching]] — Prompt caching reuses stable prompt prefixes so repeated agent turns avoid recomputing the same system, tool, and context tokens. ( #ai #agents #context #caching)
- [[wiki/concepts/Permissionless Leverage|Permissionless Leverage]] — Permissionless leverage uses code and media to multiply judgment without needing capital approval or labor hierarchy. ( #wealth #leverage #internet #media)
- [[wiki/concepts/React|React]] — React is a frontend UI library centered on components, declarative rendering, and state-driven interface updates.
- [[wiki/concepts/Software Analysis Three Generators|Software Analysis Three Generators]] — 翻书架：需求工程、用例建模、领域驱动设计、事件风暴、用户故事地图、业务流程再造、数据流图、状态机、UML 九种图、C4 模型、ArchiMate、Use Case 2.0、Jobs to be Done……每一派都说自己抓到了本质，每一派都有一套词汇表、一套图、一套流程。新人进来第一个反应是：这些到底是同一件事的不同说法，还是真的在干不同的事？
- [[wiki/concepts/Software Design Three Generators|Software Design Three Generators]] — 软件设计这门学问，名词满天飞：SOLID、设计模式二十三种、DDD、六边形、洋葱、整洁架构、CQRS、事件溯源、依赖注入、分层、微服务、界限上下文、聚合根……但任何一个设计决定，最后都能归到三根独立的生成器里。
- [[wiki/concepts/Speculative Decoding|Speculative Decoding]] — Speculative decoding proposes multiple cheap draft tokens and verifies them with the large model to reduce expensive decoding steps. (#ai #llm #inference #decoding)
- [[wiki/concepts/Specific Knowledge|Specific Knowledge]] — Specific knowledge is hard-to-train knowledge built from genuine curiosity, practice, and creative or technical edge. ( #wealth #learning #skill #judgment)
- [[wiki/concepts/State Management|State Management]] — State management controls where application state lives, how it changes, and how those changes propagate through the interface. (#frontend #architecture #state)
- [[wiki/concepts/Understanding|Understanding]] — 理解不是拥有一句定义，而是在脑中形成一团可横向类比、纵向抽象、并能被重新创造的概念云。 (#cognition #learning #concepts)
- [[wiki/concepts/Verification Loop|Verification Loop]] — A verification loop gives an agent external feedback, such as tests, visual checks, or evaluators, so errors are caught before they compound. (#ai #agents #verification)

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
- [[wiki/sources/Agent Harness Anatomy Source Guide|Agent Harness Anatomy Source Guide]] — Source guide for Akshay Pachaar's agent harness thread, focused on the 12-component harness model and architecture decisions. (#source #ai #agents #harness #architecture)
- [[wiki/sources/Agent Harness Engineering Source Guide|Agent Harness Engineering Source Guide]] — Source guide for Addy Osmani's Agent Harness Engineering article, focused on harnesses as configurable runtime systems that improve through failures. (#source #ai #agents #harness #engineering)
- [[wiki/sources/Agent Harness Qiaomu Article Source Guide|Agent Harness Qiaomu Article Source Guide]] — 这篇文章目前更适合作为一个 source facing note 进入当前仓库，而不是直接升格成稳定 topic 页。 (#article #blog #ai #agents #harness #source)
- [[wiki/sources/Agent Systems Papers Source Guide|Agent Systems Papers Source Guide]] — Source guide collecting agent-system papers and deciding which claims should stay source-level versus move into topics and syntheses. (#papers #agents #ai #source)
- [[wiki/sources/AI Coding Control Limits Source Guide|AI Coding Control Limits Source Guide]] — 这篇文章更适合作为一个 source facing note 进入当前仓库，而不是直接承担稳定 topic 页角色。 (#ai-coding #software-engineering #source #complexity #productivity #security)
- [[wiki/sources/AI Memory Survey Source Guide|AI Memory Survey Source Guide]] — Source guide for Survey on AI Memory, focused on memory theory, the 4W taxonomy, single/multi-agent memory, evaluation, and open challenges. (#paper #ai #agents #memory #survey)
- [[wiki/sources/Analysis Concept Anatomy Source Guide|Analysis Concept Anatomy Source Guide]] — Source guide for the ljg-learn concept anatomy note on analysis as reversible decomposition into actionable structure. (#source #thinking #concepts)
- [[wiki/sources/Application Concept Anatomy Source Guide|Application Concept Anatomy Source Guide]] — Source guide for the ljg-learn concept anatomy note on application as contextual fit turning abstraction into effect. (#source #thinking #concepts)
- [[wiki/sources/Before the Tool Call Source Guide|Before the Tool Call Source Guide]] — 这篇 arXiv 论文更适合作为单篇 source facing note 进入当前仓库，而不是直接升格成稳定 topic 页。 (#paper #arxiv #agents #authorization #security #source)
- [[wiki/sources/Claude Code Skills Source Guide|Claude Code Skills Source Guide]] — Source guide for Thariq Shihipar's Claude Code skills article, focused on skills as capability bundles, categories, gotchas, disclosure, hooks, and distribution. (#source #ai #agents #skills #claude-code)
- [[wiki/sources/Creation Concept Anatomy Source Guide|Creation Concept Anatomy Source Guide]] — Source guide for the ljg-learn concept anatomy note on creation as difference entering durable order. (#source #thinking #concepts)
- [[wiki/sources/Dive into Claude Code Source Guide|Dive into Claude Code Source Guide]] — 这篇 arXiv 论文更适合作为一个 source facing note 进入当前仓库，而不是直接升格成稳定 wiki 母页。 (#paper #arxiv #agents #ai #harness #source)
- [[wiki/sources/Epiplexity Paper Notes|Epiplexity Paper Notes]] — 这页保留论文 From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence 的阅读笔记，并作为 Epiplexity 的来源层。 (#paper #ai #information-theory #source)
- [[wiki/sources/Evaluation Concept Anatomy Source Guide|Evaluation Concept Anatomy Source Guide]] — Source guide for the ljg-learn concept anatomy note on evaluation as scale-shaped value judgment. (#source #thinking #concepts)
- [[wiki/sources/Frontend Development Workflow Roundtable Source Guide|Frontend Development Workflow Roundtable Source Guide]] — 这份圆桌更适合作为一个 source facing note 进入当前仓库，而不是直接承担前端工程方法论的稳定母页角色。 (#frontend #software-engineering #workflow #ux #source #roundtable)
- [[wiki/sources/GenericAgent Paper Source Guide|GenericAgent Paper Source Guide]] — Source guide for the GenericAgent paper, focused on context information density, hierarchical memory, tool minimality, and self-evolution. (#papers #agents #ai #source)
- [[wiki/sources/How to Get Rich Source Guide|How to Get Rich Source Guide]] — Source guide for Naval Ravikant's How to Get Rich tweetstorm PDF, focused on wealth, equity, specific knowledge, accountability, leverage, and judgment. ( #source #wealth #leverage #career #judgment)
- [[wiki/sources/Journals|Journals Source Guide]] — journals/ 是当前 vault 的时间流输入层。它们不应直接承担稳定知识页职责，但应该持续为 wiki/ 提供可回溯的来源。 (#journals #raw #source)
- [[wiki/sources/LLM Reasoning Is Latent, Not the Chain of Thought Source Guide|LLM Reasoning Is Latent, Not the Chain of Thought Source Guide]] — 这篇 arXiv 论文更适合作为一个 source facing note 进入当前仓库，而不是直接升格成稳定 wiki 母页。 (#paper #arxiv #reasoning #llm #source)
- [[wiki/sources/Lost in the Middle Paper Source Guide|Lost in the Middle Paper Source Guide]] — Source guide for the Lost in the Middle paper, focused on long-context positional bias and evaluation protocols for usable context. (#paper #ai #llm #context #evaluation)
- [[wiki/sources/Managed Agents Source Guide|Managed Agents Source Guide]] — 这篇 Anthropic engineering article 更适合作为一个 source facing note 进入当前仓库，而不是直接升格成稳定 wiki 母页。 (#agents #ai #harness #source #anthropic)
- [[wiki/sources/Mobu Notes|Mobu Notes Source Guide]] — mobu/ 目前是个人知识与领域素材的大池子，适合作为 raw/domain input 层，而不是直接作为稳定 wiki 层。 (#mobu #raw #source)
- [[wiki/sources/Modern Software Engineering Notes|Modern Software Engineering Notes]] — 这份读书笔记目前以摘录和图片为主，仍更适合作为 source note，而不是直接升格为稳定 wiki 页面。 (#book-notes #software-engineering #source)
- [[wiki/sources/NotebookLM Learning Workflow Source Guide|NotebookLM Learning Workflow Source Guide]] — Source guide for Ihtesham Ali's NotebookLM learning workflow thread: corpus loading, mental-model prompts, disagreement mapping, and diagnostic feedback. ( #source #ai #learning #notebooklm #questions)
- [[wiki/sources/Probability Roundtable Source Guide|Probability Roundtable Source Guide]] — 这份圆桌更适合作为一个 source facing note 进入当前仓库，而不是直接承担概率论的稳定母页角色。 (#probability #thinking #roundtable #source)
- [[wiki/sources/Prompt Caching Claude Code Case Study Source Guide|Prompt Caching Claude Code Case Study Source Guide]] — Source guide for prompt-caching case studies that frame Claude Code cache efficiency as an agent harness design problem. ( #source #ai #agents #caching #claude-code)
- [[wiki/sources/Published Posts|Published Posts Source Guide]] — content/posts/ 是对外发布层，不直接等同于 wiki 本体。 (#hugo #posts #source)
- [[wiki/sources/Qiaomu Best Prompt Source Guide|Qiaomu Best Prompt Source Guide]] — 这篇文章当前更适合作为一个 source facing note 进入当前仓库，而不是直接升格成稳定母页。 (#article #blog #ai #llm #prompting #source)
- [[wiki/sources/React Framework Background and Core Concepts Source Guide|React Framework Background and Core Concepts Source Guide]] — 这篇材料更适合作为 React 入门理解的 source facing note，而不是直接承担前端体系中的稳定概念母页。 (#react #frontend #web #ui #source)
- [[wiki/sources/Reducing Friction in AI-Assisted Development Source Guide|Reducing Friction in AI-Assisted Development Source Guide]] — Source guide for Rahul Garg's Martin Fowler article on five patterns for reducing friction in AI-assisted development. (#source #ai-coding #software-engineering #workflow #collaboration)
- [[wiki/sources/Seeing Like an Agent Source Guide|Seeing Like an Agent Source Guide]] — Source guide for Thariq Shihipar's Claude Code article on action-space design, tool iteration, elicitation, task coordination, search, and progressive disclosure. (#source #ai #agents #tools #claude-code)
- [[wiki/sources/Software Methodology by Pan Jianyu|Software Methodology by Pan Jianyu]] — 这页收纳《软件方法》相关的阅读入口与当前已经稳定下来的判断。
- [[wiki/sources/Spec-Driven Development Paper Source Guide|Spec-Driven Development Paper Source Guide]] — 这篇论文是 Deepak Babu Piskala 投稿 AIWare 2026 的 practitioner guide，把 SDD 这波被 AI coding assistant 重新点燃的旧想法梳理成三档光谱 + 四阶段流水线 + 决策框架。8 页，3 张图，零量化实验。 (#software-engineering #specs #ai-coding #paper)
- [[wiki/sources/Theory Is All You Need Source Guide|Theory Is All You Need Source Guide]] — 这页保留 Teppo Felin 与 Matthias Holweg 的论文 Theory Is All You Need: AI, Human Cognition, and Causal Reasoning 的阅读导览。 (#paper #ai #cognition #causal-reasoning #source)
- [[wiki/sources/Understanding as Concept Cloud Source Guide|Understanding as Concept Cloud Source Guide]] — Source guide for inline discussions that model understanding as a cloud and trace the frame to Hofstadter's analogy-making work. (#source #cognition #learning #concepts)
- [[wiki/sources/vLLM Inference Systems Source Guide|vLLM Inference Systems Source Guide]] — Source guide for Aleksa Gordic's vLLM article, focused on engine loops, paged attention, batching, P/D split, scaling, serving, and benchmarking. (#source #ai #llm #inference)

## Meta
- [[wiki/hot|Hot Cache]] — Added Feedback Flywheel as the maintenance loop for AI collaboration artifacts, metrics, and guardrails.
- [[wiki/log|LLM Wiki Log]] — 建立 wiki/ 作为稳定知识层入口。 明确目标结构： raw/ 为原始材料层， wiki/ 为复利知识层。 首批试点选择 AI / Agent 知识簇。 保留 pages/ 、 journals/ 、 mobu/ 、 content/posts/ 作为迁移来源。 (#llm-wiki #log)
- [[wiki/NAMING|NAMING]] — 这份文档规定 wiki/ 下笔记的命名和放置规则。
- [[wiki/README|README]] — This directory is the stable knowledge layer of the vault.
- [[wiki/Welcome|Welcome (legacy)]] — 这是历史遗留的 Obsidian 默认欢迎页，不再作为这个仓库的首页使用。
