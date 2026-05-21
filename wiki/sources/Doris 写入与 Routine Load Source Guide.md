---
title: >-
  Doris 写入与 Routine Load Source Guide
category: sources
tags: [database, systems, software-engineering, architecture]
sources:
  - conversation:2026-05-21
created: 2026-05-21T15:20:08+08:00
updated: 2026-05-21T15:20:08+08:00
summary: >-
  这页保留一段关于 Doris 2.1 写入方式、Routine Load 原理、Task 执行时序和内部 Rowset/事务/版本发布链路的中文教学说明。
provenance:
  extracted: 0.92
  inferred: 0.06
  ambiguous: 0.02
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-05-21
type: source
status: draft
aliases:
  - Doris 写入
  - Doris Routine Load
  - Doris 内部写入时序
---

# Doris 写入与 Routine Load Source Guide

> Source: conversation:2026-05-21

## Capture Policy

这页按 source guide 保存当前会话中的教学内容，保留原始问题链、解释层次、关键时序图和对比表。它不是对 Doris 官方文档的完整替代，而是保存一段围绕 Doris 2.1/2.1.11 写入机制展开的中文学习材料。

## What It Covers

这段材料覆盖 Doris 的主要写入方式、Routine Load 的整体原理、Routine Load Task 的时序逻辑，以及 Doris 内部从写入请求到 Rowset、事务提交、版本发布和查询可见的链路。

它属于 [[wiki/maps/CS Map]] 的数据库与系统实现知识，也连接到 [[wiki/topics/BoltDB Internals]] 对存储、事务和页/版本机制的学习线索，以及 [[wiki/topics/High Concurrency]] 对高吞吐批处理、并发消费和后台 compaction 压力的系统问题。

## 原始问题链

1. Doris 写入有哪种方式，说明适用场景、原理，版本：2.11。
2. 详细解释 Routine Load 的原理。
3. 展开 Task 的时序逻辑。
4. Doris 执行 Task 的时序。
5. Doris 内部写入时序。

这条问题链从“有哪些导入方式”逐步下钻到“Routine Load 如何把 Kafka 消费变成 Doris 事务写入”，最后落到 Doris 内部写入路径：分区分桶路由、Tablet 写入、Rowset 生成、事务提交与版本发布。

## Preserved Content

### Doris 主要写入方式

如果“Doris 2.11”指的是 Doris 2.1.11 / 2.1.x，主要写入/导入方式可以分为六类：Stream Load、Broker Load、Routine Load、MySQL Load、INSERT INTO SELECT、INSERT INTO VALUES。

| 写入方式               | 适用场景                                                      | 基本原理                                                       | 特点                                                      |
| ------------------ | --------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------- |
| Stream Load        | 本地文件、程序实时/准实时写入、小中批量数据，常见于业务服务、脚本、DataX、Flink Connector 等 | 通过 HTTP 向 FE/BE 提交数据，FE 可重定向到 BE，BE 作为 Coordinator 接收并分发写入 | 同步返回结果；适合小中批量；支持 CSV/JSON/Parquet/ORC；通过 `label` 防重复    |
| Broker Load        | HDFS、S3、OSS 等远端文件的大批量离线导入                                 | FE 生成导入任务，BE 并行读取远端文件、解析、分发、写入                             | 异步任务；适合大规模批量；支持 CSV/JSON/Parquet/ORC；可 `SHOW LOAD` 查看状态 |
| Routine Load       | Kafka 持续消费，实时/准实时数仓写入                                     | FE 创建常驻任务，拆成多个 BE 子任务持续消费 Kafka 分区，每批作为事务提交                | Kafka 专用；支持 CSV/JSON；支持 offset 管理；适合流式摄入                |
| MySQL Load         | 从客户端本地文件快速导入，兼容 MySQL `LOAD DATA LOCAL INFILE`            | MySQL 协议提交，本质上 FE 转成 Stream Load，由 BE 接收文件并写入              | 同步；主要适合 CSV；一般小中批量；需要客户端开启 `local-infile`               |
| INSERT INTO SELECT | Doris 内部表间 ETL，或从 Catalog/TVF 查询外部数据后写入 Doris             | FE 规划 SQL 查询，BE 执行查询，最终通过 `OlapTableSink` 写入目标表            | 同步；适合 SQL 化 ETL；可做过滤、聚合、Join、类型转换                       |
| INSERT INTO VALUES | 少量测试数据、临时手工写入、小批量值写入                                      | MySQL 协议提交 literal values，FE 规划后由 BE 写入                    | 不适合生产高吞吐写入；高并发小写入建议结合 Group Commit                      |

