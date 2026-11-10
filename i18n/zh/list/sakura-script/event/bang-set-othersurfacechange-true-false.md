# `\![set,othersurfacechange,trueかfalse]`

**カテゴリ:** 事件命令

设置是否通知 [OnOtherSurfaceChange](../../shiori-event/surface/OnOtherSurfaceChange.md)。初始值为 false。<br />
设为 true 后启用；同时运行的其他 ghost 的 surface 发生变化时，就会收到 OnOtherSurfaceChange 通知。

**対応:** SSP / Ninix

## 記述例

```sakurascript
							\![set,othersurfacechange,true]これ以降、同時に起動しているゴーストのサーフェスが変わるたびに、OnOtherSurfaceChangeが通知されるようになる。
```
