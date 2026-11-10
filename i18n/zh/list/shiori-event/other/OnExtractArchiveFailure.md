# OnExtractArchiveFailure

**カテゴリ:** 其他事件

存档解压失败时触发。

在[`\![execute,extractarchive]`](../../sakura-script/misc/bang-execute-extractarchive.md)中，如果通过--event选项指定的标识符以On开头，则会触发名称为该标识符并附加“Failure”的事件。否则触发本事件。

- **Reference0**: Sakura Script的--event选项指定的事件标识符。
- **Reference1**: 错误内容。请参阅[※错误代码列表](caption_archive_error_codes.md)。

**対応:** SSP 2.7.23
