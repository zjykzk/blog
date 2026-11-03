---
title: Agent Harness Loop and Goal Implementations
type: synthesis
status: draft
updated: 2026-11-02
aliases:
  - Agent Harness 中 Loop 与 Goal 的实现原理
  - Coding Agent Loop and Goal
  - Agent 循环与目标实现
summary: Claude Code、OpenAI Codex 与 pi 分别用 evaluator condition、provenance goal context 和 transcript state 实现目标连续性，而 tool loop、goal loop 与 recurring loop 属于不同控制层。
tags:
  - agents
  - harness
  - control-loop
  - goal
sources:
  - https://code.claude.com/docs/en/goal.md
  - https://code.claude.com/docs/en/scheduled-tasks.md
  - https://github.com/openai/codex
  - https://github.com/earendil-works/pi
---

# Agent Harness Loop and Goal Implementations

## Executive Summary

- **核心判断：** Coding agent harness 中至少存在三个嵌套控制层。Agentic tool loop 在一个 turn 内往返模型与工具；goal loop 在 turn 结束后依据完成条件决定是否重入；recurring loop 按时间或事件创建未来 turn。把三者都叫 loop 会隐藏不同的状态、预算、取消和恢复语义。[2][1][3]
- **Claude Code：** `/goal` 是独立 evaluator 驱动的 goal loop。每个 turn 后，小型快速模型根据条件和 conversation 返回未完成、完成或不可能；`/loop` 则是 session 内调度器，固定模式转成 cron，自适应模式通过 `ScheduleWakeup` 安排下一次唤醒。[6][10][11]
- **OpenAI Codex：** Rust core 把执行组织为 session、task、turn 与 sampling/tool loop。它有一等 `UserGoalUpdate`，但 goal update 只写入有 provenance 的 rollout/context，不会启动模型 step；scheduled automation 每次运行创建新 chat，属于外层触发。[26][30][31][36]
- **pi：** Core 没有 `Goal` 类型，目标由 transcript 中的 user/system messages 隐式承载。Coding-agent compaction 才把目标写入 `## Goal` 摘要；主循环由 tool calls、steering、follow-up 与 `finishTurn` 驱动，session 层负责 JSONL 持久化、压缩恢复与 abort。[14][18][20]

**Primary Recommendation:** 用 `intent + definition of done + durable progress + verifier + authority` 表示目标，并为三个循环分别设计界限、停止原因、恢复协议和可观察性。

**Confidence Level:** 高。Codex 与 pi 结论来自固定提交源码；Claude Code 来自官方行为文档。Claude 的内部字段与调度器实现仍不可见。

## Introduction

本报告回答两个容易混在一起的问题：coding agent harness 如何在一次任务内循环，以及它如何围绕一个目标跨 turn 或跨时间继续工作。范围包括 Claude Code、OpenAI Codex CLI 与 pi coding agent。分析优先使用官方文档和固定提交的上游源码；第三方框架只用于建立可比较的概念语言，不用于替代产品事实。

报告把 goal 当成功能结构，而不预设产品必须定义 `Goal` 类型。一个可运行的目标至少包含原始意图、完成定义、持久进度状态、继续谓词和完成权限。这个定义能同时解释三种实现：目标只存在于 transcript、目标由独立 evaluator 判断、目标由外部测试或调度器驱动。

研究排除模型内部不可观察的推理过程，也不把桌面或云端产品的 automation 能力自动归入 CLI。Claude Code 为闭源产品，内部实现只报告官方可观察行为；Codex 与 pi 使用提交级源码。独有实现事实允许由对应上游单源支持，跨产品结论必须由多条实现链共同支持。

## Main Analysis

### 1. 三层控制模型与分布式 Goal

“Loop”不是一个循环，而是三个可嵌套的控制层：

