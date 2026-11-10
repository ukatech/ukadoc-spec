# `\![close,dialog,ID]`

**カテゴリ:** 开放命令

关闭指定事件 ID 的对话框。要关闭全部对话框，请指定\_\_SYSTEM_ALL_DIALOG\_\_。

**対応:** SSP

## 記述例

```sakurascript
\![close,dialog,テストカラーダイアログ]現在表示されているダイアログのうち、idが「テストカラーダイアログ」のものを閉じる。ダイアログが閉じられた場合、OnSystemDialogCancelが通知される。
```
