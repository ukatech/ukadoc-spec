# `\![timerraiseother,時間,繰り返すか否か,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件命令

指定等待时间（毫秒），向正在运行的其他ghost通知事件。<br />
“是否重复”为0时，每隔指定时间重复触发事件；为1以上时，只触发一次事件。<br />
第6个参数及之后的参数为reference。<br />
不同名称的事件可以分别执行，但对同名事件重复执行时会覆盖之前的设置。<br />
执行事件名相同且时间为0的Sakura Script即可取消。<br />
将ghost名设为\_\_SYSTEM_ALL_GHOST\_\_时，向所有正在运行的ghost发送通知。<br />
可以指定多个ghost名，以字节值1分隔。<br />
\[SSP 2.9.35\] 也可以指定正在运行的ghost的[UUID](../../propertysystem/property-system/general-property/uuid.md)来代替ghost名（与[raiseother](bang-raiseother-r0-r1-r2.md)相同）。目标不是在设置定时器时查找，而是在每次通知事件时查找。

**対応:** SSP

## 記述例

```sakurascript
\![timerraiseother,30000,0,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5に30秒(30000ミリ秒)おきに繰り返しOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。\![timerraiseother,0,1,Emily/Phase4.5,OnRoastedPotate]ここで繰り返し通知をキャンセル。
```
