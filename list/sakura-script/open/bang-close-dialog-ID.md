# `\![close,dialog,ID]`

**カテゴリ:** オープンコマンド

指定したイベントIDのダイアログを閉じる。全部の場合は\_\_SYSTEM_ALL_DIALOG\_\_を指定。

**対応:** SSP

## 記述例

```sakurascript
\![close,dialog,テストカラーダイアログ]現在表示されているダイアログのうち、idが「テストカラーダイアログ」のものを閉じる。ダイアログが閉じられた場合、OnSystemDialogCancelが通知される。
```
