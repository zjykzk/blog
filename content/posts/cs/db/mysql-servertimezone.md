+++
author = "zenk"
slug = ""
tags = ["mysql","db"]
draft = false
categories=["cs"]
title="mysql连接中的serverTimezone参数解析"
description="解析mysql连接中的serverTimezone参数,说明查询和返回的时间类型结果怎么转换."
date="2020-02-12T10:41:51+08:00"

+++

在mysql连接的选项中参数`serverTimezone`用来指定服务器的时区.它的作用主要用于当我们传递时间类型的参数以及获取时间类型的数值时,转换成程序运行所在环境的时区所对应的时间.注意:如果传递字符串是没问题的,因为jdbc会把参数都转成字符串类型的sql传递到服务区上去.

如果不指定的情况下,会通过连接获取mysq服务器上面的时区.先获取变量`time_zone`值,如果是`SYSTEM`,就获取`system_time_zone`的值.参考代码:`com.mysql.cj.protocol.a.NativeProtocol.configureTimezone`.

因此,关于`system_time_zone`值的设置的目的是为了解决你写入和读取的时间值一致性.如果你是读别人写的数据,那么需要把它设置成写入的时候指定的时区.

