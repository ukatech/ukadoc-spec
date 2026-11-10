# `\![execute,compressarchive,ファイル名,ディレクトリ名,オプション...]`

**カテゴリ:** Uncategorized command

Compresses files into a ZIP archive. Using full paths is recommended. Relative paths are interpreted relative to ghost/master/.<br />
The available options are as follows.

- --event=イベント識別子……Specifying an event identifier allows compression to continue while Sakura Script execution proceeds. When compression finishes, an event is triggered. If the identifier begins with On, an event with that identifier is triggered; otherwise, OnCompressArchiveComplete or OnCompressArchiveFailure is triggered. If omitted, script execution pauses until processing is complete.
- --password=パスワード……Enables AES-encrypted ZIPs using the specified password.

See [OnCompressArchiveComplete](../../shiori-event/other/OnCompressArchiveComplete.md) and [OnCompressArchiveFailure](../../shiori-event/other/OnCompressArchiveFailure.md) for specifications on events triggered after processing.<br />
Specify a folder as the directory name. \[SSP 2.9.33\] If the path is not a folder (for example, it is a file path), compression fails without proceeding (if `--event=` is specified, `Reference1` of the failure event (OnCompressArchiveFailure, or the specified identifier with `Failure` appended) is set to `invalid parameter`).<br />
For security reasons, the destination for compression is restricted to locations under folders managed by SSP (such as the ghost and balloon folders, and locations specified by the “Folder” settings).<br />
This restriction may be tightened as appropriate, so it is safest to limit the destination to a location under the folder containing the ghost's own data.

**対応:** SSP options supported from 2.7.23

## 記述例

```sakurascript
\![execute,compressarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4]Cドライブ直下にSSPがインストールされている場合、Emily/Phase4.5のフォルダをtest.zipに圧縮してghostフォルダに置く。処理が完了するまでスクリプトの実行は停止する。
```

```sakurascript
\![execute,compressarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4,--event=OnCompressComplete]非同期で圧縮を実行し、完了時にOnCompressCompleteイベントが発生する。
```
