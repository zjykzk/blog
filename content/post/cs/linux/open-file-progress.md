+++
author = "zenk"
slug = ""
tags = ["linux"]
draft = false
categories=["cs"]
title="如何定位一个文件"
description="linux中怎么通过文件名找到具体的数据。"
date="2018-10-24T14:57:53+08:00"

+++

linux的VFS包含4个重要概念：
1. superblock，包含文件系统的信息，管理整个文件系统。
2. inode，索引文件（index node），代表一个文件，包含文件的元数据和数据，不包含文件名。
3. dentry，目录项，代表路径中的每个部分，包含文件路径到inode的映射。
4. file，文件，是文件在进程中的表示。

同时，在linux中一切兼文件，包括目录。目录的内容是文件名和inode号。

当打开一个文件`/bin/vim`，系统首先把路径分解成`/`、`bin`、`vim`，根据dentry查`vim`的inode，如果dentry还没有`bin`，会根据superblock中**根目录**的inode号得到它的子目录信息，其中就有`bin`和它的inode，并把它放到dentry中，然后根据`bin`的内容找到`vim`的inode。最终，返回一个文件描述符（file descriptor）。
