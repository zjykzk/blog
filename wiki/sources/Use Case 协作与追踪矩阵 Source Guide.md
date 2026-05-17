---
title: >-
  Use Case 协作与追踪矩阵 Source Guide
category: sources
tags: [requirements, software-engineering, architecture, testing]
sources:
  - conversation:2026-05-16
created: 2026-05-16T00:23:43+08:00
updated: 2026-05-16T00:23:43+08:00
summary: >-
  这页保存一份关于 Use Case 如何由产品、业务、RD、QA 协作完成，并通过领域模型、UI、API、测试和任务矩阵追踪到代码落地的中文讲解。
provenance:
  extracted: 0.92
  inferred: 0.08
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-16
aliases:
  - 用例协作与追踪矩阵
  - Use Case 协作流程
  - 用例到领域模型 API UI
---

# Use Case 协作与追踪矩阵 Source Guide

> Source: conversation:2026-05-16

## Capture Policy

这页保存一次关于 Use Case 开发协作的会话式教学内容。它不重复定义 Use Case 本体，而是保留“谁先写、谁补充、什么时候补领域模型/API/UI、如何用追踪矩阵拆到代码任务”的协作流程与示例。

## What It Covers

Use Case 不只是产品写给研发的需求文本，也不是 RD 自己推导代码结构的技术草稿。它应该是产品/BA、领域专家、RD/架构师、QA、设计共同围绕一个业务目标形成的行为契约，再向外连接 UI、API、领域模型、测试和开发任务。

这页补充 [[wiki/sources/Use Case 开发管理 Source Guide|Use Case 开发管理 Source Guide]]：前者说明 Use Case 如何关联开发工件；本页说明这些工件在团队协作中何时出现、由谁补充、如何保持可追溯。

## Preserved Content

### 基本分工

Use Case 的 owner 可以是产品经理或业务分析师，但它必须是跨职能协作产物。

```text
产品 / BA：主笔 Use Case 初版，表达用户目标、主流程、业务异常和验收标准。
领域专家 / 业务方：校验术语、业务规则、状态变化和真实流程。
RD / 架构师：校准系统边界、领域模型、技术约束、事务边界、幂等和外部依赖。
QA：补充验收标准、异常路径、边界条件和测试场景。
设计 / UI：把 Use Case 映射成页面流、交互状态、错误态和文案。
```

产品先写的初版不是“定稿需求”，而是一个可讨论的锚点。好的 Use Case 通常不是一次写完，而是在业务校验、技术建模、交互设计和测试推导中被不断修正。

### 协作流程

一个实用流程是：

```text
1. 产品/BA 写 Use Case 初版
2. 领域专家 / 业务方校验业务语义
3. 产品 + RD + QA 做 Use Case Review
4. RD / 架构师补领域模型
5. 设计 / 产品补 UI Flow
6. RD 补 API 设计和应用层落点
7. QA 补测试用例
8. 开发任务按同一个 Use Case ID 拆分
```

每一步的产物不同：

```text
Use Case 初版：用户目标、参与者、主成功场景、异常场景、后置状态。
业务校验：术语、业务规则、真实状态变化、例外规则。
Review：系统边界、范围进出清单、核心领域对象、遗漏异常。
领域模型：聚合、实体、值对象、状态机、不变量、领域服务。
UI Flow：页面流转、操作入口、加载态、错误态、空态、成功态。
API 设计：Endpoint、Request/Response、错误码、幂等、权限、一致性约束。
测试用例：主路径、异常路径、边界值、状态流转、回归范围。
开发任务：前端、后端 API、应用层、领域层、基础设施、测试任务。
```

这条流程和 [[wiki/maps/Software Analysis Map|Software Analysis Map]] 中“系统用例到应用服务、业务规则到领域逻辑、执行者到接口入口、异常流程到错误处理”的衔接关系一致。

### 什么时候补领域模型

领域模型应该在 Use Case 初版之后、Use Case Review 阶段开始出现。初版阶段只需要识别必要的领域词汇，不需要完整建模。

例如“购买专栏”初版里先出现：

```text
用户
专栏
订单
支付
阅读权限
价格
```

Review 时，RD/架构师再把这些词推进为领域模型问题：

```text
什么叫专栏可购买？
订单有哪些状态？
支付成功前是否授予权限？
用户已经购买后再次点击购买怎么办？
待支付订单是否复用？
价格以什么时候为准？
```

轻量领域模型可以这样沉淀：

