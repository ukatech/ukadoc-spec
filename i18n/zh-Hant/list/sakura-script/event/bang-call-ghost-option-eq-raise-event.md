# `\![call,ghost,ゴースト名(,--option=raise-event)]`

**カテゴリ:** 事件指令

呼叫由 ghost 名稱指定的 ghost。<br />
將 ghost 名稱設為 lastinstalled 時，呼叫最後安裝的 ghost。<br />
將 ghost 名稱設為 random 時，隨機呼叫。<br />
\[SSP 2.9.35\] 也可指定 ghost 的 [UUID](../../propertysystem/property-system/general-property/uuid.md) 代替 ghost 名稱（避免混淆同名的 ghost）。

從 SSP 2.4.74 起，在 ghost 名稱後加上 --option=raise-event 時，會通知 [OnGhostCalling](../../shiori-event/boot-close-change/OnGhostCalling.md)，與從選單執行切換操作相同。<br />
未指定時則不會通知。

**対応:** SSP / Ninix

## 記述例

```sakurascript
Emily/Phase4.5を呼び出す。\![call,ghost,Emily/Phase4.5]
```
