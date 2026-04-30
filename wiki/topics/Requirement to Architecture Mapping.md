---
title: Requirement to Architecture Mapping
type: topic
status: growing
source_count: 3
updated: 2026-05-01
aliases:
  - req_map_to_arch
  - 用户故事到架构映射
tags:
  - architecture
  - requirements
  - mapping
---

# Requirement to Architecture Mapping

这个主题页沉淀的是：如何把用户故事、PRD、free-form requirement 先归一化，再稳定映射到分层架构。

## Normalized input

在做架构映射前，先把输入统一为：

- feature
- use_case
- entry
- input / output
- business_rules
- domain_objects
- data_access
- external_calls
- errors
- shared_utils
- assumptions

如果输入不完整，保守推断，并明确标出 assumptions。

## Engineering mental model

工程师实现需求时，不应从“要写哪些代码”开始，而应先问：系统要在什么场景下，对谁，稳定地产生什么结果。

需求实现是一条逐步收窄的链路：

```text
原始需求
  -> 澄清后的业务场景
  -> 领域对象和业务规则
  -> 用例定义
  -> 模块职责划分
  -> 数据流和状态机
  -> 异常处理方案
  -> 代码结构和接口定义
  -> 具体实现
```

每一步都要产生可检查的中间结果，而不是只在脑子里想一遍。

## Intermediate artifacts

以“用户导出订单报表”为例：

### 1. Clarified requirement

原始需求：

```text
用户可以导出订单报表。
```

澄清后：

```text
运营人员希望按时间范围和订单状态导出订单报表，
用于每周财务核对。
导出文件为 CSV。
普通运营只能导出自己负责店铺的订单。
单次最多导出 100000 条。
超过 10000 条时异步生成。
```

中间结果：

- 需求说明
- 场景描述
- 约束清单

### 2. Domain objects and rules

领域对象：

```text
User
Order
Shop
ExportTask
OrderReport
Permission
```

业务规则：

```text
用户必须有 order.export 权限
普通运营只能导出自己负责的店铺
管理员可以导出所有店铺
时间范围最多 90 天
导出数量 <= 10000 时同步返回
导出数量 > 10000 时创建异步任务
导出文件保留 7 天
```

中间结果：

- 领域词表
- 业务规则表
- 权限规则表

### 3. Use case

```text
用例：导出订单报表

触发者：
运营人员

输入：
- userId
- shopId
- startDate
- endDate
- orderStatus
- exportFormat

前置条件：
- 用户已登录
- 用户拥有导出权限

主流程：
1. 用户提交导出请求
2. 系统校验参数
3. 系统校验权限
4. 系统查询符合条件的订单数量
5. 如果数量较少，直接生成 CSV
6. 如果数量较多，创建导出任务
7. 系统返回文件或任务 ID

输出：
- CSV 文件
- ExportTaskId

失败情况：
- 无权限
- 时间范围过大
- 没有符合条件的订单
- 导出任务创建失败
```

中间结果：

- 用例文档
- 主流程
- 异常流程
- 输入输出定义

### 4. Responsibility boundaries

```text
核心逻辑：
- 判断用户能否导出某个店铺的订单
- 判断导出方式是同步还是异步
- 生成报表字段
- 管理导出任务状态

外围设施：
- HTTP API
- 数据库查询
- CSV 文件生成库
- 对象存储
- 消息队列
- 前端下载按钮
```

中间结果：

- 职责边界图
- 模块划分
- 逻辑放置规则

一个可能的模块切分：

```text
OrderExportController
  接收 HTTP 请求

ExportOrderReportUseCase
  编排导出流程

OrderExportPolicy
  判断权限和业务规则

OrderRepository
  查询订单

ExportTaskRepository
  保存导出任务

CsvReportGenerator
  生成 CSV

FileStorage
  上传文件
```

### 5. Data flow and state flow

同步路径：

```text
POST /order-reports/export
  -> OrderExportController
  -> ExportOrderReportUseCase
  -> OrderExportPolicy
  -> OrderRepository.count()
  -> CsvReportGenerator.generate()
  -> FileStorage.upload()
  -> return downloadUrl
```

异步路径：

```text
POST /order-reports/export
  -> OrderExportController
  -> ExportOrderReportUseCase
  -> ExportTaskRepository.create()
  -> GenerateOrderReportJob.enqueue()
  -> return taskId
```

任务状态：

```text
PENDING
RUNNING
SUCCESS
FAILED
EXPIRED
```

中间结果：

- 数据流图
- 状态机
- 接口调用链

### 6. Failure paths

```text
用户无权限
  -> 返回 403

时间范围超过 90 天
  -> 返回 400，提示缩小时间范围

订单数量为 0
  -> 返回空 CSV 或提示无数据，取决于产品约定

CSV 生成失败
  -> 任务状态变为 FAILED，记录失败原因

文件上传失败
  -> 重试 3 次，仍失败则标记 FAILED

用户重复点击导出
  -> 如果参数相同且已有运行中任务，返回已有 taskId
```

中间结果：

- 异常处理表
- 错误码
- 重试策略
- 幂等策略

### 7. Code shape

```text
src/
  orders/
    application/
      ExportOrderReportUseCase.ts
    domain/
      OrderExportPolicy.ts
      ExportTask.ts
      ExportTaskStatus.ts
    infrastructure/
      OrderRepository.ts
      ExportTaskRepository.ts
      CsvOrderReportGenerator.ts
      S3FileStorage.ts
    interface/
      OrderExportController.ts
```

接口草稿：

```ts
type ExportOrderReportInput = {
  userId: string;
  shopId?: string;
  startDate: Date;
  endDate: Date;
  orderStatus?: OrderStatus;
  format: "csv";
};

type ExportOrderReportOutput =
  | { type: "sync"; downloadUrl: string }
  | { type: "async"; taskId: string };
```

中间结果：

- 目录结构
- 类型定义
- 接口定义
- 类和函数职责

## Layer mapping heuristics

- 协议入口、handler、DTO、协议错误码 → `api/`
- 业务判断、校验、状态流转、领域对象、业务错误 → `service/`
- service 需要的外部能力接口定义 → `service/` 中的 repo / capability interface
- MySQL / Redis / RPC / HTTP / MQ / SDK 的技术实现 → `infra/`
- 无业务语义的纯技术 helper → `pkg/`

## Fast judgment questions

拿到一句需求后，依次问：

1. 它是在描述怎么接请求吗？→ `api/`
2. 它是在描述业务如何判断或流转吗？→ `service/`
3. 它是在描述系统需要什么外部能力吗？→ `service/` 定义接口
4. 它是在描述能力如何落地实现吗？→ `infra/`
5. 它只是纯技术工具吗？→ `pkg/`

## Common mistakes

- 把库存校验规则放到 `infra/`
- 把 RPC client 放到 `pkg/`
- 在 `infra/` 定义 repo interface
- 让 handler 直接依赖 MySQL repo

## Navigation

- [[wiki/topics/面向对象分析与设计]]
- [[wiki/maps/AI Map]]
- [[wiki/topics/Karpathy Guidelines]]
- `content/posts/cs/arch/arch.md`

## Source notes

- `pages/项目___AI___req_map_to_arch.md`
- `journals/2026_04_01.md`
- `pages/项目___AI.md`