```text
核心实体 / 聚合：
- Column
- Order
- ColumnAccess
- Payment

核心状态：
- Column: Published / Unpublished
- Order: PendingPayment / Paid / Closed
- ColumnAccess: Active / Revoked

关键规则：
- 只有 Published 且 purchasable=true 的专栏可以购买。
- 一个用户对一个专栏只能拥有一份有效购买权限。
- 支付成功后才授予阅读权限。
- 待支付订单在有效期内可以复用。
- 订单价格使用创建订单时的价格快照。
```

领域模型不是 Use Case 的附录装饰，而是让 Use Case 中的行为可以被稳定执行的业务结构。它连接到 [[wiki/concepts/Domain-Driven Design|Domain-Driven Design]] 和 [[wiki/maps/Software Design Map|Software Design Map]] 中领域层的业务规则、不变量与语义边界。

### 什么时候补 API

API 不应该早于系统边界和领域对象。它适合在以下内容基本清楚后补充：

```text
Use Case 主流程稳定。
系统边界清楚。
领域对象和状态基本明确。
外部系统依赖清楚。
异常路径已经识别。
```

API 设计从 Use Case 的动作、异常和状态推导出来：

```text
Use Case 步骤 -> API 入口
前置条件 -> API 校验
主成功场景 -> 成功响应
异常场景 -> 错误码
后置状态 -> 返回状态 / 领域状态变化
```

例如：

```text
Use Case：购买专栏
API：POST /columns/{columnId}/purchase

成功：
- 对应创建待支付订单
- 返回 orderId、paymentUrl、status

错误：
- 401 UNAUTHORIZED：用户未登录
- 409 COLUMN_NOT_PURCHASABLE：专栏不可购买
- 409 COLUMN_ALREADY_PURCHASED：用户已购买
- 409 ORDER_ALREADY_EXISTS：已有待支付订单
```

API 是系统入口，不是业务规则的归宿。核心规则应该进入领域模型或应用层策略，API 只表达协议、输入输出和边界错误。

### 什么时候补 UI

UI 可以在 Use Case 初版后更早开始低保真探索，但完整交互状态应该在 Use Case Review 后补齐。

低保真阶段关注页面流：

```text
专栏详情页
  -> 购买确认弹窗
  -> 支付页
  -> 购买成功页
```

Review 后，Use Case 的每个主流程和异常流程都应该映射到 UI 状态：

```text
主流程：用户点击立即购买
UI：展示购买确认弹窗或进入支付页。

支付成功：
UI：展示购买成功页，按钮变为“开始阅读”。

用户未登录：
UI：跳转登录页或弹出登录框。

已购买：
UI：按钮显示为“开始阅读”，不再展示购买入口。

专栏下架：
UI：隐藏购买按钮，展示“暂不可购买”。

支付失败：
UI：展示失败提示和“重新支付”按钮。
```

UI 的职责是让用户能完成 Use Case，不是把 Use Case 重写成页面说明。Use Case 写“系统拒绝购买并提示原因”；UI 再决定提示位、文案、禁用态、弹窗或跳转。

### 极简用例开发管理模板

一个极简模板可以把业务需求和代码落地放在同一页：

```markdown
# 用例名称

[动宾结构，如：提交商品订单]

# 参与者与目标

[谁，为了达成什么商业价值]

# 验收标准（测试用例映射）

主场景：Given [前置条件], When [触发动作], Then [成功状态]。
扩展场景 1a：When [库存不足], Then [提示失败并记录]。

# 外部依赖“辐条”（UI & 规则）

关联 UI 原型：[Figma 链接]
关联业务规则：[折扣计算规则链接]

# 架构落地（开发任务拆分）

API 接口：POST /orders
App Service (协调者)：OrderAppService.placeOrder()
Domain Model (执行者)：Order 聚合根（验证有效性）与 InventoryClient 端口（检查库存）
```

这个模板的关键不是字段齐全，而是让每个开发工件都能回到同一个用例：业务目标、验收标准、UI、规则、API、应用服务、领域模型和任务拆分不再分散成互相失联的文档。

### 示例：购买专栏

#### 用例名称

```text
购买专栏
```

#### 参与者与目标

```text
参与者：已登录用户

目标：
用户希望购买一个付费专栏，从而获得该专栏内容的阅读权限。

商业价值：
- 用户完成内容购买。
- 平台获得付费转化。
- 作者获得内容销售收入。
- 系统沉淀订单、支付、权限数据。
```

#### 验收标准

