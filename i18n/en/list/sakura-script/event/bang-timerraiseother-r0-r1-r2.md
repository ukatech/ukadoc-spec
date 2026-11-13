# `\![timerraiseother,時間,繰り返すか否か,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

Notifies other running ghosts of an event after a specified delay in milliseconds.<br />
For "whether to repeat", 0 causes the event to recur at the specified interval, while 1 or greater causes it to occur only once.<br />
The sixth and subsequent arguments are references.<br />
Events with different names can be scheduled independently, but repeatedly scheduling an event with the same name overwrites the previous schedule.<br />
Running Sakura Script with the same event name and a time of 0 cancels the schedule.<br />
If the ghost name is \_\_SYSTEM_ALL_GHOST\_\_, all running ghosts are notified.<br />
Multiple ghost names can be specified, separated by byte value 1.<br />
\[SSP 2.9.35\] The [UUID](../../propertysystem/property-system/general-property/uuid.md) of a running ghost can also be specified instead of its name (as with [raiseother](bang-raiseother-r0-r1-r2.md)). The destination is resolved each time the event is sent, not when the timer is set.

**対応:** SSP

## 記述例

```sakurascript
\![timerraiseother,30000,0,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5に30秒(30000ミリ秒)おきに繰り返しOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。\![timerraiseother,0,1,Emily/Phase4.5,OnRoastedPotate]ここで繰り返し通知をキャンセル。
```
