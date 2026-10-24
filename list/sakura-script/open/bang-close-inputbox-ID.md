# `\![close,inputbox,ID]`

**カテゴリ:** オープンコマンド

IDで指定されたInputBox(日付、時間、スライダー、入力非表示ボックスも含む)を閉じる。全部閉じたい場合は、\_\_SYSTEM_ALL_INPUT\_\_を指定する。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![close,inputbox,時間入力テスト]IDが「時間入力テスト」のInputBoxを閉じる。\![close,inputbox,__SYSTEM_ALL_INPUT__]その後、全てのInputBoxを閉じる。
```
