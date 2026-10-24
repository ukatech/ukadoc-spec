# `\![open,dialog,save,パラメータ]`

**カテゴリ:** オープンコマンド

ファイルの保存のダイアログを開く。このダイアログで保存を行っても、実際に何かが保存されるわけではない。<br />
決定時、SHIORIイベント[OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md)が発生し、reference0に「save」、Reference2にファイルパスが格納されているため、ここで実際の処理を各ゴースト作者が作成し実行させる。<br />
閉じるとSHIORIイベント[OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md)が発生する。<br />
[パラメータ指定は後述](notes_selectfile.md)をカンマ区切りで複数指定。

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,save,--title=セーブダイアログ表示テスト,--dir=__system_mydocument__,--filter=テキストファイル|*.txt;*.dic,--ext=txt,--name=test,--id=テスト保存ダイアログ]マイドキュメントを初期位置として、.txtと.dicのファイルのみを表示し、初期ファイル名「test.txt」の保存ダイアログを開く。
```
