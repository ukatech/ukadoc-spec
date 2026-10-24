# `\![open,readme]`

**カテゴリ:** オープンコマンド

readme.txtを開く。<br />
何も指定しな場合、起動中ゴーストの、\[実行したゴーストのフォルダ\]/ghost/master/descript.txtのreadmeに指定してあるファイルが開く。<br />
`\![open,readme,種類(ghost/shell/balloon/headline/plugin/calendar.skin/calendar.plugin),名前]` と指定すると、指定したreadmeが開く。例：`\![open,readme,ghost,Emily/Phase4]`<br />
calendar.skinはカレンダースキン、calendar.pluginはカレンダープラグイン（スケジュールセンサ）。「calendar skin」「calendar plugin」のスペース区切り表記も受け付ける。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![open,readme]readme.txtを開く。
```
