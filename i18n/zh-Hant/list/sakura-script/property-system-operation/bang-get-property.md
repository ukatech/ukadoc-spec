# `\![get,property,イベント名,プロパティ名,プロパティ名,...]`

**カテゴリ:** Property system operation command

Retrieves values from the property system.<br />
The event specified by the event name occurs, and the property system values are placed one by one in reference0 and subsequent references.<br />
※For details about the property system, see the [property system](../../propertysystem/index.md) page.

**対応:** SSP / CROW

## 記述例

```sakurascript
このスクリプトの再生後、SHIORIイベント「SSPからバルーン情報取得」が通知される。Reference0に現在使用中のバルーンの、本体側の表示可能な幅(ピクセル数)、Reference1にその高さが入っている。\![get,property,SSPからバルーン情報取得,currentghost.balloon.scope(0).validwidth.initial,currentghost.balloon.scope(0).validheight.initial]
```
