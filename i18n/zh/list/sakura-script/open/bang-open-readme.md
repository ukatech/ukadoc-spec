# `\![open,readme]`

**カテゴリ:** 打开命令

打开readme.txt。<br />
如果未指定任何内容，则打开当前运行的 ghost 的 \[所执行的 ghost 文件夹\]/ghost/master/descript.txt 中指定为 readme 的文件。<br />
指定为 `\![open,readme,种类(ghost/shell/balloon/headline/plugin/calendar.skin/calendar.plugin),名称]` 时，会打开指定的 readme。示例：`\![open,readme,ghost,Emily/Phase4]`<br />
calendar.skin是日历皮肤，calendar.plugin是日历插件（计划传感器）。也支持使用空格分隔的「calendar skin」「calendar plugin」写法。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![open,readme]readme.txtを開く。
```
