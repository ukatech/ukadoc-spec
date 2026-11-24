# `\![timerraiseplugin,時間,繰り返すか否か,プラグインのIDまたは名前,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

Sends a specified event to a plugin after a specified delay in milliseconds.<br />
Set the repeat argument to 0 to raise the event repeatedly at the specified interval, or to 1 or greater to raise it only once.<br />
Events with different names can run independently, but repeatedly executing this command for an event with the same name overwrites it.<br />
To cancel the event, execute Sakura Script with the same event name and a time of 0.<br />
\[SSP 2.9.35\] The plugin's [UUID](../../propertysystem/property-system/general-property/uuid.md) can also be specified, as with [raiseplugin](bang-raiseplugin-ID-r0-r1-r2.md). The destination is determined each time the event is sent, not when the timer is set.

**対応:** SSP

## 記述例

```sakurascript
\![timerraiseplugin,60000,0,実体化,OnMenuExec]プラグイン「実体化」を60秒(60000ミリ秒)おきに繰り返し実行。\![timerraiseplugin,0,0,実体化,OnMenuExec]ここで繰り返し実行をキャンセル。
```
