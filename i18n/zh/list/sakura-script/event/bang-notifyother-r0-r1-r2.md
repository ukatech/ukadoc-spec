# `\![notifyother,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件命令

与raiseother相同，区别仅在于，即使此通知事件返回了某个值，该值也不会反映到SSP中。

**対応:** SSP

## 記述例

```sakurascript
\![notifyother,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5にOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。もしこの通知イベントでEmily/Phase4.5が何かトークをしても、バルーンには何も表示されない。
```
