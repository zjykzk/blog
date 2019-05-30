+++
author = "zenk"
slug = ""
tags = ["golang"]
draft = true
categories=["cs"]
title="sync.Map实现分析"
description="sync.Map实现分析。"
date="2019-05-29T14:44:31+08:00"

+++

golang的SDK中提供线程安全的map实现`sync.Map`，它主要适用于两个场景：

1. 针对一个key一次写多次读。
2. 多个goroutine并发读写修改的key是没有交集。

在这两种情况下，相比一个`Mutex`或者`RWMutex`加上普通的map，锁的竞争要少的多。那为什么呢？

### 数据结构

```
type Map struct {
  mu Mutex

  // read contains the portion of the map's contents that are safe for
  // concurrent access (with or without mu held).
  //
  // The read field itself is always safe to load, but must only be stored with
  // mu held.
  //
  // Entries stored in read may be updated concurrently without mu, but updating
  // a previously-expunged entry requires that the entry be copied to the dirty
  // map and unexpunged with mu held.
  read atomic.Value // readOnly

  // dirty contains the portion of the map's contents that require mu to be
  // held. To ensure that the dirty map can be promoted to the read map quickly,
  // it also includes all of the non-expunged entries in the read map.
  //
  // Expunged entries are not stored in the dirty map. An expunged entry in the
  // clean map must be unexpunged and added to the dirty map before a new value
  // can be stored to it.
  //
  // If the dirty map is nil, the next write to the map will initialize it by
  // making a shallow copy of the clean map, omitting stale entries.
  dirty map[interface{}]*entry

  // misses counts the number of loads since the read map was last updated that
  // needed to lock mu to determine whether the key was present.
  //
  // Once enough misses have occurred to cover the cost of copying the dirty
  // map, the dirty map will be promoted to the read map (in the unamended
  // state) and the next store to the map will make a new dirty copy.
  misses int
}

// readOnly is an immutable struct stored atomically in the Map.read field.
type readOnly struct {
  m       map[interface{}]*entry
  amended bool // true if the dirty map contains some key not in m.
}

// An entry is a slot in the map corresponding to a particular key.
type entry struct {
  // p points to the interface{} value stored for the entry.
  //
  // If p == nil, the entry has been deleted and m.dirty == nil.
  //
  // If p == expunged, the entry has been deleted, m.dirty != nil, and the entry
  // is missing from m.dirty.
  //
  // Otherwise, the entry is valid and recorded in m.read.m[key] and, if m.dirty
  // != nil, in m.dirty[key].
  //
  // An entry can be deleted by atomic replacement with nil: when m.dirty is
  // next created, it will atomically replace nil with expunged and leave
  // m.dirty[key] unset.
  //
  // An entry's associated value can be updated by atomic replacement, provided
  // p != expunged. If p == expunged, an entry's associated value can be updated
  // only after first setting m.dirty[key] = e so that lookups using the dirty
  // map find the entry.
  p unsafe.Pointer // *interface{}
}
```

`Map.read`包含了部分数据，读写请求优先考虑`read`，针对它的操作都是CAS，无锁的。

`Map.dirty`包含的数据是`read`的超集，对他的操作需要加锁。

`readOnly.m`表示当前`read`的数据，`readOnly.amended`表示是否有数据在`dirty`中。

`entry`保存具体数值的指针。有三种情况：

1. `nil`，表示已经删除，这个时候`dirty`中`entry`的值也是`nil`，因为他们是同一个`entry`的地址。
2. `expunged`，表示数据已经擦除，`entry`不在`dirty`中。
3. 具体的数据值，一定会在`dirty`中。

### 接口

`sync.Map`包含五个接口：`Load`、`Store`、`LoadOrStore`、`Delete`和`Range`。

#### Load、Store、LoadOrStore和Delete

这几个接口都有类似的模式：

