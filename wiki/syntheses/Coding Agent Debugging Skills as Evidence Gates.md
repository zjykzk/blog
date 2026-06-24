---
title: Coding Agent Debugging Skills as Evidence Gates
category: syntheses
type: synthesis
status: draft
tags: [agents, skills, ai-coding, debugging, verification, software-engineering]
sources:
  - conversation:2026-06-21
  - conversation:2026-06-23
created: 2026-06-21T20:00:10+0800
updated: 2026-06-23T00:47:58+0800
summary: 高频编码 skill 的核心不是提示词技巧，而是把 agent 的修复、设计、测试和完成声明变成证据门禁、责任账本与反馈回路。
provenance:
  extracted: 0.80
  inferred: 0.20
  ambiguous: 0.00
base_confidence: 0.82
lifecycle: draft
lifecycle_changed: 2026-06-21
aliases:
  - 高频编码 skill 解剖
  - coding skill evidence gates
  - debugging skill feedback loops
  - high-frequency coding skills
relationships:
  - target: "[[wiki/concepts/Agent Skill]]"
    type: extends
  - target: "[[wiki/concepts/Verification Loop]]"
    type: uses
  - target: "[[wiki/topics/Karpathy Guidelines]]"
    type: related_to
  - target: "[[wiki/topics/Testing Strategy]]"
    type: related_to
  - target: "[[wiki/topics/Modern Software Engineering]]"
    type: related_to
  - target: "[[wiki/syntheses/Agent Skill Implementation Landscape]]"
    type: extends
---
# Coding Agent Debugging Skills as Evidence Gates

## Context

高频编码 skill 的研究不应停留在“哪些 GitHub repo star 高”或“哪些 skill 名字常见”。更有价值的问题是：优秀 coding skill 到底在控制什么失败模式？它们如何把人类工程经验转成 agent 可执行的触发条件、阶段门禁、证据要求和完成定义？

本页综合拆解了八组代表性 coding skills：`systematic-debugging`、`verification-before-completion`、`diagnosing-bugs`、`improve-codebase-architecture`、`golang-concurrency`、`webapp-testing`、Vercel React skills，以及 TDD skills。它们共同显示：高质量 coding skill 的本质不是提示词技巧，而是把工程活动中的隐性责任和反馈结构显性化。^[inferred]

## Candidate Landscape

值得优先研究的编程相关 skill repo 包括：

- `obra/superpowers`：代表 skill 包括 `systematic-debugging`、`test-driven-development`、`verification-before-completion`、`requesting-code-review`。它们通常更像严格纪律和行动门禁。
- `mattpocock/skills`：代表 skill 包括 `diagnosing-bugs`、`tdd`、`improve-codebase-architecture`、`codebase-design`。它们偏向真实工程判断、测试 seam、deep module 和实验反馈。
- `anthropics/skills`：官方 Agent Skills repo，代表 skill 包括 `webapp-testing`、`claude-api`、`frontend-design`。它们更像平台能力和工具使用样板。
- `vercel-labs/agent-skills`：React/Next.js 范式型 skill，代表包括 `react-best-practices`、`composition-patterns`。它们把框架运行模型压成规则库。
- `samber/cc-skills-golang`：Go 语言哲学型 skill，代表包括 `golang-error-handling`、`golang-concurrency`、`golang-performance`。它们把语言运行时责任压成可审查规则。
- `wshobson/agents`、`github/awesome-copilot`、`ciembor/agent-rules-books` 等可作为候选池，但需要逐个检查 skill 是否具备触发边界、证据门禁和完成定义。

这些候选可按底层功能分为：工程纪律型、反馈回路型、架构深度型、框架范式型、语言哲学型、浏览器证据型、行为授权型、工具/平台操作型。

## Core Finding

高频编码 skill 的本质是 **证据门禁化的工程反馈回路**。它们并不只是告诉 agent “应该怎么写代码”，而是在关键时刻禁止 agent 越权：没有 loop 不准想，没有 root cause 不准修，没有 failing test 不准写 production code，没有 fresh verification 不准说完成。

一个成熟 coding skill 通常回答五个问题：

1. **触发条件**：什么任务、风险或失败信号必须进入该 skill。
2. **默认失败模式**：agent 在这个场景下最容易犯什么错。
3. **阶段门禁**：每个阶段有什么进入条件和退出条件。
4. **证据要求**：什么外部反馈足以支撑下一步行动或成功声明。
5. **完成定义**：什么状态才算真的完成，而不是语言上看起来完成。

