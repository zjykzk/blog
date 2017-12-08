+++
author = "zenk"
tags = ["mq","rocketmq"]
draft = true
categories=["cs"]
title="rocketmq store模块"
description="消息队列RocketMQ的核心模块store的设计与实现。"
date="2017-12-08T17:59:56+08:00"
+++

# rocketmq store模块

store模块是rocketmq的核心。主要功能有：

1. 消息存储管理
2. 消息的索引存储管理
3. 消费队列存储管理
4. 消息的主从同步
5. 延迟消息的管理

## CommitLog

## FlushConsumeQueueService

## CleanCommitLogService

## CleanConsumeQueueService

## IndexService

## AllocateMappedFileService

## ReputMessageService

## HAService

## ScheduleMessageService

## StoreStatsService

## TransientStorePool