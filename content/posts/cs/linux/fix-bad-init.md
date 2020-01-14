+++
author = "zenk"
slug = ""
tags = ["linux"]
categories=["linux"]
title="initramfs中的init进程系统启动失败"
description="修复initramfs中的init进程系统启动失败日志"
date="2020-01-14T11:11:37+08:00"

+++

## 缘起

执行系统全量更新数据`yay -Syu`，更新了以下软件：

```
upgraded grub (2:2.04-4 -> 2:2.04-5)
upgraded libjpeg-turbo (2.0.3-1 -> 2.0.4-1)
upgraded imagemagick (7.0.9.10-1 -> 7.0.9.13-1)
upgraded libarchive (3.4.0-3 -> 3.4.1-1)
upgraded libmagick6 (6.9.10.80-1 -> 6.9.10.83-1)
upgraded linux (5.4.6.arch3-1 -> 5.4.7.arch1-1)
upgraded linux-headers (5.4.6.arch3-1 -> 5.4.7.arch1-1)
upgraded marisa (0.2.5-5 -> 0.2.5-7)
upgraded opencl-nvidia (440.44-1 -> 440.44-2)
upgraded openvpn (2.4.8-1 -> 2.4.8-3)
upgraded s-nail (14.9.15-3 -> 14.9.16-1)
```

系统重启，启动失败。显示：

```
[Firmware Bug]: TSC_DEADLINE disabled due to Errata; please update microcode to version: 0x22 (or later)
```

## 解决

google结果提示安装`intel-ucode`。烧个live cd进去执行命令`pacman -S intel-ucode`安装完毕，重启。失败，显示：

```
Failed to execute /init (error -2)
Console: switching to colour frame buffer device 175x65
.....
```

命令`/init`位于initramfs这个rootfs中。简单说来initramfs是启动系统过程中用于其他系统的中间过程。上面显示的问题原因是启动的时候失败了。

接着google，因为initramfs是gzip压缩的，可以通过命令`zcat /boot/initramfs-linux.img | cpio -i`解压initramfs系统。

解压以后通过命令`chroot . /bin/sh`测试能否进入这个rootfs。提示找不到命令`/bin/sh`。检查发现文件存在，然后确定是因为找不到依赖的动态连接库导致。

通过命令`/usr/lib/ld-linux-x86-64.so.2 --list /bin/sh`找到依赖，然后把依赖更新到文件`/etc/mkinitcpio.conf`的字段`FILES`中去，然后重新执行命令`mkinitcpio -p linux`生成initramfs文件，重启系统。通过上面的循环测试发现，其实还有其他命令依赖的动态链接库也缺失了。都拷贝过去以后搞定！

## 覆盘

系统更新以后不知道什么原因initramfs中缺失了很多动态连接库。最重要的是因为对initramfs系统不熟悉，导致没有地方下手，好在有google大法和archlinux的论坛，搞定。