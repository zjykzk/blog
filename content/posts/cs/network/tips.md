+++
author = "zenk"
slug = ""
tags = ["network"]
draft = true
categories=["cs"]
title="网络相关的一个技巧"
description="网络相关的一个技巧"
date="2019-04-23T12:04:21+08:00"

+++

### 查看端口是否被使用

```
netstat -anp | grep port-value

ss -anp | grep port-value
```