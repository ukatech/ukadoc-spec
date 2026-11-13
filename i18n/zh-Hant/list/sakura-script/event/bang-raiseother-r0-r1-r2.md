# `\![raiseother,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件指令

向其他正在執行的 ghost 通知事件。<br />
第 4 個參數起為 reference。<br />
將 ghost 名稱設為「\_\_SYSTEM_ALL_GHOST\_\_」時，通知所有正在執行的 ghost。<br />
ghost 名稱只能直接指定，可用位元組值 1 分隔以指定多個名稱。<br />
\[SSP 2.9.35\] 也可指定正在執行的 ghost 的 [UUID](../../propertysystem/property-system/general-property/uuid.md) 代替 ghost 名稱。若有多個相同 UUID 的 ghost 正在執行，則通知顯示中的 ghost；若沒有，則通知執行中的 ghost 清單中排在第一個的 ghost。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![raiseother,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5にOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。
```