生产选择规则：

| 场景 | 推荐方式 |
|---|---|
| 本地文件、小中批量、程序写入 | Stream Load |
| HDFS/S3/OSS 上的大批量离线文件 | Broker Load |
| Kafka 实时/准实时摄入 | Routine Load |
| MySQL 客户端本地 CSV 快速导入 | MySQL Load |
| Doris 内部 ETL / SQL 加工写入 | INSERT INTO SELECT |
| 少量测试数据 | INSERT INTO VALUES |
| Flink/Spark/DataX 等外部工具写 Doris | 通常底层使用 Stream Load 或 Doris Connector |
| 高频小批量写入 | 优先批量化，或考虑 Group Commit + Stream Load/INSERT |

生产建议：实时 Kafka 数据优先 Routine Load；如果已有 Flink 作业，则用 Flink Doris Connector。业务服务写入优先 Stream Load，不建议单条 `INSERT VALUES`。离线湖仓文件导入优先 Broker Load。表内加工优先 `INSERT INTO SELECT`。小文件或测试可以用 Stream Load、MySQL Load 或 INSERT VALUES，但生产要避免大量小事务。所有导入都建议设置 label，尤其是 Stream Load、Broker Load、INSERT，方便幂等与排查。

### Routine Load 的整体原理

Routine Load 可以理解成 Doris 内置的、长期运行的 Kafka 消费导入任务。它不是一次性导入，而是 Doris 自己持续从 Kafka 拉数据，按小批次写入 Doris 表。

核心链路：

```text
Kafka Topic
   ↓
Routine Load Job，FE 管理的常驻导入作业
   ↓
多个 Routine Load Task，FE 拆分并调度
   ↓
BE 消费 Kafka 分区数据
   ↓
解析 CSV / JSON
   ↓
写入 Doris Tablet
   ↓
事务提交，可见
   ↓
更新 Kafka Offset
```

Routine Load 的定位是：Doris 内置 Kafka Consumer + Doris 分布式导入事务 + 持续调度机制。它适合日志实时入仓、埋点数据入仓、订单/支付/交易事件流、CDC 结果写入 Doris，以及 Kafka 作为数据总线、Doris 作为实时 OLAP 查询层的场景。

### FE 与 BE 的职责

Routine Load 主要涉及 FE、BE、Kafka 三个角色。

FE 不直接消费 Kafka 数据，主要负责：保存 Routine Load Job 元数据；解析 `CREATE ROUTINE LOAD`；根据 Kafka Topic、分区、BE 节点数量拆分任务；调度 Routine Load Task 到 BE；管理任务状态；管理导入事务；记录和推进 Kafka offset；判断任务成功、失败、暂停、恢复。

BE 负责真正的数据处理：从 Kafka 拉取消息；按 CSV 或 JSON 解析数据；做列映射、表达式转换、过滤；根据 Doris 表的分区、分桶规则分发数据；写入对应 Tablet；向 FE 汇报任务执行结果；配合完成事务提交。

简化为：FE 管任务，BE 干活。

### Job 与 Task 的关系

Routine Load 是两层结构：Job 是长期存在的导入作业，Task 是 FE 动态生成的短生命周期执行单元。

