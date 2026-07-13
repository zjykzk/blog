---
title: AGENTS.md as Repository Operation Contract
type: synthesis
status: draft
category: synthesis
tags: [agents, ai-coding, software-engineering, harness, context]
aliases:
  - AGENTS.md 行业最佳实践
  - Agent Repository Instructions
sources:
  - conversation:2026-07-12
  - https://agents.md/
  - https://docs.anthropic.com/en/docs/claude-code/memory
  - https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot
created: 2026-07-12T23:18:57+0800
updated: 2026-07-12T23:18:57+0800
summary: >-
  AGENTS.md 是仓库面向编码智能体的最小操作契约，用导航、命令、边界和完成证据降低高代价的不确定性，并把强制约束交给自动化机制。
provenance:
  extracted: 0.70
  inferred: 0.30
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-07-12
tier: supporting
---

# AGENTS.md as Repository Operation Contract

## Context

编码智能体进入代码仓库时，面对的主要困难不是缺少通用编程知识，而是不知道这个仓库的正确入口、真实约束、验证方式和完成标准。`AGENTS.md` 的作用，是把这些只有维护者知道、又会反复影响任务结果的知识，压缩成一个跨工具、可版本控制的操作契约。

开放的 AGENTS.md 约定使用普通 Markdown，没有强制字段；根文件提供全局指导，嵌套文件可提供局部规则，离目标文件最近的文件通常具有更具体的作用域。GitHub Copilot 也支持仓库内多个 `AGENTS.md`，并采用最近文件优先的模型。Claude Code 原生读取 `CLAUDE.md`，官方建议通过导入或符号链接复用 `AGENTS.md`，避免维护重复规则。

## Finding

最好的 `AGENTS.md` 不是信息最多的项目百科，而是用最少的常驻上下文，消除最昂贵的工程不确定性。^[inferred]

它主要承载三类知识：

1. **导航信息**：规范实现在哪里，架构入口在哪里，哪些目录是遗留区或生成区。
2. **操作信息**：环境如何准备，命令从哪里运行，何种改动应执行哪些测试、lint、构建或生成步骤。
3. **约束信息**：哪些依赖方向、修改路径、数据边界或工作区纪律不能违反。

它还必须定义任务的证据闭环：Agent 不是在“代码看起来完成”时停止，而是在相关测试、静态检查、生成物一致性和必要的运行时验证已经产生新鲜证据后停止。

## Design Principles

### 1. 最小充分

常驻指令会消耗上下文，也会争夺模型注意力。说明应具体、简洁、结构化；单文件过长时，应把局部规则下沉到子目录，把多步骤流程移到 skill 或 playbook，把详细背景链接到架构文档。Anthropic 对同类 `CLAUDE.md` 的建议是尽量控制在 200 行以内，这可以作为 AGENTS.md 的经验性上限，而不是格式标准。

一条内容是否值得常驻，可以用失败成本检验：

> 删除这条指令后，Agent 是否更容易犯一个具体、可观察且代价较高的错误？

如果不会，它通常不值得进入 `AGENTS.md`。^[inferred]

### 2. 优先保存决策性知识

Agent 可以从 manifest、CI、Makefile 和邻近代码中发现大量事实。`AGENTS.md` 应优先解释代码不能直接回答的选择：多个命令中应该运行哪个、哪个目录才是规范入口、修改 schema 后还要更新什么、某个看似可行的依赖为什么被禁止。

因此，它不是可发现事实的复制品，而是仓库决策知识的压缩层。^[inferred]

### 3. 指令必须可执行、可定位、可验证

“充分测试”“遵循最佳实践”“保持高质量”无法稳定指导行为。有效指令应说明：

- 在什么条件下适用；
- 执行什么动作；
- 从哪个目录执行；
- 成功标准是什么；
- 为什么存在这条约束。

推荐句式是：`When <condition>, do <action>, because <reason>.` 原因不必展开成设计文档，但应足以帮助 Agent 判断边界和冲突。

### 4. 用分层文件表达作用域

根 `AGENTS.md` 只保存全局不变量、仓库地图和共同验证入口。前端、后端或 monorepo package 的专属命令和边界，应进入离代码更近的 `AGENTS.md`。局部规则不应复制到根文件，也不应让所有任务承担无关上下文成本。

