# `\![change,ghost,ゴースト名(,--option=raise-event)]`

**カテゴリ:** 事件指令

切換至該 ghost。<br />
將 ghost 名稱設為 random，即可隨機切換（與 `\+` 相同）。<br />
設為 sequential，即可依序切換（與 `\_+` 相同）。<br />
執行後，若不存在相應的 ghost，則忽略。

將 ghost 名稱設為 lastinstalled，即可切換至最後安裝的 ghost。但若曾結束 SSP，則此設定無效。<br />
將 ghost 名稱設為 random，即可隨機切換。

SSP 2.4.74 之後，若在 ghost 名稱後加上 --option=raise-event，則會像從選單執行切換操作一樣，通知 [OnGhostChanging](../../shiori-event/boot-close-change/OnGhostChanging.md)。<br />
請注意，此時也可以透過 balloon break（通常為雙擊）中止操作。<br />
若未指定，則不會通知。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
Emily/Phase4.5に交代。\![change,ghost,Emily/Phase4.5]
```
