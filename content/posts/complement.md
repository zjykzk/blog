+++
author = "zenk"
date = "2017-05-30T23:18:02+08:00"
description = "complement representation of number"
draft = true
keywords = ["complement"]
tags = ["program"]
title = "complement"
topics = ["program"]
type = "post"

+++



# 补码

## 缘起

计算机中负数的表示

考虑2位数的减法，等价于：99 - 减数 + 被减数 + 1 - 100，这么做的好处避免了借位的情况，实现借位的逻辑电路比较复杂

99 - 减数 => 10 的反码

-100 表示取反



考虑 1 - 2 => 99 - 2 + 1 + 1 - 100 => 99 - 100 => -1

99 -> -1

