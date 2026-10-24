# `\![execute,compressarchive,ファイル名,ディレクトリ名,オプション...]`

**カテゴリ:** 未分類コマンド

ZIPファイルの圧縮をする。指定はフルパスで行うことを推奨する。相対パス指定の場合はghost/master/以下の相対パスと解釈される。<br />
オプションは以下の通り。

- --event=イベント識別子……イベント識別子を指定すると、Sakura Scriptの続きを実行しながら圧縮を続け、終わり次第イベントが起きる。識別子がOnではじまる場合はその識別子のイベントが発生し、それ以外の場合はOnCompressArchiveCompleteまたはOnCompressArchiveFailureが発生する。省略時は処理が完了するまでスクリプトの実行は停止する。
- --password=パスワード……指定したパスワードを使用してAES暗号化ZIPを有効にする。

動作後のイベントに関する仕様は[OnCompressArchiveComplete](../../shiori-event/other/OnCompressArchiveComplete.md)・[OnCompressArchiveFailure](../../shiori-event/other/OnCompressArchiveFailure.md)を参照。<br />
セキュリティ上の観点から、圧縮先は、SSP管理下のフォルダ(ghostフォルダ、balloonフォルダなど「フォルダ」設定で指定した場所)以下への展開に制限される。<br />
また、この制限は適宜強化される可能性があるため、ゴースト自身のデータが置かれているフォルダ以下に限定するのが無難。

**対応:** SSP オプション指定は2.7.23以降

## 記述例

```sakurascript
\![execute,compressarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4]Cドライブ直下にSSPがインストールされている場合、Emily/Phase4.5のフォルダをtest.zipに圧縮してghostフォルダに置く。処理が完了するまでスクリプトの実行は停止する。
```

```sakurascript
\![execute,compressarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4,--event=OnCompressComplete]非同期で圧縮を実行し、完了時にOnCompressCompleteイベントが発生する。
```
