+++
author = "zenk"
slug = ""
tags = ["transaction"]
draft = true
categories=["cs"]
title="二阶段提交和三阶段提交"
description="2PC&3PC"
date="2020-04-17T15:12:22+08:00"

+++

事务恢复需要满足的两个条件：

In particular, it must enforce two rules:
**The Write-Ahead Log Protocol**: Do not flush an uncommitted update to the stable database until the log record containing its before-image has been flushed to the log.
**The Force-at-Commit Rule**: Do not commit a transaction until the after-images of all of its updated pages are in stable storage(in the log or the stable	database)

## 缘起

事务是一段访问或者更新数据的程序。它的特点是ACID。本地事务只涉及到一个数据库能够保证事务ACID了。当涉及到多个不同数据库（广义的数据库，他们可以是MQ，甚至缓存）操作时，为了保证每个数据库的操作要么都成功或者都失败，就需要额外的技术来处理。这是因为单个数据库操作会失败，同时通信失败会导致整个事务无法感知这个失败。二阶段提交（2PC）或者三阶段提交（3PC）就是用来解决这个问题。

一般来说这个有两个角色一个是事务协调者，简称**TC**，一个是事务参，简称**TP**。下文用简称来说明。

## 2PC