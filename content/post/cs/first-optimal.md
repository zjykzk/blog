+++
author = "zenk"
slug = ""
tags = ["编程"]
draft = false
categories=["cs"]
title="记一次mongo数据库优化经历"
description="优化首要的是profile，profile一切"
date="2017-10-24T18:46:11+08:00"
+++

# 缘起

最近，做一个项目：封装一个MQ，提供发送、拉取、查询的基本功能，需要保证一条消息只被消费一次。写完了基本功能以后，开始做benchmark。结果超级糟糕：

| 发送线程数量 | 消费线程数量 |  发送TPS  | 消费TPS |
| :----: | :----: | :-----: | :---: |
|   3    |   3    | 200-400 | 20-60 |

而且，随着消费线程的数量增加发送&消费的TPS都下降。

# 排查

## 接口

一次发送涉及的数据库操作：

1. 一次topic查询
2. 一次跟MQ之间的RPC
3. 一次写统计数据

一次消费涉及的数据库操作：

1. 两次cas操作
2. 两次写统计操作

## 系统状态

### 磁盘IO

通过命令 `iotop` 发现：mongodb写磁盘速度最大2M/s。

### 网络

通过命令 `nethogs` 发现：mongodb的通信速度最大200+KB/s。

### 系统总体情况

通过命令`vmstat`发现：

1. 系统和用户的CPU使用率都超低，两者加起来不到5%，系统的中断和上下文切换非常高，特别是上下文切换，达到了十几万/s
2. 从缓存写到磁盘的io比较高好几百/s
3. 内存使用率非常低

### 结论

问题一定是使用mongodb上面。

## 排查

### profile程序

通过golang自带的profile功能，在程序里面添加profile代码，通过`go tool pprof`对程序做profile，用 `go-torch`生成火焰图。发现果不其然，一个请求过程中，数据操作耗时占整体的40%以上。

发送消息火焰图

![](/imgs/create.job.png)

拉取消息火焰图

![](/imgs/pull.job.png)

确认消息火焰图

![](/imgs/finish.job.png)

通过看程序以及对需求的分析，程序可以做优化：

1. 统计数据可以不用每次都去写数据库，把它放在内存或者写本地磁盘，定期刷到数据库
2. 去重以后的消息，可以放在内存，减少拉取消息时候一次cas操作

### mongodb

通过命令 `mongostat` 查看mongodb的运行状态，发现随着消费线程并发的提高锁的百分比越来越高最后超过的90%。查看mongodb的版本是2.4.9，它用的全局锁。换个mongodb版本，避免锁的开销，通过了解公司线上使用的版本3.0.15，并使用wireTiger存储引擎。果断按照这个环境进行benchmark，结果仍然不尽任意。查看**profiler**，一个类似mysql的慢查询的命令。通过以下命令加上专家的讲解，其中扫描对象比较多（**从信息"nscannedObjects" : 71040看出**） 确认是缺少了一个索引。

```
> db.setProfilingLevel(2);
{"was" : 0 , "slowms" : 100, "ok" : 1} // "was" is the old setting
> db.system.profile.find().sort({millis:-1}) // 列出耗时的操作，按照操作耗时排序
{ "op" : "query", "ns" : "broker_test.working_message", "query" : { "$query" : { "state" : 2 }, "$orderby" : { "created_at" : 1 } }, "cursorid" : 24924786875, "ntoreturn" : 256, "ntoskip" : 0, "nscanned" : 0, "nscannedObjects" : 71040, "scanAndOrder" : true, "keyUpdates" : 
0, "writeConflicts" : 0, "numYield" : 557, "locks" : { "Global" : { "acquireCount" : { "r" : NumberLong(1116) } }, "Database" : { "acquireCount" : { "r" : NumberLong(558) } }, "Collection" : { "acquireCount" : { "r" : NumberLong(558) } } }, "nreturned" : 256, "responseLengt
h" : 182909, "millis" : 192, "execStats" : { "stage" : "OR", "nReturned" : 256, "executionTimeMillisEstimate" : 180, "works" : 71299, "advanced" : 256, "needTime" : 71043, "needFetch" : 0, "saveState" : 557, "restoreState" : 557, "isEOF" : 0, "invalidates" : 0, "dupsTested"
 : 256, "dupsDropped" : 0, "locsForgotten" : 0, "matchTested_0" : 0, "matchTested_1" : 0, "inputStages" : [ { "stage" : "SORT", "nReturned" : 256, "executionTimeMillisEstimate" : 180, "works" : 71299, "advanced" : 256, "needTime" : 71042, "needFetch" : 0, "saveState" : 557,
 "restoreState" : 557, "isEOF" : 1, "invalidates" : 0, "sortPattern" : { "created_at" : 1 }, "memUsage" : 184937, "memLimit" : 33554432, "limitAmount" : 256, "inputStage" : { "stage" : "COLLSCAN", "filter" : { "state" : { "$eq" : 2 } }, "nReturned" : 70469, "executionTimeMi
llisEstimate" : 60, "works" : 71042, "advanced" : 70469, "needTime" : 572, "needFetch" : 0, "saveState" : 557, "restoreState" : 557, "isEOF" : 1, "invalidates" : 0, "direction" : "forward", "docsExamined" : 71040 } }, { "stage" : "SORT", "nReturned" : 0, "executionTimeMilli
sEstimate" : 0, "works" : 0, "advanced" : 0, "needTime" : 0, "needFetch" : 0, "saveState" : 557, "restoreState" : 557, "isEOF" : 0, "invalidates" : 0, "sortPattern" : { "created_at" : 1 }, "memUsage" : 0, "memLimit" : 33554432, "inputStage" : { "stage" : "COLLSCAN", "filter
" : { "state" : { "$eq" : 2 } }, "nReturned" : 0, "executionTimeMillisEstimate" : 0, "works" : 0, "advanced" : 0, "needTime" : 0, "needFetch" : 0, "saveState" : 557, "restoreState" : 557, "isEOF" : 0, "invalidates" : 0, "direction" : "forward", "docsExamined" : 0 } } ] }, "
ts" : ISODate("2017-10-24T07:54:08.773Z"), "client" : "10.200.20.56", "allUsers" : [ ], "user" : "" }
```

在程序里面加上索引，再次benchmark达到预期。

## 总结

本次调优最大问题是思维盲区，由于自己对mongodb不熟悉，就没有想到去profile mongodb，把精力放在了优化代码层面的数据库操作，中间还做过把消息放在缓存中虽然达到预期，但是有数据不一致的问题。其实，方法没对，**优化的首要原则是做profile，profile一切。**