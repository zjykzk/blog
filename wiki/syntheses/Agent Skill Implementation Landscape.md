---
title: Agent Skill Implementation Landscape
category: syntheses
type: synthesis
status: draft
tags: [agents, skills, tools, context, workflow]
sources:
  - conversation:2026-06-21
  - /Users/zenk/Documents/Agent_Skills_Research_20260621/research_report_20260621_agent_skills.md
created: 2026-06-21T15:34:41+0800
updated: 2026-06-21T15:34:41+0800
summary: Agent skill 是按需加载的操作知识包；行业实践可分为知识包、工具函数、协议服务和企业插件四类实现路线。
provenance:
  extracted: 0.70
  inferred: 0.30
  ambiguous: 0.00
base_confidence: 0.72
lifecycle: draft
lifecycle_changed: 2026-06-21
tier: supporting
aliases:
  - Agent Skill 的本质原理
  - agent skill 实现实践
  - skill implementation landscape
relationships:
  - target: "[[wiki/concepts/Agent Skill]]"
    type: extends
  - target: "[[wiki/concepts/Agent Tool]]"
    type: related_to
  - target: "[[wiki/syntheses/Tool and Skill Boundary in Agent Harnesses]]"
    type: extends
  - target: "[[wiki/topics/Tool Routing]]"
    type: uses
---
# Agent Skill Implementation Landscape

## Context

Agent skill 容易被误解成“保存下来的 prompt”或“另一种 tool”。这次调研把 Hermes Skills、Agent Skills 规范、OpenAI function calling、MCP、LangChain、LlamaIndex、Semantic Kernel、CrewAI，以及 ReAct、Toolformer、MRKL、Gorilla、SWE-agent 等 tool-use 论文放在一起比较，目标是看清 skill 的本质、实现机制、行业实践差异和可复用设计原则。

这页不是保存完整调研报告，而是把报告中的结构性结论编译进 wiki：skill 是 [[wiki/topics/Context Management]]、[[wiki/topics/Tool Routing]]、[[wiki/concepts/Agent Tool]] 和 [[wiki/topics/AI Harness]] 之间的一层操作知识边界。

## Finding / Decision

Agent skill 的本质不是提示词片段，而是 **可按需加载的操作知识包**。它把“何时使用、如何操作、依赖什么、怎样验证、失败时怎么办”封装成一个可发现、可审计、可演化的能力边界。

一个成熟 skill 至少同时承担四个职责：

1. **路由**：用名称、描述、frontmatter 或 catalog metadata 决定什么时候进入上下文。
2. **程序**：用正文说明任务步骤、前置条件、输出结构、约束、失败模式和验证方式。
3. **资源**：把长材料、模板、脚本、示例和参考资料放进 `references/`、`scripts/`、`assets/` 等二级资源，实现 progressive disclosure。
4. **治理**：让团队可以审查触发条件、脚本行为、危险动作、验证证据和后续更新，而不是把经验埋在一次聊天里。^[inferred]

因此，skill 比 tool 更靠近“操作系统扩展”：tool 提供一个可执行动作面，skill 决定这类工作应该如何被组织、校验和演化。

## Implementation Families

### 知识包路线：Hermes / Claude / Agent Skills

Hermes、Claude Code 和 Agent Skills 规范把 skill 设计成目录包：根部 `SKILL.md` 提供 metadata 与指令，`references/`、`scripts/`、`assets/` 承载长资料、确定性脚本和模板。这个路线的核心是 progressive disclosure：启动时只暴露轻量 metadata，触发后加载完整 instruction，必要时再读取具体资源。

知识包路线适合沉淀 workflow、checklist、项目惯例、故障处理路径、文档阅读方法和团队经验。它的关键风险是 skill 过宽、描述过泛、正文过长、资源分层不清，最终把可复用知识变成新的上下文噪声。

### 函数工具路线：OpenAI / LangChain / LlamaIndex

OpenAI function calling、LangChain tools 和 LlamaIndex tools 把能力暴露为可调用函数或 tool abstraction。模型通过 tool name、description、schema、type hints、docstring 和返回值语义来决定是否调用以及如何填参数。

函数工具路线适合构建确定性动作面：查数据库、调用 API、执行代码、检索文件、运行浏览器、生成图像。它的关键风险是 schema 污染和误调用：工具太多、名称相似、描述不清、参数约束弱时，模型可能知道要行动，却调用错接口、填错参数或误解结果。

### 协议服务路线：MCP

MCP 把外部能力变成 host-client-server 协议。AI 应用作为 host，为每个 MCP server 创建 client；server 暴露带有 name、metadata 和 schema 的 tools。这个路线解决的是能力跨进程、跨应用、跨组织边界复用的问题。

MCP 更像 agent 生态的“能力总线”，不是 skill 的替代物。MCP 可以提供 Jira、数据库、浏览器、代码索引或企业内部服务的动作面；skill 则规定“事故复盘”“需求评审”“发布回滚”这类任务如何使用这些动作面。没有 skill，MCP 只是工具集合；没有 tool/MCP，skill 只能停留在操作建议。^[inferred]

