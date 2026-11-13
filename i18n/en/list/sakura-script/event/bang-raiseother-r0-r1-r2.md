# `\![raiseother,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** Event commands

Notifies another running ghost of an event.<br />
The fourth and subsequent arguments are references.<br />
Set the ghost name to "\_\_SYSTEM_ALL_GHOST\_\_" to notify all running ghosts.<br />
Ghost names must be specified directly; multiple names can be separated by byte value 1.<br />
\[SSP 2.9.35\] The [UUID](../../propertysystem/property-system/general-property/uuid.md) of a running ghost can also be specified instead of its name. If multiple ghosts with the same UUID are running, the visible ghost is notified; if none is visible, the first ghost in the running-ghost list is notified.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![raiseother,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5にOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。
```
