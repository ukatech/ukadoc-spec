# `\![open,readme]`

**カテゴリ:** Open command

Open readme.txt.<br />
If nothing is specified, the file specified as the readme in \[the folder of the ghost that executed this\]/ghost/master/descript.txt of the running ghost is opened.<br />
`\![open,readme,種類(ghost/shell/balloon/headline/plugin/calendar.skin/calendar.plugin),名前]` と指定すると、指定したreadmeが開く。例：`\![open,readme,ghost,Emily/Phase4]`<br />
calendar.skin is a calendar shell, and calendar.plugin is a calendar plugin (schedule sensor). The space-separated forms "calendar skin" and "calendar plugin" are also accepted.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![open,readme]readme.txtを開く。
```
