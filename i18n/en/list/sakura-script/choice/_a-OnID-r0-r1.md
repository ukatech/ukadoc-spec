# `\_a[OnID,r0,r1...]`

**カテゴリ:** Choice command

The range up to `\_a` becomes an anchor. The choice does not time out, but the balloon times out as it does during normal talk.<br />
As above, if the ID starts with "On", clicking the anchor starts the SHIORI event OnID (the event as written).<br />
Arguments following the ID are stored in Reference0 and onward in order.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\_a[OnHint,0]ヒント\_aが欲しいならクリックしよう。\_a[OnHint,1]ほらほら早く\_a。この2つのアンカーは、クリックするとSHIORIイベントOnHintが通知されるが、クリックしたものによってReference0の値が「0」か「1」に変わる。
```
