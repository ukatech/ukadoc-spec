# `\![notify,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件命令

与 raise 相同，唯一的区别是，即使此通知事件返回某个值，也不会反映到 SSP。

**対応:** SSP

## 記述例

```sakurascript
\![notify,OnNotifyTest,test]OnNotifyTestが通知され、Reference0に「test」が入っている。OnNotifyTestでトークを書いてもSSPに反映されない。
```
