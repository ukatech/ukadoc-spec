# `\![get,property,イベント名,プロパティ名,プロパティ名,...]`

**カテゴリ:** 属性系统操作命令

获取属性系统的值。<br />
指定的事件会发生，属性系统的值会依次放入其 reference0 及后续 reference 中。<br />
※属性系统的详情请参阅[属性系统](../../propertysystem/index.md)页面。

**対応:** SSP / CROW

## 記述例

```sakurascript
このスクリプトの再生後、SHIORIイベント「SSPからバルーン情報取得」が通知される。Reference0に現在使用中のバルーンの、本体側の表示可能な幅(ピクセル数)、Reference1にその高さが入っている。\![get,property,SSPからバルーン情報取得,currentghost.balloon.scope(0).validwidth.initial,currentghost.balloon.scope(0).validheight.initial]
```