### 企业插件与协作路线：Semantic Kernel / CrewAI

Semantic Kernel 的 plugin 更接近企业服务封装：把已有 services and APIs 组织成可注入、可复用、可治理的一组能力。CrewAI 的 tools 更强调多 agent 协作、delegation、web search、data analysis 和 coworker collaboration。

这一路线适合组织级 agent 系统，因为它把 skill/tool 问题从单个 agent 的局部能力推进到服务边界、依赖注入、权限、协作责任和多角色工作流。

## Reasoning

[[wiki/syntheses/Tool and Skill Boundary in Agent Harnesses]] 已经区分了 tool 和 skill：tool 回答“agent 能对世界做什么”，skill 回答“agent 应该如何完成这类工作”。本次调研进一步补上 industry landscape：不同框架不是在争夺同一个概念名，而是在不同层级解决 agent 能力扩展问题。^[inferred]

ReAct、Toolformer、Gorilla 这类研究说明 tool-use 的根问题不是“是否有工具”，而是模型如何决定调用哪个 API、何时调用、填什么参数、如何吸收反馈、如何避免 API hallucination。skill 工程把这些问题转成显式边界：什么时候进入 workflow、哪些工具可用、哪些参数需要先确认、哪些结果必须回读验证。^[inferred]

这也解释了为什么 skill 质量不应按“内容多少”判断，而应按四个变量判断：

- **路由精度**：description 是否让 agent 在正确任务上加载 skill，同时避免误触发。
- **执行确定性**：可机械执行的部分是否被脚本、schema、模板或检查器承载。
- **验证强度**：完成后是否有真实工具输出、测试、文件、外部系统 ID 或回读证据。
- **演化速度**：一次失败或成功是否能更新 skill、reference、script、test 或 harness rule。

## Best-Practice Frame

设计 agent skill 时，应先问“这个任务主要缺什么”：

| 主导缺口 | 更适合的实现层 | 设计重点 |
|---|---|---|
| 缺操作知识、流程和判断顺序 | skill package | 触发条件、步骤、失败模式、验证 |
| 缺可执行动作面 | tool/function | 名称、schema、权限、错误处理 |
| 缺跨系统能力复用 | MCP / tool server | 协议、server 边界、metadata、认证 |
| 缺企业服务封装 | plugin / service wrapper | API 分组、依赖注入、权限、审计 |
| 缺多角色协作 | multi-agent tool / CrewAI-style collaboration | delegation、责任分配、状态同步 |

好的 skill 通常不是单独存在，而是与工具和协议组合：skill 决定任务语义，tool/MCP 执行动作，plugin/service 承载企业系统边界，harness 负责权限、反馈、审计和恢复。^[inferred]

## Anti-Patterns

- 把 skill 写成百科式长文，导致加载后仍然不可执行。
- 把所有能力都做成 tool，缺少 workflow，导致 agent 会调用动作但不知道正确顺序。
- 把所有流程都做成 skill，缺少确定性脚本，导致 agent 每次重建细节。
- `description` 写得像宣传语，而不是触发边界。
- 缺少验证步骤，让“完成”只停留在 agent 叙述而没有外部证据。
- 高风险动作藏在 skill 内，没有权限、确认、审计和回滚边界。
- skill 不维护，旧 API、旧命令、旧项目惯例继续污染未来运行。

## Implications

个人或团队不应先追求“写很多 skills”，而应先建立 skill inventory：优先 skill 化那些高频、复杂、容易出错、跨工具、需要验证、历史坑多的任务。一次性解释、过期快事实、纯概念百科不应直接进入 skill；它们更适合进入 [[wiki/sources/LLM Wiki Source Guide]] 所代表的 wiki/source 层，或进入概念页与综合页。

在 agent 工程中，skill 是一种责任边界。没有 skill 时，失败很难归因：是模型不懂、工具 schema 不好、文档太长、流程缺失，还是验证不足？有了 skill，团队可以审查和修复具体表面：`description`、步骤、examples、scripts、references、done condition、permission rule 或测试。^[inferred]

这把 [[wiki/concepts/Agent Skill]] 接到 [[wiki/concepts/Harness Ratchet]]：一次 agent 失败只有沉淀成 skill、tool schema、verification loop、harness rule 或 team standard，才会改变下一次运行，而不是重新变成 prompt 技巧。

## Related

- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Agent Tool]]
- [[wiki/topics/Tool Routing]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/Context Management]]
- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/Tool and Skill Boundary in Agent Harnesses]]
- [[wiki/syntheses/Agent Skill × Context Management]]
- [[wiki/syntheses/Agent Skill × Harness Ratchet]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/sources/Claude Code Skills Source Guide]]
- [[wiki/sources/Agent Skills Survey Paper Source Guide]]
