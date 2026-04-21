---
title: Go Memory Model
type: topic
status: growing
source_count: 1
updated: 2026-04-21
aliases:
  - GO 内存模型
  - Go happens before
tags:
  - golang
  - concurrency
  - memory-model
---

# Go Memory Model

Go Memory Model 的核心作用，是定义并发场景下内存操作之间的顺序约束，让我们能判断一个 goroutine 读取到的值在什么条件下是确定的。

## Core idea

关键不是“语句看起来先后怎么写”，而是多个操作之间是否建立了 `happens before` 关系。

如果多个 goroutine 访问共享变量，但没有同步机制建立 `happens before`，那读取结果就可能是不确定的。

## Happens before

- 在同一个 goroutine 中，程序表达的顺序就是 happens before 顺序
- 在多个 goroutine 中，需要借助同步机制才能建立顺序约束
- 如果两个事件之间既不存在 happens before，也不存在 happens after，就可以视为并发

## What synchronization gives you

常见同步机制会建立 happens before 关系，例如：

- goroutine 创建
- channel 发送 / 接收 / close
- mutex / rwmutex
- once.Do
- init 到 main 的初始化顺序

## Practical takeaway

写并发程序时，真正重要的问题是：

- 哪个写必须先于哪个读可见？
- 这个顺序由什么同步原语来保证？
- 如果没有保证，是不是已经形成 data race？

## Related

- [[wiki/sources/Published Posts]]
- [[content/posts/cs/golang/go-memory-model]]
