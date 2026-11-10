# `\![open,readme]`

**カテゴリ:** Open command

Open readme.txt.<br />
If nothing is specified, the file specified as readme in the running ghost's \[folder of the ghost that ran the command\]/ghost/master/descript.txt is opened.<br />
Specify `\![open,readme,type(ghost/shell/balloon/headline/plugin/calendar.skin/calendar.plugin),name]` to open the specified readme. Example: `\![open,readme,ghost,Emily/Phase4]`<br />
calendar.skin is the calendar shell, and calendar.plugin is the calendar plugin (schedule sensor). The space-separated forms “calendar skin” and “calendar plugin” are also accepted.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![open,readme]readme.txtを開く。
```
