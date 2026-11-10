# OnExecuteFileWatchChange

**カテゴリ:** 其他通信事件

通过[`\![execute,filewatch]`](../../sakura-script/misc/bang-execute-filewatch.md)监视的文件或目录发生变化时触发。

使用--async指定以On开头的ID时，该ID将成为事件名。

由于文件可能会在短时间内被多次写入，因此变更停止后，会等待--debounce指定的时间（省略时为500毫秒），然后合并为一次触发。如果写入间隔更长，或者变更持续未停止且从首次变更起经过了指定时间的3倍，则一次保存可能会触发多次。

- **Reference0**: --async指定的字符串本身（未指定时为空）
- **Reference1**: 指定路径的字符串本身
- **Reference2**: 变更类型<br />
  文件：modified（更新）、created（创建）、deleted（删除）<br />
  目录：changed（其直接子项发生创建、删除、重命名或更新之一）、deleted（目录本身已不存在）
- **Reference3**: 正在监视的文件或目录的完整路径

**対応:** SSP 2.8.91
