# `\![timernotify,時間,繰り返すか否か,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件命令

与 timerraise 相同，区别仅在于，即使此通知事件返回了某个值，该值也不会应用到 SSP。

**対応:** SSP

## 記述例

```sakurascript
\![notify,OnNotifyTest,test]OnNotifyTestが通知され、Reference0に「test」が入っている。OnNotifyTestでトークを書いてもSSPに反映されない。
```
