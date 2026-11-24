# `\![timerraiseother,時間,繰り返すか否か,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

Notifies another running ghost of an event after a specified delay in milliseconds.<br />
Set the repeat argument to 0 to raise the event repeatedly at the specified interval, or to 1 or greater to raise it only once.<br />
The sixth and subsequent arguments are references.<br />
Events with different names can run independently, but repeatedly executing this command for an event with the same name overwrites it.<br />
To cancel the event, execute Sakura Script with the same event name and a time of 0.<br />
Set the ghost name to \_\_SYSTEM_ALL_GHOST\_\_ to notify all running ghosts.<br />
Multiple ghost names can be specified, separated by byte value 1.<br />
\[SSP 2.9.35\] A running ghost's [UUID](../../propertysystem/property-system/general-property/uuid.md) can also be specified instead of its name, as with [raiseother](bang-raiseother-r0-r1-r2.md). The destination is determined each time the event is sent, not when the timer is set.

**対応:** SSP

## 記述例

```sakurascript
\![timerraiseother,30000,0,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5に30秒(30000ミリ秒)おきに繰り返しOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。\![timerraiseother,0,1,Emily/Phase4.5,OnRoastedPotate]ここで繰り返し通知をキャンセル。
```