1. **Agentic tool loop**：模型输出工具调用，harness 执行、回填观察并再次采样，直到没有工具调用或控制边界终止。
2. **Goal loop**：agent turn 结束后，completion predicate 或 evaluator 判断是否重入，并把反馈作为下一轮输入。
3. **Recurring loop**：timer、cron、wakeup 或事件在未来提交新 prompt；它只决定何时运行，不天然判断任务是否完成。

Microsoft Agent Framework 对 goal loop 的定义是“重新调用 agent，直到完成条件满足”，并要求 autonomous loop 必须有上界；其 continuation predicate 可以同时返回继续决策与下一轮 feedback。VS Code 的 harness 说明则把内层循环概括为 think、act、observe、repeat，并在无 tool call 时结束。[1][3]

Goal 也不是必须存在的类。更一般的表示是：

`G = <I, D, S, V, A>`

其中 `I` 是原始意图，`D` 是 definition of done 与约束，`S` 是持久进度状态，`V` 是 verifier 或继续谓词，`A` 是能够宣告完成、批准、取消或重排的 authority。只有 prompt 时，模型隐式估计 `D` 与 `V`；goal loop 显式化 `V`；长任务 harness 外置 `S`；安全边界显式化 `A`。

### 2. Claude Code：Evaluator Goal Loop 与 Session Scheduler

Claude Code 官方文档把内部 agentic loop 描述为获取上下文、行动、验证三类交叠阶段。每次工具执行结果都会反馈给下一次模型决策，因此这一层是 model-directed tool loop，而不是公开的固定工作流图。官方没有公开内部循环状态结构或 `Goal` 序列化 schema，所以只能对其行为做文档级还原。[5]

`/goal` 位于内部工具循环之外。命令给当前 session 设置一个完成条件，同一 session 只能有一个 active goal；新 goal 会替换旧 goal。每当主 Claude 完成一个 turn，Claude Code 会把完成条件与截至当前的会话发送给配置的小型快速模型。这个 evaluator 返回 `Not yet met`、`Met` 或 `Impossible`，并附带理由。前者把理由变成下一 turn 的指导，后两者清除 goal 并在 transcript 记录结果。[6]

这一实现把继续谓词从主 agent 中分离出来，但 evaluator 不是独立验证器。它不会读仓库或运行测试，只判断主 agent 已经在 conversation 中暴露的证据。因此，如果 definition of done 是“测试通过”，主 agent 必须把测试结果带入会话；否则 evaluator 只能根据文本声称判断。这是 `/goal` 最重要的可信度边界。[6]

Goal 状态会随 session 保存并在 resume 时恢复，但只保留条件本身。turn count、timer 与 token-spend baseline 会重置。恢复的 conversation 以最后一次 compaction summary、未被压缩的消息及之后的新消息为基础；已经开始但被进程中断的工具不会在 resume 时自动重放。这避免了非幂等工具重复执行，但也意味着外部世界可能留下半完成状态，恢复后需要重新观察。[6][7]

`/goal` 的停止不只依赖 `Met`。`Impossible`、显式 clear、需要用户修复的错误都会结束 goal；无工具进展、只反复响应 evaluator 的连续 turn 会触发保护性停止，但 goal 仍保留，让用户接管。认证失败、余额耗尽、自动压缩无法解决的上下文溢出、模型不可用等错误会清除 goal；其他错误则保留 goal，以便 retry 或 pause。瞬态 API 错误由另一套重试机制处理，最多自动重试并使用指数退避；若重放可能重复已经启动的工具调用，则不重试。[6][9]

`/loop` 又是另一层。固定间隔模式把间隔转换成 cron 表达式，受一分钟粒度和 cron 可表达性约束。省略间隔时进入 self-paced loop：每轮结束后，模型通过内部 `ScheduleWakeup` 工具选择一分钟到一小时之间的下次延迟，或以 `stop: true` 终止。若一轮既未调度也未停止，harness 安排一次约二十分钟后的 fallback wakeup；下一轮仍不重排则结束。[10][11]

