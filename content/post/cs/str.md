+++
author = "zenk"
date = "2017-01-19T14:05:14+08:00"
description = "字符串与编码"
draft = false
keywords = ["string", "go","python"]
tags = [ "编程"]
title = "字符串"
type = "post"
categories = ["cs"]

+++

# 为什么要字符

人类发明了文字，同时想用计算机来处理文字。由此，就产生了字符。每个字符代码一个文字的图形。

# 字符串的表示

在计算机内部，只有01的信息。因此，为了能让计算机能够认识字符串，每个字符就的被映射成01数据。这个映射功能就叫编码。

## ASCII

   ASCII是美国19世纪60年代发明的一种编码，总共规定了128个字符，每个字符有1个字节大小。范围从0-127，比如`A`的编码是`01000001`

## Unicode

世界语言文字异常丰富，每个国家都有自己独特的语言文字。ASCII的编码无法编码所有的文字，因此产生了很多编码，比如中文的BIG5，GB2312等等。这些编码无法兼容，比如`中`在GB2312编码是`1101011011010000`，BIG5的编码是`1010010010100100`。因此，Unicode就出现了。Unicode规定了每个字符的唯一编号，目前已经有100多万个字符。需要注意的是Unicode只规定了字符的编号，没有规定二进制的表示。

## Utf8编码

utf8是Ken Thompson于1992年创建，现在已经标准化为RFC 3629。是目前使用最为广泛的unicode编码方式，其他的有utf-16，utf-32。它的特点是变长的，使用1-4个字节表示一个字符，不同的符号有不同的长度。

utf8编码规则：

      1. 一个字节的编码，最高位为0，其他的位表示unicode编号
      2. n个字节的编码（n>1），第一个字节的n位都是1，第n+1位是0，后面的每个字节的最高两位都是10，其余的位用来表示unicode编号

   下表表示了utf8的编码，z表示用于编码的bit

| unicode范围                       | utf8编码                              |
| :------------------------------ | :---------------------------------- |
| 十六进制表示                          | 二进制表示                               |
| 000000 - 00007F                 | 0zzzzzzz                            |
| 000080 - 0007FF                 | 110zzzzz 10zzzzzz                   |
| 000800 - 00D7FF/00E000 - 00FFFF | 1110zzzz 10zzzzzz 10zzzzzz          |
| 010000 - 10FFFF                 | 11110zzz 10zzzzzz 10zzzzzz 10zzzzzz |


# 环境中的编码

一个程序读取字符的输入的时候，读取的是二进制的数据。如果程序需要理解这个字符串是什么意思，必须了解字符的编码。同理，程序输出字符串的时候必须告知字符串的编码，不然使用者就无法理解程序的输出。程序中遇到乱码的问题，都是因为一个程序输出的字符串的编码和另一个程序接受字符串时使用的编码不一致导致的。因此，在解决编码的问题的思路就是搞清楚涉及到了哪几个环境。

比如：一个程序打印一个字符串到终端。程序的编码是utf8，终端显示的编码是gbk。这样就会造成乱码。

# 不同语言的字符串的支持

## python 中的字符串

### python 2

#### 字符类型

分为byte字符串(str)和unicode(unicode)，前者的内容是字节，后者的内容是unicode中的编号。默认的是byte字符串。

#### 重要方法

```python
# <type 'str'> to <type 'unicode'>
# 如果 s 是'unicode'类型，python会先通过encode函数把s转换成'str'类型
# encode函数的encoding是sys.getdefaultencoding()的值
s.decode(encoding)

# <type 'unicode'> to <type 'str'>
# 如果u是'str'类型，python会通过decode函数把u转换成'unicode'类型
# decode函数的encoding是sys.getdefaultencoding()的值
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

#### codecs

指定encoding参数生成file-object-like对象，利用：

1. 函数 `read` 读取byte字符串，按照encoding的编码返回unicode
2. `write` 输入unicode，按照encoding的编码转换成byte字符串写入文件

### python 3

显然，python2中的字符串处理方式会变得复杂，因此在python3中字符串统一都是unicode。

## go中的字符串

go中有两种类型支持字符串分别是：`string` 和 `rune` 。

1. string表示字节slice（分片）
2. rune表示unicode的编码（code point）

go对utf8有天然的支持。go的源代码是utf8编码，`for ... range` 循环字符串的时候也是按照utf8编码来处理每个字符，而不是字节。