优秀 skill 的共同点不是“内容全面”，而是能把错误行动拦在发生之前，或者把一次失败转成可复用的反馈结构。^[inferred]

## Skill Anatomy 1: systematic-debugging

`obra/superpowers/systematic-debugging` 的第一性规则是：

> No fixes without root cause investigation first.

它默认 agent 最容易犯的错是：把症状当根因、没有复现就修、一次改多个变量、先修后补测试、连续 patch 失败后仍然继续叠补丁。

它把 debugging 拆成四阶段：

1. **Root Cause Investigation**：读完整错误、稳定复现、检查最近变化、在多组件边界加诊断、追溯坏值来源。
2. **Pattern Analysis**：寻找同类工作代码，完整阅读 reference implementation，列出 working path 与 broken path 的差异。
3. **Hypothesis and Testing**：写出单一假设，用最小变更验证，失败后回到分析而不是叠 patch。
4. **Implementation**：先创建 failing test，再做单一根因修复，最后验证；若三次 fix 失败，停止并质疑架构。

它的配套 technique 强化了这个模型：`root-cause-tracing` 要求沿调用链回溯坏状态的源头；`defense-in-depth` 要求在 entry point、business logic、environment guard 和 debug instrumentation 多层防御；`condition-based-waiting` 要求等待真实条件而不是猜时间。

`systematic-debugging` 的底层逻辑是：在修复之前，先把 bug 从“现象”变成“可复现对象”，再从“可复现对象”变成“因果链”，最后才允许代码变更。它更像纪律法庭，重点是防止 agent 在没有根因时行动。

## Skill Anatomy 2: verification-before-completion

`obra/superpowers/verification-before-completion` 的第一性规则是：

> No completion claims without fresh verification evidence.

它解决的不是“怎么写代码”，而是“agent 什么时候有资格说完成”。它默认 agent 容易把代码已修改、逻辑上看起来合理、历史测试通过、子 agent 汇报成功、局部检查通过，误结算为“已完成”。

它的核心结构是 Claim-Evidence Gate：

1. **Identify**：我准备声明什么？什么命令或观察能证明这个 claim？
2. **Run**：运行完整、新鲜、覆盖当前状态的验证命令。
3. **Read**：读取完整输出、exit code 和失败数量。
4. **Verify**：判断输出是否真的支持 claim。
5. **Only then**：只有在证据支持后才声明完成；否则报告实际状态。

这个 skill 的底层哲学是：在工程系统里，语言没有证明力，只有可复现证据有证明力。完成不是主观状态，而是系统状态；不同 claim 需要不同证据。它和 `systematic-debugging` 形成闭环：没有根因不准修，没有验证不准说完成。

## Skill Anatomy 3: diagnosing-bugs

`mattpocock/skills/diagnosing-bugs` 的第一性规则是：

> Build a feedback loop. This is the skill.

它与 `systematic-debugging` 的差异在于：`systematic-debugging` 首先问“你有根因吗”，而 `diagnosing-bugs` 首先问“你有 tight feedback loop 吗”。它默认 agent 容易在没有 red-capable loop 时读代码生成解释。

它把 bug 诊断拆成六阶段：

1. **Build a feedback loop**：构造 tight、red-capable、deterministic、fast、agent-runnable 的 pass/fail loop。可用 failing test、curl script、CLI fixture、headless browser、trace replay、throwaway harness、fuzz loop、bisect harness、differential loop 或 HITL script。
2. **Reproduce + minimise**：确认 loop 抓到用户 exact symptom，并把复现裁剪到每个剩余因素都是 load-bearing。
3. **Hypothesise**：先生成 3-5 个 ranked、falsifiable hypotheses；每个 hypothesis 必须能预测改变某变量后的结果。
4. **Instrument**：每个 probe 必须对应某个 prediction；优先 debugger/REPL，其次 targeted logs，避免 log everything。
5. **Fix + regression test**：在 correct seam 写 regression test；如果没有 correct seam，这本身就是架构发现。
6. **Cleanup + post-mortem**：原始 loop 变绿、regression pass、debug logs 清理、throwaway prototypes 删除，并把正确 hypothesis 写入 commit/PR。