Scheduled prompt 以低优先级入队，只在 turn 之间运行，不会打断进行中的响应。这说明 scheduler 没有与内部 agent loop 并发抢占，而是把未来 prompt 注入同一 session 的 turn 边界。固定调度任务可在 resume 时恢复，但 self-paced `/loop` 不恢复；两者的持久化语义不同。[10]

### 3. OpenAI Codex：持久 Goal Context 与 Rust Turn Loop

Codex 的执行入口是长寿命 session submission loop。它等待用户 submission、runtime shutdown 或 mailbox update；`TurnInput` 进入专门的生命周期处理。新输入先尝试 steer 当前 active turn，如果没有 active turn，则生成新的 `RegularTask`。因此 session、task、turn 是三个不同层级：session 接受事件，task 管理一段连续工作，turn 承载模型与工具往返。[23][24]

内部 agentic loop 的源码注释十分直接：模型请求 function call 时，Codex 执行并把结果放入下一次 sampling request；模型只返回 assistant message 时，turn 完成。`RegularTask::run_turns` 在存在 pending input 时重复 `run_turn`，遇到 terminal error 或空输入队列时停止。`run_turn` 进一步把 model continuation 与 mailbox/user pending input 合并为 `needs_follow_up`；没有 follow-up 才进入 stop hook 与结束路径。[26][25]

Tool call 在模型流结束项中被解析、立即持久化并排队执行，同时把 sampling 结果标记为需要 follow-up。Tool orchestration 先判断审批，再选择 sandbox 执行。审批结果可能跳过、禁止、要求批准或要求新的人工判断。Sandbox denial 也不是无限重试：依据 policy，要么直接返回，要么经批准进行一次明确的 second attempt。这个控制面把“模型想调用工具”与“工具被允许并成功执行”分开。[27][28]

Codex 的 stop hook 位于没有自然 follow-up 的边界。Hook 可以注入新的 continuation 并继续，也可以要求 break；否则普通无 follow-up 路径结束。取消会产生 `TurnAborted`，正常 finalization 产生 `TurnComplete`。模型流重试属于独立 transport policy：非重试错误立即返回，普通重试有预算，必要时 WebSocket 可切换一次 HTTP；稳定 feature 允许特定连接失败无限重试，但这仍是传输恢复，不是 goal loop。[26][29]

Codex 与 pi 最大的 goal 差异是存在显式 `UserGoalUpdate`。它只能由 user-facing goal API 创建，状态为 `Set { objective, status }` 或 `Clear`，并被渲染为用户上下文消息。源码明确将它与 agent-created goals 和 runtime steering 分开，避免工具输出或自动 continuation 伪造用户目标。[30]

但 goal update 本身不会启动模型 step。`record_user_goal_update` 把它追加到 rollout 与 live history，却不加入 pending input，也不重新打开 active turn。换言之，Codex 把 goal 做成有 provenance 的持久上下文状态，而不是“设置即执行”的 autonomous loop。真正的执行仍需用户输入、automation 或其他 submission 触发 task。[31]

Goal continuity 被纳入 compaction 协议。压缩时记录输入历史中的 goal message IDs；安装压缩结果时，还会保留 snapshot 之后接受的新 goal edits，避免并发更新被旧摘要覆盖。Resume 从持久化 rollout 构造 `InitialHistory::Resumed`，重建模型上下文并原子替换 history。这比让摘要模型自由“记住目标”更强，因为 goal update 具有独立 identity 与安装规则。[32][33][34]

Codex automation 与 turn loop 也是分层的。官方文档说明 standalone scheduled task 每次运行都会开启新 chat，并以 unattended 模式使用默认 sandbox 配置。协议层的 schedule 只有 Hourly、Daily、Weekdays 与 Weekly 等时间结构。它负责在未来提交新的 prompt，而不是在现有 turn 内等待工具，也不是根据完成谓词自动判断目标已达成。[36][37]

### 4. pi：Transcript-Driven Loop 与 Session Runtime

