+++
author = "zenk"
tags = ["rocketmq"]
draft = false
categories=["cs"]
title="offset管理"
description="offset相关原理与实现。"
date="2018-12-28T16:03:51+08:00"

+++

## 作用

记录每个消费队列的消费进度。以topic，group为单位。

## 类型

根据保存的位置可以分为本地和远程两种类型。本地类型就是一文件的形式保存在客户端，内容是json数据，而远程类型是指数据保存在broker服务器上面。

**代码**

本地类型：`org.apache.rocketmq.client.consumer.store.LocalFileOffsetStore`。
远程类型：`org.apache.rocketmq.client.consumer.store.RemoteBrokerOffsetStore`。

**使用**

默认情况，当消费模式是*广播*的时候使用*本地类型*，因为每个消费者管理自己的进度，而且是所有消费队列的进度，各个消费者之间不会有消费进度的交集。当消费模式是*集群*的时候使用*远程类型*，因为消息被多个消费者消费，每个消费者只负责消费其中部分消费队列，在添加、删除消费者的时候，原来消费者负责的消费队列会动态变化，因此需要集中管理消费进度，不然就冲突了。

但是，代码中依然提供了接口，让用户自己指定类型。（有什么特殊用法么？）

## 存储

**本地类型**

数据保存在`$storeDir/.rocketmq_offsets/$clientID/$group/offsets.json`中，里面的数据是非标准json数据，用的是阿里的fastjson这个库。其中`$storeDir`是可以通过系统变量`rocketmq.client.localOffsetStoreDir`配置，如果没有使用HOME目录。`$clientID`和`$group`分别表示消费者的id和分组。

```
// example
{"offsetTable":{{"brokerName":"topic","queueId":1,"topic":"broker"}:0}}
```

**远程类型**

数据保存在`$rootPath/config/consumerOffset.json`文件中，里面的数据是非标准json数据，用的是阿里的fastjson这个库。`offsetTable`中的key格式是`topic@group`，value格式`queueID:offset`。

```
// example
{
    "offsetTable":{
        "test@benchmark_consumer_61":{
            0:5280,1:5312,2:5312,3:5312
        }
    }
}
```

## 接口

通过接口类型`org.apache.rocketmq.client.consumer.store.OffsetStore`抽象了消费进度的相关操作。

`load`

在消费者启动的时候，需要把消费进度载入内存。只有本地类型会载入数据。

`updateOffset`

更新消费队列的进度。可以选择在比当前消费进度大的时候才更新，这个目的主要用于push模式下面消息是并发消费的，这样每批消息完成以后更新进度是并发，可能会导致进度低的晚于进度高的更新，这个模式就是为了避免这个情况，代码在类`ConsumeMessageConcurrentlyService`。

`readOffset`

读取消费队列的消费进度，数据存在内存和存储（本地或者broker服务）中，提供了三种读取的方式：1.内存；2.存储；3.先内存，如果没有后存储。在两个地方的实现中，从存储中读到数据以后会更新到内存。

`persistAll`

持久化指定的多个消费队列的消费进度。本地类型的实现中只会把指定的消费队列的消费进度保存到本地。远程类型除此之外，还会把指定的消费队列以外的那些队列从内存中移除。

`persist`

持久化指定的单个消费队列的消费进度。只有远程类型实现了该接口。

`removeOffset`

移除某个消费队列的消费进度。只有远程类型实现了该接口。

`updateConsumeOffsetToBroker`

更新消费队列到broker服务，只有远程类型实现了该接口。（这个设计好尴尬，本地类型需要么。。。）

## 管理

`org.apache.rocketmq.client.impl.consumer.RebalanceImpl.updateProcessQueueTableInRebalance`做消费的负载均衡时，会对消费进度做管理。这个过程通过对比新分配的消费队列（简称新队列）和`org.apache.rocketmq.client.impl.consumer.RebalanceImpl.processQueueTable`维护的消费队列（简称旧队列），有几种情况：

1. 如果旧队列的消费队列不在新队列中，那么就会先持久化该队列的消费进度，再做删除操作。*push模式同时优势有序的集群消费还需要做外的事情。*
2. 如果如果旧队列的消费队列在新队列中，*push模式下检查是否过期，过期的化先持久化，再删除进度。*
3. 如果新队列的消费队列不在旧队列中，删除消费进度。本地模式不会做删除操作，远程模式会把内存中的消费进度删除掉。同时，push模式下面会从存储中拉取消费进度并保存到内存。