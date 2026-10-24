# OnPictureViewerOpen

**カテゴリ:** ファイルドロップイベント

ファイルがDnDされて、OnFileDrop2にゴーストが応答せず(または[`\![execute,dropdefault,file]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md)を実行して\[2.9.10\])、かつ画像ビューアーが開かれた際に発生。ReferenceはOnFileDrop2と同一。

- **Reference0**: ドロップされたファイルパス。複数ファイル/ディレクトリがあればbyte値1で区切る。
- **Reference1**: ドロップされたキャラクターのスコープ番号。本体側0、相方1、3人目以降は2以降。
- **Reference2**: ドロップされたファイルのMIMEタイプ。複数ファイル/ディレクトリがあればbyte値1で区切る。

**対応:** SSP 2.8.51
