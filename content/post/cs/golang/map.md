+++
author = "zenk"
date = "2017-06-15T19:13:25+08:00"
slug = ""
tags = ["golang","编程"]
draft = false
title = "map 内部实现"
categories=["cs"]
description="golang 中map的实现细节，它是一个典型的hashmap。"

+++

# 类型

golang中的map是一个 **指针**。当执行语句 `make(map[string]string)` 的时候，其实是调用了 `makemap` 函数：

```go
// file: runtime/hashmap.go:L222
func makemap(t *maptype, hint64, h *hmap, bucket unsafe.Pointer) *hmap
```

显然，`makemap` 返回的是指针。

# 数据结构

## hashmap

```go
// hash map
type hmap struct {
    // 元素的个数 == len()返回的值，必须放在第一个位置因为 len函数需要使用
    count     int

    // map标记:
    // 1. key和value是否包指针
    // 2. 是否正在扩容
    // 3. 是否是同样大小的扩容
    // 4. 是否正在 `range`方式访问当前的buckets
    // 5. 是否有 `range`方式访问旧的bucket
    flags     uint8
    B         uint8  // log_2(B) == bucket数量
    noverflow uint16 // overflow bucket的数量，是个近似值
    hash0     uint32 // hash种子

    buckets    unsafe.Pointer // bucket slice指针，如果count == 0，这里的值为 nil
    oldbuckets unsafe.Pointer // bucket slice指针，仅当在扩容的时候不为nil
    nevacuate  uintptr        // 扩容时已经移到新的map中的bucket数量

    // 当key和value的类型不包含指针的时候，key和value就会做inline处理(怎么处理的)
    // 保证overflow的bucket活着，不被gc回收
    overflow *[2]*[]*bmap
}
```

## bucket

每个bucket固定包含8个key和value。实现上面是一个固定的大小连续内存块，分成四部分：

1. 每个条目的状态
2. 8个key值
3. 8个value值
4. 指向下个bucket的指针

数据结构定义如下：

```go
// bucket
type bmap struct {
        // 每个条目的状态，tophash[0]表示当前bucket中的条目是否已经完全移到新的bucket中去了
        tophash [bucketCnt]uint8
        // keys
        // values
        // Followed by an overflow pointer.
}
```

### 条目状态

. `0` 空，可以被使用

. `1` 空，bucket中的内容已经被移到了新的bucket中

. `2` 该条目已经被移到了新的bucket，该bucket的位置在处在前半部分

. `3` 该条目已经被移到了新的bucket，该bucket的位置在处在后半部分

. 其他大于等于`4` 的值，来自key的hash值的最高8位，如果高8位值小于4，则加4

#### 第一个条目状态

bucket的第一个条目`tophash[0]` 用来标识bucket中的条目是否已经全部被移到了新的bucket中去了， `1-3` 表示已经移动完。

### 内存布局

```
   ----+-----------------+ -.
   ^   |     bucket0     |  |------> +------------+
   |   +-----------------+ -'        | tophash0-7 |
2^h.B  |     .......     |           +------------+
   |   +-----------------+           |   key0-7   |
   v   | bucket2^h.B - 1 |           +------------+
   ----+-----------------+           |  value0-7  |
                                     +------------+ -.
                                     |overflow_ptr|  |-----> new bucket address
                                     +------------+ -'
```

选择这样的布局的好处：由于对齐的原因，*key0/value0/key1/value1...* 这样的形式可能需要更多的补齐空间，比如 `map[int64]int8` ，1字节的value后面需要补齐7个字节才能保证下一个key是 `int64` 对齐的。

## 装载因子

装载因子决定map的资源使用率以及性能高低，在实现map时，考虑四个方面：

1. %overflow：拥有overflow的bucket的百分比
2. bytes/entry: 每个key/value的额外开销
3. hitprobe: 查找存在的key时需要检查的条目数量
4. missprobe: 查找不存在的key是需要检查的条目数量

其测试数据如下：

| 装载因子 | %overflow | bytes/entry | hitprobe | missprobe |
| :--: | :-------: | :---------: | :------: | :-------: |
| 6.5  |   20.90   |    10.79    |   4.25   |    6.5    |

# hash函数

map中的key对应着一个hash函数，用于定位bucket。在golang的hash函数是固定的，用户无法修改。golang中的预定义基本类型，像 `int32/int64/string/interface` 等等都有一个hash函数与之对应，代码在runtime/alg.go中。对于struct/数组/slice，如果它每个字段或者元素都是有hash函数，那么该类型就有hash函数，hash值由每个字段的hash值来定义，代码在reflect/type.go函数`StructOf`中。

注：`map`是不能作为key的。

# 扩容

当进行添加元素的操作时，如果超过装载因子，或者overflow的bucket数量超出阈值，就会触发扩容的操作。如果是因为overflow的bucket数量过多引起的，map的容量不会扩大，不然就扩大为原来的大小的两倍。

在实现扩容的时候，会先为需要的bucket分配新内存，然后把旧的bucket保存起来，再把旧的内容移到新的bucket中去。

# 线程安全

map是线程不安全的。但是在实现中有很多关于并发访问的代码，比如

1. 在迭代的时候会做是否正在扩容
2. 添加数据的时候是否有其他数据正在写，有的话会panic

既然不是线程安全，为啥要做这样的检查，不检查的话可以简化代码提高性能。检查的好处就是告知提醒用户并发访问了map，但是这个检查也不是百分之一百的检测到所有的并发访问。

# 键值NaN

`NaN` 的hash值是随机([原因](https://research.swtch.com/randhash))，也就是说每次计算hash值都有可能是不一样的。这个跟python/java等其他语言有比较大的差别。

正是因为这样有了以下几个有趣的事情：

1. 当 `NaN` 作为key的时候，为了保持hash值的不变性，利用 `tophash` 的最低位来判断是放在扩容以后bucket的上半部份还是下半部分
2. 用 `NaN` 做key取数据时永远也取不到，用 `for` 迭代map是唯一一种访问 key为`NaN` 的内容的方式

# 迭代

`for` 语句迭代map，在会调用函数 `mapiterinit` 做初始化工作：

1. 随机挑选一个起始位置开始迭代：a. bucket随机选一个，b. bucket中的起始条目也是随机的
2. 初始化overflow，目的是为了防止那些内联的数据被gc，导致迭代失败

每次获取一个元素的时候调用函数`mapiternext`