它的底层逻辑是：debug 的第一资产不是聪明解释，而是能稳定让 bug 红绿变化的反馈回路。最小复现是因果结构的显影剂；correct seam 是架构质量的投影。

## Skill Anatomy 4: improve-codebase-architecture

`mattpocock/skills/improve-codebase-architecture` 处理的不是已经显现的 bug，而是更慢、更隐蔽的架构摩擦：代码还能跑，测试也可能通过，但理解成本、修改成本和测试成本正在升高。

它的核心目标是 surface architectural friction and propose deepening opportunities：把 shallow modules 变成 deep modules，提升 testability 和 AI-navigability。

它依赖 `codebase-design` 的词汇：

- **Module**：任何有 interface 和 implementation 的东西，可大可小。
- **Interface**：调用者为了正确使用 module 必须知道的一切，包括签名、invariants、ordering constraints、error modes、required configuration 和 performance characteristics。
- **Depth**：leverage at the interface。调用者每学习一单位 interface，能获得多少行为能力。
- **Seam**：可以在不改当前位置代码的情况下改变行为的位置，是 interface 所在处。
- **Adapter**：seam 上满足 interface 的具体实现角色。
- **Leverage**：一份 implementation 服务 N 个 callers 和 M 个 tests。
- **Locality**：变化、bug、知识和验证集中在一个地方，而不是散到 callers。

这个 skill 的关键判断工具是 deletion test：如果删除一个 module，复杂度是消失了，还是扩散回 N 个 callers？如果复杂度消失，它可能只是 pass-through；如果复杂度扩散，它可能真的在集中复杂度。

它的底层逻辑是：架构改进不是把代码切得更小，也不是把层数堆得更多，而是重新安置复杂度。用更小、更稳定、更贴近领域语言的 interface，把分散在 caller、测试和调用顺序里的复杂行为吸收到 deep module 内部。测试困难、no correct seam、hidden coupling 和 repeated patch failure 都是架构反馈。

## Skill Anatomy 5: golang-concurrency

`samber/cc-skills-golang/golang-concurrency` 代表语言哲学型 skill。它不是通用 debug workflow，而是把 Go 并发的运行时责任压成规则。

它的 persona 是：

> Every goroutine is a liability until proven necessary — correctness and leak-freedom come before performance.

这句话反转了“goroutine 很轻量，所以大胆使用”的常见错觉。Go 启动 goroutine 的语法很便宜，但每个 goroutine 都引入生命周期、取消、等待、错误传播、共享状态、资源释放和背压责任。

它的核心原则包括：

- 每个 goroutine 必须有 clear exit。
- channel 传递 ownership，默认发送 value/copy，不用 pointer 制造隐形共享内存。
- 只有 sender 关闭 channel。
- channel direction (`chan<-`, `<-chan`) 让编译器约束 ownership。
- 默认 unbuffered channel，buffer 需要 measured justification，因为 buffer 会隐藏 backpressure。
- 每个阻塞 `select` 都要考虑 `ctx.Done()`。
- hot loop 里避免重复 `time.After`，timer 也是资源。
- 并发代码需要 `go test -race ./...`、`go.uber.org/goleak`、pprof 或 stress loop 这类工具化证据。

它没有神化 channel，而是给出 channel / mutex / atomic / sync.Map / sync.Once / singleflight / errgroup 的责任分工。成熟 Go 并发观不是“channel 比 lock 高级”，而是不同同步原语表达不同 ownership、contention 和 lifecycle 模型。

`golang-concurrency` 的底层逻辑是：Go 把并发启动做得太容易，因此高质量 Go 并发 skill 必须把注意力从“怎么并发”拉回“谁负责这个并发活动”。每个 goroutine 都是一笔责任负债，必须在启动前结算 exit、cancel、wait、error、ownership、backpressure 和 verification。

## Skill Anatomy 6: webapp-testing

`anthropics/skills/webapp-testing` 代表浏览器证据型 skill。它的核心不是完整测试理论，而是防止 agent 根据源码、静态 HTML、想象中的 DOM 或未加载完成的页面下结论。

它的关键 decision tree 是：

- 如果是 static HTML，可以直接读 HTML file 识别 selectors。
- 如果是 dynamic webapp，则必须进入 browser runtime。
- 如果 server 未运行，先用 `scripts/with_server.py --help`，再用 helper 管 server lifecycle。
- 如果 server 已运行，采用 reconnaissance-then-action：navigate → wait for networkidle → screenshot/inspect DOM → identify selectors from rendered state → execute actions。

