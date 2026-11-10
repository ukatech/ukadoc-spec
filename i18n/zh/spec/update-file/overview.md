# 概述

这是 ghost 更新系统（网络更新）使用的更新定义文件规范。<br />
更新定义文件记录了组成 ghost 的文件列表及其哈希值，baseware 从服务器获取该文件，与本地文件进行比较并执行差分更新。

当前有效的格式有以下2种。旧格式 updates.dau (Version 1) 已废止，因此省略。

- **updates2.dau (Version 2)**: 以字节值1分隔的偏二进制格式。
- **updates.txt (Version 3)**: 以字节值1分隔、但带有行前缀的文本格式。
