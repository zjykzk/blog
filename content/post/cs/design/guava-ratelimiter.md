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

通过令牌桶算法实现。

## 记录未使用信息

实现中通过`storedPermits`表示有多长时间没有被使用了。这个信息可以处理资源的两种情况：
1. 资源充足。这个实现是Burst模式。
2. 资源超载。比如说缓存过期，导致请求处理变慢。这个实现是Warmup模式。

`storedPermits`的计算公式：`min(maxPermits, timeNotUsedMicros/coolDownIntervalMicros())`，其中`coolDownIntervalMicros()`和`maxPermits`在不同模式下面计算方式不同。

**Burst模式**

当RateLimiter发现资源没有没使用一段时间以后，任务现在资源的十分充分的，当请求过来的时候直接可以满足。`storedPermits`代表的就是当前充足资源的数量。

另外，`coolDownIntervalMicros()`返回`stableIntervalMicros`，`maxPermits`等于`permitsPerSecond`。

**Warmup模式**

```
          ^ throttling
          |
    cold  +                  /
 interval |                 /.
          |                / .
          |               /  .   ← "warmup period" is the area of the trapezoid between
          |              /   .     thresholdPermits and maxPermits
          |             /    .
          |            /     .
          |           /      .
   stable +----------/  WARM .
 interval |          .   UP  .
          |          . PERIOD.
          |          .       .
        0 +----------+-------+--------------→ storedPermits
          0 thresholdPermits maxPermits
```

上图是warmup模式消耗`storedPermits`所需要时间的建模。
1. RateLimiter的状态是一条垂直线，包含两个信息：当前的`storedPermits`和被消耗时需要的时间。
2. 当RateLimiter没有被使用时，`storedPermits`向`maxPermits`增加，增速是`warmupPeriodMicro/maxPermits`。
3. 当RateLimiter被使用时，`storedPermits`向0减少，需要的时间是这个函数的积分。

注意：
1. 这里`thresholdPermits`是任意值，源代码中假设`storedPermits`从`thresholdPermits`减少到0需要的时间为`warmupPeriod/2`。因此，`thresholdPermits=0.5*warmupPeriod/stableInterval`。
2. 另外，`storedPermits`从`maxPermits`减少到`thresholdPermits`需要的时间为`warmupPeriod`，因此`maxPermits=thresholdPermits + 2 * warmupPeriod / (stableInterval + coldInterval)`。

当RateLimiter发现资源没有没使用一段时间以后，请求再来的时候，资源需要一个预热，这个过程中请求处理会比预热完以后有一个变化。这个变化的效果可以是快也可以是慢，这个是根据`coldFactor`来定义。当这个值分三种情况：
1. 等于1，相当于没有预热效果。
2. 小于1，表示在没有使用这段时间里面，资源会有一部分的囤积，可以较快处理请求。
3. 大于1，表示在没有使用这段时间里面，资源被回收，需要重新申请来处理请求，所以会比较慢。

另外，`coolDownIntervalMicros()`返回`warmupPeriodMicro/maxPermits`。这是一个任意值，没有理论依据。

## 保存下次请求被满足的时间

这样做的好处是，可以比较方便判断在一段时间内，多个资源是否被满足的逻辑。permit的使用来源于两个地方：一段时间未使用而累积的`storedPermits`，以及一段时间以后才能满足的，假设用`freshPermits`表示。在不同模式下面消耗`storedPermits`和`freshPermits`需要的时间是不一样的。总的公式：`freshPermits * stableIntervalMicros + storedPermitsToWaitTime(storedPermits,permitsToTake)`，其中`storedPermitsToWaitTime(...)`在不同模式下面，实现方式不一样。

**Burst模式**

在这个模式下面，`storedPermitsToWaitTime(storedPermits,permitsToTake)`返回值是0。

**Warmup模式**

`storedPermitsToWaitTime(storedPermits,permitsToTake)`返回的是建模函数在`storedPermits,permitsToTake`之间的积分（图像面积）。