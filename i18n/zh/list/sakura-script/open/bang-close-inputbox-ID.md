# `\![close,inputbox,ID]`

**カテゴリ:** 开放命令

关闭由 ID 指定的 InputBox（包括日期、时间、滑块和密码输入框）。要关闭全部 InputBox，请指定 \_\_SYSTEM_ALL_INPUT\_\_。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![close,inputbox,時間入力テスト]IDが「時間入力テスト」のInputBoxを閉じる。\![close,inputbox,__SYSTEM_ALL_INPUT__]その後、全てのInputBoxを閉じる。
```
