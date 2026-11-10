# `\![open,dialog,save,パラメータ]`

**カテゴリ:** 打开命令

打开文件保存对话框。在此对话框中执行保存，也不会实际保存任何内容。<br />
确认时会触发SHIORI事件[OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md)，并在reference0中存放“save”、在Reference2中存放文件路径，因此各ghost作者需要在此处编写并执行实际处理。<br />
关闭时会触发SHIORI事件[OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md)。<br />
[参数指定方法见下文](bang-open-dialog-color.note.md)，可以用逗号分隔指定多个参数。

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,save,--title=セーブダイアログ表示テスト,--dir=__system_mydocument__,--filter=テキストファイル|*.txt;*.dic,--ext=txt,--name=test,--id=テスト保存ダイアログ]マイドキュメントを初期位置として、.txtと.dicのファイルのみを表示し、初期ファイル名「test.txt」の保存ダイアログを開く。
```