```text
Routine Load Job
   ├── Task 1
   ├── Task 2
   ├── Task 3
   └── ...
```

每个 Task 只负责消费 Kafka 的一段 offset：

```text
Task 1:
  partition 0: offset 1000 → 1500
  partition 1: offset 2000 → 2600

Task 2:
  partition 0: offset 1500 → 2100
  partition 1: offset 2600 → 3200
```

Routine Load 的运行模型是：长期 Job = 不断生成、执行、提交短 Task。

### Kafka 分区与消费并发

Kafka Topic 通常有多个 partition。Routine Load 会把这些 partition 分配给不同 Task 和 BE。Kafka partition 数量会限制 Routine Load 的最大有效消费并发。如果 Kafka 只有一个 partition，即使 Doris 有很多 BE，也很难通过 Routine Load 获得很高并发消费能力。

```text
topic_order
   ├── partition 0
   ├── partition 1
   ├── partition 2
   └── partition 3
```

示例分配：

```text
BE 1:
  Task A: partition 0, 1

BE 2:
  Task B: partition 2, 3
```

影响并发度的因素包括 Kafka Topic partition 数量、Doris BE 数量、Routine Load 并发配置、FE/BE 当前负载和 `desired_concurrent_number` 等参数。

### Offset 管理

Routine Load 维护每个 Kafka partition 的消费进度。起始 offset 可以来自 `OFFSET_BEGINNING`、`OFFSET_END`、具体 offset 或 timestamp。

offset 推进的关键顺序是：

```text
BE 消费 Kafka 数据
   ↓
数据成功写入 Doris
   ↓
事务提交成功
   ↓
FE 更新该 partition 的 offset
```

如果只消费了 Kafka，但 Doris 写入失败，offset 不应推进，否则会丢数据。Routine Load 的 offset 推进和 Doris 事务提交绑定。

### Task 的完整时序逻辑

Routine Load Task 的整体循环是：

```text
FE 调度 Task
  → BE 执行 Task
  → BE 消费 Kafka
  → BE 写 Doris
  → FE 提交事务
  → FE 更新 offset
  → FE 再生成下一批 Task
```

更细的完整时序：

```text
T0: 用户创建 Routine Load Job
T1: FE 保存 Job 元数据
T2: FE 周期性调度 Job
T3: FE 查询 Kafka partition 信息
T4: FE 根据 offset、并发度、BE 状态生成 Task
T5: FE 将 Task 分发给 BE
T6: BE 消费 Kafka 数据
T7: BE 解析、过滤、转换数据
T8: BE 写入 Doris Tablet
T9: BE 向 FE 汇报 Task 执行结果
T10: FE 提交事务
T11: FE 更新 Kafka offset
T12: FE 生成下一轮 Task
```

Task 创建时会携带 job_id、task_id、目标 db/table、Kafka broker list、Kafka topic、需要消费的 partition、每个 partition 的起始 offset、数据格式、列映射规则、过滤条件、批次边界、事务信息、label/txnId 等。

Task 不会无限消费，它会在满足某些条件后结束当前批次：`max_batch_interval`、`max_batch_rows`、`max_batch_size`、Task 超时、Job 被暂停/停止、BE 异常或 Kafka 暂时无数据。

典型配置：

```sql
PROPERTIES
(
    "max_batch_interval" = "10",
    "max_batch_rows" = "300000",
    "max_batch_size" = "209715200"
)
```

含义是：本批最多消费 10 秒，或最多消费 300000 行，或最多消费 200MB，哪个先达到就结束本 Task。

### 成功 Task 时序

一次成功 Task 的时序：

