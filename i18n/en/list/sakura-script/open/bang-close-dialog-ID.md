# `\![close,dialog,ID]`

**カテゴリ:** Open command

Close the dialog with the specified event ID. To close all dialogs, specify \_\_SYSTEM_ALL_DIALOG\_\_.

**対応:** SSP

## 記述例

```sakurascript
\![close,dialog,テストカラーダイアログ]現在表示されているダイアログのうち、idが「テストカラーダイアログ」のものを閉じる。ダイアログが閉じられた場合、OnSystemDialogCancelが通知される。
```
