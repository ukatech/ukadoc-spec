# `\![timerraiseplugin,時間,繰り返すか否か,プラグインのIDまたは名前,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件命令

指定等待时间（毫秒），向plugin发送指定事件。<br />
“是否重复”为0时，每隔指定时间重复触发事件；为1以上时，只触发一次事件。<br />
不同名称的事件可以分别执行，但对同名事件重复执行时会覆盖之前的设置。<br />
执行事件名相同且时间为0的Sakura Script即可取消。<br />
\[SSP 2.9.35\] 也可以指定plugin的[UUID](../../propertysystem/property-system/general-property/uuid.md)（与[raiseplugin](bang-raiseplugin-ID-r0-r1-r2.md)相同）。目标不是在设置定时器时查找，而是在每次发送事件时查找。

**対応:** SSP

## 記述例

```sakurascript
\![timerraiseplugin,60000,0,実体化,OnMenuExec]プラグイン「実体化」を60秒(60000ミリ秒)おきに繰り返し実行。\![timerraiseplugin,0,0,実体化,OnMenuExec]ここで繰り返し実行をキャンセル。
```
