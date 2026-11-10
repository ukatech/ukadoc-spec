# `\![notify,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

Same as raise, except that any value returned by this notification event is not reflected in SSP.

**対応:** SSP

## 記述例

```sakurascript
\![notify,OnNotifyTest,test]OnNotifyTestが通知され、Reference0に「test」が入っている。OnNotifyTestでトークを書いてもSSPに反映されない。
```
