# `\![set,othersurfacechange,trueかfalse]`

**カテゴリ:** Event command

Set whether to send notifications for [OnOtherSurfaceChange](../../shiori-event/surface/OnOtherSurfaceChange.md). The default is false.<br />
When set to true, notifications for OnOtherSurfaceChange are sent whenever the surface of another concurrently running ghost changes.

**対応:** SSP / Ninix

## 記述例

```sakurascript
							\![set,othersurfacechange,true]これ以降、同時に起動しているゴーストのサーフェスが変わるたびに、OnOtherSurfaceChangeが通知されるようになる。
```
