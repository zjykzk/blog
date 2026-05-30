---
title: >-
  Grokking Simplicity Taming FP Source Guide
category: sources
type: source
status: draft
tags: [book, software-engineering, architecture, systems, testing]
sources:
  - mobu/读书/grokking_simplicity：taming_fp.md
created: 2026-05-30T18:11:07+0800
updated: 2026-05-30T18:11:07+0800
summary: >-
  这页保存《Grokking Simplicity》函数式编程读书笔记：用 action、calculation、data、时间线、分层和响应式架构降低代码复杂度。
provenance:
  extracted: 0.86
  inferred: 0.14
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-30
aliases:
  - grokking simplicity：taming fp
  - Grokking Simplicity 函数式编程读书笔记
  - Taming Functional Programming
---
# Grokking Simplicity Taming FP Source Guide

> Source: `mobu/读书/grokking_simplicity：taming_fp.md`

## Capture Policy

这页保留一份《Grokking Simplicity》相关读书笔记的 source 层内容。它不把材料直接提升为稳定函数式编程概念页，而是保存笔记中关于 action、calculation、data、抽象分层、时间线、响应式架构和洋葱架构的结构化理解。

## What It Covers

这份笔记关心的核心问题是：函数式编程如何把代码复杂度拆开，让依赖时间、顺序和外部世界的部分尽量变少，让纯计算和数据结构承担更多逻辑。

它适合连接 [[wiki/topics/Modern Software Engineering]]、[[wiki/maps/Software Design Map]]、[[wiki/syntheses/信息流与状态流转设计原则]] 和 [[wiki/topics/Testing Strategy]]。其中，函数式编程不是单纯语法风格，而是一套复杂度治理方法：区分 action / calculation / data，减少 action，把 calculation 做成可分析、可测试、可组合的结构。

## Preserved Content

### 核心问题：复杂与简单的分离

《Grokking Simplicity》的函数式视角可以理解为一种任务分解方法：把复杂的部分和简单的部分分开，避免简单逻辑被时间、顺序、外部状态和副作用拖复杂。

在这套视角里，代码中的东西可以按复杂度大致分成三类：

```text
data < calculation < action
```

- data 最简单，因为它只是被记录、传递和读取的值；
- calculation 只依赖输入，给定同样输入就得到同样输出；
- action 最复杂，因为它依赖执行时间、执行次数、外部世界和执行顺序。

因此，函数式编程的主线不是“到处写函数”，而是尽可能把 action 中的逻辑抽成 calculation，把可变状态变成不可变 data，把时间和顺序作为显式设计对象。

### Action：依赖时间、次数和顺序的代码

Action 的执行效果依赖时间、执行次数或外部世界。写文件、发请求、改全局变量、读当前时间、访问数据库、触发 UI 更新，都属于 action。

Action 的治理重点是控制顺序、保证只执行一次、减少外部影响，并尽量缩小范围。

常见策略包括：

- 最小化 action 的数量和范围；
- 只让 action 负责和外部世界交互；
- 把 action 内部可抽出的判断、转换、筛选和组合逻辑移到 calculation；
- 用不可变数据结构或 Copy on Write，把“读可变数据”变成“读不可变快照”；
- 调用外部函数或被外部函数调用时，用参数拷贝和返回值拷贝保护数据不变性；
- 简化代码对时间和顺序的依赖；
- 对多线程或异步场景，显式规定不同 action 的执行顺序、执行次数和冲突语义。

这里的拷贝不是为了形式上的“纯”，而是为了防止一个 action 在看似无关的位置改变共享数据，从而把原本可以推理的代码拖回时间线复杂度里。

### Calculation：只和输入有关的代码

Calculation 只和输入有关。同样的输入总是得到同样的输出，不依赖当前时间、外部状态或执行次数。

Calculation 的价值在于它更容易被静态分析、数学工具和测试策略处理。它不需要知道什么时候执行，也不需要担心被执行几次。只要输入明确，输出就可以被验证。

因此，设计代码时应尽量问：

