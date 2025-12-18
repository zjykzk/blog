+++
author = "zenk"
slug = ""
tags = ["rocketmq"]
draft = true
categories=["cs"]
title="RocketMQ中的一些实现细节"
description="RocketMQ中的一些实现细节。"
date="2018-10-24T10:23:16+08:00"

+++

**1. ConsumeQueue如何恢复writePosition/commitPosition/flushedPosition**

`ConsumeQueue.recover()`函数中会遍历所有的MappedFile，计算出当前`ConsumeQueue`的偏移量，然后调用`MappedFileQueue.truncateDirtyFiles()`设置`writePosition/commitPosition/flushedPosition`。

**2. 怎么判断PageCache繁忙**

`CommitLog`在写入的时候有一个锁，通过计算锁的时长。