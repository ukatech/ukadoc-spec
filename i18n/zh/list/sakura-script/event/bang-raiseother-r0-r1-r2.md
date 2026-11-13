# `\![raiseother,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件命令

向运行中的其他 ghost 通知事件。<br />
第 4 个及之后的参数为 reference。<br />
将 ghost 名称设为“\_\_SYSTEM_ALL_GHOST\_\_”时，向所有运行中的 ghost 通知。<br />
ghost 名称只能直接指定，可以用字节值 1 分隔来指定多个名称。<br />
\[SSP 2.9.35\] 也可以指定运行中的 ghost 的 [UUID](../../propertysystem/property-system/general-property/uuid.md) 来代替 ghost 名称。如果多个相同 UUID 的 ghost 正在运行，则通知正在显示的 ghost；如果没有，则通知运行中的 ghost 列表中的第一个。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![raiseother,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5にOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。
```
