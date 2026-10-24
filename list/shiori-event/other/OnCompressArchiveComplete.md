# OnCompressArchiveComplete

**カテゴリ:** その他イベント

アーカイブの圧縮が正常に完了した際に発生する。

[`\![execute,compressarchive]`](../../sakura-script/misc/bang-execute-compressarchive.md)にて--eventオプションで指定した識別子がOnではじまる場合、その識別子のイベントが発生する。それ以外の場合は本イベントが発生する。

- **Reference0**: Sakura Scriptの--eventオプションで指定されたイベント識別子。
- **Reference1**: 圧縮されたファイル数。
- **Reference2**: 圧縮サイズ（バイト）。
- **Reference3**: 非圧縮サイズ（バイト）。

**対応:** SSP 2.7.23
