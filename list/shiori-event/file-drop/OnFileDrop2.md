# OnFileDrop2

**カテゴリ:** ファイルドロップイベント

ファイルがDnDされた際に発生。このイベントが現時点での最新仕様となる。<br />
このイベントに応答すると、本体の既定の処理(画像ビューアー・メディアプレーヤー・アーカイブビューアーで開く)は行われない。応答したうえで既定の処理も行わせたい場合は、[`\![execute,dropdefault,file]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md)を使う。\[2.9.10\]

- **Reference0**: ドロップされたファイルパス。複数ファイル/ディレクトリがあればbyte値1で区切る。
- **Reference1**: ドロップされたキャラクターのスコープ番号。本体側0、相方1、3人目以降は2以降。
- **Reference2**: ドロップされたファイルのMIMEタイプ(SSP 2.7.98以降)。複数ファイル/ディレクトリがあればbyte値1で区切る。

**対応:** Materia / SSP / CROW / Ninix
