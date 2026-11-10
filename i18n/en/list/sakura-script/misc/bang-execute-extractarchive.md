# `\![execute,extractarchive,ファイル名,ディレクトリ名,オプション...]`

**カテゴリ:** Uncategorized command

Extract a ZIP file. Using full paths is recommended. Relative paths are interpreted as relative to ghost/master/.<br />
The options are as follows.

- --event=イベント識別子……If an event identifier is specified, extraction continues while the rest of the Sakura Script runs, and the event is raised when extraction is complete. If the identifier begins with On, that event is raised; otherwise, OnExtractArchiveComplete or OnExtractArchiveFailure is raised. If omitted, script execution stops until processing is complete.
- --password=パスワード……Extract using the specified password without prompting for one.

For details on events raised after execution, see [OnExtractArchiveComplete](../../shiori-event/other/OnExtractArchiveComplete.md) and [OnExtractArchiveFailure](../../shiori-event/other/OnExtractArchiveFailure.md).<br />
For security reasons, extraction is restricted to locations under folders managed by SSP (such as the ghost and balloon folders, specified in the "Folders" settings).<br />
Since this restriction may be strengthened as needed, it is safest to limit extraction to locations under the folder containing the ghost's own data.

**対応:** SSP Option specification supported from 2.7.23

## 記述例

```sakurascript
\![execute,extractarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4]Cドライブ直下にSSPがインストールされている場合、test.zipをemily4フォルダに解凍する。処理が完了するまでスクリプトの実行は停止する。
```

```sakurascript
\![execute,extractarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4,--event=OnExtractComplete]非同期で解凍を実行し、完了時にOnExtractCompleteイベントが発生する。
```
