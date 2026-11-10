# `\![notifyother,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件指令

與 raiseother 相同，唯一差異是即使此通知事件傳回任何值，也不會反映到 SSP。

**対応:** SSP

## 記述例

```sakurascript
\![notifyother,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5にOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。もしこの通知イベントでEmily/Phase4.5が何かトークをしても、バルーンには何も表示されない。
```
