---
title: >-
  Use Case 开发管理 Source Guide
category: sources
tags: [requirements, software-engineering, architecture, testing]
sources:
  - conversation:2026-05-14
created: 2026-05-14T00:29:01+08:00
updated: 2026-05-14T00:29:01+08:00
summary: >-
  这页保存一份关于 Use Case 如何定义行为契约，并关联 UI、API、应用服务、领域模型、数据库、测试和开发任务的中文讲解。
provenance:
  extracted: 0.78
  inferred: 0.22
  ambiguous: 0.00
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-14
aliases:
  - 用例开发管理
  - Use Case 开发管理
  - 用例到开发任务
---

# Use Case 开发管理 Source Guide

> Source: conversation:2026-05-14

## Capture Policy

这页保存一次关于 Use Case 的会话式教学内容，重点不是复述对话，而是保留其中形成的可复用解释：Use Case 如何限定系统行为契约，以及如何把 UI、API、应用服务、领域模型、数据库、测试和任务拆分挂到同一条业务行为主线上。

## What It Covers

Use Case 位于业务目标和软件实现之间。它解决的问题是：当外部参与者想达成一个目标时，系统应该承诺什么行为，包括主成功路径和失败路径。

这层知识属于 [[wiki/maps/Software Analysis Map|软件分析]] 和 [[wiki/topics/Requirement to Architecture Mapping|需求到架构映射]] 之间的接口：分析阶段用 Use Case 明确系统边界内的行为；设计和实现阶段再把这个行为分解到 UI、API、应用层、领域层、持久化和测试。

## Preserved Content

### Use Case 解决的是系统行为契约

Use Case 不是页面说明、接口文档、数据库设计或代码任务清单。它的核心问题是：

```text
谁在系统边界外？
他想完成什么目标？
系统为了响应这个目标，应该发生什么行为？
成功时系统进入什么状态？
失败或异常时系统如何响应？
```

一个最小但有用的 Use Case 通常包含：

```text
用例名称：提交订单
参与者：买家
目标：买家确认购物车后生成订单
前置条件：买家已登录，购物车中有商品

主成功场景：
1. 买家提交订单
2. 系统校验购物车商品和库存
3. 系统计算价格
4. 系统创建订单
5. 系统返回订单创建成功

扩展场景：
2a. 库存不足：系统拒绝创建订单，并告知库存不足
3a. 价格发生变化：系统要求用户重新确认
```

Use Case 应该使用系统行为语言，而不是实现语言。它写“买家提交订单”“系统创建订单”“系统拒绝创建订单”，不写“点击红色按钮”“调用 POST /api/v1/orders”“插入 orders 表”。

### Use Case 和领域模型的边界

Use Case 由外向内看系统：外部参与者触发一个目标，系统如何响应。领域模型由内向外看业务：哪些实体、值对象、状态、规则和不变量支撑这个响应。

Use Case 告诉领域模型哪些业务行为需要被支持，但不应该把所有领域规则细节都塞进 Use Case。领域规则应该在 [[wiki/concepts/Domain-Driven Design|DDD]]、领域模型和业务规则表中沉淀。

例如“提交订单”涉及的领域对象可能包括：

```text
Order
OrderItem
Cart
Inventory
Money
Coupon
```

领域规则包括：

```text
订单金额必须等于商品金额减优惠
库存不足不能创建订单
已失效优惠券不能使用
订单创建后进入 PendingPayment 状态
```

这些规则和对象可以被 Use Case 引用，但不应让 Use Case 变成领域模型全文。

### Use Case 和 User Story 的边界

[[wiki/topics/User Stories|User Story]] 是轻量沟通占位符，常用格式是：

```text
作为 X
我想要 Y
以便 Z
```

它适合表达角色、目标和价值，便于排期和沟通。Use Case 更像行为契约，适合继续展开主成功场景、扩展场景、前置条件、后置结果和验收标准。

二者可以顺接：

```text
User Story：
作为买家，我想提交购物车中的商品，以便完成购买。

Use Case：
提交订单，包括库存校验、价格确认、订单创建、库存不足和价格变化等路径。
```

User Story 说明“为什么值得做”；Use Case 说明“系统要如何承诺行为”。

### Use Case 和业务流程的边界

业务流程是组织级、跨角色、跨系统、跨时间的端到端协作过程。Use Case 通常是业务流程中由某个参与者触发、由目标系统完成的一段离散交互。

例如：

```text
业务流程：患者就诊
  - 预约
  - 挂号
  - 问诊
  - 检查
  - 缴费
  - 取药

系统 Use Case：患者在线挂号
```

业务流程回答“组织如何协作完成一件事”；系统 Use Case 回答“待开发系统在某个边界内向外部参与者提供什么行为”。

### Use Case 和 UI 的关系

UI 负责回答：用户在哪里、以什么交互方式触发这个 Use Case。

Use Case 本体写：

```text
买家提交订单。
系统提示库存不足。
系统要求用户重新确认变化后的价格。
```

UI 工件写：

```text
订单确认页
提交订单按钮
库存不足提示弹窗
价格变化确认弹窗
```

边界原则是：Use Case 写意图和系统响应；UI 写界面结构、交互状态和展示细节。

### Use Case 和 API 的关系

API 负责回答：系统边界上暴露哪个入口来执行这个 Use Case。

例如：

```text
Use Case：提交订单
API：POST /orders

Request:
{
  "cartId": "...",
  "couponId": "..."
}

Response:
{
  "orderId": "...",
  "status": "created"
}
```

一个 Use Case 通常会有一个主要 API 入口，但不必机械地一对一。复杂用例可能涉及多个查询和命令；一个 API 也可能只是某个 Use Case 的入口步骤。

