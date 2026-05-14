---
title: >-
  Use Cases as AI Coding Traceability Anchors
category: syntheses
type: synthesis
status: draft
tags: [requirements, ai-coding, software-engineering, architecture, testing]
sources:
  - conversation:2026-05-14
created: 2026-05-14T00:58:10+08:00
updated: 2026-05-14T00:58:10+08:00
summary: >-
  用例在 AI 编程中的核心价值，是把业务目标、系统边界、模块职责、代码位置和验收标准串成可执行追踪链。
provenance:
  extracted: 0.72
  inferred: 0.25
  ambiguous: 0.03
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-14
aliases:
  - AI 编程中的用例追踪链
  - 用例到代码定位
  - Use Case Traceability for AI Coding
---

# Use Cases as AI Coding Traceability Anchors

## Context

AI 编程的问题不只是“让模型写代码”，而是让模型知道：业务目标是什么，当前系统边界在哪里，行为应该由哪些模块协作完成，代码应该改在哪里，以及什么结果证明修改正确。

用例在这条链路里很有价值，因为它天然站在业务表达和软件实现之间。业务用例说明组织、执行者和系统之间的协作；系统用例说明待开发系统对外承诺的行为；用例规约说明主成功路径、扩展路径、前置条件、后置状态和验收标准。

## Finding / Decision

用例在 AI 编程中的核心价值，是把业务目标、系统边界、模块职责、代码位置和测试标准串成一条可执行追踪链。

```text
业务目标
  -> 业务用例 / 业务流程
    -> 识别业务执行者、参与系统、跨系统交互
    -> 锁定待开发系统边界
      -> 系统用例
        -> 定义外部执行者和系统行为契约
        -> 用例规约
          -> 主成功场景 / 扩展场景 / 业务规则 / 后置状态
          -> 架构映射
            -> UI / API / Application / Domain / Persistence / Integration / Tests
            -> 代码位置映射
              -> AI 定位文件
              -> AI 修改代码
              -> AI 运行测试验证
```

这条链路的关键不是把用例变成更厚的文档，而是让用例成为 AI 可使用的导航对象：它既能从业务目标向下追踪到代码，也能从代码修改向上追踪回业务行为和验收标准。

## Reasoning

### 业务用例用于识别系统边界，而不是直接定位代码

业务用例和业务流程描述目标组织如何完成业务结果。它们展示业务执行者、业务工人、外部系统、内部系统和时间顺序之间的协作。这里的交互可以暴露系统边界，因为跨边界协作必然需要消息、接口、文件、事件或人工交接。

业务用例主要回答：

```text
这件业务结果由哪些角色和系统协作完成？
当前待开发系统在整条业务链里承接哪一段责任？
它和其他系统之间通过什么消息交换？
哪些责任不属于当前系统？
```

因此，业务用例通常不能直接告诉 AI “改哪个文件”。它要先经过系统映射：

```text
业务系统 / 子系统 / 业务能力
  -> 代码仓库 / 服务 / 模块 / API / Owner
```

有了这层映射，AI 才能从业务流程中的系统交互跳到相关代码区域。

### 系统用例是 AI 编程的核心锚点

系统用例聚焦待开发系统边界内的行为。它回答：外部执行者触发什么，系统如何响应，成功后系统进入什么状态，失败时系统如何处理。

这正好能映射到常见代码结构：

```text
系统用例
  -> API / Handler / Controller
  -> Application Service / UseCase / Command Handler
  -> Domain Model / Policy / Rule / State Machine
  -> Repository / External Gateway / Adapter
  -> Test Cases
```

如果仓库里维护了用例到代码位置的映射，AI 就不需要只靠关键词搜索猜位置，而能沿着行为链路定位。

例如：

```text
用例：导出订单报表
入口：POST /order-reports/export
API：src/orders/interface/OrderExportController.ts
应用层：src/orders/application/ExportOrderReportUseCase.ts
领域规则：src/orders/domain/OrderExportPolicy.ts
持久化：src/orders/infra/OrderRepository.ts
异步任务：src/orders/infra/GenerateOrderReportJob.ts
测试：tests/orders/export-order-report.spec.ts
```

这类映射把“系统应该做什么”转成“代码大概在哪里”。

### 用例规约提供“改成什么才算对”

代码位置只解决“在哪里改”。AI 还需要知道“改成什么才算正确”。这个判断来自用例规约和验收标准。

一个对 AI 有用的用例规约至少应该包含：

```text
用例名称
执行者
触发入口
前置条件
主成功场景
扩展 / 异常场景
业务规则
后置状态
验收标准
```

