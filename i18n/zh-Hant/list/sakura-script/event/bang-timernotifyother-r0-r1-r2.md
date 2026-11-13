# `\![timernotifyother,時間,繰り返すか否か,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件指令

與 timerraiseother 相同，唯一的差異是即使此通知事件回傳了值，也不會反映至 SSP。同樣可以用 UUID 代替 ghost 名稱。

**対応:** SSP

## 記述例

```sakurascript
\![notifyother,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5にOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。もしこの通知イベントでEmily/Phase4.5が何かトークをしても、バルーンには何も表示されない。
```
