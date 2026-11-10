# `\![change,shell,シェル名(,--option=raise-event)]`

**カテゴリ:** 事件指令

切換至該 shell。<br />
若不存在相應的 shell，則忽略。<br />
切換後會通知 SHIORI 事件 [OnShellChanged](../../shiori-event/boot-close-change/OnShellChanged.md)。

將 shell 名稱設為 lastinstalled，即可切換至最後安裝的 ghost。但若曾結束 SSP，則此設定無效。<br />
將 shell 名稱設為 random，即可隨機切換。

SSP 2.4.74 之後，若在 shell 名稱後加上 --option=raise-event，則會像從選單執行切換操作一樣，通知 [OnShellChanging](../../shiori-event/boot-close-change/OnShellChanging.md)。<br />
請注意，此時也可以透過 balloon break（通常為雙擊）中止操作。<br />
若未指定，則不會通知。

**対応:** SSP / CROW / Ninix

## 記述例

```sakurascript
masterシェルに切り替え。\![change,shell,master]
```
