# `\![set,othersurfacechange,trueかfalse]`

**カテゴリ:** Event command

Sets whether to send the [OnOtherSurfaceChange](../../shiori-event/surface/OnOtherSurfaceChange.md) notification. The default is false.<br />
When set to true, OnOtherSurfaceChange is sent whenever the surface of another concurrently running ghost changes.

**対応:** SSP / Ninix

## 記述例

```sakurascript
							\![set,othersurfacechange,true]これ以降、同時に起動しているゴーストのサーフェスが変わるたびに、OnOtherSurfaceChangeが通知されるようになる。
```