它的底层哲学是：现代 web app 的真实行为存在于浏览器运行时，而不是源码或静态 HTML 里。前端真实状态由 JS 执行、hydration、routing、network、state initialization、CSS visibility 和 user events 共同生成。

因此，前端 claim 必须进入浏览器：启动 server，等待 runtime ready，侦察真实 DOM/screenshot/console，再基于 discovered selectors 操作。点击本身不是验证；断言用户可见结果、DOM 状态、network result 或 console clean 才是验证。^[inferred]

这个 skill 和 `diagnosing-bugs` 的关系是：它给出了 web app 场景下 tight browser feedback loop 的构造方法。它和 `verification-before-completion` 的关系是：它提供完成声明所需的 screenshot、DOM assertion、console log 和 browser behavior evidence。

## Skill Anatomy 7: Vercel React Skills

Vercel 的 `react-best-practices` 和 `composition-patterns` 代表框架范式型 skill。它们处理的不是单个 bug，而是 React/Next.js 代码形态是否符合框架运行模型。

`react-best-practices` 把 70 条规则分为 8 类并按 impact 排序：

1. Eliminating Waterfalls：避免不必要的 sequential await，用 `Promise.all`、start early await late、Suspense 等表达真实 async dependency。
2. Bundle Size Optimization：避免 barrel imports、控制 module graph、用 dynamic import、延迟 third-party、只在 feature activated 时加载模块。
3. Server-Side Performance：区分 request scope、process scope、client scope；避免把 request/user data 放进 mutable module-level state。
4. Client-Side Data Fetching：请求去重、global event listener 去重、passive listener、localStorage schema。
5. Re-render Optimization：避免不必要 re-render，能 render 派生的值不要存成 state，不要用 effect 同步可派生状态。
6. Rendering Performance：content-visibility、resource hints、hydration flicker、script defer/async 等。
7. JavaScript Performance：Map/Set lookup、loop、hoist RegExp、idle callback 等。
8. Advanced Patterns：effect event deps、handler refs、init once、useLatest。

这些规则的共同点是：React/Next.js 性能问题通常不是单个函数慢，而是时间结构、模块图、渲染边界、状态来源和 server/client scope 被写错。

`composition-patterns` 则处理组件 API 设计，核心反模式是 boolean prop proliferation。每增加一个 boolean prop，组件可能状态空间翻倍，非法组合增多，测试矩阵膨胀，调用者必须知道隐性组合规则。它建议用 explicit variants、compound components、provider context 和 `state/actions/meta` context interface，把业务变体显式化，让 UI consume interface 而不是具体 state implementation。

这组 skill 的底层逻辑是：React/Next.js 代码的很多失败不是语法错误，而是框架运行模型错配：把可并行的异步写成瀑布，把小 import 写成大模块图入口，把 request-local 数据放进 process-wide module scope，把可派生值复制成 state，把业务变体压成 boolean prop 组合。

## Skill Anatomy 8: TDD Skills

TDD skills 以 `obra/superpowers/test-driven-development` 和 `mattpocock/skills/tdd` 为代表。两者都讲 TDD，但重心不同：obra 是铁律型，Matt 是接口设计型。

obra 的第一性规则是：

> No production code without a failing test first.

它要求 RED → GREEN → REFACTOR：先写一个最小失败测试，确认它因正确原因失败，再写最小 production code 让它通过，最后只在 green 后重构。它特别反对“先写实现，再补测试”，因为实现会污染测试想象；测试后置容易测试“代码做了什么”，而不是“代码应该做什么”。

Matt 的第一性规则是：

> Tests should verify behavior through public interfaces, not implementation details.

它反对 horizontal slicing：不要一次写完一批 tests，再一次写完一批 implementation。正确方式是 vertical slice：一个行为测试 → 一个最小实现 → 下一行为测试。它还强调好测试应该是 integration-style，通过 public API 测 observable behavior，能 survive internal refactors；mock 应该只放在 system boundaries，而不是 mock 自己的 modules/internal collaborators。

TDD 的底层逻辑是：测试不是实现后的背书，而是实现前的行为契约。只有一个 public-interface test 先因正确原因失败，再由最小实现变绿，才能证明测试确实捕获了缺失行为，也才能让代码在可验证反馈中逐步生长。

