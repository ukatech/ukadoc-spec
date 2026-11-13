# `\![change,ghost,ゴースト名(,--option=raise-event)]`

**カテゴリ:** 事件指令

切換至指定的 ghost。<br />
將 ghost 名稱設為 random 時，隨機切換（與 `\+` 相同）。<br />
設為 sequential 時，依序切換（與 `\_+` 相同）。<br />
執行時若找不到對應的 ghost，則忽略此指令。

將 ghost 名稱設為 lastinstalled 時，切換至最後安裝的 ghost。但若 SSP 已經結束過一次，則無效。<br />
將 ghost 名稱設為 random 時，隨機切換。

\[SSP 2.9.35\] 也可指定 ghost 的 [UUID](../../propertysystem/property-system/general-property/uuid.md) 代替 ghost 名稱（避免混淆同名的 ghost）。

從 SSP 2.4.74 起，在 ghost 名稱後加上 --option=raise-event 時，會通知 [OnGhostChanging](../../shiori-event/boot-close-change/OnGhostChanging.md)，與從選單執行切換操作相同。<br />
請注意，此時也可透過 balloon break（通常為連按兩下）中止操作。<br />
未指定時則不會通知。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
Emily/Phase4.5に交代。\![change,ghost,Emily/Phase4.5]
```
