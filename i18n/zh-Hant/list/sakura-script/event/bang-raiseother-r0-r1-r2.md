# `\![raiseother,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件指令

通知正在執行的其他 ghost 事件。<br />
第 4 個引數起為 reference。<br />
若 ghost 名稱設為「\_\_SYSTEM_ALL_GHOST\_\_」，則會通知所有正在執行的 ghost。<br />
只能直接指定 ghost 名稱；可用位元組值 1 作為分隔符指定多個名稱。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![raiseother,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5にOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。
```