```text
T1: FE 创建 Task
T2: FE 为 Task 绑定导入事务
T3: FE 下发 Task 到 BE
T4: BE 从 Kafka 指定 offset 开始消费
T5: BE 消费到一批数据
T6: BE 解析并写入 Doris
T7: BE 达到 batch 条件，停止本批消费
T8: BE 向 FE 汇报成功写入行数、过滤行数、消费到的最新 offset、错误信息
T9: FE 判断错误率是否可接受
T10: FE 提交 Doris 导入事务
T11: 事务提交成功，数据可见
T12: FE 更新 Job 的 Kafka offset
T13: FE 继续调度下一批 Task
```

例如当前进度：

```text
partition 0 offset = 1000
partition 1 offset = 5000
```

Task A 消费后：

```text
p0: 1000 → 1800
p1: 5000 → 6200
```

FE 提交事务成功后，Job 进度更新为：

```text
partition 0 offset = 1800
partition 1 offset = 6200
```

下一批 Task 从这里继续。

### 失败 Task 时序

如果 BE 消费了 Kafka，但 Doris 写入失败：

```text
T1: FE 创建 Task
T2: BE 从 offset 1000 开始消费
T3: BE 消费到 offset 1800
T4: 写 Doris 失败
T5: BE 向 FE 汇报失败
T6: FE 回滚事务
T7: FE 不更新 offset
T8: 下一次 Task 仍然从 offset 1000 开始
```

结果是 Kafka 数据会被重新消费，Doris 不会提交失败批次，offset 不会前进。

如果 BE 执行 Task 时宕机：

```text
T1: Task A 分配给 BE 1
T2: BE 1 从 Kafka offset 1000 开始消费
T3: BE 1 消费到 offset 1500
T4: BE 1 宕机
T5: FE 检测 Task 超时或失败
T6: FE 标记 Task A 失败
T7: FE 回滚或放弃该事务
T8: offset 仍然保持 1000
T9: FE 重新生成 Task B
T10: Task B 分配给 BE 2
T11: BE 2 从 offset 1000 重新消费
```

### Exactly-Once 的含义

Routine Load 的 Exactly-Once 不能简单理解为 Kafka 消息物理上只被读一次。更准确地说，Doris 通过事务提交和 offset 提交绑定，尽量保证 Kafka 消息不会因为失败重试而在 Doris 中重复可见，也不会在写入失败时丢失。

核心目标是：Kafka 可以被重复消费，但不能让重复数据重复提交可见。

```text
重读可以发生
  ↓
事务未提交则不推进 offset
  ↓
事务提交后才推进 offset
  ↓
Doris 可见数据与 offset 进度保持一致
```

### Doris 执行 Routine Load Task 的内部时序

FE 调度 Task 后，BE 执行 Task 的内部步骤是：

```text
BE 收到 Task
  ↓
初始化 Kafka Consumer
  ↓
根据 Task 指定 offset 执行 seek
  ↓
开始 poll Kafka
  ↓
累计数据
  ↓
解析数据
  ↓
写入 Doris
  ↓
达到批次结束条件
  ↓
停止消费本批
  ↓
汇报结果给 FE
```

更细一点：BE 初始化导入上下文、建立 Kafka Consumer、seek 到指定 offset、poll Kafka 消息、解析 CSV/JSON、做列映射、表达式计算、数据质量检查、将数据写入 Doris 内部写入管道、记录本次消费到的 offset、向 FE 返回执行结果。

BE 收到 Task 后会创建执行上下文，包括 RuntimeState、导入 Profile、内存跟踪器、目标表 schema、表达式和列映射、Kafka 读取端与 Doris 写入端。

Kafka Consumer 初始化时，BE 会根据 Task 中的 partition 与 offset 执行 assign 和 seek。这意味着 Routine Load 的消费进度由 Doris FE 控制，而不是由 Kafka consumer group 自动提交控制。

### 数据解析与列映射

Routine Load 支持 CSV 和 JSON。

JSON 示例：

```json
{"order_id":1001,"user_id":88,"amount":59.9,"ts":1716268800}
```