pi core 是最透明的实现。`agentLoop` 接收 `AgentMessage[]` 和 context；`Agent.prompt` 把 string、单条消息或消息数组标准化，再启动 run。prompt、tools 与系统指令都由 transcript 的 system messages 承载。代码中没有一等 `Goal` 类型，说明 core 的目标只是用户消息及其累计 transcript 语义。[14][15][17]

真正的主循环有两层。外层 `while (true)` 负责在自然结束后吸收 follow-up；内层 `while (hasMoreToolCalls || pendingMessages.length > 0)` 处理 tool result 与 steering。每一轮可以先经过 `prepareNextTurn` 和 `prepareRequest` 改写上下文、model 或 thinking level，再进行一次流式模型调用。正常响应中，tool calls 被解析、校验、执行，tool results 追加进 transcript，随后运行 `finishTurn` 并发出 `turn_end`。[14]

Steering 与 follow-up 不是同一队列。steering 优先，并在工具批次完成后进入当前 run；follow-up 只在内层循环本来要停止时被读取，因而更像下一 turn 的排队输入。这种结构为人类运行中转向与任务结束后的追加工作提供了明确插入点，同时避免 steering 插到半个 tool batch 中间，破坏 observation 的完整性。[15][14]

工具执行具有完整的 harness 边界：查找工具、改写或校验参数、运行 `beforeToolCall`、执行工具、运行 `afterToolCall`，最后写入标准化 tool-result message。工具可以 sequential 或 parallel 执行；并行完成顺序可以不同，但结果按源顺序写回 transcript。未知工具、非法参数、hook 阻止、异常或 abort 都会被转换成显式错误结果，使模型能在下一次调用中观察失败。长度截断的 assistant response 不会执行其中可能不完整的工具调用。[14][22]

停止路径同时来自模型、harness hook 与外部取消。assistant 的 `stopReason` 区分 stop、length、toolUse、error、aborted 等状态；`finishTurn` 可以返回 continue 或 end；tool batch 也可通过结果的 `terminate` 触发终止。provider error 或 abort 是 hard exit，不能被 continue decision 覆盖。`Agent.abort()` 通过 AbortController 传播取消。[17][16][14][15]

pi coding-agent 的 session 层把 core loop 包装成长任务运行时。它调用 `agent.prompt(...)`，执行 post-run 处理，并可通过 `agent.continue()` 在没有新用户消息时继续。session 状态以 append-only JSONL tree 持久化；branch 移动当前 leaf 而不修改历史，fork/resume 在 runtime 层重建活动 session。与只保存线性聊天相比，这个结构同时支持审计、回退和分支实验。[19][20][21]

Context overflow 与普通 retry 分开处理。session 层会标记一次 overflow recovery，忽略失败 attempt，然后自动 compaction 并重试。compaction prompt 显式要求生成 `## Goal`，并在增量压缩时保留既有目标、补充扩展后的目标。这里的 goal 不是运行时控制对象，而是给后续模型读取的语义摘要。abort 则同时取消 retry、compaction、branch summary 和 core agent，再等待 idle，防止后台恢复流程在用户停止后继续运行。[19][18]

### 5. 横向比较

| 维度 | Claude Code | OpenAI Codex | pi coding agent |
|---|---|---|---|
| 内层执行单元 | 模型 turn 与工具结果反馈 | session → task → turn → sampling/tool | `agentLoop` 外层 follow-up 与内层 tool/steering |
| Goal 表示 | Session 内单一完成条件 | `UserGoalUpdate::Set/Clear` 加 objective/status | Core 无一等 Goal；由 transcript 承载 |
| Goal 是否自动执行 | `/goal` 每 turn 后自动 evaluator 重入 | 否；goal update 不产生 pending input | 否；需 prompt、continue 或外部 wrapper |
| 继续条件 | evaluator 返回未完成 | tool follow-up、pending input、stop hook continuation | tool calls、steering、follow-up、`finishTurn` |
| 定时重入 | `/loop`、cron、`ScheduleWakeup` | Automation 每次新建 chat | Core 无内建 scheduler |
| 压缩中的目标 | 条件独立持久化；会话历史摘要 | goal message ID 独立保留并处理并发 edit | 摘要模板生成并保留 `## Goal` |
| Resume | 恢复 active goal 与 compacted conversation；不重放中断工具 | 从 rollout 重建并原子安装 history | Append-only JSONL tree、branch/fork/resume |
| 停止边界 | met、impossible、clear、错误、无进展保护 | 无 follow-up、stop hook、abort、terminal error | assistant stop/error/abort、hook end、tool terminate |
| Retry | API retry 与 goal evaluation 分离 | transport retry 与 goal/task loop 分离 | session retry、overflow compact-and-retry 与 abort 分离 |

