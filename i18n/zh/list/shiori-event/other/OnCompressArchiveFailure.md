# OnCompressArchiveFailure

**カテゴリ:** 其他事件

压缩归档失败时触发。

使用 [`\![execute,compressarchive]`](../../sakura-script/misc/bang-execute-compressarchive.md)时，如果 --event 选项指定的标识符以 On 开头，则触发在该标识符后添加「Failure」的事件。否则触发本事件。

- **Reference0**: Sakura Script 的 --event 选项指定的事件标识符。
- **Reference1**: 错误内容。请参阅[※错误代码列表](caption_archive_error_codes.md)。

**対応:** SSP 2.7.23