Routine Load 可以通过 `jsonpaths` 提取字段：

```sql
PROPERTIES
(
  "format" = "json",
  "jsonpaths" = "["$.order_id", "$.user_id", "$.amount", "$.ts"]"
)
```

并通过 `COLUMNS` 执行列映射和表达式计算：

```sql
COLUMNS(
  order_id,
  user_id,
  amount,
  dt = date(from_unixtime(ts))
)
```

CSV 示例：

```text
1001,88,59.9,1716268800
```

BE 会按分隔符切列、检查字段数量、做类型转换，然后生成 Doris 内部行。

常见脏数据包括字段类型不匹配、字符串超长、日期非法、JSON 格式错误、CSV 列数不匹配、目标分区不存在、NOT NULL 列为空。BE 会记录 filtered rows，FE 根据 `max_filter_ratio` 判断是否允许提交。

### Doris 内部写入总时序

Stream Load、Routine Load、Broker Load、INSERT INTO 最终都会进入一套相似的 Doris 内部写入链路：

```text
外部导入 / SQL
  ↓
FE 创建导入事务
  ↓
FE 生成执行计划
  ↓
BE 执行写入
  ↓
数据路由到 Tablet
  ↓
TabletWriter / DeltaWriter 写入
  ↓
生成 Rowset
  ↓
FE commit 事务
  ↓
FE publish version
  ↓
数据对查询可见
```

Doris 写入可以分成两层：控制面由 FE 负责事务、元数据、调度、版本发布；数据面由 BE 负责接收数据、分发数据、写 Tablet、生成 Rowset。

更完整的内部写入顺序：

```text
1. 请求进入 Doris
2. FE 校验权限、表结构、分区、导入参数
3. FE 创建事务 txn
4. FE 生成执行计划
5. BE 执行计划
6. 数据进入写入算子 OlapTableSink
7. 根据分区列找到 Partition
8. 根据分桶列计算 Bucket
9. 找到目标 Tablet
10. 数据发送到 Tablet 所在 BE
11. 每个目标 BE 打开 TabletWriter / DeltaWriter
12. 数据写入内存缓冲
13. 缓冲达到阈值后 flush 成 Segment
14. Segment 组成临时 Rowset
15. BE 返回 commit info
16. FE commit txn
17. FE publish version
18. BE 把 Rowset 绑定到 Tablet 新版本
19. 数据可见
```

### 关键内部对象

| 对象 | 作用 |
|---|---|
| FE | 元数据、事务、调度、版本发布 |
| BE | 实际执行查询和写入 |
| Coordinator BE | 一次导入任务的协调 BE |
| OlapTableSink | 查询/导入计划里的最终写入算子 |
| Partition | 表分区 |
| Bucket | 分桶 |
| Tablet | Doris 的基本数据分片 |
| Replica | Tablet 的副本 |
| Rowset | 一次写入形成的数据集合 |
| Segment | Rowset 内部的列式文件 |
| Version | Tablet 的可见版本 |
| Transaction | 写入事务，控制原子提交 |

Doris 表结构可以理解成：

```text
Table
  ├── Partition
  │     ├── Bucket
  │     │     ├── Tablet
  │     │     │     ├── Replica on BE-1
  │     │     │     ├── Replica on BE-2
  │     │     │     └── Replica on BE-3
```

写入的本质是把一批数据按照分区、分桶规则切分后，写入对应 Tablet 的多个副本，并生成新的 Tablet Version。

### 事务状态与可见性

Doris 写入不是直接让数据立即可见，而是先创建事务。事务会记录 txn_id、label、db_id、table_id、partition_ids、timeout、load job id、callback 和状态。

事务状态大致是：

```text
PREPARE
  ↓
COMMITTED
  ↓
VISIBLE
```

失败则：

```text
PREPARE / COMMITTED
  ↓
ABORTED
```

