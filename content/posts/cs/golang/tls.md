+++
author = "zenk"
slug = ""
tags = ["golang"]
draft = false
categories=["cs"]
title="golang中的tls"
description="golang中tls的使用。"
date="2018-02-27T19:51:16+08:00"
+++

在golang中，为了性能的目的，当前执行的[`g`](https://github.com/golang/go/blob/release-branch.go1.8/src/runtime/runtime2.go#L332)是保存在当前线程的TLS中的，而TLS的地址在结构体[`m`](https://github.com/golang/go/blob/release-branch.go1.8/src/runtime/runtime2.go#L412)里面。问题是怎么放进去的呢？

可以从程序的启动入手，顺藤摸瓜。

编写一个打印`hello,world`的程序

```
// hello.go

package main

func main() {
        print("hello, world")
}
```

编译生成可执行文件

```
go build -o hello hello.go
```

用gdb进行调试，找到程序的入口 [`_rt0_amd64_linux`](https://github.com/golang/go/blob/release-branch.go1.8/src/runtime/rt0_linux_amd64.s#L7)

```
gdb hello
(gdb) info files
...
Entry point: 0x448f20
...
(gdb) list *0x448f20
0x448f20 is in _rt0_amd64_linux (/home/zenk/tools/goroot/src/runtime/rt0_linux_amd64.s:8)
3       // license that can be found in the LICENSE file.
4
5       #include "textflag.h"
6
7       TEXT _rt0_amd64_linux(SB),NOSPLIT,$-8
8               LEAQ    8(SP), SI // argv
9               MOVQ    0(SP), DI // argc
10              MOVQ    $main(SB), AX
11              JMP     AX
12
```

发现`_rt0_amd64_linux`调用了[`main`](https://github.com/golang/go/blob/release-branch.go1.8/src/runtime/rt0_linux_amd64.s#L72)函数，后者调用了[`runtime.rt0_go`](https://github.com/golang/go/blob/release-branch.go1.8/src/runtime/asm_amd64.s#L10)。而在函数`runtime.rt0_go`中

```
127 	LEAQ	runtime·m0+m_tls(SB), DI
128 	CALL	runtime·settls(SB)
```

把[`m0.tls`](https://github.com/golang/go/blob/release-branch.go1.8/src/runtime/proc.go#L79)的地址放到寄存器`DI`，并调用了函数`runtime.settls`，查看[`runtime.settls`](https://github.com/golang/go/blob/release-branch.go1.8/src/runtime/sys_linux_amd64.s#L496)核心代码

```
503 	ADDQ	$8, DI	// ELF wants to use -8(FS)
504 #endif
505 	MOVQ	DI, SI
506 	MOVQ	$0x1002, DI	// ARCH_SET_FS
507 	MOVQ	$158, AX	// arch_prctl
508 	SYSCALL
```

可以看到，这里调用了系统调用[`arch_prctl`](http://man7.org/linux/man-pages/man2/arch_prctl.2.html)，在linux下把`m0.tls+8`的地址保存到`fs`寄存器。到此，完成TLS的设置。
