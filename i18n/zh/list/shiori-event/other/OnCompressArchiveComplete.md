# OnCompressArchiveComplete

**カテゴリ:** 其他事件

压缩归档成功完成时触发。

使用 [`\![execute,compressarchive]`](../../sakura-script/misc/bang-execute-compressarchive.md)时，如果 --event 选项指定的标识符以 On 开头，则触发该标识符对应的事件。否则触发本事件。

- **Reference0**: Sakura Script 的 --event 选项指定的事件标识符。
- **Reference1**: 已压缩的文件数。
- **Reference2**: 压缩后大小（字节）。
- **Reference3**: 未压缩大小（字节）。

**対応:** SSP 2.7.23
