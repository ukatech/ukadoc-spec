# OnCompressArchiveFailure

**カテゴリ:** その他イベント

アーカイブの圧縮が失敗した際に発生する。

[`\![execute,compressarchive]`](../../sakura-script/misc/bang-execute-compressarchive.md)にて--eventオプションで指定した識別子がOnではじまる場合、その識別子に「Failure」を付加したイベントが発生する。それ以外の場合は本イベントが発生する。

- **Reference0**: Sakura Scriptの--eventオプションで指定されたイベント識別子。
- **Reference1**: エラー内容。[※エラーコード一覧](caption_archive_error_codes.md)を参照。

**対応:** SSP 2.7.23
