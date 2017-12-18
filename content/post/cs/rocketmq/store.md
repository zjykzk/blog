+++
author = "zenk"
tags = ["mq","rocketmq"]
draft = true
categories=["cs"]
title="rocketmq store模块"
description="消息队列RocketMQ的核心模块store的设计与实现。"
date="2017-12-08T17:59:56+08:00"
+++

## 功能

store模块是rocketmq的核心。主要功能有：

1. 消息存储管理
2. 消息的索引存储管理
3. 消费队列存储管理
4. 消息的主从同步
5. 延迟消息的管理
6. 清理过期的消息和消费队列

保存消息的目录通过配置项 `storePathCommitLog` 指定，默认是 `$HOME/store/commitlog`

保存其他数据的目录通过配置项 `storePathRootDir` 指定，默认是 `$HOME/store`

告警的磁盘使用率阀值通过系统变量 ``指定，默认是 0.9

强制删除的磁盘使用率阀值通过系统变量 ``指定，默认是 0.75

## CommitLog

## 消费队列写盘

系统每隔1000ms（可配置）进行一次消费队列的写盘操作。

### 核心代码

```
org.apache.rocketmq.store.DefaultMessageStore.FlushConsumeQueueService
```



## 清理消息

系统每隔10s（可以配置）执行尝试删除过期的消息。

### 核心代码

```
org.apache.rocketmq.store.DefaultMessageStore.CleanCommitLogService
```

### 清理条件

1. 清理时间到达，默认是凌晨4点
2. 消息所在的磁盘使用率或者其他数据所在磁盘使用率操作告警阀值和强制删除阀值
   * 保存消息的目录通过配置项 `storePathCommitLog` 指定，默认是 `$HOME/store/commitlog`
   * 保存其他数据的目录通过配置项 `storePathRootDir` 指定，默认是 `$HOME/store`
   * 告警的磁盘使用率阀值通过系统变量 ``指定，默认是 0.9
   * 强制删除的磁盘使用率阀值通过系统变量 ``指定，默认是 0.75
3. 手动触发清理，这里提供了一个接口暴露给外面调用，调用以后会在连续执行20次删除

### 清理逻辑

1. 正常清理过期的消息，过期时间可以通过配置项 `fileReservedTime` 指定，默认是72小时

2. 清理上次没有清理成功的消息，这是因为消息被清理时，其他地方正在使用。每隔一段时间执行一次，同时如果距离上次被清理时间超过了一段时间会被强制清理

   * 通过配置项 `redeleteHangedFileInterval`指定执行周期，默认120s
   * 通过配置项 `destroyMapedFileIntervalForcibly`指定强制清理的时间，默认120s

## 清理消费队列以及索引

随着消息的清理，包含已经清理掉消息的消费队列以及索引就变得没有用处了，所以系统每隔100ms（可以配置）执行清理消费队列和索引。

### 核心代码

```
org.apache.rocketmq.store.DefaultMessageStore.CleanConsumeQueueService
```

### 清理逻辑

获取当前消息的最小偏移量，这个偏移量随着消息的清理会不停的变化。

1. 消费队列：如果队列的最大消息偏移量都比当前最小的消息偏移量小，那么就可以清理本队列
2. 消息索引：如果索引中最大的消息偏移量都比当前最小的消息偏移量小，那么就可以清理本索引

## IndexService

## AllocateMappedFileService

## ReputMessageService

## HA

![ha](/imgs/rocketmq/ha.png)

### 核心逻辑

1. 启动的时候，MASTER会启动监听服务`AcceptSocketService`，SLAVE会启动同步服务 `HAClient`
2. 建立连接`HAConnection`之后，MASTER会为连接建立两个线程`WriteSocketService`和`ReadSocketService`分别负责这条连接的写和读
3. SLAVE向MASTER报告，当前同步的位置，具体是到目前为止同步到的偏移量
4. MASTER根据SLAVE报告的偏移量，发送消息

### 核心代码

```
org.apache.rocketmq.store.ha.HAService
org.apache.rocketmq.store.ha.HAConnection
```

### SYNC_MASTER

在这种模式下，也是通过上述的HA实现的

## ScheduleMessageService

## StoreStatsService

## 写buffer

如果开启了这个功能，系统启动时会向系统申请多块写buffer。每块buffer都会被锁在内存中。这个buffer只会被commitlog使用。

### 核心代码

```
org.apache.rocketmq.store.TransientStorePool
```

## 内存映射的文件管理

rocketmq中的索引、消费队列、消息这些数据都通过内存映射进行读写。

### 映射文件

1. 逻辑文件：数据按照顺序写入，由类`org.apache.rocketmq.store.MappedFileQueue` 表示
2. 物理文件：具体写数据的文件，由类`org.apache.rocketmq.store.MappedFile` 表示

它们之间的关系：

```
|<-                                  MappedFileQueue                                        ->|
+-------------------+--------------------+-------------+-------------------+------------------+
|000000000000000000 | 000000000000000100 |   ...       |000000000000010000 |000000000000020000|
+-------------------+--------------------+-------------+-------------------+------------------+
|<- MappedFile-0  ->|<-  MappedFile-1  ->|   ...       |<- MappedFile-n-1->|<- MappedFile-n ->|
+-------------------+--------------------+-------------+-------------------+------------------+
```

一个 `MappedFileQueue` 由多个 `MappedFile` 组成，每个 `MappedFile` 文件大小相等，文件名是32个字符，并且表示当前文件中第一个记录在 `MappedFileQueue`所代表的逻辑文件中的序号。

### 引用计数

TODO

### 统计

TODO

### 优化

#### 预热

1. 新建`MappedFile`时通过先把文件映射的内存都写一遍，内核为文件分配物理页
2. 使用`mlock`锁住文件映射的物理内存，确保这部分内存不被交换出去
3. 使用`madvise`通知内核这部分数据将来会读到

#### 写buffer

建立一个buffer池，这些buffer是堆外内存。buffer所占用的内存是不会被交换出去的，同时也会通知内核这部分数据将来会读到。`MappedFile`新建的时候可以通过这个池子获得buffer作为写的buffer。