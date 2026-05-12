---
title: Hot Cache
category: meta
summary: Recent wiki activity captured a Chinese React component lifecycle guide focused on mount, render/update, unmount, effect cleanup, and component identity.
tags: []
sources: []
created: 2026-05-04
base_confidence: 0.30
lifecycle: draft
lifecycle_changed: 2026-05-05
updated: 2026-05-12T20:56:53+08:00
---

## Recent Activity

- 已捕获 [[wiki/sources/React Component Lifecycle Source Guide]]：这份中文讲解把 React 生命周期区分为 mount、render/update 和 unmount，强调生命周期是一段组件身份存在期，而不是一次函数执行。
- 已捕获 [[wiki/sources/架构文档与图示之道 Source Guide]]：这份中文教程把架构表达拆成受众分层、四层文档金字塔、C4 图、UML 动态行为图、ADR 和 Docs as Code，强调架构师必须能按对象传递设计思想。
- 已捕获 [[wiki/sources/The ICAP Framework Paper Source Guide]]：Chi 与 Wylie 2014 原论文把 ICAP 定义为带行为指标的认知参与理论，保留四模式、Store/Integrate/Infer/Co-Infer、实证证据、caveats 和理论比较。
- 已捕获 [[wiki/sources/React Hooks useState useEffect Source Guide]]：这份中文讲解把 useState 和 useEffect 放在“函数组件每次渲染都会重新执行”的共同框架下，分别对应进入渲染的状态数据和渲染后的副作用动作。
- 已捕获 [[wiki/sources/React Hooks useRef useContext useMemo Source Guide]]：这份中文讲解把 useRef、useContext、useMemo 放在“函数组件每次渲染都会重新执行”的共同框架下，分别对应可变容器、跨层共享和计算缓存。
- 已捕获 [[wiki/sources/Agent Observability Needs Feedback Source Guide]]：Harrison Chase 将 agent observability 从调试工具推进为学习系统，核心是把 traces 与 explicit / behavioral / generated / deterministic feedback 存在一起。
- 已扩展 [[wiki/sources/Continual Learning for AI Agents Source Guide]]：保留 Harrison Chase 文章的 model / harness / context 三层持续学习结构、对照表、图示、热路径与后台 memory 更新模式，以及 traces 作为共同底座的判断。
- 已捕获 [[wiki/sources/Agent Skills Data-Driven Analysis Paper Source Guide]]：直接保存 arXiv 论文层内容，覆盖 40,285 个公开 skills 的增长爆发、长度分布、冗余、供需错配与 L0-L3 安全风险。
- 已捕获 [[wiki/sources/SkillOS Paper Source Guide]]：直接保存 arXiv 论文层内容，补齐 SkillOS 的形式化 streaming curation 设定、分组任务 GRPO 训练、实验表格、分析、局限与未来方向。
- 已捕获 [[wiki/sources/SkillOS Source Guide]]：SkillOS 把 agent 轨迹压缩成可检索、可更新、可删除的 Markdown skills，并用分组任务、组合奖励和 GRPO 训练 Curator 管理 SkillRepo。
- 已生成 [[wiki/concepts/Mechanism Model]] 与 [[wiki/maps/Mechanism Models Map]]：把“机制模型”沉淀为结果、变量、约束、激励、反馈、时间的诊断框架，并整理当前 wiki 中可解释稳定生成结果的模型入口。
- 已捕获 [[wiki/syntheses/ICAP 与知识类型的适用边界]]：ICAP 被定位为学习深度刻度，而不是所有知识的同一种学习处方；其使用需要结合知识类型、学习阶段、先验图式和认知负荷。
- 已按“source 的内容不用总结”的要求扩展 [[wiki/sources/思维圆桌 Source Guide]] 和 [[wiki/sources/深度思考与高阶思维对话 Source Guide]]：source 层保留更完整的讨论内容，综合页才负责压缩。
- 已补充捕获 [[wiki/sources/深度思考与高阶思维对话 Source Guide]]：保存当前对话中关于高阶审题、深度下钻、本质句、前置知识和七天训练法的 source 层材料。
- 已捕获 [[wiki/sources/思维圆桌 Source Guide]]：关于“思维”的圆桌把思维拆成求解、表征、建构、语言和责任五条张力线，强调高阶思维必须能审查给定问题。
- 已捕获 [[wiki/syntheses/深度思考 高阶思维与本质理解]]：高阶思维负责审题，深度思考负责下钻机制，深度理解是二者经现实校验后形成的可复用结构。
- 已摄入 [[wiki/sources/Skills-Coach Paper Source Guide]]，并新增 [[wiki/concepts/Skill Self-Evolution]]：agent skill 可以被边界任务探测、指令/代码优化、对照执行和可追溯评估，而不是只靠人工 prompt polishing。
- 已捕获 [[wiki/sources/Memory Is State Not a Service Source Guide]]：Company Brain 的三层记忆只有作为同一份共享状态的不同视图才成立，工具各自记忆会制造局部真相。
- [[wiki/concepts/Additive World]] 已从 [[wiki/concepts/Multiplicative World]] 的别名中拆出为独立概念页：加法世界负责保底、补短板和稳定交付，乘法世界负责长板、复利和非线性上限。