### Use Case 和 Application Service / Command Handler 的关系

Application Service 或 Command Handler 是 Use Case 在代码中的主要落点。Use Case 属于问题空间，说明系统要做什么；Application Service / Command Handler 属于解空间，编排这个行为如何落地。

例如：

```text
Use Case：提交订单
Command：PlaceOrderCommand
Handler：PlaceOrderHandler
Application Service：OrderApplicationService.placeOrder()
```

应用层通常负责：

```text
1. 接收命令
2. 加载领域对象
3. 调用领域模型
4. 调用外部端口
5. 保存结果
6. 返回结果
```

应用层不应该承载核心业务规则。它负责协调，领域模型负责判断和执行业务规则。这个分工也连接到 [[wiki/maps/Software Design Map|软件设计地图]] 中表现层、应用层、领域层、基础设施层的边界。

### Use Case 和数据库的关系

数据库是 Use Case 的实现结果，不是 Use Case 的表达方式。Use Case 可以说明系统状态如何变化，但不应该关心表结构、SQL 或 ORM 细节。

合适的表达：

```text
系统创建订单。
系统记录库存占用。
系统保存订单事件。
```

不合适的表达：

```text
insert into orders
update sku_stock
select cart_items
```

持久化设计可以从 Use Case 推导出来：

```text
Use Case：提交订单
持久化影响：
- 创建 Order
- 创建 OrderItem
- 记录库存占用
- 记录订单事件
```

但这些属于 Repository、ORM、迁移脚本和数据库设计任务，不属于 Use Case 本体。

### Use Case 和测试的关系

Use Case 是验收测试的直接来源。主成功场景对应正向测试，扩展场景对应失败和异常测试，前置条件、触发动作和后置状态可以直接转成 Given / When / Then。

主成功路径：

```gherkin
Given 买家已登录，购物车中有 2 件有库存商品
When 买家提交订单
Then 系统创建一个 PendingPayment 订单
And 返回订单号
```

失败路径：

```gherkin
Given 买家购物车中有库存不足的商品
When 买家提交订单
Then 系统拒绝创建订单
And 提示库存不足
```

这让 Use Case 成为需求、设计和测试之间的共同对象。它也连接到 [[wiki/topics/Testing Strategy|测试策略]]：测试不是从代码覆盖率开始，而是从系统承诺的行为是否被验证开始。

### Use Case 如何拆成开发任务

Use Case 可以作为任务拆分的行为主线。每个开发工件都围绕同一个行为展开：

```text
Use Case：提交订单

产品 / 需求：
- 明确主成功场景和失败场景
- 明确验收标准

前端：
- 订单确认页
- 提交订单交互
- 库存不足提示
- 价格变化提示

后端 API：
- POST /orders
- 请求 / 响应 DTO
- 错误码设计

应用层：
- PlaceOrderCommand
- PlaceOrderHandler
- 事务边界

领域层：
- Order 聚合
- 价格计算规则
- 库存校验规则
- 优惠券规则

持久化：
- orders 表
- order_items 表
- 库存占用记录
- repository 实现

测试：
- 主流程验收测试
- 库存不足测试
- 优惠券失效测试
- 价格变化测试
```

这种拆分方式避免前端只做页面、后端只做接口、数据库只做表结构。所有任务都要回到同一个行为契约：系统是否正确支持这个 Use Case。

### 极简管理模板

```text
# Use Case：<动宾结构，例如：提交订单>

## 1. 行为契约
参与者：
目标：
前置条件：
主成功场景：
扩展 / 失败场景：
后置结果：

## 2. 验收标准
- Given ...
- When ...
- Then ...

## 3. 关联 UI
- 页面：
- 组件：
- 状态：
- 错误提示：

## 4. 关联 API
- Endpoint：
- Request：
- Response：
- Error Codes：

## 5. 应用层落点
- Command：
- Handler / Application Service：
- Transaction Boundary：

## 6. 领域模型
- Aggregates：
- Entities：
- Value Objects：
- Domain Services：
- Business Rules：

## 7. 持久化
- Tables / Collections：
- Repository：
- Events / Outbox：

## 8. 开发任务
- Frontend：
- Backend API：
- Domain：
- Persistence：
- Tests：
```

### 核心边界句

Use Case 管“用户目标与系统行为”；开发工件管“如何让这个行为可见、可调用、可执行、可持久化、可验证”。

因此，Use Case 不替代 UI 文档、接口文档、数据库设计或任务拆分。它把这些工件挂到同一条业务行为主线上，防止需求、界面、接口、领域规则、数据库和测试彼此失联。

## Integration Decisions

这页应保持 source guide 角色，而不是直接替代 [[wiki/topics/Requirement to Architecture Mapping|Requirement to Architecture Mapping]]。它提供的是一次围绕 Use Case 的教学型解释，适合未来被进一步提炼为稳定概念页“Use Case”或补入软件分析主题。

页面中的“Use Case 是行为契约”“UI/API/数据库是关联工件而不是 Use Case 本体”“主成功场景和扩展场景映射测试”可以后续提升到概念页或综合页。当前先保留为来源层，便于和 NotebookLM 中的 DDD、OOAD、软件方法资料继续对照。

## Open Questions

- 是否需要单独创建稳定概念页 `Use Case`，把业务用例、系统用例和 Clean Architecture 中的 Use Case 分开定义？
- 在具体项目管理工具中，Use Case、Story、Task、Test Case 的一对多关系应该如何建模，才能既可追溯又不过度管理？

## Related

- [[wiki/maps/Software Analysis Map]]
- [[wiki/maps/Software Design Map]]
- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/topics/User Stories]]
- [[wiki/concepts/Domain-Driven Design]]
- [[wiki/topics/Testing Strategy]]