BE 写完数据，只是生成了待提交的 Rowset。只有 FE 提交并发布版本后，查询才看得到。

查询可见性路径：

```text
写入磁盘
  ↓
返回 commit info
  ↓
FE commit
  ↓
FE publish
  ↓
BE tablet version 更新
  ↓
查询可见
```

`COMMITTED` 表示事务提交成功，但发布可见可能稍有延迟。`VISIBLE` 表示数据已经可查询。

### 分区、分桶与 Tablet 路由

数据进入 `OlapTableSink` 后，Doris 先判断每一行属于哪个分区，再根据分桶列计算 Bucket，最后找到目标 Tablet。

```text
Row
  ↓
读取分区列
  ↓
匹配 Range / List Partition
  ↓
得到 partition_id
  ↓
根据分桶列计算 hash
  ↓
得到 bucket_id
  ↓
得到 tablet_id
```

例如表按日期分区、按 `user_id` HASH 分桶：

```sql
PARTITION BY RANGE(dt)
DISTRIBUTED BY HASH(user_id) BUCKETS 16
```

Doris 会找到某行的目标 partition，然后计算 `bucket = hash(user_id) % 16`，最终得到目标 Tablet。

### TabletWriter、DeltaWriter、MemTable、Segment 与 Rowset

目标 BE 收到写入数据后，会通过写入通道写入 Tablet：

```text
LoadChannel
  ↓
TabletsChannel
  ↓
TabletWriter / DeltaWriter
  ↓
MemTable
  ↓
RowsetWriter
  ↓
Segment / Rowset
```

Doris 不会每来一行就落盘，而是先写入内存缓冲 MemTable。MemTable 达到阈值后 flush 成 Segment 文件。多个 Segment 会组成一个 Rowset。

```text
Rows
  ↓
MemTable
  ↓
达到阈值
  ↓
flush
  ↓
Segment file
  ↓
Rowset
```

生成 Segment 时可能做列式编码、压缩、索引构建、ZoneMap、Bitmap Index、BloomFilter、倒排索引和短 key index。

一次导入在某个 Tablet 上写入的数据会形成一个 Rowset：

```text
Tablet 10001
  ↓
Rowset txn_123
      ├── segment_0
      ├── segment_1
      └── segment_2
```

此时 Rowset 还不是可见版本，只是和某个事务绑定的临时写入结果。只有 publish 后，pending rowset 才会变成 Tablet 的新版本。

### 表模型对写入的影响

Duplicate Key 表主要是追加写，适合日志、明细数据。Aggregate Key 表保留聚合语义，相同 key 的 value 列按聚合函数合并。Unique Key 表表达主键更新语义，Doris 2.x 常见是 Merge-on-Write：同 key 新数据写入新版本，查询时看到最新版本，旧版本后续通过 compaction 清理。

### Publish Version 与查询可见

FE commit 后，会通知相关 BE 发布版本：

```text
FE
  ↓
publish version request
  ↓
BE
  ↓
把 txn rowset 转成 tablet 新版本
  ↓
tablet version graph 更新
  ↓
数据可见
```

例如原来 Tablet 版本是：

```text
[0-1], [2-2], [3-3]
```

事务发布后变成：

```text
[0-1], [2-2], [3-3], [4-4]
```

查询规划时就可以读到新版本。

### 写入后 Compaction

一次导入会生成 Rowset。如果频繁小批量写入，会产生很多 Rowset，影响查询性能、元数据开销、版本管理和 Compaction 压力。Doris 后台会做 Compaction，把多个小 Rowset 合并为更大的 Rowset。Compaction 不改变用户可见的逻辑数据，只是优化物理存储。

```text
多个小 Rowset
  ↓
Compaction
  ↓
较大的 Rowset
```

生产上如果小批量导入太频繁，容易出现 too many versions、compaction score 高、BE 写入和查询变慢等问题。

### Routine Load 放入内部写入时序

