# `\![execute,extractarchive,ファイル名,ディレクトリ名,オプション...]`

**カテゴリ:** Uncategorized command

Extracts a ZIP file. Using full paths is recommended. Relative paths are interpreted as paths relative to ghost/master/.<br />
The options are as follows.

- --event=イベント識別子……When an event identifier is specified, extraction continues while Sakura Script execution proceeds, and the event is triggered when extraction is complete. If the identifier starts with On, the event with that identifier is triggered; otherwise, OnExtractArchiveComplete or OnExtractArchiveFailure is triggered. If omitted, script execution stops until processing is complete.
- --password=パスワード……Extracts without prompting for a password, using the specified password.

For specifications concerning events after execution, see [OnExtractArchiveComplete](../../shiori-event/other/OnExtractArchiveComplete.md) and [OnExtractArchiveFailure](../../shiori-event/other/OnExtractArchiveFailure.md).<br />
For security reasons, the extraction destination is restricted to locations under folders managed by SSP (such as the ghost and balloon folders and locations specified by the "Folders" setting).<br />
Also, since this restriction may be strengthened as needed, it is safest to limit the destination to a location under the folder containing the ghost's own data.

**対応:** SSP option specification supported from 2.7.23 onward

## 記述例

```sakurascript
\![execute,extractarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4]Cドライブ直下にSSPがインストールされている場合、test.zipをemily4フォルダに解凍する。処理が完了するまでスクリプトの実行は停止する。
```

```sakurascript
\![execute,extractarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4,--event=OnExtractComplete]非同期で解凍を実行し、完了時にOnExtractCompleteイベントが発生する。
```
