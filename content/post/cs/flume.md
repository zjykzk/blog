+++
author = "zenk"
date = "2016-03-27T22:17:17+08:00"
description = "description"
draft = false
keywords = ["flume", "日志收集"]
tags = ["编程"]
title = "flume"
topics = ["大数据","技术"]
type = "post"

+++
# 简介

flume是通用的数据收集框架。特点是分布式、高可靠、高可用、高可定制化。

# 架构

![](/imgs/flume.dot.png)

# 概念

## source

数据的生成源。比如：读取一个本地文件，MQ等等。一个数据单元被封装成一个**event**。

### event

数据单元，从**source**产生，直到被序列化到存储中。**event**包含*header*，*body*两个部分：

* header: 一个map数据，可以被**interceptor**引用
* body: 一个字节序列，具体日志数据

### interceptor

**source**读取一个**event**在放到**channel**中之前，**event**可以被添加数据。比如说：采集机器的主机名称，时间戳。

## channel

数据队列，高可用的保障。**source**产生的数据先放到这里，**sink**接着从这里取出来放到存储当中。

### channel selector

两个作用：

1. 复制：把一个**event**写到一个或者多个**channel**中
2. 路由：根据**event**中的某个属性值，把数据写到指定的**channel**中

## sink

负责把**channel**中的数据写入目标存储。

### sink processor

选择**sink**，在这里可以完成负载均衡和容错处理。

### event serializer

把**event**中的数据，转换成存储需要的格式。
