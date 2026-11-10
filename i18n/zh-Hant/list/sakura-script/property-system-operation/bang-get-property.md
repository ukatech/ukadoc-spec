# `\![get,property,イベント名,プロパティ名,プロパティ名,...]`

**カテゴリ:** 屬性系統操作命令

取得屬性系統的值。<br />
會觸發指定的事件，並依序將屬性系統的值放入該事件的 Reference0 及後續項目。<br />
※屬性系統的詳細資訊請參閱[屬性系統](../../propertysystem/index.md)頁面。

**対応:** SSP / CROW

## 記述例

```sakurascript
このスクリプトの再生後、SHIORIイベント「SSPからバルーン情報取得」が通知される。Reference0に現在使用中のバルーンの、本体側の表示可能な幅(ピクセル数)、Reference1にその高さが入っている。\![get,property,SSPからバルーン情報取得,currentghost.balloon.scope(0).validwidth.initial,currentghost.balloon.scope(0).validheight.initial]
```
