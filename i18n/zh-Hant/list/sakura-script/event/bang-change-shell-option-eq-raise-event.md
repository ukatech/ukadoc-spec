# `\![change,shell,シェル名(,--option=raise-event)]`

**カテゴリ:** 事件指令

切換至指定的 shell。<br />
若找不到對應的 shell，則忽略此指令。<br />
變更後會通知 SHIORI 事件 [OnShellChanged](../../shiori-event/boot-close-change/OnShellChanged.md)。

將 shell 名稱設為 lastinstalled 時，切換至最後安裝的 ghost。但若 SSP 已經結束過一次，則無效。<br />
將 shell 名稱設為 random 時，隨機切換。

\[SSP 2.9.35\] 也可指定 shell 的 [UUID](../../propertysystem/property-system/general-property/uuid.md) 代替 shell 名稱。

從 SSP 2.4.74 起，在 shell 名稱後加上 --option=raise-event 時，會通知 [OnShellChanging](../../shiori-event/boot-close-change/OnShellChanging.md)，與從選單執行切換操作相同。<br />
請注意，此時也可透過 balloon break（通常為連按兩下）中止操作。<br />
未指定時則不會通知。

**対応:** SSP / CROW / Ninix

## 記述例

```sakurascript
masterシェルに切り替え。\![change,shell,master]
```
