# `\![execute,compressarchive,ファイル名,ディレクトリ名,オプション...]`

**カテゴリ:** Uncategorized command

Compresses files into a ZIP archive. Using full paths is recommended. Relative paths are interpreted as relative to ghost/master/.<br />
The available options are as follows.

- --event=Event identifier……Specifying an event identifier continues executing the Sakura Script while compression proceeds, then raises the event when compression finishes. If the identifier starts with On, that event is raised; otherwise, OnCompressArchiveComplete or OnCompressArchiveFailure is raised. If omitted, script execution pauses until processing is complete.
- --password=Password……Enables AES-encrypted ZIP files using the specified password.

For specifications related to events raised after processing, see [OnCompressArchiveComplete](../../shiori-event/other/OnCompressArchiveComplete.md) and [OnCompressArchiveFailure](../../shiori-event/other/OnCompressArchiveFailure.md).<br />
Specify a folder for the directory name. \[SSP 2.9.33\] If it is not a folder (for example, if it is a file path), compression fails without creating an archive. (If `--event=` is specified, `Reference1` of the failure event (OnCompressArchiveFailure, or the specified identifier with `Failure` appended) is `invalid parameter`.)<br />
For security reasons, the destination is restricted to locations under folders managed by SSP (such as the ghost and balloon folders, and locations specified in the "Folder" settings).<br />
This restriction may be strengthened as needed, so it is safest to limit the destination to a folder under the one containing the ghost's own data.

**対応:** SSP. Option specification supported from 2.7.23

## 記述例

```sakurascript
\![execute,compressarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4]Cドライブ直下にSSPがインストールされている場合、Emily/Phase4.5のフォルダをtest.zipに圧縮してghostフォルダに置く。処理が完了するまでスクリプトの実行は停止する。
```

```sakurascript
\![execute,compressarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4,--event=OnCompressComplete]非同期で圧縮を実行し、完了時にOnCompressCompleteイベントが発生する。
```