三套实现的共同点不是 API 名称，而是都把“下一步动作”“是否继续追目标”“何时再次运行”放在不同机制中。差别主要在 goal 的显式程度：Claude 是 evaluator condition，Codex 是带 provenance 的 context mutation，pi 则是 transcript 语义与 compaction summary。

## Synthesis & Insights

### 结论一：控制面不是单环，而是嵌套环

最内层工具循环的时钟是“模型响应或工具结果”；goal loop 的时钟是“一个 agent turn 完成”；recurring loop 的时钟是“时间或外部事件到期”。三者的 state、stop 与 retry 不能共用一个布尔变量。内层结束不代表目标完成，定时器到期也不代表应该继续执行高风险动作。[1][10][14]

### 结论二：goal 是分布式协议，不只是 prompt

只有原始 prompt 时，模型同时承担理解目标、判断进度和宣告完成，容易出现“说完成即完成”。Claude `/goal` 把继续谓词交给独立模型，但证据仍来自 conversation。pi 把目标留在 transcript，并在 compaction summary 中显式保留。更可靠的 harness 会把 definition of done 与外部验证绑定，把 progress 写入可恢复状态，并单独定义谁能宣告结束。[6][18][1]

### 结论三：compaction 是语义迁移，不是无损压缩

上下文压缩会把历史变成新的控制输入。保留 goal、未完成工作、关键约束和失败尝试，相当于把运行状态迁移到下一窗口。Claude 明确提醒早期详细指令可能丢失；pi 的 summary template 则把 `## Goal` 作为结构字段。由此可见，compaction schema 是 goal protocol 的一部分，不能只按 token 节省评价。[8][18]

### 结论四：停止、失败与暂停必须区分

成功完成、目标不可能、瞬态 API 错误、需要用户修复、等待审批、用户 abort、上下文溢出不是同一种 terminal state。把它们都表示成“loop=false”会丢失恢复策略。产品实现普遍需要至少 `completed`、`failed_terminal`、`paused_external`、`retryable`、`cancelled` 与 `scheduled` 等状态，且必须记录终止原因。[6][9][16][1]

### 结论五：恢复语义必须防止重复副作用

Session resume 不等于重放最后动作。Claude 不重跑中断工具；pi 把失败 attempt 从恢复上下文中排除，并使用 append-only session tree。可靠恢复需要先重新观察外部状态，再决定是否补偿或重试。对写文件、发送消息、支付或部署等非幂等工具，request ID、操作日志和幂等键比“自动再试一次”更重要。[7][20][19]

## Limitations & Caveats

本研究是实现原理比较，不是性能基准。公开资料无法证明不同模型在同一 harness 中的完成率。Claude Code 的核心代码和 `ScheduleWakeup` 内部实现未公开，报告只描述官方文档承诺。pi 的结论固定在提交 `9823079ad98d39f3587286c8d9f29556dfb3687b`，未来版本可能调整队列、压缩和 session schema。Codex 结论将固定到检索时的上游提交。

官方产品文档与源码属于同一组织来源集，不能把多个页面误算成完全独立的三方验证。实现独有事实标记为上游单源高可信；“三层循环”“分布式 goal”与设计建议属于跨实现综合，而非任何单一来源的原话。

