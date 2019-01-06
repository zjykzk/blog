+++
author = "zenk"
slug = ""
tags = ["performance"]
draft = true
categories=["cs"]
title="常见性能诊断工具"
description="常见性能诊断工具。"
date="2019-01-06T17:49:18+08:00"

+++

## dstat

检查Cpu、内存、磁盘、网路情况。

说明：

```
-c：显示CPU系统占用，用户占用，空闲，等待，中断，软件中断等信息。
-C：当有多个CPU时候，此参数可按需分别显示cpu状态，例：-C 0,1 是显示cpu0和cpu1的信息。 
-d：显示磁盘读写数据大小。 -D hda,total：include hda and total。 
-n：显示网络状态。 -N eth1,total：有多块网卡时，指定要显示的网卡。 
-l：显示系统负载情况。 
-m：显示内存使用情况。 
-g：显示页面使用情况。 
-p：显示进程状态。 
-s：显示交换分区使用情况。 
-S：类似D/N。 
-r：I/O请求情况。 
-y：系统状态。 
--ipc：显示ipc消息队列，信号等信息。 
--socket：用来显示tcp udp端口状态。 
-a：此为默认选项，等同于-cdngy。 
-v：等同于 -pmgdsc -D total。 
--output 文件：此选项也比较有用，可以把状态信息以csv的格式重定向到指定的文件中，以便日后查看。例：dstat --output /root/dstat.csv & 此时让程序默默的在后台运行并把结果输出到/root/dstat.csv文件中。    
```

例子：

```
dstat -lcdngy
```

## pidstat

监控进程的上下文切换，CPU利用率，内存使用，缺页，磁盘IO等情况。它是sysstat工具的一个命令。

说明：

```
-d IO的统计。
-p 指定具体的进程号，ALL表示显示所有进程。
-r 缺页错误和内存使用情况。
-u CPU的利用率，这个是默认的。
-w 上下文切换。
-t 显示线程的统计。
-T {TASK|ALL|CHILD}，TASK只统计每个任务占用的CPU情况，是默认值，CHILD只统计全局的平均值，ALL包括TASK和CHILD的功能。
```

例子：

```
pidstat -p 1 -d 2 5 // 显示1号进程的IO使用情况，每2秒打印一次，统计5次
06:53:20 PM   UID       PID   kB_rd/s   kB_wr/s kB_ccwr/s  Command
06:53:22 PM     0         1      0.00      0.00      0.00  systemd
06:53:24 PM     0         1      0.00      0.00      0.00  systemd
06:53:26 PM     0         1      0.00      0.00      0.00  systemd
06:53:28 PM     0         1      0.00      0.00      0.00  systemd
06:53:30 PM     0         1      0.00      0.00      0.00  systemd
Average:        0         1      0.00      0.00      0.00  systemd
```

## mpstat

监控CPU的使用率。

说明：

```
-P { cpu [,...] | ON | ALL }指定CPU，从0开始。ON表示只统计工作的CPU，ALL表示统计所有CPU。
-u 打印使用率，默认。
```

例子：

```
mpstat 1 2 // 每隔1秒，统计2次
```

