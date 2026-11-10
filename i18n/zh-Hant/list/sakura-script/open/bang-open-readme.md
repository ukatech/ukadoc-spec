# `\![open,readme]`

**カテゴリ:** 開啟命令

開啟 readme.txt。<br />
若未指定任何內容，會開啟目前執行中的 ghost 在\[執行中的 ghost 資料夾\]/ghost/master/descript.txt 的 readme 欄位中指定的檔案。<br />
指定為 `\![open,readme,種類(ghost/shell/balloon/headline/plugin/calendar.skin/calendar.plugin),名稱]` 時，會開啟指定的 readme。範例：`\![open,readme,ghost,Emily/Phase4]`<br />
calendar.skin 是行事曆 shell，calendar.plugin 是行事曆 plugin（排程感測器）。也接受以空格分隔的「calendar skin」和「calendar plugin」寫法。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![open,readme]readme.txtを開く。
```