## Comparative Frame

不同 coding skill 的差异来自它们面对的主要不确定性不同：

| Skill 类型 | 核心问题 | 门禁 / 控制手段 |
|---|---|---|
| `systematic-debugging` | 如何避免症状修复 | root cause before fix |
| `verification-before-completion` | 如何避免虚假完成声明 | fresh verification evidence |
| `diagnosing-bugs` | 如何把 bug 变成可实验对象 | tight red-capable loop |
| `improve-codebase-architecture` | 如何重新安置复杂度 | depth / seam / locality / deletion test |
| `golang-concurrency` | 如何结算并发责任 | exit / cancel / wait / ownership / backpressure |
| `webapp-testing` | 如何进入浏览器事实 | browser runtime evidence |
| Vercel React skills | 如何符合框架物理约束 | async / bundle / scope / state / composition rules |
| TDD skills | 如何让行为先于实现 | failing public-interface test |

它们合在一起形成一条更完整的 agent coding 宪法：

> 没有 loop，不准想；没有 root cause，不准修；没有 failing public-interface test，不准写行为实现；没有 responsibility account，不准启动并发活动；没有 browser runtime evidence，不准声明前端行为；没有 fresh verification，不准说完成。

## Transferable Workflow

可以把这些 skill 压缩成一个通用 coding-agent workflow：

```text
Task / Symptom / Behavior Need
  ↓
Classify Risk Surface
  - bug?
  - new behavior?
  - architecture friction?
  - concurrency?
  - frontend runtime?
  - framework performance?
  ↓
Build Feedback or Responsibility Gate
  - red-capable loop
  - public-interface failing test
  - goroutine responsibility ledger
  - browser evidence loop
  - claim-evidence gate
  ↓
Act in Small Authorized Steps
  - one hypothesis
  - one behavior
  - one variable
  - one minimal fix
  ↓
Verify Against the Right Surface
  - original symptom
  - regression test
  - public API behavior
  - race/leak tools
  - Playwright DOM/screenshot/console
  - build/test/lint/profile outputs
  ↓
Refactor / Deepen / Ratchet
  - improve seam
  - update tests
  - remove debug scaffolding
  - record postmortem or skill rule
  - escalate to architecture if repeated failure or no correct seam
```

## Personal Rules to Absorb

- Bugfix 前必须能写出根因句：我认为根因是 X，证据是 Y，我将用 Z 验证。
- 多组件问题先画边界：输入、输出、配置、状态在哪一层第一次变坏。
- 错误点和根因点分开记录：错误点是坏状态被发现的位置，根因点是坏状态被制造或允许通过的位置。
- Flaky bug 的进展可以是提高复现率：1% → 10% → 50% 本身就是信号增强。
- 每个 hypothesis 必须能预测一个实验结果；不能预测的解释只是 vibe。
- Instrumentation 必须服务 prediction；debug log 要有唯一 tag 并在结束时清理。
- Regression test 要在 correct seam；没有 seam 是架构反馈，不是测试小问题。
- 三次 patch 失败后停止继续补丁，改问当前架构是否在稳定生成 bug。
- 完成声明必须带 fresh verification evidence；不能用信心、推理、历史输出或子 agent 汇报代替证据。
- 每个 goroutine 启动前都要回答 owner、exit、cancel、wait、error propagation、shared state、channel ownership、backpressure 和 verification。
- 前端 claim 必须进入 browser runtime；源码推断不能替代 Playwright/DOM/screenshot/console evidence。
- React/Next.js 性能优先看 async waterfall、bundle graph、server/client scope、derived state 和 component API state space，不要先做微优化。
- TDD 中没看过 RED，就不要相信 GREEN；测试必须测 public interface 的 observable behavior，而不是 implementation detail。

## Related

- [[wiki/concepts/Agent Skill]]
- [[wiki/concepts/Verification Loop]]
- [[wiki/concepts/Feedback Loops]]
- [[wiki/concepts/Harness Ratchet]]
- [[wiki/topics/Karpathy Guidelines]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/topics/Modern Software Engineering]]
- [[wiki/concepts/engineering-thinking|Engineering Thinking]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/topics/AI Harness]]
- [[wiki/syntheses/Agent Skill Implementation Landscape]]
- [[wiki/syntheses/AI Harness × Testing Strategy]]
- [[wiki/syntheses/Agentic Engineering × Verification Loop]]
