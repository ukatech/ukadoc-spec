# OnExecuteFileWatchFailure

**カテゴリ:** 其他通信事件

通过[`\![execute,filewatch]`](../../sakura-script/misc/bang-execute-filewatch.md)执行失败或无法继续监视时触发。在这种情况下，该监视会被解除。

使用--async指定以On开头的ID时，事件名为该ID后附加Failure。

- **Reference0**: --async指定的字符串本身（未指定时为空）
- **Reference1**: 指定路径的字符串本身
- **Reference2**: 失败原因<br />
  notauthorized：尝试通过SSTP等外部发送的脚本进行监视<br />
  invalid：未指定路径<br />
  notfound：监视目标目录（若目标是文件，则为存放该文件的目录）不存在、无法开始监视，或在监视期间消失<br />
  limit：SSP整体监视的目录种类超过上限（63）

**対応:** SSP 2.8.91
