# `\![set,othersurfacechange,trueかfalse]`

**カテゴリ:** イベントコマンド

[OnOtherSurfaceChange](../../shiori-event/surface/OnOtherSurfaceChange.md)を通知するかどうかを設定。初期値false。<br />
trueで有効になり、同時起動している他ゴーストのサーフェスが変わるとOnOtherSurfaceChangeが通知されるようになる。

**対応:** SSP / Ninix

## 記述例

```sakurascript
							\![set,othersurfacechange,true]これ以降、同時に起動しているゴーストのサーフェスが変わるたびに、OnOtherSurfaceChangeが通知されるようになる。
```
