---
title: High Concurrency
type: topic
status: seed
source_count: 1
updated: 2026-04-21
aliases:
  - 高并发
tags:
  - cs
  - concurrency
  - systems
---

# High Concurrency

当前这篇旧笔记内容还很少，但主题本身值得先占位，因为它很可能会成为系统设计和性能治理的重要母页。

## Core idea

当前线索虽然只留下一个很短的案例入口，但它已经暴露出高并发主题里最常见的一类问题：

- 在流量、连接、消息或会话数量上升时，系统某个环节因为资源耗尽而失稳
- 当前已知案例：信令助手 OOM 问题

所以高并发不应该只被理解成“请求很多”，而应该理解成：系统在高负载下如何维持可用性、延迟、内存稳定性和故障边界。

## Key dimensions

高并发问题通常会牵涉几个核心维度：

- 资源耗尽：内存、连接、线程、队列、文件句柄
- 吞吐与延迟平衡：追求吞吐时可能牺牲响应时间
- 排队与背压：入口流量大于处理能力时，系统如何不被压垮
- 内存与对象生命周期：缓存、批量、堆积对象是否可控
- 容量评估与故障隔离：局部压力能否被局部吸收，而不是扩散成系统级故障

## A practical lens from the OOM case

如果从“信令助手 OOM”这个入口反推，一个高并发问题通常至少可以按下面顺序检查：

1. 是谁在快速增长：请求数、连接数、消息数、对象数、缓冲区还是 goroutine 数
2. 增长是否可被限制：是否有队列上限、连接上限、超时、丢弃策略
3. 压力是否被放大：是否存在重试风暴、无限堆积、慢消费者、批量过大
4. 故障是否能隔离：一个热点资源出问题会不会拖垮其他路径
5. 系统是否能快速降级：是否可以拒绝、限流、熔断、缩短保留时间

## Why it matters

高并发问题的难点，不只是“代码够不够快”，而是系统是否能在压力上升时保持有序：

- 不被单点资源耗尽拖垮
- 不把局部问题放大成级联故障
- 不在错误恢复过程中进一步放大压力

## Upstream topics

- [[wiki/topics/Modern Software Engineering]]

## Peer topics

- [[wiki/topics/Circuit Breaker]]
- [[wiki/topics/Go Memory Model]]

## Navigation

- [[wiki/maps/CS Map]]

## Source notes

- `mobu/work/高并发.md`
