# `\![timerraiseother,時間,繰り返すか否か,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件命令

指定等待时间（毫秒），向正在运行的其他 ghost 通知事件。<br />
“是否重复”为0时，每隔指定时间重复触发事件；为1以上时，仅触发一次事件。<br />
第6个及之后的参数为 reference。<br />
不同名称的事件可以分别执行，但对同名事件重复执行时会覆盖原有设置。<br />
执行事件名相同且时间为0的 Sakura Script 即可取消。<br />
将 ghost 名称设为\_\_SYSTEM_ALL_GHOST\_\_时，向所有正在运行的 ghost 发送通知。<br />
可以用字节值1分隔，指定多个 ghost 名称。<br />
\[SSP 2.9.35\] 也可以指定正在运行的 ghost 的 [UUID](../../propertysystem/property-system/general-property/uuid.md) 代替 ghost 名称（与 [raiseother](bang-raiseother-r0-r1-r2.md) 相同）。接收对象在每次通知事件时确定，而不是在设置计时器时确定。

**対応:** SSP

## 記述例

```sakurascript
\![timerraiseother,30000,0,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5に30秒(30000ミリ秒)おきに繰り返しOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。\![timerraiseother,0,1,Emily/Phase4.5,OnRoastedPotate]ここで繰り返し通知をキャンセル。
```
