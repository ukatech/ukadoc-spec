# `\![timerraiseother,時間,繰り返すか否か,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件指令

指定等待時間（毫秒）後，向正在執行的其他 ghost 通知事件。<br />
「是否重複」指定為 0 時，事件會依指定時間重複發生；指定為 1 以上時，事件只會發生一次。<br />
第 6 個引數以後為 reference。<br />
不同名稱的事件可以分別執行，但若對同名事件重複執行，先前的設定會被覆寫。<br />
執行事件名稱相同、時間為 0 的 Sakura Script，即可取消計時器。<br />
將 ghost 名稱指定為 \_\_SYSTEM_ALL_GHOST\_\_，即可通知所有正在執行的 ghost。<br />
可使用位元組值 1 作為分隔符，指定多個 ghost 名稱。

**対応:** SSP

## 記述例

```sakurascript
\![timerraiseother,30000,0,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5に30秒(30000ミリ秒)おきに繰り返しOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。\![timerraiseother,0,1,Emily/Phase4.5,OnRoastedPotate]ここで繰り返し通知をキャンセル。
```