### Counterevidence Register

- **Claude 的 `/goal` 不是外部事实验证器。** Evaluator 只能读取 conversation，不会独立运行测试或读取文件。因此它能分离完成判断，但不能替代确定性 verification。[6]
- **Codex 有一等 goal 类型，但不等于有 goal loop。** `UserGoalUpdate` 被持久化，却明确不启动 model step；执行仍需要 turn submission 或 automation。[30][31]
- **pi compaction 中出现 `## Goal`，但 core 仍无 Goal 对象。** 该字段是语义摘要协议，不是 continuation predicate。[18][14]
- **Recurring automation 不保证趋近完成。** Claude `/loop` 与 Codex scheduled tasks 决定何时再次运行；若没有 verifier、进度状态与停止政策，它们可能只是重复同一 prompt。[10][36]


## Recommendations

### 对 harness 设计者

1. **显式定义五元目标协议。** 保存 intent、definition of done、progress state、verifier 与 authority。不要把“模型说完成”当作唯一完成标准。
2. **拆分三个循环。** 内层工具循环、goal evaluator 与 scheduler 分别拥有状态、预算、取消句柄和 observability span。
3. **优先确定性 verifier。** 测试、类型检查、lint、产物 hash 与外部状态查询优先于语言模型 evaluator。必须使用 judge 时，让它读取可验证证据，而非主 agent 的自述。
4. **给每层设置界限。** 内层限制 tool/model iterations，goal loop 限制 turn、token、时间和无进展次数，scheduler 限制期限、并发、重叠运行和总成本。
5. **把 compaction 当成 schema migration。** 摘要必须保留目标、约束、已完成项、未完成项、失败原因、外部副作用和下一验收点，并对摘要做回归测试。
6. **把停止原因持久化。** 至少区分完成、不可能、终端失败、可重试、等待审批、用户取消与定时等待。
7. **恢复前先观察。** 不自动重放中断工具。先检查文件、进程、部署、消息或远端任务的真实状态，再决定重试或补偿。

### 对使用者

使用 `/goal` 或类似能力时，把条件写成主 agent 能在 conversation 中展示证据的结果，例如测试命令与预期输出。使用 `/loop` 时，把它视为“定时重新提问”，而不是完成保证。对长任务，把进度与验收状态写入仓库或 session 工件，避免只依赖压缩后的聊天历史。

## Bibliography

