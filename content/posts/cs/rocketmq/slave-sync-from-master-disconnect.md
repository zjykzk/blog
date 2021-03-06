+++
author = "zenk"
slug = ""
tags = ["mq","rocketmq"]
draft = false
categories=["cs"]
title="slave和master同步连接经常重连，导致发送消息失败"
description="slave向master同步数据的时候，由于没有发送自己的同步，导致没有同步新的消息，在SYNC_MASTER模式下，发消息失败。"
date="2018-10-22T17:07:02+08:00"

+++

## 缘起

封装RocketMQ的组件boots-broker每天都返回几个的500。排查发现是因为slave向master同步消息的时候，由于没有及时向master报告自己的同步进度，从而master没有向slave及时同步消息，导致消息发送失败。

## 排查过程

查看boots-broker日志，发现问题日志：

```
[TIMEOUT_CLEAN_QUEUE]broker busy, start flow control for a while, period in queue: 1008ms, size of queue: 0
```

说明，RocketMQ处理发送消息比较慢。可是，从`size of queue`可以看出，堆积的消息为0。

查看机器资源消耗情况，发现资源都是充裕的。

查看RocketMQ日志，发现store.log中有异常，master中的store.log周期性的发生以下日志：

```
2018-10-22 15:44:07 INFO AcceptSocketService - HAService receive new connection, /10.38.34.27:54052
2018-10-22 15:44:07 INFO ReadSocketService - ReadSocketService service started
2018-10-22 15:44:07 INFO WriteSocketService - WriteSocketService service started
2018-10-22 15:44:08 INFO WriteSocketService - WriteSocketService service end
2018-10-22 15:44:12 INFO ReadSocketService - slave[/10.38.34.27:54052] request offset 157843228
2018-10-22 15:44:12 INFO WriteSocketService - master transfer data from 157843228 to slave[/10.38.34.27:54052], and slave request 157843228
2018-10-22 15:44:33 WARN ReadSocketService - ha housekeeping, found this connection[/10.38.34.27:54052] expired, 20019
2018-10-22 15:44:33 INFO ReadSocketService - ReadSocketService service end
```

从上可以看出，slave主动向master建立连接，5s之后发送自己当前同步的进度，master收到以后向slave发送同步数据，最后master由于slave的连接过期，主动断开连接。

slave中的store.log周期性的发生以下日志：

```
2018-10-22 15:44:07 WARN HAClient - HAClient, housekeeping, found this connection[10.38.33.22:10912] expired, 1540194247979
2018-10-22 15:44:07 WARN HAClient - HAClient, master not response some time, so close connection
2018-10-22 15:44:33 INFO HAClient - HAClient, processReadEvent read socket < 0
```

从上可以看出，slave也发现和master的连接超时，断开连接。

到这里，非常困惑，master和slave都主动断开连接！看代码，master的同步比较清晰和日志也比较一致。slave的同步日志和日志不一致。slave的同步代码核心[代码](https://github.com/zjykzk/rocketmq/blob/master/store/src/main/java/org/apache/rocketmq/store/ha/HAService.java#L546)中通过比较`lastWriteTimestamp`和当前时间判断出与master的同步连接过期，以及master没有响应。在接收到master的消息、创建连接、关闭连接的时候都修改这个`lastWriteTimestamp`值。关闭重置为0，其他重置为当前时间。看日志发现`lastWriteTimestamp`和当前的时间差别巨大是`1540194247979`，可以得出`lastWriteTimestamp`其实是0。基本上可以判断是因为master主动关闭的。后来，通过tcpdump抓包得到了确认。这里要吐槽这个日志了，slave是被关闭的却是提示master没响应，其实master在关闭之前总共发了5次同步信息。

确认是master主动关闭，接下来的问题是为什么slave没有告诉master自己的进度。日志已经无能为力了，看到代码中有`while(true)`片段，猜测会不会是死循环，通过`jstack`发现没有。最后，通过手动添加日志发现master向slave发送的同步信息，slave都收到了，然后把`lastWriteTimestamp`重置为当前的时间，巧合的是，每次函数`isTimeToReportOffset`判断是否需要发送同步进度的时候恰好都为`false`。这是因为master向slave同步间隔和slave向master报告同步进度的间隔默认都是5s，slave处理master的同步信息以后会重置`lastWriteTimestamp`为当前时间，因此一直无法满足同步的条件，导致以上的现象。

## 解决方案

可以知道，连接经常断开显然会影响同步的效率。解决方案可以把master同步时间设置的比slave的同步长，比如slave的同步间隔为3s，master同步间隔为5s。