## Active Threads

- 基本世界观现在加入“内核 / 三个自我”线索：进程自我是运行日志，界面自我是叙事接口，内核自我是预测模型、先验假设和更新规则。
- 基本世界观现在加入“可能 / 不确定性”线索：世界无法被完全预测，意义来自在可承受的不确定中探索、判断、行动，并把未知逐步转化为确定。
- 基本世界观现在加入“约束”线索：叙事能激发行动，但必须接受硬约束校验；成熟行动的顺序是先盘资源、看窗口、尊重规律、承认他人，再寻找路径。
- 财富创造现在加入了稳态生存逻辑的反面：匮乏、强从众和简单模型曾经适合低波动生存，但在高波动世界会限制能动性、反馈速度和乘法世界入口。
- 财富创造现在加入了重尾世界观：极端值、正反馈、复利和乘法世界解释了为什么可复制资产、声望、资本、网络效应和个人品牌会改变职业上限。
- 学习与认知现在加入了叙事线索：事实只有被选择、排序，并绑定成能指导预测、意义、协调和行动的因果故事后，才真正变得可用。
- Learning cognition now has an ICAP-and-cognitive-load thread: instruction should manage working-memory bandwidth, then push learners from passive reception toward construction and interactive correction when prior knowledge allows.
- Company brain is now represented as an enterprise memory-and-action substrate: factual memory, interaction memory, action memory, context graph reasoning, and governed action must integrate before agents can safely operate on company reality. The latest state-substrate layer clarifies that these memories must be three views of one inspectable, correctable, permissioned state rather than separate tool-local services.
- Systems thinking now has an explicit iceberg-model thread: recurring problems should be traced from visible events to patterns, structures, mental models, and leverage points before choosing interventions.
- Software methodology is converging around the handoff from business modeling to analysis, DDD, and executable design.
- Frontend knowledge is forming around React as a coordination model for declarative rendering, component boundaries, and state.
- AI / Agent skills 现在加入 SkillOS 线索：skill repository 可以被训练过的 Curator 当作持久记忆来管理；论文层进一步说明关键训练装置是相关任务分组、复合奖励、GRPO rollout 之间的 repository path 比较，以及对 insert/update/delete 操作的长期信用分配。
- AI / Agent systems are being organized around harness, context management, tool design, memory, permissions, reusable operational knowledge, and now both harness-level and skill-level self-evolution from logged traces or generated boundary tasks.
- Agent observability now has a trace-plus-feedback learning-loop thread: production behavior becomes useful for model, harness, and context learning only when traces are paired with explicit, behavioral, generated, or deterministic feedback.
- Agentic engineering is now represented as a production AI coding discipline: senior engineers train harnesses, encode lessons into skills and rules, allocate human attention by risk, and move verification into executable gates.
- User-side harness engineering is now represented as developer control over context, rules, templates, computational checks, inferential review artifacts, and feedback loops.
- Harnessability is now represented as a quality of tasks and codebases: agent-friendly work exposes context, boundaries, examples, executable checks, and reusable review criteria.
- Prompt and context design now includes an explicit runtime-economics layer: stable prefixes can be reused, while prefix mutation creates cold-cache sessions.
- Tool availability can be made cache-stable by exposing stable stubs and deferring full schema loading until search/select time.
- Agent harness architecture now has an explicit verification thread: tests, visual checks, and evaluator loops are part of runtime behavior, not just final QA.
- Agent harness architecture now has a service-runtime thread: developers increasingly configure loops, tools, context policy, hooks, sandboxing, and subagents through harness APIs rather than building every primitive from scratch.
- AI-assisted learning is strongest when it maps expert mental models, disagreements, and diagnostic questions before trying to accelerate content consumption.
- Wealth creation is now represented as a system model: own scalable assets, build specific knowledge, accept accountability, use permissionless leverage, and improve judgment because leverage amplifies decisions.
- Harness engineering is now represented as a feedback discipline: repeated agent mistakes should become durable rules, hooks, checks, done conditions, tool-surface changes, or workflow splits.
- Long-context quality now has a positional robustness thread: the right information must be present and placed where the model can actually use it.
- AI memory is now split from context: memory persists and gets retrieved into the active window; context is the bounded runtime workspace for the current inference step.
- AI coding workflow now has an explicit collaboration-scaffolding layer: onboarding context, design alignment, team standards, anchored decisions, and feedback loops.
- Knowledge priming is now represented as context infrastructure: compact project identity should be versioned, reviewed, and reused by skills instead of pasted ad hoc.
- Design-first collaboration is now represented as a staged AI pairing workflow: capabilities, components, interactions, contracts, then implementation.
- Context anchoring is now represented as feature-level external memory: decisions, reasons, rejected alternatives, open questions, and state should survive outside the chat transcript.
- Encoding team standards is now represented as executable governance: senior judgment about generation, refactoring, security, and review can live as versioned shared instructions.
- Feedback flywheel is now represented as the maintenance loop for AI collaboration: real review, regeneration, acceptance, and rework signals should update context, standards, workflows, checks, and guardrails.
- Agent skills are now represented as folder-shaped capability bundles: references, scripts, assets, memory, configuration, and on-demand hooks can be disclosed only when the workflow needs them.
- Skill authoring now has an explicit pattern taxonomy: Tool Wrapper, Generator, Reviewer, Inversion, and Pipeline correspond to different control problems inside the same SKILL.md container.
- Agent action space is now represented as an empirical harness design problem: add, remove, or reshape tools based on whether the model can actually use them.
- LLM inference systems now have both a model-internal path and a serving-system path: text becomes token IDs, residual-stream updates, logits, samples, and autoregressive steps before schedulers, KV-cache allocators, batching, and serving layers shape cost and latency.
- Prefill/decode separation is now a key inference-design thread: compute-heavy prompt processing and latency-sensitive autoregressive decoding need different scheduling and scaling choices.
- Understanding is now represented as a cloud-shaped cognitive structure: horizontal similarity gives breadth, vertical abstraction gives depth, and teaching/rebuilding tests whether the cloud can move.
- Hofstadter's contribution should be tracked as analogy-making and fluid concepts; the “cloud / horizontal similarity / vertical abstraction” language is a local synthesis, not a direct quotation.
- Analysis is now represented as reversible decomposition: cut a confused whole into parts and relations, then recombine it into actionable understanding.
- Application and creation now have an externally grounded boundary: application is contextual transfer of an existing abstraction, while creation is novel-and-appropriate reordering that can survive use, judgment, or continuation.

