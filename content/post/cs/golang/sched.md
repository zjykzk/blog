+++
author = "zenk"
slug = ""
tags = ["golang"]
draft = true
categories=["cs"]
title=""
description="golang 1.8.1 goroutine 调度细节"
date="2017-08-08T15:50:01+08:00"
+++

# 程序启动

反编译二进制文件, `objdump -f file` 获取程序路口，入口函数为

 `_rt0_amd64_linux` (runtime/rt0_linux_amd64.s) -> `main` (runtime/rt0_linux_amd64.s) -> `runtime.rt0_go` (runtime/asm_amd64.s)



1. 获取CPU信息
2. 初始化cgo
3. 设置tls的值为g0的地址
4. osinit
5. schedinit
6. newproc -> 运行main(runtime/proc.go)函数
7. mstart