+++
author = "zenk"
date = "2017-03-28T11:22:09+08:00"
draft = false
keywords = ["go", "内存模型"]
tags = ["编程", "golang"]
title = "GO 内存模型"
description = "GO内存模型，happens before 定义"
type = "post"
categories = ["cs"]

+++

内存模型定义了一系列的条件，在这些条件下，多个goroutine对一个变量进行读写，保证一个goroutine读取到的值是是另外一个goroutine写入的某个值。

## Happens Before

编译器会对程序做优化，比如指令重排。在go语言中规定，在同一个goroutine里面，程序表达的顺序就是读写的顺序。但是，多个goroutine执行同样的代码时，就会出现读写顺序不一样的情况。例如，代码：

```go
int a = 0;
int b = 1;
print(a);
print(b);
```

在编译器的优化下，代码的执行顺序有可能变成下面这样的情况：

```go
int a = 0;
print(a);
int b = 1;
print(b);
```

但是，多个goroutine执行时，就无法保证打印*a*的时候，*b*的值一定是1.

**happens before**定义了内存操作的顺序，它是一种偏序。*e1* happens before *e2*, *e2* happens after *e1* 。如果 *e1* 既不happens before *e2* 也不happens after *e2* ，那么 *e1* 和 *e2* 是并发执行的。它有传递的性质（自反性，对称性就不考虑了）。这个关系就决定了共享变量在某个上下文下面读写顺序，那么它的具体值变化也就确定了。

*在一个goroutine中，happens before的顺序就是代码表达的顺序。*

共享变量 *v* 的读操作 *r* ，能够读到是另一个对变量 *v* 写操作 *w* 写入的值的条件是：

1. *w* happens before *r*
2. 没有其他的对变量 *v* 写操作happens before *r* 并且happens after *w*

这两个条件并不能保证有一个与 *r&w* 没有任何happens before关系的对共享变量 *v* 写操作 *w'* 的存在，导致 *r* 读到的是 *w'* 的结果。所以，保证 *r* 的结果是 *w* 的值的条件是：

1. *w* happens before *r*
2. 在 *w* 和 *r* 之间没有任何写操作，也就是说其他的写操作要么happens before *w* ，要么happens after *r*

在只有一个goroutine中1和2是等价的。 *r* 的结果一定是最近一次 *w* 的结果。**如果多个goroutine访问共享变量，就会产生竞争，必须要通过同步机制建立happens before关系才能确定共享变量的值**。


另外，1) 变量自动的初始化为其类型对应的0时，相当于是一个写操作，也会产生竞争；2) 对多个机器字进行读写的时候，哪个字先读写是不确定的。


## 同步机制

### 初始化

程序的初始化是通过一个goroutine执行的，这个goroutine会生成一个新的goroutine，因此会有竞争存在。

1. 包 *p* 依赖 *q*，*q* 的 *init* 函数happens before包 *p* 的任何操作
2. 所有 *init* 函数执行结束happens before *main.main* 函数

### Goroutine 创建

*go* 语句happens before新创建的goroutine的运行。以下代码中，***1*** happens before ***2***，***2*** happens before 函数***f***的执行，在将来的某个时刻所以打印 `hello, world`（可能是在hello函数返回之后）。

```go
var a string

func f() {
	print(a)
}

func hello() {
	a = "hello, world" // 1
	go f()			  // 2
}
```

### Goroutine 销毁

goroutine的退出跟其他的操作没有任何的happens before操作。以下代码无法保证***print(a)***的结果就是 `hello, world`。事实上，编译器完全有可能把 *go* 语句完全的删除掉。

```go
var a string

func hello() {
	go func() { a = "hello" }()
	print(a)
}
```

### Channel通信

channel在golang里面是同步的一个重要手段。channel上面的每个发送操作，都唯一对应着一个channel上面的接受操作，显然发送／接受操作在不同的goroutine下面才需要讨论。

**在一个channel上面的发送操作的完成happens before想对应的接受操作的完成。**以下代码中，按照本规则 *1* happens before *2* ，另外，因为 *2* 和 *3* 在同一个goroutine中执行， *2* happens before *3* ，所以能够打印出 `hello, world`。

```go
var c = make(chan int, 10)
var a string

func f() {
	a = "hello, world"
	c <- 0		// 1
}

func main() {
	go f()
	<-c			// 2
	print(a)	 // 3
}
```

**channel的关闭操作happens before因为关闭channel读到的0值。**上面例子中，用 *close( c)* 代替 *ch <- 0* 同样能够保证 *1*  happens before *2*  。

**没有缓冲的channel上面的接受操作happens before发送操作。也就是说，发送操作只有在channel上面进行的接受操作结束以后才返回。**以下代码中，根据本规则 *1* happens before *2* 。另外，因为 *2* 和 *3* 在同一个goroutine中执行， *2* happens before *3* ，所以能够打印出 `hello, world`。

```
var c = make(chan int)
var a string

func f() {
	a = "hello, world"
	<-c					// 1
}

func main() {
	go f()
	c <- 0				// 2
	print(a)			// 3
}
```

**如果一个channel有 *C* 容量的缓冲，第 *k* 个接受操作happens before第 *k+C* 个发送操作。**根据这个规则可以用带缓冲的channel来模拟信号量。以下程序就保证了，同时最多只有3个goroutine同时执行 *w* 函数。

```go
var limit = make(chan int, 3)

func main() {
	for _, w := range work {
		go func(w func()) {
			limit <- 1
			w()
			<-limit
		}(w)
	}
	select{}
}
```

### Locks

包 *sync* 实现了两类锁分别是： *sync.Mutex* 和 *sync.RWMutex。*

**给定类型为 *sync.Mutex* 或者是 *sync.RWMutex* 的变量 *l* ,以及满足 *n<m* 条件的整数。调用 *n* 次 *l.Unlock()*  happens before 调用 *m* 次 *l.Lock()* （返回）。**以下代码中，根据本规则 *1* happens before *2* ，另外，因为 *2* 和 *3* 在同一个goroutine中执行， *2* happens before *3* ，所以能够打印出 `hello, world`。

```go
var l sync.Mutex
var a string

func f() {
	a = "hello, world"
	l.Unlock()		// 1
}

func main() {
	l.Lock()
	go f()
	l.Lock()		// 2
	print(a)		// 3
}
```



**对于 *sync.RWMutex* 类型的变量l，存在一个整数 *n* ， *l.RLock* 的调用happens after(返回)调用 *n* 次 *l.Unlock* ，与这个 *l.RLock* 想对应的 *l.RUnlock* happens before 第 *n+1* 的 *l.Lock* 。**

### Once

Once提供了保证某段代码只执行一次的机制。对某个函数 *f* ， *once.Do(f)* 调用保证了 *f* 只被执行一次，如果有多个goroutine执行 *once.Do(f)* ，其中一个执行了，其他就等待直到f执行完毕。

**调用 *once.Do(f)* 中 *f* (返回)happens before 其他 *once.Do(f)* 调用完成。**

## 总结

为了更有效率的执行程序，编译器，CPU都会一某种方式进行优化。当程序是并发执行的时候，内存的数据就变得无法根据程序代码判断内存中的值。内存模型的作用就是在程序的层面规定内存的操作顺序，以达到确定内存值的目的。而happens before是一个定义这个操作顺序的规范。
