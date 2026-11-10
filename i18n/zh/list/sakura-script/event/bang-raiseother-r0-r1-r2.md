# `\![raiseother,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

Notifies another running ghost of an event.<br />
The fourth and subsequent arguments are references.<br />
Setting the ghost name to “\_\_SYSTEM_ALL_GHOST\_\_” notifies all running ghosts.<br />
Only direct ghost names can be specified; multiple names can be specified, separated by byte value 1.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![raiseother,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5にOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。
```
