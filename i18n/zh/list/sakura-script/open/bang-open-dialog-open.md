# `\![open,dialog,open,パラメータ]`

**カテゴリ:** 打开命令

打开文件选择对话框。在此对话框中选择文件，也不会实际打开文件。<br />
确认时会触发SHIORI事件[OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md)，并在reference0中存放“open”、在Reference2中存放文件路径，因此各ghost作者需要在此处编写并执行实际处理。<br />
关闭时会触发SHIORI事件[OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md)。<br />
[参数指定方法见下文](bang-open-dialog-color.note.md)，可以用逗号分隔指定多个参数。

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,open,--title=オープンダイアログ表示テスト,--dir=C:/SSP/ghost/emily4/ghost/master,--filter=辞書ファイル|dic*.txt;*.dic;*.aym;*.kis|全てのファイル|*.*,--id=テストダイアログ]SSPがCドライブ直下に、SSPという名前のフォルダで存在する場合、Emily/Phase4.5の[実行したゴーストのフォルダ]/ghost/masterを初期位置とし、dic～.txtと～.dicと～.aymと～.kisのファイルのみ表示する。
```
