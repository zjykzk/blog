---
title: BoltDB Internals
type: topic
status: growing
source_count: 1
updated: 2026-04-21
aliases:
  - bolt源码分析
  - bolt internals
tags:
  - database
  - storage
  - golang
---

# BoltDB Internals

BoltDB 是一个非常适合入门数据库实现的案例：代码量相对小，但已经覆盖了页式存储、B+ 树、事务、空闲页管理、写时复制等核心机制。

## Main structural pieces

- `node`：内存中的 B+ 树节点
- `inode`：节点中 key / value 或 key / pgid 的元信息
- `page`：磁盘上的页表示
- `freelist`：管理可复用页
- `bucket`：类似逻辑分区，每个 bucket 对应一棵 B+ 树
- `cursor`：有序遍历接口
- `tx`：事务上下文
- `meta`：数据库元信息

## Design ideas

### Single-file storage

- 以单文件保存数据
- 读写单位按 page size 对齐
- 使用 mmap 读取

### Copy-on-write

写入更新时，不原地改旧 page，而是把修改写入新 page。这样更容易实现事务隔离，同时旧 page 可以通过 freelist 回收复用。

### Freelist

freelist 负责管理可以复用的页，以及那些暂时还不能立即复用、需要等事务边界推进后再释放的页。

## Why it matters

如果你想理解数据库的最小核心构件，BoltDB 是很好的学习样本，因为它把很多数据库设计问题压缩到了一个相对紧凑的实现里。

## Related

- [[wiki/sources/Published Posts]]
- [[content/posts/cs/db/bolt]]
