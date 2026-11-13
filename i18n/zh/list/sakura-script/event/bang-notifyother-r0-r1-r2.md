# `\![notifyother,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件命令

与 raiseother 相同，唯一区别是此通知事件即使返回值，也不会反映到 SSP 中。同样可以指定 UUID 来代替 ghost 名称。

**対応:** SSP

## 記述例

```sakurascript
\![notifyother,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5にOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。もしこの通知イベントでEmily/Phase4.5が何かトークをしても、バルーンには何も表示されない。
```
