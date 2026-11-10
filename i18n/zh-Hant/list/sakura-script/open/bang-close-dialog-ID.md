# `\![close,dialog,ID]`

**カテゴリ:** 開啟命令

關閉指定事件 ID 的對話方塊。若要關閉全部，請指定 \_\_SYSTEM_ALL_DIALOG\_\_。

**対応:** SSP

## 記述例

```sakurascript
\![close,dialog,テストカラーダイアログ]現在表示されているダイアログのうち、idが「テストカラーダイアログ」のものを閉じる。ダイアログが閉じられた場合、OnSystemDialogCancelが通知される。
```