- 这段 action 里有没有一部分其实只是计算？
- 这段逻辑能否改写成输入到输出的转换？
- 是否可以用 data 传入需要的信息，而不是在 calculation 内部读取外部状态？
- 测试是否可以直接覆盖 calculation，而不是绕过一串外部依赖？

这与 [[wiki/topics/Testing Strategy]] 的主线相通：越多逻辑落在 calculation，测试就越能直接验证核心行为，而不是依赖脆弱的环境搭建。

### Data：记录事件和长期规则的材料

Data 是被记录、传递和组织的信息。笔记中特别强调“记录事件的数据，每次事件一份数据”。这和事件溯源、不可变日志的思路接近：事件一旦发生，就作为事实保存下来，而不是被后续状态覆盖。^[inferred]

Data 的设计问题不只是“有什么字段”，还包括：

- 如何组织数据，让访问高效；
- 如何记录长时间不坏的规则；
- 如何捕捉主使用场景中的重点信息；
- 如何在性能和不可变性之间做权衡。

不可变 data 会让推理变简单，但可能带来拷贝成本。笔记中特别提到效率问题：作者认为拷贝在很多场景下是省事的，可以通过浅拷贝和深拷贝组合来控制成本。这里的关键不是永远深拷贝，而是把数据共享和修改边界说清楚。

### 函数式编程的思维方式

这份笔记把函数式思维压成两个动作：

1. 区分 action、calculation、data；
2. 用函数抽象组织 calculation。

函数抽象的价值不是把代码拆碎，而是让函数签名表达意图，让函数体停留在同一抽象层，让调用者不必同时理解语言细节、通用业务规则和具体业务规则。

### 分层模式：函数签名表达意图，函数体保持同层

直接实现时，函数签名应表达要解决的问题；函数体应使用相同抽象层次的代码来解决这个问题。

这里的关键疑问是：不要出现跨层。一个函数如果同时混合语言基础操作、通用业务逻辑、特定业务逻辑和基础设施调用，读者就必须在多个抽象层之间来回跳。

可以用函数调用图检查分层问题：

- 从全局视角看层之间的交互：是否存在跨层调用；
- 从层视角看某一层的实现：是否有函数明显落在错误层；
- 从函数视角看局部实现：调用的函数是否处在同一层；
- 如果函数体混合基础语言特性和高层函数调用，可以把低层操作抽成同层函数。

这种分层思想与 [[wiki/concepts/Conceptual Integrity]] 和 [[wiki/maps/Software Design Map]] 相通：可读代码不是信息越多越好，而是每一层只暴露当前需要面对的问题。

### 抽象边界：应对不确定性与降低信息负载

抽象边界的好处包括：

- 应对不确定性；
- 减少信息负载；
- 让读者关注主要问题；
- 减少模块耦合；
- 让代码更容易读写。

何时停止抽象没有机械公式。笔记中保留了一个判断：当你觉得 OK 的时候就停，这里需要品味。这个“品味”可以理解为在可读性、变化预期、重复程度、调试成本和抽象负担之间做判断。^[inferred]

### Timeline：把时间作为一等概念

Timeline 用来表示 action 在时间上的执行关系。它适合分析多线程、异步或事件驱动代码中可能出现的不同执行顺序。

基本画法是：

- 有先后顺序的 action 放在同一条时间线上；
- 同时发生、乱序发生或没有现有顺序关系的 action 放在不同时间线上；
- 需要考虑执行环境的线程模型；
- 中间不会插入其他 action 的一组动作可以合在一个框里；
- 如果一个时间线执行完以后只多出一条时间线，可以合并；
- 虚线表示不同时间线之间的顺序约束。

Timeline 的作用是让一段代码在多线程执行时的不同顺序显形，从而发现可能不符合预期的执行顺序，也就是 bug。

核心原则：

- 时间线越少越好；
- 时间线越短越好；
- 不同时间线共享的资源越少越好；
- 有资源共享时，必须协调不同时间线访问资源的顺序；
- 锁、队列、WaitGroup、Once、cut 等机制都是在控制时间；
- 控制时间线本身应该成为显式设计对象。

