# OnExtractArchiveComplete

**カテゴリ:** その他イベント

アーカイブの解凍が正常に完了した際に発生する。

[`\![execute,extractarchive]`](../../sakura-script/misc/bang-execute-extractarchive.md)にて--eventオプションで指定した識別子がOnではじまる場合、その識別子のイベントが発生する。それ以外の場合は本イベントが発生する。

- **Reference0**: Sakura Scriptの--eventオプションで指定されたイベント識別子。
- **Reference1**: 解凍されたファイル数。
- **Reference2**: 圧縮サイズ（バイト）。
- **Reference3**: 非圧縮サイズ（バイト）。

**対応:** SSP 2.7.23
