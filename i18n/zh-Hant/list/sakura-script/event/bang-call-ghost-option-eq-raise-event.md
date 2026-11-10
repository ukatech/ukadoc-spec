# `\![call,ghost,ghost 名稱(,--option=raise-event)]`

**カテゴリ:** 事件命令

呼叫指定 ghost 名稱的 ghost。<br />
將 ghost 名稱設為 lastinstalled 時，會呼叫最後安裝的 ghost。<br />
將 ghost 名稱設為 random 時，會隨機呼叫 ghost。

在 SSP 2.4.74 及之後的版本中，於 ghost 名稱後加上 --option=raise-event 時，會像透過選單執行切換操作一樣，收到[OnGhostCalling](../../shiori-event/boot-close-change/OnGhostCalling.md)通知。<br />
未指定時則不會收到通知。

**対応:** SSP / Ninix

## 記述例

```sakurascript
Emily/Phase4.5を呼び出す。\![call,ghost,Emily/Phase4.5]
```
