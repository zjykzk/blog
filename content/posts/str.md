+++
author = "zenk"
date = "2017-01-19T14:05:14+08:00"
description = "字符串与编码"
draft = true
keywords = ["string", ""]
tags = ["one", "two"]
title = "字符串"
topics = ["program"]
type = "post"

+++

# 为什么要字符串

# 字符串的表示

## 计算机中的字符串

## 编码

# python 中的字符串

## python 2

### 字符类型

### 重要方法

```py
# <type 'str'> to <type 'unicode'>
# 如果 s 是'unicode'类型，python会先通过encode函数把s转换成'str'类型，而encode函数的encoding是sys.getdefaultencoding()的值
s.decode(encoding)

# <type 'unicode'> to <type 'str'>
# 如果u是'str'类型，python会通过decode函数把u转换成'unicode'类型，而decode函数的encoding是sys.getdefaultencoding()的值
u.encode(encoding)

# 获取系统默认的编码
sys.getdefaultencoding()

# 修改系统的默认编码
sys.setdefaultencoding(encoding)

# 修改代码
import sys
reload(sys) # 因为python初始化的时候会把setdefaultencoding方法给删除掉
sys.setdefaultencoding('utf8')
```



## python 3

# go中的字符串

# java中的字符串