例如“导出订单报表”的主成功场景和扩展场景可以直接变成实现分支、错误码、状态机、幂等逻辑和测试用例：

```text
主成功场景：
1. 用户提交导出请求
2. 系统校验参数
3. 系统校验权限
4. 系统统计订单数量
5. 数量较少时同步生成 CSV
6. 数量较多时创建异步任务
7. 返回下载地址或任务 ID

扩展场景：
- 无权限
- 时间范围过大
- 数据量超限
- 导出任务创建失败
- 重复提交
```

这让 AI 能把自然语言行为约束转成代码分支和测试断言。

### 非行为需求需要补到用例链路旁边

用例主要捕获行为需求。AI 编程还需要质量属性、约束、业务规则、数据生命周期、集成和运维要求。否则模型容易只实现 happy path。

这些需求不一定都适合塞进用例步骤，但应该挂在同一条追踪链上：

```text
性能：超过 10000 条异步导出
安全：普通运营只能导出负责店铺
可用性：任务失败要可重试
可观测性：记录任务状态和失败原因
合规：导出文件保留 7 天后删除
幂等：重复提交相同参数返回已有任务
```

这些内容分别影响缓存、异步、鉴权、审计、重试、状态机、清理任务和测试策略。它们可以作为质量场景、规则表、状态机、数据生命周期或运维要求，连接到同一个系统用例。

### AI 编程需要一张可执行映射表

最有用的工件不是孤立的用例图，而是一张用例到实现的追踪表：

```text
业务用例：订单履约
业务流程步骤：运营导出订单报表
参与系统：订单系统、权限系统、文件系统、任务系统

系统用例：导出订单报表
执行者：运营人员
入口：POST /order-reports/export

代码落点：
- API：src/orders/interface/OrderExportController.ts
- 应用服务：src/orders/application/ExportOrderReportUseCase.ts
- 权限规则：src/orders/domain/OrderExportPolicy.ts
- 导出任务：src/orders/domain/ExportTask.ts
- 仓储：src/orders/infra/OrderRepository.ts
- 文件存储：src/orders/infra/FileStorage.ts
- 测试：tests/orders/export-order-report.spec.ts

验收：
- 主流程测试
- 无权限测试
- 数据量过大异步测试
- 重复提交幂等测试
- 文件过期清理测试
```

这张表就是 AI 编程的导航层。它把业务语言、架构语言、代码语言和测试语言对齐到同一个行为对象上。

### AI 需要三类输入

面向 AI 编程时，用例相关上下文应分成三类：

```text
1. 行为契约：系统应该发生什么
2. 代码定位：这些行为落在哪些模块和文件
3. 验证标准：什么测试、状态、输出证明它做对了
```

缺少行为契约，AI 会按实现猜业务。缺少代码定位，AI 会靠搜索和模式匹配猜文件。缺少验证标准，AI 会写出看似合理但无法验收的代码。

## Implications

用例可以成为 AI 编程中的 traceability spine：

- 从业务目标追踪到业务流程。
- 从业务流程追踪到系统边界。
- 从系统边界追踪到系统用例。
- 从系统用例追踪到模块职责。
- 从模块职责追踪到代码位置。
- 从代码位置追踪到测试与验收。

这要求团队把用例写成可执行上下文，而不是只写成需求归档。最小可用模板可以是：

```text
# AI Coding Use Case Context

## Business Context
业务目标：
业务用例 / 流程：
参与系统：
待开发系统边界：

## System Use Case
执行者：
触发入口：
前置条件：
主成功场景：
扩展 / 异常场景：
后置状态：

## Rules and Qualities
业务规则：
质量属性：
约束：
数据生命周期：
集成要求：
运维 / 审计要求：

## Code Map
UI：
API：
Application：
Domain：
Persistence：
Integration：
Tests：

## Verification
验收测试：
回归测试：
人工检查点：
运行观测指标：
```

这也解释了为什么 [[wiki/sources/Use Case 开发管理 Source Guide]] 中的 “Use Case 管用户目标与系统行为；UI、API、数据库、测试和任务拆分管这个行为如何可见、可调用、可执行、可持久化和可验证” 可以进一步扩展到 AI 编程：AI 需要的不只是代码片段，而是一条可追踪的行为—实现—验证链。

## Related

- [[wiki/sources/Use Case 开发管理 Source Guide]]
- [[wiki/syntheses/Requirements Expression Beyond Use Cases]]
- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/maps/Software Analysis Map]]
- [[wiki/maps/Software Design Map]]
- [[wiki/concepts/Software Analysis Three Generators]]
- [[wiki/topics/Spec-Driven Development]]
- [[wiki/topics/Testing Strategy]]