```gherkin
主场景：
Given 用户已登录，专栏可购买，用户尚未购买该专栏
When 用户点击“立即购买”并完成支付
Then 系统创建订单，支付成功后授予用户该专栏阅读权限，并展示购买成功页面。

扩展场景 1a：用户未登录
Given 用户未登录
When 用户点击“立即购买”
Then 系统引导用户登录，不创建订单。

扩展场景 1b：用户已购买
Given 用户已登录，且已经购买过该专栏
When 用户再次点击“立即购买”
Then 系统不重复创建订单，提示“你已购买该专栏”，并允许进入阅读。

扩展场景 1c：专栏已下架
Given 用户已登录，专栏已下架
When 用户点击“立即购买”
Then 系统拒绝购买，提示“该专栏暂不可购买”。

扩展场景 1d：支付失败
Given 用户已登录，专栏可购买，订单已创建
When 支付失败
Then 系统保留待支付订单，不授予阅读权限，提示用户重新支付。

扩展场景 1e：重复点击购买
Given 用户已登录，专栏可购买
When 用户连续多次点击“立即购买”
Then 系统只创建一个有效订单，避免重复下单。
```

#### 外部依赖辐条

```text
UI：
- 专栏详情页
- 购买确认弹窗
- 支付页
- 购买成功页
- 已购买状态
- 支付失败状态

业务规则：
- 用户必须登录后才能购买专栏。
- 一个用户对同一个专栏只能拥有一份有效购买记录。
- 只有 Published 且 purchasable=true 的专栏可以购买。
- 订单支付成功后才授予阅读权限。
- 支付失败、支付取消、支付超时均不授予阅读权限。
- 待支付订单在有效期内可以继续支付，不重复创建订单。
- 订单超过支付有效期后关闭，用户再次购买需要创建新订单。
- 专栏价格以创建订单时的价格快照为准。
```

#### 架构落地

```text
API：
POST /columns/{columnId}/purchase
GET /columns/{columnId}/access
POST /payments/callback

App Service：
PurchaseColumnAppService.purchaseColumn()
ConfirmColumnPaymentAppService.confirmPayment()
ColumnAccessQueryService.getAccess()

Domain Model：
Column
Order
ColumnAccess
Payment
Money

外部端口：
PaymentGateway
OrderRepository
ColumnRepository
ColumnAccessRepository
```

Application Service 是协调者：加载用户、专栏、权限和待支付订单，调用领域模型创建订单，调用支付网关创建支付单，保存并返回支付入口。

Domain Model 是执行者：`Column` 判断是否可购买，`Order` 维护订单状态和价格快照，`ColumnAccess` 表达购买后的阅读权限。支付网关、数据库和第三方服务通过端口隔离，不应泄漏进领域规则。

### 支付回调也是独立 Use Case

购买专栏通常不是一个同步接口完成的完整闭环。支付成功往往由支付系统异步回调触发，因此需要第二个 Use Case：

```text
用例名称：确认专栏订单支付成功
参与者：支付系统
目标：支付系统通知平台某笔订单已支付，平台据此授予用户专栏阅读权限。

主场景：
Given 存在待支付订单
When 支付系统回调支付成功
Then 系统标记订单为已支付，并授予用户专栏阅读权限。

扩展场景：
- 回调重复到达：系统保持幂等，不重复授予权限。
- 订单不存在：系统记录异常，不授予权限。
- 订单已关闭：系统拒绝状态变更，并记录异常。
```

这说明一个业务目标可能拆成多个系统 Use Case：用户发起购买、支付系统确认支付、用户查询权限。拆分边界应来自执行者、触发事件和系统承诺，而不是来自代码层文件数。

### 开发任务拆分

开发任务可以按 Use Case 和测试覆盖拆：

```text
BE-001：实现购买专栏 API
关联：购买专栏主场景、未登录、已购买、下架、重复点击
内容：登录校验、专栏查询、权限查询、待支付订单复用、订单创建、支付单创建、返回支付链接。

BE-002：实现 Order 聚合根
关联：业务规则 BR-002、BR-003、BR-006、BR-008
内容：createForColumnPurchase()、markPaid()、closeExpired()、isPendingPayment()、isPaid()。

BE-003：实现支付回调处理
关联：确认专栏订单支付成功
内容：签名校验、订单查询、标记 Paid、授予 ColumnAccess、重复回调幂等。

FE-001：专栏详情页购买入口
关联：进入专栏页、已购买、已下架
内容：未购买展示“立即购买”，已购买展示“开始阅读”，下架展示“暂不可购买”。

FE-002：购买确认与支付跳转
关联：点击购买、创建订单、跳转支付
内容：调用购买 API、处理 loading、防重复点击、处理错误提示。

QA-001：购买专栏主路径测试
覆盖：创建订单、支付成功、授予权限、页面状态变为已购买。

QA-002：购买专栏异常路径测试
覆盖：未登录、已购买、下架、支付失败、重复点击。
```

任务名可以属于不同角色，但每个任务都应该引用同一个 Use Case ID、场景编号和测试编号。

### 追踪矩阵

最简单的管理方式是给 Use Case 步骤编号，然后所有设计都引用这些编号。

