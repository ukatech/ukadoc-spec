# `\![notify,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

As with raise, the only difference is that even if this notification event returns a value, it is not reflected in SSP.

**対応:** SSP

## 記述例

```sakurascript
\![notify,OnNotifyTest,test]OnNotifyTestが通知され、Reference0に「test」が入っている。OnNotifyTestでトークを書いてもSSPに反映されない。
```