Routine Load 的完整内部时序可以这样对应：

```text
FE Routine Load Scheduler
  ↓
创建 Task
  ↓
begin txn
  ↓
下发 Task 到 BE
  ↓
BE Kafka Consumer poll
  ↓
解析 Kafka 消息
  ↓
OlapTableSink
  ↓
Partition / Bucket / Tablet 路由
  ↓
TabletWriter / DeltaWriter
  ↓
MemTable
  ↓
Segment
  ↓
Rowset
  ↓
BE 返回 commit info + Kafka end offset
  ↓
FE commit txn
  ↓
FE publish version
  ↓
FE 更新 Kafka offset
  ↓
下一批 Task
```

Routine Load 里最重要的是这个顺序：

```text
写 Rowset
  ↓
commit txn
  ↓
publish visible
  ↓
更新 Kafka offset
```

不能先更新 Kafka offset，否则 Doris 写入失败会丢数据。

### Stream Load 与 INSERT INTO 的内部对应

Stream Load 的内部链路：

```text
Client HTTP PUT
  ↓
FE / BE 接收请求
  ↓
begin txn
  ↓
BE 接收文件流
  ↓
解析 CSV / JSON / Parquet / ORC
  ↓
OlapTableSink
  ↓
Tablet 写入
  ↓
Rowset
  ↓
commit txn
  ↓
publish version
  ↓
HTTP 返回结果
```

`INSERT INTO SELECT` 的内部链路：

```text
Client SQL
  ↓
FE Parser / Analyzer / Planner
  ↓
begin txn
  ↓
BE 执行 SELECT
  ↓
中间结果进入 OlapTableSink
  ↓
Tablet 写入
  ↓
Rowset
  ↓
commit txn
  ↓
publish version
  ↓
返回 affected rows
```

### 核心总结

Doris 内部写入不是直接把数据插进一张表，而是先按分区分桶把数据写成各个 Tablet 上的临时 Rowset，再由 FE 通过事务提交和版本发布，把这些 Rowset 变成查询可见的新版本。

最核心的内部写入顺序是：

```text
FE 开事务
  ↓
BE 收数据
  ↓
BE 解析和转换
  ↓
BE 按分区分桶路由到 Tablet
  ↓
BE 写 MemTable
  ↓
BE flush Segment
  ↓
BE 生成 Rowset
  ↓
BE 返回 commit info
  ↓
FE commit 事务
  ↓
FE publish 版本
  ↓
Tablet 新版本可见
```

## Integration Decisions

这页保持为 source guide，而不是提升为稳定概念页，因为它保存的是一段多轮教学解释的完整下钻过程：先横向梳理 Doris 写入方式，再纵向下钻 Routine Load、Task、BE 执行和内部存储写入链路。后续如果继续学习 Doris，可以从这页拆出更稳定的概念页，例如 Doris Load Transaction、Doris Rowset、Doris Routine Load 或 Tablet Version Visibility。

当前内容中的版本判断基于 Doris 2.1.x / 2.1.11 语境；“2.11”如果实际指不同版本，需要用官方文档进一步校准。Routine Load 细节也可能随版本演进，尤其是 Group Commit、Unique Key Merge-on-Write、部分列更新和 Connector 生态相关行为。

## Open Questions

- “Doris 2.11”是否确指 2.1.11，而不是其他内部版本号或误写。
- Routine Load 的 FE/BE 内部类名、事务回调和 publish 细节是否需要进一步对照源码确认。
- Unique Key、Merge-on-Write、partial update、delete sign、sequence column 等写入语义是否需要单独成页。
- 高频小批量写入与 Group Commit 的版本边界、适用条件和限制是否需要进一步展开。

## Related

- [[wiki/maps/CS Map]]
- [[wiki/topics/BoltDB Internals]]
- [[wiki/topics/High Concurrency]]
- [[wiki/topics/Testing Strategy]]
