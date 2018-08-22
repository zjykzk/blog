+++
author = "zenk"
slug = ""
tags = ["mq","pulsar"]
draft = true
categories=["cs"]
title="pulsar"
description="pulsar下一代分布式消息系统"
date="2018-08-20T16:31:35+08:00"
+++

https://streaml.io/blog/why-apache-pulsar

https://streaml.io/blog/why-apache-pulsar-part-2

## 介绍

特点

支持topic数量

投递保证

性能

对比

## 架构

## 协议

## 生成消费模型

## 存储

**bookkeeper**

如何写quorum，PendingAddOp会等待多个bookier写完

bookkeeper中的journal文件写要求比较高，因为这个文件内容是同步写的，最好用SSD

topic的映射

message的映射

读写逻辑

高可用

## 高可用

## 高并发