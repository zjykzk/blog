+++
author = "zenk"
slug = ""
tags = ["program","design"]
draft = false
categories=["cs"]
title="guava中RateLimiter的设计"
description="guava中RateLimiter的设计原理。"
date="2018-10-11T15:33:32+08:00"

+++

guava中的[RateLimiter](https://github.com/google/guava/blob/master/guava/src/com/google/common/util/concurrent/RateLimiter.java#L131)实现了比较有意思的功能：

1. 平滑。
2. 记录未使用的信息。
3. 保存下次请求被满足的时间。

## 平滑

采用令牌桶算法实现。

## 记录未使用信息

实现中通过`storedPermits`表示有多长时间没有被使用了。这个信息可以处理资源的两种情况：

1. 资源充足。这个实现是Burst模式。
2. 资源超载。比如说缓存过期，导致请求处理变慢。这个实现是Warmup模式。

**Burst模式**

当RateLimiter发现资源没有没使用一段时间以后，任务现在资源的十分充分的，当请求过来的时候直接可以满足。`storedPermits`代表的就是当前充足资源的数量。

**Warmup模式**

当RateLimiter发现资源没有没使用一段时间以后，请求再来的时候，资源需要一个预热，这个过程中请求处理会比预热玩以后有一个变化。这个变化的效果可以是快也可以是慢，这个是根据`coldFactor`来定义。当这个值分三种情况：

1. 等于1，相当于没有预热效果。
2. 小于1，表示在没有使用这段时间里面，资源会有一部分的囤积，可以较快处理请求。
3. 大于1，表示在没有使用这段时间里面，资源被回收，需要重新申请来处理请求，所以会比较慢。

## 保存下次请求被满足的时间

这样做的好处是，可以比较方便判断在一段时间内，多个资源是否被满足的逻辑。