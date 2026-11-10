# `\![set,othersurfacechange,trueかfalse]`

**カテゴリ:** 事件命令

設定是否通知[OnOtherSurfaceChange](../../shiori-event/surface/OnOtherSurfaceChange.md)。初始值為false。<br />
設為true後即啟用，同時啟動的其他ghost變更surface時，便會通知OnOtherSurfaceChange。

**対応:** SSP / Ninix

## 記述例

```sakurascript
							\![set,othersurfacechange,true]これ以降、同時に起動しているゴーストのサーフェスが変わるたびに、OnOtherSurfaceChangeが通知されるようになる。
```