[1] Microsoft. (2026). [Agent Looping](https://learn.microsoft.com/en-us/agent-framework/agents/looping)
[2] Microsoft. (2026). [Agent Harness](https://learn.microsoft.com/en-us/agent-framework/concepts/harness)
[3] Microsoft. (2026). [The Coding Harness Behind GitHub Copilot in VS Code](https://code.visualstudio.com/blogs/2026/05/15/agent-harnesses-github-copilot-vscode)
[4] AG2. (2026). [The Agent Harness](https://docs.ag2.ai/latest/docs/beta/agent_harness/)
[5] Anthropic. (2026). [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works.md)
[6] Anthropic. (2026). [Keep Claude working toward a goal](https://code.claude.com/docs/en/goal.md)
[7] Anthropic. (2026). [Manage sessions](https://code.claude.com/docs/en/sessions.md)
[8] Anthropic. (2026). [Explore the context window](https://code.claude.com/docs/en/context-window.md)
[9] Anthropic. (2026). [Errors and automatic retries](https://code.claude.com/docs/en/errors.md)
[10] Anthropic. (2026). [Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks.md)
[11] Anthropic. (2026). [Claude Code tools reference](https://code.claude.com/docs/en/tools-reference.md)
[12] Anthropic. (2026). [Claude Code CLI reference](https://code.claude.com/docs/en/cli-reference.md)
[13] Anthropic. (2026). [Claude Code legal and compliance](https://code.claude.com/docs/en/legal-and-compliance.md)
[14] Mario Zechner & pi contributors. (2026). [pi agent loop implementation](https://github.com/earendil-works/pi/blob/9823079ad98d39f3587286c8d9f29556dfb3687b/packages/agent/src/agent-loop.ts)
[15] Mario Zechner & pi contributors. (2026). [pi Agent state and queue implementation](https://github.com/earendil-works/pi/blob/9823079ad98d39f3587286c8d9f29556dfb3687b/packages/agent/src/agent.ts)
[16] Mario Zechner & pi contributors. (2026). [pi agent state and event types](https://github.com/earendil-works/pi/blob/9823079ad98d39f3587286c8d9f29556dfb3687b/packages/agent/src/types.ts)
[17] Mario Zechner & pi contributors. (2026). [pi transcript and message types](https://github.com/earendil-works/pi/blob/9823079ad98d39f3587286c8d9f29556dfb3687b/packages/ai/src/types.ts)
[18] Mario Zechner & pi contributors. (2026). [pi coding-agent compaction implementation](https://github.com/earendil-works/pi/blob/9823079ad98d39f3587286c8d9f29556dfb3687b/packages/coding-agent/src/core/compaction/compaction.ts)
[19] Mario Zechner & pi contributors. (2026). [pi coding-agent session lifecycle](https://github.com/earendil-works/pi/blob/9823079ad98d39f3587286c8d9f29556dfb3687b/packages/coding-agent/src/core/agent-session.ts)
[20] Mario Zechner & pi contributors. (2026). [pi session persistence and branching](https://github.com/earendil-works/pi/blob/9823079ad98d39f3587286c8d9f29556dfb3687b/packages/coding-agent/src/core/session-manager.ts)
[21] Mario Zechner & pi contributors. (2026). [pi session resume and fork runtime](https://github.com/earendil-works/pi/blob/9823079ad98d39f3587286c8d9f29556dfb3687b/packages/coding-agent/src/core/agent-session-runtime.ts)
[22] Mario Zechner & pi contributors. (2026). [pi agent package README](https://github.com/earendil-works/pi/blob/9823079ad98d39f3587286c8d9f29556dfb3687b/packages/agent/README.md)
[23] OpenAI. (2026). [Codex session submission loop](https://github.com/openai/codex/blob/ba0d0e1f74ee0f41c27ef24b37ed5fc030b487e7/codex-rs/core/src/session/handlers.rs)
[24] OpenAI. (2026). [Codex turn input lifecycle](https://github.com/openai/codex/blob/ba0d0e1f74ee0f41c27ef24b37ed5fc030b487e7/codex-rs/core/src/session/turn_input.rs)
[25] OpenAI. (2026). [Codex regular task loop](https://github.com/openai/codex/blob/ba0d0e1f74ee0f41c27ef24b37ed5fc030b487e7/codex-rs/core/src/tasks/regular.rs)
[26] OpenAI. (2026). [Codex inference loop, stop hooks, and compaction](https://github.com/openai/codex/blob/ba0d0e1f74ee0f41c27ef24b37ed5fc030b487e7/codex-rs/core/src/session/turn.rs)
[27] OpenAI. (2026). [Codex model output and tool call handling](https://github.com/openai/codex/blob/ba0d0e1f74ee0f41c27ef24b37ed5fc030b487e7/codex-rs/core/src/stream_events_utils.rs)
[28] OpenAI. (2026). [Codex tool approval and sandbox orchestration](https://github.com/openai/codex/blob/ba0d0e1f74ee0f41c27ef24b37ed5fc030b487e7/codex-rs/core/src/tools/orchestrator.rs)
[29] OpenAI. (2026). [Codex model stream retry policy](https://github.com/openai/codex/blob/ba0d0e1f74ee0f41c27ef24b37ed5fc030b487e7/codex-rs/core/src/responses_retry.rs)
[30] OpenAI. (2026). [Codex explicit user goal representation](https://github.com/openai/codex/blob/ba0d0e1f74ee0f41c27ef24b37ed5fc030b487e7/codex-rs/core/src/context/user_goal.rs)
[31] OpenAI. (2026). [Codex retained goal context](https://github.com/openai/codex/blob/ba0d0e1f74ee0f41c27ef24b37ed5fc030b487e7/codex-rs/core/src/session/retained_context.rs)
[32] OpenAI. (2026). [Codex compaction goal continuity](https://github.com/openai/codex/blob/ba0d0e1f74ee0f41c27ef24b37ed5fc030b487e7/codex-rs/core/src/compact.rs)
[33] OpenAI. (2026). [Codex session resume and compacted history installation](https://github.com/openai/codex/blob/ba0d0e1f74ee0f41c27ef24b37ed5fc030b487e7/codex-rs/core/src/session/mod.rs)
[34] OpenAI. (2026). [Codex resumed history types](https://github.com/openai/codex/blob/ba0d0e1f74ee0f41c27ef24b37ed5fc030b487e7/codex-rs/history/src/lib.rs)
[35] OpenAI. (2026). [Codex CLI documentation](https://learn.chatgpt.com/docs/codex/cli)
[36] OpenAI. (2026). [Codex automations documentation](https://learn.chatgpt.com/docs/automations)
[37] OpenAI. (2026). [Codex scheduled task schema](https://github.com/openai/codex/blob/ba0d0e1f74ee0f41c27ef24b37ed5fc030b487e7/codex-rs/app-server-protocol/src/protocol/v2/plugin.rs)

## Appendix: Methodology

研究按 scope、retrieve、triangulate、outline refinement、synthesis 和 package 六阶段执行。检索从每个产品的官方文档或 canonical GitHub 仓库出发，记录固定提交、代码路径、函数、原句和访问日期。证据即时写入 `evidence.jsonl`，来源身份写入 `sources.jsonl`，避免只保存在会话上下文。

初始提纲按产品平铺。证据显示 `/goal`、agentic tool loop 与 `/loop` 位于不同控制层后，提纲改为先建立三层模型，再映射产品。核心事实由源码或官方行为文档支持；跨产品推论明确标记为综合。最终报告将运行结构、引用、claim-support 与 HTML 校验。

### Claims-Evidence Table

| Claim ID | Major Claim | Evidence Type | Supporting Sources | Confidence |
|---|---|---|---|---|
| C1 | Harness loop 至少分为 tool、goal、recurring 三层 | 跨实现综合 | Microsoft harness、Claude schedule、Codex automation、pi loop | High |
| C2 | Claude `/goal` 是 turn 后 evaluator 重入 | 官方行为文档 | Goal、session、error docs | High |
| C3 | Codex goal 是持久 context mutation，不自动执行 | 固定提交源码 | `user_goal.rs`、`retained_context.rs` | High |
| C4 | pi core 由 transcript 与队列驱动，无一等 Goal | 固定提交源码 | `agent-loop.ts`、`agent.ts`、compaction | High |
| C5 | Compaction 是 goal continuity 协议的一部分 | 跨实现源码与文档 | Claude context、Codex compact、pi compaction | High |
| C6 | Scheduler 与 agentic loop 是不同控制面 | 官方文档与协议源码 | Claude scheduled tasks、Codex automation、pi negative evidence | High |


### Report Metadata

- Research mode: Standard
- Source records: 37
- Evidence records: 79
- Temporal snapshot: 2026-11-02
- Codex commit: `ba0d0e1f74ee0f41c27ef24b37ed5fc030b487e7`
- pi commit: `9823079ad98d39f3587286c8d9f29556dfb3687b`
- Claude Code observed version: `2.1.316`

## Related

- [[wiki/topics/AI Harness]]
- [[wiki/concepts/Agentic Control Loop]]
- [[wiki/concepts/Loop Engineering]]
- [[wiki/concepts/Event-Driven Agent Loop]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Long-Running Agent Harness]]
- [[wiki/topics/Context Management]]
