# `\_a[OnID,r0,r1...]`

**カテゴリ:** Choice command

The range up to `\_a` is treated as an anchor. Choices do not time out, but the balloon times out as with normal talk.<br />
As above, if the ID starts with "On", clicking it triggers the SHIORI event OnID (the event as written).<br />
The arguments following the ID are stored in Reference0 and later references, in order.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\_a[OnHint,0]ヒント\_aが欲しいならクリックしよう。\_a[OnHint,1]ほらほら早く\_a。この2つのアンカーは、クリックするとSHIORIイベントOnHintが通知されるが、クリックしたものによってReference0の値が「0」か「1」に変わる。
```
