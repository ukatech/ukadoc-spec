# `\![notifyother,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

Like raiseother, the only difference is that values returned by this notification event are not applied by SSP.

**対応:** SSP

## 記述例

```sakurascript
\![notifyother,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5にOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。もしこの通知イベントでEmily/Phase4.5が何かトークをしても、バルーンには何も表示されない。
```
