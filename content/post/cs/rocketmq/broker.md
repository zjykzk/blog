+++
author = "zenk"
slug = ""
tags = ["mq","rocketmq"]
draft = true
categories=["cs"]
title="rocketmq broker模块"
description="消息队列RocketMQ的核心模块broker的设计与实现。"
date="2017-11-20T18:15:51+08:00"
+++

# rocketmq broker模块

broker模块是rocketmq的核心。主要功能：

1. RPC接口
2. 管理消费者信息
3. 管理消息
4. 主重同步
5. 状态统计

![/static/imgs/rocketmq/broker.png]()

## MessageStore

消息管理模块。

TODO

## RemotingServer

处理请求的模块。包含：

1. 发消息
2. 拉消息
3. 消费者管理
4. admin请求
5. 事务
6. 与namesrv/filterserver连接的客户端管理

分几类请求，每类请求有自己的请求队列以及相应的处理请求的线程池，通过请求编码来绑定队列和线程池。

![/static/imgs/rocketmq/broker-remotingserver.png]()

### 协议

长度头的方式。

|<-- 4 byte -->|<--  4 byte -->   |
+------------------+---------------------+-------------------+----------------+
| total length | header length| header data | body data |
+------------------+---------------------+-------------------+----------------+

### 数据封包

1. JSON，默认
2. ROCKETMQ，按照字段类型封包

## BrokerOuterAPI

broker和namesrv以及主broker通信的API。主要包含：

1. 向namesrv注册broker
2. 向主broker拉取订阅信息
3. 向主broker拉取topic信息

## PullRequestHoldService

当broker接收到拉取消息的请求，当前执行请求的时候，没有找到消息，同时判断消息在后面一段时间能够取到，该消息就会被本模块处理，也就是放入一个队列一段时间以后再处理。

### 再次拉取的条件

1. 请求的偏移量比当前的偏移量大
2. 请求偏移量偏移量为0
3. 请求没有匹配到
4. 请求偏移量下面的数据找不到

### 拉取时间

1. 长模式，5秒，默认模式
2. 短模式，1秒

## ClientHouseKeepingService

负责清理broker和其他模块的异常连接，主要包括跟生产者、消费者以及FilterServer之间的连接。

## BrokerStatsManager

管理broker统计信息。定时统计各种指标比如：tps/消息总数。

## FilterServerManager

负责通过JAVA代码过滤消息。提供拉取消息和注册过滤消息的JAVA代码的接口。

## BrokerFastFailure

每10ms检查等待写盘的消息，在磁盘IO过载或者等待时间过长情况下，返回系统繁忙。

1. 写消息的时候会有一个锁，当锁的时间过长时，表示系统页刷盘太慢，IO过载。这时，broker会把没有处理的消息都以系统繁忙的状态返回，直到系统恢复正常。
2. 检查发送消息的队列，把等待时间过长的消息以系统繁忙的状态返回，直到发送消息的队列为空为止。