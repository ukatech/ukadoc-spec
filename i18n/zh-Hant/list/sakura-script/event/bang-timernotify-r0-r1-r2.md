# `\![timernotify,時間,繰り返すか否か,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

It is the same as timerraise, except that any value returned by this notification event is not applied to SSP.

**対応:** SSP

## 記述例

```sakurascript
\![notify,OnNotifyTest,test]OnNotifyTestが通知され、Reference0に「test」が入っている。OnNotifyTestでトークを書いてもSSPに反映されない。
```