```
read, _ := m.read.Load().(readOnly)
if e, ok := read.m[key]; ok {
	ret := do_the_operation()
	if ret is success {
		return
	}
}
m.mu.Lock()
read, _ := m.read.Load().(readOnly)
if e, ok := read.m[key]; ok {
	ret := do_the_operation()
} else if e, ok := m.dirty[key]; ok {
	ret := do_the_operation()
}
m.mu.Unlock()
```

利用`read`的CAS操作减少锁并发，同时由于并发存在获取锁之后还是有可能数据已经在`read`中，因此还是对`read`再做一次同样的操作，复用内存。如果数据仍然不在`read`中才会考虑操作`dirty`。针对数据是否在`read`中这几个接口的逻辑如下：

`read`包含了部分数据，如果`key`存在并而且与它对应的`entry`不是`expunged`，数据操作优先在这里进行。

1. `Store`：直接更新`entry`值。
2. `Load`：直接返回`entry`值。
3. `LoadOrStore`:针对`entry`做`tryLoadOrStore`操作。
4. `Delete`:把`entry`设置成`nil`。

当数据不在`read`中时，就会涉及到`dirty`了：

1. `Store`：
   a. 如果`entry`在`read`中并且是`expunged`，则复用，同时把它修改成`nil`，然后把`entry`赋值到`dirty`，这样就避免了只在`read`不在`dirty`的情况。
   b. 如果`entry`在`dirty`中，那么更新`entry`值。
   c. 如果`entry`也不在`dirty`中，如果`dirty`是`nil`，则复制`read`中的`entry`值非`nil`的数据。然后，添加值到`dirty`。
2. `Load`：从`dirty`查找，同时增加`misses`。如果超过一定的阀值，就会发生数据从`dirty`到`read`的迁移。
3. `LoadOrStore`：流程和`Store`接口类似，只是返回值和对`entry`的处理逻辑不一样。
   a. 如果`entry`有值，则返回具体值以及存在的标识。
   b. 如果`entry`值为`nil`，设置`entry`为新的值并返回它和不存在标识。
   c. 如果`entry`值是`expunged`，则返回`nil`和存在标志，这个是比较特殊。在`LoadOrStore`同时，并发的把`entry`从`read`复制到`dirty`，这种情况就会发生。

#### Range

`Range`接口相对简单，如果有部分数据在`dirty`中就会把`dirty`的数据提升到`read`中，并重置`dirty`。然后，遍历的是`dirty`数据。否则，只遍历`read`中的数据。这里不保证能遍历到之后添加的数据。

通过上面的逻辑我们发现`read`和`dirty`直接数据流转逻辑如下：

1. `read`到`dirty`：在`Store`和`LoadOrStore`的时候，如果需要保存的key既不在`read`也不在`dirty`，而且这时`dirty`是`nil`，就会把`read`中的`nil`数据变成`expunged`，并复制除了这份以外的数据到`dirty`。
2. `dirty`到`read`：
   a. 在`Load`和`LoadOrStore`的时候，如果`read`中不存在，需要从`dirty`中获取数据，就会增加`misses`，当`misses`等于`dirty`的大小时，就会把`dirty`封装成`readOnly`，然后原子的赋值给`read`，并重置`dirty`。
   b. 在`Range`的时候，如果有数据不在`read`中同样会把`dirty`封装成`readOnly`，然后原子的赋值给`read`，并重置`dirty`数据。 

#### 疑问

1. **为什么需要expunged状态？**
2. **为什么newEntry的时候取的是参数interface{}的地址，这个地址不是栈上的么，会不会有问题？**

参数i已经逃逸到堆上面去了。

### 总结

文中开头提到的两个主要使用场景的原因主要使用的以下技术：

1. 无锁的CAS操作。
2. 读写分离，通过一份只读的数据结合CAS操作减少锁竞争。
3. 延迟删除，只有当只读的数据被写的数据覆盖以后才会被gc回收。
4. 内存复用，已经删除的数据所在的内存，当同一个key赋值的时候，可以被重新被使用。
5. 分摊分析。