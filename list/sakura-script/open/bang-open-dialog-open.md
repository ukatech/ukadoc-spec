# `\![open,dialog,open,パラメータ]`

**カテゴリ:** オープンコマンド

ファイルを開くのダイアログを開く。このダイアログでファイルを選択しても、実際にファイルが開かれるわけではない。<br />
決定時、SHIORIイベント[OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md)が発生し、reference0に「open」、Reference2にファイルパスが格納されているため、ここで実際の処理を各ゴースト作者が作成し実行させる。<br />
閉じるとSHIORIイベント[OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md)が発生する。<br />
[パラメータ指定は後述](notes_selectfile.md)をカンマ区切りで複数指定。

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,open,--title=オープンダイアログ表示テスト,--dir=C:/SSP/ghost/emily4/ghost/master,--filter=辞書ファイル|dic*.txt;*.dic;*.aym;*.kis|全てのファイル|*.*,--id=テストダイアログ]SSPがCドライブ直下に、SSPという名前のフォルダで存在する場合、Emily/Phase4.5の[実行したゴーストのフォルダ]/ghost/masterを初期位置とし、dic～.txtと～.dicと～.aymと～.kisのファイルのみ表示する。
```
