# `\![timerraiseother,時間,繰り返すか否か,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件指令

指定等待時間（毫秒），向其他正在執行的 ghost 通知事件。<br />
「是否重複」指定為 0 時，每隔指定時間重複觸發事件；指定為 1 以上時，只觸發一次事件。<br />
第 6 個引數以後為 reference。<br />
不同名稱的事件可分別執行，但對同名事件重複執行時會覆寫先前的設定。<br />
執行事件名稱相同且時間為 0 的 Sakura Script 即可取消。<br />
將 ghost 名稱設為 \_\_SYSTEM_ALL_GHOST\_\_ 時，會通知所有正在執行的 ghost。<br />
可用位元組值 1 分隔，指定多個 ghost 名稱。<br />
\[SSP 2.9.35\] 除了 ghost 名稱，也可以指定正在執行的 ghost 的 [UUID](../../propertysystem/property-system/general-property/uuid.md)（與 [raiseother](bang-raiseother-r0-r1-r2.md) 相同）。目的對象是在每次通知事件時查找，而非設定計時器時查找。

**対応:** SSP

## 記述例

```sakurascript
\![timerraiseother,30000,0,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5に30秒(30000ミリ秒)おきに繰り返しOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。\![timerraiseother,0,1,Emily/Phase4.5,OnRoastedPotate]ここで繰り返し通知をキャンセル。
```
