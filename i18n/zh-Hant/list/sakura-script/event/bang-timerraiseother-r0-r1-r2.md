# `\![timerraiseother,時間,繰り返すか否か,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

Notify another running ghost of an event after the specified wait time (in milliseconds).<br />
For 「繰り返すか否か」, specify 0 to trigger the event repeatedly at the specified interval, or 1 or greater to trigger it only once.<br />
The sixth and subsequent arguments are references.<br />
Events with different names can each be executed, but repeated execution of an event with the same name overwrites the previous one.<br />
To cancel, execute Sakura Script with the same event name and a time of 0.<br />
Set the ghost name to \_\_SYSTEM_ALL_GHOST\_\_ to notify all running ghosts.<br />
Multiple ghost names can be specified, separated by byte value 1.

**対応:** SSP

## 記述例

```sakurascript
\![timerraiseother,30000,0,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5に30秒(30000ミリ秒)おきに繰り返しOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。\![timerraiseother,0,1,Emily/Phase4.5,OnRoastedPotate]ここで繰り返し通知をキャンセル。
```
