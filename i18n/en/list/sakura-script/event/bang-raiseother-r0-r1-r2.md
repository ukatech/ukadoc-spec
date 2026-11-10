# `\![raiseother,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

Notify other running ghosts of an event.<br />
The fourth and subsequent arguments are references.<br />
If the ghost name is "\_\_SYSTEM_ALL_GHOST\_\_", the event is sent to all running ghosts.<br />
Ghost names can only be specified directly; multiple names can be specified separated by byte value 1.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![raiseother,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5にOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。
```
