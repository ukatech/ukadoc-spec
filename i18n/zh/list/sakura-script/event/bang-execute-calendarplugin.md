# `\![execute,calendarplugin,カレンダープラグイン名]`

**カテゴリ:** 事件命令

开始获取日历插件（schedule sensor）的日程。其效果与从日历菜单中选择插件相同。<br />
即使日历未显示，也会执行。<br />
将日历插件名称设为 random 时，会随机选择。<br />
设为 lastinstalled 时，会执行最后安装的日历插件。但如果 SSP 曾经退出，则此功能无效。<br />
如果没有对应的日历插件，则忽略此命令。<br />
日历插件名称通过[installedcalendarpluginname](../../shiori-event/notify/installedcalendarpluginname.md)通知。

**対応:** SSP 2.8.93