这和 [[wiki/syntheses/信息流与状态流转设计原则]] 里的运行时结构问题相连：状态变化不是静态字段问题，而是对象在时间中如何被合法推进、观察和协调的问题。

### Reactive architecture：解耦原因和效果

响应式架构把“原因”和“效果”解耦。

普通写法中，很多地方会修改同一份数据；而某些逻辑又依赖这份数据的变化。于是，每个修改数据的地方都要记得调用依赖逻辑。修改原因越多，调用遗漏和重复的风险越高。

响应式做法是封装这份数据，让依赖逻辑监听数据变化。数据变化是原因，监听逻辑是效果；原因不再直接调用每个效果。

这种结构接近观察者模式：

- 好处是原因和效果解耦；
- 坏处是依赖关系不再直观，读代码时可能不知道哪些逻辑依赖这份数据；
- 一个时间线上的 action 变少了；
- 时间线可能变多了；
- 共享变量通常会减少。

笔记中把响应式架构定义为：反转“先做 x，后做 y”，改成“当 x 发生时，触发 y”。

### Pipeline：把操作步骤当作流水线

响应式架构的极限形式是 pipeline：每个操作都是流水线中的一环，一步一步触发。JavaScript 中的 Promise 可以作为参考。

Pipeline 的价值在于把步骤之间的时间关系显式化，让每一步的输入输出更清楚。它也会改变复杂度形态：局部 action 少了，但整体时间线和触发关系可能变多。

因此，pipeline 不是无条件更简单。它适合把顺序和转换链条说清楚，但如果依赖关系隐藏太深，也会牺牲直观性。^[inferred]

### 洋葱架构：把 action 放外层，把领域层推向 calculation

笔记把洋葱架构和函数式编程连接起来：

- 交互层对外提供接口，对内使用基础设施，主要是 action；
- 领域层尽量做成 calculation；
- 编程语言层提供表达这些结构的基础能力。

这个划分的价值在于把外部世界、基础设施和时间依赖压到外层，把业务规则尽量留在纯计算中。这样领域逻辑更容易测试、组合和推理。

权衡点包括：

- 可读性；
- 性能；
- 紧急业务；
- 技术债记录。

函数式风格和洋葱架构契合的原因，是高阶函数天然支持装饰者模式，可以把横切逻辑包在外层，同时不污染内层计算。

### 最重要的三个点

这份笔记最后把《Grokking Simplicity》的要点压成三条：

1. 尽可能从 action 中抽取 calculation；
2. 使用高阶函数做抽象；
3. 封装并发代码：对不同时间线中的 action 明确语义，包括不同顺序执行的语义和多次执行的语义。

## Integration Decisions

这页暂时作为 book/source guide 保存，不直接创建“函数式编程”概念页。原因是当前 wiki 已有 [[wiki/maps/Software Design Map]]、[[wiki/syntheses/信息流与状态流转设计原则]]、[[wiki/topics/Testing Strategy]] 等相关页面，本页更适合先作为源材料，为后续的软件设计、测试和并发治理综合提供证据。

后续可提升的方向包括：

- 把 action / calculation / data 提升为软件复杂度分解模型；
- 把 timeline 方法整合进并发或运行时状态流转主题；
- 把“领域层尽量 calculation、交互层承接 action”整合进架构设计与测试策略。

## Open Questions

- 拷贝策略如何在性能和不可变性之间选择，哪些场景适合浅拷贝、深拷贝或结构共享？
- “什么时候停止抽象”能否从品味进一步拆成可操作检查项？
- Timeline 是否应该单独沉淀成并发代码阅读和设计方法？

## Related

- [[wiki/topics/Modern Software Engineering]]
- [[wiki/maps/Software Design Map]]
- [[wiki/syntheses/信息流与状态流转设计原则]]
- [[wiki/topics/Testing Strategy]]
- [[wiki/topics/High Concurrency]]
- [[wiki/concepts/Conceptual Integrity]]
- [[wiki/maps/Reading Map]]
