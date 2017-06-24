+++
author = "zenk"
date = "2016-10-09T14:45:21+08:00"
description = "prometheus介绍"
draft = false
keywords = ["monitor", "prometheus"]
tags = ["编程"]
title = "prometheus"
type = "post"

+++

prometheus是开源的现代监控系统。它用go开发，发布于2012。
社区热度比较高，功能比较丰富灵活。

## 架构

![](/imgs/promutheus.arch.svg)

## 基本概念

### 数据模型

prometheus把数据当作时间序列进行存储。
每个时间序列通过 **metric name**和 **key-value pairs**(也叫做 **label**)标识。

**metric name**表示需要进行测量的系统指标。
它允许包含ASCII字母，数字，下划线和分号。
正则表示为：\[a-zA-Z_:]\[a-zA-Z0-9_:]*。

**label**表示一个系统指标的维度，可以按照这个维度进行查询统计。
Label名字允许包含ASCII字母，数字以及下划线。
正则表示为：\[a-zA-Z_][a-zA-Z0-9_]*。同时，“__”开头的名字系统保留的。
Label值允许任意的Unicode字符

### 度量类型

#### Counter

累计统计度量的单个值。适用于只增不减度量，比如累计请求数量。

#### Gauge

统计度量的单个值。适用于可以增减的度量，比如当前的内存使用情况。

#### Histogram

统计度量事件发生的次数以及度量值的和。还支持统计小于某个阀值的度量事件发生的次数。

这个度量类型有三个时间序列统计：

- \<base_name>_bucket{le="upper inclusive bound"}：小于某个阀值的度量事件发生的次数
- \<base_name>_sum：度量值的和
- \<base_name>_count：度量事件发生的次数

#### Summary

统计度量时间发生的次数以及度量值的和。还支持统计某个百分比内的度量事件发生的次数。

这个度量类型有三个时间序列统计：

- \<base_name>{quantile="\<p>"}：度量值在前百分之p的度量事件发生的次数
- \<base_name>_sum：度量值的和
- \<base_name>_count：度量事件发生的次数

### Job & Instance

在prometheus里面对监控的对象分成Job和Instance。Instance代表一个监控的实例。比如
一个支付进程。Job代表一个监控的逻辑单位。
比如支付服务，它在多台机器上面部署着，每台机器对应一个Instance。

* job: payment-server
    - instance 1: 1.2.3.4:5678
    - instance 2: 1.2.3.5:5689
    - instance 3: 1.2.3.6:5689

#### 自动生成的label和时间序列

当prometheus抓取一个目标的时候，会自动生成时间序列以及label，用来标识抓取的目标状态。

label:

* job: 配置好的job名字
* instance:\<host>:\<port>格式的url

时间序列：

* up{job="\<job-name>", instance="\<host:port>"}：1 表示监控目标活着，0表示挂了
* scrape_duration_seconds{job="\<job-name>", instance="\<host:port>"}：抓取日志的时间
