# `\![timemachine,reset]`

**カテゴリ:** 未分類指令

將「虛擬變更目前時間」（時光機）的偏移量重設為 0，恢復實際時間。與 [`\![timemachine,set,0]`](bang-timemachine-set-value.md) 相同。<br />
僅在啟動 SSP 時指定 `--allow-timemachine-control` 才有效。未指定時不執行任何動作，並在錯誤日誌中記錄警告。無法從未獲授權的 SSTP（外部 SSTP）執行。

**対応:** SSP 2.9.39

## 記述例

```sakurascript
\![timemachine,reset]
```
