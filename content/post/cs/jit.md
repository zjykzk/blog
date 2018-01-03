+++
author = "zenk"
slug = ""
tags = ["jit"]
draft = false
categories=["cs"]
title="jit的基本原理以及实现"
description="jit的基本原理以及hello,world实现"
date="2018-01-03T15:12:25+08:00"
+++

## 基本原理

JIT（Just-In-Time）是指程序运行的过程中生成可执行的代码。这里有两个工作：
1. 生成可以执行的代码
2. 执行代码

### 生成代码
生成的代码是平台相关，一般就是一些机器码。

### 执行代码
生成的代码如果要被执行，必须要确保代码所在的内存拥有可执行的标志。在linux下面通过`mmap`系统调用映射一块可执行的内存，然后把相关的代码复制到这块内存中。最后，把内存首地址转换成函数地址并进行调用。

## Hello，World

一个基于x86_64平台的JIT代码， 通过系统调用`write`实现打印`hello,world！`。

### 基于x86_64平台的JIT代码

linux下面系统调用通过软中断来实现，参数通过寄存器来传递。寄存器的使用情况如下：
```
+----------+--------+--------+--------+--------+--------+--------+
| Syscall #| Param 1| Param 2| Param 3| Param 4| Param 5| Param 6|
+----------+--------+--------+--------+--------+--------+--------+
| rax      |  rdi   |  rsi   |   rdx  |   r10  |   r8   |   r9   |
+----------+--------+--------+--------+--------+--------+--------+
```

系统调用[write(int fd, const void *buf, size_t count)](http://man7.org/linux/man-pages/man2/write.2.html)

* 参数`fd`:文件描述符号
* 参数`buf`:输出的内存起始地址
* 参数`count`:输出的字节数

因此，x86_64平台下调用`write`的机器码为
```
0:  48 c7 c0 01 00 00 00    mov    rax,0x1
7:  48 c7 c7 01 00 00 00    mov    rdi,0x1
e:  48 c7 c2 0c 00 00 00    mov    rdx,0xc
15: 48 8d 35 03 00 00 00    lea    rsi,[rip+0x4]        # 0x1f
1c: 0f 05                   syscall
1e: c3 cc                   ret
1f: 48 65 6c 6c 6f 20 57 6f 72 6c 64 21   // Hello World!
```

其中：
1. `rax`值为1，系统调用`write`的编号
2. `rdi`值为1，参数`fd`的值，标准输出
3. `rsi`值为`rip+4`，参数`buf`的值，通过相对地址得到
4. `rdx`值为0xc（12），参数`count`的值

### 执行代码

通过系统调用[void *mmap(void *addr, size_t length, int prot, int flags, int fd, off_t offset)](http://man7.org/linux/man-pages/man2/mmap.2.html)创建内存映射，确保这块内存可以执行，通过参数`prot`指定，其中`PROT_EXEC`可执行，`PROT_READ`可读，`PROD_WRITE`可写。

```
unsigned short code[] = {
    0x48c7, 0xc001, 0x0,          // mov %rax,$0x1
    0x48, 0xc7c7, 0x100, 0x0,     // mov %rdi,$0x1
    0x48c7, 0xc20c, 0x0,          // mov 0x12, %rdx
    0x48, 0x8d35, 0x400, 0x0,     // lea 0x4(%rip), %rsi
    0xf05,                        // syscall
    0xc3cc,                       // ret
    0x4865, 0x6c6c, 0x6f20,       // Hello_(whitespace)
    0x576f, 0x726c, 0x6421, 0xa,  // World!
};

#define PROTS PROT_READ|PROT_WRITE|PROT_EXEC
#define FLAGS MAP_PRIVATE|MAP_ANONYMOUS

void *m = mmap(NULL, sizeof(code), PROTS, FLAGS, -1, 0);
```

接下来，把机器码复制到刚刚映射的内存中，注意为了显示方便机器码保存在了`unsigned short`数组中，加上x86_64平台字节顺序按照小端来存储，需要把机器码字节顺序调换。
```
for (int i = 0; i < sizeof(code)/sizeof(code[0]); i++) {
    *((unsigned short *)m+i) = (unsigned short)(((code[i]>>8) | (code[i]<<8)) & 0xffff);
}
```

最后，调用一个没有参数以及没有返回值的函数：`void (*)()`
```
((void (*)())m)();
```

### 完整代码

```
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/types.h>
#define _GNU_SOURCE

int main(void) {
  unsigned short code[] = {
    0x48c7, 0xc001, 0x0,          // mov %rax,$0x1
    0x48, 0xc7c7, 0x100, 0x0,     // mov %rdi,$0x1
    0x48c7, 0xc20c, 0x0,          // mov 0x12, %rdx
    0x48, 0x8d35, 0x400, 0x0,     // lea 0x4(%rip), %rsi
    0xf05,                        // syscall
    0xc3cc,                       // ret
    0x4865, 0x6c6c, 0x6f20,       // Hello_(whitespace)
    0x576f, 0x726c, 0x6421, 0xa,  // World!
  };

#define PROTS PROT_READ|PROT_WRITE|PROT_EXEC
#define FLAGS MAP_PRIVATE|MAP_ANONYMOUS

  void *m = mmap(NULL, sizeof(code), PROTS, FLAGS, -1, 0);
  if (m == MAP_FAILED) {
      printf("mmap error");
      return -1;
  }

  for (int i = 0; i < sizeof(code)/sizeof(code[0]); i++) {
    *((unsigned short *)m+i) = (unsigned short)(((code[i]>>8) | (code[i]<<8)) & 0xffff);
  }

  ((void (*)())m)();
}
```

## 参考

https://medium.com/kokster/writing-a-jit-compiler-in-golang-964b61295f