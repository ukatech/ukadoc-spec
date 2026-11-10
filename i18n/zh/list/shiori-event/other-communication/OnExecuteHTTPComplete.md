# OnExecuteHTTPComplete

**カテゴリ:** 其他通信事件

通过execute-http成功完成获取时触发。

- **Reference0**: post/get/head/put/delete之一
- **Reference1**: 通过--sync・--async选项指定的字符串。
- **Reference2**: 目标URL。
- **Reference3**: 如果指定了--nofile选项，则为获取的数据内容。但是换行符会被替换为字节值1。<br />
  否则为获取文件的完整路径。
- **Reference4**: 获取结果代码。（timeout|fileio|200|204|403|404）等。另请参阅[\[失败原因\]](../network-update/caption_updateresultfailure.md)。
- **Reference5**: Cookie字符串。
- **Reference6**: 接收到的所有响应头。以字节值1代替换行符进行分隔。 \[2.6.40\]

**対応:** SSP / Ninix
