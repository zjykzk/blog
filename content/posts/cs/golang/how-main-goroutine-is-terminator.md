+++
author = "zenk"
tags = ["golang"]
draft = false
categories=["cs"]
title="为什么main函数是终结者"
description="为什么main函数退出以后不管是否有其他goroutine程序就直接退出了。"
date="2018-11-16T14:13:32+08:00"

+++

来一个`hello, world!`。

```
package main

func main() {
    println("hello, world!")
} // line 5
```

编译调试。

```
# go build -o debug_main main.go // 编译
# gdb debug_main                 // 开始调试
(gdb) b 5 // 在第5行打断点
(gdb) r   // 执行，这时代码停在第5行，还在main函数中，其实在二进制文件里面它符号是main_main
(gdb) s   // 单步往下走，进入runtime.main代码
runtime.main () at /home/zenk/tools/goroot/src/runtime/proc.go:207
207             if atomic.Load(&runningPanicDefers) != 0 {
(gdb) bt  // 查看调用栈
#0  runtime.main () at /home/zenk/tools/goroot/src/runtime/proc.go:207
#1  0x0000000000446891 in runtime.goexit () at /home/zenk/tools/goroot/src/runtime/asm_amd64.s:2361
#2  0x0000000000000000 in ?? ()
(gdb) s
216             if atomic.Load(&panicking) != 0 {
(gdb) s
220             exit(0)
(gdb) s
runtime.exit () at /home/zenk/tools/goroot/src/runtime/sys_linux_amd64.s:52
52              MOVL    code+0(FP), DI
```

从上面的结果可以知道，自己写的`main`函数被编译成`main_main`，然后被`runtime.main`所调用。通过查看`runtime.main`可以看到以下代码，说明它执行结束以后会调用`exit(0)`。

```
   // file: goroot/src/runtime/proc.go: main()
   220   exit(0)
   221   for {
   222     var x *int32
   223     *x = 0
   224   }
```

查看`exit`函数代码，它调用了系统调用`exit_group`，退出所有线程。

```
// file: goroot/src/runtime/sys_linux_amd64.s:52
 51 TEXT runtime·exit(SB),NOSPLIT,$0-4
 52     MOVL    code+0(FP), DI
 53     MOVL    $SYS_exit_group, AX
 54     SYSCALL
 55     RET
```

还有一个比较有意思的事情是当查看调用栈的时候，显示`runtime.main`是通过`runtime.goexit()`调用的。其实这是因为创建goroutine的时候会把`goexit`的地址加1这个值放到它的栈顶，这样goroutine的函数执行完毕就会接着执行`goexit`而`goexit`又会调用`schedule`这个函数，继续寻找goroutine并执行。

把`goexit`放到goroutine的栈顶代码：

```
// file: goroot/src/runtime/proc.go:newproc1(fn *funcval, argp *uint8, narg int32, callerpc uintptr)

3315   newg.sched.pc = funcPC(goexit) + sys.PCQuantum // +PCQuantum so that previous instruction is in same function
3316   newg.sched.g = guintptr(unsafe.Pointer(newg))
3317   gostartcallfn(&newg.sched, fn)
            |
            V
// file: goroot/src/runtime/stack.go:func gostartcallfn(gobuf *gobuf, fv *funcval) 
1085   gostartcall(gobuf, fn, unsafe.Pointer(fv))
            |
            V
// file: goroot/src/runtime/sys_x86.go:func gostartcall(buf *gobuf, fn, ctxt unsafe.Pointer)
22   sp -= sys.PtrSize
23   *(*uintptr)(unsafe.Pointer(sp)) = buf.pc // 这里的pc就是 funcPC(goexit) + sys.PCQuantum
```

再看`runtime.goexit`代码：

```
// file: goroot/src/runtime/asm_amd64.s
2360 TEXT runtime·goexit(SB),NOSPLIT,$0-0
2361     BYTE    $0x90   // NOP
2362     CALL    runtime·goexit1(SB) // does not return
2363     // traceback from goexit1 must hit code range of goexit
2364     BYTE    $0x90   // NOP
```

因为压入goroutine栈的值是`runtime.goexit+sys.PCQuantum(=1)`，因此goroutine函数返回的时候会执行第`2361`行代码。