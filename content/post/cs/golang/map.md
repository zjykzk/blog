+++
author = "zenk"
date = "2017-06-15T19:13:25+08:00"
slug = ""
tags = ["golang","编程"]

draft = true

title = "map 内部实现"

categories=["cs"]

+++

# hash

TODO

# 扩容

TODO

# 查询

TODO

# 删除

TODO

# 更新

TODO

# 线程安全

TODO

# 类型

golang中的map是一个 **指针**。当执行语句 `make(map[string]string)` 的时候，其实是调用了 `makemap` 函数：

```go
// file: runtime/hashmap.go:L222
func makemap(t *maptype, hint64, h *hmap, bucket unsafe.Pointer) *hmap
```

显然，`makemap` 返回的是指针。

## 数据结构

#### hashmap

```go
// hash map
type hmap struct {
    count     int    // 元素的个数 == len()返回的值，必须放在第一个位置因为 len函数需要使用
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

    // If both key and value do not contain pointers and are inline, then we mark bucket
    // type as containing no pointers. This avoids scanning such maps.
    // However, bmap.overflow is a pointer. In order to keep overflow buckets
    // alive, we store pointers to all overflow buckets in hmap.overflow.
    // Overflow is used only if key and value do not contain pointers.
    // overflow[0] contains overflow buckets for hmap.buckets.
    // overflow[1] contains overflow buckets for hmap.oldbuckets.
    // The first indirection allows us to reduce static size of hmap.
    // The second indirection allows to store a pointer to the slice in hiter.
    // 当key和value的类型不包含指针的时候，key和value就会做inline处理(怎么处理的)
    // 保证overflow的bucket活着，不被gc回收
    overflow *[2]*[]*bmap
}
```

#### bucket

每个bucket固定包含8个key和value。实现上面是一个固定的大小连续内存块，分成四部分：

1. 每个条目的状态
2. 8个key值
3. 8个value值
4. 指向下个bucket的指针

数据结构定义如下：

```go
// bucket
type bmap struct {
        // tophash generally contains the top byte of the hash value
        // for each key in this bucket. If tophash[0] < minTopHash,
        // tophash[0] is a bucket evacuation state instead.
        tophash [bucketCnt]uint8
        // Followed by bucketCnt keys and then bucketCnt values.
        // NOTE: packing all the keys together and then all the values together makes the
        // code a bit more complicated than alternating key/value/key/value/... but it allows
        // us to eliminate padding which would be needed for, e.g., map[int64]int8.
        // Followed by an overflow pointer.
}
```

##### 条目状态

. `0` 空，可以被使用

. `1` 空，bucket中的内容已经被移到了新的bucket中

. `2` 该条目已经被移到了新的bucket，该bucket的位置在处在前半部分

. `3` 该条目已经被移到了新的bucket，该bucket的位置在处在后半部分

. 其他大于等于`4` 的值，来自key的hash值的最高8位，如果高8位值小于4，则加4

##### 内存布局

```
   ^   +-----------------+ -\
   |   |       bucket0   |  |------> +------------+
   |   +-----------------+ -/        | tophash 0  |
   |   |       bucket1   |           +------------+
   |   +-----------------+           | tophash 1  |
2^h.B  |      .......    |           +------------+
   |   +-----------------+           | .........  |
   |   | bucket2^h.B - 2 |           +------------+
   |   +-----------------+           | tophash 6  |
   |   | bucket2^h.B - 1 |           +------------+
   v   +-----------------+           | tophash 7  |
                                     +------------+
                                     |   key 0    |
                                     +------------+
                                     |   key 1    |
                                     +------------+
                                     |   .....    |
                                     +------------+
                                     |   key 6    |
                                     +------------+
                                     |   key 7    |
                                     +------------+
                                     |  value 0   |
                                     +------------+
                                     |  value 1   |
                                     +------------+
                                     |  .......   |
                                     +------------+
                                     |  value 6   |
                                     +------------+
                                     |  value 7   |
                                     +------------+ -\
                                     |overflow_ptr|  |-----> new bucket address
                                     +------------+ -/
```
