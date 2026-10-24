# `\![open,dialog,folder,パラメータ]`

**カテゴリ:** オープンコマンド

フォルダ選択のダイアログを開く。このダイアログで選択しても、実際に何かが行われるわけではない。<br />
決定時、SHIORIイベント[OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md)が発生し、reference0に「folder」、Reference2にフォルダパスが格納されているため、ここで実際の処理を各ゴースト作者が作成し実行させる。<br />
閉じるとSHIORIイベント[OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md)が発生する。<br />
[パラメータ指定は後述](notes_selectfile.md)をカンマ区切りで複数指定。

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,folder,--title=フォルダ選択ダイアログ表示テスト,--id=OnTestFolderDialog]ダイアログで前回開いた場所を初期位置として、フォルダ選択ダイアログを開く。保存ボタンを押すと、指定したID名が「OnTestFolderDialog」でOnで始まっているため、同名のSHIORIイベントOnTestFolderDialogが通知される。
```
