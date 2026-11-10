# `\![execute,extractarchive,ファイル名,ディレクトリ名,オプション...]`

**カテゴリ:** 未分類コマンド

解压 ZIP 文件。建议使用完整路径指定。使用相对路径时，会被解释为相对于 ghost/master/ 的路径。<br />
选项如下。

- --event=イベント識別子……指定事件标识符后，会在继续执行 Sakura Script 的同时继续解压，并在完成时触发事件。如果标识符以On开头，则触发该标识符对应的事件；否则触发OnExtractArchiveComplete或OnExtractArchiveFailure。省略时，脚本执行会暂停，直到处理完成。
- --password=パスワード……使用指定的密码解压，不会询问密码。

有关执行后的事件规范，请参阅[OnExtractArchiveComplete](../../shiori-event/other/OnExtractArchiveComplete.md)和[OnExtractArchiveFailure](../../shiori-event/other/OnExtractArchiveFailure.md)。<br />
出于安全考虑，解压目标限制在 SSP 管理的文件夹（ghost文件夹、balloon文件夹等由“文件夹”设置指定的位置）之下。<br />
此外，该限制可能会适时加强，因此最好将解压位置限制在存放 ghost 自身数据的文件夹之下。

**対応:** SSP 选项指定支持2.7.23及更高版本

## 記述例

```sakurascript
\![execute,extractarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4]Cドライブ直下にSSPがインストールされている場合、test.zipをemily4フォルダに解凍する。処理が完了するまでスクリプトの実行は停止する。
```

```sakurascript
\![execute,extractarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4,--event=OnExtractComplete]非同期で解凍を実行し、完了時にOnExtractCompleteイベントが発生する。
```