不同 Agent 对继承、拼接、覆盖和加载时机的实现并不完全相同，因此公共文件应保持工具无关；工具特有内容放在薄适配层中，例如让 `CLAUDE.md` 导入 `AGENTS.md`。^[inferred]

### 5. 明确定义架构边界和 Done

架构指令应表达允许或禁止的依赖关系，而不是要求“保持良好架构”。例如：domain 不得依赖 HTTP、ORM 或框架类型；handler 只能通过 application service 访问业务能力；生成目录不得直接修改。

完成标准也应按改动类型绑定验证证据：公共接口改动需要下游检查，数据库 schema 改动需要 migration 验证，生成代码改动需要重新生成并检查 diff，前端交互改动需要类型检查和运行时或浏览器证据。^[inferred]

### 6. 文档负责告知，机制负责强制

`AGENTS.md` 是上下文，不是安全边界。模型可能忽略、误解或受到更高优先级指令影响。必须执行的格式、依赖、测试、安全和权限规则，应由 formatter、CI、架构测试、hook、sandbox 和权限系统强制。

分工应是：

- `AGENTS.md` 解释仓库如何工作以及为什么；
- skill / playbook 承载按需加载的多步骤流程；
- 自动化检查阻止可机械判断的错误；
- 权限系统控制高风险或不可逆动作。

这使 `AGENTS.md` 成为 [[wiki/concepts/Coding Agent User Harness]] 的前馈控制面，而测试、lint、CI 和审查构成反馈控制面。^[inferred]

## Recommended Structure

一个成熟但紧凑的根文件通常按以下顺序组织：

1. Purpose：一至三句话说明系统主轴。
2. Repository Map：规范入口、主要模块和易走错区域。
3. Setup：准确、可复制的环境准备方式。
4. Common Commands：开发、测试、lint、构建和生成命令。
5. Architecture Boundaries：允许和禁止的依赖方向。
6. Change Workflow：改动前、中、后的必要动作。
7. Generated Files and Migrations：不可直接编辑的文件及正确更新方式。
8. Security and Workspace Discipline：密钥、数据、提交与用户未完成改动的边界。
9. Definition of Done：完成前必须提供的验证证据。
10. Further Documentation：链接 ADR、运行手册和详细设计，而不复制全文。

实际仓库只应保留能阻止真实错误的章节。^[inferred]

## Evolution Loop

`AGENTS.md` 应通过真实失败演化：

1. 观察重复错误、PR 驳回、错误命令和无效搜索；
2. 判断问题来自偶发执行，还是缺失的仓库知识；
3. 对知识缺失补充最小、可验证规则；
4. 对可机械判断的错误增加自动检查；
5. 观察同类失败是否减少；
6. 删除无效、冲突、过期或已被自动化吸收的规则。

这条回路把一次 Agent 失败变成 [[wiki/concepts/Harness Ratchet]]：经验不是停留在一次性纠正里，而是进入未来任务默认可用的控制面。^[inferred]

## Implications

评价 `AGENTS.md` 不应看篇幅，而应看它是否减少：首次探索时间、失败命令、架构越界、遗漏验证、无关改动和被拒绝的 PR。^[inferred]

成熟度的终点也不是越来越厚的说明文件，而是关键约束逐渐进入可执行治理：`AGENTS.md` 保留导航、解释和不可轻易发现的决策知识，机器可判定的规则进入 CI、linter、hook 和权限机制。^[inferred]

因此，`AGENTS.md` 同时连接了 [[wiki/concepts/Knowledge Priming]] 与 [[wiki/concepts/Encoding Team Standards]]：前者告诉 Agent 项目如何运作，后者告诉 Agent 团队如何判断；`AGENTS.md` 则把其中最需要常驻、最具仓库作用域的部分压成操作契约。^[inferred]

## Related

- [[wiki/concepts/Coding Agent User Harness]]
- [[wiki/concepts/Encoding Team Standards]]
- [[wiki/concepts/Knowledge Priming]]
- [[wiki/concepts/Computational and Inferential Controls]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/topics/AI Harness]]