```text
UC-BUY-COLUMN/S1：用户进入专栏详情页
UC-BUY-COLUMN/S2：用户点击立即购买
UC-BUY-COLUMN/S3：系统创建待支付订单
UC-BUY-COLUMN/S4：系统返回支付入口
UC-BUY-COLUMN/S5：支付成功后授予阅读权限

UC-BUY-COLUMN/E1：用户未登录
UC-BUY-COLUMN/E2：用户已购买
UC-BUY-COLUMN/E3：专栏已下架
UC-BUY-COLUMN/E4：支付失败
UC-BUY-COLUMN/E5：重复点击
```

追踪矩阵可以这样写：

| Use Case | 场景 | UI | API | App Service | Domain Model | 测试 |
|---|---|---|---|---|---|---|
| UC-BUY-COLUMN | S1 进入专栏页 | 专栏详情页 | GET /columns/{id} | ColumnQueryService | Column | TC-001 |
| UC-BUY-COLUMN | S2 点击购买 | 立即购买按钮 | - | - | - | TC-001 |
| UC-BUY-COLUMN | S3 创建订单 | 支付跳转 | POST /columns/{id}/purchase | PurchaseColumnAppService | Order | TC-001 |
| UC-BUY-COLUMN | S5 支付成功 | 购买成功页 | POST /payments/callback | ConfirmColumnPaymentAppService | Order, ColumnAccess | TC-002 |
| UC-BUY-COLUMN | E1 未登录 | 登录弹窗 | POST /columns/{id}/purchase | Auth Middleware | - | TC-004 |
| UC-BUY-COLUMN | E2 已购买 | 开始阅读按钮 | POST /columns/{id}/purchase | PurchaseColumnAppService | ColumnAccess | TC-005 |
| UC-BUY-COLUMN | E3 已下架 | 不可购买状态 | POST /columns/{id}/purchase | PurchaseColumnAppService | Column | TC-006 |
| UC-BUY-COLUMN | E4 支付失败 | 重新支付 | Payment Callback | ConfirmColumnPaymentAppService | Order | TC-007 |
| UC-BUY-COLUMN | E5 重复点击 | Button Loading | POST /columns/{id}/purchase | PurchaseColumnAppService | Order | TC-008 |

这张表的作用是防止设计断链：

```text
UI 有页面，但 Use Case 没有场景。
API 有字段，但业务规则没有解释。
领域模型有状态，但测试没有覆盖。
异常场景写了，但前端没有错误态。
产品说一个流程，RD 实现另一个流程。
```

### 分层但不断回写

实际开发不应理解为：

```text
Use Case 定稿 -> 领域模型定稿 -> API 定稿 -> UI 定稿
```

更真实的工作方式是：

```text
Use Case 初版
  -> 领域模型发现规则缺口，回写 Use Case
  -> UI 发现交互遗漏，回写 Use Case
  -> API 发现边界不清，回写 Use Case
  -> QA 发现异常场景遗漏，回写 Use Case
```

Use Case 是中心文档，其他设计是它的投影；但其他设计也会反过来修正 Use Case。

### 核心句

Use Case 先定义“用户和系统发生了什么”；领域模型补“业务对象和规则是什么”；UI 补“用户如何完成它”；API 补“系统之间如何协作”；测试补“如何证明它成立”；开发任务补“谁在哪一层实现它”。

## Integration Decisions

这页应保持 source guide 角色，作为 [[wiki/sources/Use Case 开发管理 Source Guide|Use Case 开发管理 Source Guide]] 的 companion capture。已有页面已经保存 Use Case 与 UI、API、应用服务、领域模型、数据库、测试的边界关系；本页新增的是团队协作流程、开发时机、购买专栏样例和追踪矩阵。

本页中的“Use Case 是中心文档，其他设计是投影并反向修正 Use Case”“追踪矩阵防止设计断链”等判断，可以后续提升到 [[wiki/topics/Requirement to Architecture Mapping|Requirement to Architecture Mapping]] 或新的稳定概念页。当前先保留为来源层，避免把一次教学示例直接升格为唯一方法论。

## Open Questions

- 项目管理工具中是否应该把 Use Case ID、场景编号、测试编号、API、任务 ID 建成结构化字段，而不是只写在 Markdown 表格里？
- 对更复杂的 B2B 流程，Use Case Review 是否需要先经过业务流程图、事件风暴或业务序列图，再进入系统 Use Case？

## Related

- [[wiki/sources/Use Case 开发管理 Source Guide]]
- [[wiki/maps/Software Analysis Map]]
- [[wiki/maps/Software Design Map]]
- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/concepts/Domain-Driven Design]]
- [[wiki/topics/Testing Strategy]]
