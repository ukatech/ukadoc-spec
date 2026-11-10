# `\![timernotify,時間,繰り返すか否か,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件指令

與 timerraise 相同，差異僅在於即使此通知事件傳回任何值，也不會反映至 SSP。

**対応:** SSP

## 記述例

```sakurascript
\![notify,OnNotifyTest,test]OnNotifyTestが通知され、Reference0に「test」が入っている。OnNotifyTestでトークを書いてもSSPに反映されない。
```
