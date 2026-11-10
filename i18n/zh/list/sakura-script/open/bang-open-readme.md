# `\![open,readme]`

**カテゴリ:** Open command

Open readme.txt.<br />
If nothing is specified, open the file specified as readme in ghost/master/descript.txt in the folder of the currently running ghost.<br />
If you specify `\![open,readme,種類(ghost/shell/balloon/headline/plugin/calendar.skin/calendar.plugin),名前]`, the specified readme opens. Example: `\![open,readme,ghost,Emily/Phase4]`<br />
calendar.skin is a calendar shell, and calendar.plugin is a calendar plugin (schedule sensor). The space-separated forms "calendar skin" and "calendar plugin" are also accepted.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![open,readme]readme.txtを開く。
```
