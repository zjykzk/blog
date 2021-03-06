+++
author = "zenk"
date = "2016-06-05T20:21:39+08:00"
description = "IEEE 754"
draft = true
keywords = ["program"]
tags = ["编程"]
title = "浮点数 IEEE 754"
topics = ["编程"]
type = "post"
categories = ["cs"]

+++

## 表示

标准IEEE 754中，浮点数由三部分组成符号、指数、尾数。

* 符号：表示正负，用**S**表示，用**Sn**表示使用的bit数
* 指数：2的幂次，用**E**表示，用**En**表示使用的bit数
* 尾数：小数部分，用**M**表示，用**Mn**表示使用的bit数

<pre>
+-----+------+--------+
|  S  |   E  |    M   |
+-----+------+--------+
</pre>

### 单、双精度的bit位数

| 类型   | Sn   | En   | Mn   | Sn+En+Mn |
| ---- | ---- | ---- | ---- | -------- |
| 单精度  | 1    | 8    | 23   | 32       |
| 双精度  | 1    | 11   | 52   | 64       |


浮点数从二进制到十进制数值的转化分两种情况：

1. normalized, E!=0

公式：value = (-1)^S * 2^(E - 2^(En - 1) + 1) * (1+M/2^Mn)
例子：

1.5

* 单精度

<pre>
|<-S->|<--E--->|<---------M----------->|
+-----+--------+-----------------------+
|  0  |01111111|10000000000000000000000|
+-----+--------+-----------------------+
</pre>

* 双精度
  <pre>
  |<-S->|<----E---->|<----------------------------M----------------------->|
  +-----+-----------+------------------------------------------------------+
  |  0  |01111111111|100000000000000000000000000000000000000000000000000000|
  +-----+-----------+------------------------------------------------------+
  </pre>

2. denormalized, E==0

公式：value = (-1)^S * 2^(2 - 2^(En - 1)) * (M/2^Mn) 

### 范围

* NAN:not a number，E==2^En - 1，M!=0
* 无穷大(小)Infinity: E==2^En - 1, M == 0
* normalized: E!=0
* denormalized: E==0
* 最大值：2^(2^(En-1)+1) * (2-2^-Mn)
* 最小值：-2^(2 - 2^(En - 1)) * (1-1/2^Mn)

### 精度
IEEE 754用有限的位数表示整个实数，肯定是不精确。主要表现在几个方面：

1. 无法覆盖所有实数，也就是说有些数根本无法表示，比如说：0.000000000000000000000001
2. 无法精确表达某些数，比如：0.3
3. 十进制精度(两浮点数的差，正确的小数个数)：1/2^Mn，单精度：1/2^23 = 0.0000001192092895507812，精确到6位；双精度：1/2^52 = 0.0000000000000002220446049250313，精确到15位。

## 加法

## 减法
