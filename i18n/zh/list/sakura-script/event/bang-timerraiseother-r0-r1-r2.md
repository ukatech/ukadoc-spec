# `\![timerraiseother,時間,繰り返すか否か,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件命令

指定等待时间（毫秒）后，向其他正在运行的ghost发送事件通知。<br />
「是否重复」指定为0时，每隔指定时间重复触发事件；指定为1以上时，只触发一次。<br />
第6个及之后的参数为reference。<br />
不同名称的事件可以分别执行，但对同名事件重复执行时会被覆盖。<br />
执行同一事件名且时间为0的Sakura Script即可取消。<br />
ghost名称指定为\_\_SYSTEM_ALL_GHOST\_\_时，会向所有正在运行的ghost发送通知。<br />
ghost名称可以用字节值1作为分隔符指定多个名称。

**対応:** SSP

## 記述例

```sakurascript
\![timerraiseother,30000,0,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5に30秒(30000ミリ秒)おきに繰り返しOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。\![timerraiseother,0,1,Emily/Phase4.5,OnRoastedPotate]ここで繰り返し通知をキャンセル。
```
