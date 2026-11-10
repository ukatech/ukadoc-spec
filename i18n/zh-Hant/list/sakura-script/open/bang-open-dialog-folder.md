# `\![open,dialog,folder,パラメータ]`

**カテゴリ:** Open commands

Opens a folder selection dialog. Selecting a folder in this dialog does not perform any action by itself.<br />
When confirmed, the SHIORI event [OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md) is triggered, with “folder” stored in reference0 and the folder path stored in Reference2. Each ghost author must implement and run the actual processing here.<br />
When the dialog is closed, the SHIORI event [OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md) is triggered.<br />
[Parameters described below](bang-open-dialog-color.note.md) can be specified as a comma-separated list.

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,folder,--title=フォルダ選択ダイアログ表示テスト,--id=OnTestFolderDialog]ダイアログで前回開いた場所を初期位置として、フォルダ選択ダイアログを開く。保存ボタンを押すと、指定したID名が「OnTestFolderDialog」でOnで始まっているため、同名のSHIORIイベントOnTestFolderDialogが通知される。
```
