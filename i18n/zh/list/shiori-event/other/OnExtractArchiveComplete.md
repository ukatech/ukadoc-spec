# OnExtractArchiveComplete

**カテゴリ:** 其他事件

存档解压成功完成时触发。

在[`\![execute,extractarchive]`](../../sakura-script/misc/bang-execute-extractarchive.md)中，如果通过--event选项指定的标识符以On开头，则会触发名称与该标识符相同的事件。否则触发本事件。

- **Reference0**: Sakura Script的--event选项指定的事件标识符。
- **Reference1**: 解压出的文件数。
- **Reference2**: 压缩大小（字节）。
- **Reference3**: 未压缩大小（字节）。

**対応:** SSP 2.7.23