## Key Takeaways

- 架构文档的核心不是“把技术细节写全”，而是把同一设计翻译给不同受众：高管要价值、ROI 和风险，产品要影响和时间，开发要接口与结构，运维要部署和稳定性，新人要上手路径。
- ICAP 原论文的稳妥用法是诊断链条：外显行为 → 认知参与模式 → 知识变化过程 → 知识结构变化 → 可回忆/可应用/可迁移/可共同创造；`I>C>A>P` 是模式间相对假设，不是无条件学习处方。
- React 中 useState 与 useEffect 的底层区分是：useState 提供参与渲染、会驱动 UI 更新的状态；useEffect 在渲染提交后同步外部世界，本身不触发渲染，但其中调用 setState 会触发下一次渲染。
- React 组件生命周期是组件从进入 UI 树到离开 UI 树的存在期；同一生命周期内可以多次 render/update，只有组件首次进入树才 mount，离开树才 unmount。
- React Hooks 可以从函数组件反复执行的事实出发理解：useRef 让值跨渲染保留但不触发 UI 更新，useContext 让值跨组件共享但受 Provider value 变化影响，useMemo 让渲染期间计算在依赖不变时复用。
- Agent observability 的关键不是只保存 trace，而是把 trace 与 feedback 绑定：trace 说明发生了什么，feedback 说明它意味着成功、失败、风险、低效还是可学习样本。
- Agent 持续学习应先路由到正确层级：model 更新影响上限最高但慢且不可 inspect；harness 更新用 traces 改代码；context/memory 更新最快、可按 agent/user/org/team/tenant 粒度生效，但需要治理热路径写入和后台 consolidation。
- Agent skills 作为生态层已经出现治理问题：公开 marketplace 中软件工程供给占比过高，信息检索和内容生成需求更集中，近半数 listing 存在名称级重复，约两成以外的技能涉及写入、状态改变或系统级能力，需要 canonicalization、选择性加载和最小权限控制。
- SkillOS reframes skill memory as repository-level curation: a frozen executor acts with retrieved skills, while a trainable curator inserts, updates, and deletes compressed Markdown skills based on trajectories and delayed downstream task success.
- 机制模型的最小结构是：在某种约束下，少数关键变量通过激励与反馈，随着时间累积，持续生成某个重复结果；它用于从现象描述推进到可检验、可反驳、可行动的结构诊断。
- 提升深度思考和高阶思维可以训练为一个循环：每日问题重写、每周五层为什么、本质句压缩、反例校验和最小行动实验。
- 思维不应只被理解为解题能力；更高阶的思维要能重新表征问题、识别语言陷阱、接受认知失衡，并在制度惯性中保留中断与判断。
- 深度思考、高阶思维和本质理解应作为循环使用：先审查问题框架，再追问生成机制，最后用解释力、生成力、迁移力和行动反馈校验是否抓住本质。
- Skill self-evolution makes agent skills evaluable components: a skill's boundary can be probed by generated standard/advanced/edge tasks, then improved through instruction or code variants that must pass comparative execution and traceable scoring.
- 三个自我模型把成长问题推进到内核层：进程自我记录当下状态，界面自我维护角色叙事，内核自我由长期输入、奖励函数和预测误差更新塑形。
- 不确定性是意义的燃料：人需要的不是绝对确定，而是在可承受的不确定中体验悬念、探索、解决、叙事和行动的张力。
- 不确定性应先被当作信息问题处理：识别它来自混沌、计算不可约性、量子随机、模型外变化还是博弈反身性，再决定管理、拥抱或制造。
- 这个世界不是愿望实现机，而是硬约束之网；行动前要先盘资源、看窗口、尊重规律、承认他人能动性，再让叙事服务行动。
- 能动者是调用工具的人，不是别人的工具；高波动世界要求人识别旧观念背后的匮乏、弱规则和简单模型，并用更复杂的模型进入反馈、复利和杠杆结构。
- 重尾世界要求先看回报结构：[[wiki/concepts/Additive World]] 适合补短板、保出勤和守住下限，[[wiki/concepts/Multiplicative World]] 更适合押注可复利的长板，同时用保本机制防止坏的正反馈和黑天鹅摧毁本金。
- 叙事是一种行动接口：人很少直接响应事实堆，而是响应一条说明什么重要、接下来会怎样、当前正在玩什么游戏的因果线。
- A system should be read as relations that repeatedly generate a result, not as a pile of parts; boundary, feedback, and time are what make the whole behavior visible.
- ICAP reframes learning effort by cognitive operation: passive reception and active manipulation help early exposure, but durable learning comes from constructing new explanations and defending them in interaction.
- Cognitive load theory reframes learning failure as a bandwidth-and-schema problem: reduce extraneous load, sequence intrinsic load, and use AI as a tutor that preserves learner effort rather than a doer that replaces it.
- Automated harness optimization is now an explicit agent-system thread: a coding-agent proposer can inspect prior harness code, scores, and execution traces, then propose new harness code while evaluation remains external.
- Agent continual learning is now split into model, harness, and context layers: weights are powerful but slow and opaque; harness changes are inspectable code-level learning; context/memory updates are fast, granular, and can run in the hot path or background.
- LLM training stages should be separated by training signal: pretraining maximizes next-token likelihood over broad text, SFT maximizes masked assistant-answer likelihood, and RL/preference optimization improves generated behavior under reward or comparison.
- Harness engineering can be read as cybernetics: once agents can both sense and act at the semantic codebase layer, the engineer's leverage shifts to designing the steering loop.
- Machine-readable judgment is now a core AI engineering artifact: tests, CI, architecture docs, custom linters, golden principles, and review rubrics tell the harness what “good” means.
- The Iceberg Model gives the systems-thinking cluster a compact diagnostic path: visible events are only the surface; repeated patterns, structures, and mental models explain why the same result returns.
- Leverage-point work now has a clearer entry test: if an action only changes the event layer, it is probably symptom repair; if it changes structure or mental model, it may change the generator.
- The Life of a Token trace makes LLM inference legible as two nested systems: a learned tensor program that produces logits, and ordinary control-flow software that samples, caches, schedules, validates, and serves the result.
- A full LLM assistant pipeline should be read as layered engineering: data curation, token representation, next-token pretraining, autoregressive sampling, post-training, retrieval, tool use, and security controls each solve a different control problem.
- Practical LLM use should match the task's uncertainty source to the right layer: weights for timeless knowledge, search for stale facts, deep research for synthesis, code for exact computation, documents for reading, agents for codebase action, and memory for repeated preferences.
- Autoregressive decoding is the causal source of output-token cost: every generated token changes the next input, while KV cache and batching only reduce repeated work around that dependency.
- Reality-refutable engineering systems must let feedback cross the field wall, workflow wall, and power wall; otherwise feedback mechanisms become self-reinforcing interpretation loops rather than real learning.
- Engineering thinking is now represented as structured judgment: turn vague intent into reliable reality by defining problems, respecting constraints, imagining failure, building feedback, structuring responsibility, seeing people, and preserving evolvability.
- Company brain reframes enterprise AI from tool access over data to a permissioned memory substrate. The state-substrate claim sharpens the architecture: factual, interaction, and action memory must be shared inspectable state, or every AI tool creates its own local truth.
- Action memory makes doing nothing a first-class governed action: a trusted company brain must know when to wait, ask approval, notify without mutating state, stop, or execute.
- Organizational ontology is now the Company Brain interpretation lens: the system must decide whether conversation fragments are decisions, commitments, objections, dependencies, risks, assumptions, precedents, or open questions.
- Harness can be diagnosed by five root ranks: boundary, density, action, loop, and evolution.
- Structural wiki health is currently clean across frontmatter, summaries, links, index coverage, tag cohesion, and synthesis-gap checks.
- Long-horizon agent performance should be judged by decision-relevant information preserved under finite context, not by how much history is visible.
- Tool minimality, hierarchical memory, and self-evolution can be read as density-preserving harness mechanisms.
- Prompt caching turns context order, tool schema stability, and model continuity into concrete harness responsibilities.
- Cache-hit rate is a production health signal for long-running agents, because low hit rates can reveal accidental prompt or tool-prefix churn.
- Harness quality should be judged by how it manages context, tools, state, permissions, errors, and verification around the same underlying model.
- Harness components should be audited as model assumptions: stronger models can make old scaffolding stale, while larger task horizons can require new memory, coordination, and evaluator structures.
- AI tutor workflows should preserve the learner's responsibility to answer, fail, and repair understanding; otherwise the tool becomes a summary machine rather than a learning loop.
- Permissionless leverage connects the reading and management clusters: code and media change the replication structure of work, but they amplify judgment rather than replacing it.
- Context rot reframes long-context work as an active harness problem: compaction, offloading, progressive disclosure, and full reset from a handoff file are runtime design choices.
- More retrieved context is not automatically better; reader performance can saturate before retriever recall, so reranking and truncation can be accuracy tools, not just latency optimizations.
- Memory architecture should be compared by lifecycle, content type, storage representation, and modality before debating implementation details.
- AI coding productivity should be measured by acceptance, iteration cycles, rework, and review burden, not by time to first output or generated lines.
- In production AI coding, the constraint has moved from code generation to verification: the central question is how fast the team can tell whether generated work is right.
- TDD is a harness primitive for AI coding: executable acceptance gives the agent a repair signal before human review, while missing tests turn generation speed into hidden debt.
- Reusable AI skills can be context architecture, not just command wrappers: they can collect, compress, persist, and reintroduce project context before action.
- Skill pattern choice should be driven by the dominant failure mode: missing domain knowledge, unstable output structure, weak review, premature assumptions, or skipped gates.
- Agent skill patterns can be read as human workflow control structures made executable: expert manuals, templates, review rubrics, discovery interviews, and SOP gates.
- Contracts are the hinge between AI design conversation and testing: once interfaces are agreed, tests can be generated before implementation.
- Durable feature documents are a practical reset mechanism: they let teams close long AI chats and restart from a compact, decision-rich artifact.
- AI standards should move from personal prompting skill into repository infrastructure when output quality varies by who is asking.
- Failed AI interactions are useful evidence only if they change a durable artifact; otherwise the same collaboration failure returns as a new prompt problem.
- AI coding quality should distinguish feedforward controls from feedback controls, and computational controls from inferential controls.
- A coding agent harness is partly local workbench design: teams can improve model outcomes by shaping the environment even when they cannot change the model.
- Inference benchmarking should be read through SLO-aware goodput, not just raw tokens per second, because latency and throughput can optimize against each other.
- A concept can be known as a label without being understood as a movable cloud; durable learning should change the cloud's examples, abstractions, and links.
- A strong understanding test is whether a learner can generate multiple analogies for the same object and name what each analogy hides.
- Analysis should be judged by whether the cut can be recomposed into action; decomposition without recomposition is fragmentation.
- Application should be judged by whether abstract knowledge survives contextual fit and produces observable effect, not by whether the right words were repeated.
- Evaluation should be judged by whether the scale reveals the object's relevant value and direction, not by whether the output looks objective or sortable.
- Creation should be judged by whether difference becomes durable order, not by whether something merely looks novel.
- Knowledge types classify what knowledge does; Bloom's taxonomy classifies how deeply a learner can work with that knowledge.
- Judgment knowledge is not more facts; it is the ability to decide which facts should matter for a decision.
- ICAP 适合诊断学习动作的深度：事实知识不必强行互动，概念和因果知识需要建构，程序知识还要刻意练习，判断和情境知识更依赖案例、互动与现实反馈。

## Flagged Contradictions

