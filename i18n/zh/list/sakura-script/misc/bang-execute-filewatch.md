# `\![execute,filewatch,パス,オプション...]`

**カテゴリ:** 未分類コマンド

开始监视指定的文件或目录，每次发生变化时通过[OnExecuteFileWatchChange](../../shiori-event/other-communication/OnExecuteFileWatchChange.md)通知。如果无法开始监视，或监视期间目标目录消失，则通过[OnExecuteFileWatchFailure](../../shiori-event/other-communication/OnExecuteFileWatchFailure.md)通知，并结束该监视。不能在从外部（例如 SSTP）发送的脚本中执行。<br />
参数如下。

- 路径……要监视的文件或目录。使用相对路径时，会被解释为相对于 ghost/master/ 的路径。
- --async=事件或标识符……指定以On开头的字符串时，会触发该事件（而非后述的事件）
- --debounce=毫秒……停止收到变化通知后，等待指定的时间；如果期间没有新的变化，则发送通知。只要变化持续发生，就会一直等待，因此写入期间连续发生的变化会合并为一次通知。但即使变化没有停止，从首次变化开始经过指定时间的3倍后也会发送通知。省略时为500。指定0时不等待，立即发送通知。

指定文件时，会通知更新、创建和删除。也可以指定尚不存在的文件；文件创建后会收到通知。但用于存放该文件的目录必须存在。<br />
指定目录时，只会通知其直接子级中的文件或目录发生创建、删除、重命名或更新。不会通知发生变化的文件，也不会通知子目录中的变化。要将目录作为监视目标，该目录必须在执行时存在（不存在的路径会作为文件进行监视）。<br />
再次指定相同路径时，之前的指定会被替换。ghost 结束时会解除所有监视。

**対応:** SSP 2.8.91

## 記述例

```sakurascript
\![execute,filewatch,config.json,--async=OnConfigChanged]ghost/master/config.jsonが変化するたびに、OnConfigChangedイベントが起きる。
```
