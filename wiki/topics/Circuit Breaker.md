---
title: Circuit Breaker
type: topic
status: growing
source_count: 1
updated: 2026-04-21
aliases:
  - 熔断
tags:
  - distributed-systems
  - resilience
  - architecture
---

# Circuit Breaker

Circuit Breaker 是分布式系统里的保护机制：当下游服务已经过载或不可用时，不再继续把请求打过去，而是主动快速失败，避免故障扩大。

## Why it exists

在 RPC 密集的系统里，如果某个服务已经不可用，还继续转发请求，会导致：

- 请求堆积
- 资源被进一步耗尽
- 故障从一个点扩散到多个依赖方

因此需要一个中间层来判断：当前请求是应该继续放行，还是应该直接拒绝。

## State machine

### Closed

- 正常转发请求
- 统计失败次数或失败率
- 达到阈值后切到 Open

### Open

- 直接拒绝请求
- 等待一个恢复窗口
- 到期后尝试进入 Half Open

### Half Open

- 放少量探测请求
- 成功则关闭
- 失败则重新打开

## Design concerns

- 不同错误类型应有不同策略
- 状态变化和失败请求需要记录到日志/监控
- Half Open 最好支持专门探测，而不是直接用用户请求探测
- 返回错误时要区分“后端错误”和“熔断器自己返回的错误”
- 需要支持人工重置
- 需要考虑并发下的计数开销
- 最好按资源维度隔离，而不是把所有请求混成一个断路器
- 如需重试失败请求，要处理幂等性

## Example implementation idea

Hystrix 的典型做法是维护滑动时间窗口，统计最近一段时间里的成功、失败、超时、拒绝，再决定是否打开断路器。

## Upstream topics

- [[wiki/topics/Modern Software Engineering]]

## Peer topics

- [[wiki/topics/Go Memory Model]]
- [[wiki/topics/BoltDB Internals]]

## Navigation

- [[wiki/maps/CS Map]]

## Source notes

- [[wiki/sources/Published Posts]]
- `content/posts/cs/dist/circuit-breaker.md`
