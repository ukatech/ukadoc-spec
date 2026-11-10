# `\![open,dialog,folder,パラメータ]`

**カテゴリ:** 打开命令

打开选择文件夹对话框。即使在此对话框中选择了文件夹，也不会实际执行任何操作。<br />
确认时会触发SHIORI事件[OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md)，并在reference0中存放“folder”、在Reference2中存放文件夹路径，因此各ghost作者需要在此处编写并执行实际处理。<br />
关闭时会触发SHIORI事件[OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md)。<br />
[参数指定方法见下文](bang-open-dialog-color.note.md)，可以用逗号分隔指定多个参数。

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,folder,--title=フォルダ選択ダイアログ表示テスト,--id=OnTestFolderDialog]ダイアログで前回開いた場所を初期位置として、フォルダ選択ダイアログを開く。保存ボタンを押すと、指定したID名が「OnTestFolderDialog」でOnで始まっているため、同名のSHIORIイベントOnTestFolderDialogが通知される。
```
