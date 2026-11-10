# delete.txt

## 概要

也请参阅[文件结构「网络更新」](../../../manual/update.md)页面。

更新时，客户端（用户）的文件只会被服务器（作者）的文件覆盖，并不会进行同步。<br />
也就是说，已经下载到客户端或在客户端创建的文件，即使在服务器端删除，也无法将其移除。<br />
因此，发布后如果需要删除已发布的文件，必须在delete.txt中列出该文件。<br />
另外，delete.txt在执行删除后不会自动删除；除非修改内容，否则已列出的文件会一直被排除。

以下是仅适用于SSP的规范。

- **charset,(字符编码)**: 指定文件的字符编码

## 記述例

```
ghost\master\ai.dtx
ghost\master\testdict\
shell\master\surface110.png
```
